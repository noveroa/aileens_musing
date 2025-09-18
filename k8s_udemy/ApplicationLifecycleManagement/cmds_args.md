## Kubernetes Commands and Arguments and Envs

* commands and arguments in a Pod definition file; override the entry points in docker file of image; these are in arrays
* env variables - are arrays of key value pairs, congif maps, or secrets

```pod.yaml
apiVersion: v1
    kind: Pod
    metadata:
        name: myapp-pod

    spec:
        containers:
        - name: nginx-container
          image: nginx
          command: ["sleep", "5000"]
          <!-- command: 
          - "sleep"
          - "5000"
          command: ["sleep"]
          args: ["5000"]  -->
        env:
            - name: APP_COLOR
                value: pink
            - name: APP_COLOR
                valueFrom:
                   configMapKeyRef: 
                      name: webapp-config-map
                      key: APP_COLOR
            - name: SECRET_VALUE
                valueFrom:
                    secretKeyRef:
                        name: secret-name
                        key: secret-key
```

# ConfigMaps
 * With alot of Pod definition files,  you need to manage the environment data stored within the various files.
* ConfigMaps: take this information out of the Pod definition file and manage it centrally
    * Config maps are used to pass configuration data in the form of key value pairs in Kubernetes.
    * When a pod is created, inject the configmap into the pod so the key value pairs are available as environment
    * two phases:
        * create config map
        ```configmap
        apiVersion: v1
        kind: ConfigMap
        metadata:
            name: my-config
        data:
            VAR1: blue
            VAR2: red
        ```

        * inject them into a pod
        ```
            envFrom:
                - configMapRef
                  name: my-config 
            containers:
            - env:
                - name: APP_COLOR
                  valueFrom:
                    configMapKeyRef: 
                      name: webapp-config-map
                      key: APP_COLOR
            volumes:
            - name: app-config-volume
              configMap:
               name: my-config
        ```
# Secrets
* To store sensitive information like passwords or keys.
* similar to config maps, except that they are stored in an encoded or hashed format rather than plain text
* doc: 
    * Dive deep into the world of Kubernetes security with our comprehensive guide to Secret Store CSI Driver. https://www.youtube.com/watch?v=MTnQW9MxnRI
    * https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/
* two phases:
    * createsecret
        ```secret
        apiVersion: v1
        kind: Secret
        metadata:
            name: my-secret
        data:
            -VAR1: blue-
            -VAR2: red-  you need to encode it first! `$echo -n <scret plain text> | base64`
        ```

    * inject them into a pod
        * If you were to mount the secret as a volume in the pod, each attribute in the secret is created as a file with the value of the secret as its content.
        ```
        envFrom:
        - secretRef:
            name: my-secret
        env:
        - name: SECRET_VALUE
            valueFrom:
            secretKeyRef:
                name: my-secret
                key: SECRET_VALUE
        volumes:
        - name: app-secret-volume
        secret:
            secretName: app-secret
        ```
    ie.
    ```
        apiVersion: v1
        kind: Pod
        metadata:
        labels:
            name: webapp-pod
        name: webapp-pod
        namespace: default
        spec:
        containers:
        - image: kodekloud/simple-webapp-mysql
            imagePullPolicy: Always
            name: webapp
            envFrom:
            - secretRef:
                name: db-secret
    ```

# Multicontainer pods
* despite the use of microservices, sometimes two apps need to work together
    * still be developed and deployed separately.
    * need is for the two functionality to work together.
    * You need one web server per main app instance paired together so they can scale up and down together.
        * *multi-container pods* : 
            * share same lifecycle, which means they are created and destroyed together
            * share same network space, which means they can refer to each other as localhost
            * access to the same storage volumes.
* patterns
    * Co-located
        * two containers sharing a lifecyle, dependent on eachother
        ```
        apiVersion: v1
        kind: Pod
        metadata:
            name: webapp-pod
            namespace: default
        labels:
            name: webapp-pod
        spec:
            containers:
            - name: webapp
              image: web11
              ports: 
                - containerPosrt: 8080
            - name: nginx
              image: nginx
        ```
    * initContainer
        * used when initialization steps are performed when a pod starts before main app 
            * ie waiting for db to be ready
        * starts and ends job befpre the main app starts
         ```
        apiVersion: v1
        kind: Pod
        metadata:
            name: webapp-pod
            namespace: default
        labels:
            name: webapp-pod
        spec:
            containers:
            - name: webapp
              image: web11
              ports: 
                - containerPosrt: 8080
            initContainers:
            - name: db-checker
              image: busybox
              command 'wait-for-db-to-start.sh'
          ```
    * sideCarContainer
        * starts first - like initContainer- before the main app
        * executes job
        * _continues_ to run throughout lifecycle of pod
        * uses?
            * log shipper
        * _note_ initContainer with `restartPolicy: Always`
         ```
        apiVersion: v1
        kind: Pod
        metadata:
            name: webapp-pod
            namespace: default
        labels:
            name: webapp-pod
        spec:
            containers:
            - name: webapp
              image: web11
              ports: 
                - containerPosrt: 8080
            initCon tainers:
            - name: log-shipper
              image: busybox
              command 'setup-log-shipper.sh'
              restartPolicy: Always
          ```

# Self Healing Applications
* Self-healing applications through ReplicaSets and Replication Controllers. 
    * The replication controller helps in ensuring that a POD is re-created automatically when the application within the POD crashes. It helps in ensuring enough replicas of the application are running at all times.
* additional support to check the health of applications running within PODs and take necessary actions through Liveness and Readiness Probes

# AutoScaling
* Horizontal
    * manual 
        * max this pod can use is 500m, using ` kubectl top pod <pod>` you can monitor usage ( with metrics server running), as it gets to 450, you can manually run `kubectl scale deployment <deployment name> replcas=X` to add pods 
    * automatic in kubernetes
        * _horizontal pod autoscaler_ (HPA) continuously monitors the metrics and increases/decreases the number of pods in a deployment Statefulset or replica set based on the CPU, memory, or custom metrics.
        `kubectl autoscale deployment my-app --cpu-percent=50 --min=1 max=10`
        `kubectl get hpa`

        ``` 
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: my-app
        spec:
          replicas: 1
          selector: 
            matchLabels:
              app: my-app
          template:
            metadata:
              labels: my-app
            spec:
              containers:
                - name: mt-ap
                  image: nginx
                  resources: 
                    requests: 
                      cpu: "250m"
                    limits: 
                      cpu: "500m"
            ```
            ``` 
            apiVersion: autoscaling/v2
            kind: HorizontalPodAutoscaler
            metadata:
              name: my-app-hpa
            spec:
              scaleTargetRef:
                apiVersion: apps/v1
                kind: Deployment
                name: my-app
              minReplicas: 1
              maxReplicas: 10
              metrics:
                - type: Resource
                  resource:
                    name: cpu
                    target:
                      type: utilization
                      averageUtilization: 50
            ```
* Vertical
    * inplace pod resizing
        *  the default behavior is to delete the existing pod, spin up a new pod with the new changes.

    * new in beta: https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/  
    * Autoscaling:
      * `kubectl edit deployment my-app`
      * NOT native to kubectl - must download
           ``` 
            apiVersion: autoscaling.k8s.io/v1
            kind: VeriticalPodAutoscaler
            metadata:
              name: my-app-vpa
            spec:
              scaleTargetRef:
                apiVersion: apps/v1
                kind: Deployment
                name: my-app
              updatePolicy:
                updateMode: "Auto" [off|initial|recreate|auto]
              resourcePolicy:
                containerPolicies:
                  - containerName: "my-app"
                    minAllowed:
                      cpu: "250m"
                    maxAllowed: 
                      cpu: "2"
                    controlledResources: ["cpu"]
            ```