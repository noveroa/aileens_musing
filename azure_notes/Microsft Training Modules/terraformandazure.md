# some note on terraform adb azure

* multiple providers 
    | provider | details |
    | ----- | ----- |
    | azurerm    | This provider is the most user friendly way to deploy resources into Azure. This provider may take time to support new Azure features. | 
    | azapi    | This provider enables deployment of any Azure resource, including resources in preview. It's always up to date with the latest Azure features. | 
    | azuread    | This provider is used to managed Microsoft Entra ID. It can manage many features, including user, groups, and service principals. | 
    | azuredevops    | This provider is used to manage all aspects of Azure DevOps, including repos, pipelines, and projects. | 
    | github    | This provider is used to manage all aspects of GitHub, including organizations, repositories, and actions. | 

* azure verified modules 
    * (azure verified modules)[https://azure.github.io/Azure-Verified-Modules/]
    * (terraform registry for azure)[https://registry.terraform.io/providers/hashicorp/azurerm/latest]

* example 
    ```sh
    variable "name_prefix" {
    type    = string
    default = "storage"
    }

    locals {
    storage_account_name             = "${var.name_prefix}${random_id.random_suffix.hex}"
    storage_account_replication_type = "RAGRS"
    }

    resource "random_id" "random_suffix" {
        byte_length = 4
    }

    resource "azurerm_resource_group" "example" {
    name     = "storage-resource-group"
    location = "eastus"
    }

    resource "azurerm_storage_account" "example" {
    name                      = local.storage_account_name
    location                  = azurerm_resource_group.example.location
    resource_group_name       = azurerm_resource_group.example.name
    sku                       = "Standard"
    account_replication_type  = local.storage_account_replication_type
    account_kind              = "StorageV2"
    access_tier               = "Hot"
    enable_https_traffic_only = true
    }

    output "storage_account_resource_id" {
    value = azurerm_storage_account.example.id
    }
    ```