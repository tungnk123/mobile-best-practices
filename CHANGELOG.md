# Changelog

All notable changes to this project will be documented in this file.

Format: [Semantic Versioning](https://semver.org/)

---

## [1.7.0] — 2026-03-06

### Added
- `Source URL` column in `code-snippets.csv` — 37 Android snippets now link directly to verified `androidx/` source code on `cs.android.com` (ViewModel.kt, LazyList.kt, NavHost.kt, RoomDatabase.kt, BiometricPrompt.kt, AppInitializer.kt, WorkManager.kt, and more)
- `Source URL` now shown in BM25 search output for snippet domain results
- `scripts/check-urls.py` — concurrent HTTP checker (10 threads) for all 964 unique Reference URL, Docs URL, and Source URL entries across 14 CSV files
- `DEMO.md` — live search output samples showing real database results before install
- `CONTRIBUTING.md` — full guide for adding entries: column schemas, CSV conventions, quality checklist, gap areas
- `CHANGELOG.md` — version history

### Fixed
- **61 broken reference URLs** fixed across all CSV files:
  - `refactoring.guru` (16): `/refactoring/smells/xxx` → `/smells/xxx`
  - `developer.android.com` (17): perfetto, RTL, bottom-nav, predictive-back, companion-device, drawable-animation, SMS retriever, and more — all moved after 2024 site redesign
  - `developer.apple.com` (8): Xcode performance docs renamed, SwiftUI task URL, app-privacy-details path changed
  - `support.google.com` (4): Play Console answer IDs replaced with `developer.android.com` canonical URLs
  - `reactnative.dev` (3): turbo-modules/native-modules migrated to new architecture docs
  - `gdpr.eu` (2): replaced with `gdpr-info.eu`
  - Apollo Kotlin, Expo prebuild, Flutter perf, Redux Toolkit, AsyncStorage, MITRE ATLAS, EBA DORA, FTC COPPA — updated paths
- CSV parse bug in `platforms/android.csv` row 413: unquoted comma caused `Severity` field to contain `"or Parcelable"` — now correctly quoted

### Changed
- `scripts/validate-csv.py` upgraded with:
  - Severity value validation (Critical/High/Medium/Low only)
  - Duplicate detection per domain identifier column
  - Source URL presence check for Android snippets
  - Missing URL count per file
- `.github/workflows/ci.yml` upgraded:
  - New `check-urls` job (runs on push to `main`)
  - `test-search` job now asserts JSON output and verifies `cs.android.com` in snippet Source URL
  - All search smoke tests use JSON assertions per domain
- `README.md`: added npm version, downloads, Python, MIT, entries, and platforms badges; added links to Demo, Changelog, Contributing
- Badges: `[![npm version]...]`, `[![npm downloads]...]`, `[![Python 3.x]...]`, `[![MIT]...]`, `[![entries: 2,042]...]`, `[![platforms]...]`

---

## [1.6.1] — 2025-03-04

### Added
- `/mobile-anr-crash-check` slash command — comprehensive ANR, crash, and splash screen audit with 20 targeted database searches
- Step 5 post-generation checks in `android.md` — after every code generation, automatically checks performance, security, and ANR/crash/splash using keywords extracted from the generated code
- Splash screen searches added to ANR/crash workflow (cold start, SplashScreen API, deferred init)
- `mobile-anr-crash-check` command listed in CLI installer output

### Changed
- All workflow searches updated to `-n 5` (focused results)
- All audit commands updated to `-n 10` to `-n 15` (thorough coverage)
- Removed `--filter-platform` from workflow searches — results now pull from all platforms for broader coverage
- Updated description metadata in `android.md` and `SKILL.md` to mention post-generation checks

---

## [1.6.0] — 2025-02-14

### Added
- TypeScript dependency updated to 5.9.3
- Version metadata synchronized across `SKILL.md` and `package.json`

### Changed
- Performance and security audit documentation enhanced for clarity
- README updated with real project image examples

---

## [1.5.0] — 2025-01-20

### Added
- `/mobile-performance-check` slash command — full project performance audit
- `/mobile-security-audit` slash command — full project security audit mapped to OWASP Mobile Top 10
- `/mobile-setup-android` slash command — guided Android project setup by app type

### Changed
- README updated with slash command documentation and use case examples
- IDE restart note added for slash command registration

---

## [1.4.0] — 2025-01-10

### Added
- Hardcoded string best practices — `stringResource(R.string.xxx)` enforcement
- Hardcoded color anti-pattern — `MaterialTheme.colorScheme` enforcement

### Changed
- Anti-patterns updated with Compose-specific rules

---

## [1.3.0] — 2024-12-15

### Added
- Android security best practices (437 entries in `security.csv`)
- Android XML View support via `android-xml` platform flag
- Enhanced code quality guidelines
- `.gitignore` auto-update fix in CLI installer

### Changed
- CLI version bumped to 1.3.0

---

## [1.2.0] — 2024-12-01

### Added
- Version compatibility matrix for key Android libraries
- Kotlin Serialization replacing Moshi as default JSON library
- OpenCode platform support with slash commands

---

## [1.1.0] — 2024-11-15

### Added
- Design patterns domain (`design-patterns.csv`) — 117 entries
- Repository, Factory, Observer, Strategy, Adapter patterns with code smells
- Code smell detection entries

### Changed
- README updated with design pattern documentation

---

## [1.0.0] — 2024-11-01

### Initial Release

- 2,042 searchable mobile best practices across 12 domains
- BM25 search engine (`scripts/core.py`, `scripts/search.py`)
- Android platform guidelines (423 entries)
- iOS platform guidelines (60 entries)
- Flutter platform guidelines (54 entries)
- React Native platform guidelines (55 entries)
- Code snippets (80 Kotlin/Compose/Swift/Dart templates)
- Gradle dependency declarations (78 entries)
- Security practices (437 entries)
- Performance rules (228 entries)
- Anti-patterns (120 entries)
- Architecture patterns (49 entries)
- CLI installer (`npx mobile-best-practices init`)
- Support for 15 AI coding assistants (Claude Code, Cursor, Windsurf, GitHub Copilot, and 11 more)
- `android.md`, `ios.md`, `flutter.md`, `react-native.md` skill files
