# Linux

## 从 Console 启动

* ./prog
* ./prog &
  后台运行，不阻塞当前终端
  输出仍然到当前终端

## trace

<span style="color:red">yum install ltrace</span>

* ltrace targetProc
  * 所有动态库导出函数的调用
  * -e 过滤
  * -T 执行时间

* strace targetProc
  * 所有系统调用

# Windows

## 从 CMD 启动

* start /B .\prog.exe
  后台运行
  输出仍然到当前终端

## trace

### ltrace

* Dependency Walker
  * 使用 Profile 功能运行程序
* x64dbg /x32dbg
  * 精准跟踪指定 DLL 的函数调用，可设置断点、查看参数和返回值
  * 如需跟踪所有函数，可使用 Trace 功能
* API Monitor

### strace

* Process Monitor (ProcMon)
* WinDbg
