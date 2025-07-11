# aileens_musing

## Cambridge, MA

![N|Solid](https://ca.slack-edge.com/T0495HV8H-U01AM69UW3E-ae635702c574-72)

### 
Terraform vs Cloudformation ... you know where i stand


# terraform (open tofu?)
* open source
* cloud / operations agnostic
* dynamic resource creation 
* useful features
    * multi cloud support
    * execution plans
    * declarative lanuage (HCL)
    * resource graphs
    * state management
    * built in functions

# AWS Cloudformation
* aws specific service for creating/provisioning resources (YAML/JSON)
* aws support, CF modules, (nested code ... ugh)
* useful features?
    * aws support (i guess?)
    * YAML/JSON
    * execution plans/change sets
    * custom resources (3rd party obvi)
    * roll back automated (sure, aws sure, resurce deletion
    * cross regional 