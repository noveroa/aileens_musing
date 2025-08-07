# MOnitoring with Azure Monitor

* Azure Monitor Metrics
> Metrics are numerical value collected at predetermined intervals describing a certain aspect of the system (VM performance, utilization, error counts, responses). In Azure, metrics retained for 93 days (generally)

* Azure Monitor Logs
> Recorded system events with timetamp/metadata - at resource level. Logs not collected by default

* Monitoring VM Layers
    * Host Vm - host machine in Azure
        * compute, storage, network resources azure allocates to the VM
        * Basic metrics  - VM availability, CPU usage, OS disk usage, network operatoins, disk operatoins per second 
        * Azure Monitor Logs 
        * Boot Diagnostics
    * Guest Operating System (OS) - windows/linux OS running on the VM host
    * Client Workloads - workloads running on guest OS supporting business applicatoins
    * VM run applications - business application/s
