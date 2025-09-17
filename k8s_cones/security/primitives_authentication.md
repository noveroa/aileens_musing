# Primitives and authentication

* A secure host is crucial
    * root access disabled, password based authentication disabled, and only SSH key based authentication to be made available

* Kubernetes Relares security
    * kube API server is at the center of all operations within Kubernetes _first line of defense_
        * authenticaton - who can access
            * tokens, certificates, LDAP (external auth providers), service acts
        * authorization - what can they access
            * rbac, abac, node authorizarion, webhook mode
    * TLS certs:
        * All communication with the cluster between the various components such as the etcd cluster, the kube controller, manager, scheduler, API server, as well as those running on the worker nodes such as the Kubelet and kube proxy, is secured using TLS encryption
    * Pod - to -pod
        * by default, all pods can access all other pods within the cluster; restrict access between them using network policies.

* Authentication
    * applications
        * Security of end users who access the applications deployed on the cluster is managed by the applications themselves
    * Kubernetes does not manage user accounts natively; relies on an external source, like a file with user details or certificates, or a third party identity service like Ldap to manage these users.
    * kubernetes can create and manage service accounts
    * users
        * all user access is managed by the API server
        * kube API server authenticates the requests before processing it
            * using, un + pw/token,  certificates, third party authentication protocols like Ldap, Kerberos.. , 