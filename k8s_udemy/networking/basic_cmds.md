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
