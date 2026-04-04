# 🧠 AI 学习 & 项目积累

> 启动日期: 2026-04-02
> 目标: 转型 AI Systems Engineer，通过项目积累可展示的作品，9 月起求职

## 定位

**AI Systems Engineer** — 设计让 agent 可靠工作的系统：评估体系、架构约束、知识结构、反馈循环。

详见 [areas/career/ai-engineer-roadmap.md](../../areas/career/ai-engineer-roadmap.md)

## 完成标准

- [ ] 至少 1 个可展示的 harness 项目（面试能讲 5 分钟）
- [ ] personal repo 本身打磨成 showcase（multi-agent ingest + evaluator）
- [ ] 1-2 篇内容输出（博客/推文）
- [ ] Claude Agent SDK + Anthropic eval 框架跑通

---

## 一、深化 personal repo harness（4月起，持续）

已有基础：CLAUDE.md + commands + memory + areas rules。

- [ ] `/ingest` 做成 multi-agent 版：一个 agent 抓取/压缩，一个 agent 评估质量和分类
- [ ] 加 evaluator 给 ingest 结果打分（信息密度、分类准确度），迭代调优评分标准
- [ ] 写一篇文章记录设计决策和 trade-off

## 二、可展示的 harness 项目（4月启动）

→ **独立项目**: [coding-agent-harness](../coding-agent-harness/) ([GitHub repo TBD](https://github.com/xingli/coding-agent-harness))

用 Claude Agent SDK 构建 multi-agent coding harness：generator 写代码 + evaluator 打分验证 + 反馈循环。

- [ ] Generator agent + Evaluator agent + 反馈循环
- [ ] 量化对比 solo agent vs harness 效果
- [ ] 整理成可讲述的 story（架构、evaluator 调优过程、量化数据）

## 三、内容输出（可选）

- [ ] "后端工程师视角的 Harness Engineering"
- [ ] "用 generator-evaluator 模式重构个人知识管理"

## 四、基础输入（30% 时间）

- [ ] Claude Agent SDK 文档通读 + 官方 examples 跑一遍
- [ ] Anthropic Building Effective Agents 指南精读
- [ ] 评估方法论：LMSYS Chatbot Arena、Anthropic eval 框架
- [ ] 每周 2-3 篇 AI 工程文章（resources/pending 阅读习惯）
- [ ] Claude Code 工具探索：`/rewind`、`/loop`、`/branch` 实际试用

## 五、Knowledge Sprint（大规模主题摄入）

按 topic 策划高质量资源列表 → 批量 fetch → compile → wiki。覆盖转型所需的基础知识 + 主线深化。

| Topic | 预算 | URLs | Status | 详情 |
|-------|------|------|--------|------|
| ML/DL Fundamentals | 25h | 14 | curating | [→](topics/ml-fundamentals.md) |
| RAG & Retrieval | 15h | 12 | curating | [→](topics/rag-retrieval.md) |
| AI Eval & Safety | 15h | 12 | curating | [→](topics/ai-eval-safety.md) |
| Agent SDK & Harness | 20h | 13 | curating | [→](topics/agent-harness.md) |
| AI Infra & Deployment | 15h | 12 | curating | [→](topics/ai-infra.md) |

Sprint 工作流和进度总览见 [topics/_index.md](topics/_index.md)

### 批量 fetch

```bash
# 单 topic Tier 1
python3 .ingest/batch-fetch.py projects/ai-learning/topics/ml-fundamentals.md --tier 1

# 单 topic 全部
python3 .ingest/batch-fetch.py projects/ai-learning/topics/ml-fundamentals.md

# 全部 topics Tier 1（dry run 预览）
python3 .ingest/batch-fetch.py projects/ai-learning/topics/*.md --tier 1 --dry-run
```

## 时间线

| 阶段 | 时间 | 重点 |
|------|------|------|
| 在职期 | 4-7月 | 70% 做项目 + 30% 基础，用微软福利（服务器/token） |
| 自驾期 | 7-8月 | 放松为主，碎片输入 |
| 求职期 | 9月起 | 集中求职，项目持续完善 |

### Sprint 推荐顺序（融入 30% 基础时间）

| Week | Topic | 说明 |
|------|-------|------|
| 1-2 | ML/DL Fundamentals | 先打地基 |
| 3-4 | RAG & Retrieval | 最可实操 |
| 5-6 | AI Eval & Safety | 核心定位 |
| 7-8 | Agent SDK & Harness | 有了新基础后再深化 |
| 9-10 | AI Infra & Deployment | 运维侧，最后补 |
| 11+ | 查漏补缺、二次 compile | |

详细 action plan 见 [areas/career/action-plan-apr-jul.md](../../areas/career/action-plan-apr-jul.md)

---

*Created: 2026-04-02*
*Updated: 2026-04-04 — 新增 Knowledge Sprint*
