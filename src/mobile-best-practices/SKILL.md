---
name: mobile-best-practices
description: "Mobile development intelligence for Android, iOS, Flutter, and React Native. 1,738 searchable entries: 49 architecture patterns, 91 UI patterns, 113 anti-patterns, 101 libraries, 228 performance rules, 437 security practices, 73 testing patterns, 56 reasoning rules, 18 project templates, 415 platform-specific guidelines, 79 copy-paste code snippets, and 78 Gradle dependency declarations. Use when building, reviewing, fixing, or optimizing mobile apps. Covers MVVM, MVI, VIPER, TCA, BLoC, Clean Architecture, state management, navigation, DI, networking, database, testing, security, performance, accessibility, Material3, Gradle version catalog."
license: MIT
compatibility: Requires Python 3.x for BM25 search. Works with Claude Code and other skills-compatible agents.
metadata:
  author: tungnk123
  version: "1.0"
---

# Mobile Best Practices - Development Intelligence

Searchable database of **1,738 mobile development best practices** covering architecture patterns, UI components, anti-patterns, libraries, performance rules, security practices, testing patterns, code snippets, Gradle dependencies, and platform-specific guidelines for Android, iOS, Flutter, and React Native.

**Android-first**: Optimized for Android/Jetpack Compose with full copy-paste code snippets and ready-to-use Gradle declarations.

## Prerequisites

Check if Python is installed:

```bash
python3 --version || python --version
```

If Python is not installed, install it based on user's OS:

**macOS:**
```bash
brew install python3
```

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install python3
```

**Windows:**
```powershell
winget install Python.Python.3.12
```

---

## How to Use This Skill

When user requests mobile development work (build, create, architect, review, fix, optimize), follow this workflow:

### Step 1: Detect Platform (Default: Android)

If user doesn't specify a platform, **default to Android with Jetpack Compose**. Extract:
- **Platform**: Android (default), iOS, Flutter, React Native
- **Product type**: E-commerce, Banking, Social Media, Healthcare, Delivery, Fitness, Education, Chat
- **Scope**: New project, new feature, code review, refactor, fix bug, optimize

### Step 2: Search the Database

Use `search.py` to gather comprehensive information. Run multiple searches across domains.

```bash
# Basic domain search
python3 scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]

# Platform-specific guidelines
python3 scripts/search.py "<keyword>" --platform android

# Filter any domain by platform
python3 scripts/search.py "<keyword>" --domain library --filter-platform android

# Get code snippets (Android copy-paste templates)
python3 scripts/search.py "viewmodel hilt" --domain snippet

# Get Gradle dependencies
python3 scripts/search.py "compose room hilt" --domain gradle
```

### Step 3: Android-First Workflow (Recommended Order)

For Android projects, search in this order:

```bash
# 1. Get code snippet for what you're building
python3 scripts/search.py "viewmodel repository" --domain snippet -n 3

# 2. Get Gradle dependencies needed
python3 scripts/search.py "hilt room retrofit" --domain gradle -n 5

# 3. Get Android-specific best practices
python3 scripts/search.py "compose state hilt" --platform android -n 5

# 4. Check anti-patterns to avoid
python3 scripts/search.py "android compose" --domain antipattern

# 5. Get architecture guidance
python3 scripts/search.py "mvvm clean architecture" --domain architecture

# 6. Check performance rules
python3 scripts/search.py "compose recomposition lazy" --domain performance
```

### Step 4: Generate Code

Use snippet results as starting templates. Customize for user's specific needs. Follow the [code generation rules](references/CODE-RULES.md) and verify against the [pre-delivery checklist](references/CHECKLIST.md).

---

## Search Reference

### Available Domains (11 total)

| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `snippet` | **Copy-paste code templates (Android)** | viewmodel, repository, room setup, hilt module, compose screen, navigation, paging, datastore |
| `gradle` | **Ready-to-paste Gradle dependencies** | compose bom, hilt, room, retrofit, coil, navigation, testing, paging |
| `reasoning` | Product type recommendations | e-commerce, banking, social media, healthcare, delivery |
| `architecture` | Architecture patterns | mvvm, clean architecture, bloc, viper, redux, mvi |
| `library` | Libraries & dependencies | retrofit, hilt, coil, kingfisher, dio, bloc, redux |
| `ui` | UI patterns & components | bottom navigation, list, bottom sheet, pull refresh |
| `antipattern` | Common mistakes | god activity, memory leak, prop drilling, setState |
| `performance` | Performance optimization | startup, recomposition, memory, battery, list, image |
| `security` | Security best practices | encryption, keychain, ssl pinning, token, biometric |
| `testing` | Testing patterns | unit test, ui test, bloc test, snapshot, mocking |
| `template` | Project templates/starters | e-commerce android, banking ios, delivery flutter |

### Available Platforms

| Platform | Guidelines | Focus |
|----------|-----------|-------|
| `android` | 246 | Jetpack Compose, Material3, Coroutines, Hilt, Room, Navigation, Gradle |
| `ios` | 60 | SwiftUI, Combine, async/await, Actors, NavigationStack, SwiftData |
| `flutter` | 54 | Widgets, BLoC/Riverpod, Dart 3, GoRouter, Slivers, Freezed |
| `react-native` | 55 | Hooks, React Navigation, Reanimated, FlatList, Zustand, Expo |

### Flags

| Flag | Description | Example |
|------|-------------|---------|
| `--domain` / `-d` | Search a specific domain | `--domain snippet` |
| `--platform` / `-p` | Search platform guidelines | `--platform android` |
| `--filter-platform` / `-fp` | Filter any domain by platform | `--domain library --filter-platform android` |
| `--max-results` / `-n` | Number of results (default: 3) | `-n 5` |
| `--json` | Output as JSON | `--json` |

---

## Example Workflows

### New Android Feature: "Add a product list screen"

```bash
# 1. Get ViewModel + Screen code templates
python3 scripts/search.py "viewmodel compose screen" --domain snippet -n 3

# 2. Get Gradle deps for image loading and paging
python3 scripts/search.py "coil paging compose" --domain gradle -n 5

# 3. Get LazyColumn and image best practices
python3 scripts/search.py "lazy list image performance" --platform android -n 3

# 4. Get UI patterns for product list
python3 scripts/search.py "product list card" --domain ui
```

### New Android Project: "Build an e-commerce app"

```bash
# 1. Get full product-type recommendation
python3 scripts/search.py "e-commerce" --domain reasoning

# 2. Get architecture details
python3 scripts/search.py "mvvm clean architecture android" --domain architecture

# 3. Get ALL code templates
python3 scripts/search.py "viewmodel repository hilt" --domain snippet -n 5
python3 scripts/search.py "room navigation theme" --domain snippet -n 5

# 4. Get ALL Gradle dependencies
python3 scripts/search.py "compose hilt room retrofit" --domain gradle -n 10

# 5. Get anti-patterns and performance
python3 scripts/search.py "android architecture" --domain antipattern
python3 scripts/search.py "compose startup image" --domain performance
```

### Code Review: "Review my Android code"

```bash
# 1. Check for anti-patterns
python3 scripts/search.py "android compose viewmodel" --domain antipattern -n 5

# 2. Check Compose best practices
python3 scripts/search.py "state recomposition lifecycle" --platform android -n 5

# 3. Check performance
python3 scripts/search.py "compose lazy image startup" --domain performance

# 4. Check security
python3 scripts/search.py "android storage encryption api key" --domain security
```

### Gradle Setup: "What dependencies do I need?"

```bash
# Get all core Android dependencies
python3 scripts/search.py "compose material3 bom" --domain gradle -n 5
python3 scripts/search.py "hilt room retrofit" --domain gradle -n 5
python3 scripts/search.py "navigation coil paging" --domain gradle -n 5
python3 scripts/search.py "testing junit mockk turbine" --domain gradle -n 5
```

### Cross-Platform: "Compare architectures for banking iOS app"

```bash
# 1. Get reasoning-based recommendation
python3 scripts/search.py "banking" --domain reasoning

# 2. Compare architectures
python3 scripts/search.py "viper tca mvvm ios" --domain architecture

# 3. Get security for banking
python3 scripts/search.py "banking encryption biometric" --domain security

# 4. iOS-specific practices
python3 scripts/search.py "keychain security architecture" --platform ios
```

---

## Tips for Better Results

1. **Start with snippets** - For Android, search `snippet` domain first for ready-to-use code templates
2. **Get Gradle deps early** - Search `gradle` domain to know exact dependency declarations
3. **Be specific with keywords** - "android mvvm compose hilt" > "architecture"
4. **Search multiple domains** - Snippet + Gradle + Platform + Anti-pattern = Complete picture
5. **Use --filter-platform** - Filter library/antipattern/performance results for your platform
6. **Always check anti-patterns** - Prevent common mistakes before they happen
7. **Check platform guidelines** - Platform-specific practices catch issues generic advice misses
8. **Use -n 5 for more results** - Default is 3, increase for broader coverage

---

## Code Generation & Quality

Before generating code, read the [code generation rules](references/CODE-RULES.md) for platform-specific conventions, required patterns, and anti-patterns to avoid.

Before delivering code, verify against the [pre-delivery checklist](references/CHECKLIST.md) covering architecture, Compose, Gradle, performance, security, testing, and accessibility.
