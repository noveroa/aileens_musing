# Azure security and compliance

* Microsoft EntraId
    * Cloud based identity-management solution allowing access to external services and internal resources within the corporate network
    * Stores users in a _tenant_ representing the organization; each tenant can have multiple groups holding multiple users

* Microsoft Entra ID vs Active Directory
    * EntraId --> cloud based manages users / applications
    * AD --> manages objects (devices/users) on-premises networks
    | Service	| Authentication	| Structure		| Used for |
    |   ------	|    ------	|   ------	|   ------	| 
    | Active Directory	| Kerberos, NTLM	| Forests, domains, organizational units	| Authentication and authorization for on-premises printers, applications, file services, and more |
    | Microsoft Entra ID	|  Includes SAML, OAuth, WS-Federation	| Tenants	| Internet-based services and applications like Microsoft 365, Azure services, and third-party SaaS applications |
* Linking on-premise AD with cloud-based Microsoft EntraId
    * Users have single identity for authentication and access to resources - hybrid identity - single sign on (SSO)
        * microsoft entra hash synchronization - pw is hashed twice and synced between AD and EntraID
        * pass-through authentication - agent on-premis server authenticates against on premise AD 
        * federated authenticatio - Active Directory Federatoin Services (AD FS) validates users
* Licensing
    * Pay as you go for specific features 
    * Office 365 Apps - custom sign-in and sign out pages, self-service password reset for cloud users, and device write-back.
    * Microsoft Entra ID P1: You get all the features from the free tier, but you can also let users access on-premises and cloud-based services and resources. You can use self-service group management or dynamic groups, self-service password reset
    * Microsoft Entra ID P2: You get all the features of the previous two tiers, along with Microsoft Entra ID Protection. This feature helps you configure risk-based Conditional Access to protect applications from identity risks. You can also use privileged identity management, which lets you monitor and put detailed restrictions on Administrators
    * Microsoft Entra ID Governance: An advanced set of identity governance capabilities available for Microsoft Entra ID P1 and P2 customers. 
    * Microsoft Entra Suite: A complete cloud-based solution for workforce access, available for Microsoft Entra ID P1 and P2 customers. Microsoft Entra Suite brings together Microsoft Entra Private Access, Microsoft Entra Internet Access, Microsoft Entra ID Governance, Microsoft Entra ID Protection, and Microsoft Entra Verified ID. 
* Microsoft Entra Terminology
    | Term | Description |
    | -----| ----- |
    | Identify  |  Something that has to be identified and authenticated. An identity is typically a user with a username and password credentials, but the term can also apply to applications or services.|
    | Account	| An identity and its associated data. An account can't exist without an identity. |
    | Microsoft Entra account	| An identity created in Microsoft Entra ID, or in services like Microsoft 365. These identities are stored in Microsoft Entra ID. For example, internal staff members might use Microsoft Entra accounts daily at work. | 
    | Azure subscription | 	Your level of access to use Azure and its services. For pay-as-you-go access, use your credit card to set up an Azure subscription. There are several types of subscriptions. For example, enterprise-level customers can use Azure Enterprise Agreement subscriptions. Each account can use many subscriptions. | 
    | Microsoft Entra tenant |	An instance of a Microsoft Entra ID. This tenant is automatically created for you when you first sign up for Azure or other services like Microsoft 365. A tenant (which represents an organization) holds your users, user groups, and applications. |
    | Multitenant | 	Access by multiple tenants to the same applications and services in a shared environment. These tenants represent multiple organizations. |
    | Microsoft Entra directory	| An Azure resource created for you automatically when you subscribe to Azure. You can create many Microsoft Entra directories. Each of these directories represents a tenant. | 
    | Custom domain	| A domain you customize for your Microsoft Entra directory. When you create a Microsoft Entra directory, Azure automatically assigns it a default domain like <your-organization>.onmicrosoft.com. However, you can customize domain names. Your users could then have accounts like user@contoso.com instead of user@contoso.onmicrosoft.com. | 
    | Owner role |	The role you use to manage all Azure resources, including the access levels users need for resources. |
    | Global Administrator	| The role that gives you access to all Administrative capabilities in Microsoft Entra ID. When you create a tenant, you automatically have this role for the tenant. This role allows you to reset passwords for all users and Administrators, for example. | 
* Default permissions
    * default permissions for member users and guest users:

    | Area    | 	Member user permissions	    | Guest-user permissions    | 
    | ------- |     ------- |      ------- | 
    | Users and contacts    | Can view all profile details. Can change own password, mobile phone number, and profile photos.    | Can view the profile name, email, sign-in name, photo, and user principal name. Can view the user type properties of other users and contacts. Can change own password. | 
    | Devices | 	Can read all properties of devices. |  Can manage all properties of owned devices.	Can't read all properties of devices. Can't manage all properties of owned devices. Can delete owned devices. | 
    | Applications | 	Can register new applications. | Can't register new applications. Can delete owned applications. | 
    | Policies | 	Can read all properties of policies and manage all properties of owned policies. | 	No permissions. | 
    | Subscriptions | 	Can read all subscriptions and enable service plan members.	No permissions. | 
    | Roles and scopes	Can read all Administrative roles and memberships. Can read all roles and scopes and membership of Administrative units. | 	No permissions. | 
* Essential Features of Microsoft EntraID
    * Microsoft Entra B2B
        * Collaborating with external partner - Business to Business
        * Partners invited as guests and once work done, access can be revoked
    * Azure AD B2C
        * Manage customers' identities and access
    * Microsoft Entra Domain Services
        * Add VMs to a domain without needing a domain controller; internal staff can acces via microsoft entra credentials
    * App Management
        * Access can be managed and granted for both internal and external users
        * Microsoft Entra App Gellery applications (SaaS apps integrated with Microsoft EntraID), Non-gallery apps, On-premise apps
    * Conditional Access Polcies
        * Added layers of authentication
    * Monitoring app access
    * Microsoft Entra ID Protection
        * automatically detect, investigate, and remediate identity risks for users. It also lets you export all the information collected about risks. 

# How to get started
> lay a foundation, deploy Microsoft Entra ID by creating a tenant, and associate a subscription with it.

* Stage 1 : Foundation
    * Configure baseline security features before you add or create user accounts
    | Task    | Description	    | License needed    | 
    | -----    | ------    | -----|
    | Assign more than one Global Administrator	Give at least two Microsoft Entra accounts the Global Administrator role. Make sure you don't use these accounts daily. Ensure the accounts have long and complicated passwords.    | 	Free|
    | Use regular Administrative roles where possible	    | Administrators who aren't Global Administrators should never have more permissions than they need to do their work. Use these regular Administrator roles by default. Avoid using the Global Administrator roles unless needed.    | 	Free |
    | Configure Privileged Identity Management (PIM) to track Administrators    | 	Use PIM to monitor how your Administrator roles are used. This action helps you improve your governance and compliance.    | 	Microsoft Entra ID P2    | 
    | Configure self-service password reset	    | Let internal users reset their passwords through policies that you configure. This action reduces the number of help desk tickets for password resets.	    | Free    | 
    | Create a list of banned passwords	    | Use this list to prevent users from using passwords that are common phrases or words in your organization. For example, your list can include your company name or headquarters location.	    | Microsoft Entra ID P1    | 
    | Warn users to not reuse credentials	    | When someone reuses the same credentials on multiple platforms, an attacker can use the credentials to access all of those platforms if a single platform is compromised.	    | Free    | 
    | Set passwords to never expire for cloud-based user accounts	    | Routine password resetting tempts users to increment their existing passwords. For example, they might change their password from R4ndom1Strong to R4ndom2Strong and so on. In this case, because most of the password remains the same, it increases the risk of using already exposed credentials to gain access to an account.    | 	Free    | 
    | Enforce multifactor authentication through Conditional Access policies	    | Configure Conditional Access policies to require users to pass multiple authentication challenges before they can access an application.	    | Microsoft Entra ID P1    | 
    | Configure Microsoft Entra ID Protection	    | Flag and block suspicious sign-ins and compromised user credentials for your organization's users. You can also use Microsoft Entra ID Protection to automatically trigger multifactor authentication or a password reset, depending on the severity of the detected risk.	    | Microsoft Entra ID P2    | 
* Stage 2 - Add users, manage devices, and configure synchronization
    | Task    | 	Description    | 	License needed    | 
        |  ------    | -----    | ----- |
    | Install and configure Microsoft Entra Connect	    | Use Microsoft Entra Connect to synchronize users from your on-premises instance of Active Directory to Azure.	    | Free    | 
    | Use password hash synchronization    | 	You can synchronize password changes and detect and fix bad passwords. You get reports about leaked user credentials.    | 	Free    | 
    | Use password writeback	    | Configure password writeback so any changes to passwords in Azure are written to your on-premises instance of Active Directory.	    | Microsoft Entra ID P1    | 
    | Use Microsoft Entra Connect Health    | 	Use Microsoft Entra Connect Health to monitor the health statistics for your Microsoft Entra Connect environment.	    | Microsoft Entra ID P1    | 
    | Give users the licenses they need at a group level    | 	When you assign licenses at a group level, you control licensing for many users simultaneously. This action saves your organization time and reduces complexity.    | 	Free    | 
    | Use Microsoft Entra B2B Collaboration for guest-user access    | 	Use this resource to ensure that external healthcare partner users can use their own work or social identities to access your applications and services. You don't need to manage their credentials for them.	    | Required licenses depend on which features you want the guest users to access    | 
    | Prepare a device-management strategy    | 	Put together a plan based on which devices your company allows. For example, are you going to permit Bring Your Own Device (BYOD), or is the company only accepting its own devices given to users?	    | Free    | 
    | Provide authentication methods that don't require passwords    | 	Make authentication more convenient. For example, if users install Microsoft Authenticator on their phones, they can receive a notification that provides a code to enter at sign-in, along with a PIN or a biometric attribute like their fingerprint.    | 	Microsoft Entra ID P1    | 
* Stage 3: Manage your applications
    * Integrate applications as needed.
    |  Task    | 	Description    | 	License needed    | 
        |  ------    | -----    | ----- |
    | Identify applications	Investigate the applications in your organization. Your organization could, for example, have applications on-premises or software-as-a-service (SaaS) applications in the cloud. Choose applications that you want to manage in Microsoft Entra ID.	    | N/A    | 
    | Use SaaS applications in the Microsoft Entra gallery    | 	Your organization probably uses SaaS applications that are already in the gallery, and that you can find in the Azure portal. Use these applications from the gallery whenever you can. You can save time by integrating your applications and Microsoft Entra ID.	    | Free    | 
    | Integrate your on-premises applications using Application Proxy    | 	You can let Microsoft Entra users sign in to your on-premises applications using their Microsoft Entra account.	    | Free    | 
* Stage 4 : Monitor your Administrators, do access reviews, and automate user life cycles
    * Principles of Least Priviledge; automate common lifecycles
    |  Task    | 	Description    | 	License needed    | 
        |  ------    | -----    | ----- |
    | Use PIM to control Administrator access	    | Ensure that Administrators can use their account only after they pass a multifactor authentication challenge or receive approval from an accepted approver.	    | Microsoft Entra ID P2    | 
    | Complete access reviews for Microsoft Entra directory roles in PIM    | 	Configure access review policies in PIM so you can regularly review Administrative access based on your organization's requirements for privileged roles.	    | Microsoft Entra ID P2    | 
    | Configure dynamic group membership policies    | 	Save time and effort by automatically adding users to specific groups based on known profile information, like department or region. For example, you can automatically add all users who are part of the human resources department to a user group called Human Resources.	    | Microsoft Entra ID P1 or P2    | 
    | Use group-based application assignment    | 	Use group-based access management to give all group members access to an application. When you use dynamic groups, users who are removed from a group automatically lose access to the application. This action helps keep your applications secure.	    | Free    | 
    | Configure automated user account provisioning and deactivation    | 	Automatically create application-specific accounts to allow users to use SaaS applications based on existing Microsoft Entra users and groups. You can also automatically deprovision user accounts when a user leaves the organization. This action keeps your organization protected from unauthorized access.	    | Free    | 
* Stage : Create a tenant
* Stage : Associate a subscription  - a billing entity and a security boundary.