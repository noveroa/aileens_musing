# Kubernetes DNS
 >DNS essentially the phone book - 
* Pods have dynamic IPS thus use dns
```Pod A: 10.244.1.5  →  Pod restarts  →  10.244.2.8```
``` curl http://my-app-service    # Always works!```

* Kubernetes DNS
* CoreDNS : The DNS Server 
    * Every Kubernetes cluster runs CoreDNS (usually in the `kube-system` namespace)
        * Automatic service discovery
        * Resolves service names to IP addresses
        * Updates automatically when services change
        * No manual configuration needed!
* DNS Names in Kubernetes
| Resource | DNS Name Pattern | Example |
|----------|------------------|---------|
| Service | `<service>.<namespace>.svc.cluster.local` | `web.default.svc.cluster.local` |
| Pod | `<pod-ip>.<namespace>.pod.cluster.local` | `10-244-1-5.default.pod.cluster.local` |
| Headless Service | `<pod>.<service>.<namespace>.svc.cluster.local` | `web-0.mysql.default.svc.cluster.local` |

* DNS Resolution Examples
    * Within the Same Namespace
    ```bash
    # All these work from a Pod in 'default' namespace:
    curl http://my-service              # Short name
    curl http://my-service.default      # With namespace  
    curl http://my-service.default.svc  # With svc
    curl http://my-service.default.svc.cluster.local  # Full FQDN
    ```
    *  Across Different Namespaces
    ```bash
    # From 'frontend' namespace calling 'backend' namespace:
    curl http://api-service.backend           # Must specify namespace
    curl http://api-service.backend.svc       # More explicit
    curl http://api-service.backend.svc.cluster.local  # Full FQDN
    ```
    * Pod-to-Pod DNS (Headless Services)
    ```bash
    # For StatefulSets with headless services:
    mysql-0.mysql-service.default.svc.cluster.local
    mysql-1.mysql-service.default.svc.cluster.local  
    mysql-2.mysql-service.default.svc.cluster.local
    ```

* Service Types and DNS Behavior
    * ClusterIP Service (Normal)
        * `web-service.default.svc.cluster.local` → Single ClusterIP
        ```yaml
        apiVersion: v1
        kind: Service
        metadata:
          name: web-service
          namespace: default
        spec:
          type: ClusterIP
          selector:
            app: web
          ports:
          - port: 80
        ```
    * Headless Service
        * : `mysql-headless.default.svc.cluster.local` → Individual Pod IPs
        ```yaml
        apiVersion: v1
        kind: Service
        metadata:
          name: mysql-headless
        spec:
          clusterIP: None  # This makes it headless!
          selector:
            app: mysql
          ports:
          - port: 3306
        ```

* DNS Configuration in Pods
    * Default DNS Settings
        * Every Pod automatically gets:
        ```yaml
        spec:
        dnsPolicy: ClusterFirst
        dnsConfig:
            nameservers:
            - 10.96.0.10  # CoreDNS service IP
            searches:
            - default.svc.cluster.local
            - svc.cluster.local  
            - cluster.local
        ```
    * Custom DNS Configuration
    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: custom-dns-pod
    spec:
      dnsPolicy: None  # Override default DNS
      dnsConfig:
        nameservers:
        - 8.8.8.8
        - 1.1.1.1
        searches:
        - my-company.com
      containers:
        - name: app
          image: nginx
    ```
    * DNS Policies

| Policy | Behavior | Use Case |
|--------|----------|----------|
| **ClusterFirst** | Use cluster DNS first, then upstream | Default for most Pods |
| **None** | Use custom dnsConfig only | Custom DNS requirements |
| **Default** | Use node's DNS settings | Special system Pods |
| **ClusterFirstWithHostNet** | Cluster DNS for hostNetwork Pods | Network utilities |

* Troubleshooting DNS Issues
    * Check DNS Resolution
    ```bash
    # From inside a Pod:
    nslookup kubernetes.default.svc.cluster.local
    nslookup my-service
    dig my-service.default.svc.cluster.local

    # Check if CoreDNS is running:
    kubectl get pods -n kube-system -l k8s-app=kube-dns
    ```

    * Common DNS Debug Pod
    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: dns-debug
    spec:
      containers:
      - name: debug
        image: busybox
        command: ["sleep", "3600"]
    ```

    ```bash
    # Test DNS from debug pod:
    kubectl exec -it dns-debug -- nslookup kubernetes.default
    kubectl exec -it dns-debug -- cat /etc/resolv.conf
    ```

    * DNS Debugging Commands
    ```bash
    # Check CoreDNS configuration
    kubectl get configmap coredns -n kube-system -o yaml

    # Check CoreDNS logs
    kubectl logs -n kube-system -l k8s-app=kube-dns

    # Verify service endpoints
    kubectl get endpoints my-service

    # Check DNS from a Pod
    kubectl run tmp-shell --rm -i --tty --image nicolaka/netshoot
    ```

* Quick Reference Card


```bash
# Short names (same namespace)
my-service
my-service:8080

# Cross-namespace
my-service.other-namespace
my-service.other-namespace:8080

# Full FQDN  
my-service.other-namespace.svc.cluster.local
```

### Essential Commands
```bash
# Test DNS resolution
kubectl exec -it <pod> -- nslookup <service>

# Check CoreDNS status
kubectl get pods -n kube-system -l k8s-app=kube-dns

# View DNS configuration
kubectl exec -it <pod> -- cat /etc/resolv.conf
```
