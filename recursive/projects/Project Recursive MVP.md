## Deliverable

- 一个可用的 Q-E-T-D demo 原型

## Questions

- Q: Recursive MVP？
	- Delivery?
		- Q: **Delivery** 是一个Demo App还是一个Obsidian的验证过的demo? (their could be a decision matrics)
			- E: Decision Matrics: TBD
				- E: Obsidian无法native和AI进行integration。我们需要一些inline的edit和补全功能
				- E: Obsidian是纯文本，可以跟Claude Code, Codex等等写作。
				- E: 我们可以创建一些claude code skills来暂时与AI集成，并且可以复用。
					- Q: 我们可以在obisidian里面调用claude code吗？可以内置terminal吗？或者我们可以不打开第二个软件就写作吗？one click to skills? 需要什么呢？
						- E: 应该可以的。TBD.
				- E：Obsidian有现成的编辑器等等内容，我们只需要专注于核心的用户故事和交互即可，等验证完成之后，可以在继续往后走。effort是最少的。
					- E: 重建一个应用可能会分散现在的注意力
				- E: obsidian需要我们自己去创建bullet points, 创建Q, E, T，无法自动更新gaps和更新状态，还有就是无法做一些customize。
	- Initiative?
		- Q: 这个项目的出发点是？
			- E: 这个项目是为了把面向知识库的软件，改成项目优先，以练促学。同时鼓励思考，鼓励问问题，而不是被信息淹没。
		- Q: 为什么一定要做这个项目？
			- E: 是自己的兴趣所在。问题，思考等等一直是我的课题。
		- Q: 有什么特异点吗？
			- E: 项目优先，问题有限。
	- Q: 功能设计？
		- Q: Projects 视角？
			- Q: 创建项目？
				- E: 创建项目阶段需要确认项目的
					- Scope: 需要明确和澄清
					- Delivery: 需要明确Delivery
					- Dependency: 有没有一个强依赖需要提前解决，比如比较大块的前置知识?
						- Q：如何判断是dependency还是gaps?
		- Q: 知识视角？
			- Q: 复杂知识应该如何处理？
		- Q: AI功能？
			- E: 自动提问应该有意思
			- E: 自动更新状态
			- E: 自动对于内容进行结构化重构。
			- E: 自动建议
			- E: 自动ondemand, search, fetch信息，并且用于项目中。
			- Q: 这里的AI功能似乎可以做一些类似于代码编辑器的交互，比直接chat的效率更高一些呢?
	- Q: 遇到的问题?
		- Q: Tree goes too big, 不能focus在具体的内容中。
		- Q: 当前的必须是QET格式，是不是有些死板，是不是有一些Info节点？
			- E: 我们需要一些节点用于分类和拆分。现在的问题可能并不能算作一个问题。或者说问题除了问题，这个框架之外是不是还有别的内容呢？
			- E: 我们现在可能无法严格区分三种内容，或者说不是完全按照QETD的结构的。
