# Kubernetes - TLS and certs

* certificates
    * public - - *.crt, *.pem
    * privtae  - *.key, *-pem.key
    * serving certificates
        *  public / private keys are, how a server uses keys to secure connectivity.
    * root certificates
        * certificate authority has its own set of public and private key pairs that it uses to sign server certificates
    * client certificates
        * a server can request a client to verify themselves using

* kubernetes
    * all communication between these nodes need to be secure and must be encrypted
    * all interactions between all services and their clients need to be secure\
    * two primary requirements 
        * all various services within the cluster to use server certificates
        * all clients to use client certificates
    ## server
    * the kube-api-server
        * API server exposes an Https service that other components as well as external users use to manage the Kubernetes cluster.
        * it is a server and it requires certificates to secure all communication with its clients
        * Thus : certificate and key pair: apiservert.crt (public crt); apiserver.key (private key)
    * etcd server
    * kubelet server
    ## clients
    --> kube-api-server
    * admin : client tls certificates,  admin.crt, admin.key
    * kubescheduler
    * kube-controller-manager
    * kube-proxy
    * (kube-api-server --> etcd; kublet)

    ## root certs
    * need a certificate authority to sign all of these certificates; Kubernetes requires you to have at least one certificate authority for your cluster.

* creating certificates
    * companies
    * openSSL

* certificate api
    * 