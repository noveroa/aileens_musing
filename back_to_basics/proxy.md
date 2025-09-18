# Proxy
> A proxy is an intermediary server or service that acts as a gateway between clients and servers, forwarding requests and responses between them. It sits between the client and the destination server, handling communication on behalf of the client.

* Forward Proxy
    * Sits between clients and the internet
    * Clients send requests to the proxy, which forwards them to destination servers
    * Common use cases:
        * Web filtering and content blocking
        * Caching for performance
        * Anonymizing client requests
        * Bypassing geographic restrictions
* Reverse Proxy
    * Sits between the internet and servers
    * Receives requests from clients and forwards them to backend servers
    * Common use cases:
        * Load balancing across multiple servers
        * SSL termination
        * Caching responses
        * API gateway functionality
* Transparent Proxy
    * Intercepts network traffic without client configuration
    * Client is unaware of the proxy's existence
    * Often used in corporate networks for monitoring/filtering

* Proxy Functions
    * Traffic Routing
        * Directs requests to appropriate backend services
        * Can modify request headers, paths, or protocols
        * Load distribution across multiple servers

    * Security
        * Filters malicious requests
        * Hides internal network topology
        * Implements authentication and authorization
    * Performance
        * Caches frequently requested content
        * Compresses responses
        * Connection pooling and reuse
    * Monitoring & Logging
        * Request/response logging
        * Traffic analytics
        * Performance metrics

| Type	 | Purpose	| Example Use Case | 
| HTTP Proxy | 	Web traffic	 | Corporate web filtering | 
| SOCKS Proxy | 	Any TCP traffic	Tunneling applications | 
| SSL Proxy	Encrypted traffic | 	SSL inspection/termination | 
| Application Proxy	Specific protocols | 	Database or API gateways | 
