---
name: cryptyx-holdings
description: Pressure Read and Allocation Read across a set of coins (a book, a watchlist, or the coins in a recurring buy or sell). Use for "where is pressure building", "what does the evidence say about this week's allocation", "should I add or trim" style questions. Quantitative, backtested, concise.
---

# CRYPTYX: Pressure Read and Allocation Read

Follow the [CRYPTYX router](../cryptyx/SKILL.md). If the coins come from an exchange account, read them first with the [exchange bridge](../cryptyx-exchange-bridge/SKILL.md).

## Pressure Read (any set of coins)

Tool: `get_heat_check` with 1–25 symbols. Present the result as the **Pressure Read**. Each coin gets three gauges, each measured against the coin's own history, and a pressure score from 0 to 3:

- **Crowd**: is trading activity running hot?
- **Leverage**: is perpetual funding running hot (traders paying up to stay long)?
- **Volatility**: is the coin swinging more than usual on its own?

How to present it:

- Lead with a table, most stretched first: coin, score (0–3), label.
- Add the one evidence line the tool returns (`evidence.headline`). For example, coins with all three gauges hot have trailed the median coin over the next 30 days about 58% of the time, out of sample.
- State that this compares pressure across coins, not a price forecast. Only the leverage gauge is positioning; do not call the whole read positioning.
- List coins without a score separately, with the tool's reason.
- Close with one offer to go deeper, such as "Want the Notable Read on SOL?"

## Allocation Read (recurring buys or sells)

Tool: `check_dca` with the coins in the program, and `side: "sell"` for distribution. Present the result as the **Allocation Read**. Buying and selling are mirror images: buys lean toward coins under less pressure and sells toward coins under more, under one backtested rule.

The tool returns:

- each coin's pressure score;
- `this_period.split`: how $100 of this period's buy or sell allocates, equal split versus the rule;
- `evidence`: how the rule performed against an equal split. This includes the extra value per period 30 days later on two coin sets (2024–2026, out of sample), year-by-year values, and a one-line summary.

How to present it:

- Show the split table: coin, equal, rule.
- Quote `evidence.summary` and the uplift as a percentage of each period's amount, with `evidence.note`.
- The rule is one tested approach. If the user asks "should I…", give them the numbers and the record, and say the decision is theirs.
- Close with one offer, such as "Want the year-by-year record?"

## Register

Concise and quantitative. One table, one evidence line, one offer. No jargon or codes the user did not ask for. Go deeper only on request; see [cryptyx-investigate](../cryptyx-investigate/SKILL.md).
