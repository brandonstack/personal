---
source: "Braintrust"
url: "https://www.braintrust.dev/docs/guides/evals"
date: "2026-04-04"
tags: ["AI", "Evaluation", "Safety"]
status: "compiled"
---
# Evaluate systematically - Braintrust

[Skip to main content](https://www.braintrust.dev/docs/guides/evals#content-area)

[Braintrust home page![Image 1: light logo](https://mintcdn.com/braintrust/u7i5gTV-ad3TRDYt/logo/logo-light.svg?fit=max&auto=format&n=u7i5gTV-ad3TRDYt&q=85&s=23878ca308aee393dcc8c89ed8705189)![Image 2: dark logo](https://mintcdn.com/braintrust/u7i5gTV-ad3TRDYt/logo/logo-dark.svg?fit=max&auto=format&n=u7i5gTV-ad3TRDYt&q=85&s=affa9d0eafd44b6cd7fb22c80afee713)](https://www.braintrust.dev/docs)

Search...

⌘K Ask AI

*   [Request demo](https://braintrust.dev/contact)
*   [Start building](https://braintrust.dev/app)
*   [Start building](https://braintrust.dev/app)

Search...

Navigation

Evaluate

Evaluate systematically

[Docs](https://www.braintrust.dev/docs)[Integrations](https://www.braintrust.dev/docs/integrations)[Reference](https://www.braintrust.dev/docs/reference)[Cookbook](https://www.braintrust.dev/docs/cookbook)[Troubleshooting](https://www.braintrust.dev/docs/kb)[Changelog](https://www.braintrust.dev/docs/changelog)

##### Start

*   [Introduction](https://www.braintrust.dev/docs)
*   [Braintrust workflow](https://www.braintrust.dev/docs/workflow)
*   [Log your first trace](https://www.braintrust.dev/docs/observability)
*   [Run your first eval](https://www.braintrust.dev/docs/evaluation)
*   [Plans and limits](https://www.braintrust.dev/docs/plans-and-limits)

##### Instrument

*   [Overview](https://www.braintrust.dev/docs/instrument)
*   [Trace LLM calls](https://www.braintrust.dev/docs/instrument/trace-llm-calls)
*   [Trace application logic](https://www.braintrust.dev/docs/instrument/trace-application-logic)
*   [Advanced tracing patterns](https://www.braintrust.dev/docs/instrument/advanced-tracing)
*   [Capture user feedback](https://www.braintrust.dev/docs/instrument/user-feedback)
*   [Log attachments](https://www.braintrust.dev/docs/instrument/attachments)

##### Observe

*   [Overview](https://www.braintrust.dev/docs/observe)
*   [View your logs](https://www.braintrust.dev/docs/observe/view-logs)
*   [Filter and search logs](https://www.braintrust.dev/docs/observe/filter)
*   [Discover insights with Topics](https://www.braintrust.dev/docs/observe/topics)
*   [Monitor with dashboards](https://www.braintrust.dev/docs/observe/dashboards)
*   [Use Loop](https://www.braintrust.dev/docs/observe/loop)
*   [Use deep search](https://www.braintrust.dev/docs/observe/deep-search)

##### Annotate

*   [Overview](https://www.braintrust.dev/docs/annotate)
*   [Add human feedback](https://www.braintrust.dev/docs/annotate/human-review)
*   [Create custom trace views](https://www.braintrust.dev/docs/annotate/custom-views)
*   [Add labels and corrections](https://www.braintrust.dev/docs/annotate/labels)
*   [Build datasets](https://www.braintrust.dev/docs/annotate/datasets)
*   [Export annotated data](https://www.braintrust.dev/docs/annotate/export)

##### Evaluate

*   [Overview](https://www.braintrust.dev/docs/evaluate)
*   Define components 
*   Iterate in playgrounds 
*   Run experiments 
*   [Score production traces](https://www.braintrust.dev/docs/evaluate/score-online)
*   [Best practices](https://www.braintrust.dev/docs/evaluate/best-practices)

##### Deploy

*   [Overview](https://www.braintrust.dev/docs/deploy)
*   [Deploy prompts](https://www.braintrust.dev/docs/deploy/prompts)
*   [Deploy functions](https://www.braintrust.dev/docs/deploy/functions)
*   Braintrust gateway 
*   [Manage environments](https://www.braintrust.dev/docs/deploy/environments)
*   [Monitor deployments](https://www.braintrust.dev/docs/deploy/monitor)
*   [Stream responses](https://www.braintrust.dev/docs/deploy/streaming)
*   [Use the proxy (deprecated)](https://www.braintrust.dev/docs/deploy/ai-proxy)

##### Admin

*   [Overview](https://www.braintrust.dev/docs/admin)
*   [Manage organizations](https://www.braintrust.dev/docs/admin/organizations)
*   [Manage projects](https://www.braintrust.dev/docs/admin/projects)
*   [Access control](https://www.braintrust.dev/docs/admin/access-control)
*   Billing 
*   Automations 
*   Self-hosting 
*   [Authentication](https://www.braintrust.dev/docs/admin/authentication)
*   [Personal settings](https://www.braintrust.dev/docs/admin/personal-settings)
*   [Architecture](https://www.braintrust.dev/docs/admin/architecture)
*   [Service health](https://www.braintrust.dev/docs/admin/service-health)

##### Best practices

*   [Evaluating agents](https://www.braintrust.dev/docs/best-practices/agents)
*   [Writing scorers](https://www.braintrust.dev/docs/best-practices/scorers)
*   [PM workflows](https://www.braintrust.dev/docs/best-practices/pm-workflows)

*   [Security](https://www.braintrust.dev/docs/security)

On this page

*   [Offline evaluation](https://www.braintrust.dev/docs/guides/evals#offline-evaluation)
*   [Iterate in playgrounds](https://www.braintrust.dev/docs/guides/evals#iterate-in-playgrounds)
*   [Run experiments](https://www.braintrust.dev/docs/guides/evals#run-experiments)
*   [Online evaluation](https://www.braintrust.dev/docs/guides/evals#online-evaluation)
*   [Anatomy of an evaluation](https://www.braintrust.dev/docs/guides/evals#anatomy-of-an-evaluation)
*   [Next steps](https://www.braintrust.dev/docs/guides/evals#next-steps)

Evaluate

# Evaluate systematically

Copy page

Test and monitor AI application quality at every stage of development

Copy page

AI systems behave differently from traditional software: the same input can produce different outputs, there’s rarely a single correct answer, and a change that improves one metric can silently degrade another. Systematic evaluation is how you measure quality, detect regressions before they reach users, and build confidence that your system is actually improving over time.Braintrust supports evaluation at every stage of AI development — from rapid iteration in the browser to systematic experiments to continuous production monitoring. The full evaluation cycle:
1.   **Iterate in playgrounds** — Prototype prompts, models, scorers, or custom agent code
2.   **Promote to an experiment** — Lock in an immutable snapshot when you find a good configuration
3.   **Automate in CI/CD** — Run evals on every pull request to catch regressions
4.   **Score in production** — Monitor live traffic continuously with online scoring rules
5.   **Feed back** — Pull interesting production traces into datasets to improve offline test coverage

## [​](https://www.braintrust.dev/docs/guides/evals#offline-evaluation)

Offline evaluation

Offline evaluation runs against known datasets before deployment. Because you control the inputs and can define expected outputs, you can use code-based scorers or LLM-as-a-judge — and results are reproducible and comparable over time.
### [​](https://www.braintrust.dev/docs/guides/evals#iterate-in-playgrounds)

Iterate in playgrounds

[Playgrounds](https://www.braintrust.dev/docs/evaluate/playgrounds) are a browser-based environment for rapid iteration. Run evaluations in real time, compare configurations side by side, and share results with teammates via URL. Results are mutable — re-running a playground overwrites previous generations, which is ideal for fast iteration.When your task can’t be expressed as a prompt, connect custom agent code to the playground via [remote evals or sandboxes](https://www.braintrust.dev/docs/evaluate/remote-evals). The iteration workflow stays the same.When you’ve found a good configuration, promote it to an experiment to capture an immutable snapshot.
### [​](https://www.braintrust.dev/docs/guides/evals#run-experiments)

Run experiments

Experiments are the immutable, comparable record of your eval runs. [Run them](https://www.braintrust.dev/docs/evaluate/run-evaluations) from code or in the UI, track progress over time, and integrate into CI/CD to catch regressions before they reach production.
## [​](https://www.braintrust.dev/docs/guides/evals#online-evaluation)

Online evaluation

[Online scoring](https://www.braintrust.dev/docs/evaluate/score-online) evaluates production traces automatically as they’re logged, running asynchronously with no impact on latency. Because there’s no ground truth for live requests, it relies on LLM-as-a-judge scorers to assess quality. Use it to monitor for regressions, catch edge cases you haven’t seen before, and surface real user interactions that become new test cases.
## [​](https://www.braintrust.dev/docs/guides/evals#anatomy-of-an-evaluation)

Anatomy of an evaluation

Every evaluation has three parts:**Data** — a dataset of test cases with inputs, optional expected outputs, and metadata. Build [datasets](https://www.braintrust.dev/docs/annotate/datasets) from production logs, user feedback, or manual curation.**Task** — the function being evaluated. Typically an LLM call, but can be any logic: a multi-step agent, a retrieval pipeline, or a custom workflow.**Scores** — functions that measure quality by comparing inputs, outputs, and expected values. Use built-in autoevals, [LLM-as-a-judge scorers](https://www.braintrust.dev/docs/evaluate/write-scorers), or custom code.
## [​](https://www.braintrust.dev/docs/guides/evals#next-steps)

Next steps

*   [Test prompts and models](https://www.braintrust.dev/docs/evaluate/playgrounds) in the playground
*   [Test complex agents](https://www.braintrust.dev/docs/evaluate/remote-evals) in the playground via remote evals or sandboxes
*   [Run experiments](https://www.braintrust.dev/docs/evaluate/run-evaluations) with the SDK or in the UI
*   [Run in CI/CD](https://www.braintrust.dev/docs/evaluate/run-evaluations#run-in-cicd) to catch regressions automatically
*   [Score production traces](https://www.braintrust.dev/docs/evaluate/score-online) with online scoring rules
*   [Best practices](https://www.braintrust.dev/docs/evaluate/best-practices) for reliable evaluations

Was this page helpful?

Yes No

[Export annotated data Previous](https://www.braintrust.dev/docs/annotate/export)[Create prompts Next](https://www.braintrust.dev/docs/evaluate/write-prompts)

⌘I

[Braintrust home page![Image 3: light logo](https://mintcdn.com/braintrust/u7i5gTV-ad3TRDYt/logo/logo-light.svg?fit=max&auto=format&n=u7i5gTV-ad3TRDYt&q=85&s=23878ca308aee393dcc8c89ed8705189)![Image 4: dark logo](https://mintcdn.com/braintrust/u7i5gTV-ad3TRDYt/logo/logo-dark.svg?fit=max&auto=format&n=u7i5gTV-ad3TRDYt&q=85&s=affa9d0eafd44b6cd7fb22c80afee713)](https://www.braintrust.dev/docs)

[github](https://github.com/braintrustdata)[x](https://x.com/braintrust)[discord](https://discord.gg/6G8s47F44X)[youtube](https://www.youtube.com/@BraintrustData)

[Pricing](https://www.braintrust.dev/pricing)[Blog](https://www.braintrust.dev/blog)[Careers](https://www.braintrust.dev/careers)[Status](https://status.braintrust.dev/)

[github](https://github.com/braintrustdata)[x](https://x.com/braintrust)[discord](https://discord.gg/6G8s47F44X)[youtube](https://www.youtube.com/@BraintrustData)

[Powered by This documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/?utm_campaign=poweredBy&utm_medium=referral&utm_source=braintrust)

Assistant

Responses are generated using AI and may contain mistakes.

[Contact support](mailto:support@braintrust.dev)
