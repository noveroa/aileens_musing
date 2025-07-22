AKS - Azure Kubernetes Service

> Managed Kubernetes service offered by Microsoft Azure that simplifies the deployment and management of containerized applications. AKS handles the complexities of Kubernetes, allowing users to focus on their applications rather than infrastructure management. It provides a scalable, secure, and cost-effective way to run containerized workloads in the cloud. 

3 ways devops to create kubernetes cluster
* On-premise (data center) 
    * self managed
    * spin up the master and worker nodes as vms all in private cloud
    * maintanence - upgrades (kubernetes, centOs, ...)
    * cost - servers, dataserver...
    * scale / availibilty - unless using software, no real 'out of the box' autoscaling
    * integration - (ingress, secrets, csi drivers...) - all managed by you - and these are stateless
    * security - on private cloud, customization
    * 
* Virtual Machine K8s
    * self managed 
    * virtual machines on azure service as master and workers (install configurations)
    * maintanence - upgrades (kubernetes, centOs, ...)
    * cost - moderate - depends on how you are cost optimizing the azure VMs, storage, downtimes (pre requesting the vms, storage..)
    * scale / availibilty - manually configure the virtual machine autoscaling with scale sets
    * int egration - make sure integrate with the other services to manage the storage, secrets, active directory
* AKS
    * azure managed 
    * maintanence - AKS can support automated upgrades/patches with scheduler for minor versions
    * cost - charge per resources used, ie aks will be a bit more efficiently cost optimized
    * scale / availibilty -  configured node pools (virtual machine scale sets)
    * integration - easier to integrate the azure services automatically
    * security - on a public cloud, managing connections to potentially on-premise databases,  not as customizable as on-premise
    * less learning curve, easier maintenance.

# Concepts
* Nodes and Node Pools:
    * Nodes are virtual machines hosting Virtual machines
    * Node pools group nodes with similar configurations. 
* Pods
    * Pods are the smallest deployable units in Kubernetes
    * encapsulating one or more containers that share the same network and storage 
* Control Plane
    * control plane manages the cluster and its resources, including scheduling pods, managing networking, and more. 

