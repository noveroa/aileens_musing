# Azure Docker & Kubernetes

* Node Pool
    * A group of nodes with the same configuration in an AKS (azure kubernetes service) cluster.  
    * the nodes contain the underlying VMs that run the applications
    * Types
        * User
            * Nodes supporting the workloads
            * Windows or Linux OS systems
        * System
            * Host the critical system pods making up the control plane
            * _allows only LINUX as the node OS_ running Linux-based workloads
            * reserved for system workloads and normally would not run custom workloads
            * AKS cluster must have **at least** one system node pool with at least one node
    * Number Considerations
        * Up to 100 nodes per pool - set limits!
        * System : must have at least 1, standard at least 3 for production
        * User: 0 +; depends on your workloads and usage
    * Application Deman in AKS Clusters
        * _Scaling_ 
            * Manually scale the pods/nodes (silly)
                ```sh
                $ az aks nodepool add {} 
                $ az aks nodepool scale {}
                ```
            * Automation via horizontal scaling
                * _pod autoscalers_ to scale the pods
                    * scale workload replicas
                    * Kubernets Metrics server collects memory and processor metrics fro the controllers, noes, containers
                    * pod autoscaler checks _metrics api_ every 30 secs and determines scaling up/down given demand
                    * scales pods only on available nodes in the configured node pools of the cluster
                * cluster autoscalers to scale the nodes
                    * if no more pods can be scheduled, resource contraint is triggered
                    * scale the number of nodes in the cluster node pool
    * AKS Spot node pools 
        * good for workloads tat can be interrupted
        * Spot Virtual Machines (Spot VM)
            * a VM that gives you access to unused azure compute capacity like AWS spot instances
            * availabilty : cpacity, size, region, time of day
            * no SLAs
            * Eviction Policy:
                * azure will default with 30 escond notice when capacity in region becomes limited
                * default : Deallocate
                    * state of vm -> stopped/deallocated when evicted and can be redeployed when capacity opens up again
                    * when deallocated is its still being charged for any unerlyging disks
                * delete: 
                    * avoid quota limits or disk costs; delete VM; the autoscaling of a spot VMSS can handle the recreatoin of new VMs as applicable
        * Spot Vitual Machine Scale Set
            * VMSS supporting spot Vms
            * choose the eviction policy : deallocate (default) or delete
            * autoscaling can handle recreation if delete is chosen
        * Spot Node Pool
            * use spot vmss for the user node pool
            * limitations:
                * no high availabilty guarentee
                * need to enable multuple-node-pool support
                * only user (not system) node pools
                * can't upgrade a spot node pool
                ```sh
                $ az aks nodepool add 
                    --resource-group resourceGroup 
                    --cluster-name aksCluster 
                    --name spotpool01 
                    --max-count 3 
                    --min-count 1 
                    --enable-cluster-autoscaler # note
                    --priority Spot  # note
                    --eviction-policy Delete    # note
                    --spot-max-price -1 
                    --no-wait
                    ```
        * Taint
            * apply to a node to indicate that only specific pods can be schdeuled on it
        * Toleration
            * specification on a pod to allow (but not require) a pod to be scheduled on a node with a corresponding taint
            > Taints and tolerations don't guarantee a pod will be placed on a specific node. For example, if a node has no taint, then it's possible that the pod with the toleration might be scheduled on the untainted node. Specifying an affinity with taints and tolerations can address this issue.
        * Node Affinity
            *  describe which pods are scheduled on a node. 
        
        ```sh
        apiVersion: v1
        kind: Pod
        metadata:
        name: nginx
        labels:
            env: test
        spec:
        containers:
        - name: nginx
            image: nginx
            imagePullPolicy: IfNotPresent
        tolerations:
        - key: "kubernetes.azure.com/scalesetpriority"
            operator: "Equal"
        value: "spot"
        effect: "NoSchedule"
        affinity:
            nodeAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
            - key: "kubernetes.azure.com/scalesetpriority"
                operator: In
                values:
                - "spot"
        ```
* AKS resource-quota policies - Azure Policy 
    * Azure Policy helps you enforce standards and assess compliance at scale for your cloud environment.
    * Kubernetes admission controller
        * kubernetes plug-in that intercepts authenticated and authorized requests to the kubernetes api 
        * admission-controller webhook
            * http callback functoin receiving the admission requests then acts on them 
                * validating
                    * validates object values and can reject requests
                * mutating
                    * invoked first, change / apply defaults on the api object sent to the API server
    * Open Policy Agent (OPA) 
        * open source, general purpose policy engine to author policies on how system should behave with declarative language
        * OPA Gatekeeper
            * open-source, validating, Kubernetes admission controller webhook that enforces Custom Resource Definition (CRD)-based policies that follow the OPA synta
    * Azure Policy for AKS
        * extends OPA Gatekeeper integrating it with AKS via built in policies