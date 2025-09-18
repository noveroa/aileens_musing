
# general security
* pods
    * Containers are encapsulated in pods
    * can configure the security settings at a container level or at a pod level
        * pod level
            * settings will carry over to all the containers within the pod
        * both the pod and the container, 
            * settings on the container will override
    * security contexts: 
        * pod: `spec.securityContext`
        * container level: `soec.container.securityContext`
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod
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

* Network Security & Policies
    * basics
        * ingress
        * egress
    * given a cluster with a set of nodes hosting a set of pods and services.
        * Each node, pod, and service has an IP address
        * so how do pods communicate
            * if within same vpn (spanning the nodes) - by default all pods can communicate
            * default:  `All Allow` rule: 
                * allows traffic from any pod to any other pod or services within the cluster
    * Network Polcies
        * define rule concerning traffic between pods by rules, etc 
        * Network policies are namespace-scoped
        * Policies are additive - multiple policies can apply to the same pod
        * linked / applied to pods
            * labels and selectors
                ```yaml
                apiVersion: networking.k8s.io/v1
                kind: NetworkPolicy
                metadata:
                  name: db-policy
                spec:
                  policyTypes:
                  - Ingress
                  ingress:
                  - from:
                    - podSelector:
                        matchLabels:
                          name: api-pod
                    ports:
                    - protocol: TCP
                      port: 3306
                  <!-- - Egress -->
                ```
            * protecting a db pod further (ipblock | spec.podSelector | ingress.namespace)
               ```yaml
                apiVersion: networking.k8s.io/v1
                kind: NetworkPolicy
                metadata:
                  name: db-policy
                spec:
                  podSelector:
                    matchLabels:
                      role: db  <!-- how to match pods to apply too -->
                  policyTypes:
                  - Ingress
                  ingress:
                  - from:
                    - podSelector:
                        matchLabels:
                          name: api-pod
                      namespaceSelector:
                        matchLabels:
                          kubernetes.io/metadata.name: my-namespace
                    - ipBlock:
                        cidr: 192.168.5.10/32 <--- range specify a range of IP address from which to allow traffic --->
                    ports:
                    - protocol: TCP
                      port: 3306
                ```