# Mobile Best Practices - Development Intelligence

Searchable database of **1,738 mobile development best practices** covering architecture patterns, UI components, anti-patterns, libraries, performance rules, security practices, testing patterns, code snippets, Gradle dependencies, and platform-specific guidelines for Android, iOS, Flutter, and React Native.

**Android-first**: Optimized for Android/Jetpack Compose with full copy-paste code snippets and ready-to-use Gradle declarations.

## Prerequisites

Python 3.x required for the search engine.

## How to Use

When the user requests mobile development work (build, create, architect, review, fix, optimize), search the database for relevant best practices:

```bash
python3 {SKILL_PATH}/scripts/search.py "<query>" --domain <domain> [-n <max_results>]
```

### Available Domains (11 total)

| Domain | Use For |
|--------|---------|
| `snippet` | Copy-paste code templates (Android) |
| `gradle` | Gradle dependency declarations |
| `reasoning` | Product type recommendations |
| `architecture` | Architecture patterns |
| `library` | Libraries and dependencies |
| `ui` | UI patterns and components |
| `antipattern` | Common mistakes |
| `performance` | Performance optimization |
| `security` | Security best practices |
| `testing` | Testing patterns |
| `template` | Project starters |

### Flags

| Flag | Description |
|------|-------------|
| `--domain` / `-d` | Search specific domain |
| `--platform` / `-p` | Platform-specific search (android, ios, flutter, react-native) |
| `--filter-platform` / `-fp` | Filter results by platform |
| `--stack` / `-s` | Filter by tech stack |
| `--persist` | Save architecture blueprint |
| `--max-results` / `-n` | Number of results (default: 3) |
| `--json` | Output as JSON |

### Android Default Stack

```
Architecture:  MVVM + Clean Architecture + Repository Pattern
DI:            Hilt (@HiltViewModel, @Inject, @Module)
UI:            Jetpack Compose + Material3
State:         StateFlow + sealed interface UiState
Navigation:    Navigation Compose with @Serializable type-safe routes
Network:       Retrofit + Moshi + OkHttp
Database:      Room + KSP
Image:         Coil (AsyncImage)
Testing:       JUnit5 + MockK + Turbine + Compose Test
Build:         Version Catalog (libs.versions.toml) + KSP
```
