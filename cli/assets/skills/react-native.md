---
name: mobile-best-practices
description: "React Native development intelligence with TypeScript. 1,738 searchable entries including 55 React Native-specific guidelines. Default stack: Redux Toolkit/Zustand + Axios + React Navigation + MMKV + FastImage + React Native Reanimated. Use when building, reviewing, fixing, or optimizing React Native apps. Covers architecture patterns, UI components, anti-patterns, performance, security, and testing."
license: MIT
compatibility: Requires Python 3.x for BM25 search. Works with Claude Code and other skills-compatible agents.
metadata:
  author: tungnk123
  version: "1.0"
---

# React Native Best Practices - TypeScript Development Intelligence

Searchable database of **1,738 mobile best practices**, **optimized for React Native with TypeScript**. All searches default to React Native platform. Covers architecture, hooks, navigation, performance, and testing for cross-platform RN apps.

## Prerequisites

```bash
python3 --version || python --version
```

If not installed: `brew install python3` (macOS) | `sudo apt install python3` (Linux) | `winget install Python.Python.3.12` (Windows)

---

## How to Use This Skill

When user requests React Native development work (build, create, architect, review, fix, optimize), follow this workflow:

### Step 1: Extract Requirements

No need to detect platform - **always React Native with TypeScript**. Extract:
- **Product type**: E-commerce, Banking, Social Media, Healthcare, Delivery, Fitness, Education, Chat
- **State management**: Redux Toolkit (default), Zustand, MobX
- **Scope**: New project, new feature, code review, refactor, fix bug, optimize

### Step 2: Search the Database

Use `search.py` with `--platform react-native` or `--stack react-native` for focused results.

```bash
# React Native platform guidelines (ALWAYS search this first)
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --platform react-native -n 5

# Stack-specific search
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --stack react-native
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --stack hooks
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --stack redux

# Architecture patterns
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain architecture

# Anti-patterns filtered for React Native
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain antipattern --filter-platform react-native

# Performance rules filtered for React Native
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain performance --filter-platform react-native

# Libraries for React Native
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain library --filter-platform react-native
```

### Step 3: Recommended Search Order for React Native

```bash
# 1. Get React Native-specific best practices
python3 {SKILL_PATH}/scripts/search.py "hooks navigation state" --platform react-native -n 5

# 2. Get architecture guidance
python3 {SKILL_PATH}/scripts/search.py "redux clean architecture react native" --domain architecture

# 3. Get React Native libraries
python3 {SKILL_PATH}/scripts/search.py "navigation state image" --domain library --filter-platform react-native

# 4. Check anti-patterns to avoid
python3 {SKILL_PATH}/scripts/search.py "react native hooks effect" --domain antipattern --filter-platform react-native

# 5. Check performance rules
python3 {SKILL_PATH}/scripts/search.py "flatlist image bridge" --domain performance --filter-platform react-native

# 6. Check security
python3 {SKILL_PATH}/scripts/search.py "react native storage encryption" --domain security --filter-platform react-native
```

---

## Search Reference

### Available Domains (11 total)

| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `reasoning` | Product type recommendations | e-commerce, banking, social media, healthcare |
| `architecture` | Architecture patterns | redux, clean architecture, feature-sliced, zustand |
| `library` | Libraries & dependencies | react-navigation, zustand, mmkv, flashlist, axios |
| `ui` | UI patterns & components | bottom tab, list, sheet, drawer, modal |
| `antipattern` | Common mistakes | prop drilling, useEffect, inline styles, ScrollView |
| `performance` | Performance optimization | FlatList, bridge, image, bundle, hermes |
| `security` | Security best practices | mmkv, encryption, ssl pinning, keychain |
| `testing` | Testing patterns | jest, react-native-testing-library, detox, e2e |
| `template` | Project templates/starters | e-commerce react-native, social react-native |
| `snippet` | Code templates | (cross-platform patterns available) |
| `gradle` | Gradle dependencies | (useful for Android module in RN project) |

### Flags

| Flag | Description | Example |
|------|-------------|---------|
| `--platform` / `-p` | Platform guidelines | `--platform react-native` |
| `--stack` / `-s` | Stack-specific search | `--stack react-native` or `--stack hooks` |
| `--domain` / `-d` | Search a specific domain | `--domain architecture` |
| `--filter-platform` / `-fp` | Filter results by platform | `--domain library --filter-platform react-native` |
| `--max-results` / `-n` | Number of results (default: 3) | `-n 5` |
| `--json` | Output as JSON | `--json` |

---

## Example Workflows

### New Feature: "Add a product list screen"

```bash
python3 {SKILL_PATH}/scripts/search.py "list flatlist hooks state" --platform react-native -n 5
python3 {SKILL_PATH}/scripts/search.py "list card image" --domain ui --filter-platform react-native
python3 {SKILL_PATH}/scripts/search.py "axios flashlist mmkv" --domain library --filter-platform react-native
python3 {SKILL_PATH}/scripts/search.py "flatlist image render" --domain performance --filter-platform react-native
```

### New Project: "Build an e-commerce app"

```bash
python3 {SKILL_PATH}/scripts/search.py "e-commerce" --domain reasoning
python3 {SKILL_PATH}/scripts/search.py "redux clean architecture react native" --domain architecture
python3 {SKILL_PATH}/scripts/search.py "navigation zustand axios mmkv" --domain library --filter-platform react-native
python3 {SKILL_PATH}/scripts/search.py "react native hooks prop drilling" --domain antipattern --filter-platform react-native
python3 {SKILL_PATH}/scripts/search.py "flatlist startup image bundle" --domain performance --filter-platform react-native
python3 {SKILL_PATH}/scripts/search.py "react native storage ssl encryption" --domain security --filter-platform react-native
```

### Code Review: "Review my React Native code"

```bash
python3 {SKILL_PATH}/scripts/search.py "react native hooks effect prop" --domain antipattern --filter-platform react-native -n 5
python3 {SKILL_PATH}/scripts/search.py "hooks navigation state" --platform react-native -n 5
python3 {SKILL_PATH}/scripts/search.py "flatlist image memory bridge" --domain performance --filter-platform react-native
python3 {SKILL_PATH}/scripts/search.py "react native storage encryption api key" --domain security --filter-platform react-native
```

---

## Code Generation & Quality

Before generating code, read the [code generation rules](references/CODE-RULES.md) for platform-specific conventions, required patterns, and anti-patterns to avoid.

Before delivering code, verify against the [pre-delivery checklist](references/CHECKLIST.md) covering architecture, components, performance, security, testing, and accessibility.
