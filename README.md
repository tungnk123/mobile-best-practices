# Mobile Best Practices

Searchable database of **598 mobile development best practices** packaged as an AI skill for Claude Code and 14 other AI coding assistants. Covers Android, iOS, Flutter, and React Native.

## What's Inside

| CSV Database | Entries | Description |
|---|---|---|
| Architecture Patterns | 25 | MVVM, MVI, Clean Architecture, VIPER, TCA, BLoC, Redux |
| UI Patterns | 55 | Bottom navigation, lists, sheets, pull-to-refresh, tabs |
| Anti-Patterns | 54 | God Activity, memory leaks, prop drilling, setState abuse |
| Libraries | 64 | Retrofit, Hilt, Coil, Kingfisher, Dio, BLoC, Redux Toolkit |
| Performance | 43 | Startup, recomposition, memory, battery, image loading |
| Security | 35 | Encryption, keychain, SSL pinning, biometric, token storage |
| Testing | 35 | Unit tests, UI tests, BLoC tests, snapshot, mocking |
| Reasoning Rules | 32 | Product-type recommendations (e-commerce, banking, etc.) |
| Project Templates | 18 | Starter configs for common app types |
| Code Snippets | 28 | Copy-paste Android/Compose templates |
| Gradle Dependencies | 46 | Ready-to-paste dependency declarations |
| Platform Guidelines | 163 | Android (59), iOS (35), Flutter (34), React Native (35) |

Every entry includes a **Reference URL** linking to official docs, GitHub repos, or guides.

## Quick Start

### Option A: CLI Installer (any AI assistant)

```bash
npm install -g mobilepro-cli

cd /path/to/your/project

# Android-focused skill
mobilepro init --ai claude --platform android

# iOS-focused skill
mobilepro init --ai claude --platform ios

# Flutter-focused skill
mobilepro init --ai cursor --platform flutter

# All platforms (unified)
mobilepro init --ai claude --platform all

# Interactive mode (prompts for AI + platform)
mobilepro init
```

Supported AI: `claude`, `cursor`, `windsurf`, `copilot`, `kiro`, `codex`, `gemini`, `roocode`, `continue`, `opencode`, `qoder`, `codebuddy`, `trae`, `antigravity`, `all`

Supported platforms: `android`, `ios`, `flutter`, `react-native`, `all`

### Option B: Manual (Claude Code)

Copy the `.claude/skills/mobile-best-practices/` directory into your project. Ensure Python 3 is available.

## How It Works

The skill installs a SKILL.md file that teaches your AI assistant to search the CSV databases using a built-in BM25 search engine. When you ask your AI to build, review, or fix mobile code, it automatically queries the right domains.

### Search Examples

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
```

### Search Domains

`architecture` `ui` `antipattern` `library` `performance` `security` `testing` `reasoning` `template` `snippet` `gradle`

### Search Flags

| Flag | Description |
|---|---|
| `--domain` / `-d` | Search a specific domain |
| `--platform` / `-p` | Platform guidelines (android, ios, flutter, react-native) |
| `--stack` / `-s` | Filter by tech stack (compose, swiftui, flutter, react-native, etc.) |
| `--filter-platform` / `-fp` | Filter any domain results by platform |
| `--persist` | Save results as architecture blueprint markdown |
| `--max-results` / `-n` | Number of results (default: 3) |
| `--json` | Output as JSON |

## Project Structure

```
src/mobile-best-practices/          # Source of truth
├── data/                           # 15 CSV databases
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
│   ├── core.py                     # BM25 search engine
│   └── search.py                   # CLI interface
└── templates/
    ├── base/                       # Shared SKILL.md content
    └── platforms/                  # 15 AI platform configs

cli/                                # npm package (mobilepro-cli)
├── src/                            # TypeScript source
├── assets/                         # Bundled data for offline install
└── package.json

.claude/skills/mobile-best-practices/  # Symlinks to src/
```

## Supported Platforms

| Platform | Default Stack |
|---|---|
| **Android** | Jetpack Compose + Hilt + Room + Retrofit + Coil + Navigation Compose |
| **iOS** | SwiftUI + Combine/async-await + SwiftData + URLSession + Kingfisher |
| **Flutter** | BLoC/Riverpod + Dio + Drift/Hive + GoRouter + CachedNetworkImage |
| **React Native** | Redux Toolkit/Zustand + Axios + MMKV + React Navigation + FastImage |

## Supported AI Assistants

Claude Code, Cursor, Windsurf, GitHub Copilot, Kiro, Codex CLI, Gemini CLI, Roo Code, Continue, OpenCode, Qoder, CodeBuddy, Trae, Antigravity

## Contributing

1. **Data changes** - Edit CSVs in `src/mobile-best-practices/data/`. Changes auto-propagate via symlinks.
2. **Search engine** - Edit `src/mobile-best-practices/scripts/core.py`.
3. **CLI** - Edit `cli/src/`, build with `npm run build` in `cli/`.
4. **Sync CLI assets** before publishing:
   ```bash
   cp -r src/mobile-best-practices/data/* cli/assets/data/
   cp -r src/mobile-best-practices/scripts/* cli/assets/scripts/
   cp -r src/mobile-best-practices/templates/* cli/assets/templates/
   ```

## Requirements

- Python 3.x (no external dependencies)
- Node.js 18+ (CLI only)

## License

MIT
