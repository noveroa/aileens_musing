# Kustomize Kustomize?
Kustomize is a _configuration management tool_ for Kubernetes that lets you customize YAML configurations without templates. It uses an _overlay and patch approach_ to modify base Kubernetes manifests for different environments.

# Overview
* "Configuration as Data" - Treat Kubernetes YAML as data, not code
* No Templates - Pure YAML manipulation without templating languages
* Declarative - Define what you want, not how to get there
* Built into kubectl - Native Kubernetes integration (`kubectl apply -k`)

## Core Concepts
* Base
    * Original Kubernetes manifests that define your application
    * Common configuration shared across environments
    * Foundation that other environments build upon
* Overlays
    * Environment-specific modifications to the base
    * Patches and customizations for dev, staging, prod
    * Inherits from base and applies targeted changes

* Kustomization File
    * kustomization.yaml - Configuration file that defines transformations
    * Specifies resources to include and modifications to apply
    * Entry point for Kustomize operations

## Basic Structure

```
project/
├── base/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── kustomization.yaml
└── overlays/
    ├── dev/
    │   ├── kustomization.yaml
    │   └── patch-deployment.yaml
    ├── staging/
    │   ├── kustomization.yaml
    │   └── resource-quota.yaml
    └── prod/
        ├── kustomization.yaml
        ├── hpa.yaml
        └── ingress.yaml
```

## Simple Example

### Base Configuration
```yaml
# base/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myapp:latest
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
```

```yaml
# base/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
- deployment.yaml
- service.yaml

commonLabels:
  app: myapp
  version: v1
```

### Production Overlay
```yaml
# overlays/prod/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

namespace: production

resources:
- ../../base
- hpa.yaml

patchesStrategicMerge:
- patch-deployment.yaml

images:
- name: myapp
  newTag: v2.1.0

replicas:
- name: myapp
  count: 5

commonLabels:
  environment: production
```

```yaml
# overlays/prod/patch-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  template:
    spec:
      containers:
      - name: myapp
        resources:
          requests:
            memory: "128Mi"
            cpu: "500m"
          limits:
            memory: "256Mi"
            cpu: "1000m"
```

## Common Kustomize Operations

### 1. Built-in Transformers
```yaml
# kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
- base

# Change namespace for all resources
namespace: my-namespace

# Add common labels to all resources
commonLabels:
  team: backend
  env: prod

# Add common annotations
commonAnnotations:
  managed-by: kustomize

# Add prefixes/suffixes to resource names
namePrefix: prod-
nameSuffix: -v2

# Update image tags
images:
- name: nginx
  newTag: 1.21.0
- name: myapp
  newName: registry.company.com/myapp
  newTag: v2.0.0

# Set replica counts
replicas:
- name: frontend
  count: 3
- name: backend
  count: 5
```

### 2. ConfigMap and Secret Generators
```yaml
# kustomization.yaml
configMapGenerator:
- name: app-config
  literals:
  - DATABASE_URL=postgresql://localhost/mydb
  - DEBUG=false
- name: app-properties
  files:
  - application.properties
  - logging.conf

secretGenerator:
- name: app-secrets
  literals:
  - password=secret123
  - api-key=abc123
- name: tls-secret
  files:
  - tls.crt
  - tls.key
  type: kubernetes.io/tls
```

### 3. Patches
```yaml
# Strategic Merge Patches
patchesStrategicMerge:
- patch-deployment.yaml
- patch-service.yaml

# JSON 6902 Patches
patchesJson6902:
- target:
    group: apps
    version: v1
    kind: Deployment
    name: myapp
  path: patch-replicas.yaml

# Inline patches
patches:
- patch: |-
    - op: replace
      path: /spec/replicas
      value: 3
  target:
    kind: Deployment
    name: myapp
```

## Commands

### Basic Usage
```bash
# Build and view the result
kustomize build overlays/prod

# Apply directly
kubectl apply -k overlays/prod

# Build and save to file
kustomize build overlays/prod > deployment.yaml

# Validate
kustomize build overlays/prod --validate
```

### With kubectl (Built-in)
```bash
# Apply using kubectl's built-in kustomize
kubectl apply -k overlays/prod

# Dry run
kubectl apply -k overlays/prod --dry-run=client -o yaml

# Delete
kubectl delete -k overlays/prod
```

# Features
* Component
    * Reusable pieces that can be included in multiple kustomizations
    * Mix-and-match approach for common functionality

```yaml
# components/monitoring/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1alpha1
kind: Component

resources:
- servicemonitor.yaml
- prometheusrule.yaml
```
* Replacements
    * Variable substitution across resources
    * Dynamic value injection based on other resource fields

```yaml
replacements:
- source:
    kind: Service
    name: myapp-service
    fieldPath: metadata.name
  targets:
  - select:
      kind: Ingress
    fieldPaths:
    - spec.rules.[name=myapp].http.paths.[path=/].backend.service.name
```
* Generators
    * Custom resource generation using plugins
    * Helm chart integration with Helm generator

## Kustomize vs Helm

| Feature | Kustomize | Helm |
|---------|-----------|------|
| Approach | Overlay/Patch | Template |
| Complexity | Simpler | More complex |
| Learning Curve | Easier | Steeper |
| Packaging | No packages | Charts |
| Dependencies | Limited | Rich dependency management |
| Templating | No templating | Rich templating |
| Integration | Built into kubectl | Separate tool |
| Use Case | Environment variants | Application packaging |

## Best Practices
* Directory Structure
```
app/
├── base/                    # Common resources
│   ├── deployment.yaml
│   ├── service.yaml
│   └── kustomization.yaml
├── components/              # Reusable components
│   ├── monitoring/
│   └── security/
└── overlays/               # Environment-specific
    ├── dev/
    ├── staging/
    └── prod/
```
* Keep It Simple
     * Use built-in transformers when possible
     * Avoid complex patches that are hard to understand
     * Prefer strategic merge over JSON patches
     * Use components for reusable functionality
* Organization
     * One application per kustomization
     * Keep bases generic and overlays specific
     * Use meaningful names for patches and resources
     * Document complex transformations

## Common Use Cases

### 1. Multi-Environment Deployments
```bash
# Development
kubectl apply -k overlays/dev

# Production with different configs
kubectl apply -k overlays/prod
```

* Feature Flags
```yaml
# Enable monitoring component conditionally
components:
- ../../components/monitoring  # Only in prod overlay
```

* GitOps Integration
```yaml
# ArgoCD Application
spec:
  source:
    path: overlays/prod
    repoURL: https://github.com/company/app-config
```

## Summary
* Kustomize is ideal for:
     * Environment-specific configurations without templates
     * Teams comfortable with YAML and patch-based modifications
     * Simple to moderate complexity applications
     * GitOps workflows with clear environment separation
     * Kubernetes-native approach using built-in tools

* Key Benefits:
    * No templating complexity - Pure YAML
    * Built into kubectl - No additional tools
    * Clear inheritance model - Base + overlays
    * Kubernetes-native - Fits well with K8s ecosystem
    * Version control friendly - Easy to diff and review

Use Kustomize when you need environment-specific configurations with a simple, patch-based approach rather than complex application packaging.
