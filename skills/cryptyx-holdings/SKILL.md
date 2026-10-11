---
name: cryptyx-holdings
description: Check a set of coins (holdings, a watchlist or a DCA) with CRYPTYX - which are running hot or cool, and for a DCA, how a tested rule would split this period and what that rule did historically. Use for "heat check my coins", "check my DCA", "should I add or trim" style questions. Answers stay simple.
---

# CRYPTYX holdings check

Follow the [CRYPTYX router](../cryptyx/SKILL.md). If the coins come from an exchange account, read them first with the [exchange bridge](../cryptyx-exchange-bridge/SKILL.md).

## Heat check (any set of coins)

Call `get_heat_check` with 1–25 symbols. Each coin gets three gauges and a heat score from 0 to 3:

- **Crowd heat**: is trading volume running high against the coin's own history?
- **Leverage heat**: is futures funding running high?
- **Volatility heat**: is the coin swinging more than usual on its own?

How to answer:

- Lead with a short table: coin, heat score, label. Sort hottest first.
- Add one line from the tool's `evidence.headline`. For example: coins with all 3 gauges hot have lagged the median coin over the next 30 days about 58% of the time.
- This is a comparison with other coins, not a price forecast. Say so when quoting it.
- List coins without a score separately, with the tool's reason.
- Offer one next step, such as "Want to see what's driving SOL's heat?"

## DCA check (recurring buys or sells)

Call `check_dca` with the coins in the DCA, and `side: "sell"` for a selling program. The tool returns:

- each coin's heat score;
- `this_period.split`: how $100 of this period's buy or sell divides with an equal split and with the tested rule;
- `evidence`: the rule's history against an equal split. This includes the extra value per period 30 days later, on two coin sets, for 2024–2026, plus year-by-year values and a one-line summary.

How to answer:

- Show the split table: coin, equal, rule.
- Quote `evidence.summary` and the uplift numbers as percentages of each period's amount, with `evidence.note`.
- The rule is one tested approach, not a recommendation. Do not tell the user to change their DCA. If they ask "should I…", give them the numbers and the history, and say the choice is theirs.
- Offer: "Want the year-by-year results?" or "Want to see what's driving the hottest coin?"

## Keep it simple

Retail users want a clear read, not a research report. Keep to one table, one evidence line and one offer. Go deeper only when the user asks; see [cryptyx-investigate](../cryptyx-investigate/SKILL.md).
