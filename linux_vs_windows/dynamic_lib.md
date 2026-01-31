# 动态库编译

Linux 编译的时候需要使用 -fPIC 选项，用于生成 Position Independent Code，生成如下元素
* PLT：Procedure Linkage Table
* GOT：Global Offset Table

# 动态库加载

| 对比维度 | Windows（.dll） | Linux（.so） |
|----------|----------------|--------------|
| 核心加载器 | `ntdll.dll` 内置加载模块（Windows 内核） | `ld.so`/`ld-linux.so.2`（用户态动态链接器） |
| 本地目录优先级 | 程序当前工作目录（`.exe` 所在目录，高优先级） | 编译时指定的 `DT_RUNPATH`（低于 `LD_LIBRARY_PATH`） |
| 用户自定义目录 | 依赖 `PATH` 环境变量（同时查找 `.exe` 和 `.dll`） | 1. 临时：`LD_LIBRARY_PATH`（仅查找 `.so`）<br>2. 永久：`/etc/ld.so.conf.d/` + `ldconfig` 缓存 |
| 系统目录处理 | 32/64 位隔离（`System32`=64 位，`SysWOW64`=32 位） | 无隔离，通过目录区分（`lib`=32 位，`lib64`=64 位） |
| 系统缓存机制 | 无专门缓存，每次运行都遍历目录（速度较慢） | 有 `/etc/ld.so.cache` 缓存（`ldconfig` 生成，速度较快） |
| 兜底目录 | `%SystemRoot%`（`C:\Windows`） | `/lib`/`/lib64`、`/usr/lib`/`/usr/lib64` |
| 关键调试工具 | `dumpbin.exe`、`Process Monitor` | `ldd`、`ldconfig`、`LD_DEBUG` |
| 安全限制 | 无特殊限制（`PATH` 优先级高，易被恶意 `.dll` 劫持） | 调试 `setuid`/`setgid` 程序时，忽略 `LD_LIBRARY_PATH`（防止恶意劫持） |
| 部署推荐方式 | 自定义 `.dll` 放入 `.exe` 同目录（最简单、最安全） | 1. 自定义目录放入 `/usr/local/lib`，执行 `ldconfig` 更新缓存<br>2. 编译时用 `-Wl,-rpath,$ORIGIN` 指定相对目录 |

# 动态库注入


Linux，使用 LD_PRELOAD 做到符号覆盖

* 临时生效 - LD_PRELOAD=libumem.so.1 ./Test
* 作用于当前终端 - export LD_PRELOAD=libumem.so.1


Windows，注册表项 LoadAppInit_DLLs，所有依赖 user32.dll 的程序


# 调试动态库加载

| Linux `LD_DEBUG` 功能 | Windows 对应方案 | 核心工具/环境变量 | 适用场景 |
|-----------------------|------------------|-------------------|----------|
| `libs`（查看库查找/加载过程） | 查看 `.dll` 查找/加载流程 | `dumpbin.exe`（/dependents）、Process Monitor（ProcMon） | 日常排查 `.dll` 找不到、加载失败等基础问题 |
| `symbols`（查看符号解析过程） | 查看 `.dll` 导入/导出符号、符号绑定结果 | `dumpbin.exe`（/imports /exports）、WinDbg（`x`/`ln` 命令） | 排查符号缺失、同名符号冲突等问题 |
| `reloc`（查看重定位过程） | 查看 `.dll` 内存重定位、地址绑定细节 | WinDbg（`sxe ld` 命令、内存地址分析） | 排查 `.dll` 加载后地址冲突、重定位失败等底层问题 |
| `bindings`（查看符号延迟绑定过程） | 查看函数第一次调用时的符号解析、绑定过程 | WinDbg（调用栈分析、断点调试） | 排查 `.dll` 函数第一次调用崩溃、延迟绑定失败等问题 |
| `all`（全量输出动态链接所有信息） | 全量跟踪动态链接完整流程（加载→符号→重定位→绑定） | WinDbg（完整调试会话） | 复杂、难以定位的底层动态链接问题排查 |
| 环境变量直接输出调试信息（无需额外工具） | 控制台直接输出 `.dll` 加载相关调试日志 | `LOADER_DEBUG`（环境变量，值设为 1） | 简单问题快速排查（仅支持调试版 Windows、控制台程序） |

