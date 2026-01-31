# mount

| 操作目标 | Linux 命令 | Windows 核心命令 | 备注 |
|----------|------------|------------------|------|
| 本地卷挂载 | mount 到节点 <br> `mount /dev/sda1 /mnt/data` | mount 到根或节点 <br> `mountvol C:\mnt\data 卷GUID` <br> `mountvol C: 卷GUID`| 管理员，永久生效 |
| 节点映射到根 | Linux 是单一文件系统树，没有盘符 | `subst E: C:\data`（临时） | subst 重启失效 |
| 网络SMB共享 | `mount -t cifs //ip/share /mnt` | `net use Z: \\ip\share` | 支持账号密码/永久 |
| 网络NFS共享 | `mount -t nfs ip:/data /mnt` | `mount -o anon ip:/data Z:` | 需安装NFS客户端 |
| ISO/虚拟磁盘 | `mount -o loop xxx.iso /mnt` | `Mount-DiskImage -ImagePath xxx.iso` | PowerShell，原生支持 |
| 卸载挂载 | `umount /mnt/data` | `mountvol 路径 /d`<br>`net use Z: /d`<br>`Dismount-DiskImage` | 对应各自挂载命令 |


# 特殊文件系统节点

| Linux 基于内存目录 | Windows 核心等效机制 | 核心访问方式 | 关键特点 |
|--------------------|----------------------|--------------|----------|
| `/dev`（设备节点） | `\\.\` 设备命名空间 + 内核 `\Device\` | 1. 盘符（C:/D:）<br>2. `\\.\XXX` 路径<br>3. Win32 API `CreateFile` | 无实际目录，用户态直接访问，完全等效设备节点 |
| `/proc`（进程/系统状态） | 1. Win10+ `ProcFS`（WSL）<br>2. WMI/`wmic`<br>3. Win32 API<br>4. 资源监视器 | 1. WSL 中直接 `cat /proc/xxx`<br>2. 命令行 `wmic`<br>3. PowerShell `Get-CimInstance`<br>4. Win32 API | 无单一目录，功能完全覆盖，Win10+ 原生兼容Linux ProcFS |
| `/sys`（硬件/驱动配置） | 1. WMI<br>2. 注册表（`HKLM\SYSTEM`）<br>3. IOCTL<br>4. WSL `sysfs` | 1. PowerShell `Get-CimInstance`<br>2. 注册表编辑器/`reg` 命令<br>3. Win32 API `DeviceIoControl`<br>4. WSL 中直接 `/sys` | 功能分散，注册表为静态配置核心，IOCTL 为交互核心 |


# Linux

进程可以通过 chroot 改变它看到的文件系统根

# Windows

格式：psexec64 -w <隔离根目录> -d cmd.exe
示例：将 D:\chroot_root 设为隔离根，启动新的cmd，该cmd仅能访问 D:\chroot_root 内的文件
psexec64 -w D:\chroot_root -d cmd.exe

