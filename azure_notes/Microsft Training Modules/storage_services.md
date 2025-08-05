# Azure Storage Solutions

* Azure Storage Accounts
    * Unique namepaces for stoage data accessible globally over HTTP/s - secure highly available durable scalable
* Services
    * Azure Blobs
        * A massively scalable object store for text and binary data. Also includes support for big data analytics through Data Lake Storage Gen2.
        * text/binary/video data, dynamic logs, encrypted messages, custom foramts
        * storage tiers for cost management / lifetime cycles
            * Hot access - frequently accessed (website images)
            * Cool Access - infrequently access and stored >= 30 days
            * Cold Access - infrequently access  and stored >= 90 days
            * Archive Access - rarelt access and stored > 180 days with flexible latency requirements
    * Azure Files
        * Managed file shares for cloud or on-premises deployments.
        * mounted concurrently by clou or on-premise deployments
        * shared access (SMB, NFS protocols)
    * Azure Queues 
        * A messaging store for reliable messaging between application components.
        * Hook with Azure functions to trigger events
    * Azure Disks
        * Block-level storage volumes for Azure VMs.
    * Azure Tables
        * NoSQL table option for structured, non-relational data.

| Type | Support services | Redundancy Options | Usage |
| -------- | ------- | -------- | ------- |
| Standard general-purpose v2	| Blob Storage (including Data Lake Storage),Queue Storage, Table StorageAzure Files	 | LRS, GRS, RA-GRS, ZRS, GZRS, RA-GZRS | Standard storage account type for blobs, file shares, queues, and tables. Recommended for most scenarios using Azure Storage. If you want support for network file system (NFS) in Azure Files, use the premium file shares account type.|
| Premium block blobs | Blob Storage (including Data Lake Storage)| LRS, ZRS |Premium storage account type for block blobs and append blobs. Recommended for scenarios with high transaction rates or that use smaller objects or require consistently low storage latency.|
| Premium file shares |	Azure Files	| LRS, ZRS	 | Premium storage account type for file shares only. Recommended for enterprise or high-performance scale applications. Use this account type if you want a storage account that supports both Server Message Block (SMB) and NFS file shares.| 
| Premium page blobs |	Page blobs  |only LRS |Premium storage account type for page blobs only. |


* Storage ccount Endpoints
    * Every storage account haas a unique0in-Azure accuont name - endpoint == account name + azure stoage services
        | Storage service	| Endpoint | 
        | -------- | ------- | 
        | Blob Storage	| https://<storage-account-name>.blob.core.windows.net |
        | Data Lake Storage Gen2	 | https://<storage-account-name>.dfs.core.windows.net |
        | Azure Files	| https://<storage-account-name>.file.core.windows.net |
        | Queue Storage	| https://<storage-account-name>.queue.core.windows.net |
        | Table Storage	 | https://<storage-account-name>.table.core.windows.net |
* Redundancy
    *  Primary Region - data is always replicated three times in the primary region 
        * Locally redundant storage (LRS) - three time replcation within a single data center - 11 nines of durability - lowest cost
        * Zone-redundant storage (ZRS) - replicates storage data synchronously acrorss three availabilty zones in the primary regoin 12 nines of durabilty 
    * Secondary Region Redundancy - for high durabilty - copy to a secondary region (paired region) - not available for read/write unless there is a failover - **asychnronous**
        * Geo-redundant storage (GRS) ~ "LRS of primary in two regions" - 16 nines of durabity
            * Read-access geo-redundant storage (RA-GRS) - replicates data to a second location in the secondary region; if enabled access always available (not just with a failover to secondary regoin)
        * Geo-zone-redundant storage (GZRS) ~ "ZRS in primary and secondary regions" - 
            * Read-access geo-zone-redundant storage (RA-GZRS)
* Data Migration Options
    * Azure Migrate - migrate on-premise environemtn to cloud
    * Azure data Box - physical migration service to transfer large aounts of data (80 TB)
* Azure File Movement Options
    * AzCopy
        * CLI to copy blobs / files to/from storage account
    * Azure Storage Explorer
        * GUI to manage files / blobs 
    * Azure File Sync
        "Like turning your Windows file server into a miniature content delivery network. Once you install Azure File Sync on your local Windows server, it will automatically stay bi-directionally synced with your files in Azure."