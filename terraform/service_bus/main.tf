terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=2.57.0"
    }
  }
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "servicebusrg"
  location = "West Europe"
}

resource "azurerm_servicebus_namespace" "sbn" {
  name                = "svcbusns"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "Standard"

  tags = {
    source = "terraform"
  }
}

resource "azurerm_servicebus_queue" "queue" {
  name                = "svcbusq"
  resource_group_name = azurerm_resource_group.rg.name
  namespace_name      = azurerm_servicebus_namespace.sbn.name
}

resource "azurerm_servicebus_topic" "topic" {
  name                = "svcbustopic"
  resource_group_name = azurerm_resource_group.rg.name
  namespace_name      = azurerm_servicebus_namespace.sbn.name
}

resource "azurerm_servicebus_subscription" "svcbsub1" {
  name                = "sbcbustopicsub1"
  max_delivery_count  = 100
  topic_name          = azurerm_servicebus_topic.topic.name
  resource_group_name = azurerm_resource_group.rg.name
  namespace_name      = azurerm_servicebus_namespace.sbn.name
}

resource "azurerm_servicebus_subscription" "svcbsub2" {
  name                = "sbcbustopicsub2"
  max_delivery_count  = 100
  topic_name          = azurerm_servicebus_topic.topic.name
  resource_group_name = azurerm_resource_group.rg.name
  namespace_name      = azurerm_servicebus_namespace.sbn.name
}
