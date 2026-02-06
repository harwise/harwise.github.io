# foundry - demo

https://www.bilibili.com/video/BV1uDqVBjED8

https://www.bilibili.com/video/BV1fxU4BFESU

**企业操作系统**

![alt text](image.png)





---

**数据连接器（connectors）** 


![alt text](image-1.png)


每个节点对数据进行 refining，cleaning，joining，applying business logic


**例子-和工厂相关联的具体数据：**

制造业企业，为了完成了解一个工厂，可能的数据有：

![alt text](image-20.png)






**Data Versioning**

![alt text](image-2.png)

![alt text](image-3.png)


**Software-defined data integration**

![alt text](image-4.png)

比如对于 SAP 数据，通过其 NetWeaver 应用层，可以自动生成 pipeline，甚至 objects，在**数小时之内**。手动的话需要几个礼拜甚至几个月。

之前截图中的绿色节点就是这样生成的。





---

Data Integration 之后，业务/管理人员需要参与进来，和 IT 人员一起定义 Objects (包括 Links)

**Object**

![alt text](image-5.png)

![alt text](image-6.png)

![alt text](image-7.png)


**Object Exploration**

![alt text](image-8.png)

![alt text](image-9.png)


基于定义好的 Objects，可以做各种图表，timeline，map view 等展现形式。略...


**例子-制造业企业的 Objects 有：**

![alt text](image-21.png)

---

**Modeling**

使用内置的 data science tool 来创建一个模型：

![alt text](image-10.png)


**Model Library**

Objective

![alt text](image-11.png)

Model Comparisons

![alt text](image-12.png)

![alt text](image-13.png)

**将 Model 加入到本体中**

输入来自于 Objects；将输出传给 Objects


**例子-Supply Chain Control Tower：**

* 模型 1：生产和定价模型
  * 数据：原材料
  * 数据：工厂产能数据
  * 根据价格变动 -> 估计产量和客户需求

用户利用此模型决定：对于一批原材料，决定要生产产品的数量

* 模型 2：季节性需求模型

模型 1 和 2 结合 (chain)，动态优化产品目录，提高营收

![alt text](image-22.png)

**例子-模型相关关联使用（chained）**

* 模型 1：客户需求预测模型
  * 输入 - 原材料订单 的 price 属性
  * 输入 - 物料 的 cost 属性
  * 输出 - demand（需求量？）
  * 输出 - 工厂 的 capacity 属性 (产能？)
  * 输出 - 物料 的 <span style="color:red">inventory</span> 属性 （库存？）

* 模型 2：生产模型
  * 输入 - <span style="color:red">inventory</span>
  * 输入 - demand
  * 输入 - base quality
  * 输出 - capacity
  * 输出 - production
  * 输出 - stock

---

**Operation**

例子：一个 Application，其包含的一个 model pipeline，产生了一个 Alert

![alt text](image-14.png)

此时需要 take actions，比如 取消关联的订单


**Action**

因为 Objects 之间复杂的关联关系，Action 必须属于 Core Level 中处理，和 Objects，Relations 是同一个级别

![alt text](image-15.png)

Action 可以更新 Objects

![alt text](image-16.png)

可以把数据同步回到 ERP 系统中

---

**Digital Twin**

Data-Driven Operations and Decision-Making

Birds eye view of the entire value chain

![alt text](image-17.png)

**Simulation**

在此图中，比如左边的供应商如果停止供货，比如右边的顾客需求暴增，我们如何调整整个系统？

The sandbox verion of your world，应该把 Models 放到一起来看。

![alt text](image-19.png)


**use cases 例子**

* 如果供应商只交付了 50% 的原材料，对产品的准时交付产生怎样的影响？哪些客户受到的影响最大？

