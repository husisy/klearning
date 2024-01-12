# NEMU-PA

1. link
   * [github-io/PA](https://nju-projectn.github.io/ics-pa-gitbook/ics2020/)
2. 缩写
   * PA: Programming Assignment
   * STFW: Search The Fxxking Web
   * RTFM: Reading The Fxxking Manual

## 构建环境

```bash
apt-get install build-essential man gdb git libreadline-dev libsdl2-dev libc6-dev-i386 qemu-system vim
git clone -b 2020 https://github.com/NJU-ProjectN/ics-pa.git ics2020
```

1. 关闭开发跟踪
2. 注释`nemu/src/isa/x86/reg.c/reg_test()`
