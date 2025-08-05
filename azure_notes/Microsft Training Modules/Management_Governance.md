Management and Governance - Azure

# Cost Management
    * Operatoin Expenses are affected by:
        * resource types  - sizes, uptime, regions, licensing, storage...
        * consumption - pay as you go, 'reserved' resources, 
        * maintenance - deprecated / deleting unused resources
        * geography - cost of power, labor, taxes, fees can vary by location; 
            * network traffic also can be afffected
                * within europe vs europe to asia or to s.america
                * bandwidth (data in/out of data centers), data transfer is based on zones (geographic grouping of azure resources)
        * subscription types - usage allowances
        * azure marketplace - purchasing azure-based solutions and services from third-party vendors

    * Pricing Calculator
        * tool to help understand potential azure expenses, provide an estimated cost for provisioning resources in azure (compute, storage, network costs)
    * Microsoft Cost Management Tool
        * assist in avoiding accidental resource provisioning (ie from testing, POCs, sudden demand spikes)
        * create alerts based on resource spend, budegets that can be used to automatically manage resources
            * Cost alerts
                * single locatio to check on all different alert types - budget, credit, department specing quotas
            * Budgets - set spending limits (by subscription, resource group, service types,...)
    * Tagging
        * stay organized (subscriptions, resource groups, ... ) --> .resource tags
        * tags provide estra information (metadata)
            * management - locate/act on resource associated with specific workloads, environments, business units, owners
            * cost managament / optimization - levergae SLAs
            * security tags - classification
            * governance / regulatory compliance
            * workload optimization / automation - visualize the resources particiapting in a complex deployment

# Governance
    * Microsoft Purview - risk compliance and unified data governance
        * family of data governance, risk, compliance solutions
            * Automated data discovery
            * sensitive data classification
            * end to end data lineage
    * Azure Policy
        * Service to create, assign, manage policies that control or audit your resources
        * can enforce different rules across your resource configurations such that the configurations stay compliant with corporate stds.
        * evaluates your resources and highlights resources that aren't compliance with the policies you've creates 
            * can be preventative - denying creation of noncompliant resources
            * reactive - remediate non compliance resources and configs
        * set at different levels : specific resources, resource groups, subscriptoin, ... 
        * inherited
    * Azure Policy Initiatives
        * Grouping azure polcies together
    * Resource Locks
        * Preventing resources from being 'accidentally' deleted or changed
            * Delete - authorized uses can change but prevented from deleting resource
            * ReadOnly - authorized users can read resource, but cannot update/delete
    * Service Trust Portal
        * Provides access to content, rools, resources about microsoft security, privacy, compliance
    
    * Azure Arc 
        * Utilizing the azure resource manager (ARM) extend azure compliance and monitoring to your hydrid and ,ulti-cloud configuratoins - simplifying governance with multi-cloud and on-premesis platforms
    * Azure Resource Manager (ARM)
        * IaaS - deployment and management service for Azure; create update delete resources 
        * Declarative templates (JSON files) 
            * ARM Tempaltes - decalrative JSON format, repeatable/reusable. orchestration, modular, extensible
            * BICEP - 'a lanugage using declariative syntax to deploy azure resources'
    
# other tools
    * Azure Advisor
        * Evaluates azure resources, makes recommendations to help improve reliabilty, security, performance - operational excellence / reduce costs
            * Reliability - ensure and improve the continuity of your business-critical applications.
            * Security  - detect threats and vulnerabilities that might lead to security breaches.
            * Performance - improve the speed of your applications.
            * Operational Excellence - achieve process and workflow efficiency, resource manageability, and deployment best practices.
            * Cost - optimize and reduce your overall Azure spending.
    * Azure Service Health
        * Status of overall global azure infrastructure and your individual resources
        * Azure Status
            * broad picture of azure gloablly (service outages, incidents)
        * Service Health
            * narrower view - focuses on regions and services the customer is using
            * see planned maintenance activities, communications, advisories
        * Resource Health 
            * tailored view of customers own azure resources
    * Azure Monitor
        * Platform to collect data on customer's resources - analyzing/visualizing/acting upon the results
    * Azure Log analytics
        * Query the data gathered bt Azure Monitor
    * Azure Monitor Alerts
        * automated wat to stay informed on monitor detected thresholds being crossed
        * monitor logs (can be triggered to act on log event), metrics
    * Applicatoin Insights
        * Monitor web applications - request rates, response times, failure rates, dependency issues, page views, performance, ajax calls, session counts
