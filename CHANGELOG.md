# Changelog

## 0.6.1

- Count-free copy (founder approved 2026-11-20): the plugin descriptions, README and skills no longer state scale numbers that drift as the engine grows ("200+ assets", "670+ metrics", "5+ years"). They say "hundreds of metrics", "the most-traded digital assets" and "every covered asset", and readings are scored against the asset's own trailing year, with daily history back to 2021 (the previous "scored against 5+ years" was wrong).
- "asset", not "coin", in the plugin README and the Binance and Hyperliquid exchange-bridge references.
- The build fails if shipped copy (READMEs, plugin and marketplace manifests, skills) carries a scale number or "coin" in prose; a GitHub Action runs the build on every PR.

## 0.6.0

- Release 1 of the CRYPTYX connector: skills use only the 11 tools the remote MCP now lists (overview, asset study, episode study, metric scan, single-metric and multi-factor backtests, price history, live prices, data freshness, coverage, featured metrics). Heat check, notable read, regime, setups and signals, divergences and custom triggers are no longer referenced; they stay available on the CRYPTYX REST API and x402.
- New routes: "is this move real / what followed" and "should I add on this dip" go to the asset study, then the episode study (free, 3 a day). Regime questions are answered from the readings.
- Every answer ends with a next step the user can take; the agent never promises to alert, ping, monitor or schedule. No buy, sell, add, trim or scale-in menus.
- One-liner aligned with the remote MCP server; "asset", not "coin", in prose.
- The build fails if a skill names a tool the connector does not list.

## 0.5.0

- One CRYPTYX on every surface: the README, plugin descriptions and router skill use the same positioning as the remote MCP server ("Sharpen your edge. Feed your agent the CRYPTYX quant engine."; institutional-grade quantitative intelligence, in plain English or all the way down).
- The router routes by goal: accumulate, take profit, trade short-term, catch statistically significant shifts, hold long-term, build and test strategies. Each goal has a first prompt and one next step.
- Horizons: all 8 (1–365 days) named, with groupings suggested rather than imposed.
- Removed advice-style copy ("add, trim or hold").

## 0.4.1

- README lists all five skills (adds `cryptyx-build-setup`, shipped in 0.4.0).

## 0.4.0

- New skill `cryptyx-build-setup`: the deep path from one reading to a multi-factor, multi-horizon setup or signal of the user's own (readings → conditions → setups → signals), reported with the full analytics: episodes, returns, hit rate and Sharpe against the coin's base rate, drawdowns, every horizon, and warnings.
- Router and investigate skills route "test my own idea" questions to it.

## 0.3.0

- Journey re-centred on THE STUDY (`get_coin_study`): two-horizon read per coin, what followed similar readings in the coin's history (7/30/90 days, listed as history), setups firing or close to firing, what changed. Multi-coin scan via `get_heat_check`.
- Retired the cross-coin allocation read and the invented read names; describe, never prescribe.

## 0.2.0

- Recurring checks lead with what changed: every Pressure, Allocation and Notable Read carries a `changes` block (default 7 days back), and the skills tell agents to open with it.
- Pressure Read and Notable Read naming; pooled-record explanation; repo root installable for Grok Build and the Claude Code marketplace.

## 0.1.0 — Unreleased

- Four skills: `cryptyx` (router), `cryptyx-holdings` (Pressure Read, Allocation Read), `cryptyx-investigate` (deeper reads on request), `cryptyx-exchange-bridge` (Coinbase, Kraken, Binance, Hyperliquid references; symbols only).
- Portable, Claude Code (Grok Build-readable) and Codex packages built from one skill library, with validation and checksums.
