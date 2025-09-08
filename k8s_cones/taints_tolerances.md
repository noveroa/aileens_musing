## Kubernetes Taints and Tolerances

> pod-to-node relationship and how you can restrict what pods are placed on what nodes.

* taints and tolerations have nothing to do with security or intrusion on the cluster.

* taints and tolerations are used to set restrictions on what pods can be scheduled on a node.

* case:
    * you have a group of nodes and pods with no restrictions, the scheduler will equally distribute the pods across the nodes.
    * now, say one node has dedicated resources for a particular use/application, thus only ppods belonging to that app should be placed on that node.
         * First, _taint the node_ preventing all pods from being placed ( taint: Blue) 
            ``` kubectl taint nodes <node-name> key=value:taint-effect ``` # taint-effect defines what happens if pod doesnt tolerate the taint
            * three types of taint-effect
                * no schedule - pods will not be scheduled on the node
                * prefer no schedule - avoid placing pod on the node
                * no execute -  new pods will not be scheduled on the node and existing pods on the node, if any, will be evicted if they do not tolerate the taint.
            ``` kubectl taint nodes node01 app=blue:NoSchedule  ``` 
         * Second, add a _toleration to the pods_ that are allowed for that tainted node 

            ```pod.yaml
                apiVersion: v1
                kind: Pod
                metadata:
                    name: myapp-pod
                    <!-- ******** -->
                    labels:  
                        app: myapp
                        type: front-end
                spec:
                    containers:
                    - name: nginx-container
                      image: nginx
                    tolerations:
                    - key: "app"
                      operator: "Equal"
                      value: "blue"
                      effect: "NoSchedule"
                ```
    * Remember!
        *  taints and tolerations do NOT tell the pod to go to a particular node. Instead, they tell the node to only accept pods with certain tolerations.
        * thusly, the pod CAN be placed on other nodes
        * if a requirement is for a pod to be placed ONLY on a particular node, ---> Node Affinity
