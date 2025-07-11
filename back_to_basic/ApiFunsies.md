# aileens_musing

## Cambridge, MA

![N|Solid](https://ca.slack-edge.com/T0495HV8H-U01AM69UW3E-ae635702c574-72)

###### 
Embarrassingly, I feel I google these too much :) 
API (application programming interface) - security - reliability - functional - performant
- Collection of functions to be executed by another program
- request (client) --> (communiction protocol) -->  response (server) without exposing the internals
client
####

| method  | What you do | idempotent| can you do something? |
| ------ | ------ |------ |------ |
| GET   |  Retrieve | yes | fetch |
| POST | create  | no | create |
| PUT | replace/create | yes | update/replace ENTIRE object |
| PATCH | PARTIAL update | yes | update a single entity/field|
| DELETE | delete a resource | yes | bye bye|

##### idempotent :  operation, when executed multiple times, produces the same result as if it were executed only once, with no side effects beyond the initial execution. Essentially, repeated executions don't change the outcome beyond the first time

# types
* web - web service 
* local - apps in same system
* program - one program interacting with another

# REST
* representational state transfer 
* SIMPLE, SCALABLE, FLEXIBLE, INTEROPERABLE
* architectural design style for webservices using std http methods
* stateless - each request from client to server must contain all needed information 
* client / server - indenpendent
* cacheable - improved performance
* uniform interface - standardized set of operations (http methods) and consistent representation (simple, interoperable)
# ideas
* headers - 
    * nonrequest body info (control behavior of the server handling the request)
    * response metadata status codes, content type, security policies
    * request metadata for client, auth/content type, caching
* versioning - backwards compatible
* mocking - functional vs non/performant
* security authorization 
    * authorization - what can i access (RBAC)
    * authentication - i am who i am or am i ?
    * input santitation
    * secure headers/encryption
    * rate limiting / throttling
    * tokens

# Testing you should perform on your APIS
* Functional  (requiredspecs honored?)
* UI (expected results, format)
* LOAD (stress test - aileen's daily life)
* Security
* Validation
* Runtime (errors)
* Penetration (hacker security)
* API Hacking ()
* Fuzzy Testing (unexpected input and how you handle it)
