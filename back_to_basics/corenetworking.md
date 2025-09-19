# Switching, Routing, Gateways CNI 

* Network switch
    > Connects multiple devices (computers, servers, printers, etc.) **within** a local area network (LAN) and intelligently forwards data between them
    * Layer 2 Operation
        * Data Link Layer (Layer 2) of OSI model
    * MAC Address Learning
        *  maintain a MAC address table that maps each connected device's MAC address to a specific port
        * They learn these addresses by examining the source MAC address of incoming frames
    * Intelligent Forwarding
        * send data only to the intended recipient port, reducing network congestion and improving security
    * Full-Duplex Communication
        * Each port on a switch provides a dedicated collision domain, allowing simultaneous send/receive operations at full bandwidth
    * How it works
        * Learn - record MAC
        * Filter - determine MAC and destination port
        * Forward - sends data only to specifc port the destintion device is connected
        * Flood - If the destination MAC is unknown, the switch floods the frame to all ports (except the source)
    * Types
        * Unmanaged
            * Basic plug-and-play switches with no configuration options
        * Managed
            * Advanced switches with configuration capabilities, VLANs, QoS, and monitoring features
        * Layer 3
            * Can perform routing functions in addition to switching

* Routers
    > A router connect **two+** networks together. **Gateways** are the door that allow the two networks to actually access the other network - added to the routing table