# Create resource group
az group create --resource-group photoapp --location westeurope

# Create storage account 
az storage account create  --name photoappsa --resource-group photoapp --sku Standard_LRS