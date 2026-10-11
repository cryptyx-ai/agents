# CRYPTYX for Agents

**Your agent can see your portfolio and place the trade. CRYPTYX gives it the intelligence to make the call.**

An agent connected to Coinbase, Kraken, Binance or Hyperliquid knows what you hold. It doesn't know whether the crowd is piling into those coins, whether leverage is building underneath them, or whether the rule you're about to follow has ever worked. CRYPTYX does.

670+ metrics across ~190 digital assets, scored every day against each asset's own history. Rules are pre-registered and backtested out of sample before a single result is quoted. Your agent reads the evidence, you make the decision, and the exchange executes it.

**Add, trim, hold, or how to split this week's accumulation: grounded in numbers, not narrative.**

## What your agent gets

**Pressure Read.** For every coin in your book: crowd activity, leverage (perpetual funding) and coin-specific volatility, each measured against the coin's own history, and where the coin sits against the rest of the market. Pressure has a measurable record. Coins with all three gauges running hot have trailed the median coin over the following 30 days about 58% of the time, out of sample and replicated on a separate set of 147 coins.

**Allocation Read.** For a recurring buy or sell, whether retail DCA or treasury distribution: how this period's allocation splits under a backtested pressure rule versus an equal split, and how that rule has performed against an equal split, year by year. Buying and selling are mirror images: buys lean toward coins under less pressure, sells toward coins under more.

**Notable Read and depth on demand.** When the question becomes *why*, your agent goes further into the engine, still in plain language: the readings furthest from each coin's own norm, setups firing or close to firing with their evidence tier and track record, and backtests of your own ideas.

## Connect

Remote MCP: `https://mcp.cryptyx.ai/api/mcp`. Sign in through your client's OAuth flow. Pressure Read, Allocation Read, Notable Read, coverage and data-freshness reads are free with daily limits. The full engine is on Pro.

Then ask:

- "Where is pressure building across ETH, SOL and DOGE?"
- "I accumulate ETH, SOL and AVAX weekly. What does the evidence say about this week's allocation?"
- "Pull my Coinbase holdings and run a Pressure Read across the book."
- "I'm distributing a SOL position over 12 weeks. How has a pressure-weighted schedule compared with equal tranches?"

## Skills

| Skill | Purpose |
| --- | --- |
| [cryptyx](skills/cryptyx/SKILL.md) | Entry point: routes each question and keeps the first answer sharp |
| [cryptyx-holdings](skills/cryptyx-holdings/SKILL.md) | Pressure Read and Allocation Read across a book or watchlist |
| [cryptyx-investigate](skills/cryptyx-investigate/SKILL.md) | Notable Read and depth on demand: drivers, setups, backtests |
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
