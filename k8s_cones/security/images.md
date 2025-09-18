# Kubernetes Images and Security

* Image Review
    * images are lightweight, standalone packages that contain everything needed to run an application / blueprint
        * Application code
        * Runtime environment
        * System libraries
        * Dependencies
        * Configuration files
    * Basics again
        * A _pod_ is the smallest deployable unit in Kubernetes
        * Each pod contains one or more containers
        * Each container is created from a container image
        * Images are pulled from container registries (like Docker Hub, Amazon ECR, Google Container Registry)
    * Image name structure 
        * `[registry]/[namespace]/[repository]:[tag]`
            * if no registry - assumed `docker.io`
        * ie: `nginx:latest` (Docker Hub, default registry)
            * tags: specific versions
   *  Image Pull Policy
    * determines when to download images:
        * `Always` - pull image every time pod starts
        * `IfNotPresent` - only pull if not already on node (default)
        * `Never` - never pull, use local image only

```
apiVersion: v1
kind: Pod
metadata:
  name: my-app-pod
spec:
  containers:
  - name: my-app-container
    image: nginx:1.21        # Image name and tag
    ports:
    - containerPort: 80
    imagePullPolicy: Always
```



# Security
* You can use private docker registries rather than the public.
* point image to the registry via image name construct.
* You need to authenticate
    * create a secret in kubectl with the credentials for the private docker registry.
    ` kubectl create secret my-docker-registry regcred --docker-server="" --docker-username='' --docker-password='' --docker-email=''`
For private registries, you need authentication - using secret in the section : `spec.imagePullSecrets` of the pod
```yaml
spec:
  imagePullSecrets:
  - name: my-docker-registry
  containers:
  - name: my-app
    image: private-registry.com/my-app:v1.0
```

# Security Considerations
* Base Images
    * Use minimal base images (Alpine, Distroless)
    * Avoid images with unnecessary packages
    * Regularly update base images
* Image Scanning
    * Scan images for vulnerabilities before deployment
    * Use tools like Trivy, Clair, or registry-built-in scanners
* Image Signing and Verification
    * Sign images to ensure authenticity
    * Use admission controllers to verify signatures
* Resource Limits
Always set resource limits when using images:
```yaml
spec:
  containers:
  - name: my-app
    image: my-app:v1.0
    resources:
      limits:
        memory: "512Mi"
        cpu: "500m"
      requests:
        memory: "256Mi"
        cpu: "250m"
```
* Best Practices
    * Image Management
        * Use specific tags**, avoid `latest` in production
        * Keep images small - use multi-stage builds
        * Scan for vulnerabilities regularly
        * Use immutable tags or image digests for production

* Example with Image Digest
```yaml
spec:
  containers:
  - name: my-app
    image: nginx@sha256:10d1f5b58f74683ad34eb29287e07dab1e90f10af243f151bb50aa5dbb4d62ee
```
* Security Best Practices
    * Run as non-root user
    * Use read-only root filesystem
    * Drop unnecessary capabilities
    * Use network policies

```yaml
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 2000
  containers:
  - name: secure-app
    image: my-app:v1.0
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
        - ALL
```
