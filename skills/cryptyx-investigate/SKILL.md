---
name: cryptyx-investigate
description: The Notable Read and depth on demand after a Pressure or Allocation Read - what stands out on each coin, setups firing or close to firing with their track record, how one reading has moved, and testing an idea with a backtest or custom trigger. Use when the user asks "why", "what else", or wants to test or monitor something.
---

# CRYPTYX: Notable Read and depth on demand

Follow the [CRYPTYX router](../cryptyx/SKILL.md). Use this skill only after the user asks for more than the first read in [cryptyx-holdings](../cryptyx-holdings/SKILL.md). Tools marked *Pro* return an upgrade message for free accounts. Relay that message plainly.

## Start with the Notable Read

Tool: `get_notable_read` with 1–10 symbols *(free, daily limit)*. Per coin, it returns:

- **pressure**: the Pressure Read result;
- **standout_readings**: the three readings furthest from the coin's own norm, each with a plain label, its z-score and where today sits in the coin's own history;
- **setups**: tracked setups firing or close to firing, with their evidence tier, number of past episodes, hit rate against the coin's base rate, and an `evidence_note`;
- **next_questions**: follow-ups that lead into the tools below.

How to present it:

- One short block per coin: what stands out, then any setups.
- For a setup, quote its hit rate against the base rate and the episode count, and pass on its `evidence_note` in plain words. A **pooled record** combines every past episode across the coins the setup applies to (for example BTC, ETH and SOL), each measured on its own history. That gives more episodes and a steadier read, but the record is not specific to the coin in question. Say so.
- Offer the coin's first `next_questions` item.
- What changed: each reading carries `then` (its tag `compared_with` days earlier). Setups carry `new_since`, and `no_longer_active` lists setups that have dropped off. Mention a reading only when its tag moved ("very high, normal a week ago"), and new or ended setups in one line each.

## Going further

| The user asks… | Tool | Notes |
| --- | --- | --- |
| How has one reading moved over time? | `analyze_metric` *(Pro)* | Pass the reading's `metric_id` from the Notable Read; speak in its plain label. |
| What goes into that setup? | `get_setup_details` *(Pro)* | Pass the setup's `setup_id`. Composition and history. |
| Did readings like this lead anywhere before? | `backtest_signal` or `evaluate_custom_trigger` *(Pro)* | Show sample size and the range of outcomes, not only the average. Flag small samples. |
| What's the market backdrop? | `get_regime_analysis` *(Pro)* | Present it as context, not as a call. |

## Register

- Answer the question asked, then offer one further step.
- Plain labels in prose. Metric and setup codes appear only if the user wants technical detail, in `code` formatting after the plain label.
- Label interpretation as interpretation. Historical results are history, not forecasts.
- "Positioning" means actual positioning only (funding, open interest, long/short). Do not use it for setups or for the Pressure Read as a whole.
