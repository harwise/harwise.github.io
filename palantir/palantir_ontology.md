# 本体论（Ontology）/ 本体建模

ontology 的原始字面意思是 “关于存在的研究” 或 “存在之学”。


## Palantir 对 Ontology 的解释

https://www.youtube.com/watch?v=YDAxITCNcko

Nouns and verbs that make up you business.

E.g. A manufactury.

* Plants
* Warehouses
* Products
* Customers

* Supply
* Ship

These words reflects the ground truth about how **your business** operates.

Complex inter-connected relationship

Model this into an ontology - model how your business is actually operating.

### Data

The current state of my business

300 out-of-box connectors
* enterprise systems
* Snowflake, Databricks...
* enterprise data lakes

### Logic

How do I think about the data

Integrate with all different tools (model/logic)
* rules-based logic
* ML models
* forecasts
* third-party optimizers

model them into the semantic object. e.g.
* How a warehouse works.
* The logic how to think about that warehouse.

### Actions

Actions I can take to affect the real world

* 连接到 ERP 系统
* ...

Drive back those actions into the enterprise.



## Ontology 独特之处

The actual digital twin of how my business is operating.

The ontology drives decisions in your business.
the goal: AI and humans working together on the ontology.
the goal overtime is to automate more and more of your business.


## 和其它 AI 模型的比较

https://www.bilibili.com/video/BV1fKUjBAEz2/?spm_id_from=333.788.recommend_more_video.0

为什么本体不等同于数据模型，分类法，或知识图谱。

对数据分析/数据架构理解的不同阶段

1. 把数据整合，用于制作报表或者商业智能（BI）分析
    * 典型的，关系型数据库
    * 以低延迟高效地提供数据服务，服务大量的用户
    * 主要考虑的是读取数据
      * lock，数据一致性
      * 使用场景基本是 read-only

2. 需要写操作：take insights 并将其写入数据库
    * 难点：用户写入 insights 数据，如何管理
        * 多人协作，且不同模式的写入
        * Orchestration 数据编排
        * 版本控制 - 数据变化的管理
        * 不同于系统/程序写入数据，后者在内部有对数据的处理逻辑/调和/编排
3. 从 Write 再到 Operational
    * 关键点
        * 建模：objects，relations，**actions**
        * 捕捉 actions 产生的影响，写回到系统

* 解决：在众多的数据库源之上构建了一层 - the ontological layer
    * 不止展现语义化和动态的视图（semantic and kinetic）
    * 接收写入操作 - with all the relevant metadata required
    * data + actions + processes
    * 不同的用户能对目标数据执行哪些流程
    * 这些流程级联得到的最后结果，会被本体捕捉，并写回到底层系统中
    * 也就是说，同时对 objects 和 processes 进行建模

* 相似类比：情报（IC）领域的一个例子 
    * for both legal and practical reasons，数据被用不同方式 indexing - 或者说 abstration
    * 工作在这个抽象层上
    * 这个抽象层才是 reality

* 技术和业务定位
    * 不是 data integration layer
    * 不是 model integration layer
    * 以上的能力我们 10 年前就已经有了
    * 价值在于，在这些基础上，延伸到实际业务运营 (Operations)
        * 通过上云，以及工具的使用，分析工作/BI/Dashboarding 已经解决
        * 下一个问题自然就是：如何投入生产运营？(get into operation)
        * 知道问题所在 -> 能够着手解决
        * field-driven learning: 对来自一线的经验反馈进行整合
        * 最重要的核心数据是：终端用户在不同场景下做出的决策
        * 给我的整体印象：动态，接收反馈，不断演进的系统

