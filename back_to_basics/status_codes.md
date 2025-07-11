# aileens_musing

## Cambridge, MA

![N|Solid](https://ca.slack-edge.com/T0495HV8H-U01AM69UW3E-ae635702c574-72)

###### 
Embarrassingly, I feel I google these too much :) 


    * 1xx - represents informational responses
    * 2xx - represents successful responses
    * 3xx - represents redirects
    * 4xx - represents client errors
    * 5xx - represents server errors

Most commonly used status codes are:
* 200s - Success! You did it! 
    * 200 - success/OK (GET, PUT, POST)
    * 201 - CREATED - used in POST or PUT methods. (POST)
    * 204 - No Content - Successful, but no return object, sorry dude (ie DELETE)

* 304 - NOT MODIFIED - used in conditional GET requests to reduce the bandwidth use of the network
    Here, the body of the response sent should be empty.

* 400s - Client Errors
    * 400 - BAD REQUEST - Malformed requested/JSON - This can be due to validation errors or missing input data. 
    * 401- UNAUTHORIZED - no valid authentication credentials sent along with the request.
    * 403 - FORBIDDEN - sent when the user does not have access (or is forbidden) to the resource.
    * 404 - NOT FOUND - Resource method is not available.
    * 409 - CONFLICT - duplicate data?  - request conflicts with the current state of affairs
    * 422 - Unprocessible Entity - Syntatically correct request, semantically invalid 
* 500s - Server Error
    * 500 - INTERNAL SERVER ERROR - server threw some exceptions while running the method. - generic
    * 502 - BAD GATEWAY - Server was not able to get the response from another upstream server.
    * 503 - Service Unvailable - Server Overload! Maintainance
    * 504 - Gateway Timeout - Server didn't receive the response in time.
