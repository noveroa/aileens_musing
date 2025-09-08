## Kubernetes Labels and Selectors, annotations

> Kubernetes labels are optimal for classification
> Kubernetes selectors are used for the grouping and filtering

* Group and select objects using labels and selectors.
    * For each object, attach labels as per your needs, like app, function, color
    * while selecting, specify a condition to filter specific objects.

* Labels - in the metadata

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
```
* you can cli to select:
``` kubectl get pods --selector app=myapp```

* Kubernetes objects use labels and selectors internally.to connect different objects together.
    * case: replica sets
         * the important part to be able to connect the replicaset to a pod the selector configuration to match the labels in the pod of the template:
    * similar for other resources like services

    ```replicaset.yaml
    apiVersion: apps/v1
    kind: ReplicaSet
    metadata:
        name: simple-webapp
        labels:
            app: App1
            function: Front-end
        annotations:
            buildversion: 1.34
    spec:
        replicas: 3
        selector:
        <!-- ******* -->
            matchLabels:
                app: App1
        template:
            metadata:
                labels:
                    <!-- ******* -->
                    app: App1
                    function: Front-end
            spec:
                container:
                - name: simple-webapp
                  image: simple-webapp
    ```

* Annotations
     * annotations are used to record other details for informatory purpose.
        * For example, tool details like name, version, build information, et cetera, or contact details, phone numbers, email IDs, et cetera