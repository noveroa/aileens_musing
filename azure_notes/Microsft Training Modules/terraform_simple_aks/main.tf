resource "azurerm_resource_group" "az_reg" {
  for_each = var.resource_groups
  name     = each.key
  location = each.value.location
  tags     = var.tags
}

resource "azurerm_kubernetes_cluster" "aks_cluster" {
  # https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/kubernetes_cluster
  for_each            = var.kube_params
  name                = each.key
  location            = azurerm_resource_group.az_reg[each.value.rg_name].location
  resource_group_name = azurerm_resource_group.az_reg[each.value.rg_name].name
  dns_prefix          = each.value.dns_prefix

  default_node_pool {
    auto_scaling_enabled = each.value.auto_scaling_enabled
    max_count            = each.value.auto_scaling_enabled ? each.value.max_count : null
    min_count            = each.value.auto_scaling_enabled ? each.value.min_count : null
    node_count           = each.value.node_count
    vm_size              = each.value.vm_size
    name                 = each.value.np_name
  }

  dynamic "service_principal" {
    for_each = each.value.service_principal
    content {
      client_id     = service_principal.value.client_id
      client_secret = service_principal.value.client_secret
    }
  }

  dynamic "identity" {
    for_each = each.value.identity
    content {
      type         = identity.value.type
      identity_ids = identity.value.identity_ids
    }
  }
  tags = each.value.tags
}