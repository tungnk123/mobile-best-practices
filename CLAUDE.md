# Mobile Best Practices - Development Intelligence

This file guides Claude Code (claude.ai/code) when working with this repository.

## Project Overview

**Mobile Best Practices** is a searchable database of **1,896 mobile development best practices** packaged as an AI skill for Claude Code and other AI coding assistants. It covers architecture patterns, UI components, anti-patterns, libraries, performance rules, security practices, testing patterns, code snippets, Gradle dependencies, and platform-specific guidelines for Android, iOS, Flutter, and React Native.

## Architecture

**Source of Truth:** `src/mobile-best-practices/`

Follows the [Agent Skills](https://agentskills.io/specification) open format.

```
src/mobile-best-practices/           (Agent Skills directory)
├── SKILL.md                 (Required: skill metadata + instructions)
├── data/                    (Canonical CSV databases - 15 files)
│   ├── architectures.csv    (49 architecture patterns)
│   ├── libraries.csv        (101 libraries)
│   ├── ui-patterns.csv      (91 UI/UX patterns)
│   ├── anti-patterns.csv    (113 anti-patterns)
│   ├── testing.csv          (73 testing patterns)
│   ├── security.csv         (437 security practices)
│   ├── performance.csv      (228 performance rules)
│   ├── code-snippets.csv    (79 code templates)
│   ├── reasoning-rules.csv  (56 product recommendations)
│   ├── project-templates.csv(18 starters)
│   ├── gradle-deps.csv      (78 Gradle deps)
│   └── platforms/
│       ├── android.csv      (404 Android guidelines)
│       ├── ios.csv           (60 iOS guidelines)
│       ├── flutter.csv       (54 Flutter guidelines)
│       └── react-native.csv  (55 React Native guidelines)
├── scripts/                 (Executable code for agents)
│   ├── core.py              (BM25 search engine)
│   └── search.py            (CLI search interface)
├── references/              (Progressive disclosure docs)
│   ├── CODE-RULES.md        (Code generation rules & anti-patterns)
│   └── CHECKLIST.md         (Pre-delivery quality checklist)
└── templates/
    ├── base/
    │   ├── skill-content.md  (Common SKILL.md content)
    │   └── quick-reference.md
    └── platforms/            (AI platform configs)
        ├── claude.json
        ├── cursor.json
        ├── windsurf.json
        └── ...

cli/                          (npm installer: mobile-best-practices)
├── src/
├── assets/                   (bundled data ~500KB)
│   ├── data/                 (CSV databases)
│   ├── scripts/              (Search engine)
│   ├── references/           (Reference docs)
│   ├── skills/               (Platform-specific SKILL.md variants)
│   └── templates/            (Platform configs)
└── package.json

.claude/skills/mobile-best-practices/ (symlinks to src/)
├── SKILL.md → src/SKILL.md
├── data → src/data
├── scripts → src/scripts
└── references → src/references
```

## Search Command

```bash
python3 src/mobile-best-practices/scripts/search.py "<query>" --domain <domain> [-n <max_results>]
```

### Domains
- `snippet` - Copy-paste code templates (Android, iOS, Flutter, React Native)
- `gradle` - Gradle dependency declarations
- `reasoning` - Product type recommendations
- `architecture` - Architecture patterns
- `library` - Libraries and dependencies
- `ui` - UI patterns and components
- `antipattern` - Common mistakes
- `performance` - Performance optimization
- `security` - Security best practices
- `testing` - Testing patterns
- `template` - Project starters

### Flags
- `--domain` / `-d` - Search specific domain
- `--platform` / `-p` - Platform-specific search (android, ios, flutter, react-native)
- `--filter-platform` / `-fp` - Filter results by platform
- `--stack` / `-s` - Filter by tech stack (compose, swiftui, flutter, react-native)
- `--persist` - Save results to architecture blueprint file
- `--max-results` / `-n` - Number of results (default: 3)
- `--json` - Output as JSON

## Sync Rules

When modifying files:

1. **Data & Scripts** - Always edit in `src/mobile-best-practices/`:
   - `data/*.csv` and `data/platforms/*.csv`
   - `scripts/*.py`
   - Changes auto-available via symlinks to `.claude/skills/`

2. **Templates** - Edit in `src/mobile-best-practices/templates/`:
   - `base/skill-content.md` - Common SKILL.md content
   - `platforms/*.json` - Platform-specific configs

3. **References** - Edit in `src/mobile-best-practices/references/`:
   - `CODE-RULES.md` - Code generation rules and anti-patterns
   - `CHECKLIST.md` - Pre-delivery quality checklist

4. **CLI Assets** - Sync before publishing:
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
- Platform CSVs already have `Docs URL` column
- Other CSVs have `Reference URL` column
- Code snippets use `\n` for literal newlines in quoted CSV fields
- Search engine: BM25 ranking with auto-domain detection
- Default platform: Android with Jetpack Compose
