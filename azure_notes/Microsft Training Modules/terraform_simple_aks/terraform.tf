
terraform {
  required_version = "~> 1.9"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.27"
    }
  }
}

provider "azurerm" {
  features {
    resource_group {
      prevent_deletion_if_contains_resources = false
    }
  }
  # Replace with your Azure subscription ID - SET IN ENVIRON VAR
  subscription_id = ""
  # Optional The Cloud Environment which should be used. Possible values are public, usgovernment, german, and china. Defaults to public. This can also be sourced from the ARM_ENVIRONMENT Environment Variable. Not used when metadata_host is specified.
  environment = "public"
  # Optional: 
  # ... 
}