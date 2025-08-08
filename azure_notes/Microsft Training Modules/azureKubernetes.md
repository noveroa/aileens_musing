# Azure Docker & Kubernetes

* Kubernetes
    * A container management platform/tool
    * Standard container management runtime focuses on multiple containers working together 
    * Portable, extensisible open-source platform for managing / ochestrating containerized workloads - simplifying container management tasks and a declarative configuration for ochestrator
        * Benefits - abstraction of taasks
            * self healing
            * dynamic scaling
            * rolling updates / rollbacks
            * managing storage
            * managing network traffic
            * storing / managing sensitive information (usernames / passwords)
        * configure/maintain load balancing
        * Network connectivity
        * ochestrating deployment process
    * Container Management
        * Process of organizaing, adding, removing, updating significant number of containers
        * repetivie tasks of changing caching, rolling out new versions, updating all active containers
    * Container Orchestrator
        * System that automatically deployes and manages containerized apps
        * Handles scaling dynamic changes in the environment to increase/decreases the number of deployed instances of the app
        * Ensures all deployed container instances are updated when a new version of a service is released
* kubernetes - how it works
    * computer cluster 
        * a set of computers that are configured to work together and view as a single system
        * a cluster uses centralized software thats responsible to scheduling / controlling these tassks
        * the computer in a cluster that run tasks is called a **node**
        the computer that runs the scheduling softwaree are called the **control planes**
    * Kubernetes Cluster
        * 1+ main control plane and 1+ nodes
        * K*s Control Plane
            * Runs collection of services that manage the orchestration funtionality in Kubernetes
                * _note_ The fact that a control plane runs specific software to maintain the state of the cluster doesn't exclude it from running other compute workloads. However, you usually want to exclude the control plane from running noncritical and user app workloads.
                * Services:
                    * administrative services: cluster component communication, workload schduling, cluster-state peristence
                    * API server
                        * front end of k8 control place
                    * Backing Store
                        * persistent storage in which your kubernetes cluster saves completed configurations; etcd - a key-value stor storing the current state and desired state of all objects within the cluster
                    * Scheduler
                        * assigns worklaods acorss all nodes
                        * assigns nodes to newly created containers
                    * Controller Manager
                        * launches/monitors the controllers configured for a cluster via the API server; tracks object sttes in the cluster 
                    * Cloud Controller Manager
                        * integrates with underlying cloud technologies in your cluster like balances queues and storage      
        * K8s Node
            * The cluster where the workload runs
            * each node communicates with teh contraol plane via api server to inform about chanegs on the node
            * Services - how the workload runs
                * Kubelet
                    * agent on each node monitoring work requests and health
                * Kube-proxy
                    * local cluster neetowrking and runs on each node, ensuring each node has a unique IP address, handles routig and loadbalancing and traffic
                * Container runtime
                    * underlying software to run the containers on a kubernetes cluster; fetch, start, stop container images (like docker)
        * ![alt text](https://learn.microsoft.com/en-us/training/modules/intro-to-kubernetes/media/3-cluster-architecture-components.svg)
    * interactions
        * Pod
            * represents a single instance of an app runnnig on kubernetes, the containerized apps
            * can contain 1+ containers (but noramlly not 1+ of teh same app)
            * YAML templates that can be reused 
            * Lifecycles
                * Pod Phases
                    | State | description |
                    | ----- | ----- |
                    | Pending|The pod accepts the cluster, but not all containers in the cluster are set up or ready to run. The Pending status indicates the time a pod is waiting to be scheduled and the time spent downloading container images.|
                    | Running |The pod transitions to a running state after all of the resources within the pod are ready.
                    | Succeeded |	The pod transitions to a succeeded state after the pod completes its intended task and runs successfully.|
                    | Failed | Pods can fail for various reasons. A container in the pod might fail, leading to the termination of all other containers, or maybe an image wasn't found during preparation of the pod containers. In these types of cases, the pod can go to a Failed state. Pods can transition to a Failed state from either a Pending state or a Running state. A specific failure can also place a pod back in the pending state.|
                    | Unknown |	If the pod's state can't be determined, the pod is in an Unknown state.|
                * Container States
                    | State	| Description |
                    | ------ | ----- |
                    | Waiting |	Default state of a container and the state that the container is in when it's not running or terminated.|
                    | Running |	The container is running as expected without any problems.|
                    | Terminated |	The container is no longer running. The reason is that either all tasks finished or the container failed for some reason. A reason and exit code are available for debugging both cases.|
            
            * Deploying Kubernetes
                * Pod Deployment Options
                    * Pod Templates
                        *  yaml template to define config of a pod to be deployed
                    * Replication Controllers
                        * yaml using pod tempaltes and defines the number of pods to run
                    * Replica Sets
                        * _preferred_ yaml replaces teh replication controller - same as repcontroller but also has _selector value_ identifying the pods running beneath it
                    * Deployments
                        * creates the management object one level higher than replica set, deploy/manage updates for pods in a cluster
                * Networking
                    * by default pods and nodes can't communicate with each other by using different IP address ranges
                    * pods are transient, thus ip addresses is temporary  and can't be used to reconnect to a newly created pod
                    * A kubernetes service
                        * a kubernetes object that provides stable networking for pods, enabling communication betwee nodes, pods, and users of the app
                        * assigbs a service an IP address on reation (like a node / pod) and get assigned from a service cluster's ip range, and a DNS name
                            | Service	| Description |
                            | ----- | ----- |
                            | ClusterIP	| The address assigned to a service that makes the service available to a set of services inside the cluster. For example, communication between the front-end and back-end components of your app. |
                            | NodePort	| The node port between 30000 and 32767 that the Kubernetes control plane assigns to the service; for example, 192.169.1.11 on clusters01. You then configure the service with a target port on the pod that you want to expose. For example, configure port 80 on the pod running one of the front ends. You can now access the front end through a node IP and port address. |
                            | LoadBalancer	| The load balancer that allows for the distribution of load between nodes running your app, and exposing the pod to public network access. You typically configure load balancers when you use cloud providers. In this case, traffic from the external load balancer is directed to the pods running your app. |
                        * grouping pods
                            * Silly to manage by IPs
                            * Service object allows to target/ anahge specific pods in the cluster using selector labels
                * Kubernetes Storage
                    * Like docker - volume storage
                    * if pod removed, volume removed
                    * thus _PersistentVolume_ and _PersistenVolumeClaims_
