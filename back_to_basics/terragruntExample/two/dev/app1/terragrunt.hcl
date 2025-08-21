#  include this in each of your unit terragrunt.hcl files using the include block for each infrastructure module you need to deploy:

include "root" {
  path = find_in_parent_folders("root.hcl")
}