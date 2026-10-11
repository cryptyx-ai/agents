---
name: cryptyx-investigate
description: Go deeper on a coin with CRYPTYX after a simple read - what is driving its heat, which tracked setups are firing or close to firing, how one reading has moved over time, and testing an idea with a backtest or custom trigger. Use when the user asks "why", "show me more", or wants to test or monitor something.
---

# CRYPTYX investigate

Follow the [CRYPTYX router](../cryptyx/SKILL.md). Use this skill only after the user asks for more than the simple read in [cryptyx-holdings](../cryptyx-holdings/SKILL.md). Tools marked *Pro* return an upgrade message for free accounts. Relay that message plainly.

## Map the question to a tool

| The user asks… | Tool | Notes |
| --- | --- | --- |
| What's driving a coin's heat? | `get_heat_check` | Use the per-gauge `gauges` block: each gauge's label and how unusual it is for that coin. |
| What's firing or close to firing on this coin? | `get_harness_snapshot` with `scope: "asset:SOL"` *(Pro)* | Report each setup's plain name and its evidence tier. Only quote performance numbers the tool returns. |
| Tell me more about that setup | `get_setup_details` *(Pro)* | Composition and history for one setup. |
| How has one reading moved over time? | `analyze_metric` *(Pro)* | Use the readable name the tool returns, not the code. |
| Did this idea work before? | `backtest_signal` or `evaluate_custom_trigger` *(Pro)* | Show sample size and the range of outcomes, not only the average. Flag small samples. |
| What's the market backdrop? | `get_regime_analysis` *(Pro)* | Present it as context, not as a call. |

## How to answer

- Keep the user's thread. Answer the question they asked, then offer one further step.
- Use the readable names the tools return. Metric and signal codes go in `code` formatting after the readable name, only if the user wants technical detail.
- Separate what the data shows from your own interpretation, and label the interpretation.
- Historical results are history, not forecasts. Small samples and weak evidence tiers get a plain warning.
