# Kubernetes Accounts - Service Accounts

# User Account
* Real humans (developers, administrators, operators)
* Characteristics:
    * Not managed by Kubernetes - No User objects in the API
    * External identity providers - Managed by external systems (LDAP, OIDC, certificates, etc.)
    * Global scope - Not namespaced
    * Long-lived - Typically persistent identities
* Authentication Methods:
    * Client certificates - Most common for kubectl access
    * Bearer tokens - Static tokens (not recommended for production)
    * OIDC tokens - Integration with identity providers (Google, Azure AD, etc.)
    * Webhook authentication - Custom

# Service Accounts
* Applications, pods, and automated processes running in the cluster
* asssociated with a service and token (this proves the identity)
* Characteristics:
    * Managed by Kubernetes - ServiceAccount objects exist in the API
    * Namespaced - Each belongs to a specific namespace
    * Short-lived tokens - Automatically rotated
    * Pod integration - Automatically mounted into pods
* common uses:
    * Application accessing Kubernetes API
    * Monitoring systems (Prometheus, etc.)
    * Ingress controllers
    * Cloud provider integrations

    ```
    apiVersion: v1
    kind: ServiceAccount
    metadata:
        name: my-app-sa
        namespace: production
    ___
    apiVersion: v1
    kind: Pod
    spec:
        serviceAccountName: my-app-sa  # Uses this SA
        containers:
        - name: app
          image: my-app:latest
          # Token automatically mounted at /var/run/secrets/kubernetes.io/serviceaccount/
    ```
* Default behavior:
    * Every namespace gets
        * default ServiceAccount
        * Automatically assigned to pods if no serviceAccountName specified
    * Every pod gets:
        * ServiceAccount token mounted at /var/run/secrets/kubernetes.io/serviceaccount/
        * Contains: token, ca.crt, namespace files

* RBAC Integration
    * account types work with Role-Based Access Control:
   
   * user
   ```
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
        name: jane-admin
    subjects:
    - kind: User
      name: jane
      apiGroup: rbac.authorization.k8s.io
    roleRef:
      kind: ClusterRole
      name: cluster-admin
      apiGroup: rbac.authorization.k8s.io
    ```
    * service account
    ```
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
    name: my-app-binding
       namespace: production
    subjects:
    - kind: ServiceAccount
      name: my-app-sa
      namespace: production
    roleRef:
      kind: Role
      name: pod-reader
      apiGroup: rbac.authorization.k8s.io
      ```