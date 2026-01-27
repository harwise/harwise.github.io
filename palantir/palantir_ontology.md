# 本体论（Ontology）/ 本体建模  
Ontology 的原始字面意思是 “关于存在的研究” 或 “存在之学”。  
**The original literal meaning of ontology is "the study of existence" or "the science of being."**

---

## Palantir 对 Ontology 的解释  
https://www.youtube.com/watch?v=YDAxITCNcko  

Nouns and verbs that make up your business.  
**构成你业务的名词和动词。**

E.g. A manufactury.  
**例如：一个制造业公司。**

* Plants  
  **工厂**  
* Warehouses  
  **仓库**  
* Products  
  **产品**  
* Customers  
  **客户**

* Supply  
  **供应**  
* Ship  
  **运输**

These words reflect the ground truth about how **your business** operates.  
**这些词反映了关于你的业务如何运作的基本事实。**

Complex inter-connected relationship  
**复杂的互相关联关系**

Model this into an ontology - model how your business is actually operating.  
**将这些建模为本体——建模你的业务实际是如何运作的。**

---

### Data  
The current state of my business  
**我业务的当前状态**

300 out-of-box connectors  
**300 个开箱即用的连接器**  
* enterprise systems  
  **企业系统**  
* Snowflake, Databricks...  
  **Snowflake、Databricks 等**  
* enterprise data lakes  
  **企业数据湖**

---

### Logic  
How do I think about the data  
**我如何理解这些数据**

Integrate with all different tools (model/logic)  
**与各种不同的工具集成（模型/逻辑）**  
* rules-based logic  
  **基于规则的逻辑**  
* ML models  
  **机器学习模型**  
* forecasts  
  **预测**  
* third-party optimizers  
  **第三方优化器**

Model them into the semantic object. e.g.  
**将它们建模为语义对象。例如：**  
* How a warehouse works.  
  **仓库是如何运作的。**  
* The logic how to think about that warehouse.  
  **关于如何理解该仓库的逻辑。**

---

### Actions  
Actions I can take to affect the real world  
**我可以采取的影响现实世界的行动**

* Connect to ERP systems  
  **连接到 ERP 系统**

Drive back those actions into the enterprise.  
**将这些行动反馈到企业中。**

---

## Ontology 独特之处  
The actual digital twin of how my business is operating.  
**业务运作的真实数字孪生。**

The ontology drives decisions in your business.  
**本体驱动你的业务决策。**

The goal: AI and humans working together on the ontology.  
**目标：AI 与人类在本体上协同工作。**

The goal overtime is to automate more and more of your business.  
**长期目标是逐步自动化更多的业务。**

---

以上描述过于 high level 和抽象，可以通过实际的 demo 来结合理解。

---

## 为什么本体不等同于数据模型，分类法，或知识图谱。

本体建模：**语义数据模型，定义领域内的概念、属性、关系及逻辑。规则和定义。可支持推理、语义一致性、跨系统理解。**

https://www.bilibili.com/video/BV1fKUjBAEz2/?spm_id_from=333.788.recommend_more_video.0


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

