# Changelog

## 0.3.0

- Journey re-centred on THE STUDY (`get_coin_study`): two-horizon read per coin, what followed similar readings in the coin's history (7/30/90 days, listed as history), setups firing or close to firing, what changed. Multi-coin scan via `get_heat_check`.
- Retired the cross-coin allocation read and the invented read names; describe, never prescribe.

## 0.2.0

- Recurring checks lead with what changed: every Pressure, Allocation and Notable Read carries a `changes` block (default 7 days back), and the skills tell agents to open with it.
- Pressure Read and Notable Read naming; pooled-record explanation; repo root installable for Grok Build and the Claude Code marketplace.

## 0.1.0 — Unreleased

- Four skills: `cryptyx` (router), `cryptyx-holdings` (Pressure Read, Allocation Read), `cryptyx-investigate` (deeper reads on request), `cryptyx-exchange-bridge` (Coinbase, Kraken, Binance, Hyperliquid references; symbols only).
- Portable, Claude Code (Grok Build-readable) and Codex packages built from one skill library, with validation and checksums.
