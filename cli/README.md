# mobile-best-practices

CLI to install Mobile Best Practices skill for AI coding assistants.

## Install

```bash
npm install -g mobile-best-practices
```

## Usage

```bash
cd /path/to/your/project

# Android-focused (Jetpack Compose)
mobile-best-practices init --ai claude --platform android

# iOS-focused (SwiftUI)
mobile-best-practices init --ai claude --platform ios

# Flutter-focused (Dart/BLoC)
mobile-best-practices init --ai cursor --platform flutter

# React Native-focused (TypeScript)
mobile-best-practices init --ai copilot --platform react-native

# All platforms (unified)
mobile-best-practices init --ai claude --platform all

# All AI assistants + Android
mobile-best-practices init --ai all --platform android

# Interactive mode (prompts for both)
mobile-best-practices init
```

## Commands

```bash
mobile-best-practices init        # Install skill for your AI assistant
mobile-best-practices update      # Check for updates
mobile-best-practices versions    # List versions and changelog
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
