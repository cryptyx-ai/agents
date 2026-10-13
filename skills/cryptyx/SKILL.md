---
name: cryptyx
description: Ground crypto decisions in CRYPTYX intelligence. Use when the user names a coin, mentions their holdings or watchlist, or asks whether to add, trim or hold. Leads with THE STUDY for each coin - tactical and structural reads, what followed similar readings in the coin's history, and setups firing or close to firing.
---

# CRYPTYX

CRYPTYX is the intelligence layer for digital assets: 669 metrics across about 190 coins, each scored daily against the coin's own history and the market, plus a catalogue of setups whose records are tested before they are shown. Every number comes from a live database. This skill routes each question to the right part of the engine.

Remote MCP: `https://mcp.cryptyx.ai/api/mcp` (OAuth sign-in through the user's client). Tools marked *free* work on free accounts, with daily limits.

## Route the question

| The user… | Start with | Skill |
| --- | --- | --- |
| Names a coin ("how does SOL look?", "is ETH stretched?", "what happened last time?") | `get_coin_study` *(free)*, one call per coin | [cryptyx-holdings](../cryptyx-holdings/SKILL.md) |
| Refers to their holdings or watchlist | Exchange read, then `get_heat_check` *(free)* across the coins and `get_coin_study` for the ones that stand out | [cryptyx-exchange-bridge](../cryptyx-exchange-bridge/SKILL.md) |
| Asks what else stands out, or why | `get_notable_read` *(free)* or the deeper tools | [cryptyx-investigate](../cryptyx-investigate/SKILL.md) |
| Wants to test or build their own idea: a reading, a combination of factors, a signal | `analyze_metric`, `analyze_metrics_composite` *(Pro)* and the signal tools | [cryptyx-build-setup](../cryptyx-build-setup/SKILL.md) |
| Asks what CRYPTYX can do | `get_cryptyx_overview` *(free)* | — |

Unsure whether a coin is covered? Call `check_coverage` *(free)*. `get_data_liveness` *(free)* reports when each data source last updated.

## Depth follows the user

1. **First answer: the read.** For each coin, where it stands on the two horizons, the readings that stand out, and any setup firing or close to firing.
2. **Second answer: history.** What followed this coin's past readings like today's, with sample size and base rate. Only when the user asks, or when one reading clearly dominates.
3. **Further: test and build.** From one reading to a multi-factor, multi-horizon setup or signal of their own, with the full analytics, only on request.

## Ground rules

- Every number comes from a tool response in this session. Never estimate or fill gaps.
- Describe what the engine shows. Do not tell the user to buy, sell, add or trim; they decide.
- History is history: quote the number of past episodes and the base rate, and never present it as a forecast.
- Send coin symbols only. Never send balances, position sizes or account identifiers to CRYPTYX.
- "Positioning" means actual positioning (funding, open interest). Do not use it for other readings or for setups.
- If a coin is not covered, say so plainly.
