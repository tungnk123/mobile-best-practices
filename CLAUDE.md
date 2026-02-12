# Mobile Best Practices - Development Intelligence

This file guides Claude Code (claude.ai/code) when working with this repository.

## Project Overview

**Mobile Best Practices** is a searchable database of 500+ mobile development best practices packaged as an AI skill for Claude Code and other AI coding assistants. It covers architecture patterns, UI components, anti-patterns, libraries, performance rules, security practices, testing patterns, code snippets, Gradle dependencies, and platform-specific guidelines for Android, iOS, Flutter, and React Native.

## Architecture

**Source of Truth:** `src/mobile-best-practices/`

```
src/mobile-best-practices/
├── data/                    (Canonical CSV databases - 15 files)
│   ├── architectures.csv    (26 architecture patterns)
│   ├── libraries.csv        (66 libraries)
│   ├── ui-patterns.csv      (57 UI/UX patterns)
│   ├── anti-patterns.csv    (56 anti-patterns)
│   ├── testing.csv          (37 testing patterns)
│   ├── security.csv         (36 security practices)
│   ├── performance.csv      (45 performance rules)
│   ├── code-snippets.csv    (30 code templates)
│   ├── reasoning-rules.csv  (34 product recommendations)
│   ├── project-templates.csv(20 starters)
│   ├── gradle-deps.csv      (48 Gradle deps)
│   └── platforms/
│       ├── android.csv      (60+ Android guidelines)
│       ├── ios.csv           (35+ iOS guidelines)
│       ├── flutter.csv       (34+ Flutter guidelines)
│       └── react-native.csv  (35+ React Native guidelines)
├── scripts/
│   ├── core.py              (BM25 search engine)
│   └── search.py            (CLI search interface)
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
└── package.json

.claude/skills/mobile-best-practices/ (symlinks to src/)
```

## Search Command

```bash
python3 src/mobile-best-practices/scripts/search.py "<query>" --domain <domain> [-n <max_results>]
```

### Domains
- `snippet` - Copy-paste code templates (Android)
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

3. **CLI Assets** - Sync before publishing:
   ```bash
   cp -r src/mobile-best-practices/data/* cli/assets/data/
   cp -r src/mobile-best-practices/scripts/* cli/assets/scripts/
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
