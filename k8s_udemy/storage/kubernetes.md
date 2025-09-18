# Kubernetes and storage

* Container Runtime Interface
    * The container runtime interface is a standard that defines how an orchestration solution like Kubernetes would communicate with container runtimes like Docker, and now other vendors
    * no longer bound to docker
    * supports multiple storage solutions with CSI

* Container Storage Interface (CSI) 
    * defines a set of rpcs (remote procedure calls) that will be called by the container orchestrator and these must be implemented by the storage drivers.
    * Example 
        * CSI says that when a pod is created and requires a volume, the container orchestrator in this case Kubernetes should call the create volume RPC and pass a set of details such as the volume name
        * storage driver should implement this RPC and handle that request, and provision a new volume on the storage array and return the results of the operation.

* Volumes
    * containers/pods are transient as is the data
    * by attaching a volume, the pod can terminate and the data persists
    ```yaml
        apiVersion: v1
        kind: Pod
        metadata:
          name: pod
        spec:
          containers:
            - name: pod-app
              image: alpine
              command: ["/bin/sh", "-c"]
              args: ["shuf -i 0-100 -n 1 >> /opt/number.out;"]
              volumeMounts:
              - mountPath: /opt. <--- the host --->
                name: data-volume
          volumes:
          - name: data-volume
          hostPath:
            path: /data
            type: Directory    
        ```
* Persistent Volumes
    * instead of configuring for every pod
    * manage centrally
    * persistent volume is a cluster wide pool of storage volumes configured by an administrator, to be used by users deploying applications on the cluster
    ```yaml
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: my-pv
    spec:
      capacity:
        storage: 1Gi # Defines the size of the volume
      accessModes:
        - ReadWriteOnce # Allows a single node to mount the volume as read-write
      hostPath:
        path: "/mnt/data" # The path on the host node where the data will be stored
      persistentVolumeReclaimPolicy: Retain # Specifies what happens to the volume after the PVC is deleted
    ```
* Persistent Volume Claims
    * to make storage available to a pod
    * volume claims are created, Kubernetes binds the persistent volumes to claims based on the request and properties set on the volume
    * Every persistent volume claim is bound to a single persistent volume
    ```yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: my-claim
    spec:
      resources:
        requests: 
                storage: 500Mi
      accessModes:
        - ReadWriteOnce # Allows a single node to mount the volume as read-write
      ```

* using in resources:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
    - name: myfrontend
      image: nginx
      volumeMounts:
      - mountPath: "/var/www/html"
        name: mypd
  volumes:
    - name: mypd
      persistentVolumeClaim:
        claimName: my-claim
 ```

 * Storage Classes
    * static storage: storage manually provisioned before using
    * dynamic storage allowed by using storage classes
    * replaces PV
        ``` yaml
        apiVersion: storage.k8s.io/v1
        kind: StorageClass
        metadata:
          name: standard-storage
        provisioner: csi.example.com # Replace with your actual CSI provisioner (e.g., ebs.csi.aws.com, disk.csi.azure.com)
        volumeBindingMode: Immediate
        reclaimPolicy: Delete
        parameters:
          type: gp2 # Example parameter for AWS EBS; adjust based on your provisioner
          fsType: ext4 # Example parameter for filesystem type
        ```
    * the pvc ->
    ```yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: my-claim
    spec:
      storageClassName: standard-storage
      resources:
        requests: 
                storage: 500Mi
      accessModes:
        - ReadWriteOnce # Allows a single node to mount the volume as read-write
      ```