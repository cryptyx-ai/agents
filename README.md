# CRYPTYX for Agents

**CRYPTYX — Digital Asset Intelligence. Sharpen your edge. Feed your agent the CRYPTYX quant engine.**

Institutional-grade quant intelligence for digital assets. Scan the market on hundreds of metrics, study every prior instance of a move, and build and backtest the strategies your agent runs.

It's a multi-factor, multi-horizon quant engine: hundreds of metrics across 8 factor classes for the most-traded digital assets, each read on 8 horizons from 1 to 365 days and scored against the asset's own trailing year, with daily history back to 2021. Your agent reads the intelligence; your rules decide; your exchange executes.

## Start with a goal

| Goal | Ask your agent |
| --- | --- |
| **Accumulate** with a rule, not a hunch | "My rule: add to ETH only when it's statistically oversold vs its 1-year history. Where is it now, and what followed the last times?" |
| **Take profit** when the data says extended | "Where is BTC on the 90- and 180-day horizons against its own history, and what followed similar readings?" |
| **Trade short-term** with sharper entries and exits | "Which of ETH, SOL and DOGE have short-term momentum, and what changed this week?" |
| **Catch statistically significant shifts** | "Which assets just had a statistically significant volatility expansion?" |
| **Hold long-term** on the right side of the trend | "Where are BTC and ETH on the 90-, 180- and 365-day horizons?" |
| **Build and test strategies** | "Find assets that are oversold vs their 90-day history with an improving trend, then backtest that combination." |

Every answer ends with one next step: a recheck you can ask your own agent to schedule, or one level deeper. You own the rules; CRYPTYX evaluates the conditions and shows what followed before, with sample sizes and base rates.

## What's under the hood

- **Asset intelligence:** one asset on every horizon vs its own history and the market, every prior instance of a condition, and what followed at 7, 30 and 90 days vs the base rate.
- **Market scan:** scan every asset CRYPTYX covers for a condition on any metric and horizon.
- **Strategy research and backtesting:** one reading or several factors at once on the full daily history (back to 2021), every horizon vs the base rate.
- **Statistically significant shifts** by factor class (volatility expansion, trend emergence, flow turns), found by scanning a metric across all assets.

## Connect

Remote MCP: `https://mcp.cryptyx.ai/api/mcp`. Sign in through your client's OAuth flow. The overview, asset study, episode study, coverage and data freshness are free with daily limits; scans and backtests are on Pro.

## Skills

| Skill | Purpose |
| --- | --- |
| [cryptyx](skills/cryptyx/SKILL.md) | Entry point: routes each question by the user's goal |
| [cryptyx-holdings](skills/cryptyx-holdings/SKILL.md) | The asset study on each asset you hold or watch |
| [cryptyx-investigate](skills/cryptyx-investigate/SKILL.md) | Going deeper: every prior instance of a move and what followed, backtests |
| [cryptyx-build-setup](skills/cryptyx-build-setup/SKILL.md) | Test your own idea: from one reading to a multi-factor, multi-horizon combination, with episodes, hit rate, drawdowns and the base rate |
| [cryptyx-exchange-bridge](skills/cryptyx-exchange-bridge/SKILL.md) | Reads holdings from an exchange connection; symbols only |

## Install

- **Grok Build:** install `cryptyx` from the xAI plugin marketplace.
- **Claude Code:** `/plugin marketplace add cryptyx-ai/agents`, then install `cryptyx`. Open `/mcp` to sign in.
- **Any MCP client:** add `https://mcp.cryptyx.ai/api/mcp` as a remote MCP server and sign in with OAuth.

## Network endpoints and credentials

- The only network endpoint is the CRYPTYX remote MCP server, `https://mcp.cryptyx.ai/api/mcp`, over HTTPS.
- Credentials: OAuth sign-in handled by your client. The plugin contains no API keys, scripts, hooks or local executables.
- Data sent: asset symbols and the read requested. Never balances, position sizes or account identifiers.

## Packages

The repository root is itself a plugin. `python3 scripts/build-distributions.py dist` also builds three standalone packages under `dist/packages/`, with a `SHA256SUMS` file:

- `cryptyx-agent-plugin-vX.Y.Z`: portable [Agent Plugins 1.0.0](https://agent-plugins.org/) package (Cursor, Hermes and other compatible clients).
- `cryptyx-claude-vX.Y.Z`: Claude Code package (also readable by Grok Build).
- `cryptyx-codex-vX.Y.Z`: Codex marketplace containing the portable package.

Claude Code: `claude --plugin-dir "$PWD"` from the extracted Claude package, then `/mcp` to sign in.

## Privacy

CRYPTYX receives asset symbols only, never balances, position sizes or account identifiers. Requests for assets not yet covered are counted per symbol and day, with no personal data, to decide which assets to add next.

## Legal notice

CRYPTYX provides historical market statistics. Nothing here is an offer, a solicitation or investment advice, and historical results do not predict future results. You are responsible for your agent's actions and for any orders you approve on your exchange. Digital assets carry substantial risk of loss.

## License

MIT. The license does not grant rights to CRYPTYX names or logos.
