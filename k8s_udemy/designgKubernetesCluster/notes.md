# Kubernetes Clusters

* Questions to ask
    Depending on the kind of application, the resource requirements may vary

    * What is the purpose of this cluster? 
        * learning
           * minikube, singlenode cluster
        * development/ testing 
            * multi-node cluster with a single master node, multple workers
            * kubeadm or quick provision gcp, aws, aks
        * production 
            * high available, multi node with multiple master nodes
            * kubecdm or provision tools
            * up to 5000 nodes
            * up to 150000 pods
            * up to 300000 total containers
            * up to 100 pods/node          
    * What is the cloud adoption at your organization?
        * managed by a cloud provider
        * on-prem
        * self-hosted
    * What kind of workloads are you going to run on this cluster?
        * consider your storage options
    * How many applications are to be hosted on the cluster?
    * What kind of applications are going to be hosted on the cluster?
        * Web applications
        * big data
        * analytics?
    * What type of network traffic are these applications expecting?
        * Continuous 
        * heavy traffic
        * burst?