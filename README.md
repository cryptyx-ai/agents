# CRYPTYX Agents

Skills and an MCP connection that give AI agents CRYPTYX market evidence: which coins are running hot or cool, how a tested rule would split a DCA, and deeper investigation when the user asks for it.

It is built to sit next to an exchange connection the user already has (Coinbase, Kraken, Binance, Hyperliquid). The agent reads holdings from the exchange, sends only coin symbols to CRYPTYX, and leaves any order to the exchange's own approval flow.

## Remote MCP

`https://mcp.cryptyx.ai/api/mcp`. Sign in through your client's OAuth flow. Free accounts can run heat checks, DCA checks, coverage and data-freshness reads with daily limits. Deeper tools need a Pro account.

After connecting, try:

- "Run a heat check on ETH, SOL and DOGE."
- "I DCA weekly into ETH, SOL and AVAX. Run a DCA check."
- "Read my Coinbase balances and heat check what I hold." (needs a Coinbase connection too)

## Skills

| Skill | Purpose |
| --- | --- |
| [cryptyx](skills/cryptyx/SKILL.md) | Start here: picks the right tool and keeps the first answer simple |
| [cryptyx-holdings](skills/cryptyx-holdings/SKILL.md) | Heat check and DCA check on a set of coins |
| [cryptyx-investigate](skills/cryptyx-investigate/SKILL.md) | Going deeper: what's driving a reading, setups, backtests |
| [cryptyx-exchange-bridge](skills/cryptyx-exchange-bridge/SKILL.md) | Reading holdings from an exchange connection, symbols only |

## Packages

Run `python3 scripts/build-distributions.py dist` to build three packages under `dist/packages/`, with a `SHA256SUMS` file:

- `cryptyx-agent-plugin-vX.Y.Z`: portable [Agent Plugins 1.0.0](https://agent-plugins.org/) package (Cursor, Hermes and other compatible clients).
- `cryptyx-claude-vX.Y.Z`: Claude Code package (also readable by Grok Build).
- `cryptyx-codex-vX.Y.Z`: Codex marketplace containing the portable package.

Claude Code: `claude --plugin-dir "$PWD"` from the extracted Claude package, then `/mcp` to sign in.

## Privacy

CRYPTYX receives coin symbols, never balances, position sizes or account identifiers. Requests for coins CRYPTYX does not cover yet are counted per symbol and day, with no personal data, to decide which coins to add next.

## Legal notice

CRYPTYX provides historical market statistics. Nothing here is an offer, a solicitation or investment advice, and historical results do not predict future results. You are responsible for your agent's actions and for any orders you approve on your exchange. Digital assets carry substantial risk of loss.

## License

MIT. The license does not grant rights to CRYPTYX names or logos.
