# Mobile Best Practices - Development Intelligence

This file guides Claude Code (claude.ai/code) when working with this repository.

## Project Overview

**Mobile Best Practices** is a searchable database of **2,042 mobile development best practices** packaged as an AI skill for Claude Code and other AI coding assistants. It covers architecture patterns, design patterns, UI components, anti-patterns, libraries, performance rules, security practices, testing patterns, code snippets, Gradle dependencies, and platform-specific guidelines for Android, iOS, Flutter, and React Native.

## Architecture

**Source of Truth:** `src/mobile-best-practices/` — follows the [Agent Skills](https://agentskills.io/specification) open format. See `SKILL.md` for full skill documentation.

Key paths: `data/*.csv` (16 CSV databases), `scripts/core.py` (BM25 engine), `scripts/search.py` (CLI), `references/` (CODE-RULES.md, CHECKLIST.md), `templates/` (platform configs).

**CLI package:** `cli/` — npm installer with bundled assets in `cli/assets/`.

## Search Command

```bash
python3 src/mobile-best-practices/scripts/search.py "<query>" --domain <domain> [-n <max_results>]
```

Flags: `--domain`/`-d` | `--platform`/`-p` | `--filter-platform`/`-fp` | `--stack`/`-s` | `--max-results`/`-n` | `--compact`/`-c` | `--json` | `--persist`

## Sync Rules

When modifying files:

1. **Data & Scripts** — Always edit in `src/mobile-best-practices/`. Changes auto-available via symlinks to `.claude/skills/`.
2. **Templates** — Edit in `src/mobile-best-practices/templates/`.
3. **References** — Edit in `src/mobile-best-practices/references/`.
4. **CLI Assets** — Sync before publishing:
   ```bash
   cp -r src/mobile-best-practices/data/* cli/assets/data/
   cp -r src/mobile-best-practices/scripts/* cli/assets/scripts/
   cp -r src/mobile-best-practices/references/* cli/assets/references/
   cp -r src/mobile-best-practices/templates/* cli/assets/templates/
   ```

## Prerequisites

Python 3.x (no external dependencies required)

## Git Workflow

- Never push directly to `main`
- Create feature/fix branch: `git checkout -b feat/...` or `fix/...`
- Commit and push: `git push -u origin <branch>`
- Create PR: `gh pr create`

## Key Conventions

- CSV delimiter: comma (`,`), multi-value separator: pipe (`|`)
- Platform CSVs have `Docs URL` column; other CSVs have `Reference URL` column
- Code snippets use `\n` for literal newlines in quoted CSV fields
- Search engine: BM25 ranking with auto-domain detection
- Default platform: Android with Jetpack Compose (XML available via `android-xml`)
