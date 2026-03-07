# 项目经历展开 — Price / Price Drop Accuracy

> 面试时用，3-5 分钟讲完，面试官会追问细节

---

## Overview（1 分钟）— 讲故事线

> "I work on price accuracy for Microsoft Copilot's Product Tracking feature — Price Drop Alert. Users track products they want to buy, and when the price drops to their target, we send a notification.
>
> This means price accuracy is critical — not just 'is the price right', but 'is the price *change* right'. A false drop notification directly damages user trust.
>
> The core challenge is: we have multiple data sources — Merchant Feeds, our own crawlers, CSS Selectors running in user browsers, and third-party data like Keepa for Amazon. Each source has different coverage, latency, and reliability. And our ingestion system uses Last Write Wins — whoever writes last overwrites everything before it, regardless of quality.
>
> So the fundamental problem is: **limited crawl capacity vs. continuous price changes, combined with no intelligent conflict resolution**. My job was to build the measurement system to understand where we stand, diagnose why things go wrong, and drive improvements."

---

## Deep Dive 1: Multi-Source Governance Framework（主打 — 系统性思考）

### 怎么说

> "The first thing I realized was that we had **zero visibility** into which source was helping and which was hurting. We couldn't tell if a source was correcting bad prices or polluting good ones.
>
> So I designed a **Waterfall Model** — think of it as a layered attribution system. Each source is a layer: L0 is Merchant data, L1 is our crawler, L2 is CSS Selector, and so on. A source only gets credit for its *incremental* contribution on top of all previous layers.
>
> For each layer, I defined three metrics:
> - **Coverage Lift** — how many prices did this source fill that didn't exist before?
> - **Correction Rate** — how often did it fix a wrong price?
> - **Pollution Rate** — how often did it overwrite a correct price with a wrong one?
>
> And then a composite score: `Contribution = Corrections - α × Pollutions`, where α = 1.5 because pollution is worse than missing a correction.
>
> The key insight was the concept of **Destructive Win Rate** — measuring how often a source 'wins' the write competition (Last Write Wins) but the price it wrote is actually wrong, while the previous price was correct. This directly quantifies the cost of our architecture limitation.
>
> This framework immediately showed us that one source — Organic — had a very high pollution rate with 2-3 day latency. The data made it clear: we needed to cut it off."

### 面试官可能追问
- **Q: How did you validate this framework?**
  → "I used ground truth sampling — our daily accuracy measurement — as the baseline, then traced back each mismatch to identify which source last wrote the price. This gave us the per-source Correction and Pollution rates."
  
- **Q: How did you handle the fact that ground truth itself might be wrong?**
  → "Good question. Ground truth has its own issues — location differences, timing gaps, extraction errors. I addressed this by looking at the *distribution* of discrepancies rather than individual cases. Systematic patterns (like Organic always being 2-3 days stale) are reliable even if individual GT samples have noise."

- **Q: What was the impact?**
  → "It led to cutting off Organic source, which directly reduced pollution. It also established a **Shadow Mode protocol** — any new source must go through a validation phase where data is recorded but not written to production, and only promoted if Efficiency > 80% and Pollution < 10%."

---

## Deep Dive 2: 1% Tolerance Proposal（Metric Design + Experiment）

### 怎么说

> "Our accuracy metric used exact match — if the system price differed from ground truth by even one cent, it was counted as wrong. Our accuracy was around 78% for Amazon.
>
> But when I looked at the distribution of mismatches, I noticed a large cluster of tiny discrepancies — rounding differences, tax inclusion, minor shipping variations. These weren't real errors from a user perspective.
>
> So I proposed a tolerance-based metric: `max($0.10, Price × 1%)`. If the difference is within this threshold, it's considered a match.
>
> I tested this on Amazon data first. Accuracy went from 78% to 88%. That 10% gap represented noise, not signal — these were prices that looked 'wrong' to our metric but would never trigger a false Price Drop Alert.
>
> The key argument I made to PM was: **our metric should measure what matters to users, not what's mathematically exact**. A $0.03 difference on a $50 item is irrelevant for a price drop notification. This got approved and changed how we define success."

### 面试官可能追问
- **Q: How did you choose 1%? Why not 2% or 0.5%?**
  → "I analyzed the distribution of price deltas. There was a natural break point around 1% — below that, the mismatches were dominated by rounding/tax noise. Above that, they were genuine price errors from stale or wrong sources. The $0.10 floor handles low-price items where 1% would be too small."

- **Q: Isn't this just making your metric look better without actually improving anything?**
  → "Fair challenge. The key distinction is: tolerance doesn't hide real errors, it removes measurement noise. The remaining 12% mismatches on Amazon are *real* problems — stale Keepa data, buybox changes, etc. By cleaning up the metric, we can now focus engineering effort on actual issues instead of chasing noise."

---

## Deep Dive 3: Source 治理 — 断 Organic（Data-Driven Decision Making）

### 怎么说

> "Organic was one of our price sources — it ingested prices from Bing's organic index. The problem was a 2-3 day latency. In a world where prices change hourly, a source that's 2-3 days behind is actively harmful.
>
> Using the Waterfall Model, I quantified its Destructive Win Rate — how often Organic overwrote a correct, fresh price with a stale one. The number was significant.
>
> I wrote the code to cut off Organic ingestion, presented the data to the team and PM, and we executed the change. This was a 'subtraction' move — sometimes the best thing you can do for data quality is remove a bad input rather than add a new one."

### 面试官可能追问
- **Q: Was there any risk in cutting it off?**
  → "Organic did provide some coverage for tail domains where we had no other source. But the trade-off was clear: the pollution it caused on domains with multiple sources far outweighed its coverage lift on tail domains. We monitored for a week after cutting it to confirm no regression."

---

## 串联叙事（如果面试官问 "Walk me through your biggest project"）

> "Let me walk you through how I approached price accuracy for Product Tracking.
>
> **First, I built visibility.** We had multiple data sources but no way to know which was helping and which was hurting. I designed a layered attribution framework — the Waterfall Model — that quantifies each source's Coverage Lift, Correction Rate, and Pollution Rate. This gave us the first-ever source-level transparency.
>
> **Then, I fixed the measurement.** Our accuracy metric was too noisy — exact match was penalizing rounding differences. I proposed a 1% tolerance, validated it on Amazon (78% → 88%), and got it approved. Now our metric reflects what actually matters to users.
>
> **Then, I took action.** The framework showed Organic source was a net polluter. I led the effort to cut it off — writing the code, presenting the data, and monitoring the impact.
>
> **And throughout, I built the ongoing measurement infrastructure** — dynamic sampling algorithm, debug framework for Keepa, dashboards for continuous monitoring.
>
> The meta-lesson is: **you can't improve what you can't measure, and you can't measure well if your metric doesn't reflect reality.** I think this applies directly to Copilot quality — how do you define 'good'? How do you attribute quality to different components? How do you separate signal from noise in evaluation?"

---

## Copilot 类比（结尾加分）

| Price Accuracy | Copilot Quality |
|---------------|----------------|
| Waterfall Model（source 归因） | Model/component attribution |
| Correction vs Pollution | Helpful vs harmful responses |
| Destructive Win Rate | 好回答被坏回答覆盖的场景 |
| 1% Tolerance | Quality threshold 定义 |
| Shadow Mode | A/B test / canary deployment |
| 断 Organic | 下线表现差的 model/feature |

---

*Created: 2026-02-25*
