# Skills 设计指南

Skills 是 Claude Code 的控制层核心——`.claude/commands/` 下的 markdown 文件，定义了可复用的工作流。Anthropic 内部经验总结了 9 大类别和关键写作原则。

## 9 大 Skill 类别

| 类别 | 说明 | 典型例子 |
|------|------|----------|
| Library/API Reference | 工具和框架用法 | "使用 X 库做 Y" |
| Product Verification | 产品质量检查 | 截图对比、功能验证 |
| Data Fetching | 数据获取和处理 | API 调用、数据转换 |
| Business Process | 业务流程自动化 | 发布流程、审批 |
| Code Scaffolding | 代码生成脚手架 | 新组件模板、项目初始化 |
| Code Quality | 代码质量保障 | lint 规则、review checklist |
| CI/CD | 持续集成/部署 | 构建、测试、发布 |
| Runbooks | 运维手册 | 故障排查、回滚步骤 |
| Infrastructure | 基础设施管理 | 环境配置、资源管理 |

## 写作最佳实践

### Description 是触发条件

`description` 字段不只是说明文字——它是模型判断"什么时候该用这个 skill"的触发条件。写法应该是条件式的：

```yaml
---
description: 当需要批量处理 inbox 文件并更新 wiki 时使用
---
```

而不是：
```yaml
---
description: 一个用来消化 inbox 文件的工具
---
```

### Gotchas 区块

在 skill 中加一个 "已知陷阱" 区块，列出常见错误和边界情况。这比正面指令更有效——模型对"不要做 X"的遵从度高于隐含在长指令中的约束。

### 文件系统渐进式披露

不要在 skill 中堆一整个文件结构说明。而是：
1. 给一个入口点（"先读 _index.md"）
2. 教模型下一步去哪找（"然后根据主题读相关目录的 _index.md"）
3. 让模型按需探索

这与 OpenAI 的 "地图而非手册" 原则一致。

### 避免过度约束

过于详细的步骤反而降低质量——模型会机械执行而不思考。关键是定义"what"和"why"，让模型自己决定"how"。

例外：涉及安全、数据完整性的操作必须精确约束。

## Skill 组合

Skills 可以互相调用，形成工作流链：

```
/ce:plan → /ce:work → /ce:review → /ce:compound
```

每个 skill 输出是下一个的输入。设计时考虑可组合性——单个 skill 做好一件事，复杂流程通过组合实现。

## 分发策略

- **个人 skills**：`.claude/commands/`（项目级）
- **团队共享**：通过 git 仓库分发
- **社区插件**：npm 包 → `settings.json` 中注册

Skill 本质是可分发的 prompt 工程——写好一次，团队/社区复用。

## 测量与迭代

通过 Hooks 收集 skill 使用数据：
- 调用频率
- 成功/失败率
- 执行时间
- Token 消耗

基于数据迭代 skill prompt，与 evaluator-generator 的评分标准调优逻辑一致。

→ [tool-governance.md](tool-governance.md) — Skills 在工具治理中的位置
→ [architecture-overview.md](architecture-overview.md) — Skills 是控制层的核心
→ [../harness-engineering/evaluator-generator.md](../harness-engineering/evaluator-generator.md) — Skill 质量测量与评估闭环

> 来源：resources/20260318-claude-code-skills-lessons.md, resources/20260312-claude-code-architecture-governance.md
