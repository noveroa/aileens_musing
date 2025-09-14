## Admission Controllers

> Authorization [ Kubectl cmd ] --> [ Authentication - certificates ] ---> [ Authorization - rbac  ] ---> [Create Pod]
* **Admission Controllers** allow access control beyonnd the api level of the rbac roles.
    * help implement better security measures to enforce how a cluster is used.
    * validating configuration, perform additional operations before the pod gets created
    * Kubernetes does have some preBuilt AdminControllers
        * AlwaysPullImages :  every time a pod is created, the images are always pulled
        * DefaultStorageClass : adds default storage class to PVCs if not specified
        * EventRateLimit : limit on the request with the API server to avoid throttling
        * NameSpaceExists: request rejected if namespace doesn't exist
        * to view those that exists:
            `kube-apiserver -h | grep enable-admission-plugins`
            `ps -ef | grep kube-apiserver | grep admission-plugins`
        * To add an admission controller, update the enable admission plugins flag on the Kube API server service to add the new admission controller within the Kube API server manifest file `/etc/kubernetes/manifests/kube-apiserver.yaml`


* Authorization- RBAC
    * most of these rules that you can create with role-based access control, is at the Kubernetes API level,
        ```developer-role.yaml
            apiVersion: rbac.authorization.k8s.io/v1
            kind: Role
            metadata:
            name: developer
            rules:
            - apiGroups: [""]
            resources: ["pods"]
            verbs: ["create"]
            resourceNames: ["name1", "name2"]
            ```
    * how can you go beyond the api level to restric access?
        * ie. reviewing the configuration file : only allow certain images, or blacklist public images, enforce tags

* Validating & Mutating Admission Controllers
    * Types: 
        * Mutating (DefaultStorageClass)
            * change the request
            * generally invoked first, ensuring the change would then be validated
        * Validating (NameSpaceExists)
            * can validate the request and allow or deny it,
        * Admission controllers that can do multiple 'types'

* Now supporting external/custom validating/mutating controllers
    * You configure these webhooks to point to a server that's hosted either within the Kubernetes cluste or outside it, and our server will have our own admission webhook service running with our own code and logic
    * After a request goes through all the built-in admission controllers,  it hits the webhook that's configured
    * this makes a call to the admission webhook server by passing in an AdmissionReview object in a JSON format
        * an object has all the details about the request (user that made the request, type of operation the user is trying to perform, on what objects, metadata)
    * Admission webhook server responds to allow or reject

    * MutatingAdmissionWebhook
    * ValidatingAdmissionWebhook

    * Steps:
        * Deploy a webhook (api server...) with api mutate() and validate()
            * contains the logic / code to permit or reject a request
            * be able to receive and respond with the appropriate responses that the admission webhook expects
        * create a kubernetes validating webhook configuration object.
            ```
            apiVersion: admissionregistratoin.k8s.io/v1
            kind: ValidatingWebhookCongifuration
            metadata:
                name: "pod-policy.example.com"
            webhooks:
            - name: "pod-policy.example.com"
              clientConfig: 
                <url if external>
                service: 
                  namespace: "erbhook-namespace"
                  name: "webhook-service"
                caBundle: "Ci0..."
              rules:
              - apiGroups: [""]
                apiVersiosn: ["v1"]
                operations: ["CREATE"]
                resources: ["pods"]
                scope: "Namespaced"
            ``` 