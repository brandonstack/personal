# 技术能力与成长

## 技术演进线

全栈开发 → 数据工程 → 数据治理 → 数据科学/度量

## 核心能力

- **工程**：Java/Python/C#, Azure 云基建, Spark/SCOPE 分布式计算, 服务端开发
- **数据**：ETL pipeline, 数据质量治理, 采样/Tolerance/Waterfall 治理体系
- **度量**：non-stationary distribution 上的度量设计, domain-specific treatment, 信号 vs 噪音

## 思考

从 builder 到 measurer 的转变——在 Bing Shopping 做 Price Accuracy 的经验本质上是度量工程：
- 在 non-stationary distribution 上做度量
- 需要 domain-specific treatment
- 区分信号和噪音

这套能力可以迁移到 Copilot Quality、推荐系统效果评估等场景。

### 2026-03-30: Claude Code 工具探索习惯

- [ ] 逐个探索 `/rewind`、`/loop`、`/branch`，每个命令做一次真实场景试用
- [ ] 用 `/loop` 跑起一个真正有用的自动化（URL list 批量抓取）
- [ ] 每月查看一次 Claude Code [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) 和社区推荐

反思：一直是"等文档型"用户，从未主动探索工具能力边界。工具层面的主动探索应该和代码/业务层面的探索一样成为习惯。

详细命令参考 → [wiki/claude-code/workflow-commands.md](../../wiki/claude-code/workflow-commands.md)
