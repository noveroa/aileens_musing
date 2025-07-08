#!/usr/bin/env bash
set -euxo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" ; pwd -P)
ROOT_DIR="${SCRIPT_DIR}/../.."
PATH="$PATH:${ROOT_DIR}/node_modules/.bin/:$SCRIPT_DIR"

GENERATORS_PATH=$(cd "${SCRIPT_DIR}" && cd ../.. && pwd -P)

# shellcheck source=util.sh
source "$SCRIPT_DIR/util.sh"

source env_parallel.bash
echo "" > ~/.parallel/ignored_vars

PAAC_JOB_RETRIES=${PAAC_JOB_RETRIES:-5}

LEVEL="$1"

if [ -z "$LEVEL" ]; then
  error "You need to specify level (directory name) to deploy."
  exit 1
fi

STEP_COUNT=$(exec-tree "${LEVEL}" | jq -r 'length')
STEP_COUNT=$(( STEP_COUNT - 1 ))

LEVEL_NAME=$(basename "${LEVEL}")
log "${LEVEL_NAME}"

for step in $(seq 0 "$STEP_COUNT" ); do
  log "stage $step/$STEP_COUNT"

  PRETTY_FLAGS='--eta --bar'
  if [ -n "${BUILD_NUMBER:-''}" ]; then # jenkins
    PRETTY_FLAGS=''
  fi

  JOB_LIST="${LEVEL_NAME}-${step}.parallel.joblist"

  PAAC_SUBMIT_ALL_JOBS_AT_ONCE=${PAAC_SUBMIT_ALL_JOBS_AT_ONCE:-''}

  if [ -z "$PAAC_SUBMIT_ALL_JOBS_AT_ONCE" ]; then
    log "Scheduling individual jobs using GNU Parallel"

    set +e
    # parallel is very chatty
    set +x

    # if you want an orderly log use --keep-order instead of --ungroup
    # shellcheck disable=SC2086,SC2016 # we want PRETTY_FLAGS to expand as individual flags
    if ! env_parallel --arg-file "${JOB_LIST}" --retries "$PAAC_JOB_RETRIES" \
        --joblog "${LEVEL_NAME}-${step}.parallel.log" --keep-order \
        $PRETTY_FLAGS --jobs "$MAX_CONCURRENT_DEPLOYMENTS" --halt soon,fail=1 \
        --env _ "$SCRIPT_DIR/runners/dispatch.sh {} {%} 2>&1 | tee -a {}.log; exit \${PIPESTATUS[0]}"; then
        
      cat "${LEVEL_NAME}-${step}.parallel.log"
      error "Job failed (see above) - aborting deployment."
      set +x
      env_parallel --end-session

      exit 1
    fi
  fi
done
