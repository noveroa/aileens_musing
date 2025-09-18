# Docker Storage Drivers and Volume Drivers

* Architecture Overview
    * Docker uses a layered storage system with two main components:
    * storage Drivers --> manage container layers and images
    * volume Drivers --> manage persistent data storage

* Storage Drivers (Graph Drivers)
    > Storage drivers control how Docker stores and manages container images and container layers on the host filesystem.
    `docker info | grep "Storage Driver" # Check current storage driver`
    * default storage:
        * /var/lb/docker/ ...
            * aufs (Legacy)
            * containers
            * images
            * volumes
            * data_volume 
    * dockers builds in layered architecture (only updating rebuilding changes and using the cached old)
        * Layer 1 - base ubuntu
        * Layer 2 - changes in apt packages
        * Layer 3 - changes in pip packages
        * Layer 4 - source code
        * Layer 5 - update entry point
    * when a container terminates, all data / changes terminates as well; to revent this - use persistent volumes mounted in the container
        * two types of mounting
            * Volume mount:  mounts a volume from the volumes directory 
            * B ind mount:  mounts a directory from any location
### Storage Driver Selection
```bash
# Configure storage driver in daemon.json
cat /etc/docker/daemon.json
{
  "storage-driver": "overlay2",
  "storage-opts": [
    "overlay2.override_kernel_check=true"
  ]
}
```

* Volume Drivers
    > Volume drivers manage persistent data that survives container lifecycle.
    * *volumes are not handled by storage drivers, but volume driver plugins.
    * default volume driver plugin is local.
        * create a volume on the Docker host and store its data under the `/var/lb/docker/`
    * Built-in Volume Drivers   
        * local (Default)
            * Storage - Host filesystem
            * Use case - Single host deployments
            * Features - Bind mounts, named volumes
            * Limitations - Not shared between hosts
        * tmpfs
            * Storage - Host memory (RAM)
            * Use case - Temporary data, sensitive information
            * Features - Fast access, automatic cleanup
            * Limitations - Data lost on container stop
    * Third-Party Volume Drivers
        * NFS Driver
        * CIFS/SMB Driver
        * Cloud Storage Drivers
            * aws ebs, azure disk, Google Persistent Disk
        * Distributed Storage Drivers

