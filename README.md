# Mobile Best Practices

[![npm version](https://img.shields.io/npm/v/mobile-best-practices?color=blue)](https://www.npmjs.com/package/mobile-best-practices)
[![npm downloads](https://img.shields.io/npm/dm/mobile-best-practices)](https://www.npmjs.com/package/mobile-best-practices)
[![Python](https://img.shields.io/badge/python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Entries](https://img.shields.io/badge/entries-2%2C461-orange)](src/mobile-best-practices/data/)
[![Platforms](https://img.shields.io/badge/platforms-Android%20%7C%20iOS%20%7C%20Flutter%20%7C%20RN-blueviolet)](README.md)

Searchable database of **2,461 mobile development best practices** packaged as an AI skill for Claude Code and 14 other AI coding assistants. Covers Android, iOS, Flutter, and React Native.

Your AI assistant becomes a mobile development expert — it automatically searches architecture patterns, security rules, performance tips, anti-patterns, and code snippets while helping you build, review, and fix mobile apps.

**[Live Demo →](DEMO.md)** | **[Changelog →](CHANGELOG.md)** | **[Contributing →](CONTRIBUTING.md)**

## What's Inside

| Category | Entries | What You Get |
|---|---|---|
| Architecture Patterns | 49 | MVVM, MVI, Clean Architecture, VIPER, TCA, BLoC, Redux, KMP |
| Design Patterns | 112 | Repository, Factory, Observer, Strategy, Adapter, code smells |
| UI Patterns | 191 | Navigation, lists, sheets, inputs, modals, animations, onboarding |
| Anti-Patterns | 243 | God Activity, memory leaks, prop drilling, setState abuse |
| Libraries | 103 | Retrofit, Hilt, Coil, Kingfisher, Dio, BLoC, Redux, Apollo, Koin |
| Performance | 228 | Startup, rendering, memory, network, Compose, CI/CD, monitoring |
| Security | 437 | Encryption, keychain, SSL pinning, biometric, compliance, privacy |
| Testing | 73 | Unit, UI, integration, E2E, screenshot, contract, fuzz testing |
| Reasoning Rules | 56 | Smart recommendations based on your product type |
| Project Templates | 18 | Starter configs for common app types |
| Code Snippets | 81 | Copy-paste templates for Android, iOS, Flutter, React Native |
| Gradle Dependencies | 78 | Ready-to-paste dependency declarations and plugins |
| Platform Guidelines | 792 | Android (623), iOS (60), Flutter (54), React Native (55) |

Every entry includes a **Reference URL** linking to official docs, GitHub repos, or guides.

---

## Why BM25 Search Instead of a Markdown File?

Most "best practices" repos give you a giant markdown file and tell you to paste it into your AI's context or system prompt. This project does something different — and the difference matters at 2,461 entries.

### The problem with a static markdown file

| Problem | Impact |
|---|---|
| **Entire file loaded every request** | 2,461 entries ≈ 150,000+ tokens consumed whether relevant or not |
| **Context window bloat** | Less room for your actual code, leaving the AI with less to work with |
| **No ranking** | AI sees everything with equal weight — a Compose tip buried 300 lines down gets the same attention as the first line |
| **Stale retrieval** | AI "remembers" patterns from a big blob of text rather than precisely fetching what fits your query |
| **Hard to scale** | Every new entry makes the problem worse |

### How BM25 search fixes this

BM25 (Best Match 25) is the same ranking algorithm used by search engines like Elasticsearch and Lucene. Instead of loading the whole database, it scores every entry against your query and returns only the top matches — ranked by relevance.

```
Query: "compose state management viewmodel"

BM25 scores every entry → returns top 15 ranked results
→ AI sees ~2,000 tokens of highly relevant content
→ vs 150,000+ tokens if the whole database were loaded
```

**Result:** The AI gets precise, high-signal context instead of a firehose — and generates better code because of it.

### Fuzzy search on top of BM25

Typos and abbreviations break exact keyword search. The `--fuzzy` flag adds character bigram similarity (Dice coefficient) to catch near-matches:

```bash
# Exact match fails:  "recompostion" → 0 results
# Fuzzy match works:  "recompostion" → finds "recomposition" entries ✓

# Exact match fails:  "LazyColum" → 0 results
# Fuzzy match works:  "LazyColum" → finds "LazyColumn" entries ✓
```

Bigram expansion runs before BM25 scoring, so results are still ranked by relevance — not just "close enough to match."

### Cross-domain search (`--all-domains`)

A single query like `"login screen banking"` spans multiple domains at once — security rules, architecture patterns, UI components, anti-patterns, code snippets. The `--all-domains` flag runs BM25 across all 12 domains in parallel and merges results by normalised score, so the most relevant entries float to the top regardless of which domain they live in.

### Summary

| Approach | Tokens used | Relevance | Scales with more entries |
|---|---|---|---|
| Static markdown file | All 150,000+ | Low — everything equally weighted | Gets worse |
| BM25 search (this project) | ~2,000 (top results) | High — ranked by query match | Stays fast |
| BM25 + fuzzy + cross-domain | ~2,000–6,000 | Highest — typo-tolerant, multi-domain | Stays fast |

---

## Installation

### Install in OpenAI Codex (Skill Creator)

1. Open **Codex** → **Skills** → click the **Skill Creator** bar at the bottom:

   ![Skill Creator bar](docs/codex/skill-creator-bar.png)

2. Paste the URL and press Enter:

   ```
   https://github.com/tungnk123/mobile-best-practices
   ```

   ![Skill Creator URL input](docs/codex/skill-creator-url.png)

3. **Mobile Best Practices** appears under **Installed** with a toggle to enable it:

   ![Codex skill installed](docs/codex/skill-installed.png)

4. Start chatting — Codex now searches 2,461 mobile best practices in real time.

---

### Quick Install (Recommended)

```bash
cd /path/to/your/mobile/project
npx mobile-best-practices init
```

This launches an interactive prompt — pick your AI assistant and mobile platform, and the skill files are installed into your project.

**Note**: The installer automatically updates your `.gitignore` to exclude AI assistant directories (`.claude/`, `.cursor/`, etc.), so skill files won't appear in git changes.

### One-liner Install

```bash
# Android + Claude Code
npx mobile-best-practices init --ai claude --platform android

# iOS + Cursor
npx mobile-best-practices init --ai cursor --platform ios

# Flutter + Windsurf
npx mobile-best-practices init --ai windsurf --platform flutter

# React Native + GitHub Copilot
npx mobile-best-practices init --ai copilot --platform react-native

# All platforms + All AI assistants
npx mobile-best-practices init --ai all --platform all
```

### Supported AI Assistants

Claude Code, Cursor, Windsurf, GitHub Copilot, Kiro, Codex CLI, Gemini CLI, Roo Code, Continue, OpenCode, Qoder, CodeBuddy, Trae, Antigravity

### Supported Mobile Platforms

| Platform | Default Stack |
|---|---|
| **Android** | Jetpack Compose + Hilt + Room + Retrofit + Coil + Navigation Compose |
| **iOS** | SwiftUI + Combine/async-await + SwiftData + URLSession + Kingfisher |
| **Flutter** | BLoC/Riverpod + Dio + Drift/Hive + GoRouter + CachedNetworkImage |
| **React Native** | Redux Toolkit/Zustand + Axios + MMKV + React Navigation + FastImage |

### Update to Latest Version

```bash
npx mobile-best-practices update
```

### Manual Install (Claude Code only)

Copy the `.claude/skills/mobile-best-practices/` directory into your project. Ensure Python 3 is available.

---

## How It Works

After installation, your AI assistant gains access to 2,461 best practices through a built-in search engine. **You don't need to learn any commands** — just chat naturally and your AI assistant searches the right databases automatically.

```
You: "Build a login screen for my banking app"

AI assistant automatically:
  1. Searches architecture patterns → recommends MVVM + Clean Architecture
  2. Searches security practices → encryption, biometric auth, SSL pinning
  3. Searches code snippets → ViewModel, Repository, Compose screen templates
  4. Searches anti-patterns → warns about common banking app mistakes
  5. Generates production-ready code following all best practices
```

### Slash Commands (Claude Code & Cursor)

Claude Code and Cursor users can also invoke the skill using slash commands:

- **`/mobile-best-practices`** - Invokes the main skill
- **`/mobile-security-audit`** - Runs a comprehensive security audit
- **`/mobile-performance-check`** - Analyzes performance issues
- **`/mobile-anr-crash-check`** - Checks for ANR, crashes, and splash screen issues
- **`/mobile-setup-android`** - Sets up a new Android project with best practices

Just type `/` in your AI assistant to see all available commands!

---

## Use Cases & Examples

### "Review my project for security issues"

Ask your AI assistant to audit your codebase against 437 security best practices:

```
"Check my Android project for security vulnerabilities"
"Audit my iOS app for data privacy issues"
"Review my Flutter app for OWASP mobile top 10"
"Are there any hardcoded API keys or secrets in my project?"
```

The AI will scan your code and cross-reference it against security rules covering:
- Hardcoded secrets and API keys
- Insecure data storage (SharedPreferences, UserDefaults)
- Missing SSL/certificate pinning
- Improper encryption usage
- Insecure authentication flows
- Missing root/jailbreak detection
- Sensitive data in logs or crash reports

### "Check my project for performance issues"

Get your app reviewed against 228 performance optimization rules:

```
"Find performance issues in my Android app"
"Why is my app startup slow?"
"Review my Compose code for unnecessary recompositions"
"Check my RecyclerView/LazyColumn for performance problems"
"Audit my app's memory usage patterns"
```

Catches issues like:
- Unnecessary recompositions in Jetpack Compose
- Missing image caching and downsizing
- Blocking the main thread with I/O operations
- Inefficient list rendering (LazyColumn, FlatList, ListView)
- Memory leaks from lifecycle-unaware observers
- Missing R8/ProGuard configuration
- Unoptimized app startup (cold start, splash screen)

### "Check for ANR, crashes, or slow startup"

Diagnose freezing, crashing, or slow splash screen issues against performance and anti-pattern rules:

```
"My app shows ANR dialogs — what's blocking the main thread?"
"My app crashes on startup — check for common causes"
"My splash screen takes too long to dismiss"
"Check my coroutine usage for threading issues"
"Why does my app crash after coming back from background?"
```

Covers:
- Main thread I/O and blocking calls causing ANR
- Coroutine dispatcher misuse (IO on Main)
- Null pointer and lifecycle-related crashes
- Splash screen cold start optimization (SplashScreen API, Baseline Profiles)
- Memory leaks leading to OOM crashes
- Context leaks and lifecycle-unaware components

### "Check accessibility in my app"

Validate your app against accessibility guidelines:

```
"Review my app for accessibility issues"
"Does my Compose UI follow accessibility best practices?"
"Check if my app works with screen readers"
"Audit content descriptions and touch targets"
```

### "Review my entire project"

Run a comprehensive audit across all domains:

```
"Do a full code review of my Android project"
"Audit my iOS app — architecture, security, performance, everything"
"Review my Flutter project and suggest improvements"
```

The AI reviews your project against:
- Architecture patterns — is the structure maintainable?
- Anti-patterns — any God Activities, memory leaks, tight coupling?
- Security — any vulnerabilities or data leaks?
- Performance — any slow paths or wasted resources?
- Testing — adequate test coverage?
- Platform guidelines — following platform conventions?

### "Build a new feature"

Get production-ready code with best practices baked in:

```
"Build a product list screen with search and filtering"
"Add biometric authentication to my app"
"Create an offline-first data sync feature"
"Implement pull-to-refresh with pagination"
"Add a bottom navigation with 4 tabs"
```

### "Set up a new project"

Start with the right architecture from day one:

```
"Set up a new Android e-commerce app with Clean Architecture"
"Create a new iOS banking app — what architecture should I use?"
"Start a Flutter delivery app with BLoC pattern"
"What dependencies do I need for a React Native social media app?"
```

### "Fix a bug"

Get fixes that follow best practices:

```
"My ViewModel survives configuration changes but leaks the Activity"
"State is lost when navigating back in Compose"
"My app crashes on Android 14 — photo picker permissions"
"Room database migration is failing"
```

### "Help with Gradle setup"

Get exact dependency declarations:

```
"What Gradle dependencies do I need for Compose + Hilt + Room?"
"Set up my version catalog with latest stable versions"
"Add testing dependencies — JUnit, Mockk, Turbine"
"Configure code quality tools — Detekt, Ktlint, Spotless"
```

---

## Search Domains

The skill organizes knowledge into 12 searchable domains:

| Domain | Entries | Use For |
|---|---|---|
| `architecture` | 49 | Choosing patterns (MVVM, MVI, Clean, VIPER, BLoC) |
| `designpattern` | 112 | Design patterns & code smell detection |
| `ui` | 191 | UI components, navigation, lists, inputs, animations |
| `antipattern` | 243 | Common mistakes to avoid |
| `library` | 103 | Libraries and dependencies |
| `performance` | 228 | Speed, memory, battery, rendering optimization |
| `security` | 437 | Encryption, auth, storage, compliance |
| `testing` | 73 | Unit, UI, integration, E2E testing |
| `reasoning` | 56 | Smart recommendations by product type |
| `template` | 18 | Project starter configurations |
| `snippet` | 81 | Copy-paste code templates |
| `gradle` | 78 | Gradle dependency declarations |

---

## Advanced: Manual Search

You can also run searches directly from the terminal:

```bash
# Search by domain
python3 scripts/search.py "mvvm clean architecture" --domain architecture

# Search platform guidelines
python3 scripts/search.py "compose state management" --platform android

# Search by tech stack
python3 scripts/search.py "navigation" --stack swiftui

# Get code snippets
python3 scripts/search.py "viewmodel hilt" --domain snippet

# Get Gradle dependencies
python3 scripts/search.py "compose room retrofit" --domain gradle

# Generate architecture blueprint
python3 scripts/search.py "e-commerce android" --persist --project-name MyApp

# Output as JSON
python3 scripts/search.py "security encryption" --domain security --json

# Get more results
python3 scripts/search.py "compose performance" --domain performance -n 10
```

### Search Flags

| Flag | Description |
|---|---|
| `--domain` / `-d` | Search a specific domain |
| `--platform` / `-p` | Platform guidelines (android, ios, flutter, react-native) |
| `--stack` / `-s` | Filter by tech stack (compose, swiftui, flutter, react-native) |
| `--filter-platform` / `-fp` | Filter any domain/cross-domain results by platform |
| `--all-domains` / `-a` | Search across all domains at once, ranked by normalised BM25 score |
| `--fuzzy` / `-f` | Enable typo-tolerant search via character bigram expansion |
| `--max-results` / `-n` | Number of results (default: 15 per-domain, 30 for `--all-domains`) |
| `--compact` / `-c` | Token-optimized compact output |
| `--comment-style` / `-cs` | Code comment verbosity: `all` (default), `none`, or `important` |
| `--persist` | Save results as architecture blueprint markdown |
| `--page` | Generate a page-specific blueprint override |
| `--json` | Output as JSON |

---

## Project Structure

```
src/mobile-best-practices/          # Source of truth
├── SKILL.md                       # Skill metadata + instructions
├── data/                          # 16 CSV databases
│   ├── architectures.csv
│   ├── design-patterns.csv
│   ├── libraries.csv
│   ├── ui-patterns.csv
│   ├── anti-patterns.csv
│   ├── performance.csv
│   ├── security.csv
│   ├── testing.csv
│   ├── reasoning-rules.csv
│   ├── project-templates.csv
│   ├── code-snippets.csv
│   ├── gradle-deps.csv
│   └── platforms/
│       ├── android.csv
│       ├── ios.csv
│       ├── flutter.csv
│       └── react-native.csv
├── scripts/
│   ├── core.py                    # BM25 search engine
│   └── search.py                  # CLI interface
├── references/
│   ├── CODE-RULES.md              # Code generation rules
│   └── CHECKLIST.md               # Pre-delivery quality checklist
└── templates/
    ├── base/                      # Shared SKILL.md content
    └── platforms/                 # 15 AI platform configs

cli/                               # npm package (mobile-best-practices)
├── src/                           # TypeScript source
├── assets/                        # Bundled data for offline install
└── package.json
```

## Requirements

- Python 3.x (no external dependencies)
- Node.js 18+ (CLI installer only)

## Contributing

1. **Data changes** — Edit CSVs in `src/mobile-best-practices/data/`. Changes auto-propagate via symlinks.
2. **Search engine** — Edit `src/mobile-best-practices/scripts/core.py`.
3. **CLI** — Edit `cli/src/`, build with `npm run build` in `cli/`.
4. **Sync CLI assets** before publishing:
   ```bash
   cp -r src/mobile-best-practices/data/* cli/assets/data/
   cp -r src/mobile-best-practices/scripts/* cli/assets/scripts/
   cp -r src/mobile-best-practices/references/* cli/assets/references/
   cp -r src/mobile-best-practices/templates/* cli/assets/templates/
   ```

## License

MIT
