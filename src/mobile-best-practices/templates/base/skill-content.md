# Mobile Best Practices

**1,926 searchable best practices** for Android, iOS, Flutter, and React Native. Android-first with Jetpack Compose.

## Prerequisites

Python 3.x required. Check: `python3 --version`

## Search

```bash
python3 {SKILL_PATH}/scripts/search.py "<query>" --domain <domain> [-n <max_results>]
python3 {SKILL_PATH}/scripts/search.py "<query>" --platform <platform>
python3 {SKILL_PATH}/scripts/search.py "<query>" --domain <domain> --filter-platform <platform>
python3 {SKILL_PATH}/scripts/search.py "<query>" --domain <domain> --compact  # token-optimized output
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

`android` (404) | `android-xml` (404) | `ios` (60) | `flutter` (54) | `react-native` (55)

### Flags

`--domain`/`-d` domain | `--platform`/`-p` platform | `--filter-platform`/`-fp` filter | `--stack`/`-s` tech stack | `--max-results`/`-n` count (default: 3) | `--compact`/`-c` shorter output | `--json` JSON output | `--persist` save blueprint

## Workflow

When user requests mobile work, **default to Android with Jetpack Compose** unless specified otherwise.

### Build: search snippet → gradle → platform → antipattern → designpattern → architecture

```bash
python3 {SKILL_PATH}/scripts/search.py "viewmodel repository" --domain snippet -n 3
python3 {SKILL_PATH}/scripts/search.py "hilt room retrofit" --domain gradle -n 5
python3 {SKILL_PATH}/scripts/search.py "compose state" --platform android -n 5
python3 {SKILL_PATH}/scripts/search.py "android compose" --domain antipattern
python3 {SKILL_PATH}/scripts/search.py "repository factory" --domain designpattern
python3 {SKILL_PATH}/scripts/search.py "mvvm clean" --domain architecture
```

### Review: antipattern → designpattern → platform → performance → security

```bash
python3 {SKILL_PATH}/scripts/search.py "android compose viewmodel" --domain antipattern -n 5
python3 {SKILL_PATH}/scripts/search.py "code smell switch if-else" --domain designpattern -n 5
python3 {SKILL_PATH}/scripts/search.py "state recomposition lifecycle" --platform android -n 5
python3 {SKILL_PATH}/scripts/search.py "compose lazy startup" --domain performance
python3 {SKILL_PATH}/scripts/search.py "storage encryption api key" --domain security
```

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
