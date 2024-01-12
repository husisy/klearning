# internet

1. link
   * [阮一峰 互联网协议入门一](http://www.ruanyifeng.com/blog/2012/05/internet_protocol_suite_part_i.html)
   * [阮一峰 互联网协议入门二](http://www.ruanyifeng.com/blog/2012/06/internet_protocol_suite_part_ii.html)
   * [howhttps-works](https://howhttps.works/)
2. 五层模型
   * 应用层application layer
   * 传输层transport layer
   * 网络层network layer
   * 链接层link layer
   * 实体层physical layer
3. 链接层
   * 以太网协议Ethernet protocol：电信号0/1分组协议。帧Frame，标头Head（发送者、接收者、数据类型等说明项，固定18Byte），数据Data（64Byte-1518byte）
   * MAC地址，48bit，12个十六进制位，前六位是厂商编号，后六位是网卡流水号
   * 广播，ARP协议address resolution protocol
4. 网络层
   * IP协议Internet Protocol，IPv4，32bit，网络部分，主机部分，子网掩码subnet mask
   * IP数据包，标头Head（版本，长度，IP地址，20-60Byte），数据Data（0-65515Byte）
   * ARP协议
5. 传输层
   * 端口，16bit，0-1023系统占用
   * 套接字socket：主机+端口
   * UDP协议，标头Head（发出端口，接受端口），数据Data，一个UDP数据包对应一个IP数据包，一个IP数据包可能对应多个以太网数据包
   * TCP协议：确保数据不会遗失，一般一个TCP数据包对应一个IP数据包
6. 应用层
   * 应用程序协议
7. 用户发送数据
   * 对方在同一个子网络：对方的IP地址，对方的MAC地址（通过IP+ARP协议获得）
   * 对方不在同一个子网络：对方的IP地址，个人自网络网关gateway的MAC地址
8. 用户上网设置
   * 静态IP地址：本机的IP地址，子网掩码，网关的IP地址，DNS的ip地址
   * 动态ip地址：DHCP协议（建立在UDP协议之上）

## mail server

1. link
   * amazon simple mail service [link](https://aws.amazon.com/ses/)
   * spam haus project [link](https://check.spamhaus.org/)
   * gmail custom domain service
   * [github/postal](https://github.com/postalserver/postal)

## cloudflare

1. link
   * [documentation](https://developers.cloudflare.com/)
   * [test-ipv6](https://test-ipv6.com/) `curl https://api64.ipify.org`
   * using caddy with cloudflare [blog-link](https://samjmck.com/en/blog/using-caddy-with-cloudflare/)
2. concept
   * proxied DNS record, unproxied DNS record, cloudflare anycast IP
   * WAF: web application firewall
   * SSL encryption mode: full, full(strict), off (not recommended), flexible (not recommended)
3. misc
   * no ssh through proxy
