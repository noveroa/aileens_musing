# some notes

Module Directory
* terraform.tf - This file holds the provider definitions and versions.
* variables.tf - This file contains the input variable definitions and defaults.
* outputs.tf - This file contains the outputs and their descriptions for use by any external modules calling this root module.
* main.tf - This file contains the core module code for creating the solutions infrastructure.
* development.tfvars - This file will contain the inputs for the instance of the module that is being deployed. Content in this file will vary from instance to instance.

# global exports:

```sh
    export TF_LOG=ERROR
    export TF_LOG_PATH="/<path>/<to>/{}.log"
    export ARM_SUBSCRIPTION_ID={}

    terraform init
    terraform plan -var-file=development.tfvars
    terraform apply -var-file=development.tfvars

```

> i also added this to speed up deployment:
```sh
    provider "azurerm" {
        ...
        resource_provider_registrations = "none"
        ...
    }
```


> Simplified Resource Configuration: AVM modules handle much of the complex configuration work behind the scenes
Built-in Recommended Practices: The modules implement many of Microsoft’s recommended practices by default
Consistent Outputs: Each module exposes a consistent set of outputs that can be easily referenced
Reduced Boilerplate Code: What would normally require hundreds of lines of Terraform code can be accomplished in a fraction of the space
