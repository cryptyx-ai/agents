# CRYPTYX for Agents

**CRYPTYX — Digital Asset Intelligence. Sharpen your edge. Feed your agent the CRYPTYX quant engine.**

Institutional-grade quantitative intelligence for digital assets. Ask about any coin in plain English, or go all the way down: scan the market, build and backtest your own strategies.

Whether you're trading short-term, accumulating over months, taking profit into strength or watching for a statistically significant shift, CRYPTYX gives your agent the numbers behind the call. It's a multi-factor, multi-horizon quant engine: 670+ metrics across 8 factor classes for 200+ coins, each read on 8 horizons from 1 to 365 days, with 5+ years of daily history. Ask about any coin in plain English and see what followed similar moments before. Or go deeper: 150 multi-factor setups and 160 signals with their track records, market-wide scans, and backtests of your own strategies. Your agent reads the intelligence; your rules decide; your exchange executes.

## Start with a goal

| Goal | Ask your agent |
| --- | --- |
| **Accumulate** with a rule, not a hunch | "My rule: add to ETH only when it's statistically oversold vs its 1-year history. Where is it now, and what followed the last times?" |
| **Take profit** when the data says stretched | "Is BTC stretched on the 90- and 180-day horizons? What happened after similar readings?" |
| **Trade short-term** with sharper entries and exits | "Which of ETH, SOL and DOGE have short-term momentum, and what changed this week?" |
| **Catch statistically significant shifts** | "Which coins just had a statistically significant volatility expansion or trend breakout?" |
| **Hold long-term** on the right side of the trend | "Where are BTC and ETH on the 90-, 180- and 365-day horizons?" |
| **Build and test strategies** | "Find coins that are oversold vs their 90-day history with an improving trend, then backtest that combination." |

Every answer ends with one next step: a recheck your agent can schedule, or one level deeper. You own the rules; CRYPTYX evaluates the conditions and shows what followed before, with sample sizes and base rates.

## What's under the hood

- **Coin intelligence:** one coin or a basket on every horizon, vs its own history and the market, with what followed similar readings.
- **Market scan and rankings:** scan 200+ coins for a condition; rank by factor class.
- **Setups and signals:** trend and momentum, mean reversion, volatility compression and expansion, capitulation, breakouts, each with its track record and evidence tier.
- **Strategy research and backtesting:** single metrics, multi-factor combinations, cross-horizon gaps and signal variants on 5+ years, every horizon vs the base rate.
- **Shifts and risk context:** statistically significant shifts by factor class, divergences between factors, liquidity.

## Connect

Remote MCP: `https://mcp.cryptyx.ai/api/mcp`. Sign in through your client's OAuth flow. Coin study, quick scan, notable read, coverage and data freshness are free with daily limits; the full engine is on Pro.

## Skills

| Skill | Purpose |
| --- | --- |
| [cryptyx](skills/cryptyx/SKILL.md) | Entry point: routes each question by the user's goal |
| [cryptyx-holdings](skills/cryptyx-holdings/SKILL.md) | The coin study on each coin you hold or watch, plus a quick scan |
| [cryptyx-investigate](skills/cryptyx-investigate/SKILL.md) | Going deeper: what else stands out, setup records, backtests |
| [cryptyx-build-setup](skills/cryptyx-build-setup/SKILL.md) | Test your own idea: from one reading to a multi-factor, multi-horizon setup, with episodes, hit rate, drawdowns and the base rate |
| [cryptyx-exchange-bridge](skills/cryptyx-exchange-bridge/SKILL.md) | Reads holdings from an exchange connection; symbols only |

## Install

- **Grok Build:** install `cryptyx` from the xAI plugin marketplace.
- **Claude Code:** `/plugin marketplace add cryptyx-ai/agents`, then install `cryptyx`. Open `/mcp` to sign in.
- **Any MCP client:** add `https://mcp.cryptyx.ai/api/mcp` as a remote MCP server and sign in with OAuth.

## Network endpoints and credentials

- The only network endpoint is the CRYPTYX remote MCP server, `https://mcp.cryptyx.ai/api/mcp`, over HTTPS.
- Credentials: OAuth sign-in handled by your client. The plugin contains no API keys, scripts, hooks or local executables.
- Data sent: coin symbols and the read requested. Never balances, position sizes or account identifiers.

## Packages

The repository root is itself a plugin. `python3 scripts/build-distributions.py dist` also builds three standalone packages under `dist/packages/`, with a `SHA256SUMS` file:

- `cryptyx-agent-plugin-vX.Y.Z`: portable [Agent Plugins 1.0.0](https://agent-plugins.org/) package (Cursor, Hermes and other compatible clients).
- `cryptyx-claude-vX.Y.Z`: Claude Code package (also readable by Grok Build).
- `cryptyx-codex-vX.Y.Z`: Codex marketplace containing the portable package.

Claude Code: `claude --plugin-dir "$PWD"` from the extracted Claude package, then `/mcp` to sign in.

## Privacy

CRYPTYX receives coin symbols only, never balances, position sizes or account identifiers. Requests for coins not yet covered are counted per symbol and day, with no personal data, to decide which coins to add next.

## Legal notice

CRYPTYX provides historical market statistics. Nothing here is an offer, a solicitation or investment advice, and historical results do not predict future results. You are responsible for your agent's actions and for any orders you approve on your exchange. Digital assets carry substantial risk of loss.

## License

MIT. The license does not grant rights to CRYPTYX names or logos.
