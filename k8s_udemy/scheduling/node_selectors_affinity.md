## Kubernetes Node Selectors and Node Affinity

* Case: 
    * you have 3 nodes - two with lownumber of resources and a third with higher. 
    * You also have different workloads running in the cluster.   
    * To ensure those that have a higher cpu/horsepower will not not run out of resources ... 
> Set limitations on the pods so they only run on certain (larger/applicably sized) nodes

* Node Selectors
    * The node schdeler uses the nodeSlector key:values to match the node resources (the key:value are the labels assigned to the nodes)

    * you have to label nodes priot to the creation of the pods.
        ```kubectl label noxes <node name> <label-key>=<label-value>```
        ```kubectl label nodes node-1 size=large```
    * there is no advanced expressions like or or not with node selectors, ie  "don't put it on this type of node"  or "use this or that type"--> use nodeaffinity and anti affinity patterns.

        ```pod.yaml
            apiVersion: v1
            kind: Pod
            metadata:
                name: myapp-pod
                labels:  
                    app: myapp
                    type: front-end
            spec:
                containers:
                - name: nginx-container
                  image: nginx
                nodeSelector:
                    size: Large. <!-- labels assigned to the nodes --> 
        ```

* Node Affinty
    * Provides us with advanced capabilities to limit pod placement on specific nodes.
    * what if in a given pod, there is not node that matches the nodeaffiinity, or the node changes
        * The type of node affinity defines the behavior of the scheduler with respect to node affinity and the stages in the life cycle of the pod. _There are currently two types of node affinity available_,_
            * There are two states in the lifecyle of the pod when considering node affinity.  - scheduling (pod is being created) and execution (the pod is running and somethign in the environment changes the node affinity)
            * requiredDuringSchedulingIgnoredDuringExecution
            * preferredDuringSchedulingIgnoredDuringExecution
            * requiredDuringSchedulingRequiredDuringExecution (planned)
        ```pod.yaml
            apiVersion: v1
            kind: Pod
            metadata:
                name: myapp-pod
                labels:  
                    app: myapp
                    type: front-end
            spec:
                containers:
                - name: nginx-container
                  image: nginx
                affinity:
                  nodeAffinity:
                     requiredDuringSchedulingIgnoreDuringExecution:
                       nodeSelectorTerms:
                       - matchExpressions:
                         - key: size
                           operator: In <!-- Operators, ie  NotIn, Exists .. --> 
                           values: 
                            - Large
                            - Medium 
                            - ... 
        ```

        ```
        apiVersion: apps/v1
        kind: Deployment
        metadata:
            name: red
        spec:
            replicas: 2
            selector:
                matchLabels:
                run: nginx
            template:
                metadata:
                    labels:
                        run: nginx
                spec:
                    containers:
                    - name: nginx
                      image: nginx
                    affinity:
                        nodeAffinity:
                            requiredDuringSchedulingIgnoredDuringExecution:
                                nodeSelectorTerms:
                                - matchExpressions:
                                - key: node-role.kubernetes.io/control-plane
                                    operator: Exists
```
