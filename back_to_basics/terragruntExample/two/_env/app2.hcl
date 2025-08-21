locals {
  # Load the relevant env.hcl file based on where the including unit is.
  # This works because find_in_parent_folders always runs in the context of the unit.
  env_vars = read_terragrunt_config(find_in_parent_folders("env.hcl"))
  env_name = local.env_vars.locals.env

  source_base_url = "github.com/<org>/modules.git//app"
}

# dependency "vpc" {
#   config_path = "../vpc"
# }

# dependency "mysql" {
#   config_path = "../mysql"
# }

inputs = {
  env            = local.env_name
  basename       = "example-app-${local.env_name}"
}