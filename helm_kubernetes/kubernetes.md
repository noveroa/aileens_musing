# kubernetes

# why 
> A COE - container orchestration engine
Useful when you need to deploy an application with 100s of microservices, ie you are scaling a docker cluster up and down with a level of management and coordination
# what
> Kuberetes (K8s) automatates deploying, scaling, managing containerized applications on a group of servers
# features
* clustering - groups of computing nodes (workers)
* scheduling - 
* scalbility - able to up/down per traffic demand
* load balancing. - route as applicable
* fault tolerance - restart / rolling restarts / reprovision
* deployment - manage updates 
# engines
* kubernetesn- apache 
* docker swarm - golang, easy to set up, smaller teams
* clud specific?
    * google - GKS
    * aws - ECS
    * azure - container services

* Kubernetes (K8s)
> open resource coe managing containerized apps at a large scale
open source, mature, modular api, large community feature rich

# at a high level
> at least 1 master node/serever and 1+ worker node

master  node  <--- [CLUSTER - worker nodes which has a pod which contains a container]

* master ndde 
    * manages the cluster
    * monitors health of nodes
    * stores configuration, metadata of nodes, etc
    * schedules, provisions, controlls expoosure to apis to clients
* cluster - 1+ worker nodes
* worker node - a virtual machine (VM) - the workhorse (compute reason, storage)
* pod 
    * 1+ containers sharing storage, networking reources
    * smallest deployable unity of computing
    * ephemeral storage
* containers
    * runtime environement for a containerized environment
    * inside a pod
    * run a microservice NOT monolithic applications

# master node
> manages the kubernetes cluster
* API server 
    * gatekeeper for the c;uster
    * command center for operatuins
    * access via kubectl / UI
* Schedular
    * schedule pods across the nodes
    * configuration file controls constraints, etc to find applicable nodes to deploy
* Control Manager
    * overall health control
    * node controller
    * replication controller
    * endpoint controller
    * service content token controller
* etcd
    * distributed key:value database
    * stores current cluster state
    * single source of truth for all nodes, components, 

# worker nodes
> Any virtual machine, physical server where containers are involved, each container has a runtime environment
Connecting to the master 
* 