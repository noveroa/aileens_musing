# Kubernetes Networking

* Requirement:  all levels within a cluster need to communicate
     * Pod Level: Individual apartments (containers)
     * Service Level: Building directory (how to find apartments)
     * Ingress Level: Building entrance (how outsiders get in)

* Pods
    * Pod Networking
        * Every Pod gets its own IP address
        * Containers in the same Pod share the same IP  
        * Pods can talk to other Pods directly (flat network)
    * Keys
        * Pods are ephemeral (IP changes when Pod dies)
        * All containers in a Pod share: IP, storage, network namespace
        * No NAT needed between Pods
* Services 
    * Services solve the "how do I find Pods?" problem since Pod IPs change.
    * Types of Services:

        | Service Type | Purpose | Use Case |
        |-------------|---------|----------|
        | ClusterIP | Internal only | Database, internal APIs |
        | NodePort | External via node ports | Development, testing |
        | LoadBalancer | Cloud load balancer | Production external access |
        | ExternalName | DNS alias | External service integration |

* Networking Components
    * Container Network Interface (CNI)
        * The "plumbing" that connects Pods to the network.
        * Popular CNI Plugins:
            * Flannel: Simple overlay network
            * Calico: Network policies + routing
            * Weave: Mesh networking
            * Cilium: eBPF-based (advanced)
    * DNS in Kubernetes
        * Every cluster has a DNS service (usually CoreDNS) that:
            * Resolves Service names to IPs
            * Provides service discovery
            * Works automatically (no manual setup needed)

    * Traffic Flow Examples
        * Internal Pod-to-Pod Communication
            ```
            Pod A (10.1.1.2) → Pod B (10.1.1.5)
            Direct communication, no proxy needed
            ```
        * Pod-to-Service Communication
            ```
            Pod A → Service (my-app) → Load Balances → Pod B or Pod C
            Service acts as a load balancer/proxy
            ```
        * External-to-Pod Communication
            ```
            Internet → Ingress → Service → Pod
            or
            Internet → LoadBalancer Service → Pod
            ```


* DNS Names
    ```
    <service-name>.<namespace>.svc.cluster.local
    ```
* Network Policies - The Firewall
    * Network Policies control traffic between Pods (like firewall rules).
        * Example: Only allow traffic from frontend to backend
        ```yaml
        apiVersion: networking.k8s.io/v1
        kind: NetworkPolicy
        metadata:
          name: backend-policy
        spec:
          podSelector:
            matchLabels:
              app: backend
          ingress:
          - from:
            - podSelector:
                matchLabels:
                  app: frontend
        ```

* Common Networking Patterns
    *  Microservices Communication
        ```
        Frontend Service → Backend Service → Database Service
        Each service has multiple Pod replicas
        ```
    * External Access Patterns
        ```
        # Development
        NodePort Service (exposes random port on all nodes)

        # Production  
        Ingress Controller (HTTP/HTTPS routing)
        LoadBalancer Service (Cloud provider LB)
        ```
    *  Service Mesh (Advanced)
        ```
        Pod ↔ Sidecar Proxy ↔ Network ↔ Sidecar Proxy ↔ Pod
        Examples: Istio, Linkerd
        ```

* Troubleshooting Network Issues
    * Common Commands
    ```bash
    # Check services
    kubectl get svc

    # Check endpoints (which Pods are behind a service)
    kubectl get endpoints

    # Check network policies
    kubectl get networkpolicies

    # Test connectivity from a Pod
    kubectl exec -it <pod> -- curl <service-name>

    # DNS debugging
    kubectl exec -it <pod> -- nslookup <service-name>
    ```
    * Common Issues & Solutions

    | Problem | Symptom | Solution |
    |---------|---------|----------|
    | Service not found | DNS resolution fails | Check service name/namespace |
    | Connection refused | Can resolve DNS but can't connect | Check if Pods are running/healthy |
    | Intermittent failures | Sometimes works, sometimes doesn't | Check Pod readiness probes |
    | External access blocked | Can't reach from outside | Check Ingress/LoadBalancer config |

* Key Networking Rules in K8s
    * The Four Fundamental Rules:
        1. Pods can communicate with all other Pods without NAT
        2. Nodes can communicate with all Pods without NAT  
        3. The IP a Pod sees itself as is the same IP others see it as
        4. Services provide stable endpoints for ephemeral Pods



### Network Debugging Pod
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: netshoot
spec:
  containers:
  - name: netshoot
    image: nicolaka/netshoot
    command: ["sleep", "3600"]
```
