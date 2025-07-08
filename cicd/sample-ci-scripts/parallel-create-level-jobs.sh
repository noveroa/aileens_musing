#!/usr/bin/env bash
set -exuo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" ; pwd -P)
ROOT_DIR="${SCRIPT_DIR}/../.."
PATH="$PATH:${ROOT_DIR}/node_modules/.bin/:$SCRIPT_DIR"
GENERATORS_PATH=$(cd "${SCRIPT_DIR}" && cd ../.. && pwd -P)

# shellcheck source=util.sh
source "$SCRIPT_DIR/util.sh"

source env_parallel.bash
echo "" > ~/.parallel/ignored_vars

LEVEL="$1"

if [ -z "$LEVEL" ]; then
  echo "You need to specify level (directory name) to deploy."
  exit 1
fi

LEVEL_NAME=$(basename "${LEVEL}")
log "${LEVEL_NAME}"

STEP_COUNT=$(exec-tree "${LEVEL}" | jq -r 'length')

if [ "$STEP_COUNT" = "0" ]; then
  echo "Exec tree is empty. Not good at all"
  exit 1
fi

STEP_COUNT=$(( STEP_COUNT - 1 ))

log "$(basename "${LEVEL}")"

PAAC_JOB_RETRIES=${PAAC_JOB_RETRIES:-5}

MAX_CONCURRENT_JOB_CREATIONS=${MAX_CONCURRENT_JOB_CREATIONS:-"$MAX_CONCURRENT_DEPLOYMENTS"}

for step in $(seq 0 "$STEP_COUNT" ); do
  log "stage $step/$STEP_COUNT"

  set +x
  set +e

  STEP_FMT=$(printf "%02d" "$step")

  JOB_LIST="${LEVEL_NAME}-${step}.parallel-create.joblist"

  exec-tree "${LEVEL}" \
    | jq -r --argjson idx "$step" '.[$idx] | .[] | [.file, .module, .region] | join(" ")' \
    > "$JOB_LIST"

  # if you want an orderly log use --keep-order instead of --ungroup
  if ! env_parallel --arg-file "${JOB_LIST}" --retries "$PAAC_JOB_RETRIES" --jobs "$MAX_CONCURRENT_JOB_CREATIONS" --halt now,fail=1 --ungroup --env _ --colsep ' ' "$SCRIPT_DIR"/create-jobs.sh "${LEVEL}" "${STEP_FMT}" '{1}' '{2}' '{3}'; then 
    exit 1;
  fi

  env_parallel --end-session

  cd "${PAAC_TERRAFORM_SHARED}"
  PRETTY_FLAGS='--eta --bar'
  if [ -n "${BUILD_NUMBER:-''}" ]; then # jenkins
    PRETTY_FLAGS=''
  fi

  FIND_PATH=${PAAC_JOBS_PATH}/${LEVEL_NAME}/${STEP_FMT}

  JOB_LIST_DEFAULT_SORT="${LEVEL_NAME}-${step}.parallel.joblist.defaultsort"
  JOB_LIST="${LEVEL_NAME}-${step}.parallel.joblist"

  find "${FIND_PATH}" -name 'job.sh' | sort > "$JOB_LIST_DEFAULT_SORT"
  if [[ $(wc -l < "${JOB_LIST_DEFAULT_SORT}") -eq 0 ]]; then
    log "No jobs were found in the expected location $FIND_PATH. This could be because jobs were not generated due to missing config files."
    exit 0
  fi

  # us-east-1 deployments should roll out first, with the most privileged accounts first within the region
  ORGS_ACCOUNT_ID=$( aws --profile "$AWS_PROFILE" sts get-caller-identity --query Account --output text )
  ADM_ACCOUNT_ID=$( aws --profile "$AWS_ADM_PROFILE" sts get-caller-identity --query Account --output text )
  
  rm -f "${JOB_LIST}"

  # grep ... || [[ $? == 1 ]] is a safety mechanism so the script doesn't fail when grep matches are not found
  # but pipefail if any other exit code is returned (in which case grep will stderr and provide more information)
  # collect stack sets first (no region in file name)
  grep -Ev "/us-east-1/|/us-west-1/|/eu-central-1/" "${JOB_LIST_DEFAULT_SORT}" >> "${JOB_LIST}" || [[ $? == 1 ]]
  # now collect jobs with a region defined in the file name
  for SORT_REGION in us-east-1 us-west-1 eu-central-1; do
    grep "/${SORT_REGION}/" "${JOB_LIST_DEFAULT_SORT}" > "${JOB_LIST_DEFAULT_SORT}.${SORT_REGION}" || [[ $? == 1 ]]
    {
      grep "/${ADM_ACCOUNT_ID}/" "${JOB_LIST_DEFAULT_SORT}.${SORT_REGION}" || [[ $? == 1 ]];
      grep "/${ORGS_ACCOUNT_ID}/" "${JOB_LIST_DEFAULT_SORT}.${SORT_REGION}" || [[ $? == 1 ]];
      grep -Ev "/(${ORGS_ACCOUNT_ID}|${ADM_ACCOUNT_ID})/" "${JOB_LIST_DEFAULT_SORT}.${SORT_REGION}" || [[ $? == 1 ]];
    } >> "${JOB_LIST}"
  done

  # sanity checks
  if [[ $(wc -l < "${JOB_LIST_DEFAULT_SORT}") -ne $(wc -l < "${JOB_LIST}") ]]; then
    error "Jobs did not group and sort as expected."
    echo "Before sort"
    cat "${JOB_LIST_DEFAULT_SORT}"
    echo "--------------------------"
    echo "After sort"
    cat "$JOB_LIST"
    error "Jobs did not group and sort as expected (see above)"
    exit 1
  fi

  log "Saving individual jobs from ${JOB_LIST} to deploy with AWS Batch"
  AWS_BATCH_JOBS_LIST_PREFIX="${LEVEL_NAME}-step-${step}-part-"
  TEMP_LIST="${JOB_LIST}_temp"

  while read -r JOB; do
    JOB=$(echo "${JOB}" | sed "s#${PAAC_JOBS_PATH}#${PAAC_DOCKER_ROOT}/scratch/jobs/${PAAC_AF_PREFIX}#g")
    echo "${JOB}" >> "${TEMP_LIST}"
  done < "${JOB_LIST}"

  split -a 2 -d -l 1000 "${TEMP_LIST}" "${PAAC_JOBS_LISTS_PATH}/${AWS_BATCH_JOBS_LIST_PREFIX}"
  rm -f "${TEMP_LIST}"
done

# sleep 5