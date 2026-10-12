# CRYPTYX for Agents

**Your agent can see your portfolio and place the trade. CRYPTYX gives it the intelligence to make the call.**

An agent connected to Coinbase, Kraken, Binance or Hyperliquid knows what you hold. It doesn't know whether the crowd is piling into those coins, whether leverage is building underneath them, or how moments like this have played out before. CRYPTYX does.

669 metrics across ~190 digital assets, scored every day against each coin's own history and the market. Setups are tested before they are shown, and history is labelled as history. Your agent reads the evidence, you make the decision, and the exchange executes it.

**Add, trim or hold: grounded in numbers, not narrative.**

## What your agent gets

**THE STUDY, for every coin you hold.** Where the coin stands on two horizons, tactical (7–14 days) and structural (60–180 days), across trend, volatility, flow, futures, options, order book and correlation. Every reading carries its z-score and where today sits in the coin's own history and against the rest of the market.

**What happened last time.** For each reading that is unusually stretched, the coin's past episodes at least as extreme, and what followed over the next 7, 30 and 90 days, set against the coin's normal returns. Presented as history, with the number of episodes, never as a forecast.

**Setups firing, or close to it.** Multi-metric setups from the CRYPTYX catalogue that are live or near-live on the coin, with their evidence tier and track record. Only setups that clear the evidence bar are shown.

**What changed.** Re-run the same check next week and your agent opens with what moved: gauges that flipped, readings that turned, setups that appeared or dropped off.

## Connect

Remote MCP: `https://mcp.cryptyx.ai/api/mcp`. Sign in through your client's OAuth flow. THE STUDY, the multi-coin scan, coverage and data-freshness reads are free with daily limits. The full engine is on Pro.

Then ask:

- "Run THE STUDY on SOL. Where is it stretched, and what followed the last times it looked like this?"
- "Pull my Coinbase holdings. Which of my coins stand out, and why?"
- "Scan ETH, SOL and DOGE. What changed since last week?"
- "Is any setup close to firing on AVAX? How has it played out before?"

## Skills

| Skill | Purpose |
| --- | --- |
| [cryptyx](skills/cryptyx/SKILL.md) | Entry point: routes each question and keeps the first answer sharp |
| [cryptyx-holdings](skills/cryptyx-holdings/SKILL.md) | THE STUDY on each coin you hold or watch, plus a quick scan |
| [cryptyx-investigate](skills/cryptyx-investigate/SKILL.md) | Going deeper: what else stands out, setup records, backtests |
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
