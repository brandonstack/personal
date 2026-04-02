---
source: "Justineo"
url: "https://github.com/Justineo/working-with-ai/blob/main/journey/mcp-vs-cli.md"
date: "2026-03-29"
tags: [AI, MCP, CLI, agent, architecture]
---

# MCP vs CLI：面向 AI Agent 工具集成的深度研究

> 来源：Justineo/working-with-ai 项目 journey/ 目录，用 ChatGPT Deep Research 生成的调研报告。

---

## 核心结论

MCP 与 CLI 不是互斥替代关系，而是分别对应**「协议化互操作的能力层」**和**「人类与脚本友好的执行层」**。

- CLI 更贴近**开发内环**（inner loop）：速度、可控性、可复用的脚本化和管道组合
- MCP 更贴近**集成外环**（outer loop）：跨客户端互操作、工具发现、结构化输入输出、权限边界、企业治理

多数成熟团队最终走向**二者并存**：CLI 作为底层实现与专家入口，MCP 作为面向 Agent 的标准化接口层与分发机制。

---

## 术语澄清

- **MCP**：Anthropic 2024-11-25 发布的 Model Context Protocol，开放协议，JSON-RPC 2.0，Host-Client-Server 架构，暴露 Resources / Tools / Prompts
- **CLI**：命令行界面，通过 stdout/stderr/退出码实现可组合自动化
- 社区讨论中，「CLI」常指「给 Agent 一个受控 shell」的集成策略，「MCP」常指「为 Agent 提供大量可发现工具」的策略

---

## 属性对照

| 属性   | MCP                              | CLI                    |
| ---- | -------------------------------- | ---------------------- |
| 定位   | 标准化 LLM 应用连接外部系统                 | 文本命令交互 + 脚本化           |
| 第一用户 | AI 应用与 Agent                     | 人类开发者与自动化脚本            |
| 可发现性 | 内建 tools/list、schema 元数据         | 依赖 --help/man，无统一标准    |
| 输入输出 | schema 明确，错误协议化返回                | 字符串参数，文本输出需解析          |
| 传输   | stdio + Streamable HTTP          | 本地进程调用，可 SSH 扩展        |
| 安全授权 | Host 用户同意 + 可选 OAuth 2.1         | OS 权限决定边界，开放 shell 风险大 |
| 治理   | 规范迭代 + SEP 流程 + Linux Foundation | POSIX 约定，一致性取决于工具作者    |

---

## 各维度分析摘要

### 可发现性与边界
- MCP 把能力暴露为协议对象（Tools/Resources/Prompts），Host 负责权限与同意，接口层更清晰
- CLI 接口极简且普适，但在 Agent 场景下容易膨胀为「执行几乎任何命令」

### 性能与上下文成本
- MCP 的结构化 schema 有助于模型自我纠错，减少猜测回合数
- **上下文膨胀问题**：大量工具定义占用 context window，导致注意力稀释 → 需要渐进式披露、精简工具暴露
- CLI 运行时成本可预测（零协议开销），但文本输出歧义可能增加交互回合

### 安全性
- CLI 最大风险：**命令注入**，Agent 场景下放大为「对话触发的远程代码执行」
- OWASP 明确建议避免开放式 shell，应用细粒度工具替代
- MCP 协议层要求用户同意、数据隐私边界，HTTP 场景有标准化 OAuth 2.1
- MCP 新风险：**工具元数据攻击**（工具投毒、影子污染、rug pull）

### 可扩展性
- MCP：Streamable HTTP + 会话管理 + tasks 支持长时操作与延迟取结果
- CLI：部署简单，但远程多用户场景需要自建调度/隔离/权限层（本质上在 CLI 外再造服务面）

### 可维护性
- MCP：协议化能力发现 + 版本协商 + 向后兼容指导；风险是不同客户端特性支持不一致
- CLI：接口面小、失败模式清晰；但缺少机器可读 schema，输出格式变化会破坏自动化

---

## 场景决策矩阵

| 场景 | 推荐 | 说明 |
|------|------|------|
| 个人/小团队，本地开发为主 | **CLI 优先**，少量 MCP 补充 | CLI 适合内环；多 AI 客户端时用精简 MCP 桥接 |
| 中型团队，跨 IDE/AI 客户端复用 | **MCP 优先**，CLI 做专家入口 | MCP 标准化 tools/resources 复用；保留 CLI 供高级用户与 CI |
| 企业级系统接入，强合规审计 | **MCP + 治理** | OAuth/同意/审计 + 工具细粒度拆分；禁止开放式 shell |
| 高风险执行面（生产运维、涉密） | MCP 细粒度工具 或 CLI 强沙箱白名单 | OWASP 反对开放式 shell，应拆分为受限工具 |
| 长时任务（数据处理、批量操作） | **MCP（tasks）** | tasks 支持进度/取消/延迟取结果 |
| 工具数量爆炸，上下文敏感 | MCP + 工具路由/渐进加载 | 一次性加载大量 schema 会压上下文 |
| 遗留系统多、现有脚本资产重 | **先 CLI 稳定化**，再逐步包装 MCP | 先固化 CLI 契约（结构化输出/退出码/白名单），再作为 MCP tool 暴露 |

---

## MCP 演化时间线

- **2024-11-25**：Anthropic 正式发布并开源 MCP
- **2025-03-26**：引入 Streamable HTTP，逐步弃用旧 HTTP+SSE
- **2025-06-18**：授权与安全规范显著增强，SSE 明确弃用
- **2025-11-25**：最新稳定规范，加入 tasks、改进 OAuth 与治理流程
- **2025-12-09**：MCP 捐赠至 Linux Foundation 下 Agentic AI Foundation

---

## 落地建议

### 小团队/个人开发者
- 以 CLI 为主，优先做「机器友好化」：稳定退出码、stderr 仅诊断、必要时 JSON 输出
- 接入特定 AI 客户端时用少量 MCP server 桥接，严格限制工具数量避免上下文膨胀

### 中型组织
- 「双入口」策略：关键业务能力以 MCP 暴露，保留等价 CLI 供专家与 CI
- MCP 侧建立最小可行治理（工具注册、版本兼容、日志审计、回滚）
- 工具路由/渐进暴露作为默认实践

### 大型企业
- MCP 视为「受监管的集成平台」
- HTTP 场景标准化 OAuth 2.1 + 最小权限 + 令牌保护 + step-up 授权
- MCP server 准入与认证流程（参考 Microsoft 连接器认证）
- 工具元数据攻击防护（签名、语义审查、运行期策略引擎）
- **明确禁止向通用 Agent 直接开放无限制 shell**

### 按工作负载
- **开发调试类**（改代码、跑测试）→ CLI 主通道，最低摩擦内环效率
- **跨系统业务自动化** → MCP 为主，tasks/进度/取消支撑长时并发
- **工具数量多且上下文敏感** → 工具暴露策略（路由、渐进加载、精简 schema）与协议同等重要