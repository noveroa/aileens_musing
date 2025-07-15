
#!/bin/bash
# Simple Azure cli - create resource group and vm
#
# Usage: ./azure_cli.sh file
# -----------------------------------------------------------------------------

# for macOs:
# $ brew update && brew install azure-cli
# Note - installed 15Jul2025, had error "SyntaxWarning: invalid escape sequence '\ '"
# i just ran 
# $brew reinstall python

# ran az login to start session too .. 

export RANDOM_ID="$(openssl rand -hex 3)"
export MY_RESOURCE_GROUP_NAME="azure_cli_demo_$RANDOM_ID"
export REGION=EastUS
export MY_VM_NAME="azure_cli_demo_$RANDOM_ID"
export MY_USERNAME=azureuser
export MY_VM_IMAGE="Canonical:0001-com-ubuntu-minimal-jammy:minimal-22_04-lts-gen2:latest"

echo "Creating the resource group"
az group create --name $MY_RESOURCE_GROUP_NAME --location $REGION

echo "creating vm"
# make sure the size is available (both location and subscription)
#  az vm list-skus --location eastus --resource-type virtualMachines --zone --all --output tab
az vm create \
    --resource-group $MY_RESOURCE_GROUP_NAME \
    --name $MY_VM_NAME \
    --image Ubuntu2204 \
    --size Standard_B1s\
    --admin-username $MY_USERNAME \
    --assign-identity \
    --generate-ssh-keys \
    --vnet-name default \
    --subnet default \
    --verbose \
    --output json

az vm wait --name $MY_VM_NAME --resource-group $MY_RESOURCE_GROUP_NAME --created 

export IP_ADDRESS=$(az vm show --show-details --resource-group $MY_RESOURCE_GROUP_NAME --name $MY_VM_NAME --query publicIps --output tsv)

echo "My ip" $IP_ADDRESS
echo "now delete"
az group delete --name $MY_RESOURCE_GROUP_NAME --yes