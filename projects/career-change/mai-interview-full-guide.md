# MAI Copilot Senior Data Scientist — 面试完整准备手册

---

## 📋 面试环节总览

| 环节 | 内容 | 准备状态 |
|------|------|---------|
| 1. 自我介绍 | 2 分钟成长线 | 🔶 需打磨 |
| 2. 项目经历 | STAR × 3 | 🔶 需补数字 |
| 3. Behavioral | 6 个方向 | 🔶 需准备故事 |
| 4. Statistics | 基础概念 | 🔴 需复习 |
| 5. Causal Inference | DiD/RDD/PSM/IV | 🔶 概念 OK，细节要补 |
| 6. Experiment Design | A/B test 设计 | 🔶 有实践，术语要包装 |
| 7. System Design | 度量体系设计 | ✅ 直接迁移经验 |
| 8. Coding | Python + SQL | ✅ 没问题 |

---

## 1️⃣ 自我介绍（2 分钟）

### 注意事项
- **点到为止**，不展开细节 — 自我介绍是导航地图，面试官会追问感兴趣的
- 每个阶段一句话说清"做了什么类型的事"
- 结尾落在 **"为什么想来 Copilot"** — 要正面（能力延伸），不要负面（现在太苦）
- 展示一条清晰的 **成长线**：全栈开发 → 数据工程 → 数据治理 → 数据科学/度量

### 可以这样说

> "I've been at Microsoft for four years, and my career has evolved from full-stack development to data science and measurement.
>
> I started on Buy with Microsoft, a cross-border e-commerce project where I built backend services from scratch. As the project matured, I shifted to data integration and user growth analytics — building pipelines, dashboards, and growth analysis.
>
> After a strategic transition, I took over Bing Shopping Catalog from the India team, handling billion-scale ETL, data quality governance, and catalog coverage expansion.
>
> Currently I'm on the Price Team, responsible for price accuracy for the Product Tracking feature — our Price Drop Alert. The core challenge is: multiple data sources, limited crawl capacity, and an architecture constraint called Last Write Wins. I built the measurement system end-to-end — sampling framework, debug framework for root cause analysis, and experiment design. For example, I proposed a tolerance-based matching approach that improved Amazon accuracy from 78% to 88%.
>
> Throughout all of this, I've also been the security owner for the team and led Azure tenant migration and big data platform migration, so I'm deeply familiar with Azure infrastructure.
>
> I'm excited about the Copilot team because what I do today — measuring accuracy in noisy, multi-source data with ambiguous ground truth — is structurally the same problem as measuring AI response quality. I want to bring this measurement mindset to a space with higher impact and bigger frontier."

### 中文版（如果是中文面试）

> "我在微软四年，经历了从全栈开发到数据科学的转变。
>
> 最早做 Buy with Microsoft 跨境电商，从零搭后端，后来转做数据集成和增长分析。之后接手了印度团队的 Bing Shopping Catalog，做 billion 级 ETL 和数据质量治理。
>
> 现在在 Price Team，负责 Product Tracking 的价格准确度。核心是在多数据源、有限爬取能力和架构约束下，建立可靠的度量体系。我端到端设计了采样框架、debug framework、还做了实验设计 — tolerance matching 让 Amazon 准确率从 78% 提到 88%。
>
> 同时我一直负责团队的 security 和 Azure 基础设施迁移，对 Azure 生态很熟。
>
> 想加入 Copilot 是因为我做的'价格准确度度量'和'AI 回答质量度量'本质是同一类问题 — 在有噪声的数据和模糊的 ground truth 下建立可靠的 measurement system。我想把这个能力用在更有前景的方向。"

---

## 2️⃣ 项目经历（STAR 格式）

### 注意事项
- 准备 3 个项目，面试官通常深挖 1-2 个
- 每个项目控制在 3-5 分钟
- **一定要有数字**：提升了多少、规模多大、影响多少用户
- 讲的时候强调 **你的决策和思考过程**，不是流水账

### 项目 A: Price Accuracy Measurement System（主打）

**匹配 JD**: metrics, root cause analysis, measurement, ambiguity

> **Situation**: "Product Tracking sends price drop alerts to users. If the price is wrong, we send false notifications and lose user trust. But we had no reliable way to measure how accurate our prices were."
>
> **Task**: "I needed to build an end-to-end accuracy measurement system — from defining what 'accurate' means, to sampling, to diagnosing why things go wrong."
>
> **Action**:
> - "First I mapped out the entire problem space — five layers from data acquisition to domain characteristics. This helped the team see the full picture for the first time."
> - "I designed a dynamic sampling algorithm that distributes our daily quota of 400+ samples across time windows, avoiding concentration bias."
> - "I identified that our sampling was biased toward Amazon, which masked problems in non-Amazon domains. I proposed stratified sampling."
> - "I built a debug framework specifically for our Keepa data source, which is a black box — allowing us to trace individual offer-level discrepancies."
>
> **Result**: "We could finally quantify accuracy by source and domain. We discovered that non-Amazon accuracy was significantly lower than the blended number suggested. This shifted the team's priorities."

### 项目 B: 1% Tolerance Proposal（展示 experiment design）

**匹配 JD**: experimentation, hypothesis testing, data-driven decisions

> **Situation**: "Our accuracy metric used exact match — if system price differed from ground truth by even $0.01, it counted as wrong. This felt overly strict."
>
> **Task**: "I wanted to test whether a small tolerance (1%) would be more meaningful — capturing real errors while ignoring noise."
>
> **Action**:
> - "I analyzed the distribution of price discrepancies. Many mismatches were tiny — rounding differences, shipping inclusion, tax variations."
> - "I proposed a 1% tolerance threshold and ran the analysis on Amazon data as a pilot."
> - "I presented the findings to PM and engineering with clear before/after comparisons."
>
> **Result**: "Amazon accuracy jumped from 78% to 88%. This proved that ~10% of 'errors' were actually noise, not real inaccuracies. The proposal is now being reviewed for broader adoption."

### 项目 C: Catalog Expansion（展示大规模数据能力）

**匹配 JD**: large-scale data, pipeline, data quality

> **Situation**: "After the India team transitioned out, we inherited the Shopping Catalog with coverage gaps."
>
> **Task**: "Expand product catalog coverage across the web while maintaining data quality at billion-scale."
>
> **Action**:
> - "Built and optimized ETL pipelines on Cosmos (MS internal big data platform) processing billions of records."
> - "Implemented quality governance — deduplication, normalization, validation rules."
> - （补充具体做了什么优化）
>
> **Result**: （补充具体 coverage 提升数字）

---

## 3️⃣ Behavioral Questions

### 注意事项
- 微软面试重视 **Growth Mindset** — 展示你在学习、适应、改进
- 每个方向准备一个 **具体故事**，不要泛泛而谈
- 用 STAR 格式回答，控制在 2 分钟内

### 六大方向 + 怎么说

**Q1: "Tell me about a time you influenced a decision without direct authority."**
（考察：Influence without authority）

> 用 tolerance proposal 的故事：
> "我发现 exact match 的准确率定义有问题，但改 metric 涉及 PM 和 engineering 的共识。我没有直接权力改指标，所以我用数据说话 — 分析了价格偏差分布，展示 78%→88% 的提升，让数据证明 tolerance 是合理的。PM 接受了这个方向。"

**Q2: "How do you handle ambiguous problems?"**
（考察：Ambiguity → Structure）

> 用 Price Accuracy 全景梳理的故事：
> "Price accuracy 刚接手时，问题千头万绪 — 没人说得清到底哪里出了问题。我把整个问题分解成 5 层框架（Data Acquisition → Ingestion → Alert → Measurement → Domain），画了一张完整的问题地图。这让团队第一次有了结构化的全局视角，也让我们能按优先级逐层解决。"

**Q3: "What's your biggest impact?"**
（考察：Impact & Ownership）

> 用 measurement system 的故事：
> "之前团队对准确率的衡量是粗糙的 — 一个 blended number，不分 source 也不分 domain。我建了端到端的度量体系后，我们第一次看到 Amazon 的高准确率掩盖了非 Amazon 的问题。这改变了团队的优先级决策。"

**Q4: "How do you work with cross-functional partners?"**
（考察：Collaboration）

> "PM 提了 7 个关于产品追踪问题的大问题，每个都很模糊。我把它们结构化 — 每个问题拆成现状、root cause、action items，然后用这个框架跟 PM 和 engineering 逐个对齐。这让讨论从'感觉有问题'变成了'具体哪里有问题、怎么解决'。"

**Q5: "How do you learn new areas?"**
（考察：Growth Mindset）

> "四年里我从后端开发转到数据工程，再到数据科学。每次转型我都是先上手做，在实践中学。比如 measurement system 设计，我没有统计学背景，但我从实际问题出发 — 采样怎么做、bias 怎么识别 — 然后倒推需要什么理论知识。现在我想进入 AI 产品度量领域，同样的学习方式。"

**Q6: "Tell me about a time something didn't go as planned."**
（考察：Dealing with setback）

> "我们最大的架构问题是 Last Write Wins — 好数据会被坏数据覆盖。我提出过要做 source priority，但这需要 Ads Platform 团队改架构，短期推不动。我没有卡在那里，而是转向能控制的事情 — 从源头减少坏 source 的写入，先断掉了 Organic（延迟 2-3 天的数据源）。不完美，但在约束内是最有效的。"

---

## 4️⃣ Statistics 基础

### 注意事项
- 面试不会考公式推导，但会考 **概念理解 + 实际应用**
- 重点：能不能用自己的话解释，能不能举例
- 常见陷阱：p-value 的错误理解

### 核心概念 + 怎么说

**Hypothesis Testing**
> "我们设一个零假设 H0 说'没有效果'，然后看数据是否有足够证据拒绝它。比如我做 tolerance proposal 时，H0 就是'1% tolerance 不会改善准确率'，数据显示 78%→88%，p-value 很小，所以拒绝 H0。"

**p-value**
> "如果 H0 是对的（真的没效果），我们观察到这么大差异的概率。p < 0.05 说明这个差异不太可能是偶然的。注意：p-value 不是'效果存在的概率'。"

**Confidence Interval**
> "比 p-value 信息量更大 — 不仅告诉你'有没有效果'，还告诉你'效果大概多大'。比如 '准确率提升 8-12%, 95% CI' 比单纯说 'p < 0.05' 有用得多。"

**Power Analysis**
> "实验前算需要多少样本才能检测到预期的效果。Power = 检测到真实效果的概率，通常要 ≥ 0.8。如果样本太少，即使真的有效果也可能检测不到（Type II error）。"

**Multiple Comparison**
> "同时看 10 个指标，至少一个 p < 0.05 的概率是 40%（纯偶然）。所以需要校正，比如 Bonferroni：把 α 除以测试数量。"

---

## 5️⃣ Causal Inference

### 注意事项
- 面试会问 "when to use which method" — 重点是 **选择逻辑**
- DiD 最常用，要能详细讲 + 举例
- IV 知道概念就行，不太会深问

### 选择逻辑（背下来）
```
能做 A/B test？ → 做 A/B（gold standard）
不能 → 有阈值/cutoff？ → RDD
没有 → 有前后 + 对照组？ → DiD
没有 → 有好的 instrument？ → IV
都没有 → PSM（最后手段）
```

### 四大方法 + 怎么说

**DiD (Difference-in-Differences)** ⭐ 最重要

> "比较 treatment 和 control 组的'变化差异'。
> 
> 举例：我们断掉了 Organic source，但只对部分 domain 断了。断了的 domain 准确率 +6%，没断的 +2%。那 Organic 的真实影响 = 6% - 2% = 4%。没断的那 2% 是大盘趋势，不能归因给我们的操作。
>
> 核心假设是 Parallel Trends — 如果没有 treatment，两组趋势应该一样。验证方法：看 treatment 之前两组的趋势是否平行。"

**RDD (Regression Discontinuity)**

> "当 treatment 由一个阈值决定时用。比如 Copilot 的 confidence score > 0.8 才展示回答。那就比较 0.79 和 0.81 附近的用户 — 他们几乎一样，唯一区别是一个看到回答一个没看到。阈值处的跳跃就是 causal effect。"

**PSM (Propensity Score Matching)**

> "没有随机分组时，用特征算每个样本被 treat 的概率，然后按概率配对'长得最像'的样本来比较。比如比较用 Keepa 和不用 Keepa 的 offer，直接比不公平（domain 不同），PSM 可以控制这些差异。局限是只能控制 observed confounders。"

**IV (Instrumental Variables)**

> "找一个只通过 treatment 影响 outcome 的外部变量。实践中好 instrument 很难找。概念上理解就行。"

---

## 6️⃣ Experiment Design

### 注意事项
- 面试常见题：**"How would you design an A/B test for X?"**
- 关键是展示 **完整思考**：从 hypothesis 到 metric 到 sample size 到 pitfalls

### 回答框架

> 1. **Hypothesis**: "我们相信 X 会改善 Y"
> 2. **Primary metric**: 最核心的成功指标
> 3. **Guardrail metrics**: 不能变差的指标（如延迟、crash rate）
> 4. **Randomization unit**: 用户级？session 级？
> 5. **Sample size**: 基于 expected effect size + baseline + power ≥ 0.8
> 6. **Duration**: 要覆盖周期效应（周末 vs 工作日），注意 novelty effect
> 7. **Analysis**: 看 CI 不只看 p-value；检查 segment 差异
> 8. **Pitfalls**: novelty effect, primacy effect, network effect, multiple comparison

### 关键概念 + 怎么说

**Guardrail Metrics**
> "主指标优化了但别的指标崩了就不行。比如优化了回答质量但延迟翻倍 → latency 是 guardrail。实验前就要定好 guardrail 的红线。"

**Novelty Effect**
> "新 feature 刚上时用户因为好奇用得多，过一段时间回落。所以实验要跑够长，至少 1-2 周，看指标是否稳定。"

**Network Effect**
> "如果 treatment 组和 control 组会互相影响（比如社交功能），A/B test 的独立性假设就不成立。这时候可能需要 cluster-based randomization。"

---

## 7️⃣ System Design（度量体系设计）

### 注意事项
- DS 的 system design ≠ engineering system design
- 是设计 **metrics + measurement + monitoring system**
- 你的 Price Accuracy 经验可以直接迁移

### 典型题 + 回答框架

**"Design a quality measurement system for Copilot responses"**

> **Step 1 — 定义 quality 维度**
> "类似我做 Price Accuracy 时把问题分成 5 层，我会把 Copilot quality 分成：
> - Accuracy / Groundedness — 回答对不对
> - Relevance — 回答切不切题
> - Completeness — 回答全不全
> - Latency — 响应快不快
> - Safety — 有没有有害内容"
>
> **Step 2 — 每个维度怎么量化**
> "这就像定义'价格对不对'— 用 exact match 还是 tolerance？对于 Copilot，可能用 human rating（1-5 scale）、automated LLM-as-judge、或 binary pass/fail。需要根据维度选择。"
>
> **Step 3 — Ground Truth 怎么获取**
> "和我遇到的 ground truth 问题一样 — human judgment 有 bias、有延迟、有主观性。需要多 rater + inter-rater agreement 检查。也可以用 automated eval 作为 proxy。"
>
> **Step 4 — 采样策略**
> "直接搬我的经验 — 不能 random sample，需要按 query type、domain、user segment 分层，避免某类 query 主导整体指标（就像 Amazon 主导了我们的准确率）。"
>
> **Step 5 — 实验框架**
> "A/B test + guardrail metrics。primary metric 可能是 user satisfaction，guardrail 是 latency 和 safety。"
>
> **Step 6 — Dashboard & Monitoring**
> "实时监控 + 异常告警。按维度、按 segment 可下钻。类似我建的 Titan dashboard。"

---

## 8️⃣ Coding

✅ 你没问题，Python + SQL 都熟。

可能的题型：
- SQL: window functions, CTEs, join 优化
- Python: pandas 数据处理, scipy 统计检验
- 实战题: "给你一组 A/B test 数据，分析结果"

---

## 🔗 你的经验 ↔ Copilot 的类比（面试中反复用）

| 你做过的 | Copilot 对应 | 用在哪个环节 |
|---------|-------------|-------------|
| Price accuracy metric | Response quality metric | 自我介绍、System Design |
| 多 source 冲突 (LWW) | 多 model/grounding 质量 | 项目经历 |
| Sampling bias (Amazon) | Evaluation bias (query type) | System Design |
| Ground truth 不可靠 | Human judgment 主观 | System Design |
| Domain 特异性 | Task/query 类型差异 | System Design |
| Tolerance proposal | Quality threshold 定义 | 项目经历、Experiment |
| 5 层问题框架 | Quality 多维度分解 | Behavioral (ambiguity) |

---

## 📚 补习资源

| 主题 | 推荐 | 优先级 |
|------|------|--------|
| Causal Inference | *Causal Inference: The Mixtape*（免费在线） | 🔴 高 |
| A/B Testing | Evan Miller's blog / Ronny Kohavi's *Trustworthy Online Controlled Experiments* | 🔴 高 |
| Statistics 复习 | Khan Academy Statistics & Probability | 🟡 中 |
| LLM Evaluation | 搜 "LLM evaluation metrics" 相关 blog | 🟡 中（面试加分） |

---

## ✅ 待完善

- [ ] 打磨自我介绍至顺口（对着镜子练）
- [ ] 每个 STAR 项目补充具体数字/impact
- [ ] Behavioral 六个方向各练一遍
- [ ] Statistics 基础刷一遍
- [ ] 做 1-2 个 mock system design
- [ ] 读 Causal Inference: The Mixtape 前 3 章

---

*Created: 2026-02-25*
