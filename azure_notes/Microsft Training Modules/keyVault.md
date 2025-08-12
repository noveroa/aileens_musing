# Azure Key Vault
> Centralized cloud service for storing applicatoin secrets (encryption keys, certificates, server-side tokens)
> Key concepts: vault, keys, secrets

* Vaults
    * multiple secure containers, centralizing secret storage
    * collections of cryptographic keys and data (secrets)
    * represent logical groups of keys/secrets for an organization to be managed together 
    * control and log access
* Keys
    * cryptographic asset (ie Asymmetric master key of microsoft Azure RMS, sql server tde, cle, encypted backup)
    * applications and microsoft do not have access to stored keys directly - key vault called by api and cryptographically performs applicable actoins
    * single instanced or be versioned (versioned - primary/active key and 0+ secondary/archived keys that can be renewed)
    * Variations
        * Note: For production use, it's recommended to use HSM-protected keys and use software-protected keys in only test/pilot scenarios. There's an additional charge for HSM-backed keys per-month if the key is used in that month. The summary page has a link to the pricing details for Azure Key Vault.
        * hardware-protected keys
            * key vault supports hardware security modules (HSMs)  - BYOK
        * software-protected keys
            * key vault generate / protect keys using software based RSA and ECC algorithms
* Secrets
    * < 10K data blobs protected by a HSM generated key with key vault
    * storage account keys, sql connection strings, data encryption keys...

* Key Vault Uses
    * Secrets Management 
        * tokens, passwords, certificates, API keys, and other secrets.
    * Key Management
        * create and control the encryption keys used to encrypt your data.
    * Certificate Management
        * provision, manage deploy private SSL/TLS certificates

* Access 
    * Authentication 
        * Identify the caller
        * Microsoft EntraID
    * Authorization
        * Level of permission and access
        * Role-based access control (RBAC) 
            * azure does have built in _key vault contributor_ role providing access to management featyres (but not the data)
            * reading and writing data in the Key Vault uses a separate Key Vault access policy.
                * can use predefined : "Key, Secret, & Certificate Management"
    * Network Access Restrictions
        * What services in the network can access the key vault
