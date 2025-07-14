
# aileens_musing
## Cambridge, MA

![N|Solid](https://ca.slack-edge.com/T0495HV8H-U01AM69UW3E-ae635702c574-72)

###### 

Let's go back to basics for another moment, Networking.
I always seem to just get overwhelmed when thinking of networking.  My head immediately goes 'TOO HARD ABORT KERNAL PANIC".

But really, I just need a simple easy conversation and explanation.  Its not all random math of bite/bytes.   Its ok ... its going to be ok


## Key Ideas
```sh
.--------------house / network----___------------.
|                                      <------- [router]
| ._____________.   ._____________.    |        |
| |subnet1.     |   |subnet2| <--connect        |
| |172.16.3.0/24|   |172.16.4.0/24|             |
| ._____________.   ._____________.             |   
|                                               |
|          ._____________.   ._______________.  |
|          |subnet3.     |   |subnet4.       |--|---> internet (via route tables/internet gateway)
|          |172.16.80.0/24|  |172.16.244.0/24|  |
|          ._____________.   ._______________.  |
|                                               |
.-----------------------------------------------.
```
* VPC
    * the virtual network
* Subnet
    * Splitting of the network into partitions  (hypervisor; ie splitting a farm into lots)
        * secure, private, isolated 
        * to make a subnet public (accessible to the internet) use a route table/internet gateway
* CIDR range
    * The range from within your network's allocated subnet ipaddresses assigned to each subnet!
    * given 656 ip addresses, splitting 256 to subnetX and the rest to subnetZ
* IP Address
    * A uniquely generated address/number for a given device connecting to a network
    > in order to allow/deny/tag/monitor devices (connections) in your network, you would require a standard way to identify!  Thus the ip address
    * What does an ip address look like?
        * ipv4 - standard 4 byte generated number (4 1 byte (8bit) octals)
            * 171   .   16   .   3    .    4
            * 8bit  | 8 bit  | 8 bit  | 8 bite (or 0 - 255!)


> NETWORK --> Subnet(s) ---> CIDR Range
if you need 256 ip addresses : 172.16.3.0/**24** , 192.16.2.0/**24**

## 
___ 

Linux - File and Directory management .. obvi... 

|    | address range |
| vpc | 172.16.0.0 -- 172.16.255.255 |
| subnet A | 172.16.3.4 |
| cidr range | 172.16.3.0 / 24|
* if i only need 256 addresses: 172.16.3.0 / 24
    * in this particular subnet, since each byte = 0-255, 
    * the first 3 bytes can be common.  So "discard 32"... 
    * then if split to 24 -->. 32 -24 = 8 
    * 2^8 = 256!  We have enough addresses in the range!
* Say I only need 2 ip addresses from the range : 172.16.3.0 / 31
    * 32 - 31 = 1
    * 2^1 = 2!  (ie 0, 1)

__ 
# Reources:
* [Youtube; Networking Concepts are Easy](https://www.youtube.com/watch?v=PhTn8RkF0F4)