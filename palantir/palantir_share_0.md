# Palantir 介绍

NotebookLM audio link

[palantir_overview](./palantir_overview.md)



# 本体论 - 业务角度

[palantir_ontology - 本体建模](./palantir_ontology.md#本体论ontology-本体建模)

充满了抽象的名词和概念



# Foundry 

从实际的软件使用方法中，可以具象化以上名词和概念

[foundry demo](./palantir_foundry.md)



# 本体论 - 工程师角度

[palantir_ontology - 数据分析/数据架构的演进](./palantir_ontology.md#为什么本体不等同于数据模型分类法或知识图谱)



# FDE：前沿部署工程师

Palantir 产品迭代模式：把工程师部署到客户现场，快速解决复杂问题并将实践反哺产品，形成 “现场定制 + 总部抽象” 的闭环。

[Forward Deployed Engineer](./palantir_foundry.md)



# 启发

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
