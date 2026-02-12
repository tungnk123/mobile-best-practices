# mobilepro-cli

CLI to install Mobile Best Practices skill for AI coding assistants.

## Install

```bash
npm install -g mobilepro-cli
```

## Usage

```bash
cd /path/to/your/project

# Android-focused (Jetpack Compose)
mobilepro init --ai claude --platform android

# iOS-focused (SwiftUI)
mobilepro init --ai claude --platform ios

# Flutter-focused (Dart/BLoC)
mobilepro init --ai cursor --platform flutter

# React Native-focused (TypeScript)
mobilepro init --ai copilot --platform react-native

# All platforms (unified)
mobilepro init --ai claude --platform all

# All AI assistants + Android
mobilepro init --ai all --platform android

# Interactive mode (prompts for both)
mobilepro init
```

## Commands

```bash
mobilepro init        # Install skill for your AI assistant
mobilepro update      # Check for updates
mobilepro versions    # List versions and changelog
```

## Platform-Specific Skills

Each platform gets a focused SKILL.md with:
- Platform-specific default stack and code examples
- Targeted search commands (auto-filters by platform)
- Platform-specific anti-patterns and checklist
- Focused code generation rules

| Platform | Default Stack |
|---|---|
| `android` | MVVM + Hilt + Room + Retrofit + Coil + Compose + Material3 |
| `ios` | MVVM + SwiftUI + Combine + async/await + SwiftData + Kingfisher |
| `flutter` | BLoC + Dio + GoRouter + Drift + CachedNetworkImage |
| `react-native` | Redux Toolkit + Axios + React Navigation + MMKV + FastImage |
| `all` | Unified skill covering all 4 platforms |

## Supported AI Assistants

Claude Code, Cursor, Windsurf, GitHub Copilot, Kiro, Codex CLI, Gemini CLI, Roo Code, Continue, OpenCode, Qoder, CodeBuddy, Trae, Antigravity
