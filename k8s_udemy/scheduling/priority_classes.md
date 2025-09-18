## Kubernetes Priority Classes
>Kubernets runs different applicatoins as oids, each with different priorites (ie the kubernetes conrtol plane needs to run no matter what - they are top priority!) , similar one can have critical applications, or priority databases, or lower back ground jobs.

* Priority classes define priorities. for different workloads such that higher priority workloads always get a priority over lower priority ones.
    * If a higher priority pod cannot be scheduled, the scheduler will try to terminate a lower priority workload to make that happen.
    * Priority classes are non-namespace objects
        * not created within a specific namespace
        * not attached to a specific namespace
        * once creatd, available to be configured on any pod in any namespace
    * priorities using a range of numbers
        * high as one billion and as low as ~ negative two billion
        * larger number indicates higher priority
        * range is for the applications and workloads that are deployed on the cluster

    * There is a separate range, dedicated for internal system critical parts, such as the Kubernetes control plane components itself.

    * `kubectl get priorityclass`
        * [optional] value `globalDefault` will assign this as the default priority of all pods
            * cannot have more than one priority class with the global default property set to true.
        * [optional] value `preemptionPolicy`
            * behavior when a higher priority job comes in and there are no more resources
            * if the preemption policy is not set: default value is set to `PreemptLowerPriority` killing the pod
            * to avoid this behaivor set to `Never` and the higher priority will wait for the next resource

    ```priorityclass.yaml
    apiVersion: scheduling.k8s.io/v1
    kind: PriorityClass
    metadata:
      name: high-priority
    values: 1000000000
    description: "priority class for mission critical pods"
    globalDefault: true <--default : false --->
    preemptionPolicy: PreemptLowerPriority [never]
    ```

    * to associate with a pod - use the parameter: `priorityClassName`:
        * pods do not have to have the field, priority would just be 0
        * to add, one must make the priority class
    * compare priority classes of pods"
        * ```kubectl get pods -o custom-columns="NAME:.metadata.name,PRIORITY:.spec.priorityClassName``

    ```pod.yaml
            apiVersion: v1
            kind: Pod
            metadata:
                name: nginx
                labels:  
                    name: nginx
            spec:
                containers:
                - name: nginx-container
                  image: nginx
                  ports:
                  - containerPort: 8080

                priorityClassName: high-priority
        ```

 