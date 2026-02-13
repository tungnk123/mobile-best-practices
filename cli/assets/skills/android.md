---
name: mobile-best-practices
description: "Android development intelligence with Jetpack Compose. 1,738 searchable entries including 79 code snippets, 78 Gradle declarations, 246 Android-specific guidelines. Default stack: MVVM + Hilt + Room + Retrofit + Coil + Navigation Compose + Material3. Use when building, reviewing, fixing, or optimizing Android apps. Covers architecture patterns, UI components, anti-patterns, performance, security, and testing."
license: MIT
compatibility: Requires Python 3.x for BM25 search. Works with Claude Code and other skills-compatible agents.
metadata:
  author: tungnk123
  version: "1.0"
---

# Android Best Practices - Jetpack Compose Development Intelligence

Searchable database of **1,738 mobile best practices**, **optimized for Android with Jetpack Compose**. All searches default to Android platform. Includes copy-paste code snippets and ready-to-use Gradle dependency declarations.

## Prerequisites

```bash
python3 --version || python --version
```

If not installed: `brew install python3` (macOS) | `sudo apt install python3` (Linux) | `winget install Python.Python.3.12` (Windows)

---

## How to Use This Skill

When user requests Android development work (build, create, architect, review, fix, optimize), follow this workflow:

### Step 1: Extract Requirements

No need to detect platform - **always Android with Jetpack Compose**. Extract:
- **Product type**: E-commerce, Banking, Social Media, Healthcare, Delivery, Fitness, Education, Chat
- **Scope**: New project, new feature, code review, refactor, fix bug, optimize

### Step 2: Search the Database

Use `search.py` with `--platform android` or `--stack compose` for focused results.

```bash
# Android platform guidelines (ALWAYS search this first)
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --platform android -n 5

# Code snippets (copy-paste Kotlin/Compose templates)
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain snippet -n 3

# Gradle dependencies (ready-to-paste declarations)
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain gradle -n 5

# Architecture patterns
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain architecture

# Anti-patterns filtered for Android
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain antipattern --filter-platform android

# Performance rules filtered for Android
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain performance --filter-platform android

# Stack-specific search
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --stack compose
```

### Step 3: Recommended Search Order for Android

```bash
# 1. Get code snippet for what you're building
python3 {SKILL_PATH}/scripts/search.py "viewmodel repository" --domain snippet -n 3

# 2. Get Gradle dependencies needed
python3 {SKILL_PATH}/scripts/search.py "hilt room retrofit" --domain gradle -n 5

# 3. Get Android-specific best practices
python3 {SKILL_PATH}/scripts/search.py "compose state hilt" --platform android -n 5

# 4. Check anti-patterns to avoid
python3 {SKILL_PATH}/scripts/search.py "android compose" --domain antipattern --filter-platform android

# 5. Get architecture guidance
python3 {SKILL_PATH}/scripts/search.py "mvvm clean architecture" --domain architecture

# 6. Check performance rules
python3 {SKILL_PATH}/scripts/search.py "compose recomposition lazy" --domain performance --filter-platform android
```

### Step 4: Generate Code

Use snippet results as starting templates. Customize for user's needs. Follow the code generation rules below.

---

## Search Reference

### Available Domains (11 total)

| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `snippet` | **Copy-paste Kotlin/Compose templates** | viewmodel, repository, room setup, hilt module, compose screen, navigation, paging, datastore |
| `gradle` | **Ready-to-paste Gradle dependencies** | compose bom, hilt, room, retrofit, coil, navigation, testing, paging |
| `reasoning` | Product type recommendations | e-commerce, banking, social media, healthcare, delivery |
| `architecture` | Architecture patterns | mvvm, clean architecture, mvi |
| `library` | Libraries & dependencies | retrofit, hilt, coil, room, okhttp, moshi |
| `ui` | UI patterns & components | bottom navigation, list, bottom sheet, pull refresh |
| `antipattern` | Common mistakes | god activity, memory leak, recomposition |
| `performance` | Performance optimization | startup, recomposition, memory, battery, image |
| `security` | Security best practices | encryption, keystore, ssl pinning, biometric |
| `testing` | Testing patterns | unit test, compose test, mockk, turbine |
| `template` | Project templates/starters | e-commerce android, banking android |

### Flags

| Flag | Description | Example |
|------|-------------|---------|
| `--domain` / `-d` | Search a specific domain | `--domain snippet` |
| `--platform` / `-p` | Platform guidelines | `--platform android` |
| `--filter-platform` / `-fp` | Filter results by platform | `--domain library --filter-platform android` |
| `--stack` / `-s` | Stack-specific search | `--stack compose` |
| `--max-results` / `-n` | Number of results (default: 3) | `-n 5` |
| `--json` | Output as JSON | `--json` |

---

## Example Workflows

### New Feature: "Add a product list screen"

```bash
python3 {SKILL_PATH}/scripts/search.py "viewmodel compose screen" --domain snippet -n 3
python3 {SKILL_PATH}/scripts/search.py "coil paging compose" --domain gradle -n 5
python3 {SKILL_PATH}/scripts/search.py "lazy list image performance" --platform android -n 3
python3 {SKILL_PATH}/scripts/search.py "product list card" --domain ui --filter-platform android
```

### New Project: "Build an e-commerce app"

```bash
python3 {SKILL_PATH}/scripts/search.py "e-commerce" --domain reasoning
python3 {SKILL_PATH}/scripts/search.py "mvvm clean architecture android" --domain architecture
python3 {SKILL_PATH}/scripts/search.py "viewmodel repository hilt" --domain snippet -n 5
python3 {SKILL_PATH}/scripts/search.py "room navigation theme" --domain snippet -n 5
python3 {SKILL_PATH}/scripts/search.py "compose hilt room retrofit" --domain gradle -n 10
python3 {SKILL_PATH}/scripts/search.py "android architecture" --domain antipattern --filter-platform android
python3 {SKILL_PATH}/scripts/search.py "compose startup image" --domain performance --filter-platform android
```

### Code Review: "Review my Android code"

```bash
python3 {SKILL_PATH}/scripts/search.py "android compose viewmodel" --domain antipattern -n 5
python3 {SKILL_PATH}/scripts/search.py "state recomposition lifecycle" --platform android -n 5
python3 {SKILL_PATH}/scripts/search.py "compose lazy image startup" --domain performance --filter-platform android
python3 {SKILL_PATH}/scripts/search.py "android storage encryption api key" --domain security --filter-platform android
```

### Gradle Setup: "What dependencies do I need?"

```bash
python3 {SKILL_PATH}/scripts/search.py "compose material3 bom" --domain gradle -n 5
python3 {SKILL_PATH}/scripts/search.py "hilt room retrofit" --domain gradle -n 5
python3 {SKILL_PATH}/scripts/search.py "navigation coil paging" --domain gradle -n 5
python3 {SKILL_PATH}/scripts/search.py "testing junit mockk turbine" --domain gradle -n 5
```

---

## Code Generation & Quality

Before generating code, read the [code generation rules](references/CODE-RULES.md) for Android-specific conventions, required patterns (sealed UiState, @HiltViewModel, collectAsStateWithLifecycle), and anti-patterns to avoid.

Before delivering code, verify against the [pre-delivery checklist](references/CHECKLIST.md) covering architecture, Compose, Gradle, performance, security, testing, and accessibility.
