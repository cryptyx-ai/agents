---
name: cryptyx-holdings
description: Positioning Read and Allocation Read across a set of coins (a book, a watchlist, or the coins in a recurring buy or sell). Use for "where is positioning stretched", "what does the evidence say about this week's allocation", "should I add or trim" style questions. Quantitative, backtested, concise.
---

# CRYPTYX: Positioning Read and Allocation Read

Follow the [CRYPTYX router](../cryptyx/SKILL.md). If the coins come from an exchange account, read them first with the [exchange bridge](../cryptyx-exchange-bridge/SKILL.md).

## Positioning Read (any set of coins)

Tool: `get_heat_check` with 1–25 symbols. Present the result as the **Positioning Read**. Each coin gets three gauges, each measured against the coin's own history, and a positioning score from 0 to 3:

- **Crowd**: is trading volume running hot?
- **Leverage**: is futures funding running hot?
- **Volatility**: is the coin swinging more than usual on its own?

How to present it:

- Lead with a table, most stretched first: coin, score (0–3), label.
- Add the one evidence line the tool returns (`evidence.headline`). For example, coins with all three gauges hot have trailed the median coin over the next 30 days about 58% of the time, out of sample.
- State that this measures relative positioning against other coins, not a price forecast.
- List coins without a score separately, with the tool's reason.
- Close with one offer to go deeper, such as "Want the readings driving SOL?"

## Allocation Read (recurring buys or sells)

Tool: `check_dca` with the coins in the program, and `side: "sell"` for distribution. Present the result as the **Allocation Read**. Buying and selling are mirror images: buys lean toward cooler coins and sells toward hotter ones, under one backtested positioning rule.

The tool returns:

- each coin's positioning score;
- `this_period.split`: how $100 of this period's buy or sell allocates, equal split versus the rule;
- `evidence`: how the rule performed against an equal split. This includes the extra value per period 30 days later on two coin sets (2024–2026, out of sample), year-by-year values, and a one-line summary.

How to present it:

- Show the split table: coin, equal, rule.
- Quote `evidence.summary` and the uplift as a percentage of each period's amount, with `evidence.note`.
- The rule is one tested approach. If the user asks "should I…", give them the numbers and the record, and say the decision is theirs.
- Close with one offer, such as "Want the year-by-year record?"

## Register

Concise and quantitative. One table, one evidence line, one offer. No jargon or codes the user did not ask for. Go deeper only on request; see [cryptyx-investigate](../cryptyx-investigate/SKILL.md).
