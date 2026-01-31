| 工具链阶段 | GCC 工具链核心组件 | Clang/LLVM 工具链对应组件 | MSVC 工具链对应组件 | 核心功能 | 兼容性说明 |
|------------|--------------------|----------------------------|---------------------|----------|------------|
| 编译阶段（前端） | `gcc`/`g++`（C/C++） | `clang`/`clang++`（C/C++/OC） | `cl.exe`（C/C++/CX/WinRT） | 源代码 → 汇编代码/中间代码（IR/IL） | 1. Clang 兼容 GCC 命令行选项；2. MSVC 命令行格式与 GCC/Clang 差异较大（如 `/O2` 对应 `-O2`）；3. Clang 也支持生成 MSVC 兼容的 PE 文件 |
| 汇编阶段 | `as`（GNU Assembler） | `llc`/`llvm-mc`/`llvm-as` | `ml.exe`（x86 汇编）/`ml64.exe`（x64 汇编） | 汇编代码 → 目标文件（.o/.obj） | 1. `llvm-mc` 兼容多数 `as` 语法；2. `ml/ml64` 仅支持微软汇编语法（MASM），与 GNU 汇编（GAS）不兼容；3. MSVC 中 `cl.exe` 可直接调用汇编器，无需手动执行 |
| 链接阶段 | `ld`/`ld.bfd`/`ld.gold` | `lld`（LLVM Linker）/`lld-link`（PE 链接） | `link.exe` | 目标文件+库 → 可执行文件（.exe）/共享库（.so/.dll） | 1. `lld` 支持 ELF/PE 两种格式，`lld-link` 专门兼容 `link.exe`；2. `link.exe` 仅支持 PE/COFF 格式，依赖 Windows 系统库（`kernel32.lib` 等）；3. GCC/Clang 可通过 `-fuse-ld=lld-link` 调用 MSVC 兼容链接器 |
| 标准库（运行时） | `glibc`（C）/`libstdc++`（C++） | `libc++`（C++）/`libc++abi`/`musl libc`（C） | `msvcrt.lib`/`ucrt.lib`（C 标准库）/`msvcprt.lib`（C++ 标准库） | 提供标准库函数接口+系统调用封装 | 1. `ucrt.lib` 是现代 MSVC 的通用 C 运行时，替代老旧 `msvcrt.lib`；2. MSVC 标准库仅支持 Windows 平台，对 C++ 新标准支持略滞后于 Clang；3. Clang 可通过 `-stdlib=libc++` 或 `-mscver` 兼容 MSVC 标准库 |
| 调试工具 | `gdb` | `lldb` | `cdb.exe`（命令行）/`windbg.exe`（图形化）/`vsdebugger`（Visual Studio 集成） | 断点调试、内存查看、调用栈追踪 | 1. `lldb` 支持少量 `gdb` 命令，`cdb/windbg` 命令格式与前两者完全不同；2. `windbg` 支持内核调试，是 Windows 平台调试的权威工具；3. Clang 生成的 PE 文件可直接用 `windbg` 调试 |
| 二进制辅助工具 | `binutils`（`objdump`/`nm`/`strip`/`readelf`） | `llvm-binutils`（`llvm-objdump`/`llvm-nm`/`llvm-strip`/`llvm-readobj`） | `dumpbin.exe`（反汇编/符号查看）/`lib.exe`（库文件管理）/`editbin.exe`（二进制修改）/`link.exe`（符号表处理） | 反汇编、符号表查看、二进制格式转换、库文件打包 | 1. `dumpbin.exe` 对应 `objdump`+`readelf`，是 MSVC 二进制分析的核心工具；2. `lib.exe` 用于打包/解压 `.lib` 静态库，对应 GCC 的 `ar`；3. LLVM 工具支持解析 PE 文件，可替代部分 `dumpbin` 功能 |
| 性能/覆盖率分析 | `gcov`/`gprof` | `llvm-cov`/`llvm-profdata`/`llvm-mca` | `vsperfcmd.exe`（性能剖析）/`OpenCppCoverage`（第三方，代码覆盖率）/`Visual Studio Profiler`（图形化） | 代码覆盖率统计、性能瓶颈剖析、指令流水线分析 | 1. MSVC 无原生代码覆盖率工具，需依赖第三方 `OpenCppCoverage`；2. `vsperfcmd.exe` 对应 `gprof`，功能更强大，支持多核/多线程分析；3. `llvm-cov` 可兼容 MSVC 编译的项目（需开启对应选项） |

---

| 对比维度 | DWARF | PDB（Program Database） |
|----------|-------|-------------------------|
| 核心定位 | 跨平台开放调试信息格式 | Windows 专属闭源调试信息格式 |
| 支持平台 | Linux、macOS、嵌入式、Windows（Clang 支持） | 主要支持 Windows，少量支持 Xbox |
| 支持工具链 | GCC、Clang/LLVM、GDB、LLDB | MSVC、Clang/LLVM（部分支持）、WinDbg、Visual Studio |
| 存储方式 | 可选「嵌入可执行文件」或「单独存储」 | 默认「单独存储为 .pdb 文件」，可选项嵌入 |
| 开源性 | 开放标准，完整文档公开，无版权 | 闭源标准，部分文档公开，微软专属 |
| 存储内容 | 核心调试元数据（行号、变量、函数等） | 核心调试元数据 + 符号表 + 项目配置 + 增量编译信息 |
| 二进制格式适配 | 深度适配 ELF（Linux）、Mach-O（macOS） | 深度适配 PE/COFF（Windows .exe/.dll/.lib） |
| 生成选项（编译器） | GCC/Clang：`-g`/`-g3`/`-g5` | MSVC：`/Zi`/`/Z7`/`/Zd`；Clang：`-gcodeview` |
| 查看工具 | `llvm-dwarfdump`、`readelf`、`objdump` | `dumpbin.exe`、`pdbstr.exe`、Visual Studio |
