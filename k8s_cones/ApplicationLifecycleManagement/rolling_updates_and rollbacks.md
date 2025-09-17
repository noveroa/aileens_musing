## Kubernetes Rolling Updates and Rollbacks

* Each deployment triggers a rollout, with a version number.  As upgrades occur, rollouts continue, incrementing the version.
    * create: `kubectl create -f deployment_definition.yaml`
    * list : `kubectl get deployments`
    * status: `kubectl rollout status <deployment-name>`
* this keeps tracks of changes and allows for rollbacks as necessary.
    * historyL status: `kubectl rollout history <deployment-name>`

* Strategies:
    * Recreate Strategy
        * Destroy all the deployments and then re-deploy; sclae down all to 0
        * Downtime
        * Not default
    * RollingUpdate:
        * Remove and replace one instance at a time; scaling down/up by one 
        * No down time
        * Default deployment strategy
    * RollBacks
        * ` kubectl rollout undo <deployment name>`

    

* Updates:
    * `kubectl apply -f <>.yaml`
    * `kubectl set image <deployment-image>`. <-- but definition file will not be updated




