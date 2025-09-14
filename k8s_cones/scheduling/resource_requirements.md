## Kubernetes Resource Requirements & Limits

* In order to run, every nod consumes resources, ie 2 CPUS, 1 MEM.  When scheduled, it consumes the resources available on that node. 
* The scheduler considers the amount of resources required by a pod, resources available on the nodes, and identifies the optimal node to place a pod on at that time.
    * if no nodes have sufficient resources available, the scheduler holds back placing the pod (state: PENDING)

# resources
* _resource request_ One can specify some resources required for a container
    * ie. minimum amount of CPU, memory requested
        ``` pod.yaml
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
                  ports: 
                    - containerPOrt: 8080
                  resources:
                    requests:
                      memory: "4Gi"
                      cpu: 2
                    limts:
                      memory:"2Gi"
                      cpu: 2
        ```

    * **By default**, 
        * a container has no limit to the resources it can consume on a node; so it can consume all the resources on a pod. 
    * thus you can set limits on the amount of resources the pod can use
        * CPU if it does try to go beyond - throttle! 
        * MEM - terminates - OOM (out of memory) error
            

# Limits
* by default, Kubernetes does not have resource requests or limits configured for pods.

* **limit ranges** are used to allow you to define default values to be set for containers in pods, even those without `requests ` specidifed in the `.yaml`
    * set at namespace level
    * max - refers to the maximum limit that can be set on a container in a pod
    * min - refers to the minimum request a container in a pod can make.
    * Limits enforced when a pod is created if you create or change a limit range, it does not affect existing pods.

    ```limitrange-cpu.yaml
    apiVersion: v1
    kind: LimitRange
    metadata:
        name: cpu-resource-constriant
    spec:
        limits:
        - default:
            cpu: 500m
            defaultRequest:
            cpu: 500m
            max:
            cpu: "1"
            min:
            cpu: 100m
            type: Container
    ```

    ```limitrange-memory.yaml
    apiVersion: v1
    kind: LimitRange
    metadata:
        name: mem-resource-constriant
    spec:
        limits:
        - default:
            mem: 1Gi
            defaultRequest:
            mem: 1Gi
            max:
            mem: 1Gi
            min:
            mem: 500Mi
            type: Container
    ```

# Resource Quotas
* **resource quota**  is a namespace level object that set hard limits for requests and limits for the application

    ```resourcequota.yaml
       apiVersion: v1
       kind: ResourceQuota
       metadata: 
         name: resource-quota
       spec:
         hard:
           requests.cpu: 4
           request.memory: 4Gi
           limits.cpu: 10
           limits.memory: 10Gi
    ```




