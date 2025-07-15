
### Azure Resource Manager 
> [ARM remplates](]https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview)

> Azure Resource Manager (ARM) is the deployment and management service for Azure resources. It provides a consistent way to deploy, manage, and organize your Azure resources using a declarative approach, often through ARM templates, which are JSON files defining the infrastructure. 
 azures terraform?

_NOTE BICEP  Bicep that offers the same capabilities as ARM templates but with a syntax that's easier to use. Each Bicep file is automatically converted to an ARM template during deployment_

```sh
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "location": {
      "type": "string",
      "defaultValue": "[resourceGroup().location]"
    }
  },
  "resources": {
    "mystore": {
      "type": "Microsoft.Storage/storageAccounts",
      "apiVersion": "2023-04-01",
      "name": "mystorageaccount",
      "location": "[parameters('location')]",
      "sku": {
        "name": "Standard_LRS"
      },
      "kind": "StorageV2"
    }
  }
}```

# Deploy Azure VM using Arm templates

### Create resource group if it does not exist 

```sh
az group create --name vscode --location 'Central US'

### Create virtual machine
az deployment group create --resource-group vscode --template-file 01-create-vm.json
```