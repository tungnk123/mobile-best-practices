---
name: mobile-best-practices-ios
description: "iOS development intelligence with SwiftUI. 49 architecture patterns, 117 design patterns, 91 UI patterns, 113 anti-patterns, 103 libraries, 228 performance rules, 437 security practices, 73 testing patterns, 60 iOS-specific guidelines. Default stack: MVVM + SwiftUI + Combine + async/await + SwiftData + URLSession + Kingfisher + NavigationStack. Actions: plan, build, create, design, implement, review, fix, improve, optimize, refactor, architect iOS apps."
---

# iOS Best Practices - SwiftUI Development Intelligence

Searchable database of **2,024 mobile best practices**, **optimized for iOS with SwiftUI**. All searches default to iOS platform. Covers architecture, UI patterns, security, performance, and testing for Apple platforms.

## Prerequisites

```bash
python3 --version || python --version
```

If not installed: `brew install python3` (macOS) | `sudo apt install python3` (Linux) | `winget install Python.Python.3.12` (Windows)

---

## How to Use This Skill

When user requests iOS development work (build, create, architect, review, fix, optimize), follow this workflow:

### Step 1: Extract Requirements

No need to detect platform - **always iOS with SwiftUI**. Extract:
- **Product type**: E-commerce, Banking, Social Media, Healthcare, Delivery, Fitness, Education, Chat
- **Scope**: New project, new feature, code review, refactor, fix bug, optimize

### Step 2: Search the Database

Use `search.py` with `--platform ios` or `--stack swiftui` for focused results.

```bash
# iOS platform guidelines (ALWAYS search this first)
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --platform ios -n 5

# Stack-specific search
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --stack swiftui

# Architecture patterns
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain architecture

# Anti-patterns filtered for iOS
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain antipattern --filter-platform ios

# Performance rules filtered for iOS
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain performance --filter-platform ios

# Libraries for iOS
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain library --filter-platform ios
```

### Step 3: Recommended Search Order for iOS

```bash
# 1. Get iOS-specific best practices
python3 {SKILL_PATH}/scripts/search.py "swiftui state navigation" --platform ios -n 5

# 2. Get architecture guidance
python3 {SKILL_PATH}/scripts/search.py "mvvm tca viper ios" --domain architecture

# 3. Get iOS libraries
python3 {SKILL_PATH}/scripts/search.py "networking image database" --domain library --filter-platform ios

# 4. Check anti-patterns to avoid
python3 {SKILL_PATH}/scripts/search.py "ios swiftui" --domain antipattern --filter-platform ios

# 5. Check performance rules
python3 {SKILL_PATH}/scripts/search.py "swiftui list image startup" --domain performance --filter-platform ios

# 6. Check security
python3 {SKILL_PATH}/scripts/search.py "keychain biometric encryption" --domain security --filter-platform ios
```

---

## Search Reference

### Available Domains (11 total)

| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `reasoning` | Product type recommendations | e-commerce, banking, social media, healthcare |
| `architecture` | Architecture patterns | mvvm, tca, viper, clean architecture |
| `library` | Libraries & dependencies | alamofire, kingfisher, realm, swiftdata |
| `ui` | UI patterns & components | navigation, list, sheet, tab bar, search |
| `antipattern` | Common mistakes | force unwrap, retain cycle, @ObservedObject |
| `performance` | Performance optimization | startup, list, memory, image, animation |
| `security` | Security best practices | keychain, biometric, ssl pinning, encryption |
| `testing` | Testing patterns | xctest, swift testing, snapshot, ui test |
| `template` | Project templates/starters | banking ios, social media ios |
| `snippet` | Code templates | (primarily Android, but cross-platform patterns available) |
| `gradle` | Gradle dependencies | (Android only - use for cross-reference) |

### Flags

| Flag | Description | Example |
|------|-------------|---------|
| `--platform` / `-p` | Platform guidelines | `--platform ios` |
| `--stack` / `-s` | Stack-specific search | `--stack swiftui` |
| `--domain` / `-d` | Search a specific domain | `--domain architecture` |
| `--filter-platform` / `-fp` | Filter results by platform | `--domain library --filter-platform ios` |
| `--max-results` / `-n` | Number of results (default: 3) | `-n 5` |
| `--json` | Output as JSON | `--json` |

---

## Example Workflows

### New Feature: "Add a settings screen"

```bash
python3 {SKILL_PATH}/scripts/search.py "settings form navigation" --platform ios -n 5
python3 {SKILL_PATH}/scripts/search.py "form list settings" --domain ui --filter-platform ios
python3 {SKILL_PATH}/scripts/search.py "ios navigation state" --domain antipattern --filter-platform ios
```

### New Project: "Build a banking app"

```bash
python3 {SKILL_PATH}/scripts/search.py "banking" --domain reasoning
python3 {SKILL_PATH}/scripts/search.py "tca viper mvvm ios" --domain architecture
python3 {SKILL_PATH}/scripts/search.py "keychain biometric encryption certificate" --domain security --filter-platform ios
python3 {SKILL_PATH}/scripts/search.py "banking security authentication" --platform ios -n 5
python3 {SKILL_PATH}/scripts/search.py "networking database" --domain library --filter-platform ios
```

### Code Review: "Review my iOS code"

```bash
python3 {SKILL_PATH}/scripts/search.py "ios swiftui retain cycle" --domain antipattern --filter-platform ios -n 5
python3 {SKILL_PATH}/scripts/search.py "state navigation lifecycle" --platform ios -n 5
python3 {SKILL_PATH}/scripts/search.py "swiftui list image memory" --domain performance --filter-platform ios
python3 {SKILL_PATH}/scripts/search.py "keychain encryption storage" --domain security --filter-platform ios
```

---

## Code Generation Rules

### Default Stack

```
Architecture:  MVVM + Repository Pattern (or TCA for complex apps)
UI:            SwiftUI + NavigationStack
State:         @Observable (iOS 17+) or ObservableObject + @Published
Navigation:    NavigationStack with NavigationPath
Network:       URLSession + async/await (or Alamofire)
Database:      SwiftData (iOS 17+) or CoreData
Image:         Kingfisher or AsyncImage
Async:         Swift Concurrency (async/await, Task, Actor)
Testing:       Swift Testing + XCTest + ViewInspector
DI:            Environment + @Dependencies (TCA) or manual injection
```

### Always Use @Observable Pattern (iOS 17+)

```swift
@Observable
final class HomeViewModel {
    private(set) var uiState: HomeUiState = .loading
    private let repository: HomeRepository

    init(repository: HomeRepository) {
        self.repository = repository
    }

    func loadData() async {
        uiState = .loading
        do {
            let items = try await repository.getData()
            uiState = items.isEmpty ? .empty : .success(items)
        } catch {
            uiState = .error(error.localizedDescription)
        }
    }
}

enum HomeUiState {
    case loading
    case success([Item])
    case error(String)
    case empty
}
```

### Always Use NavigationStack (not NavigationView)

```swift
struct HomeScreen: View {
    @State private var viewModel = HomeViewModel(repository: .live)
    @State private var path = NavigationPath()

    var body: some View {
        NavigationStack(path: $path) {
            Group {
                switch viewModel.uiState {
                case .loading: ProgressView()
                case .success(let items): ItemListView(items: items)
                case .error(let msg): ErrorView(message: msg, onRetry: { Task { await viewModel.loadData() } })
                case .empty: EmptyStateView()
                }
            }
            .navigationTitle("Home")
            .task { await viewModel.loadData() }
        }
    }
}
```

### Anti-Patterns to ALWAYS Avoid

- Force unwrapping optionals (`!`) - use `guard let` or `if let`
- Retain cycles in closures - use `[weak self]`
- `@ObservedObject` for ViewModel creation - use `@StateObject` or `@State`
- `NavigationView` - use `NavigationStack` (iOS 16+)
- Blocking main thread with synchronous calls
- Not using `@Sendable` for concurrent closures
- God ViewModels (500+ lines)
- Hardcoded strings/colors - use localization and asset catalogs
- Storing secrets in UserDefaults - use Keychain
- Not handling optional binding properly

---

## Pre-Delivery Checklist

### Architecture
- [ ] MVVM or TCA with clear separation of concerns
- [ ] Repository pattern for data access
- [ ] Enum-based UI state (loading, success, error, empty)
- [ ] Proper dependency injection

### SwiftUI
- [ ] NavigationStack (not NavigationView)
- [ ] @Observable or @StateObject for ViewModel
- [ ] .task modifier for async loading
- [ ] Proper use of @State, @Binding, @Environment
- [ ] List with proper identifiable items

### Performance
- [ ] LazyVStack/LazyHStack for long lists
- [ ] Images cached with Kingfisher/AsyncImage
- [ ] No synchronous work on main actor
- [ ] Instruments profiling for memory leaks

### Security
- [ ] Keychain for sensitive data (not UserDefaults)
- [ ] Biometric authentication (Face ID/Touch ID)
- [ ] Certificate pinning for sensitive APIs
- [ ] App Transport Security enabled
- [ ] No hardcoded secrets in source code

### Testing
- [ ] Unit tests with Swift Testing or XCTest
- [ ] Mocked dependencies
- [ ] Error states tested
- [ ] UI tests for critical flows

### Accessibility
- [ ] accessibilityLabel on interactive elements
- [ ] Dynamic Type support
- [ ] VoiceOver navigation works
- [ ] Sufficient color contrast
