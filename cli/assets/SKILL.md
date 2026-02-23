---
name: mobile-best-practices
description: "Mobile development intelligence for Android, iOS, Flutter, and React Native. 2,042 searchable entries: 49 architecture patterns, 117 design patterns, 91 UI patterns, 120 anti-patterns, 103 libraries, 228 performance rules, 437 security practices, 73 testing patterns, 56 reasoning rules, 18 project templates, 592 platform-specific guidelines, 80 copy-paste code snippets, and 78 Gradle dependency declarations. Use when building, reviewing, fixing, or optimizing mobile apps."
license: MIT
compatibility: Requires Python 3.x for BM25 search. Works with Claude Code and other skills-compatible agents.
metadata:
  author: tungnk123
  version: "1.6.0"
  usage: "READER | AGENT | CLI"
  invocation: "explicit-only — database is never searched automatically"
  modes:
    reader: "Browse CSV/markdown files directly — no Python or IDE required"
    agent: "Explicit slash command /mobile-best-practices in Claude Code only"
    cli: "python3 scripts/search.py — direct terminal search, works outside Claude Code"
---

# Mobile Best Practices

**2,042 searchable best practices** for Android, iOS, Flutter, and React Native. Android-first with Jetpack Compose.

## How to Use

This skill **does not trigger automatically**. The database is only searched when you explicitly invoke it. Three ways to use it:

| Mode | How | Requires |
|------|-----|----------|
| **AGENT** | `/mobile-best-practices` slash command in Claude Code | Claude Code + IDE restart |
| **CLI** | `python3 scripts/search.py "<query>" -p android` | Python 3 |
| **READER** | Open CSV/markdown files directly | Nothing |

### AGENT — Slash command (primary mode)

```
/mobile-best-practices
```

> **Restart your IDE after installing.** The slash command registry is only loaded at startup — the skill will not appear until you restart.
>
> ⚠️ **Some IDEs do not support slash skills** (e.g. certain VS Code forks, JetBrains AI Assistant, non-Claude agents). Use CLI mode in those cases.

### CLI — Terminal search

```bash
python3 scripts/search.py "<query>" -p android -n 3
```

Works anywhere Python 3 is available. No IDE needed.

### READER — Browse files directly

No tooling required. Open the source files:

| File | Content |
|------|---------|
| `data/platforms/android.csv` | 423 Android/Compose guidelines |
| `data/platforms/ios.csv` | iOS/SwiftUI guidelines |
| `data/code-snippets.csv` | 80 copy-paste code templates |
| `data/security.csv` | 437 security practices |
| `references/CODE-RULES.md` | Code generation rules |
| `references/CHECKLIST.md` | Pre-delivery checklist |

## Installation

```bash
# via npm
npx mobile-best-practices install

# or manually symlink
ln -s /path/to/mobile-best-practices ~/.claude/skills/mobile-best-practices
```

**After installing, restart your IDE** to register the `/mobile-best-practices` slash command.

## Prerequisites

Python 3.x required. Check: `python3 --version`

## Search

```bash
python3 scripts/search.py "<query>" --domain <domain> [-n <max_results>]
python3 scripts/search.py "<query>" --platform <platform>
python3 scripts/search.py "<query>" --domain <domain> --filter-platform <platform>
python3 scripts/search.py "<query>" --domain <domain> --compact  # token-optimized output
```

### Domains (12)

| Domain | Use For |
|--------|---------|
| `snippet` | Copy-paste code templates |
| `gradle` | Gradle dependency declarations |
| `designpattern` | Design patterns & code smell detection |
| `reasoning` | Product type recommendations |
| `architecture` | Architecture patterns |
| `library` | Libraries and dependencies |
| `ui` | UI patterns and components |
| `antipattern` | Common mistakes |
| `performance` | Performance optimization |
| `security` | Security best practices |
| `testing` | Testing patterns |
| `template` | Project starters |

### Platforms

`android` (423) | `android-xml` (423) | `ios` (60) | `flutter` (54) | `react-native` (55)

### Flags

`--domain`/`-d` domain | `--platform`/`-p` platform | `--filter-platform`/`-fp` filter | `--stack`/`-s` tech stack | `--max-results`/`-n` count (default: 3) | `--compact`/`-c` shorter output | `--json` JSON output | `--persist` save blueprint

## Workflow

When user requests mobile work, **default to Android with Jetpack Compose** unless specified otherwise.

### Build: search snippet → gradle → platform → antipattern → designpattern → architecture

```bash
python3 scripts/search.py "viewmodel repository" --domain snippet -n 3
python3 scripts/search.py "hilt room retrofit" --domain gradle -n 5
python3 scripts/search.py "compose state" --platform android -n 5
python3 scripts/search.py "android compose" --domain antipattern
python3 scripts/search.py "repository factory" --domain designpattern
python3 scripts/search.py "mvvm clean" --domain architecture
```

### Review: antipattern → designpattern → platform → performance → security

```bash
python3 scripts/search.py "android compose viewmodel" --domain antipattern -n 5
python3 scripts/search.py "code smell switch if-else" --domain designpattern -n 5
python3 scripts/search.py "state recomposition lifecycle" --platform android -n 5
python3 scripts/search.py "compose lazy startup" --domain performance
python3 scripts/search.py "storage encryption api key" --domain security
```

## Code Quality

Before generating code, read [code generation rules](references/CODE-RULES.md). Before delivering, verify against [pre-delivery checklist](references/CHECKLIST.md).
