# Compute and networking services of Azure

# Virtual Networking 
* Allow azure resources (Vms, web apps, databases) to communication with each other, users on the internet, on-prem client computers
    * Isolation and segmentation - internet communication - communication between sxure resrouce - communication with on-premise resources - route network traffic - filter network traffic - connect virtual networks - 
* Public / private endpoint support 
    * communication between external / internal resources 
    * public endpoints - public IP address ; accessed from anywhere in the world
    * private endpoints - within a virtual network; private IP address
* Isolation and Segmentation 
    * support multiple isolated virtual networls
    * define a private Iddress apace using public or private IP address ranges
        * ip range only exists within the virtual network and IS NOT internet routable 
        * divide the ip space into subnets and allocate part of the defined address space to names subnets
        * DNS for name resolution
* Internet Communications
    * assign public IP address to Azure resource
    * put resource behind a public load balancer
* Intra Azure resource communication
    * Virtual Networks
        * connect VMS, App Service Environment for Power Apps, Azure Kubernetes Service, and Azure virtual machine scale sets.
    * Service endpoints 
        * connect  Connect to other resource types (sql databases, storage accounts) link mutlitple azure resources to virtual networkd for optimal routing and security
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

* Virtual Private Networks
    * Uses an encrypted tunnel within another network
    * Deployed to connect 2+ trusted private netorks to one another over an untrusted (ie public internet) network
    * traffic is encrypted while traveling (preventing eavesdropping/attacks) and share senstive information 

* VPN Gateways
    * Type of Virtual network gateway
    * Azure VPN Gateway are deployed in dedicated subnet of the virtual network and enable:
        * site-to-site connection Connect on-premise datacenters to virtual network 
        * point-to-site connection  Connect individual devices to virtual networks
        * Network-to-network Cpnnect virtual networks to other virtual networks
    * One VPN Gateway for each virtual netwrork
    * Can Use One VPN Gateway to connet multiple networks (virtual or on-prem)
    * Route or Policy based types
        * Type determines how they determine which traffic needs encyption
        * Policy based: specify statically the IP address of packets that should be encryptedthrough each tunnel
        * Route based: IP routing decrides which tunner interfaces to use when sending packets (prefeerd for on-premise)
            * Connections between virtual networks
            * Point-to-site connections
            * Multisite connections
            * Coexistence with an Azure ExpressRoute gateway

* HighAvaialbility Scenarios
    * Active / Standby
        * Default 
    * Active / Active
    * ExpressRoute Failover
    * Zone Redundant Gateways


* Azure ExpressRoute
> Azure ExpressRoute lets you extend your on-premises networks into the Microsoft cloud over a private connection, with the help of a connectivity provider. This connection is called an ExpressRoute Circuit. With ExpressRoute, you can establish connections to Microsoft cloud services, such as Microsoft Azure and Microsoft 365. This feature allows you to connect offices, datacenters, or other facilities to the Microsoft cloud. Each location would have its own ExpressRoute circuit.

* Azure DNS
> hosting service for DNS domains that provides name resolution by using Microsoft Azure infrastructure. By hosting your domains in Azure, you can manage your DNS records using the same credentials, APIs, tools, and billing as your other Azure services.

