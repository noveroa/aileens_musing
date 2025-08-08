# Azure Docker & Kubernetes

* Docker
    * Containers
        * loosely isolated environment that allows to build/run software pakcages which include code and all dependencies to run the application reliably in any computing environment - via container images (the units used to distribute the applications)
        * software containerization is an OS-virtualization method to deploy and run containers without a VM - via physcial hardware, in the cloud, on Vms, and across operating systems
        * Containers are an excellent choice when developing software based on microservice architectures. They make efficient use of hardware, provide security features to run multiple instances simultaneously on the same host without affecting each other, and enable a service to be scaled out by deploying more instances.
        * The decoupled design of microservices combined with the atomicity of containers makes it possible to scale out apps that respond to demand
    * Containerization platform to develop, ship, run containers
        * Docker Engine
            * Components configured as a client-server implementations where server and client aree on the same host via REST API
            ![alt text](https://learn.microsoft.com/en-us/training/modules/intro-to-docker-containers/media/2-docker-architecture.svg)

        * Docker Client 
            * CLI or GUI
        * Docker Server
            * Daemon: ```dockerd``` Responds to client requests via Docker REST API, and can interact with other daemons - responsible for tracking lifecycles of the containers
        * Docker Objects
            * resources - ie networks, storage volumes, plugins, other service objects 0 items created and deplpyed as applicable
        * Docker Hub
            * SaaS Focker container registry - repositories used to store and distribure contianer images that are created - public, though there are cloud based (ie Azure Container Registry) and private options as well 
        * Docker Images
            * The unit of distributed application; applicaton code, system binaries, libraries, config files, OS
            * Immutable
            * Host OS
                * the operating system on which the Docker engine runs (linux)
            * Container OS
                * the OS that is part of the packaged image
            * Stackable Unification File System (Unionfs)
                * A filesystem allowing to stack several directories (branches) in such a way as if content is merged, but the content is physically kept seperate thus allowing add/remove branches to build out
            * Base Image
                * Image using the docker _scratch_ image; an empty container image that doesn't create a filesystem layer - it assumes that the application you are running can directly use the host OS kernal
            * Parent Image
                * container image from which to create images
                * Parent vs Base Image
                    * Both are reusable images
                     * Base images allow more control over final image
        * DockerFile
            * Text file container instructions used to build and run the Docker image
                * base/parent image
                * commands to update the base OS, install addditional software
                * build artifacts to include (ie developed application)
                * services to expose (storage/network configurations)
                * command to run when container is launched
    * Managing Docker Containers
        *   Container Configuration Storage
            * Containers are always considered temporary, thus storage is ephemeral and coupled to the underlying host machine
            * Volumes
                A volume is stored on host filesystem at a specific folder location, thus chose a folder where the data won't be modified by non-docker process
                * Docker creates/manages a volume by running _docker volume create_ ; allowing you to create volumes as part of the container-creation process
                * multiple containers can simulatneously use the same volume now mounted on the host machine and will not be removed when container stops using the volume
            * Bind Mount
                * Conceptually similar to volume, but not a specific folder - fole or folder can be mounted; limited when commpared to volumes  (though more performant) depend on the specific folder structure of the host
            * Network Configuration
                * default Docker network config allows for isolating containers on the Docker host
                * bridge network
                    * default config applied to a container when launched without specifying any other network configration (internal, private isolating)
                    * has own IP address and subnet mask, hostname == container name
                    * by default Docker does not publish the container ports, but command can be anabled ```--publish``` flag
                * Host network 
                    * allows container to run on your host network directly - remoes the isolation between host and container at network level
                * Overlay and other network options
                    * Overlay - virtual switch from host so containers on a network can get IP addresses from DHCP ervers or operate with IP addressses from that network segment
                * None Network
                    * disable networking for a container
        * whe to use a Docker coontainer
            * Benefits
                * Efficient use of hardware (not running a vm)
                * Isolation of container
                * Application Portability
                * Appliation Delivery
                * Manage the hosting environment 
                * Cloud deployments
            * Drawbacks
                * Security. -single point of attack
                * Service monitoring 
                
    ![alt text](https://learn.microsoft.com/en-us/training/modules/intro-to-docker-containers/media/4-docker-container-lifecycle-2.png)

    ```sh
    ## images
    # build
    docker build -t temp-ubuntu .
    # list
    docker images
    # remove
    docker rmi temp-ubuntu:version-1.0

    ## containers##
    # show available containers
    docker ps -a
    CONTAINER ID    IMAGE        COMMAND         CREATED       STATUS           PORTS        NAMES
    d93d40cc1ce9    tmp-ubuntu:latest  "dotnet website.dll …"  6 seconds ago    Up  seconds        8080/tcp      happy_wilbur
    33a6cf71f7c1    tmp-ubuntu:latest  "dotnet website.dll …"  2 hours ago   Exited (0) 9 seconds ago            adoring_borg
    # run container
    docker run -d tmp-ubuntu
    # pause the container
    docker pause happy_wilbur
    # restart
    docker restart happy_wilbur
    # stop
    docker stop happy_wilbur
    # remove a container
    docker rm happy_wilbur

    ```