# Linux

使用 LD_PRELOAD 做到符号覆盖

* 临时生效 - LD_PRELOAD=libumem.so.1 ./Test
* 作用于当前终端 - export LD_PRELOAD=libumem.so.1


# Windows

* 注册表项 LoadAppInit_DLLs，所有依赖 user32.dll 的程序

