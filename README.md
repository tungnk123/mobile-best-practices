# Mobile Best Practices

Searchable database of **1,896 mobile development best practices** packaged as an AI skill for Claude Code and 14 other AI coding assistants. Covers Android, iOS, Flutter, and React Native.

Your AI assistant becomes a mobile development expert — it automatically searches architecture patterns, security rules, performance tips, anti-patterns, and code snippets while helping you build, review, and fix mobile apps.

## What's Inside

| Category | Entries | What You Get |
|---|---|---|
| Architecture Patterns | 49 | MVVM, MVI, Clean Architecture, VIPER, TCA, BLoC, Redux, KMP |
| UI Patterns | 91 | Navigation, lists, sheets, inputs, modals, animations, onboarding |
| Anti-Patterns | 113 | God Activity, memory leaks, prop drilling, setState abuse |
| Libraries | 101 | Retrofit, Hilt, Coil, Kingfisher, Dio, BLoC, Redux, Crashlytics |
| Performance | 228 | Startup, rendering, memory, network, Compose, CI/CD, monitoring |
| Security | 437 | Encryption, keychain, SSL pinning, biometric, compliance, privacy |
| Testing | 73 | Unit, UI, integration, E2E, screenshot, contract, fuzz testing |
| Reasoning Rules | 56 | Smart recommendations based on your product type |
| Project Templates | 18 | Starter configs for common app types |
| Code Snippets | 79 | Copy-paste templates for Android, iOS, Flutter, React Native |
| Gradle Dependencies | 78 | Ready-to-paste dependency declarations and plugins |
| Platform Guidelines | 573 | Android (404), iOS (60), Flutter (54), React Native (55) |

Every entry includes a **Reference URL** linking to official docs, GitHub repos, or guides.

---

## Installation

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

After installation, your AI assistant gains access to 1,896 best practices through a built-in search engine. **You don't need to learn any commands** — just chat naturally and your AI assistant searches the right databases automatically.

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

The skill organizes knowledge into 11 searchable domains:

| Domain | Entries | Use For |
|---|---|---|
| `architecture` | 49 | Choosing patterns (MVVM, MVI, Clean, VIPER, BLoC) |
| `ui` | 91 | UI components, navigation, lists, inputs, animations |
| `antipattern` | 113 | Common mistakes to avoid |
| `library` | 101 | Libraries and dependencies |
| `performance` | 228 | Speed, memory, battery, rendering optimization |
| `security` | 437 | Encryption, auth, storage, compliance |
| `testing` | 73 | Unit, UI, integration, E2E testing |
| `reasoning` | 56 | Smart recommendations by product type |
| `template` | 18 | Project starter configurations |
| `snippet` | 79 | Copy-paste code templates |
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
| `--filter-platform` / `-fp` | Filter any domain results by platform |
| `--persist` | Save results as architecture blueprint markdown |
| `--max-results` / `-n` | Number of results (default: 3) |
| `--json` | Output as JSON |

---

## Project Structure

```
src/mobile-best-practices/          # Source of truth
├── SKILL.md                       # Skill metadata + instructions
├── data/                          # 15 CSV databases
│   ├── architectures.csv
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
