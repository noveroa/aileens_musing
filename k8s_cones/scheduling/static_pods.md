## Kubernetes Static Pods

> Kubernetes ArchitectuteL _kubelet_ functions as one of the control plane components in K8s, relying on the _kube-apiserver_ for instructions on what Pods to load on its Node - based on the _kube-scheduler_, data stored in the _.etdc_ data store.

* the _kubelet_ can manage a Node independently of the kube-apiserver, kubescheduler, master nodes...
    * there is the kubelet and docker (to make containers), no cluster, no api server. but the kubelet knows how to make pods!
    * but you dont need the api-server to create pods, a definition yaml! and without the apiserver, you can configure the kubelet to read the Pod definition files from a directory on the server designated to store information about Pods, where it can periodically check a directory of definition.yamls.
        * the kubelet will create the pod, recreate the pod, etc.  
        * the kubelet will ONLY makes pods (not replica sets, deployments, services....)

* these are **Static Pods**
    * the kubelet only works at the pod level
    * the directory in which the pod definition files are placed is configured at the kubelet (kubelet.service file) and can be any directory on the host.
        * the path is known as the _pod manifest path_ 
            * check in the kubelet.service manifest 
                * `systemctl cat kubelet.service`
                * `ps -aux | grep kubelet` and identify config file `--config=/var/lib/kubelet/config.yaml`
            * check the config options
                * staticPodPath option
                    * `kubectl config view`
    * to view `docker ps` NOT the kubelt commands - we have no api server and no other resources
    * why use static pods?
        * static Pods are not dependent on the Kubernetes control plane; deploy components of the control place itself.
        * admin tool sets
