# TLS Certificates and Kubernetes Security

## Overview
TLS (Transport Layer Security) certificates are crucial for securing communication in Kubernetes clusters. They provide encryption and authentication between cluster components and external clients.

* A certificate is used to guarantee trust between two parties during a transaction
* Encryption
    * Symmetric Encryption
        * same key to encrypt and decrypt data
        * risk as key must be sent between sender and reciever
    * Asymmetric Encryption
        * A pair of keys - private key  and public key ("lock")
        * you can use assymetic private/public key pairs to send the symmetric key 
            * user generates a public/private key pair and accesses the server, the user gets the public key from teh server, the browser browser then encrypts the symmetric key using the public key provided by the server and sends it back; only the server with the prvate key (not sent thus not hackable) unlocks it
