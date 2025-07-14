# basics to get started creating the directories, helm takes charge with making default structure for us here... 
```sh
# create a direcrtory for our test application
cd helm_kubernetes/      
# two components, shipping and payments
mkdir -p helm_example/{payments,shipping}
# helm will create the default component/structures for each part
cd helm_example/
helm create payments
helm create shipping
 # charts/ (dependences) 
 # *** templates/  (the deployment dependenies yamls, config yamls..)
 #  .helmignore 
 # **** Chart.yaml   (meta data of chart (version ... ))
 # *** values.yaml ( any customization of the deployment yaml templates - ie prod vs. dev)

## Step 2: Since we just need an iage, the docker BusyBox is used... the template follows for the deployment.yaml template file for the BusyBox service:

### BusyBox Deployment Template:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}-{{ .Chart.Name }}
  labels:
    app: {{ .Chart.Name }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .Chart.Name }}
  template:
    metadata:
      labels:
        app: {{ .Chart.Name }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: {{ .Values.image.repository }}:{{ .Values.image.tag }}
          command: ['sh', '-c', 'echo {{ .Values.appMessage }}; sleep 3600']
          imagePullPolicy: {{ .Values.image.pullPolicy }}
```

### Values.yaml needs updating too both shipping and payments):

1. Update the `values.yaml` file in the payments chart:

   ```yaml
   image:
     repository: busybox
     tag: latest
     pullPolicy: IfNotPresent
   appMessage: "Payments Service"
   ```

2. Update the deployment template (`templates/deployment.yaml`):

   ```yaml
   spec:
     containers:
       - name: payments
         image: {{ .Values.image.repository }}:{{ .Values.image.tag }}
         command: ['sh', '-c', 'echo {{ .Values.appMessage }}; sleep 3600']
   ```

### Shipping Chart:

1. Update the `values.yaml` file in the shipping chart:

   ```yaml
   image:
     repository: busybox
     tag: latest
     pullPolicy: IfNotPresent
   appMessage: "Shipping Service"
   ```

2. Update the deployment template (`templates/deployment.yaml`):

   ```yaml
   spec:
     containers:
       - name: shipping
         image: {{ .Values.image.repository }}:{{ .Values.image.tag }}
         command: ['sh', '-c', 'echo {{ .Values.appMessage }}; sleep 3600']
   ```

---
***** 
## Step 3: Package the Charts

1. Package the payments chart:

   ```bash
   helm package payments
   Successfully packaged chart and saved it to: /Users/aileennovero/Code/aileens_musing/helm_kubernetes/helm_example/payments-0.1.0.tgz
   ```

2. Package the shipping chart:

   ```bash
   helm package shipping
   ```

3. Create an index file:

   ```bash
   helm repo index .
   ```

---

## Step 4: Host the Helm Repo on GitHub

1. **Create a new GitHub repository:**

   * Name: `helm-repo`

2. **Initialize a Git repo:**

   ```bash
   git init
   git remote add origin https://github.com/username/helm-repo.git
   ```

3. **Push the Helm charts to GitHub:**

   ```bash
   git add .
   git commit -m "Add payments and shipping charts"
   git push -u origin main
   ```

4. **Configure GitHub Pages:**

   * Go to the repo settings.
   * Enable GitHub Pages from the `main` branch.

---

## Step 5: Using the Helm Repo

1. **Add the Helm repo:**

   ```bash
   helm repo add myrepo https://username.github.io/helm-repo
   helm repo update
   ```

2. **Search for charts:**

   ```bash
   helm search repo myrepo
   ```

3. **Install a service (e.g., payments):**

   ```bash
   helm install payments-service myrepo/payments
   ```

---
