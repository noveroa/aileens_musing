# Os Upgrades, Kubernetes releases, Cluster Upgrades, Backup and Restore
> Handling maintainance in your cluster ike upgrading a base software or applying patches like security patches, etc.
 * Pod Eviction Timeout
    * default 5 minutes `kube-controller-manager --pod-eviction-timeout=5m0s`
    * if a node goes offline, the master node after the eviction time will consider the node dead; if the node comes back after the eviction time wit will come back with no pods scheduled on it.
        * if a pod that was on that node and not on a replica set, it would be lost. 
    * Prior to maintainance, 
        * Drain the node - pods are gracefully terminated from the node and recreated on another; the node is 'cordoned' or 'marked' thus unschedulable
        * you can also mark a node 'Cordon' - but does not terminate those pods on the node, just marks it unschedulable.
* Kubernetes Releases
    * (k8s releases)[https://kubernetes.io/releases/]

* Cluster Upgrades
    * the core components can be at difference releases, but **none higher than the kube-api-server**
        * controller-manager, kube-scheduler - can be one lower
        * kubelet, kube-procy - can be  lower
        * kubectl 
    * best time to upgrade? 
        * Kubernetes supports only up to the recent three minor versions.
        * one minor release at a time 1.10 --> 1.11 --> 1.12
    * kubeadm helps if manage cluster yourself
    `kubeadm upgrade plan`
        * upgrade your master nodes and then upgrade the worker nodes while the master is being upgraded.
            * the master going down does not mean your worker nodes and applications on the cluster are impacted.  All workloads hosted on the worker nodes continue to serve users as normal.
            * Since the master is down, all management functions are down.
                * cannot access the cluster using kube control or other Kubernetes API
                * cannot deploy new applications or delete or modify existing ones
                * The controller managers don't function 
                * If a pod was to fail, a new pod won't be automatically created
        * next upgrade worker nodes
            * all at once - downtime
            * roll out
            * add new provisioned nodes and move workloads over to new nodes, and remove the old

* Backup and Restore    
    * Backup candidates
        * Resource Configurations: definition files
            * source respository
            * `kubectl get all --all-namespaces -o yaml > all-deployed-services.yaml`
            * other tools
        * etcd cluster: all cluster related information is stored
            * hosted on the master node
            * While configuring etcd, a location where all the data would be stored.
                * the data directory that is, the directory that can be configured to be backed up by your backup tool.
            * take a snapshot of the etcd database by using the etcd control utilities.
        * persistent volumes: applications with configured with persistent storage