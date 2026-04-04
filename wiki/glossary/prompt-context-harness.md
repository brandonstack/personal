# Prompt → Context → Harness：三代范式演进

AI 开发方法论的三次范式转移，每一代解决的问题层次不同。

## 三代演进

### 1. Prompt Engineering（怎么说）
优化你给 LLM 的指令措辞。"请一步步思考"、"你是一个专家"这类技巧。有效但天花板低——模型能力提升后，措辞的差异越来越小。

### 2. Context Engineering（知道什么）
从优化"怎么说"到优化"知道什么"。不再只调措辞，而是精心准备 LLM 需要的参考资料：相关代码、历史记录、工具描述、项目文档。模型的推理质量取决于它看到了什么信息。

### 3. Harness Engineering（持续运行环境）
从优化"单次输入"到优化"持续运行环境"。Agent 不是单轮问答，是在一个环境中持续工作。Harness 关注的是：工具怎么注册、权限怎么管、记忆怎么存、质量怎么保。三大支柱：评估闭环、架构约束、记忆治理。

## 核心洞察

不是后一代替代前一代，而是层层叠加。好的 Harness 包含好的 Context 设计，好的 Context 包含好的 Prompt。

→ 深度阅读：[harness-generations](../harness-engineering/harness-generations.md)
