# Kubernetes - Custom Resource Definitions (CRDs), Controllers


* Custom Resource Definitions (CRDs)?
> CRDs allow you to extend Kubernetes by defining your own custom resources that behave like native Kubernetes objects (Pods, Services, etc.). They enable you to store and retrieve structured data using the Kubernetes API.
* Custom Resource (CR)
    * An instance of a CRD - your actual custom object
* Custom Resource Definition (CRD)
    * The schema that defines the structure of your custom resource
* API Group:
    * Logical grouping of resources (e.g., `apps/v1`, `networking.k8s.io/v1`)

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: databases.example.com
spec:
  scope: Namespaced  <--- scoped or not --->
  group: example.com
  names:
    kind: Database
    plural: databases
    singular: database
    shortNames:
    - db
  versions:
  - name: v1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              engine:
                type: string
                enum: ["mysql", "postgresql", "mongodb"]
              version:
                type: string
              replicas:
                type: integer
                minimum: 1
                maximum: 10
              storage:
                type: string
            required:
            - engine
            - version
          status:
            type: object
            properties:
              phase:
                type: string
              ready:
                type: boolean
              endpoints:
                type: array
                items:
                  type: string
```

### 2. Create a Custom Resource Instance
```yaml
apiVersion: example.com/v1
kind: Database
metadata:
  name: my-app-db
  namespace: default
spec:
  engine: postgresql
  version: "13.7"
  replicas: 3
  storage: "100Gi"
```

# but now how to use that new resource?

* Custom Controllers?
> Custom controllers are programs that watch for changes to custom resources and implement the desired state logic. They follow the _controller pattern_: observe current state → compare with desired state → take action.
* Controller Pattern:
    * Watch
        * Monitor Kubernetes API for resource changes
    * Reconcile
        * Compare current state vs desired state
    * Act
        * Make necessary changes to achieve desired state

```go
package main

import (
    "context"
    "fmt"
    "time"
    
    "k8s.io/client-go/kubernetes"
    "k8s.io/client-go/rest"
    "sigs.k8s.io/controller-runtime/pkg/controller"
    "sigs.k8s.io/controller-runtime/pkg/handler"
    "sigs.k8s.io/controller-runtime/pkg/reconcile"
    "sigs.k8s.io/controller-runtime/pkg/source"
)

// DatabaseReconciler reconciles Database objects
type DatabaseReconciler struct {
    Client kubernetes.Interface
}

// Reconcile implements the reconcile loop
func (r *DatabaseReconciler) Reconcile(ctx context.Context, req reconcile.Request) (reconcile.Result, error) {
    // 1. Fetch the Database instance
    database := &Database{}
    err := r.Client.Get(ctx, req.NamespacedName, database)
    if err != nil {
        return reconcile.Result{}, err
    }
    
    // 2. Check current state vs desired state
    if database.Status.Phase != "Running" {
        // 3. Create necessary resources (StatefulSet, Service, etc.)
        err = r.createDatabaseResources(ctx, database)
        if err != nil {
            return reconcile.Result{}, err
        }
        
        // 4. Update status
        database.Status.Phase = "Running"
        database.Status.Ready = true
        err = r.Client.Status().Update(ctx, database)
    }
    
    return reconcile.Result{RequeueAfter: time.Minute * 5}, nil
}

func (r *DatabaseReconciler) createDatabaseResources(ctx context.Context, db *Database) error {
    // Create StatefulSet, Service, PVC based on database spec
    // Implementation details...
    return nil
}
```

* Common Use Cases for CRDs and Controllers
    * Application Management
        * ArgoCD: `Application` CRD for GitOps deployments
        * Helm: `HelmRelease` CRD for Helm chart management
        * Knative: `Service` CRD for serverless applications
    * Database Management
        * PostgreSQL Operator: `PostgreSQL` CRD
        * MongoDB Operator: `MongoDB` CRD
        * MySQL Operator: `MySQLCluster` CRD
    * Monitoring and Observability
        * Prometheus Operator: `ServiceMonitor`, `Alertmanager` CRDs
        * Jaeger Operator: `Jaeger` CRD for distributed tracing
        * Grafana Operator: `Grafana`, `GrafanaDashboard` CRDs
    *  Networking
        * Istio: `VirtualService`, `DestinationRule` CRDs
        * Ingress Controllers: Custom ingress CRDs
        * Network Policies: Extended networking CRDs

# general
* CRDs extend Kubernetes API with custom resources that store your domain-specific data.
* Custom Controllers implement the business logic that acts on those custom resources to maintain desired state.
* Together, they enable you to build powerful, Kubernetes-native applications and operators that feel like first-class citizens in the Kubernetes ecosystem.
* This pattern is fundamental to the Kubernetes operator ecosystem and enables declarative management of complex applications and infrastructure.
