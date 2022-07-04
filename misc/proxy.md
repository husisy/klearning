# note

写在开头

1. **禁止**用该方法访问违反相关法律法规的内容
2. 请**不要**用该方法访问黄赌毒等内容
3. 请**不要**用该方法访问政治敏感内容
4. 建议的使用场景：
   * 访问学术内容
   * 学习非中文课程
   * 学习计算机技能
   * 等
5. 出于安全考虑，**不**建议在未知网络环境中输入敏感内容（例如身份证号码，银行卡密码等）

## VPS-proxy

假设读者掌握基础的linux命令行技巧：例如ssh连接，linux上的文件编辑

1. 购买VPS服务器
   * amazon web service (aws)
     * 选择aws lightsail, `3.5USD/month`，首月免费
     * 由于aws不面向中国大陆个人提供服务，需要绑定境外手机号方可注册（自行找同学借手机号注册）。服务器连接稳定性好，大多数ip可以访问谷歌学术
   * vultr [link](https://www.vultr.com/)
     * 选择New York，`3.5USD/month`，按日计费
     * 大多数ip不可访问谷歌学术
   * 其他
2. 本地ssh连接购买的VPS服务器
   * `ssh username@ip`: 其中`username`替换为**你**的用户名，`ip`替换为**你**的ip，这些信息可以在你购买服务器的页面找到
   * （可选）建议使用公钥私钥的方式登录，可以省去登录密码的麻烦，[阮一峰/ssh原理与应用](https://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html)
   * （可选）出于安全考虑，建议禁用密码登录 [askubuntu/how-to-disable-password](https://askubuntu.com/questions/435615/disable-password-authentication-in-ssh)
3. 在服务器上安装`proxy.py` [github/proxy.py](https://github.com/abhinavsingh/proxy.py)，操作系统ubuntu-20.04大概的命令如下
   * `sudo apt update`
   * `sudo apt upgrade`
   * `sudo apt install python3-pip`
   * `pip3 install proxy.py`
4. 在服务器上启动`proxy.py`，命令为`proxy --port 23333`
   * 关于`ip/port`的说明 [wiki/port(computer)](https://en.wikipedia.org/wiki/Port_(computer_networking))
   * （可选）该命令需要一次保持执行，故不能关闭当前ssh窗口，故建议将该命令后台运行`nohup proxy --port 23333 &` [ubuntu/nohup-howto](http://manpages.ubuntu.com/manpages/bionic/man1/nohup.1.html)
5. 从本地再发起一个ssh连接到服务器 `ssh -L 23333:127.0.0.1:23333 username@ip`
   * 其中`username`替换为**你**的用户名，`ip`替换为**你**的ip
   * 关于端口转发的讲解 [阮一峰/ssh的原理与应用之端口转发](https://www.ruanyifeng.com/blog/2011/12/ssh_port_forwarding.html) [ubuntu/port-forwarding](https://help.ubuntu.com/community/SSH/OpenSSH/PortForwarding)
6. 打开本地的firefox（Safari/chrome类似）
   * 在设置页面找到`General/network-settings/settings`
   * 勾选`manual proxy configuration`
   * 在`http proxy`一栏中输入`127.0.0.1`，之后的`Port`输入`23333`
   * 勾选上also use this proxy for HTTPS
   * 勾选上enable DNS over HTTPS
   * 至此firefox便可以访问谷歌
7. （可选）系统级别的http-proxy
   * windows在设置中找到`network-settings/proxy`，勾选上use a proxy server，address输入`127.0.0.1`，Port输入`23333`
   * linux命令行环境执行`export http_proxy="http://127.0.0.1:23333"`, `export https_proxy="http://127.0.0.1:23333"`
   * android在wifi连接页面可以执行proxy设置，但需要在应用商店中搜索提供ssh-port-forwarding功能的应用
   * mac未测试
   * iphone未测试

支持http-proxy便已经建立好了

## VPS-shadowsocks

shadowsocks软件提供socks5-proxy [github/shadowsocks](https://github.com/shadowsocks/shadowsocks/tree/master) 待补充

## VPS-v2ray

v2ray的社区支持人员相比shadowsocs更多，也许是未来的趋势 [github/v2ray-step-by-step](https://github.com/v2fly/v2ray-step-by-step) 待补充

## 结尾

1. 安全和便捷是对立的：以上步骤是繁琐的，安全程度大概会稍微高一些吧
