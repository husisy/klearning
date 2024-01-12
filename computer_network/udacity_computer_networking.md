# computer networking - Udacity

pre-course Networking for Web Developer

1. [course site](https://classroom.udacity.com/courses/ud256)
2. `printf 'hello\n world\n'`
3. `echo 'hello\n world\n'`
4. `nc`: net cat
   * `nc localhost 22`
5. 幺蛾子
   * `ping` use `ICMP`
   * `dns` use `UDP`
   * `ARP`
6. multi request
   * fork process
   * pool of processes or threads
   * single process quickly switch between handling requests: `epole` function in linux
7. packets
8. hosts: a machine on the internet that might host services
9. endpoints: the two machines or programs communicating over the connection
10. Domain Name System (DNS): worldwide distributed directory of network information
    * A-Record: the address of a computer connected to the internet from a name
    * CNAME-Record: canonical name
    * AAAA-Record (quad-A): IPv6 address
    * NS-Record: DNS name server
    * security mechanism for http, SSL encryption, cookie privacy
    * the Resolver: the DNS client code built into operating system
    * `host -t a google.com`
    * Global Top-Level Domain (GTLD)
    * Internet Service Provider (ISP)
    * host header
    * seach domain: a setting in the resolver configuration that makes the resolver look up names inside a domain
11. IPv4
    * octet = byte
    * `0`, `10`, `127` are entirely reserved
    * `116`, `169`, `172`, `192`, `198`, `203` are partly reserved
    * `224-239` for IP multicast
    * `240-255` was originally set aside for future use but was effectively lost due to being blocked as invalid
12. interface
    * ethernet interface
    * wifi interface
    * loopback interface
    * tunnel interface
    * virtual machine interface
    * `ifconfig`
    * `ip addr show`
    * `host localhost`
    * `ip route show default`
    * `netstat -nr`
13. Network Address Translation (NAT)
14. `tcpdump`
    * `sudo tcpdump -n host 8.8.8.8`, `ping -c3 8.8.8.8`
    * `sudo tcpdump -n port 53`, `ping yahoo.com`
    * pcap-filter
    * `sudo tcpdump -n port 80`, `printf 'HEAD / HTTP/1.1\r\nHost: example.net\r\n\r\n' | nc example.net 80`
15. TCP flag
    * `[S]`: synchronize, open a new TCP session and contain a new initial sequence number
    * `[F]`: finish, close a TCP session normally. finish sending, but still receive data from the other endpoint
    * `[P]`: push, the end of a chunk of application data, such as an HTTP request
    * `[R]`: reset,  a TCP error message; the sender has a problem and wants to reset (abandon) the session
    * `[.]`: acknowledge, acknowledges that its sender has received data from the other endpoint. Almost every packet except the first SYN will have the ACK flag set
    * `[U]`: urgent,  contains data that needs to be delivered to the application out-of-order. Not used in HTTP or most other current applications
16. middleboxes: firewall, instruction detection system, load balancers
    * iptables are NOT middleboxes
    * carrier-grade NAT
    * web proxy
17. network troubleshoot
    * `ping`: the blockage is not just dropping all of the traffic to you
    * different domain on the same server
    * `host`, `dig`: look up server's name

| layer | protocols | concepts |
| :-: | :-: | :-: | :-: |
| application | http, ssh | URL password |
| transport | TCP, UDP | port number, session |
| internet | IP | IP address, route |
| link | wifi, ethernet, DSL | signal strength, access point |

| protocol | concept | code | failure |
| :-: | :-: | :-: | :-: |
| http | resource, URL, verb, cookie | Flask, Apache, browser | error code |
| TCP | port, session, stream socket | OS kernel, system library | broken connnection, timeout |
| IP | address, packet | OS kernel, router | various |
| wifi | access points, WPA password | device driver | network unavailable |

```bash
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install netcat-openbsd tcpdump traceroute mtr

ip addr show eth0
ip route show
ping -c3 8.8.8.8
host -t aaaa google.com
host -t mx udacity.com
tcpdump -n -c5 -i eth0 port 22
traceroute wwww.udacity.com
mtr www.udacity.com
printf 'HEAD / HTTP/1.1\r\nHost: www.google.com\r\n\r\n' | nc www.google.com 80
printf 'HTTP/1.1 302 Moved\r\nLocation: https://www.baidu.com' | nc -l 2333
```
