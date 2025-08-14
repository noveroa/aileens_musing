output "resource_groups" {
  description = "Resource Group Outputs"
  value       = { for rg in azurerm_resource_group.az_reg : rg.name => rg.location }
}

output "aks" {
  description = "AKS Outputs"
  value       = { for kube in azurerm_kubernetes_cluster.aks_cluster : kube.name => { "id" : kube.id, "fqdn" : kube.fqdn } }
}