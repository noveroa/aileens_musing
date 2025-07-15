
# aileens_musing
## Cambridge, MA

![N|Solid](https://ca.slack-edge.com/T0495HV8H-U01AM69UW3E-ae635702c574-72)

###### 

Let's go back to basics for another moment, the OSI model - how data is transformed in each layers and how request is sent and response is received.
How is it when i type google.com my request travels through the netherworld of the internet to the google servers and back to display the google home page ... (ok ignore caching etc etc ).. the journey of data.

OSI Model - L7  --> L1 


### 
Key Ideas - steps 

X STOP X   .. verify first!

1. DNS Resolution
> Domain Naming Service - "simple database" mapping the domain name (google.com) to an ipaddress (first checking the routers and local cache then the internet providers DNS)
2. TCP Handshake 
> After validation, TCP handshake.  typically 3 way handshake - (a) Hi, server! (sync), (b)  Hi, requester (sync ackknowledged), (c) Coooolio.

-----> request / data request initiation to the server  ----->

### OSI (7) Layers
|  layer   |  name  | responsibilty | service|
| -------- |------- | ------- | ---|
| 7 | application layer | browser | access interface - ie email (SMTP), web browsing (HTTP) |
| 6 | presentation layer | browser | data encryption / formating / compression |
| 5 | session layer | browser | connection/session created between applications  cookies/cache|
| 4 | transport layer | server | data segmented/split (TCP/UDP protocols identified) transport between systems "the heart" |
| 3 | network layer | routers | send the data / routing packets (packets: add source and destintion ip addresses to each segmentation) from source to destination optimally |
| 2 | frames | data link layer | | MAC addresses - "data transfer between two directly connected nodes, including error detection and correction. frames data and manages access to the physical medium. "|
| 1 | physical layer |  physical | physical and electrical transmission of data, defining the physical medium (cables) and how bits are represented and transmitted|

