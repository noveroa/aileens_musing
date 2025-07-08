#!/bin/bash 
set -exo pipefail

PS4='+ \t ${BASH_SOURCE##*/}:${LINENO} '
export PS4

STIME=$SECONDS
export STIME

SCRIPT_DIR=$(cd "$(dirname "$0")" ; pwd -P)
# shellcheck source=util.sh
source "$SCRIPT_DIR/util.sh"

ROOT_DIR=$(cd "${SCRIPT_DIR}/../.." && pwd -P)
PAAC_CONFIG_DIR="${PAAC_CONFIG_DIR:-${ROOT_DIR}/config/configurations}"
PAAC_SCRATCH_DIR="${PAAC_SCRATCH_DIR:-${ROOT_DIR}/scratch}"
PAAC_TERRAFORM_SHARED="${PAAC_SCRATCH_DIR}/terraform"

PAAC_DOCKER_ROOT='/var/paac'
export PAAC_DOCKER_ROOT

export PAAC_CONFIG_DIR
export PAAC_TERRAFORM_SHARED

# we need an array, so PAAC_LEVELS_TO_DEPLOY=${PAAC_LEVELS_TO_DEPLOY:-(foo bar)} doesn't seem to work
if [ -n "$PAAC_LEVELS_TO_DEPLOY" ] ; then 
  read -r -a PAAC_LEVELS_TO_DEPLOY <<< "$PAAC_LEVELS_TO_DEPLOY"
else
  PAAC_LEVELS_TO_DEPLOY=(core system platform)
fi

log "Will be deploying these levels"
log "$(printf '%s\n' "${PAAC_LEVELS_TO_DEPLOY[@]}")"


export PAAC_LEVELS_TO_DEPLOY

AWS_PAGER='' 
export AWS_PAGER

# if detected to be run inside of tmux session, we will display progress in a
# split-window manner
if [ -n "$TMUX" ]; then
  # shellcheck source=piper.sh
  source "$SCRIPT_DIR/piper.sh"
else 
  LOG_PIPE=''
  export LOG_PIPE
fi

log "main"
log "init"

if ! (ls "$PAAC_CONFIG_DIR" > /dev/null 2>&1) then
  echo "Config directory ($PAAC_CONFIG_DIR) is missing in repo's root"
  exit 1
fi

if [ -z "$AWS_PROFILE" ]; then
  AWS_PROFILE="zze"
  AWS_ADM_PROFILE="zzb"
fi

AWS_REGION="${AWS_REGION:-us-east-1}"
export AWS_DEFAULT_REGION="$AWS_REGION"

# We check operation success manually now by finding if there are broken instances after operation completes
MAX_CONCURRENT_CFN=${MAX_CONCURRENT_CFN:-500}
export MAX_CONCURRENT_CFN

# > You mentioned that you have 500 accounts and deployments to 3 regions in each account. If you are provisioning a stack set via the "us-east-1" to 3 regions, it will contribute to 1500 active instances.
# Our current limit is 5000 => Floor(5000/1500) = 3.
# Ideally we should limit only to 3 parallel executions of stack sets targeting the root OU, but for now this is quick and working
MAX_CONCURRENT_DEPLOYMENTS=${MAX_CONCURRENT_DEPLOYMENTS:-3}
export MAX_CONCURRENT_DEPLOYMENTS

if [ -z "$PAAC_ENV" ]; then
  if [ "$AWS_PROFILE" == 'zze' ]; then
    PAAC_ENV='dev'
  else
    PAAC_ENV='prod'
  fi
fi

export PAAC_ENV

export AWS_PROFILE
export AWS_REGION
export AWS_ADM_PROFILE

PAAC_AF_ROOT="${PAAC_AF_ROOT:-${PAAC_SCRATCH_DIR}/artefacts}"
PAAC_JOBS_ROOT="${PAAC_JOBS_ROOT:-${PAAC_SCRATCH_DIR}/jobs}"
PAAC_BATCH_AF_ROOT="${PAAC_BATCH_AF_ROOT:-${PAAC_SCRATCH_DIR}/batch}"

PAAC_RESUME=${PAAC_RESUME:-$1}
PAAC_RESUME="${PAAC_RESUME:-'fresh'}"
export PAAC_RESUME

if [ "$PAAC_RESUME" == 'resume' ]; then
  PAAC_AF_PREFIX="${PAAC_AF_PREFIX:-$2}"
  if [ -z "$PAAC_AF_PREFIX" ]; then
     PAAC_AF_PREFIX=$(find "$PAAC_JOBS_ROOT" -type d -depth 1 -exec basename '{}' ';' | sort -r | head -n 1)
  fi

  if [ -z "$PAAC_AF_PREFIX" ]; then
    echo "Unable to find a deployment to resume under ${PAAC_JOBS_ROOT}"
    exit 1
  fi

  if [ ! -d "${PAAC_JOBS_ROOT}/${PAAC_AF_PREFIX}" ]; then
    echo "Unable to resume - ${PAAC_JOBS_ROOT}/${PAAC_AF_PREFIX} doesn't happen to be a directory"
    exit 1
  fi

else
  PAAC_AF_PREFIX="${PAAC_AF_PREFIX:-$(date -u +"%Y%m%d-%H%M%S")}"
  mkdir -p "${PAAC_AF_ROOT}/$PAAC_AF_PREFIX"

  mkdir -p "${PAAC_JOBS_ROOT}/$PAAC_AF_PREFIX"

  mkdir -p "${PAAC_BATCH_AF_ROOT}/$PAAC_AF_PREFIX"
fi


PAAC_AF_PATH=$(cd "${PAAC_AF_ROOT}/${PAAC_AF_PREFIX}" && pwd)
PAAC_JOBS_PATH=$(cd "${PAAC_JOBS_ROOT}/${PAAC_AF_PREFIX}" && pwd)
PAAC_JOBS_LISTS_PATH=$(cd "${PAAC_BATCH_AF_ROOT}/${PAAC_AF_PREFIX}" && pwd)

export PAAC_AF_PATH
export PAAC_JOBS_PATH
export PAAC_AF_PREFIX
export PAAC_JOBS_LISTS_PATH

PAAC_AF_BUCKETS=$(aws --profile "$AWS_ADM_PROFILE" s3api list-buckets | jq -r '.Buckets[] | select(.Name | contains("paac-artefacts")) | .Name')
export PAAC_AF_BUCKETS

PAAC_TF_STATE_BUCKET=$(aws --profile "$AWS_PROFILE" s3api list-buckets | jq -r '[.Buckets[] | select(.Name | contains("paac-terraform-state")) | .Name] | .[0]')
export PAAC_TF_STATE_BUCKET

if [ -z "$BRANCH_NAME" ]; then
  BRANCH_NAME="$(git symbolic-ref --short HEAD)"
fi

BRANCH_NAME_FORMATTED="$(echo "$BRANCH_NAME" | tr -d '\n' | tr -C '[:alnum:]' '-')"
export BRANCH_NAME_FORMATTED