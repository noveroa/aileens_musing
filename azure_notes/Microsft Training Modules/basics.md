# availability
> the importance that resources and services are availabel when needed - high availability focuses on maximizing availabilty regardless of disruptions and use; the up-time, down-time.  Microsoft azure does include availability in service SLAs (increasing sla == increasing cost)

# scalabilty
>  ability to adjust resources to meet demand (ie peak traffic times; cost optimization)
> * vertical - Add/decrease CPUS/RAM specifications to an virtual machine
> * horizontal - for sudden jumps - deploy scaling out (adding/decreasing VMs or containers)

# reliability
> ability for a system to recover from failures and continune to function as expected.  
> With a decentralized design, depoy resources in multiple regions (thus shiftin as needed)

# predictablity
> forward momentum with confidence (performance/cost) 
> * performance - ability to trust the behavior of a resource (autoscaling, load balancing, high availability)
> * cost - track resources in real time, monitoring efficiency, and find patterns to better plan deployments etc

# security - governance/compliance in the cloud
> templates allow deployed resources follow corporate stds and governmental regulatory requirements where applicable; cloud based auditing helps wiht flagging non copliance; software patches/updates can be updated to ensure governamnce/security
> patches / maintaince self service manually or via automation; cloud providers can handle DDoS (distributed denial of service) attacks

# manageability
> automatically scale resources; preconfigure templates for resources minimimixing manual, repetative configurations; health monitoring and automatic replcement; monitoring and alerts for metrics (performance) etc


____________

# Infrastructure as a Service (IaaS)
* most flexible categroy of cloud services - maximum control for your own cloud servies
* cloud provider is responsible to maintaining hardware, network connectivity ( to the internet), and physical security 
* customer is responsible to all else: operating system installations, configurations, maintainance; network configurations,  database/storage configurations. 
* "essentially renting the hardware in a cloud datacenter"

### why iaas?  
> 'Lift and shift' - essentially setting up your cloud environement to mimic one's current on-prem architecture
>  Testing & deployment - You have established configurations for development and test environments that you need to rapidly replicate. You can start up or shut down the different environments rapidly with an IaaS structure, while maintaining complete control.

# Platform as a Service (PaaS)
* middle ground service - between renting space im a datacenter ad paying for a complete/deployed solution
* cloud provider maintains physical infrastrucure, physical security, connection to the internet (like IaaS), but ALSO the operating systems, middleware, dev tools, business intelligence services, patching and licensing
* allow for deployment environment without maintaining development infrastructure.

### why PaaS?
> Development framework - framework provided for developers to build up and customize cloud-based apps with built in software components like scalability, high availabilty, multi-tenancy
> Analytics / business intelligence - tools provided to allow for analyzing/mining data, finding insights/patterns/predictions for improvement, forecasting, design decisions, investment returns .. 

# Software as a Service
* most complete cloud service model (product-wise)
* renting / using a fully developed application (email, finanical software, messaging applications, connectivity services)
* customer responsible for data, devices connected to the system , and user access. 

### why SaaS
> email, messaging, business productivity apps, finance and tracking expenses 