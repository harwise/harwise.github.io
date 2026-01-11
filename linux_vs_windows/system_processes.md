# Linux

* 进程 0 (idle)
  * 从无到有的一个内核线程
  * 使用静态分配的数据结构
  * 创建出来 *init* 进程后，执行 *cpu_idle* 函数 (重复执行 *hlt* 汇编指令)
  * 只运行在内核态
  * 每个 CPU 都有一个进程 0

* 进程 1 (init)
  * 通过 *start_kernel* 被启动
  * **一开始是临时内核线程**
  * 执行 *init* 函数，其依次完成内核初始化
    * TODO
    * TODO
  * *init* 通过 *execve* 装载可执行程序 */sbin/init* 或 *systemd*，**成为一个普通进程（有用户态了）**
  * 一直存活，创建和监控所有进程的活动
    * 如果 *init* 发生 crash，内核会 panic
    * 通过 <span style="color:red">pstree</span> 可以看到它是所有进程的祖先


# Windows

* 进程 0 (System Idle Process)
  * 严格来说不是进程
  * 每个 CPU 一个线程

* 进程 4 (System)
  * **内核模式系统线程**

* 第一个 smss 会话管理器
  * 是受保护进程轻型 (PPL)
  * **第一个用户模式进程**
  * 一直存活，等待 session 0 的 csrss 子系统退出
    * 如果拿不到 csrss 句柄，内核会崩溃

**以下内容 Linux 都没有**

<div style="border: 2px solid">

* 为每一个 session 启动一个临时的 smss
  * 创建每个 session 的 csrss 子系统进程
  * *wininit* for session 0
  * *winlogon* for user sessions
  * smss 任务完成后就退出，所以以上进程都没有父进程

* wininit
  * 启动 *Services.exe* 会话控制管理器
    * TODO
  * 启动 *lsass.exe* 本地安全身份验证子系统服务
  * 启动 *lsaIso.exe (LSA Trustlet)*
  * 等待系统关机请求

* winlogon
  * 负责登录，注销，SAS (即 Ctrl+Alt+Delete)
  * 启动 *LogonUI.exe* 完成身份验证的 UI 交互，然后此 UI 进程退出
  * 发送给 *lsass* 进行验证
  * *lsass* 生成此用户的访问令牌，用此令牌启动 *Userinit.exe* (注册表可配置启动哪一个程序)

* Userinit
  * 用户环境的初始化工作
  * 运行 Shell，即 *Explorer.exe* (注册表可配)
  * 完成任务后退出，所以 *Explorer.exe* 也没有父进程

<div>
