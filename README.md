# Mobile Best Practices

Your AI assistant just got a mobile development brain upgrade.

**2,042 battle-tested best practices** — architecture, security, performance, anti-patterns, code snippets, and Gradle dependencies — packaged as an AI skill for Claude Code and 14 other AI coding assistants. Android, iOS, Flutter, React Native.

> Install once. Every code review, security audit, and performance check from that point forward pulls from a real database of 2,042 rules — not just your AI's training data.

---

## See It in Action

Here's what `/mobile-performance-check` found in a real Android alarm clock app in **one command**:

![Performance check output — 17 real findings from a real Android app](docs/performance-check-example.png)

| # | File | Severity | Issue | DB Rule |
|---|------|----------|-------|---------|
| 1 | `AppModule.kt` | **Critical** | No WAL mode on Room DB | `database query index room` |
| 2 | `AlarmEventDao / StatisticsRepositoryImpl` | **Critical** | Full table scan + Kotlin-side aggregation | `database query index room` |
| 3 | `app/build.gradle.kts` | **Critical** | No Baseline Profiles | `baseline profile startup trace` |
| 4 | `app/build.gradle.kts` | **Critical** | No LeakCanary | `memory leak allocation heap` |
| 5 | `HomeScreen.kt` | **Critical** | Unstable lambdas → excessive recomposition | `recomposition compose lambda` |
| 6 | `SnoozeManager.kt` | Medium | SharedPreferences blocking I/O | `threading coroutine main dispatcher` |
| 7 | `LocaleManager.kt` | Medium | SharedPreferences blocking I/O | `threading coroutine main dispatcher` |
| 8 | `MusicSelectionScreen.kt:135` | Medium | Missing `key` in LazyColumn items | `list scroll lazy virtualize` |
| 9 | `SnoozeBannerCard.kt:37` | Medium | `SimpleDateFormat` created every recomposition | `recomposition compose lambda` |
| 10 | `HomeViewModel.kt:57` | Medium | CPU-bound `computeNextAlarmInfo` on wrong dispatcher | `threading coroutine main dispatcher` |
| 11 | `NetworkModule.kt` | Medium | No OkHttp response cache | `network http caching request` |
| 12 | `StatisticsScreen.kt` | Low | Missing `contentType` in LazyColumn | `list scroll lazy virtualize` |
| 13 | `AlarmEntity.kt` | Low | No index on `isEnabled` column | `database query index room` |
| 14 | `gradle.properties` | Low | Parallel builds disabled | `apk size binary proguard shrink` |
| 15 | *(missing)* | Low | No StrictMode in debug | `threading coroutine main dispatcher` |
| 16 | *(missing)* | Low | No JankStats production monitoring | `ui rendering frame drop jank` |
| 17 | `HomeScreen.kt` | Low | Business logic / string formatting in Composable | `anti-pattern: business logic in UI` |

17 real findings, each linked to an exact database rule — not generic advice.

### `/mobile-security-audit` — same app, same command

![Security audit output — 20 checks against 437 security rules](docs/security-audit-example.png)

| # | Check | Status |
|---|-------|--------|
| 1 | Encrypted SharedPreferences for sensitive local data | ❌ Fails — `SnoozeManager` uses plain SharedPreferences |
| 2 | `network_security_config.xml` with `cleartextTrafficPermitted=false` | ❌ Fails — No NSC file present |
| 3 | OkHttp `CertificatePinner` with backup pin | ❌ Fails — No pinning configured |
| 4 | TLS 1.2/1.3 minimum via `ConnectionSpec.MODERN_TLS` | ❌ Fails — No minimum TLS version set |
| 5 | Exported `BroadcastReceiver` protected by `android:permission` | ❌ Fails — `AlarmReceiver` exported without permission |
| 6 | Backup exclusion rules for sensitive files | ❌ Fails — `backup_rules.xml` and `data_extraction_rules.xml` are empty stubs |
| 7 | `FLAG_SECURE` on sensitive Activities | ❌ Fails — `AlarmTriggerActivity` missing FLAG_SECURE |
| 8 | Intent extra validation (length, range) | ❌ Fails — Alarm label/ID not sanitised |
| 9 | R8 minification enabled in release | ✅ Pass — `isMinifyEnabled=true`, `isShrinkResources=true` |
| 10 | `PendingIntent.FLAG_IMMUTABLE` used | ✅ Pass — All PendingIntents use `FLAG_IMMUTABLE` |
| 11 | Logging gated to debug builds | 🟡 Partial — `HttpLoggingInterceptor` is debug-only but uses `Level.BODY` |
| 12 | `AlarmService` not exported | ✅ Pass — `android:exported="false"` |
| 13 | `AlarmTriggerActivity` not exported | ✅ Pass — `android:exported="false"` |
| 14 | Room database encrypted (SQLCipher) | ❌ Fails — Unencrypted Room database |
| 15 | DataStore encrypted | ❌ Fails — Plain unencrypted DataStore |
| 16 | Play Integrity API / root detection | ❌ Fails — No integrity checks |
| 17 | Runtime `ACTIVITY_RECOGNITION` permission request | ❌ Needs verification |
| 18 | No hardcoded production API credentials | ✅ Pass — `BASE_URL` is placeholder, no keys in code |
| 19 | ProGuard rules minimal (no broad `-keep class **`) | 🟡 Partial — Rules are targeted but retain debug attributes |
| 20 | `allowBackup` is false or backup rules exclude sensitive data | ❌ Fails — `allowBackup=true` with no exclusions |

20 security checks, 11 failures, 2 partials — surfaced in seconds against 437 database rules.

---

## What's Inside

| Category | Entries | What You Get |
|---|---|---|
| Architecture Patterns | 49 | MVVM, MVI, Clean Architecture, VIPER, TCA, BLoC, Redux, KMP |
| Design Patterns | 117 | Repository, Factory, Observer, Strategy, Adapter, code smells |
| UI Patterns | 91 | Navigation, lists, sheets, inputs, modals, animations, onboarding |
| Anti-Patterns | 120 | God Activity, memory leaks, prop drilling, setState abuse |
| Libraries | 103 | Retrofit, Hilt, Coil, Kingfisher, Dio, BLoC, Redux, Apollo, Koin |
| Performance | 228 | Startup, rendering, memory, network, Compose, CI/CD, monitoring |
| Security | 437 | Encryption, keychain, SSL pinning, biometric, compliance, privacy |
| Testing | 73 | Unit, UI, integration, E2E, screenshot, contract, fuzz testing |
| Reasoning Rules | 56 | Smart recommendations based on your product type |
| Project Templates | 18 | Starter configs for common app types |
| Code Snippets | 80 | Copy-paste templates for Android, iOS, Flutter, React Native |
| Gradle Dependencies | 78 | Ready-to-paste dependency declarations and plugins |
| Platform Guidelines | 592 | Android (423), iOS (60), Flutter (54), React Native (55) |

Every entry includes a **Reference URL** linking to official docs, GitHub repos, or guides.

---

## Installation

### Quick Install (Recommended)

```bash
cd /path/to/your/mobile/project
npx mobile-best-practices init
```

Pick your AI assistant and mobile platform. Done. The skill is installed into your project and your `.gitignore` is updated automatically so skill files don't show up in git changes.

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

---

## How It Works

After installation, your AI assistant searches 2,042 best practices through a built-in BM25 search engine. **You don't need to learn any commands** — just chat naturally.

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

Type `/` to see all available commands:

| Command | What It Does |
|---|---|
| `/mobile-best-practices` | Invokes the main skill |
| `/mobile-security-audit` | Full security audit against 437 rules — finds hardcoded secrets, insecure storage, missing SSL pinning, and more |
| `/mobile-performance-check` | Performance analysis against 228 rules — finds recomposition issues, thread violations, slow startup, memory leaks, and more |
| `/mobile-setup-android` | Scaffolds a new Android project with the full best-practice stack |

---

## Use Cases & Examples

### "Audit my project for security issues"

Scans your entire codebase against 437 security best practices:

```
"Check my Android project for security vulnerabilities"
"Audit my iOS app for data privacy issues"
"Review my Flutter app for OWASP mobile top 10"
"Are there any hardcoded API keys or secrets in my project?"
```

Catches issues like:
- Hardcoded API keys and secrets
- Insecure data storage (SharedPreferences, UserDefaults)
- Missing SSL/certificate pinning
- Improper encryption usage
- Insecure authentication flows
- Missing root/jailbreak detection
- Sensitive data in logs or crash reports

### "Check my project for performance issues"

Reviews your code against 228 performance rules (see the real example in the table above):

```
"Find performance issues in my Android app"
"Why is my app startup slow?"
"Review my Compose code for unnecessary recompositions"
"Check my LazyColumn for performance problems"
"Audit my app's memory usage patterns"
```

### "Review my entire project"

Full audit across all domains:

```
"Do a full code review of my Android project"
"Audit my iOS app — architecture, security, performance, everything"
"Review my Flutter project and suggest improvements"
```

Reviews against:
- Architecture — is the structure maintainable?
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

### "Help with Gradle setup"

Get exact, paste-ready dependency declarations:

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
| `designpattern` | 117 | Design patterns & code smell detection |
| `ui` | 91 | UI components, navigation, lists, inputs, animations |
| `antipattern` | 120 | Common mistakes to avoid |
| `library` | 103 | Libraries and dependencies |
| `performance` | 228 | Speed, memory, battery, rendering optimization |
| `security` | 437 | Encryption, auth, storage, compliance |
| `testing` | 73 | Unit, UI, integration, E2E testing |
| `reasoning` | 56 | Smart recommendations by product type |
| `template` | 18 | Project starter configurations |
| `snippet` | 80 | Copy-paste code templates |
| `gradle` | 78 | Gradle dependency declarations |

---

## Advanced: Manual Search

Run searches directly from the terminal:

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
