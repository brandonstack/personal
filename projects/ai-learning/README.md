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

## 二、可展示的 harness 项目（5月启动）

用 Claude Agent SDK 构建 multi-agent 系统解决真实问题。

- [ ] 确定项目方向（如 code review harness：generator 写代码 + evaluator 用测试/lint 验证）
- [ ] 架构设计 & 实现
- [ ] 量化对比 solo agent vs harness 效果
- [ ] 整理成可讲述的 story（架构、evaluator 调优过程、量化数据）

## 三、内容输出（可选）

- [ ] "后端工程师视角的 Harness Engineering"
- [ ] "用 generator-evaluator 模式重构个人知识管理"

## 四、基础输入（30% 时间）

- [ ] Claude Agent SDK 文档通读 + 官方 examples 跑一遍
- [ ] Anthropic Building Effective Agents 指南精读
- [ ] 评估方法论：LMSYS Chatbot Arena、Anthropic eval 框架
- [ ] 每周 2-3 篇 AI 工程文章（inbox 习惯）
- [ ] Claude Code 工具探索：`/rewind`、`/loop`、`/branch` 实际试用

## 时间线

| 阶段 | 时间 | 重点 |
|------|------|------|
| 在职期 | 4-7月 | 70% 做项目 + 30% 基础，用微软福利（服务器/token） |
| 自驾期 | 7-8月 | 放松为主，碎片输入 |
| 求职期 | 9月起 | 集中求职，项目持续完善 |

详细 action plan 见 [areas/career/action-plan-apr-jul.md](../../areas/career/action-plan-apr-jul.md)

---

*Created: 2026-04-02*
