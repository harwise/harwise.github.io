# Foundry Use Cases





# Insights

* 数据的使用
  * 先有对业务的理解 - 提取 objects
    * Device，CPU，Memroy，storage disk，network adaptor ...
    * Application，Screen, Window
  * 数据是 objects 的状态
    * storage disk - 厂商，容量，读写速率...
    * Application - 活动时间，故障次数，active 时间
  * 数据分析，发现规律
    * 某设备型号故障率明显高
    * 某硬件型号和某软件故障关联性较高

* 把管理员的操作考虑进来
  * 预测此操作产生的影响
    * 更换掉某个硬件后，整体上设备故障率会降低多少
    * 重启某一台设备，估计要花多少时间

------------------------------------------------------

bin_version                 - 根据过去经验，使用 GetFileVersionInfoEx API
app_name                    - 根据过去经验，使用类似 GetFileVersionInfoEx & GetPackageFullName
pkg_full_name               - 根据过去经验，使用 GetPackageFullName API
pkg_display_name            - 暂时没找到直接的 API 调用，可以通过 xml 解析获得
pkg_app_id                  - 暂时没找到直接的 API 调用，可以通过 xml 解析获得


关于 cache：
以前的经验：隔一段时间整体清理一次 cache，依据的规则是某个 cache item 长时间没有被用到；
现在的计划：
1. 先不加 cache，实现基本功能；
2. 考虑使用 LRU Cache（最近最少使用缓存）
