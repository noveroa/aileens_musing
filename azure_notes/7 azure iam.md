Azure IAM
### 
 # Microsoft Entra ID
_previously (azure) active direectory_

Azure IAM (Authentication + Authorization) 
* Users
    * Individual identities, whether they are human users or service principals (like applications or managed identities), that interact with Azure resources.
    * Users can be assigned roles directly or through group membership.
* Roles 
    * Collections of users that can be used to manage access in bulk. 
    * Azure AD (Active Directory) groups can be used for various purposes, including:
        *  Authorization: Restricting access to resources based on group membership. 
        * Role Assignments: Assigning roles to groups, granting permissions to all members. 
    * Groups can be nested (a group can be a member of another group). 
    * Two main types of groups in Azure AD: Security groups and Microsoft 365 groups. 
* Groups
    * Roles define the level of access to Azure resources. 
    * Azure has built-in roles (like Owner, Contributor, Reader) and allows for custom roles. 
    * Built-in roles have fixed sets of permissions, while custom roles can be defined to meet specific needs. 
    * Roles can be assigned at different scopes: Management group, subscription, resource group, or resource. 
    *  Example: The "Reader" role allows users to view resources but not modify them, while the "Contributor" role allows full access to manage resources. 
*  Role Assignments:
    *  The process of assigning roles to users or groups at a specific scope (e.g., a resource group). 
    *  This is how Azure RBAC controls access to resources. 
    *  You can use the Azure portal, Azure CLI, or PowerShell to assign roles. 
* Azure AD Roles vs. Azure Roles:
    *  Azure AD roles: control access to Azure AD resources (like users, groups, and applications). 
    *  Azure roles: (Azure RBAC) control access to Azure resources (like virtual machines, storage accounts, etc.). 
    *  For example, an Azure AD role like "User Administrator" can manage user accounts, while an Azure role like "Virtual Machine Contributor" can manage virtual machines. 

Resources >> Service Principle || Managed Identity Principle
> In essence, Managed Identities are a type of Service Principal specifically tailored for Azure resources, offering simplified management and enhanced security compared to traditional service principals. 

| Feature|  Service Principal| Managed Identity|
| ---- | ------| -------|
|Creation | Manual| Automatic |
| Credential Management | Manual (secrets or certificates)  | Automatic |
| Lifecycle| Independent | Tied to Azure resource| 
| Scope |General (can be used outside Azure) | Azure resources only |
| Security | Requires careful management to avoid security risks | Simplified security with automatic credential management| 

_________________

| Authentication |	Authorization |
| -------------- | _______________|
| users are who they claim to be |	what users can/not access |
| Challenges to validate credentials - ie passwords,security questions,biometrics |	Verifies access is allowed via policies/rules |
| before authorization	 | post successful authentication |
| std. transmits info through an ID Token | Access Token |
| std. governed by the OpenID Connect (OIDC) protocol| std. governed by the OAuth 2.0 framework |
| Example: Employees in a company are required to authenticate through the network before accessing their company email	| After an employee successfully authenticates, the system determines what information the employees are allowed to access |
