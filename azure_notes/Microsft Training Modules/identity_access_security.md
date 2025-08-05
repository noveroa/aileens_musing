# Azure identity, access, and security services

* Azure Directory Services - Microsoft Entra Id 
    * Directory service enabling to sign in / access microsoft and your own cloud applications
    * Provisions
        * Authentication - verify identity to access applications and resources 
            * establishing the identity of a person, service, or device.
            * Standard passwords, Single Sign On (SSO), Multofacotr Authentication (MFA - know has is) , passwordless
        * Single Sign On (SSO)
        * Application Management - Applicatoin Proxy, SaaS apps, Apps Portal, SSO
        * Device Management - register useres but also devices
* Microsoft Entra Domain Services
    * managed domain services (domain join, group policy, LDAP,..) 
* Azure external Identities
    * Person, device, service outside customer's organization
    * Business to Business (B2B) - use external user preferred identiry to sign-in to azure application - 'guest users'
    * B2B Direct Connet - Mutal two wat trust with another Microsoft Entra Organization 
    * Microsoft Azure Active Directory business to customer (B2C) 

* Azure Conditional Access 
    * All / Deny access to resources based on identity signals (who user is, where user is, what device user is requesting access from)
* Azure Role Based Access Control (RBAC)
    * Prinicpal of Least Privilege - only grant access up to the level needed to complete a task
    * Azure does provide built in roles with common rules, but you can provide your own roles
    * Hierarchical, in that when you grant access at a parent scope, those permissions are inherited by all child scopes. For example
    * Scopes
        * management group (group of subscriptions)
        * single subscription
        * single resource group
        * single resource
* Zero Trust Model
    * Assumes worst case scenario and protects resources with that expectation
    * Assumes breach at outset and verifies each request as if originating from uncontrolled network
        * Verify Explicitly - always authenticate and authorize with all given data points
        * Least privilege Access
        * Assume Breach - minimize blast radius and segment access
* Defense-in-depth
    * Protect infromation and prevent it from being stolen by unauthorized users
    * Layers
        * physical security - protect hardware / data center
        * identity & access - access to  infrastructure and change control 
        * perimeter - DDoS protection to filter large scale attacks; firewalls
        * network - limits communication between resources (segmentation / access control)
        * compute - secure access to VMs
        * application - ensure applications secure / free of security vulnerabilties
        * data - control access to business / customer data
* Microsoft Defender for Cloud
    * Azure Security monitoring tool for management and threat protection 
    * 
