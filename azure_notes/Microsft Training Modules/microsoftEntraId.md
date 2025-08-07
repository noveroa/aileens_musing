# Microsoft Entra ID

* Active Directory Domain Service (AD DS; AD) - Traditional directory service that provides methods for storing directory data (user accounts/passwords) available to network users, admins, devices, and services. 
    * Characteristics
        * Directory service with hierarchical X.500-based structure
        * DNS for locating resources such as domain controllers
        * LDAP  (lightweight Directory Access Protocol) to query/manage AD DS
        * Kerberos protocol for authentication (secret-key cryptography to verify user identities and grant access to network resource)
        * Organizational Units (OUs) and Group Policy Objects (GPOs)
        * Uses Trusts Between domains for delegated management
* Microsoft Entra ID - a PaaS operating as a Microsoft-managed directory service in the Cloud. Features beyond AD DS - MFA, Identiry Protection, SelfService Password Reset
    * Uses
        * Configure application accesss
        * SSO to cloud based SaaS applicatoins
        * Managing users / groups
        * Provisioning usersu
        * Enabling federatoin between organizations
        * Identity Management Solutions
        * Monitor and identify irregular sign-in activity
        * Extending on-prem AD 
        * Configuring Applicatoin Proxy for cloud/local applicatoins
        * Configuring Conditoinal Access for users / devices
    * Characteristics
        * Identity solution designed for internet-based applications by using HTTP/S communications
        * Multi-tenant directory service
        * Users/Groups in a flat structure (no OUs/GPOs)
        * Use REST to query (not LDAP)
        * autherntication by SAML, WS-Federatoin, OpenID Connect (authentication), OAuth (authorization) Not kerberous
        * Includes federation services, and 3rd party services (ie Facebook)

* Microsoft Entra Tenets
    * Multitenent by design, and implemented to specifically ensure isolation between individual directory instances
        * tenant : 
            * a company / organization that signed up for a subscription to microsoft cloud-based service (Microsoft 365, Intune, Azure)
            * Individual Microsoft Entra Instance
            * Within an Azure Subscription you can create multiple Microsoft Entra tenent
                * YET Azure subscription must be associated with one, **and only one,** Microsoft Entra tenant _at any given time_
                    * This association allows you to grant permissions to resources in the Azure subscription (via RBAC) to users, groups, and applications that exist in that particular Microsoft Entra tenant.
                * You CAN associate the same Microsoft Entra Tenant with multiple azure subscriptoins - allowing the same users, groups, applicatoins to be manage resources across multiple azure subscriptions

* Microsoft Entra Domain Services
    * Integrates with local AD DS (when implementing Microsoft entra Connect)
        * users can use organizatoinal credits both on-premise AD DS and In cloud-based Microsoft Entra Domain Services (though can choose to hace Microsoft Entra Domain Services as cloud-only)
    * Administrators don't need to manage, update, monitor domain controllers
    * Administrators dont need to deploy and manage Active Directory replications
    * 
