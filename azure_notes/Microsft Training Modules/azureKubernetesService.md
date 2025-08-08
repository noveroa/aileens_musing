# Azure Docker & Kubernetes
## Azure Kubernetes Service (AKS)

> _ad nauseum_ a container is an atomic unit of software that packages up code, dependencies, and configurations for a specific application, allowing one to split up monolithic applications into microservices. They are immutable, smaller than a VM, lightweight,
> _ad nauseum_ container management - managing containers

* AKS
    * Axure service to manage hosted kubernetes enviornments and makes it simple to deploy/manage containerized applications in azure cloud
    * enabled with automated updates, self-healing, easy scaling
    * manages control place, customer manages the agent nodes and the VMs on which the node runs
    
    * ![alt text](https://learn.microsoft.com/en-us/training/modules/intro-to-azure-kubernetes-service/media/3-development-accelerate.png)

    * Bridge to Kubernetes
        * run/debug code on development computer while still being connected to your k8 cluster and the rest of the application or services
    * Azure servuce integration
    
    Earlier, you learned about AKS support for DevOps capabilities through Azure. Here, we list out Azure resources you should consider to enhance your AKS Kubernetes offering. These features each represent compelling factors for why customers choose AKS.

    | Service	| Consideration |
    | Identity and security management	| Do you already use existing Azure resources and make use of Microsoft Entra ID? You can configure an AKS cluster to integrate with Microsoft Entra ID and reuse existing identities and group membership. |
    | Integrated logging and monitoring	 | AKS includes Azure Monitor for containers to provide performance visibility into the cluster. With a custom Kubernetes installation, you decide on a monitoring solution that requires installation and configuration. |
    | Auto Cluster node and pod scaling | 	Deciding when to scale up or down in a large containerization environment is tricky. AKS supports two auto cluster scaling options. You can use either the horizontal pod autoscaler or the cluster autoscaler to scale the cluster. The horizontal pod autoscaler watches the resource demand of pods and increases pod resources to match demand. The cluster autoscaler component watches for pods that can't be scheduled because of node constraints. It automatically scales cluster nodes to deploy scheduled pods. |
    | Cluster | node upgrades	Do you want to reduce the number of cluster-management tasks? AKS manages Kubernetes software upgrades and the process of cordoning off nodes and draining them to minimize disruption to running applications. Once done, these nodes are upgraded one at a time. |
    | GPU enabled nodes	Do you have compute-intensive or graphic-intensive workloads? AKS supports GPU-enabled node pools. |
    | Storage volume support |	Is your application stateful, and does it require persisted storage? AKS supports both static and dynamic storage volumes. Pods can attach and reattach to these storage volumes as they're created or rescheduled on different nodes. |
    | Virtual network support |	Do you need pod-to-pod network communication or access to on-premises networks from your AKS cluster? An AKS cluster can be deployed into an existing virtual network with ease. |
    | Ingress with HTTP application-routing support |	Do you need to make your deployed applications publicly available? The HTTP application-routing add-on makes it easy to access AKS cluster deployed applications. |
    | Docker image support	| Do you already use Docker images for your containers? AKS supports the Docker file image format by default. |
    | Private container registry |	Do you need a private container registry? AKS integrates with Azure Container Registry (ACR). You aren't limited to ACR; you can use other container repositories, whether public or private. |

> All of these features are configurable, either when you create the cluster or following deployment.