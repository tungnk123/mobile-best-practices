---
name: mobile-best-practices
description: "Flutter development intelligence with Dart. 1,738 searchable entries including 54 Flutter-specific guidelines. Default stack: BLoC/Riverpod + Dio + GoRouter + Drift + CachedNetworkImage. Use when building, reviewing, fixing, or optimizing Flutter apps. Covers architecture patterns, UI components, anti-patterns, performance, security, and testing."
license: MIT
compatibility: Requires Python 3.x for BM25 search. Works with Claude Code and other skills-compatible agents.
metadata:
  author: tungnk123
  version: "1.0"
---

# Flutter Best Practices - Dart Development Intelligence

Searchable database of **1,738 mobile best practices**, **optimized for Flutter with Dart**. All searches default to Flutter platform. Covers architecture, widgets, state management, performance, and testing for cross-platform Flutter apps.

## Prerequisites

```bash
python3 --version || python --version
```

If not installed: `brew install python3` (macOS) | `sudo apt install python3` (Linux) | `winget install Python.Python.3.12` (Windows)

---

## How to Use This Skill

When user requests Flutter development work (build, create, architect, review, fix, optimize), follow this workflow:

### Step 1: Extract Requirements

No need to detect platform - **always Flutter with Dart**. Extract:
- **Product type**: E-commerce, Banking, Social Media, Healthcare, Delivery, Fitness, Education, Chat
- **State management**: BLoC (default), Riverpod, Provider, GetX
- **Scope**: New project, new feature, code review, refactor, fix bug, optimize

### Step 2: Search the Database

Use `search.py` with `--platform flutter` or `--stack flutter` for focused results.

```bash
# Flutter platform guidelines (ALWAYS search this first)
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --platform flutter -n 5

# Stack-specific search
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --stack bloc
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --stack riverpod

# Architecture patterns
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain architecture

# Anti-patterns filtered for Flutter
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain antipattern --filter-platform flutter

# Performance rules filtered for Flutter
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain performance --filter-platform flutter

# Libraries for Flutter
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain library --filter-platform flutter
```

### Step 3: Recommended Search Order for Flutter

```bash
# 1. Get Flutter-specific best practices
python3 {SKILL_PATH}/scripts/search.py "bloc state widget" --platform flutter -n 5

# 2. Get architecture guidance
python3 {SKILL_PATH}/scripts/search.py "bloc clean architecture flutter" --domain architecture

# 3. Get Flutter libraries
python3 {SKILL_PATH}/scripts/search.py "networking image state" --domain library --filter-platform flutter

# 4. Check anti-patterns to avoid
python3 {SKILL_PATH}/scripts/search.py "flutter widget setState" --domain antipattern --filter-platform flutter

# 5. Check performance rules
python3 {SKILL_PATH}/scripts/search.py "flutter widget rebuild list" --domain performance --filter-platform flutter

# 6. Check security
python3 {SKILL_PATH}/scripts/search.py "flutter storage encryption api" --domain security --filter-platform flutter
```

---

## Search Reference

### Available Domains (11 total)

| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `reasoning` | Product type recommendations | e-commerce, banking, social media, healthcare |
| `architecture` | Architecture patterns | bloc, clean architecture, riverpod, provider |
| `library` | Libraries & dependencies | dio, riverpod, go_router, drift, hive, freezed |
| `ui` | UI patterns & components | bottom navigation, list, sheet, sliver, drawer |
| `antipattern` | Common mistakes | setState, build method, no dispose, no const |
| `performance` | Performance optimization | widget rebuild, list, image, shader, startup |
| `security` | Security best practices | flutter_secure_storage, encryption, ssl pinning |
| `testing` | Testing patterns | bloc_test, widget test, integration test, mockito |
| `template` | Project templates/starters | e-commerce flutter, delivery flutter |
| `snippet` | Code templates | (cross-platform patterns available) |
| `gradle` | Gradle dependencies | (Android-specific, use for Android module config) |

### Flags

| Flag | Description | Example |
|------|-------------|---------|
| `--platform` / `-p` | Platform guidelines | `--platform flutter` |
| `--stack` / `-s` | Stack-specific search | `--stack bloc` or `--stack riverpod` |
| `--domain` / `-d` | Search a specific domain | `--domain architecture` |
| `--filter-platform` / `-fp` | Filter results by platform | `--domain library --filter-platform flutter` |
| `--max-results` / `-n` | Number of results (default: 3) | `-n 5` |
| `--json` | Output as JSON | `--json` |

---

## Example Workflows

### New Feature: "Add a product list screen"

```bash
python3 {SKILL_PATH}/scripts/search.py "list widget bloc state" --platform flutter -n 5
python3 {SKILL_PATH}/scripts/search.py "list card image" --domain ui --filter-platform flutter
python3 {SKILL_PATH}/scripts/search.py "dio cached_network_image" --domain library --filter-platform flutter
python3 {SKILL_PATH}/scripts/search.py "flutter list rebuild" --domain performance --filter-platform flutter
```

### New Project: "Build an e-commerce app"

```bash
python3 {SKILL_PATH}/scripts/search.py "e-commerce" --domain reasoning
python3 {SKILL_PATH}/scripts/search.py "bloc clean architecture flutter" --domain architecture
python3 {SKILL_PATH}/scripts/search.py "dio go_router drift riverpod" --domain library --filter-platform flutter
python3 {SKILL_PATH}/scripts/search.py "flutter widget setState" --domain antipattern --filter-platform flutter
python3 {SKILL_PATH}/scripts/search.py "flutter startup image list" --domain performance --filter-platform flutter
python3 {SKILL_PATH}/scripts/search.py "flutter encryption storage" --domain security --filter-platform flutter
```

### Code Review: "Review my Flutter code"

```bash
python3 {SKILL_PATH}/scripts/search.py "flutter setState dispose const" --domain antipattern --filter-platform flutter -n 5
python3 {SKILL_PATH}/scripts/search.py "widget state lifecycle" --platform flutter -n 5
python3 {SKILL_PATH}/scripts/search.py "flutter rebuild image memory" --domain performance --filter-platform flutter
python3 {SKILL_PATH}/scripts/search.py "flutter storage encryption key" --domain security --filter-platform flutter
```

---

## Code Generation & Quality

Before generating code, read the [code generation rules](references/CODE-RULES.md) for platform-specific conventions, required patterns, and anti-patterns to avoid.

Before delivering code, verify against the [pre-delivery checklist](references/CHECKLIST.md) covering architecture, widgets, performance, security, testing, and accessibility.
