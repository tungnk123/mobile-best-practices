---
name: mobile-best-practices-android-xml
description: "Android development intelligence with XML Views. 49 architecture patterns, 117 design patterns, 91 UI patterns, 113 anti-patterns, 103 libraries, 228 performance rules, 437 security practices, 73 testing patterns, 79 code snippets, 78 Gradle declarations, 246 Android-specific guidelines. Default stack: MVVM + Hilt + Room + Retrofit + Coil + XML Views + ViewBinding + Fragments. Actions: plan, build, create, design, implement, review, fix, improve, optimize, refactor, architect Android apps."
---

# Android Best Practices - XML Views Development Intelligence

Searchable database of **2,024 mobile best practices**, **optimized for Android with XML Views**. All searches default to Android platform. Includes best practices for View System, Fragments, and ConstraintLayout.

## Prerequisites

```bash
python3 --version || python --version
```

If not installed: `brew install python3` (macOS) | `sudo apt install python3` (Linux) | `winget install Python.Python.3.12` (Windows)

---

## How to Use This Skill

When user requests Android development work (build, create, architect, review, fix, optimize), follow this workflow:

### Step 1: Extract Requirements

No need to detect platform - **always Android with XML Views**. Extract:
- **Product type**: E-commerce, Banking, Social Media, Healthcare, Delivery, Fitness, Education, Chat
- **Scope**: New project, new feature, code review, refactor, fix bug, optimize
- **View System**: Fragments, ConstraintLayout, RecyclerView, ViewBinding

### Step 2: Search the Database

Use `search.py` with `--platform android` for focused results.

```bash
# Android platform guidelines (ALWAYS search this first)
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --platform android -n 5

# XML Views / Layout best practices
python3 {SKILL_PATH}/scripts/search.py "xml view constraintlayout recyclerview" --platform android -n 5

# Gradle dependencies (ready-to-paste declarations)
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain gradle -n 5

# Architecture patterns
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain architecture

# Anti-patterns filtered for Android
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain antipattern --filter-platform android

# Performance rules filtered for Android
python3 {SKILL_PATH}/scripts/search.py "<keyword>" --domain performance --filter-platform android
```

### Step 3: Recommended Search Order for Android XML

```bash
# 1. Get XML/View specific guidelines
python3 {SKILL_PATH}/scripts/search.py "xml viewbinding fragment" --platform android -n 5

# 2. Get Gradle dependencies needed
python3 {SKILL_PATH}/scripts/search.py "hilt room retrofit coil" --domain gradle -n 5

# 3. Get generic Android best practices
python3 {SKILL_PATH}/scripts/search.py "state lifecycle security" --platform android -n 5

# 4. Check anti-patterns to avoid
python3 {SKILL_PATH}/scripts/search.py "android xml fragment" --domain antipattern --filter-platform android

# 5. Get architecture guidance
python3 {SKILL_PATH}/scripts/search.py "mvvm clean architecture" --domain architecture
```

### Step 4: Generate Code

Use standard Android View System patterns. Follow the code generation rules below.

---

## Code Generation Rules

### Default Stack

```
Architecture:  MVVM + Clean Architecture + Repository Pattern
DI:            Hilt (@HiltViewModel, @Inject, @Module)
UI:            XML Layouts + Fragments + Activity
Binding:       ViewBinding (ActivityBinding, FragmentBinding)
State:         StateFlow + sealed interface UiState (collected in LifecycleScope)
Events:        Channel<Event> for one-shot (navigation, snackbar)
Navigation:    Jetpack Navigation Component (XML graphs)
Network:       Retrofit + Moshi + OkHttp
Database:      Room + KSP
Image:         Coil (load into ImageView)
Async:         Coroutines + Flow (viewModelScope, Dispatchers.IO)
Testing:       JUnit5 + MockK + Turbine + Espresso
Build:         Version Catalog (libs.versions.toml) + KSP
```

### Always Use ViewBinding

```kotlin
class HomeFragment : Fragment(R.layout.fragment_home) {
    private var _binding: FragmentHomeBinding? = null
    private val binding get() = _binding!!

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        _binding = FragmentHomeBinding.bind(view)
        
        // Use binding to access views
        binding.recyclerView.adapter = adapter
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null // Avoid memory leaks
    }
}
```

### Always Use sealed Interface for UiState

```kotlin
sealed interface HomeUiState {
    data object Loading : HomeUiState
    data class Success(val items: List<Item>) : HomeUiState
    data class Error(val message: String) : HomeUiState
    data object Empty : HomeUiState
}
```

### Always Collect Flow safely in Fragments

```kotlin
viewLifecycleOwner.lifecycleScope.launch {
    viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.uiState.collect { state ->
            // Update UI based on state
            when (state) {
                is HomeUiState.Loading -> binding.progressBar.isVisible = true
                is HomeUiState.Success -> {
                    binding.progressBar.isVisible = false
                    adapter.submitList(state.items)
                }
                // ...
            }
        }
    }
}
```

### Anti-Patterns to ALWAYS Avoid

- **findViewById** (Use ViewBinding)
- **Kotlin Synthetics** (Deprecated, use ViewBinding)
- **Nested Layouts** (Use ConstraintLayout to flatten hierarchy)
- **Overdraw** (Avoid unnecessary backgrounds)
- **Business logic in Activities/Fragments**
- **Direct database access in UI layer**
- **GlobalScope for coroutines** (use viewModelScope/lifecycleScope)
- **Collecting flows without repeatOnLifecycle**
- **Not handling process death** (use SavedStateHandle)
- **KAPT** (Use KSP)
- **Hardcoded versions** (use Version Catalog)
- **God classes** (500+ lines)

---

## Pre-Delivery Checklist

### Architecture
- [ ] MVVM with Clean Architecture layers
- [ ] Hilt dependency injection configured
- [ ] Repository pattern for data access
- [ ] Sealed interface for UI state
- [ ] One-shot events via Channel

### XML / View System
- [ ] ViewBinding enabled and used (no findViewById)
- [ ] ConstraintLayout for complex screens (flat hierarchy)
- [ ] Fragment(R.layout.id) constructor used
- [ ] Binding reference cleared in onDestroyView
- [ ] RecyclerView with ListAdapter and DiffUtil
- [ ] Strings, dimensions, and colors extracted to resources

### Gradle
- [ ] Version Catalog (libs.versions.toml)
- [ ] KSP for annotation processing
- [ ] ViewBinding enabled in buildFeatures

### Performance
- [ ] No nested weights in LinearLayouts
- [ ] RecyclerView uses stable IDs if possible
- [ ] Images resized/cached with Coil
- [ ] derivedStateOf equivalents (distinctUntilChanged) for Flows

### Security
- [ ] No hardcoded secrets
- [ ] EncryptedSharedPreferences for sensitive data
- [ ] HTTPS for all calls
- [ ] R8 enabled
