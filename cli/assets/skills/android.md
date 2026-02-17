---
name: mobile-best-practices-android
description: "Android development intelligence with Jetpack Compose. 49 architecture patterns, 117 design patterns, 91 UI patterns, 113 anti-patterns, 103 libraries, 228 performance rules, 437 security practices, 73 testing patterns, 79 code snippets, 78 Gradle declarations, 246 Android-specific guidelines. Default stack: MVVM + Hilt + Room + Retrofit + Coil + Navigation Compose + Material3. Actions: plan, build, create, design, implement, review, fix, improve, optimize, refactor, architect Android apps."
---

# Android Best Practices - Jetpack Compose Development Intelligence

Searchable database of **2,024 mobile best practices**, **optimized for Android with Jetpack Compose**. All searches default to Android platform. Includes copy-paste code snippets and ready-to-use Gradle dependency declarations.

## Prerequisites

```bash
python3 --version || python --version
```

If not installed: `brew install python3` (macOS) | `sudo apt install python3` (Linux) | `winget install Python.Python.3.12` (Windows)

---

## How to Use This Skill

When user requests Android development work (build, create, architect, review, fix, optimize), follow this workflow:

### Step 1: Extract Requirements

No need to detect platform - **always Android with Jetpack Compose**. Extract:
- **Product type**: E-commerce, Banking, Social Media, Healthcare, Delivery, Fitness, Education, Chat
- **Scope**: New project, new feature, code review, refactor, fix bug, optimize

### Step 2: Search the Database

Use `search.py` with `--platform android` or `--stack compose` for focused results.

```bash
# Android platform guidelines (ALWAYS search this first)
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --platform android -n 5

# Code snippets (copy-paste Kotlin/Compose templates)
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain snippet -n 3

# Gradle dependencies (ready-to-paste declarations)
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain gradle -n 5

# Architecture patterns
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain architecture

# Anti-patterns filtered for Android
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain antipattern --filter-platform android

# Performance rules filtered for Android
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain performance --filter-platform android

# Stack-specific search
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --stack compose
```

### Step 3: Recommended Search Order for Android

```bash
# 1. Get code snippet for what you're building
python3 {SKILL_PATH}/scripts/search.py "viewmodel repository" --domain snippet -n 3

# 2. Get Gradle dependencies needed
python3 {SKILL_PATH}/scripts/search.py "hilt room retrofit" --domain gradle -n 5

# 3. Get Android-specific best practices
python3 {SKILL_PATH}/scripts/search.py "compose state hilt" --platform android -n 5

# 4. Check anti-patterns to avoid
python3 {SKILL_PATH}/scripts/search.py "android compose" --domain antipattern --filter-platform android

# 5. Get architecture guidance
python3 {SKILL_PATH}/scripts/search.py "mvvm clean architecture" --domain architecture

# 6. Check performance rules
python3 {SKILL_PATH}/scripts/search.py "compose recomposition lazy" --domain performance --filter-platform android
```

### Step 4: Generate Code

Use snippet results as starting templates. Customize for user's needs. Follow the code generation rules below.

---

## Search Reference

### Available Domains (11 total)

| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `snippet` | **Copy-paste Kotlin/Compose templates** | viewmodel, repository, room setup, hilt module, compose screen, navigation, paging, datastore |
| `gradle` | **Ready-to-paste Gradle dependencies** | compose bom, hilt, room, retrofit, coil, navigation, testing, paging |
| `reasoning` | Product type recommendations | e-commerce, banking, social media, healthcare, delivery |
| `architecture` | Architecture patterns | mvvm, clean architecture, mvi |
| `library` | Libraries & dependencies | retrofit, hilt, coil, room, okhttp, moshi |
| `ui` | UI patterns & components | bottom navigation, list, bottom sheet, pull refresh |
| `antipattern` | Common mistakes | god activity, memory leak, recomposition |
| `performance` | Performance optimization | startup, recomposition, memory, battery, image |
| `security` | Security best practices | encryption, keystore, ssl pinning, biometric |
| `testing` | Testing patterns | unit test, compose test, mockk, turbine |
| `template` | Project templates/starters | e-commerce android, banking android |

### Flags

| Flag | Description | Example |
|------|-------------|---------|
| `--domain` / `-d` | Search a specific domain | `--domain snippet` |
| `--platform` / `-p` | Platform guidelines | `--platform android` |
| `--filter-platform` / `-fp` | Filter results by platform | `--domain library --filter-platform android` |
| `--stack` / `-s` | Stack-specific search | `--stack compose` |
| `--max-results` / `-n` | Number of results (default: 3) | `-n 5` |
| `--json` | Output as JSON | `--json` |

---

## Example Workflows

### New Feature: "Add a product list screen"

```bash
python3 {SKILL_PATH}/scripts/search.py "viewmodel compose screen" --domain snippet -n 3
python3 {SKILL_PATH}/scripts/search.py "coil paging compose" --domain gradle -n 5
python3 {SKILL_PATH}/scripts/search.py "lazy list image performance" --platform android -n 3
python3 {SKILL_PATH}/scripts/search.py "product list card" --domain ui --filter-platform android
```

### New Project: "Build an e-commerce app"

```bash
python3 {SKILL_PATH}/scripts/search.py "e-commerce" --domain reasoning
python3 {SKILL_PATH}/scripts/search.py "mvvm clean architecture android" --domain architecture
python3 {SKILL_PATH}/scripts/search.py "viewmodel repository hilt" --domain snippet -n 5
python3 {SKILL_PATH}/scripts/search.py "room navigation theme" --domain snippet -n 5
python3 {SKILL_PATH}/scripts/search.py "compose hilt room retrofit" --domain gradle -n 10
python3 {SKILL_PATH}/scripts/search.py "android architecture" --domain antipattern --filter-platform android
python3 {SKILL_PATH}/scripts/search.py "compose startup image" --domain performance --filter-platform android
```

### Code Review: "Review my Android code"

```bash
python3 {SKILL_PATH}/scripts/search.py "android compose viewmodel" --domain antipattern -n 5
python3 {SKILL_PATH}/scripts/search.py "state recomposition lifecycle" --platform android -n 5
python3 {SKILL_PATH}/scripts/search.py "compose lazy image startup" --domain performance --filter-platform android
python3 {SKILL_PATH}/scripts/search.py "android storage encryption api key" --domain security --filter-platform android
```

### Gradle Setup: "What dependencies do I need?"

```bash
python3 {SKILL_PATH}/scripts/search.py "compose material3 bom" --domain gradle -n 5
python3 {SKILL_PATH}/scripts/search.py "hilt room retrofit" --domain gradle -n 5
python3 {SKILL_PATH}/scripts/search.py "navigation coil paging" --domain gradle -n 5
python3 {SKILL_PATH}/scripts/search.py "testing junit mockk turbine" --domain gradle -n 5
```

---

## Code Generation Rules

### Default Stack

```
Architecture:  MVVM + Clean Architecture + Repository Pattern
DI:            Hilt (@HiltViewModel, @Inject, @Module)
UI:            Jetpack Compose + Material3
State:         StateFlow + sealed interface UiState
Events:        Channel<Event> for one-shot (navigation, snackbar)
Navigation:    Navigation Compose with @Serializable type-safe routes
Network:       Retrofit + Kotlin Serialization + OkHttp
Database:      Room + KSP
Image:         Coil (AsyncImage)
Async:         Coroutines + Flow (viewModelScope, Dispatchers.IO)
Testing:       JUnit5 + MockK + Turbine + Compose Test
Build:         Version Catalog (libs.versions.toml) + KSP
```

### Always Use Sealed Interface for UiState

```kotlin
sealed interface HomeUiState {
    data object Loading : HomeUiState
    data class Success(val items: List<Item>) : HomeUiState
    data class Error(val message: String) : HomeUiState
    data object Empty : HomeUiState
}
```

### Always Use @HiltViewModel Pattern

```kotlin
@HiltViewModel
class HomeViewModel @Inject constructor(
    private val repository: HomeRepository
) : ViewModel() {
    private val _uiState = MutableStateFlow<HomeUiState>(HomeUiState.Loading)
    val uiState: StateFlow<HomeUiState> = _uiState.asStateFlow()

    fun loadData() {
        viewModelScope.launch {
            _uiState.value = HomeUiState.Loading
            try {
                val data = repository.getData()
                _uiState.value = if (data.isEmpty()) HomeUiState.Empty
                    else HomeUiState.Success(data)
            } catch (e: Exception) {
                _uiState.value = HomeUiState.Error(e.message ?: "Unknown error")
            }
        }
    }
}
```

### Always Use collectAsStateWithLifecycle

```kotlin
@Composable
fun HomeScreen(viewModel: HomeViewModel = hiltViewModel()) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    when (val state = uiState) {
        is HomeUiState.Loading -> LoadingIndicator()
        is HomeUiState.Success -> ItemList(state.items)
        is HomeUiState.Error -> ErrorMessage(state.message, onRetry = viewModel::loadData)
        is HomeUiState.Empty -> EmptyState()
    }
}
```

### Anti-Patterns to ALWAYS Avoid

- Business logic in Activities/Fragments
- Direct database access in UI layer
- GlobalScope for coroutines (use viewModelScope)
- collectAsState without lifecycle (use collectAsStateWithLifecycle)
- Not handling process death (use SavedStateHandle)
- KAPT instead of KSP (KSP is 2x faster)
- Hardcoded versions in build.gradle (use Version Catalog)
- Toast for user feedback (use Snackbar with SnackbarHostState)
- God classes (500+ lines)
- Hardcoded strings — ALWAYS use stringResource(R.string.xxx) for user-visible text in Compose, never Text("literal")
- Hardcoded colors — use MaterialTheme.colorScheme, never Color(0xFF...)
- No error handling
- Hardcoded API keys
- Storing secrets in plain SharedPreferences

---

## Pre-Delivery Checklist

### Architecture
- [ ] MVVM with Clean Architecture layers (UI / ViewModel / Repository / DataSource)
- [ ] Hilt dependency injection configured
- [ ] Repository pattern for data access
- [ ] Sealed interface for UI state (Loading, Success, Error, Empty)
- [ ] One-shot events via Channel (not SharedFlow replay=0)

### Compose
- [ ] collectAsStateWithLifecycle (NOT collectAsState)
- [ ] LazyColumn with stable keys and contentType
- [ ] rememberSaveable for user input state
- [ ] Proper Modifier ordering (clickable before padding)
- [ ] Material3 components (Scaffold, TopAppBar, NavigationBar)
- [ ] @Preview for all screens with sample data

### Gradle
- [ ] Version Catalog (libs.versions.toml) for all dependencies
- [ ] Compose BOM managing Compose versions
- [ ] KSP for annotation processing (not KAPT)
- [ ] Correct configurations (implementation vs api vs testImplementation)

### Performance
- [ ] LazyColumn/LazyGrid with stable keys
- [ ] Images cached with Coil + size()
- [ ] No work on main thread (Dispatchers.IO)
- [ ] derivedStateOf for computed values
- [ ] Baseline Profiles for startup

### Security
- [ ] No hardcoded secrets/API keys
- [ ] EncryptedSharedPreferences for sensitive data
- [ ] HTTPS for all network calls
- [ ] R8/ProGuard enabled for release builds
- [ ] Certificate pinning for sensitive APIs

### Testing
- [ ] Unit tests for ViewModels (runTest + Turbine + MockK)
- [ ] Mocked dependencies in tests
- [ ] Error states tested
- [ ] Compose UI tests for critical screens

### Accessibility
- [ ] contentDescription on Images and IconButtons
- [ ] Sufficient color contrast (4.5:1 minimum)
- [ ] Touch targets minimum 48dp
- [ ] Screen reader navigation works
