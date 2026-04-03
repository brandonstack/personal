# Evaluator-Generator 模式

将"做工作的 Agent"和"评判工作的 Agent"分离，是解决 Agent 自我评估不可靠问题的核心设计模式。

## 为什么需要分离

Agent 自评天然不可靠——不管输出质量高低，自评永远偏正面。这类似人类的 confirmation bias。让一个 LLM 对自己的产出持批判态度，比调优一个独立的 evaluator 要困难得多。

分离后 evaluator 仍然是 LLM，仍有宽松倾向。但独立 evaluator 可以被单独调优为持怀疑态度，而且一旦有了外部反馈，generator 就有具体内容可以针对性迭代。

## 架构演进

### V1: Planner-Generator-Evaluator 三 agent

Anthropic 在 Opus 4.5 时代的完整架构：

- **Planner**：接收简短 prompt，扩展为完整产品规格。强调产品上下文和高层技术设计，不做细粒度技术指定（避免错误级联）
- **Generator**：按 sprint 逐功能实现。每个 sprint 前与 evaluator 协商"sprint 合约"——先定义"完成"的标准再写代码
- **Evaluator**：用 Playwright 实际操作运行中的应用（点击、填表单、导航），按标准逐条验证。不是看代码打分，是像用户一样测试

关键数据对比（同一 prompt "创建 2D 复古游戏制作器"）：
- 单 Agent：20 min / $9 → 核心功能不可用
- 完整 Harness：6h / $200 → 功能完整的全栈应用

### V2: 移除 Sprint，保留评估

Opus 4.6 能力提升后，sprint 分解和 context reset 都可以移除。但 evaluator 不能移除。

简化后：Planner → Generator（连续运行 2+ 小时）→ Evaluator（运行结束时单次评审）→ 循环修复。

DAW 生成案例：4h / $124，Generator 连续运行超过 2 小时无 sprint 分解。

### 何时需要 Evaluator

Evaluator 的价值取决于任务相对于模型能力的位置：
- 任务在 Generator 能力边界内 → Evaluator 是不必要开销
- 任务在 Generator 能力边缘 → Evaluator 提供真实提升

模型越强，边界越外移，但边界永远存在。

## 评分标准设计

评分标准不仅是衡量工具，更是引导工具（steering mechanism）。标准的措辞直接影响产出方向。

Anthropic 前端设计实验中的四维度：
1. **设计质量**（高权重）：整体连贯性、独特氛围
2. **原创性**（高权重）：是否有自定义创意选择，惩罚 AI slop 模式
3. **工艺**：技术执行——排版、间距、色彩
4. **功能性**：可用性

刻意加重设计和原创性的权重，因为 Claude 在工艺和功能性上默认表现不错，但审美上倾向安全和可预测。

## Sprint 合约模式

每个 sprint 开始前，Generator 和 Evaluator 协商合约：
- Generator 提出将构建什么 + 如何验证成功
- Evaluator 审查提案确保方向正确
- 迭代直至达成一致
- Evaluator 后续按合约逐条验证

合约粒度很细——Sprint 3 有 27 个验证标准。Evaluator 的发现足够具体，可直接采取行动。

## 调优 Evaluator 的实践

开箱即用的 Claude 是糟糕的 QA agent：
- 识别问题后说服自己不严重，批准工作
- 倾向浅层测试，不探测边界情况

调优循环：阅读 evaluator 日志 → 找到与人类判断不一致的例子 → 更新 prompt → 重复。经过多轮后才能达到合理水平。

## 关键洞察

- **Harness 的每个组件都编码了对模型局限性的假设**——模型变强后需要重新评估哪些该留哪些该删
- **识别 load-bearing 组件的方法**：系统地每次移除一个组件，审查对结果的影响（而非一次性大幅削减）
- **评估器也需要被评估**：Opus 4.5 找到了比标准答案更好的解法却被判失败 → 评估闭环不只检查 Agent，也检查评估本身

→ [harness-generations.md](harness-generations.md) — Harness 三代演进的大图景
→ [agent-environment-design.md](agent-environment-design.md) — OpenAI 的架构约束方法
→ [../ai-engineering/positioning-framework.md](../ai-engineering/positioning-framework.md) — 评估能力是 AI Systems Engineer 的核心迁移能力

> 来源：resources/anthropic/20260328-harness-design-long-running-apps-zh.md, resources/20260328-prompt-context-harness-paradigm-shift.md
