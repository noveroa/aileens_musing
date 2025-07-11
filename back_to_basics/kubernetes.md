

# aileens_musing

## Cambridge, MA

![N|Solid](https://ca.slack-edge.com/T0495HV8H-U01AM69UW3E-ae635702c574-72)

###### 
Kubernetes (K8s)...

Orchestration platform that automates the deployment, scaling, and management of containerized applications - ie the manager for multiple (ie hundreds/thousands) of containers (ie looking at you Docker). 
* Stay up and running
* Can communicate with each other
* Can be updated without downtime
* Recover automatically from failure


## A container is a standalone, executable package of software that includes:
* The application code
* Runtime
* Libraries
* Environment variables
* Configuration files



## Key Ideas
* Cluster
    * A Kubernetes cluster consists of:
    * Master (Control Plane): Manages the cluster.
    * Nodes (Worker Machines): Run the actual containerized applications.
* Pod
    * Smallest deployable unit in Kubernetes.
    * Usually contains 1+ containers that share resources (like networking and storage).
* Deployment
    * Describes how many replicas of a pod should run.
    * Handles rolling updates and rollbacks.
* Service
    * A stable IP and DNS name that abstracts a set of pods.
    * Allows pods to talk to each other or expose applications to the outside world.
* Ingress
    * Manages external access to services (like a reverse proxy or load balancer).
    * Often used for HTTP routing.
* ConfigMap & Secret
    * Used to inject configuration data into containers.
    * Secret is for sensitive info like passwords; ConfigMap is for general config.
* Volumes
    * Handle persistent storage for containers (since containers are ephemeral).

# What Kubernetes can do FOR YOU!
* Scaling	Automatically add/remove containers based on traffic/load
* Load Balancing	Distributes traffic between replicas of your service
* Self-Healing	Restarts failed containers, replaces unhealthy ones
* Rolling Updates	Updates your app with zero downtime
* Service Discovery	Auto-assigns DNS/IPs to containers so they can talk to each other
* Resource Management	Ensures containers don't use too much CPU/memory

