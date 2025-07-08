#!/usr/bin/env bash 

set -exo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" ; pwd -P)"

# shellcheck source=util.sh
source "$SCRIPT_DIR/util.sh"


WORK_DIR="$1"

cd "${WORK_DIR}" 

# shellcheck disable=SC1091
source "${WORK_DIR}/job.env"

JOB_KEY=$(cat job.key.txt)
log "$JOB_KEY"

if [ -n "$PAAC_TERRRAFORM_REPLAN" ] || [ ! -f tf.plan ] || [ ! -f backend.tfvars ] || [ ! -d '.terraform' ] || [ ! -f tf.plan.json ] ; then

  # if we're in a container of sorts
  if [ -n "${PAAC_INSIDE_DOCKER:-}" ]; then

    echo "
bucket = \"${PAAC_TF_STATE_BUCKET}\"
key = \"${JOB_KEY}.tfstate\"
profile = \"backend\"
" > backend.tfvars

    AWS_SHARED_CREDENTIALS_FILE="$WORK_DIR/aws_credentials_docker"
    export AWS_SHARED_CREDENTIALS_FILE

    PAAC_TERRAFORM_SHARED="$PAAC_DOCKER_ROOT/scratch/terraform"
else

    echo "
bucket = \"${PAAC_TF_STATE_BUCKET}\"
key = \"${JOB_KEY}.tfstate\"
" > backend.tfvars

fi

  TF_PLUGIN_CACHE_DIR="${PAAC_TERRAFORM_SHARED}/.terraform/providers" terraform init -input=false -backend-config=backend.tfvars
  
  terraform plan -var-file job.tfvars -out tf.plan
  terraform show -json tf.plan > tf.plan.json
fi

function change_count() {
  jq -r '[ .resource_changes[] | select(.change.actions | contains(["no-op"]) | not) ] | length' tf.plan.json
}

function import_and_show() {
  # $1 - fail_on_import_error
  terraform state pull > autoimport-state.json

  # shellcheck disable=SC2016
  jq -r '.resource_changes[] | select(.change.actions | contains(["create"])) | [.address, .type, (.change.after | (.name // .bucket))] | @tsv' tf.plan.json \
  | parallel -t --jobs 1 --colsep '\t' terraform import -var-file job.tfvars '{1}' '$(arnsonist "{2}" "{3}" "${AWS_REGION}" "${PAAC_TARGET_ACCOUNT_ID}" "{1}")' || $1

  terraform plan -var-file job.tfvars -out tf.plan
  terraform show -json tf.plan > tf.plan.json
}

if [ "$( change_count )" -gt 0 ] ; then
  set +e

  if [ -n "$PAAC_TF_IMPORT_ONLY" ]; then
    log "Import only"
    import_and_show false

    if [ "$( change_count )" -ne 0 ] ; then
      log "Change count is > 0 after import, when PAAC_TF_IMPORT_ONLY was specified."
      exit 0
    fi
  else
    if ! terraform apply -auto-approve tf.plan ; then
      set -e

      if [ -n "$PAAC_TF_AUTO_IMPORT" ] && [ "$( change_count )" -ge 0 ] ; then
        log "Auto import"
        import_and_show true
        
        if [ "$( change_count )" -gt 0 ] ; then
          terraform apply -auto-approve tf.plan
        fi
      else
        exit 1
      fi
    fi
  fi

fi