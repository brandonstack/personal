# Agentic Coding 的风险与应对

Agent 编程不是银弹。多位实践者（Mario Zechner、Jeremy Howard、Justineo）从不同角度指出了 agentic coding 的系统性风险。

## 四大风险

### 1. 错误复合 + 零学习

Agent 和人都会犯错，关键区别：
- **人会学习**，Agent 不会——同样的错一遍遍犯
- **人是瓶颈**——一天写不了多少代码，错误复合速率低，痛感到阈值会主动修
- **Agent 军团没有瓶颈**——微小错误以不可持续的速率复合，脱离 loop 后感知不到

AGENTS.md / memory 系统只能覆盖你**观察到的**特定错误类别，无法泛化。

### 2. Agent 是复杂性贩子

Agent 的决策永远是局部的——看不到彼此的 run、看不到完整代码库、看不到之前的决策。结果：
- 大量代码重复
- 为抽象而抽象
- Cargo cult "最佳实践"堆砌

> 人类企业代码库花数年才烂到那个程度。Agent + 2 人团队，几周就能到达同等复杂度。

### 3. Agentic Search 召回率低

Agent 修复问题前需要找到所有相关代码——无论用 ripgrep、代码索引、LSP 还是向量数据库，代码库越大，recall 越低。低 recall 正是 Agent 产生重复和不一致的根源。

### 4. AI 创造力的边界

Jeremy Howard 与 Chris Lattner 的测试发现：Agent 写 C 编译器时直接复制了 LLVM 代码片段，包括设计错误。LLM 具备组合式创造力（重组训练数据），但**无法突破训练分布边界**。问题超出分布范围时，"模型突然从极聪明变得特别蠢"。

## 宏观后果

- AWS 疑似 AI 引发宕机，内部 90 天整改
- Microsoft 30% 代码 AI 编写，Windows 质量明显下降
- 越来越多团队"agentically coded themselves into a corner"
- **中间层开发者（2-20 年经验）最危险**——失去通过亲手写代码成长的机会
- 企业正在积累 AI 编程产生的技术债

## 应对策略

### 什么任务适合 Agent

- 可限定范围，不需理解完整系统
- 闭环可验证，Agent 能评估自己的输出
- 非关键路径（临时工具 / 内部软件）
- 或仅作为 rubber duck，用来碰撞想法

### 核心建议

> **Slow the fuck down.** 设定每天让 Agent 生成代码的上限，匹配你实际的 review 能力。

- **定义系统 gestalt 的部分（架构、API）手写**——亲自在代码里才能感受系统的"手感"
- **你理解代码库 → 弥补 agentic search 的低 recall → Agent 输出更好**
- 更少功能但更对的功能，可维护的系统

### 自动驾驶等级视角

| 等级 | 描述 | 信任模型 |
|------|------|----------|
| L0-L2 | 人控制，AI 辅助 | 低风险 |
| **L3** | Agent 执行，人 review | **瓶颈变成 code review** |
| L4-L5 | Agent + AI review | 信任还需慢慢建立 |

当前主流在 L3。从 L3 到 L4 的关键不是模型更强，而是**验证层（harness）更可靠**。

→ [../harness-engineering/harness-generations.md](../harness-engineering/harness-generations.md) — Harness 比模型更关键
→ [evaluation-systems.md](evaluation-systems.md) — 评测是验证 Agent 输出的基础设施
→ [../claude-code/verification-patterns.md](../claude-code/verification-patterns.md) — 对抗性验证设计

> 来源：resources/20260325-slow-down-agentic-coding.md
> 来源：resources/20260329-jeremy-howard-claude-code-wrong-direction.md
> 来源：resources/work-with-ai/20260329-working-with-ai-justineo.md
