# 操作系统

1. link
   * [学堂在线-清华大学-操作系统](https://next.xuetangx.com/course/THU08091000267/1516699)
   * [清华大学计算机系统操作系统系列课程主页](http://os.cs.tsinghua.edu.cn/oscourse)
   * [github-ucore-os-lab](https://github.com/chyyuu/ucore_os_lab)
   * ucore, ucore+
   * [@book/Operating-Systems-Three-Easy-Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/)
   * [ucoreOS](https://learningos.github.io/ucore_os_webdocs/)
   * [github/learningOS](https://github.com/LearningOS)
2. concept: 操作系统结构，中断及系统调用，内存管理，进程与线程，处理机调度，同步互斥，文件系统，IO子系统
3. 并发，共享，虚拟，异步
4. x86-32
   * 实模式，保护模式，SMM模式，虚拟8086模式
   * 物理地址空间，线性地址空间，逻辑地址空间
   * 控制寄存器，系统地址寄存器，调试寄存器，测试寄存器
   * 通用寄存器：累加器EAX，基址寄存器EBX，计数器ECX，数据寄存器EDX，源地址指针寄存器ESI，目标地址寄存器EDI，基址指针寄存器EBP，堆栈指针寄存器ESP
   * 段寄存器：代码段CS (Code Segment)，数据段DS (Data Segment)，附加数据段ES (Extra Segment)，堆栈段SS (Stack Segment)，附加段FS，附加段GS
   * 指令指针寄存器EIP
   * 标志寄存器EFLAGS

## 第三讲 启动、中断、异常与系统调用

1. 计算机体系结构：CPU、内存、IO设备
2. BIOS
   * 工作在实模式
   * 功能：基本输入输出的程序、系统设置信息、开机后自检程序、系统自启动程序、字符显示、磁盘扇区读写、检测内存大小、键盘输入
   * 代码段寄存器CS，指令指针寄存器EIP
   * BIOS(1MB) -> 主引导记录扇区代码(512byte) -> 活动分区扇区代码 -> 加载程序bootloader
   * 将加载程序bootloader从磁盘的引导扇区（512字节）加载到`0x7c00`，并跳转到`0x7c00`
   * 加载程序将操作系统的代码与数据从硬盘加载到内存，并跳转到操作系统的起始地址
   * 扩展系统配置数据ESCD
   * 系统自检POST
   * 进化方向: BIOS -> BIOS-MBR -> BIOS-GPT -> PXE -> UEFI
3. 中断：用户的键盘输入是任意时间的
4. 异常：代码可能出现运行时才能确定的错误（例如除零）
5. 系统调用：在计算机运行时，内核时被信任的第三方，用户代码是不被信任的，用户代码执行特权指令只能通过内核提供的API
6. 内核与外界的所有交互（统称中断）
   * 系统调用system call：应用程序主动向操作系统发出的服务请求；同步或异步
   * 异常exception：非法指令或者其它原因导致当前指令执行失败（如内存错误）后的处理请求；同步
   * 中断hardware interrupt：来自硬件设备的处理请求；异步

```bash
sudo apt udpate
sudo apt upgrade
sudo apt install qemu-system git build-essential
```

## The Missing Semester of Your CS Education

TODO: 转移至`learning/linux/shell`

1. link
   * [course-website](https://missing.csail.mit.edu/)
   * [course/chinese-version](https://missing-semester-cn.github.io/)
   * [GNU-bash-documentation](https://www.gnu.org/software/bash/manual/html_node/index.html#SEC_Contents)
   * [wiki/shebang](https://en.wikipedia.org/wiki/Shebang_(Unix))
2. lecturer: Anish, Jon, Jose
3. 总时长`11x1 hour`

## 操作系统-蒋炎岩

1. link
   * [Yanyan-操作系统](http://jyywiki.cn/ICS/2020/)
   * [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/)
