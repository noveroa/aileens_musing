## Kubernetes Application Logs

* Create a pod that can run a docker image that called event-simulator, and all that it does is generate random events, simulating a web server, if one wanted to view the logs, use the docker logs command `docker logs <container id> .  The -f option helps us see the live log trail

* so for kubernetes: use a pod file with a kubectl command using the -f optoin to stream the log's life
    * Kubernetes pods can have multiple Docker containers in them, which containers logs would it show? you need to specifiy the name or it will fail
    * `kubectl logs -f event-stimulator-pod event-simulator`
```
apiVersion: v1
kind: Pod
metadata:
  name: event-simulator
spec:
  containers:
  - name: event-simulator
    image: kodekloud/event-simulator
  - name: image-processor
    image: some-image-processor
```

        