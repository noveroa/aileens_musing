# aileens_musing
## Cambridge, MA

![N|Solid](https://ca.slack-edge.com/T0495HV8H-U01AM69UW3E-ae635702c574-72)


###### uh like man pages?!

```kubectl label --help```
...
Update the labels on a resource.

```

###### common flags
`--dry-run`: By default as soon as the command is run, the resource will be created. 
`--dry-run=client`:  This will not create the resource, instead, tell you whether the resource can be created and if your command is right.
`-o yaml`: This will output the resource definition in YAML format on screen.


###### Create an (NGINX) Pod

```sh kubectl run nginx --image=nginx```

* Generate POD Manifest YAML file (-o yaml). Don't create it(--dry-run)

```kubectl run nginx --image=nginx --dry-run=client -o yaml```

* Create a deployment

```kubectl create deployment --image=nginx nginx```

* Generate Deployment YAML file (-o yaml). Don't create it(--dry-run)

```kubectl create deployment --image=nginx nginx --dry-run=client -o yaml```

* Generate Deployment YAML file (-o yaml). Don’t create it(–dry-run) and save it to a file.

```kubectl create deployment --image=nginx nginx --dry-run=client -o yaml > nginx-deployment.yaml```

* Make necessary changes to the file (for example, adding more replicas) and then create the deployment.

````kubectl create -f nginx-deployment.yaml```

OR

In k8s version 1.19+, wyou can specify the --replicas option to create a deployment with 4 replicas.

```kubectl create deployment --image=nginx nginx --replicas=4 --dry-run=client -o yaml > nginx-deployment.yaml```

###### Service
* Create a Service named redis-service of type ClusterIP to expose pod redis on port 6379

```kubectl expose pod redis --port=6379 --name redis-service --dry-run=client -o yaml```
> this will automatically use the pod's labels as selectors
or
```kubectl create service clusterip redis --tcp=6379:6379 --dry-run=client -o yaml```
> This will not use the pods labels as selectors, instead it will assume selectors as app=redis. You cannot pass in selectors as an option. So it does not work very well if your pod has a different label set. So generate the file and modify the selectors before creating the service

* Create a Service named nginx of type NodePort to expose pod nginx's port 80 on port 30080 on the nodes:

```kubectl expose pod nginx --type=NodePort --port=80 --name=nginx-service --dry-run=client -o yaml```
Or
```kubectl create service nodeport nginx --tcp=80:80 --node-port=30080 --dry-run=client -o yaml```
> This will not use the pods labels as selectors

_Both the above commands have their own challenges. While one of it cannot accept a selector the other cannot accept a node port. I would recommend going with the kubectl expose command. If you need to specify a node port, generate a definition file using the same command and manually input the nodeport before creating the service._

> list out specific fields
``` kubectl get pods --all-namespaces -o wide --field-selector spec.nodeName=<node-name>```

    kubectl get pods  -o wide --field-selector spec.nodeName=node01