# Kubernetes Gateway API

Gateways improve upon the idea of Ingress with more supported protocols and routing.


* Problems with Ingress
    * Annotations: Different controllers, different annotations
    * Limited functionality: Only HTTP/HTTPS
    * No separation of concerns: Everything in one resource
    * Vendor lock-in: Controller-specific features

* Gateway API Solutions
    * Standardized: Same API across all implementations
    * Multi-protocol: HTTP, HTTPS, TCP, UDP, gRPC
    * Role-based: Different teams manage different parts
    * Extensible: Built for future protocols and features
    * Type-safe: Strong typing and validation

* Core Concepts
    * GatewayClass: The "template" or "driver" for gateways
        ```yaml
        apiVersion: gateway.networking.k8s.io/v1
        kind: GatewayClass
        metadata:
          name: nginx-gateway-class
        spec:
          controllerName: nginx.org/gateway-controller
        ```
*  Gateway: entry point 
    ```yaml
    apiVersion: gateway.networking.k8s.io/v1
    kind: Gateway
    metadata:
      name: web-gateway
      namespace: default
    spec:
      gatewayClassName: nginx-gateway-class
      listeners:
      - name: http
        port: 80
        protocol: HTTP
      - name: https
        port: 443
        protocol: HTTPS
    tls:
        certificateRefs:
        - name: web-cert
    ```
* HTTPRoute:  The routing rules (where traffic goes)
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: web-route
  namespace: default
spec:
  parentRefs:
  - name: web-gateway
  hostnames:
  - "example.com"
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: "/api"
    backendRefs:
    - name: api-service
      port: 8080
  - matches:
    - path:
        type: PathPrefix
        value: "/"
    backendRefs:
    - name: web-service
      port: 80
```

* Gateway API Resource Types

| Resource | Purpose | Protocol Support |
|----------|---------|-------------------|
| GatewayClass | Gateway template/driver |  All |
| Gateway | Load balancer config |  All |
| HTTPRoute | HTTP routing rules |  HTTP/HTTPS |
| TCPRoute | TCP routing rules | TCP |
| UDPRoute | UDP routing rules |  UDP |
| TLSRoute | TLS routing rules |  TLS |

* Traffic Flow
    ```
    Internet → Gateway (Load Balancer) → HTTPRoute Rules → Service → Pods
    ```
    * Traffic hits Gateway (configured by platform team)
    * Gateway checks HTTPRoute rules (created by app teams)
    * Route rules determine destination Service
    * Service forwards to appropriate Pods

* Popular Gateway Controllers

| Controller | Provider | Features |
|------------|----------|----------|
| Istio Gateway | Istio | Service mesh integration |
| NGINX Gateway | NGINX | High performance |
| Envoy Gateway | Envoy Project | Cloud-native proxy |
| Kong Gateway | Kong | API management focus |

* Troubleshooting Commands

    ```bash
    # Check Gateway status
    kubectl get gateway

    # Check HTTPRoute status  
    kubectl get httproute

    # Describe resources for details
    kubectl describe gateway web-gateway
    kubectl describe httproute web-route

    # Check Gateway controller logs
    kubectl logs -n gateway-system deployment/gateway-controller
    ```
