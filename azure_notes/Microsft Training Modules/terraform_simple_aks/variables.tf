variable "resource_groups" {
  description = "Resource Groups Parameters"
  type = map(object({
    location = string
  }))
  default = {
    rg1 = {
      location = "eastus"
    }
  }
}

variable "kube_params" {
  description = "Azure Kubernetes Services (AKS) parameters"
  type = map(object({
    rg_name              = string
    dns_prefix           = string
    np_name              = string
    tags                 = optional(map(string), {})
    vm_size              = optional(string, "Standard_B2s")
    client_id            = optional(string, null)
    client_secret        = optional(string, null)
    auto_scaling_enabled = optional(bool, true)
    max_count            = optional(number, 1)
    min_count            = optional(number, 1)
    node_count           = optional(number, 1)
    service_principal = optional(list(object({
      client_id     = string
      client_secret = string
    })), [])
    identity = optional(list(object({
      type         = optional(string, "SystemAssigned")
      identity_ids = optional(list(string), [])
    })), [{}])
  }))
  default = {
    aks1 = {
      rg_name    = "rg1"
      dns_prefix = "kube"
      np_name    = "np1"
    }
  }
}

variable "tags" {
  description = "Tags to be applied to all resources"
  type        = map(string)
  default     = {}
}