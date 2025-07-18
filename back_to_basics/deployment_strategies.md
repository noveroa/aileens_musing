# aileens_musing

## Cambridge, MA

![N|Solid](https://ca.slack-edge.com/T0495HV8H-U01AM69UW3E-ae635702c574-72)

###### 
Deployment - cid cd vs bluegreen???  

___
# Blue / Green
> Creating two identical production environments - active (blue) & standby (green).  Once a new version (green) is validated (tested) traffic routed from Blue to Green.  Green is now the active, Blue the standby

# benefits
* Increased reliablity and reduced downtime
* Minimal disruptions for users during updates of software
* Pre-live testing and validation
* Consistent performance
# not so beneficial?
* COST - have to maintain infrastructure for two environments
* longer deployment times (rerouting traffic)
* more complex configuration/set up (when compared to Ci/Cd)

__
# CI/CD
> Uploading changes / commits at intervals - ie Continuous Integration and Continuous Delivery/Deployment (duh the name). Source, Build (compile, install deps, package artifacts), Test, Deploy - Stagining - Monitor
Source: Code is pushed to a version control system (e.g., GitHub).
## Continuous Integration (CI)
* Merge code changes frequently (usually daily).
* Each change triggers an automated build and test process.
* Goal: Detect errors quickly and keep the codebase healthy.
    * Example: When you push code to GitHub, a workflow runs unit tests.
## Continuous Delivery (CD)
* Every successful change from CI is automatically prepared for release to a staging or production environment.
* Focuses on making deployments routine and predictable.
## Continuous Deployment (CD)
* Every change that passes tests is automatically deployed to production.
* ie. no manual intervention.

# CI/CD benefits
* Fast/efficient delivery
* continuous/interative feedback
* lower costs
* automated testing/validation
* easier/ faster rollbacks
# CI/CD drawback?
* higher risk of downtime/deployment errors
* potential loss of versions
* limited pre-live testing (compared to BG)
* inconsistent performance/reliability during updates

