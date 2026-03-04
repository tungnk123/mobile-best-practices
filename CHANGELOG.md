# Changelog

All notable changes to this project will be documented in this file.

Format: [Semantic Versioning](https://semver.org/)

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
