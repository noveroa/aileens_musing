# Compute and networking services of Azure

* Azure Virtual Machines
    * create / use Virtual machines in the cloud, without buying/maintaining physical hardware 
    * provide IaaS via virtualized server 
        * control over operating system (os)
        * run custom software
        * custom hosting configurations
        * cusomtize updates
        * create or use pre-made images
    * scaling
        * Virtual Machine Scale Sets (VMSS)
            * Create / manage a group of identical, load balanced VMs
            * Configured identically
            * Centrally managed, configured, updated
            * Scale in response to demand/schedule
            * load balancing for efficient network utilization
        * Virtual Machine Availability Sets
            * For more resilient, highly available environment
            * Stagger VM updates
            * varied power and network connectivity thus preventing potential data loss with a single network / power faiure
            * Groupings:
                * Domain
                    * Vms can be rebooted at the same time
                    * Apply update knowing only one update domain grouping is offline at a time
                    * All machine sin one domain update
                    * Given 30-minute time to recover before maintainance on next upgate grouping
                * Fault Domain
                    * Group VMs by common power / network switch
                    * default: availabilty set splits VMs across up to 3 fault domains;
                    * protects against physical / netowrking failure
        * VM resources
            * Size - purpose, number of processor cores, RAM
            * Stoage Disks - hard disk drives, solid state drives, etc
            * Networking - virtual network, public IP addressing, port configurations

* Azure Containers
    > VMS can reduce costs (when compared to investing in physical hardware) but limited to a single operating systme per VM; tp run multiple instacnes of an application on a single host machine --> containers
    *   * Virtualized environment
    *   * Run mulitple containers on a single physcial / virtual host
    *   * User does not maintain an OS for a contiaer
    *   * Scale dynamically and on demand
    * Azure Container Apps
        *  ~ Container Instances
        * Remove container management piece (Paas offering) 
        * incorprate load balancing / scaling 
    * Azure Kubernetes Service (AKS)
        * Container rOrchestration Service
        * Manages the lifecycle of Containers
        * Fleet Management
    * In General
        * Containers can be used to split architecture into microservices (front end; back end, storage)

* Azure Functions
    * Event-driven, serverless compute option that doesn’t require maintaining virtual machines or containers.
    * Akin in AWS Lambda
    * just code; no underlying platform / infrastructure
    * respond to events (REST api), schdeulars, message from another Azure service
    * scale automatically based on demand
    * code runs when triggers and deallocates autmaticcalty; azure charges only by cpu time
    * stateful (durable function s - context is passed through the function track priot to activity) or stateless (restart each time respond to an event)

* Application Hosting Options
    * VMs - maximum contraol of the hosting environemt '' allow to configure it exactly as applicable
    * Containers - can isolate and individually manage different aspects of the hosting solution
    * Azure App Service
        * Builf / host web applicaitons, background jobs, mobile back-ends, RESTful APIs without managing infrastructure
        * Autocaling / high availability
        * Windows / Linuz
        * Automated deployments integrated with Github, Azure DevOps, Any Git repo to support CD models
        * HTTP-based service for hosting web applications, REST APIs, and mobile back ends. It supports multiple languages, including .NET, .NET Core, Java, Ruby, Node.js, PHP, or Python.
        * Types of App Services
            * Web Apps
            * API Apps
            * WebJobs (run a program/ background jobs)
            * Mobile Apps
networkd for optimal routing and security
* On Premise communication
    * Point-to-site virtual private network connections - external computer (outside organization) back into corporate network; client compuet intitiates encrypted VPN connection to connect to the azure virtual network
    * Site-to-site virtual private network link on-premise VPN device of gateway to Azure VPN gatewat in a virtual network; azure resource appears as if on local network
    * azure expressroute - dedicated provate connectivity to azure; doesn't travel over internet (for needs of greater bandwidth and security)
* Route Network Traffice
    * default - traffic routed between subnets on any connected vrtual netowrks, on-premis networkd, internet
    * use route tables to define routing directions
    * border gateway protocol (BGP) - 
* Filter Nwtwork Traffice
    * Network Secutiy Groups 
        * contain inbound / outbound security rules
        * allow / block traffic based in source / destination IP address, port, protocol
    * Network virtual appliances
        * specialized VMs coparable to hardened network appliance
        * carries out a particulat network function - running a firewall, performing wide area (WAN) optimization

* Ocnnect virtual networks
    * Virtual network peering - Link virtual networks together
    * Allows two virtual networkd to connect duirectly
    * Traffic is private, travels on microsoft backbone network
    * can be in seperate regions
    * User-defined routes (UDR) allow you to control the routing tables between subnets within a virtual network or between virtual networks. This allows for greater control over network traffic flow.
