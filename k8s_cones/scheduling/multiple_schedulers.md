## Kubernetes Multiple Schedulars

> default schedular: algorithm that evenly distributes pods considering taints, tolerations, node affinity.. 
> [SchedulerConfig](https://kubernetes.io/docs/reference/scheduling/config/)

* If you require steps prior to scheduling, you can create your own scheduler/s for custom conditions/checks
* A Kubernetes cluster can have multiple schedulers at a time.
* At creation of pod or a deployment, one can direct which specific scheduler to use
    * profile 
    * leaderElection 
        * a mechanism in Kubernetes designed to ensure high availability and prevent conflicts when running multiple instances of the kube-scheduler. When multiple kube-scheduler instances are deployed, leader election guarantees that only one instance actively performs scheduling decisions at any given time, while the others remain in a standby state, ready to take over if the active leader fail
* see them : `kubectl get pods --namespace=kube-system`
* see which schedulers pick up pods: 
```kubectl get events -o wide```
* view logs:
```kubectl logs <scheduler-name> --name-space=kube-system```

```my-scheduler-config.yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
- schedulerName: my-scheduler
leaderElection:
  leaderElect: true
  resoureceName
```

* how to create one?
    * To deploy the Kubernetes kube-scheduler, download the kube-scheduler binary and run it as a service with a set of options.
    `wget https://storage.googleapis.com/kubernetes-release/release/<KUBERNETES_VERSION>/bin/<OS>/<ARCH>/kube-scheduler`
    * For custom: 
        * you may use the same kube-scheduler binary (^) or use one that you might have built for yourself, and change the configs:
        * changing the --kubeconfig
        ```ExecStart=/usr/local/bin/kube-scheduler --kubeconfig=/etc/kubernetes/scheduler.kubeconfig --leader-elect=true --v=2```
    * 99% of the time -> via pods !
        * with kubeadm deployment, all the control plane components run as a pod or a deployment within the cluster
         
         ```pod.yaml
            apiVersion: v1
            kind: Pod
            metadata:
                name: my-custom-scheduler
                namespace: kube-system
            spec:
                containers:
                - command:
                  - kube-scheduler
                  - --address=127.0.0.1
                  - --kubeconfig=/etc/kubernetes/scheduler.conf
                  - --config=/etc/kubernetes/my-scheduler-config.yaml
                  image: k8s.gcr.io/kube-scheduler-amd64:v1.11.3
                  name: kube-scheduler
            ```

            to use:

         ```pod.yaml
            apiVersion: v1
            kind: Pod
            metadata:
                name: mypod
            spec:
                containers:
                - name: mypod
                  image: nginx
                dchedulerName: my-custom-scheduler
            ```