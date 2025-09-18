## Kubernetes Namespaces

> "houses" in kubernetes; ie there are two 'Marks' (Mark Smith and Mark Williams) who live at different houses.  Within the house, family members talk to each other by their first names; otherwise otherwise they are differentitated by their last names, Mark Smith and Mark Williams.  Each house has their own set of rules and define who does what.  Each has thier own set of resources they can consume.

* _default_ when a cluster is set up, there is the automatic namespace default'
* _kube-system_ when kubernetes spins up initially, some pods and services for internal purposes ( ie those needed for netowrkign solutions, dns services...). To isolate these from the user and preventing the user to delete/modify the services, K8s created them under the name space kube-system.
* _kube-public_ a third automatically created namespace by kubernetes. It should be used to create resources that should be made available to all users.

* use namespaces when your environemnt or the need for isolated resources or for consumption, ie dev / prod 
    * name spaces can have its own set of policies that define who can do what.
    * assign quota of resources
    * resources within the same namesspace can communicate by just names
    * resources communication to resources in another namespace, just flag the namesspace 


```kubectl get pods # only show pods in the current namespace```
```kubectl get pods -namespace=kube-sytem # show the pods in the given space```
```kubectl get pods --all-namespaces ```

```namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
    name: dev
```
```kubectl ccreate - f namespace.yaml```

###### resource limits / quotas

```compute-quota.yaml
apiVersion: v1
kind: ResourceQuota
metadata:
    name:compute-quota
    namespace: dev
spec:
    hard:
        pods: "10"
        requests.cpu: "4"
        requests.memory: 5Gi
        limits.cpu: "10"
        limits.memory: 10Gi
```