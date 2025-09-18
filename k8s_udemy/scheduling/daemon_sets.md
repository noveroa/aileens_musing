## Kubernetes DaemonSets

> Similar to replica sets, daemon sets deploying multiple instances of pods. Key, though, it runs one copy of the pod on _each_ node of your cluster.  As a new node is added to the cluster, a replica of the pod is added automatically to that node.  When the node is removed, so too is the pod.

* DaemonSet ensures that one copy of the pod is always present on every node in your cluster 
    * uses: logging agent, monitoring agents, netoworking the required Kuberbetes kube-proxy, 
* How do daemonsets work to ensure a pod is scheduled 
    *  Node affinity and selectors

 ```daemon-set.yaml
 apiVersion: apps/v1
 kind: DaemonSet
 metadata: 
    name: moitoring-daemon
spec: 
    selector:
      matchLabels:
        app: monitoring-agent
    template:
      metadata:
        labels:
          app: monitoring-agent
      spec:
        containers:
        - name: monitoring-agent
          image: monitoring-agent
```