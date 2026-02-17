---
name: mobile-best-practices
description: "Mobile development intelligence for Android, iOS, Flutter, and React Native. 2,024 searchable entries: 49 architecture patterns, 117 design patterns, 91 UI patterns, 113 anti-patterns, 103 libraries, 228 performance rules, 437 security practices, 73 testing patterns, 56 reasoning rules, 18 project templates, 582 platform-specific guidelines, 79 copy-paste code snippets, and 78 Gradle dependency declarations. Use when building, reviewing, fixing, or optimizing mobile apps."
license: MIT
compatibility: Requires Python 3.x for BM25 search. Works with Claude Code and other skills-compatible agents.
metadata:
  author: tungnk123
  version: "1.0"
---

# Mobile Best Practices

**2,024 searchable best practices** for Android, iOS, Flutter, and React Native. Android-first with Jetpack Compose.

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

`android` (413) | `android-xml` (413) | `ios` (60) | `flutter` (54) | `react-native` (55)

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
