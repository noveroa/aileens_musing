# Kubernetes Ingress 
>Ingress is a Kubernetes resource that manages external access to services within a cluster, typically HTTP/HTTPS traffic. It acts as a reverse proxy and load balancer, providing a single entry point for multiple services.

* Without Ingress, you would need:
    * Multiple LoadBalancer services (expensive in cloud environments)
    * NodePort services (exposes random high ports)
    *  Manual load balancer configuration
* With Ingress, you get:
    * Single entry point for multiple services
    * Path-based routing (`/app1`, `/app2`)
    * Host-based routing (`app1.example.com`, `app2.example.com`)
    * SSL/TLS termination
    * Cost efficiency (one load balancer for multiple services)
* Traffic Flow
    ```
    Internet → Load Balancer → Ingress Controller → Service → Pod
    ```
    * External traffic hits the load balancer
    * Load balancer forwards to Ingress Controller
    * Ingress Controller evaluates rules and routes to appropriate Service
    * Service forwards to backend Pods
* Components
    * Ingress Resource
        * Defines the routing rules (what traffic goes where)
    * Ingress Controller
        * The actual implementation that processes Ingress resources and configures the load balancer
            * NGINX Ingress Controller (most popular)
            * Traefik
            * HAProxy
            * AWS ALB Controller
            * GCE Ingress Controller
    * Path Types
        * Exact: Matches the exact path
        * Prefix: Matches based on URL path prefix
        * ImplementationSpecific: Depends on the Ingress Controller

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /app1
        pathType: Prefix
        backend:
          service:
            name: app1-service
            port:
              number: 80
      - path: /app2
        pathType: Prefix
        backend:
          service:
            name: app2-service
            port:
              number: 80
```

* Path-Based Routing
```yaml
rules:
- http:
    paths:
    - path: /api
      backend:
        service:
          name: api-service
    - path: /web
      backend:
        service:
          name: web-service
```

* Host-Based Routing
```yaml
rules:
- host: api.example.com
  http:
    paths:
    - path: /
      backend:
        service:
          name: api-service
- host: web.example.com
  http:
    paths:
    - path: /
      backend:
        service:
          name: web-service
```

* SSL/TLS Configuration

```yaml
spec:
  tls:
  - hosts:
    - myapp.example.com
    secretName: myapp-tls-secret
  rules:
  - host: myapp.example.com
    # ... rest of config
```

* Common Annotations

```yaml
metadata:
  annotations:
    # NGINX specific
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    nginx.ingress.kubernetes.io/proxy-body-size: "50m"
    
    # Certificate management
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
```



* Common Commands

```bash
# View ingresses
kubectl get ingress

# Describe ingress details
kubectl describe ingress <ingress-name>

# Check ingress controller pods
kubectl get pods -n ingress-nginx

# View ingress controller logs
kubectl logs -n ingress-nginx deployment/ingress-nginx-controller
```

* Limitations
    * Only supports HTTP/HTTPS traffic
    * Limited to Layer 7 (Application Layer)
    * Requires an Ingress Controller to be installed
    * Configuration can become complex with many rules