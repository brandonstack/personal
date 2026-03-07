# 简历草稿

> ⚠️ 保密文档，不对外分享

---

## 📌 基本信息

- **姓名**: [填写]
- **邮箱**: [填写]
- **电话**: [填写]
- **LinkedIn**: [填写]
- **GitHub**: github.com/brandonstack
- **所在地**: [填写]

---

## 📝 Summary

Software Engineer with 4 years at Microsoft, specializing in large-scale data pipeline systems and price accuracy for Bing Shopping (Ads). Experienced in designing multi-source data governance frameworks, real-time monitoring systems, and end-to-end feature delivery. Seeking to transition into AI/ML-related roles where data engineering expertise meets intelligent systems.

> 💡 星：根据目标岗位调整侧重点。投 AI 岗强调 data pipeline + ML 基础；投全栈强调端到端交付能力。

---

## 🎓 Education

- **[学位]** — [学校], [年份]
- [其他教育经历，如有]

> 💡 星：填上学校、专业、毕业年份。如果 GPA 亮眼可以写，不亮眼就省略。

---

## 💼 Professional Experience

### **Software Engineer II** — Microsoft, Bing Shopping (Ads)
*[起始年份] – Present*

负责 Bing Shopping Ads 平台的价格 (Price) 和库存状态 (Stock Status) 准确度，服务全球广告主。

**Price Drop Alert (核心项目)**
- Designed and implemented Price Drop Alert system enabling users to track product prices and receive email notifications when prices reach target thresholds
- [补充：规模数据，如 daily tracked items, notification volume 等]

**Multi-Source Price Pipeline & Data Governance**
- Built and maintained multi-source price ingestion pipeline handling data from Merchant feeds (Advertiser/Organic), Landing Page crawlers (SFS), CSS Selectors, and Keepa API
- Designed a multi-source governance framework including Waterfall Model for marginal contribution analysis, Shadow Mode for safe source onboarding, and composite scoring (Coverage Lift, Correction Rate, Pollution with α=1.5 penalty)
- [补充：pipeline 处理的数据量级，如 daily records, number of merchants]

**Accuracy Monitoring & Tolerance Framework**
- Proposed and implemented tolerance-based accuracy metrics (1% threshold: `max($0.10, Price × 1%)`), improving Amazon accuracy measurement from 78% to 88%
- Designed monitoring dashboards for real-time price accuracy tracking across multiple sources and markets
- [补充：监控覆盖多少 market, 多少 domain]

**Data Quality Improvement Initiatives**
- Identified and eliminated Organic price source (2-3 day delay) as the primary cause of severe pricing errors in the "Last Write Wins" architecture
- Investigated and resolved cross-source data pollution issues (CSS Selector Pollute > Correct finding)
- Led Keepa integration for third-party price validation, including currency handling and Buybox prediction
- [补充：具体改善了多少准确度百分点]

**其他贡献**
- Collaborated with cross-functional teams (PM, crawl team, Ads platform) to drive data quality initiatives
- Mentored team members on pipeline architecture and debugging methodology
- [补充：带人经历、cross-team 合作等]

> 💡 星：这是大头，每个 bullet point 尽量用数字量化。格式：Action → What → Impact/Scale

---

### **[之前的工作/实习]** — [公司]
*[时间]*

- [填写]

> 💡 星：微软之前有工作经历吗？实习也算。按时间倒序排列。

---

## 🔧 Technical Skills

- **Languages**: C#, .NET, Python, TypeScript/JavaScript, SQL
- **Data & Pipeline**: Large-scale data ingestion, ETL, real-time monitoring
- **Cloud**: Azure (补充具体服务: Cosmos DB? Azure Data Explorer? etc.)
- **Web**: React, Vite (from Inquiry V3 project)
- **Tools**: Git, ADO, [补充]
- **Other**: [补充：ML 相关的任何经验]

> 💡 星：把你实际用过的技术都列上，特别是 Azure 相关的服务名。

---

## 🚀 Personal Projects

### Inquiry V3 — Knowledge Management App
- Building a PKM application with concept network (X-Ray) driven knowledge graph
- Tech stack: React + Vite + PowerSync | .NET 9 + Semantic Kernel | Supabase
- Features: Capture → Inbox → Lab (reading/checking/crystallize) → Knowledge Base

> 💡 星：个人项目能展示你的 AI 兴趣和全栈能力，投 AI 岗时特别加分。

---

## 📋 填写清单

星需要补充的信息：
- [ ] 基本信息（姓名、联系方式、所在地）
- [ ] 教育背景（学校、专业、学位、年份）
- [ ] 微软之前的工作/实习经历
- [ ] 微软入职年份
- [ ] 各项目的量化数据（数据量、准确度提升、覆盖范围等）
- [ ] 完整技术栈（特别是 Azure 服务）
- [ ] 是否需要中文版（内部转组可能用中文）
