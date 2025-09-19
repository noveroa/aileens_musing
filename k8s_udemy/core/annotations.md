# Kubernetes Annotations
> Annotations are like sticky notes you put on your Kubernetes resources. They store extra information that tools, controllers, or humans might need, but Kubernetes itself doesn't use for core functionality.

* Annotations vs Labels

| Feature | Labels | Annotations |
|---------|--------|-------------|
| Purpose | Selection & grouping | Metadata & configuration |
| Used by Kubernetes | Yes (selectors) | No (tools only) |
| Size limit | 63 characters | 256KB |
| Format | Key-value pairs | Key-value pairs |
| Example | `app: web` | `deployment.kubernetes.io/revision: "3"` |

* Use Cases
* Tool Configuration 
```yaml
metadata:
  annotations:
    # Ingress controller settings
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    
    # Certificate manager
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
```
* Deployment Information
```yaml
metadata:
  annotations:
    # Deployment tracking
    deployment.kubernetes.io/revision: "5"
    kubectl.kubernetes.io/last-applied-configuration: "{...}"
    
    # Build information
    build.version: "v2.1.0"
    build.commit: "abc123"
    build.date: "2024-01-15"
```

* Documentation & Context
```yaml
metadata:
  annotations:
    # Human-readable information
    description: "Frontend web application for user dashboard"
    maintainer: "platform-team@company.com"
    runbook: "https://wiki.company.com/app-runbook"
    
    # Change information
    change.ticket: "JIRA-1234"
    change.reason: "Security patch update"
```

* Resource Management
```yaml
metadata:
  annotations:
    # Resource requirements
    cluster-autoscaler.kubernetes.io/safe-to-evict: "true"
    
    # Backup configuration
    backup.kubernetes.io/enabled: "true"
    backup.kubernetes.io/schedule: "0 2 * * *"
```

* Ingress with Annotations
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-ingress
  annotations:
    # NGINX configuration
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/proxy-body-size: "50m"
    nginx.ingress.kubernetes.io/rate-limit: "100"
    
    # SSL configuration
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  # ... rest of ingress config
```

* Service with Load Balancer Annotations
```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
  annotations:
    # AWS Load Balancer configuration
    service.beta.kubernetes.io/aws-load-balancer-type: "nlb"
    service.beta.kubernetes.io/aws-load-balancer-scheme: "internet-facing"
    
    # Azure Load Balancer configuration
    service.beta.kubernetes.io/azure-load-balancer-resource-group: "my-rg"
```

* Pod with Monitoring Annotations
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-app
  annotations:
    # Prometheus monitoring
    prometheus.io/scrape: "true"
    prometheus.io/port: "8080"
    prometheus.io/path: "/metrics"
    
    # Documentation
    description: "Main web application pod"
    owner: "frontend-team"
spec:
  # ... pod spec
```

* Common Commands
    * Adding Annotations
    ```bash
    # Add annotation to a resource
    kubectl annotate pod my-pod description="Frontend application pod"

    #Add multiple annotations
    kubectl annotate service my-service \
    prometheus.io/scrape=true \
    prometheus.io/port=8080
    ```

    * Viewing Annotations
    ```bash
    # See all annotations
    kubectl get pod my-pod -o yaml | grep -A 10 annotations:

    # Get specific annotation
    kubectl get pod my-pod -o jsonpath='{.metadata.annotations.description}'

    # Describe shows annotations
    kubectl describe pod my-pod
    ```

    * Removing Annotations
    ```bash
    # Remove annotation (note the minus sign)
    kubectl annotate pod my-pod description-

    # Remove multiple annotations
    kubectl annotate pod my-pod prometheus.io/scrape- prometheus.io/port-
    ```
    * Other
    ```bash
    # Add annotation
    kubectl annotate <resource-type> <resource-name> key=value

    # View annotations
    kubectl get <resource-type> <resource-name> -o yaml

    # Remove annotation
    kubectl annotate <resource-type> <resource-name> key-
    ```

* Common Annotation Namespaces

| Prefix | Used For | Examples |
|--------|----------|----------|
| `kubernetes.io/` | Core Kubernetes | `kubernetes.io/os: linux` |
| `k8s.io/` | Kubernetes ecosystem | `k8s.io/cluster-autoscaler/enabled` |
| `nginx.ingress.kubernetes.io/` | NGINX Ingress | `nginx.ingress.kubernetes.io/rewrite-target` |
| `prometheus.io/` | Prometheus monitoring | `prometheus.io/scrape: "true"` |
| `cert-manager.io/` | Certificate management | `cert-manager.io/cluster-issuer` |

* Quick Reference
    * Syntax
```yaml
metadata:
  annotations:
    key1: "value1"
    domain.com/key2: "value2"
    very-long-key-name: |
      This is a multi-line
      annotation value that
      can contain lots of text
```
