

# aileens_musing

## Cambridge, MA

![N|Solid](https://ca.slack-edge.com/T0495HV8H-U01AM69UW3E-ae635702c574-72)

###### 
So obviously, containers are a significant concept to understand and thus ...

But when asked "What is a container?"  Do you freeze... I'm like... Its the package that is a standalone of your application ready to be shipped (duh, the name, docker and container!) and *ensures that no matter where it is shipped/deployed it will run the same regardless*...

  But, probably not the most elegant way to answer...

## A container is a standalone, executable package of software that includes:
* The application code
* Runtime
* Libraries
* Environment variables
* Configuration files



## Key Ideas
* Images
    * Snapshot of a container with everything needed to run the app.
    * They create containers.
    * THE BLUEPRINT
* Containers
    * Running instance of an image.
    * Isolated from other processes on the host.
    * Lightweight (shares the host OS kernel, *unlike virtual machines*).
* Docker
    * The most popular container platform.
    * Offers tools to build, run, and manage containers.
    * Uses a Dockerfile to define how an image is built.
* Container Orchestration
    * Tools to manage large numbers of containers (ie Kubernetes; DockerSwarm)
        * Scaling
        * Load balancing
        * Rolling updates
        * Self-healing
* Isolation
    * Containers provide process and file system isolation using OS features like namespaces and cgroups.
    * Each container has its own network interface, filesystem, and runtime environment.


## Use Cases
* Microservices architecture
* CI/CD pipelines
* Testing and QA
* Cloud-native applications
* Dev/prod parity

```sh 
# example Dockerfile
# Use base image
FROM node:18

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN npm install

# Start app
CMD ["npm", "start"]
```