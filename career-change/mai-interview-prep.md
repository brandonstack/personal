# 面试准备 — MAI Copilot Senior Data Scientist

## JD 来源
Microsoft AI (MAI) Copilot 团队 Senior Data Scientist

---

## 星的四年微软经历

### Phase 1: Buy with Microsoft（~2年）— 从 0 到 1 的电商项目
- **角色**：后端开发 → 数据分析
- **前期**：跨境电商项目，从零构建，后端开发（Falcon, ASP.NET）
- **中后期**：转向 data integration + user growth 分析
  - PowerBI dashboard 做增长分析
  - Build pipeline，数据集成与分析
- **技术栈**：Cosmos DB, Data Factory, Service Bus, Synapse, Spark, Cosmos (MS internal big data), ADX

### Phase 2: Bing Shopping Catalog（战略接手）
- **背景**：战略收缩后接手印度团队的 catalog 业务
- **职责**：Shopping Catalog Expansion
  - Billion 级数据 ETL
  - 质量治理
  - 提升全网 product catalog coverage

### Phase 3: Price Team（当前）— Price Accuracy
- **职责**：Price accuracy 增长 + Price Drop Notification 项目
- **核心工作**：
  - Measurement system 设计（采样框架、accuracy metric）
  - 问题诊断（多 source 冲突、Keepa debug framework）
  - Experiment design（1% tolerance proposal: Amazon 78%→88%）
  - Dynamic sample rate algorithm 设计
- **技术栈**：ADX, Titan Dashboard, Cosmos + SCOPE

### Infra 经验（贯穿全程）
1. **PME Migration** — 所有 Azure resources 从 Microsoft tenant → PME tenant
2. **Security Owner** — 接手印度团队后整个 Shopping team 的 security
3. **MT Migration** — 代表 catalog team 调研 Bing 内部大数据平台（Spark, Kafka, Flink），已迁移数个 pipeline

→ 证明：Azure 深度熟悉（权限管理、tenant 管理、资源使用）+ 大数据平台实操

---

## 成长线

```
全栈开发 → 数据工程/分析 → 大规模数据治理 → 数据科学/度量体系
                                               ↑ 当前位置
基础设施线：Azure infra + security + 大数据平台迁移（贯穿全程）
```

---

## JD 匹配分析

### 强匹配 ✅
- **Metrics / Dashboard / Monitoring** — Price accuracy measurement, PowerBI, Titan Dashboard
- **Root cause analysis** — Keepa debug framework, 多 source 问题诊断
- **Experimentation** — 1% tolerance proposal (hypothesis → data → recommendation)
- **Cross-functional** — PM(Miao), Engineering, 多 stakeholder 协调
- **Ambiguous problems** — Price accuracy 千头万绪就是 ambiguity
- **Python + SQL + large-scale data** — Cosmos, Spark, ADX, billion 级 ETL
- **Azure / cloud platforms** — 极其熟悉，security owner + PME migration 证明
- **Data pipeline** — Data Factory, Cosmos pipeline, MT migration

### 需要突出/补强 🔶
- **Causal inference / statistical modeling** — 有实践，理论需准备
- **LLM evaluation / AI product analytics** — 讲出 Copilot 连接（见下）
- **Experimentation rigor** — 需要用统计语言包装（p-value, power analysis 等）

---

## 面试叙事策略

### 自我介绍（2 分钟）

**核心叙事：从 builder 到 measurer，从电商到 AI**

> "我在微软四年，经历了从全栈开发到数据科学的完整转变。
>
> 最开始做 Buy with Microsoft 跨境电商项目，从零构建后端，后来转向 data integration 和 user growth 分析。之后接手了 Bing Shopping Catalog，做 billion 级数据的 ETL 和质量治理。
>
> 现在在 Price Team，负责 Product Tracking 功能的价格准确度。这个工作的核心是：在多数据源、有限 crawl 能力、和架构约束下，建立可靠的 measurement system。我设计了采样框架、建了 debug framework 做 root cause analysis，也做 experiment design — 比如提出 tolerance-based matching，让 Amazon 准确率从 78% 提升到 88%。
>
> 同时我一直在做基础设施工作 — Azure tenant 迁移、security owner、大数据平台迁移 — 所以对 Azure 和生产环境非常熟悉。
>
> 我想加入 Copilot 团队，是因为我做的 '价格准确度度量' 和 'AI response 质量度量' 本质上是同一类问题 — 在 noisy data 和 ambiguous ground truth 下建立可靠的 measurement 和 experimentation 体系。我想把这套能力用到更有前景的方向上。"

### 项目 STAR 准备（3 个）

**A: Price Accuracy Measurement System（主打 — 最匹配 JD）**
- S: Product Tracking 需要准确价格，但没有可靠衡量体系
- T: 建立端到端的 accuracy measurement
- A: 动态采样算法、识别 sampling bias、分层采样提案、debug framework
- R: 量化了各 source/domain 准确率，发现 Amazon 掩盖 non-Amazon 问题

**B: 1% Tolerance Proposal（展示 experiment design）**
- S: Exact match 准确率低，但很多"不匹配"其实是微小偏差
- T: 验证 tolerance 是否合理
- A: 数据分析 → 提出 1% threshold → Amazon 验证
- R: 78%→88%，证明很多 mismatch 是 noise 不是 error

**C: Catalog Expansion（展示大规模数据能力）**
- S: 接手印度团队，catalog 覆盖不足
- T: 提升全网 product catalog coverage
- A: Billion 级 ETL pipeline, 质量治理
- R: Coverage 提升（补充具体数字）

### AI 兴趣 & Copilot 连接

| 你的经验 | Copilot 对应 |
|---------|-------------|
| Price accuracy metric | Response quality metric |
| 多 source 冲突（LWW） | 多 model/grounding source 质量 |
| Sampling bias | Evaluation bias |
| Ground truth 不可靠 | Human judgment 主观性 |
| Domain 特异性 | Task/query 类型差异 |
| Tolerance proposal | Quality threshold 定义 |

### 技术面准备清单

- **Statistics**: hypothesis testing, p-value, CI, power analysis, multiple comparison correction
- **Causal inference**: DiD, RDD, IV, propensity score matching
- **Experiment design**: sample size calc, metric selection, guardrail metrics, novelty effect
- **Coding**: Python (pandas, scipy, statsmodels) + SQL ✅ 没问题
- **System design**: metrics pipeline, dashboard, telemetry

---

## 技术知识详解

### Causal Inference 四大方法

**选择逻辑：**
```
能做 A/B test？→ 做 A/B（gold standard）
不能 → 有阈值/cutoff？→ RDD
没有 → 有前后 + 对照组？→ DiD
没有 → 有好的 instrument？→ IV
都没有 → PSM（最后手段）
```

**1. DiD (Difference-in-Differences)** ⭐ 最常用
- 比较 treatment 组和 control 组的"变化的差异"
- 例：断 Organic 后，断了的 domain +6%，没断的 +2%，DiD = +4%
- 核心假设：**Parallel Trends** — 没有 treatment 的话两组趋势应一致
- 星的经验：断 Organic 就是 DiD，只是没用这个名字

**2. RDD (Regression Discontinuity)**
- 当 treatment 由阈值决定时，比较阈值两边
- 例：confidence > 0.8 展示，< 0.8 不展示 → 比较 0.79 vs 0.81 的结果
- 适用：有 hard cutoff 的场景

**3. IV (Instrumental Variables)**
- 找一个"只通过 treatment 影响 outcome"的外部变量
- 实践中不太常用，好 instrument 难找
- 面试知道概念即可

**4. PSM (Propensity Score Matching)**
- 没有随机分组 → 人工配对"长得最像"的样本
- 用特征算每个样本被 treat 的概率（propensity score），按 score 配对后比较
- 最后手段，因为只能控制 observed confounders

### Statistics 基础（面试语言）

- **Hypothesis testing**: H0（无效果）vs H1（有效果），用数据决定拒绝还是不拒绝 H0
- **p-value**: 如果 H0 成立，观察到这么极端结果的概率。**不是**"效果存在的概率"
- **Confidence Interval**: 真实效果有 95% 概率落在此区间。比 p-value 信息量更大（含 effect size）
- **Power Analysis**: 实验前算需要多少样本。Power = P(检测到真实效果) = 1-β，通常 ≥ 0.8
- **Multiple Comparison**: 同时看 N 个指标，假阳性风险上升 → Bonferroni correction（α/N）

### Experiment Design 关键概念

- **Sample size calculation**: 基于 expected effect size + baseline variance + desired power
- **Metric selection**: Primary metric（核心目标）+ Guardrail metrics（不能恶化的指标）
- **Guardrail metrics**: 例：优化质量但延迟暴涨 → latency 是 guardrail
- **Novelty effect**: 新 feature 刚上用户好奇用得多，后来回落 → 实验要跑够长
- **Primacy effect**: 老用户习惯旧版，新版初期指标偏低 → 也需要时间

### Behavioral Questions 准备方向

**JD 暗示的考察点：**

1. **Influence without authority** — 你怎么推动跨团队的事？
   → 用 tolerance proposal / 断 Organic 的故事：数据说服 PM 和 Engineering

2. **Ambiguity** — 面对模糊问题怎么办？
   → Price accuracy 本身就是模糊的（什么叫"对"？tolerance 多少？）
   → 你把它结构化了（思维导图 / 5 层框架）

3. **Impact & ownership** — 端到端做了什么？
   → Measurement system 从定义 metric → 采样 → debug → proposal 全链路

4. **Collaboration** — 怎么跟不同角色合作？
   → PM(Miao) 的 7 个问题 → 你结构化回复
   → Engineering 推动断 Organic

5. **Growth mindset** — 怎么学习新领域？
   → 从后端开发转到数据科学，每个阶段都在学新东西
   → 主动了解 AI/LLM evaluation（为什么想来 Copilot）

6. **Dealing with failure / setback** — 遇到挫折怎么办？
   → LWW 推不动（架构债务不是你能改的）→ 转而从源头减少坏数据

### 可能的 System Design 面试题

DS 的 system design 不是写代码，是设计 **metrics + measurement system**：

**典型题：** "Design a quality measurement system for Copilot responses"

你的回答框架（直接迁移你的 Price Accuracy 经验）：
1. 定义 quality 的维度（accuracy, relevance, latency, safety — 类似你的 5 层框架）
2. 每个维度怎么量化（metric definition — 类似 exact match vs tolerance）
3. Ground truth 怎么获取（human eval? automated eval? — 类似你的 sampling + GT 问题）
4. 采样策略（避免 bias — 按 query type/domain 分层，类似 Amazon/non-Amazon）
5. 实验框架（A/B test + guardrail metrics）
6. Dashboard & monitoring（类似你建的 Titan dashboard）

---

## 待完善
- [ ] 打磨自我介绍至顺口
- [ ] 每个 STAR 项目补充具体数字/impact
- [ ] 模拟 behavioral questions（每个准备一个具体故事）
- [ ] Statistics 刷题（推荐：Brilliant.org 或 Khan Academy 的 AB testing 模块）
- [ ] 练习 system design：Design metrics for X（X = Copilot / Search / Recommendation）
- [ ] Causal inference 实战理解（推荐：Causal Inference: The Mixtape — 免费在线书）

---

*Created: 2026-02-25*
*Last updated: 2026-02-25*
