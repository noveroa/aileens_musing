# Kube Config
> kube config file
* the "profile" to connect to kubernetes cluster
` kubectl config view `
` kubectl config use-context <>`

*  settings file that tells your computer how to connect to a Kubernetes cluster.
* Three main sections: 
	* Clusters  
        * information about the Kubernetes cluster (like its server address).
	* Users 
        * authentication details (like tokens or certificates) so you can prove who you are.
	* Contexts 
        * combinations of a cluster + a user + a namespace (kind of like a shortcut).

* When you run kubectl commands, Kubernetes looks at the kubeconfig file to know:
	* Which cluster to talk to
	* Who you are (your credentials)
	* Which namespace to use by default

```
apiVersion: v1
kind: Config
clusters:
- name: my-cluster
  cluster:
    server: https://123.45.67.89:6443
    certificate-authority: /path/to/ca.crt

users:
- name: my-user
  user:
    client-certificate: /path/to/client.crt
    client-key: /path/to/client.key

contexts:
- name: my-context
  context:
    cluster: my-cluster
    user: my-user
    namespace: default

current-context: my-context (the default)
```

* API groups
    * API groups = categories that organize Kubernetes resources
    * organize the different features of the Kubernetes API
	* resources are grouped into API groups
        * Each group is like a folder/category of related resources
    * types:
        * Core group (no name) 
            * basic stuff like pods, services, nodes.
	    * apps 
            * things for running apps : deployments, statefulsets, daemonsets.
	    * batch 
            * jobs and cronjobs.
	    * rbac.authorization.k8s.io 
            * roles and role bindings (for permissions).

    | API Group                     | Example Resources                               |
    |-------------------------------|-------------------------------------------------|
    | **Core (v1)** (no group name) | Pods, Services, Nodes, ConfigMaps, Secrets      |
    | **apps**                      | Deployments, StatefulSets, DaemonSets, ReplicaSets |
    | **batch**                     | Jobs, CronJobs                                  |
    | **rbac.authorization.k8s.io** | Roles, RoleBindings, ClusterRoles               |
    | **networking.k8s.io**         | Ingress, NetworkPolicies                        |
    | **apiextensions.k8s.io**      | CustomResourceDefinitions (CRDs)                |

* Authorization 
    * what can an actor do
    * types : node, rbac, abac, webhook
        * Always Allowed is default

| Authorization Type | Description                                                                 | Typical Use Case |
|--------------------|-----------------------------------------------------------------------------|------------------|
| **Node**           | Grants permissions to kubelets (nodes) so they can interact with the API; use the 'node authorizer'  | Allowing nodes to read pods, secrets, and report status. |
| **RBAC**           | Role-Based Access Control; uses roles and role bindings to control access.  | Most common method for managing user/service permissions - external |
| **ABAC**           | Attribute-Based Access Control; uses policies defined in JSON files.        | Legacy setups or simple clusters (not recommended for new). - external |
| **Webhook**        | Delegates authorization decisions to an external service via HTTP callbacks.| Integrating with custom or enterprise identity systems. |

* RBAC
    * role:
        * scoped to a namespace
        ``` 
        apiVersion: rbac.authorization.k8s.io/v1
        kind: Role
        metadata:
          name: pod-reader
          namespace: default   # Role is namespace-scoped
        rules:
          - apiGroups: [""]      # "" = core API group
        resources: ["pods"]
        verbs: ["get", "list", "watch"]
         ```
    * RoleBinding: now bind the user
        ```
        apiVersion: rbac.authorization.k8s.io/v1
        kind: RoleBinding
        metadata:
          name: read-pods-binding
          namespace: default   # Must match the Role's namespace
        subjects:
        - kind: User
          name: jane           # The user who will get the permissions
          apiGroup: rbac.authorization.k8s.io
          roleRef:
        - kind: Role
          name: pod-reader     # The Role this binding refers to
          apiGroup: rbac.authorization.k8s.io``
        ```
    * ClusterRole
        * A ClusterRole is like a Role, but it’s not limited to a namespace — it can apply across the whole cluster.
        ```
        apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRole
        metadata:
          name: pod-reader
        rules:
         - apiGroups: [""]
           resources: ["pods"]
           verbs: ["get", "list", "watch"]
        ```
    * ClusterRoleBinding
        ```
        apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRoleBinding
        metadata:
          name: read-pods-global
        subjects:
          - kind: User
            name: jane             # The user to bind (could also be a ServiceAccount)
            apiGroup: rbac.authorization.k8s.io
        roleRef:
          kind: ClusterRole
          name: pod-reader       # Must match the ClusterRole name above
          apiGroup: rbac.authorization.k8s.io
        ```