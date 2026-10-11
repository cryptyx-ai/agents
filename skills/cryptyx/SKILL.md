---
name: cryptyx
description: Route crypto questions to CRYPTYX market evidence. Use when the user names coins, mentions their holdings, watchlist or a DCA (recurring buy or sell), or asks whether coins are running hot, crowded or calm. Starts simple and goes deeper only when the user asks.
---

# CRYPTYX

CRYPTYX reads the crypto market every day across about 190 coins and returns deterministic numbers from a live database. This skill picks the right starting point for the user's question and keeps the first answer simple.

Remote MCP: `https://mcp.cryptyx.ai/api/mcp` (OAuth sign-in through the user's client). Free accounts can use the tools marked *free* below, with daily limits.

## Pick the starting point

| The user… | Start with | Skill |
| --- | --- | --- |
| Names one or a few coins ("is SOL overheated?", "compare ETH and AVAX") | `get_heat_check` *(free)* | [cryptyx-holdings](../cryptyx-holdings/SKILL.md) |
| Mentions their holdings or portfolio | Read holdings with their exchange tool, then `get_heat_check` | [cryptyx-exchange-bridge](../cryptyx-exchange-bridge/SKILL.md) |
| Mentions a DCA or recurring buys/sells | `check_dca` *(free)* | [cryptyx-holdings](../cryptyx-holdings/SKILL.md) |
| Asks why a coin reads the way it does, or wants to test an idea | Depends on the question | [cryptyx-investigate](../cryptyx-investigate/SKILL.md) |
| Asks what CRYPTYX can do | `get_cryptyx_overview` *(free)* | — |

If unsure whether a coin is covered, call `check_coverage` *(free)* first. `get_data_liveness` *(free)* says when the data last updated.

## Depth follows the user

1. **First answer: simple.** One or two numbers per coin in plain words, plus one offer to dig deeper. No signal names, metric codes or scores the user did not ask for.
2. **Second answer: why.** Only when the user asks why, or asks for more.
3. **Deeper: build and test.** Only when the user asks to test, backtest or monitor something.

## Ground rules

- Every number comes from a tool response in this session. Do not estimate or fill gaps.
- Report what the data shows and what happened historically. Do not tell the user to buy, sell, add or trim; they decide.
- Send coin symbols only. Never send balances, position sizes or account identifiers to CRYPTYX.
- Keep each tool's disclaimer when quoting its evidence.
- If a tool says a coin is not covered, say so plainly.
