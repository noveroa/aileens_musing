
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
|         .______________.   ._______________.  |
|         |subnet3.      |   |subnet4.       |--|---> internet (via route tables/internet gateway)
|         |172.16.80.0/24|   |172.16.244.0/24|  |
|         .______________.   ._______________.  |
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
>
>if you need 256 ip addresses : 172.16.3.0/**24** , 192.16.2.0/**24**

## 
___ 

|  module | address range |
| -------- | ------- |
| vpc | 172.16.0.0 - 172.16.255.255 |
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

* Common networking commands for linux


| command   | result | 
|-----------|--------|
| ip link | Shows all network interfaces with their states (UP/DOWN) and MAC addresses |
| ip addr | Displays IP addresses assigned to all network interfaces |
| ip addr add 192.168.1.10/24 dev eth0 | Adds IP address 192.168.1.10 with /24 subnet to eth0 interface (no output if successful) |
| ip route | Shows the routing table with destination networks and gateways |
| ip route add 192.168.1.0/24 via 192.168.2.1 | Adds a route to 192.168.1.0/24 network via gateway 192.168.2.1 (no output if successful) |
| arp | Shows ARP table with IP-to-MAC address mappings for local network |
| route | Displays kernel routing table in traditional format |
| netstat -plnt | Shows listening TCP ports with process IDs and names |
| ip link add v-net-0 type bridge | Creates a bridge interface named v-net-0 (no output if successful) |
| ip addr add 192.168.15.5/24 dev v-net-0 | Assigns IP address 192.168.15.5/24 to the v-net-0 bridge interface |
| ip link set veth-red netns red | Moves veth-red interface to the 'red' network namespace |
| ip -n red link set veth-red up | Brings up the veth-red interface within the 'red' namespace |
| ip netns exec blue ip route add 192.168.1.0/24 via 192.168.15.5 | Adds route in 'blue' namespace to reach 192.168.1.0/24 via gateway 192.168.15.5 |
| ip link set dev v-net-0 up | Brings up the v-net-0 bridge interface |
| ip link add veth-red type veth peer name veth-red-br | Creates a veth pair: veth-red and veth-red-br (virtual ethernet cable) |
| ip -n red addr add 192.168.15.1/24 dev veth-red | Assigns IP 192.168.15.1/24 to veth-red interface in 'red' namespace |
| ip link set veth-red-br master v-net-0 | Connects veth-red-br to the v-net-0 bridge (makes it a bridge port) |
| iptables -t nat -A POSTROUTING -s 192.168.15.0/24 -j MASQUERADE | Adds NAT rule for outbound traffic from 192.168.15.0/24 subnet | 

__ 
# Resources:
* [Youtube; Networking Concepts are Easy](https://www.youtube.com/watch?v=PhTn8RkF0F4)