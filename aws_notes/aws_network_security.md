# aws and network security

> Protecting resources helps ensure confidentiality, availabilty, integrity, useability

* Expand networks across aws regions/accounts that can be divided into isolated networks witg segments
    * each network segment represents a routing domain where you can produce additional security layers at the perimeter of each
    * external calls to applications destined for web layer come through the perimter and must pass through a secure devide and access control lists (ACLS)
* Enforce strong security policies to encrypt data and present its integrity accountabilty authenticity across networks
* Inpspect north.south (ingress/egress) traffic - internet connectivity, cross application (quicksight)
* Firewall manager creates rules for difference environments to filter traffic at the perimeter - layer 3/4
* Protect VPC access using endpoints - where identity based control over network resoure=ces and connection of workloads
* guard duty to analyze logs
# considerations
* management/govenernance
* securtity/compliance
* traffic
* shared responsibility
* 3rd party tools


> How can you take advantage of cloud technologies to protect data systems and assets to improve your security posture
* design principles
    * strong *identity foundation* - principle of least privledges, seperation of duties, centralize identity control, eliminate longstanding/static credentials
* *traceablity* - monitor, alert, audit, logs
* security at all layers (edge, voc, LBs, intances...)
* *automate* best practices 
* *protect data* intransit and at rest
* eliminate direct access to data
* pre prepare for security events - incident management, runbooks, disaster recovery plans

# Ares to consider
* foundation
* identity and access management
* detection
* infrastructure
* data protection
* incident response
* application security and access
