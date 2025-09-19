# Helm
* "package manager for kubernetes"
Helm is the **package manager for Kubernetes** that simplifies the deployment and management of applications on Kubernetes clusters. Think of it like `apt` for Ubuntu, `yum` for RHEL, or `npm` for Node.js - but for Kubernetes applications.
* Key Problems Helm Solves:
     * Complex YAML Management - Eliminates managing dozens of Kubernetes YAML files
     * Configuration Management - Handles different environments (dev, staging, prod)
     * Application Lifecycle - Streamlines install, upgrade, rollback, and uninstall operations
     * Dependency Management - Manages application dependencies automatically
     * Versioning - Tracks application versions and deployment history

## Core Concepts
* Charts
     * Definition - Packaged Kubernetes applications
     * Structure - Collection of YAML templates with metadata
     * Analogy - Like a recipe that defines how to deploy an application
     * Contents - Deployments, Services, ConfigMaps, Secrets, etc.

```
mychart/
├── Chart.yaml          # Chart metadata
├── values.yaml         # Default configuration values
├── charts/             # Chart dependencies
└── templates/          # Kubernetes YAML templates
    ├── deployment.yaml
    ├── service.yaml
    └── ingress.yaml
```
* Releases
     * Definition - An instance of a chart deployed to a Kubernetes cluster
     * Analogy - Like installing a specific version of an application
     * Features - Each release has a unique name and can be managed independently
     * History - Helm tracks release history for rollbacks
*  Repositories
     * Definition - Collections of Helm charts stored remotely
     * Purpose - Share and distribute charts across teams/organizations
     * Examples - 
        * Artifact Hub (public charts)
        * Private company repositories
        * Cloud provider repositories (AWS, GCP, Azure)
*  Values
     * Definition - Configuration parameters that customize chart behavior
     * Flexibility - Same chart can be deployed with different configurations
     * Sources - Default values, custom values files, command-line overrides

## Helm Architecture
* Helm 3 Architecture (Current)
     * Client-Only - Helm runs as a client-side tool only
     * No Tiller - Removed server-side component (Tiller) from Helm 2
     * Direct API - Communicates directly with Kubernetes API server
     * Improved Security - Uses Kubernetes RBAC and user permissions
* How Helm Works:
    * Template Rendering - Combines chart templates with values
    * Kubernetes API Calls - Sends rendered YAML to Kubernetes
    * Release Tracking - Stores release information as Kubernetes secrets
    * State Management - Tracks what's deployed and manages updates

## Basic Helm Commands
* Repository Management
```bash
# Add a chart repository
helm repo add bitnami https://charts.bitnami.com/bitnami

# Update repository information
helm repo update

# List repositories
helm repo list

# Search for charts
helm search repo nginx
```

* Chart Operations
```bash
# Install a chart
helm install my-nginx bitnami/nginx

# Install with custom values
helm install my-app ./mychart -f custom-values.yaml

# Upgrade a release
helm upgrade my-nginx bitnami/nginx --version 2.1.0

# Rollback a release
helm rollback my-nginx 1
```

* Release Management
```bash
# List releases
helm list

# Get release status
helm status my-nginx

# View release history
helm history my-nginx

# Uninstall release
helm uninstall my-nginx
```

## Helm Chart Structure Deep Dive

* Chart.yaml Example
```yaml
apiVersion: v2
name: my-application
description: A Helm chart for my application
type: application
version: 0.1.0        # Chart version
appVersion: "1.16.0"  # Application version
dependencies:
  - name: postgresql
    version: 11.6.12
    repository: https://charts.bitnami.com/bitnami
```

* values.yaml Example
```yaml
replicaCount: 1

image:
  repository: nginx
  tag: "1.21"
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: false
  className: ""
  annotations: {}
  hosts:
    - host: chart-example.local
      paths:
        - path: /
          pathType: Prefix

resources:
  limits:
    cpu: 100m
    memory: 128Mi
  requests:
    cpu: 100m
    memory: 128Mi
```

* Template Example
```yaml
# templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "mychart.fullname" . }}
  labels:
    {{- include "mychart.labels" . | nindent 4 }}
spec:
  {{- if not .Values.autoscaling.enabled }}
  replicas: {{ .Values.replicaCount }}
  {{- end }}
  selector:
    matchLabels:
      {{- include "mychart.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      labels:
        {{- include "mychart.selectorLabels" . | nindent 8 }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
            - name: http
              containerPort: 80
              protocol: TCP
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
```

## Common Use Cases
* Application Deployment
```bash
# Deploy WordPress with MySQL
helm install my-wordpress bitnami/wordpress \
  --set wordpressUsername=admin \
  --set wordpressPassword=password \
  --set mariadb.auth.rootPassword=secretpassword
```
* Environment-Specific Deployments
```bash
# Development environment
helm install myapp ./chart -f values-dev.yaml

# Production environment
helm install myapp ./chart -f values-prod.yaml
```
* CI/CD Integration
```bash
# In CI/CD pipeline
helm upgrade --install myapp ./chart \
  --set image.tag=${BUILD_NUMBER} \
  --wait --timeout=300s
```

## Advanced Features
* Hooks
     * Purpose - Execute actions at specific points in release lifecycle
     * Types - pre-install, post-install, pre-upgrade, post-upgrade, pre-delete, post-delete
     * Use Cases - Database migrations, backup creation, cleanup tasks
* Subcharts and Dependencies
     * Subcharts - Include other charts as dependencies
     * Management - Automatic dependency resolution and installation
     * Override - Parent chart can override subchart values

* 3. Chart Testing
```bash
# Run chart tests
helm test my-release

# Test with cleanup
helm test my-release --cleanup
```

* 4. Dry Run and Debug
```bash
# See what would be installed
helm install myapp ./chart --dry-run --debug

# Template rendering only
helm template myapp ./chart
```

## Best Practices
* Chart Development
     * Use semantic versioning for charts
     * Provide meaningful defaults in values.yaml
     * Include resource limits and requests
     * Use labels and selectors consistently
     * Document values and templates
* Values Management
     * Separate values files for different environments
     * Use meaningful value names that are self-documenting
     * Validate required values using templates
     * Keep sensitive data in Kubernetes secrets
* Security
     * Use RBAC to control Helm permissions
     * Scan charts for security vulnerabilities
     * Use signed charts when possible
     * Avoid privileged containers unless necessary
* Operational
     * Test charts before deploying to production
     * Use version pinning for dependencies
     * Monitor release health after deployments
     * Plan rollback strategies for critical applications

## Popular Helm Charts
* Infrastructure
     * nginx-ingress - Ingress controller
     * cert-manager - TLS certificate management
     * prometheus - Monitoring stack
     * grafana - Visualization and dashboards

* Databases
     * postgresql - PostgreSQL database
     * mysql - MySQL database
     * mongodb - MongoDB database
     * redis - Redis cache

* Applications
     * wordpress - Content management system
     * jenkins - CI/CD platform
     * gitlab - DevOps platform
     * nextcloud - File sharing platform

## Helm vs Alternatives
* Helm vs Raw YAML
     * Pros - Templating, reusability, lifecycle management
     * Cons - Additional complexity, learning curve

* Helm vs Kustomize
     * Helm - Template-based, package manager approach
     * Kustomize - Overlay-based, patch-oriented approach
     * Use Together - Helm for packaging, Kustomize for environment-specific patches

* Helm vs Operators
     * Helm - Stateless deployment tool
     * Operators - Stateful application lifecycle management
     * Complementary - Use both for complete application management

## Summary

**Helm simplifies Kubernetes application management** by:

     * Packaging - Bundle complex applications into reusable charts
     * Templating - Generate Kubernetes YAML from templates and values
     * Lifecycle Management - Install, upgrade, rollback, and uninstall applications
     * Dependency Management - Handle application dependencies automatically
     * Version Control - Track application versions and deployment history

**Key Benefits:**
- Reduces complexity of managing multiple Kubernetes YAML files
- Enables consistent deployments across environments
- Facilitates application sharing and reuse
- Provides powerful templating and configuration management
- Integrates well with CI/CD pipelines

Helm has become the de facto standard for managing Kubernetes applications, making it an essential tool for anyone working with Kubernetes at scale.