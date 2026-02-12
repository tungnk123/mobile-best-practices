---
name: mobile-best-practices-flutter
description: "Flutter development intelligence with Dart. 25+ architecture patterns, 55+ UI patterns, 55+ anti-patterns, 65+ libraries, 45+ performance rules, 35+ security practices, 35+ testing patterns, 34+ Flutter-specific guidelines. Default stack: BLoC/Riverpod + Dio + GoRouter + Drift + CachedNetworkImage. Actions: plan, build, create, design, implement, review, fix, improve, optimize, refactor, architect Flutter apps."
---

# Flutter Best Practices - Dart Development Intelligence

Searchable database of 500+ mobile best practices, **optimized for Flutter with Dart**. All searches default to Flutter platform. Covers architecture, widgets, state management, performance, and testing for cross-platform Flutter apps.

## Prerequisites

```bash
python3 --version || python --version
```

If not installed: `brew install python3` (macOS) | `sudo apt install python3` (Linux) | `winget install Python.Python.3.12` (Windows)

---

## How to Use This Skill

When user requests Flutter development work (build, create, architect, review, fix, optimize), follow this workflow:

### Step 1: Extract Requirements

No need to detect platform - **always Flutter with Dart**. Extract:
- **Product type**: E-commerce, Banking, Social Media, Healthcare, Delivery, Fitness, Education, Chat
- **State management**: BLoC (default), Riverpod, Provider, GetX
- **Scope**: New project, new feature, code review, refactor, fix bug, optimize

### Step 2: Search the Database

Use `search.py` with `--platform flutter` or `--stack flutter` for focused results.

```bash
# Flutter platform guidelines (ALWAYS search this first)
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --platform flutter -n 5

# Stack-specific search
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --stack bloc
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --stack riverpod

# Architecture patterns
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain architecture

# Anti-patterns filtered for Flutter
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain antipattern --filter-platform flutter

# Performance rules filtered for Flutter
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain performance --filter-platform flutter

# Libraries for Flutter
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain library --filter-platform flutter
```

### Step 3: Recommended Search Order for Flutter

```bash
# 1. Get Flutter-specific best practices
python3 {SKILL_PATH}/scripts/search.py "bloc state widget" --platform flutter -n 5

# 2. Get architecture guidance
python3 {SKILL_PATH}/scripts/search.py "bloc clean architecture flutter" --domain architecture

# 3. Get Flutter libraries
python3 {SKILL_PATH}/scripts/search.py "networking image state" --domain library --filter-platform flutter

# 4. Check anti-patterns to avoid
python3 {SKILL_PATH}/scripts/search.py "flutter widget setState" --domain antipattern --filter-platform flutter

# 5. Check performance rules
python3 {SKILL_PATH}/scripts/search.py "flutter widget rebuild list" --domain performance --filter-platform flutter

# 6. Check security
python3 {SKILL_PATH}/scripts/search.py "flutter storage encryption api" --domain security --filter-platform flutter
```

---

## Search Reference

### Available Domains (11 total)

| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `reasoning` | Product type recommendations | e-commerce, banking, social media, healthcare |
| `architecture` | Architecture patterns | bloc, clean architecture, riverpod, provider |
| `library` | Libraries & dependencies | dio, riverpod, go_router, drift, hive, freezed |
| `ui` | UI patterns & components | bottom navigation, list, sheet, sliver, drawer |
| `antipattern` | Common mistakes | setState, build method, no dispose, no const |
| `performance` | Performance optimization | widget rebuild, list, image, shader, startup |
| `security` | Security best practices | flutter_secure_storage, encryption, ssl pinning |
| `testing` | Testing patterns | bloc_test, widget test, integration test, mockito |
| `template` | Project templates/starters | e-commerce flutter, delivery flutter |
| `snippet` | Code templates | (cross-platform patterns available) |
| `gradle` | Gradle dependencies | (Android-specific, use for Android module config) |

### Flags

| Flag | Description | Example |
|------|-------------|---------|
| `--platform` / `-p` | Platform guidelines | `--platform flutter` |
| `--stack` / `-s` | Stack-specific search | `--stack bloc` or `--stack riverpod` |
| `--domain` / `-d` | Search a specific domain | `--domain architecture` |
| `--filter-platform` / `-fp` | Filter results by platform | `--domain library --filter-platform flutter` |
| `--max-results` / `-n` | Number of results (default: 3) | `-n 5` |
| `--json` | Output as JSON | `--json` |

---

## Example Workflows

### New Feature: "Add a product list screen"

```bash
python3 {SKILL_PATH}/scripts/search.py "list widget bloc state" --platform flutter -n 5
python3 {SKILL_PATH}/scripts/search.py "list card image" --domain ui --filter-platform flutter
python3 {SKILL_PATH}/scripts/search.py "dio cached_network_image" --domain library --filter-platform flutter
python3 {SKILL_PATH}/scripts/search.py "flutter list rebuild" --domain performance --filter-platform flutter
```

### New Project: "Build an e-commerce app"

```bash
python3 {SKILL_PATH}/scripts/search.py "e-commerce" --domain reasoning
python3 {SKILL_PATH}/scripts/search.py "bloc clean architecture flutter" --domain architecture
python3 {SKILL_PATH}/scripts/search.py "dio go_router drift riverpod" --domain library --filter-platform flutter
python3 {SKILL_PATH}/scripts/search.py "flutter widget setState" --domain antipattern --filter-platform flutter
python3 {SKILL_PATH}/scripts/search.py "flutter startup image list" --domain performance --filter-platform flutter
python3 {SKILL_PATH}/scripts/search.py "flutter encryption storage" --domain security --filter-platform flutter
```

### Code Review: "Review my Flutter code"

```bash
python3 {SKILL_PATH}/scripts/search.py "flutter setState dispose const" --domain antipattern --filter-platform flutter -n 5
python3 {SKILL_PATH}/scripts/search.py "widget state lifecycle" --platform flutter -n 5
python3 {SKILL_PATH}/scripts/search.py "flutter rebuild image memory" --domain performance --filter-platform flutter
python3 {SKILL_PATH}/scripts/search.py "flutter storage encryption key" --domain security --filter-platform flutter
```

---

## Code Generation Rules

### Default Stack

```
Architecture:  BLoC + Clean Architecture + Repository Pattern
State:         flutter_bloc (Cubit for simple, Bloc for complex)
Routing:       GoRouter with typed routes
Network:       Dio + Retrofit (code gen)
Database:      Drift (SQLite) or Hive (NoSQL)
Image:         CachedNetworkImage
DI:            get_it + injectable
Serialization: freezed + json_serializable
Testing:       bloc_test + mocktail + integration_test
Linting:       very_good_analysis
```

### Always Use BLoC/Cubit Pattern

```dart
// State
sealed class HomeState {
  const HomeState();
}

class HomeLoading extends HomeState {
  const HomeLoading();
}

class HomeLoaded extends HomeState {
  final List<Item> items;
  const HomeLoaded(this.items);
}

class HomeError extends HomeState {
  final String message;
  const HomeError(this.message);
}

class HomeEmpty extends HomeState {
  const HomeEmpty();
}

// Cubit
class HomeCubit extends Cubit<HomeState> {
  final HomeRepository _repository;

  HomeCubit(this._repository) : super(const HomeLoading());

  Future<void> loadData() async {
    emit(const HomeLoading());
    try {
      final items = await _repository.getData();
      emit(items.isEmpty ? const HomeEmpty() : HomeLoaded(items));
    } catch (e) {
      emit(HomeError(e.toString()));
    }
  }
}
```

### Always Use BlocBuilder/BlocConsumer

```dart
class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return BlocBuilder<HomeCubit, HomeState>(
      builder: (context, state) => switch (state) {
        HomeLoading() => const Center(child: CircularProgressIndicator()),
        HomeLoaded(:final items) => ItemListView(items: items),
        HomeError(:final message) => ErrorView(message: message, onRetry: () => context.read<HomeCubit>().loadData()),
        HomeEmpty() => const EmptyStateView(),
      },
    );
  }
}
```

### Anti-Patterns to ALWAYS Avoid

- `setState` for complex state (use BLoC/Riverpod/Provider)
- Business logic in `build()` methods
- Not disposing controllers/streams
- Non-`const` constructors for static widgets
- `Column`/`Row` for long lists (use `ListView.builder`)
- Not using `freezed` for data classes
- Mutable state in widgets
- God widgets (500+ lines)
- Hardcoded strings/colors - use l10n and ThemeData
- Storing secrets in SharedPreferences - use flutter_secure_storage

---

## Pre-Delivery Checklist

### Architecture
- [ ] BLoC/Cubit or Riverpod for state management
- [ ] Clean Architecture layers (presentation / domain / data)
- [ ] Repository pattern for data access
- [ ] Sealed class for UI state
- [ ] Dependency injection with get_it

### Widgets
- [ ] `const` constructors where possible
- [ ] `ListView.builder` for long lists (not Column)
- [ ] Proper widget decomposition (no 500+ line widgets)
- [ ] Keys on list items
- [ ] `const` keyword on static widgets

### Performance
- [ ] `const` constructors to prevent unnecessary rebuilds
- [ ] `ListView.builder`/`GridView.builder` for lazy loading
- [ ] Images cached with CachedNetworkImage
- [ ] No heavy computation in build methods
- [ ] RepaintBoundary for complex animations

### Security
- [ ] flutter_secure_storage for sensitive data
- [ ] Certificate pinning for sensitive APIs
- [ ] No hardcoded secrets in source code
- [ ] Obfuscation enabled for release builds
- [ ] Input validation on user inputs

### Testing
- [ ] BLoC tests with bloc_test
- [ ] Widget tests for critical UI
- [ ] Integration tests for critical flows
- [ ] Mocked dependencies with mocktail

### Accessibility
- [ ] Semantics widgets for screen readers
- [ ] Sufficient color contrast
- [ ] Touch targets minimum 48x48
- [ ] Proper label text for form fields
