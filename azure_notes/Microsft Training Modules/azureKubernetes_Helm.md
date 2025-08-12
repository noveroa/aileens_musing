# Azure Docker & Kubernetes

## HELM 
> Helm is a package manager for Kubernetes that combines all your application's resources and deployment information into a single deployment package. The package manager!
* benefits 
    * Repeatable
    * Reliable
    * Manageable in multiple and complex environments
    * Reusable across different development teams
   
* Helm uses four components to manage application deployments on a Kubernetes cluster:
    * Helm client
        * Client Installed Binary responsible for creating and submitting the manifests required to deploy a kubernetes application
        * the interaction between the user and the kubernetes cluster
        ![alt text](https://learn.microsoft.com/en-us/training/modules/aks-app-package-management-using-helm/media/2-helm-components.svg)
    * Helm releases
        * application or group of applications deployed using a chart
    * Helm repositories
        * dedicated HTTP server that stores information on Helm charts. The server hosts a file that describes charts and where to download each chart.
        * The Helm project hosts many public charts, and many repositories exist from which you can reuse charts. Helm repositories simplify the discoverability and reusability of Helm packages.
        * ```helm repo add ```
    * Helm charts
        * Templated deployment package that describes a related set of Kubernetes resources
        * Contains all the information required to build and deploy the manifest files for an application to run on a Kubernetes cluster
        | File / Folder	 | Description |
        | ------         | ------       |
        | Chart.yaml	 | A YAML file containing the information about the chart | 
        | values.yaml	 | 	The default configuration values for the chart | 
        | templates/	 | 	A folder that contains the deployment templates for the chart | 
        | LICENSE	     | 	A plain text file that contains the license for the chart | 
        | README.md	     | 	A markdown file that contains instructions on how to use the chart | 
        | values.schema.json**	 | 	A schema file for applying structure on the values.yaml file | 
        | charts/	     | 	A folder that contains all the subcharts to the main chart | 
        | crds/	         | 	Custom Resource Definitions | 
        | templates/Notes.txt	 | 	A text file that contains template usage notes | 

* HELM Chart
    * one of the required files in a Helm chart definition and provides information about the chart. 
    * The contents of the file consists of three required fields and various optional fields.
    * The three required fields include:
        * apiVersion: The chart API version to use. You set the version to v2 for charts that use Helm 3.
        * name: The name of the chart.
        * version: The version number of the chart, which uses semantic versioning 2.0.0 and follows the MAJOR.MINOR.PATCH version number notation.
        ```sh
        apiVersion: apps/v1
        kind: Deployment
        metadata:
        name: store-front
        spec:
        replicas: {{ .Values.replicaCount }}
        selector:
            matchLabels:
            app: store-front
        template:
            metadata:
            labels:
                app: store-front
            spec:
            nodeSelector:
                "kubernetes.io/os": linux
            containers:
            - name: store-front
                image: {{ .Values.storeFront.image.repository }}:{{ .Values.storeFront.image.tag }}
                ports:
                - containerPort: 8080
                name: store-front
                env: 
                - name: VUE_APP_ORDER_SERVICE_URL
                value: "http://order-service:3000/"
                - name: VUE_APP_PRODUCT_SERVICE_URL
                value: "http://product-service:3002/"
                resources:
                requests:
                    cpu: 1m
                    memory: 200Mi
                limits:
                    cpu: 1000m
                    memory: 512Mi
                startupProbe:
                httpGet:
                    path: /health
                    port: 8080
                failureThreshold: 3
                initialDelaySeconds: 5
                periodSeconds: 5
                readinessProbe:
                httpGet:
                    path: /health
                    port: 8080
                failureThreshold: 3
                initialDelaySeconds: 3
                periodSeconds: 3
                livenessProbe:
                httpGet:
                    path: /health
                    port: 8080
                failureThreshold: 5
                initialDelaySeconds: 3
                periodSeconds: 3
        ---
        apiVersion: v1
        kind: Service
        metadata:
        name: store-front
        spec:
        type: {{ .Values.storeFront.serviceType }}
        ports:
        - port: 80
            targetPort: 8080
        selector:
            app: store-front
    ```
* Values.yaml
    * customize the configuration of a Helm chart
    * predefined value is a case-sensitive value that's predefined in the context of a Helm chart and can't be changed by a user.
    ```sh
    ...
    replicaCount: 1
    ...
    storeFront:
    image:
        repository: "ghcr.io/azure-samples/aks-store-demo/store-front"
        tag: "latest"
    serviceType: LoadBalancer
    ...
    ```