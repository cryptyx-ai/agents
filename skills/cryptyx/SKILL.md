---
name: cryptyx
description: Ground crypto decisions in CRYPTYX intelligence. Use when the user names coins, mentions their book, watchlist or a recurring buy or sell, or asks whether to add, trim or hold. Routes to the Pressure Read, the Allocation Read, the Notable Read or deeper engine reads, and keeps the first answer sharp.
---

# CRYPTYX

CRYPTYX is the intelligence layer for digital assets: 670+ metrics across about 190 coins, scored daily against each coin's own history, with rules pre-registered and backtested out of sample. It returns deterministic numbers from a live database. This skill routes each question to the right read and keeps the first answer sharp.

Remote MCP: `https://mcp.cryptyx.ai/api/mcp` (OAuth sign-in through the user's client). Tools marked *free* work on free accounts, with daily limits.

## Route the question

| The user… | Read | Tool | Skill |
| --- | --- | --- | --- |
| Names coins: "where is pressure building?", "compare ETH and AVAX" | Pressure Read | `get_heat_check` *(free)* | [cryptyx-holdings](../cryptyx-holdings/SKILL.md) |
| Refers to their book or holdings | Pressure Read on the book | Exchange read, then `get_heat_check` | [cryptyx-exchange-bridge](../cryptyx-exchange-bridge/SKILL.md) |
| Runs a recurring buy or sell (DCA, treasury distribution) | Allocation Read | `check_dca` *(free)* | [cryptyx-holdings](../cryptyx-holdings/SKILL.md) |
| Asks why, or what else stands out | Notable Read | `get_notable_read` *(free)* | [cryptyx-investigate](../cryptyx-investigate/SKILL.md) |
| Wants to test an idea or go further | Depth on demand | Depends on the question | [cryptyx-investigate](../cryptyx-investigate/SKILL.md) |
| Asks what CRYPTYX can do | Overview | `get_cryptyx_overview` *(free)* | — |

Unsure whether a coin is covered? Call `check_coverage` *(free)*. `get_data_liveness` *(free)* reports when each data source last updated.

## Depth follows the user

1. **First answer: sharp.** The read, one or two numbers per coin, one evidence line, one offer to go deeper.
2. **Second answer: the drivers.** Only when the user asks why.
3. **Further: build and test.** Only when the user asks to test, backtest or monitor.

## Ground rules

- Every number comes from a tool response in this session. Never estimate or fill gaps.
- Present the evidence and its record. The user makes the call to add, trim or hold.
- Send coin symbols only. Never send balances, position sizes or account identifiers to CRYPTYX.
- Keep each tool's disclaimer when quoting its evidence.
- If a coin is not covered, say so plainly.
