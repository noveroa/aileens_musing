# monitoring for security

* Microsoft Entra Logs
    * captures log information for your entire azure tenant; available for analysis and reporting, 
    * activity logs
        * user behavior and interacrtions with network and assets
        * sign-in logs 
            * details of all user activity and the applications that requested authentication for sign-in
            * only tracks _traditional_ sign-ins that used user credentials, **not** server-to-server
            * identify:
                * pattern of user sign-in behavior
                * trends in activity over time
                * overall status of all users accessing the network
        * audit logs 
            * what user/group did while signed into the network
            * history of every activity in microsoft entra tenant - compliance, may be delayed up to an hour
    * security logs
        * list of exceptions found in activity logs
        * risky sign-ins
            * user data in which sign-in is inconsistent with earlier sign-in attempts
        * users flagged for risk
            * logs of users flgged for risk --> all users flagged as risky users

* Log Analytics workspace
    * Azure Moitor can provide real-time views and alerting of sign-in/activity behavior
    * log analytics workspace for azure monitor holds, stores, visualizes the sign-in and acitvity log behavior