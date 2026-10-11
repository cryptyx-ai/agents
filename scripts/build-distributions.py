#!/usr/bin/env python3
"""Build and validate the CRYPTYX agent plugin distributions.

Usage: python3 scripts/build-distributions.py dist

Produces, under <out>/packages/:
  cryptyx-agent-plugin-vX.Y.Z  portable Agent Plugins 1.0.0 package (Cursor, Hermes, ...)
  cryptyx-claude-vX.Y.Z        Claude Code / Grok Build package (.claude-plugin + .mcp.json)
  cryptyx-codex-vX.Y.Z         Codex marketplace wrapping the portable package
plus a SHA256SUMS file. Standard library only; the repository root is not a plugin.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MCP_URL = "https://mcp.cryptyx.ai/api/mcp"
SKILLS = ("cryptyx", "cryptyx-exchange-bridge", "cryptyx-holdings", "cryptyx-investigate")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)#]+)(?:#[^)]*)?\)")


def load(path: Path) -> dict:
    with path.open() as f:
        return json.load(f)


def fail(msg: str) -> None:
    raise SystemExit(f"build failed: {msg}")


def validate_sources() -> str:
    claude = load(ROOT / "src/plugins/claude/plugin.json")
    portable = load(ROOT / "src/plugins/portable/plugin.json")
    market = load(ROOT / "src/plugins/claude/marketplace.json")
    version = claude["version"]
    if portable.get("version") != version or market["plugins"][0].get("version") != version:
        fail("version mismatch across manifests")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        fail(f"version is not semver: {version}")

    # Portable manifest: only schema-declared top-level keys (schema has additionalProperties: false).
    allowed = set(load(ROOT / "schemas/1.0.0/plugin.schema.json")["properties"])
    extra = set(portable) - allowed
    if extra:
        fail(f"portable plugin.json has keys outside the schema: {sorted(extra)}")
    for key in ("$schema", "name"):
        if key not in portable:
            fail(f"portable plugin.json missing {key}")

    # Every MCP declaration points at the one canonical endpoint.
    servers = [
        claude["mcpServers"]["cryptyx"],
        load(ROOT / "src/plugins/claude/mcp.json")["mcpServers"]["cryptyx"],
        load(ROOT / "src/plugins/portable/mcp.json")["mcpServers"]["cryptyx"],
    ]
    if any(s.get("url") != MCP_URL for s in servers):
        fail(f"every MCP server must use {MCP_URL}")

    # Skills: expected set, valid frontmatter, local links resolve.
    found = sorted(p.name for p in (ROOT / "skills").iterdir() if p.is_dir())
    if found != sorted(SKILLS):
        fail(f"expected skills {sorted(SKILLS)}, found {found}")
    for name in SKILLS:
        md = ROOT / "skills" / name / "SKILL.md"
        text = md.read_text()
        m = re.match(r"^---\nname: (.+)\ndescription: (.+)\n---\n", text)
        if not m or m.group(1) != name or not NAME_RE.match(name):
            fail(f"bad frontmatter in {md}")
        for doc in [md, *sorted((md.parent / "references").glob("*.md"))]:
            for link in LINK_RE.findall(doc.read_text()):
                if link.startswith("http"):
                    continue
                if not (doc.parent / link).resolve().is_file():
                    fail(f"broken link {link} in {doc.relative_to(ROOT)}")
    return version


def copy_skills(target: Path) -> None:
    shutil.copytree(ROOT / "skills", target / "skills", ignore=shutil.ignore_patterns(".DS_Store"))
    shutil.copy2(ROOT / "LICENSE", target / "LICENSE")
    shutil.copy2(ROOT / "src/plugins/README.md", target / "README.md")


def build(out: Path) -> None:
    version = validate_sources()
    pkgs = out / "packages"
    if out.exists():
        shutil.rmtree(out)
    pkgs.mkdir(parents=True)

    portable = pkgs / f"cryptyx-agent-plugin-v{version}"
    portable.mkdir()
    shutil.copy2(ROOT / "src/plugins/portable/plugin.json", portable / "plugin.json")
    shutil.copy2(ROOT / "src/plugins/portable/mcp.json", portable / "mcp.json")
    copy_skills(portable)

    claude = pkgs / f"cryptyx-claude-v{version}"
    (claude / ".claude-plugin").mkdir(parents=True)
    shutil.copy2(ROOT / "src/plugins/claude/plugin.json", claude / ".claude-plugin/plugin.json")
    shutil.copy2(ROOT / "src/plugins/claude/marketplace.json", claude / ".claude-plugin/marketplace.json")
    # Grok Build reads MCP servers only from .mcp.json at the plugin root.
    shutil.copy2(ROOT / "src/plugins/claude/mcp.json", claude / ".mcp.json")
    copy_skills(claude)

    codex = pkgs / f"cryptyx-codex-v{version}"
    (codex / ".agents/plugins").mkdir(parents=True)
    shutil.copy2(ROOT / "src/plugins/codex/marketplace.json", codex / ".agents/plugins/marketplace.json")
    shutil.copytree(portable, codex / "plugins/cryptyx")
    shutil.copy2(ROOT / "LICENSE", codex / "LICENSE")

    lines = []
    for pkg in sorted(pkgs.iterdir()):
        for f in sorted(p for p in pkg.rglob("*") if p.is_file()):
            lines.append(f"{hashlib.sha256(f.read_bytes()).hexdigest()}  {f.relative_to(pkgs)}")
    (out / "SHA256SUMS").write_text("\n".join(lines) + "\n")
    print(f"built v{version}: " + ", ".join(p.name for p in sorted(pkgs.iterdir())))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: build-distributions.py <out-dir>")
    build(ROOT / sys.argv[1])
