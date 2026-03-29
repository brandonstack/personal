# 4-7 月 Action Plan（在职期）

约 300 小时可用（工作日晚 1-2h + 周末半天），按 70/30 分。

## 70% 做项目（~210h）

### 项目 1：深化 personal repo harness（4月起，持续）

已有基础：CLAUDE.md + commands + memory + areas rules。

- 把 `/ingest` 做成 multi-agent 版：一个 agent 抓取/压缩，一个 agent 评估质量和分类（generator-evaluator 最小实践）
- 加 evaluator 给 ingest 结果打分（信息密度、分类准确度），迭代调优评分标准
- 写一篇文章记录设计决策和 trade-off

### 项目 2：可展示的 harness 项目（5月启动）

用 Claude Agent SDK 构建 multi-agent 系统解决一个真实问题。

建议方向：code review harness（generator 写代码 + evaluator 用测试/lint 验证）+ 量化对比 solo vs harness 效果。

面试可讲 5 分钟：架构设计、evaluator 调优过程、量化数据。

### 项目 3（可选）：内容输出

把 inbox 阅读 + 实践心得写成博客/推文：
- "后端工程师视角的 Harness Engineering"
- "用 generator-evaluator 模式重构个人知识管理"

内容输出 = 作品集 + 被发现的渠道。

## 30% 基础输入（~90h）

### 每周固定

- 2-3 篇 AI 工程文章（inbox 习惯保持）
- 读完问自己：这改变我的分配吗？

### 系统性补课（选 1-2 个）

- Claude Agent SDK 文档通读 + 官方 examples 跑一遍
- Anthropic Building Effective Agents 指南精读
- 评估方法论：LMSYS Chatbot Arena 评估体系、Anthropic eval 框架

不需要上课/刷题——在项目中边做边学。

## 节奏

| 时间 | 内容 |
|------|------|
| 工作日晚 1-2h | 项目 coding / inbox 阅读 |
| 周末半天 4-5h | 项目集中推进 / 写文章 |
| 每周日晚 30min | 回顾本周进展，调整下周重点 |
