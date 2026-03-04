# Live Demo — Mobile Best Practices Search

All outputs below are **real results** from the database. Run them yourself:

```bash
python3 src/mobile-best-practices/scripts/search.py "<query>" --domain <domain> -n 3
```

---

## Code Snippets — Copy-paste Kotlin/Compose templates

**Query:** `viewmodel hilt`

```
python3 scripts/search.py "viewmodel hilt" --domain snippet -n 2
```

**Result 1 — Basic ViewModel**
```kotlin
@HiltViewModel
class HomeViewModel @Inject constructor(
    private val repository: HomeRepository
) : ViewModel() {

    private val _uiState = MutableStateFlow<HomeUiState>(HomeUiState.Loading)
    val uiState: StateFlow<HomeUiState> = _uiState.asStateFlow()

    init { loadData() }

    fun loadData() {
        viewModelScope.launch {
            _uiState.value = HomeUiState.Loading
            try {
                val data = repository.getData()
                _uiState.value = HomeUiState.Success(data)
            } catch (e: Exception) {
                _uiState.value = HomeUiState.Error(e.message ?: "Unknown error")
            }
        }
    }
}

sealed interface HomeUiState {
    data object Loading : HomeUiState
    data class Success(val items: List<Item>) : HomeUiState
    data class Error(val message: String) : HomeUiState
}
```

> Notes: Always use sealed interface for UiState. Expose immutable StateFlow.

---

## Performance — ANR detection and prevention

**Query:** `anr main thread blocking`

```
python3 scripts/search.py "anr main thread blocking" --domain performance -n 2
```

**Result 1 — Main Thread Blocking Detection** `Severity: Critical`
- **Do:** Use StrictMode in debug to detect violations; move work to IO dispatcher
- **Don't:** Perform blocking work on main thread
```kotlin
// Good
withContext(Dispatchers.IO) { database.query() }

// Bad
runBlocking { api.fetch() } // blocks main thread → ANR after 5s
```
> Metric: Zero main thread violations. ANR rate target: < 0.47%

---

## Security — SSL / Certificate Pinning

**Query:** `ssl certificate pinning`

```
python3 scripts/search.py "ssl certificate pinning" --domain security -n 2
```

**Result 1 — No SSL Pinning** `Severity: Critical`
- **Threat:** No certificate pinning allows MITM attacks
- **Mitigation:** Implement certificate or public key pinning
```kotlin
// Good
val pinner = CertificatePinner.Builder()
    .add("api.example.com", "sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=")
    .build()

// Bad
OkHttpClient() // trusts any valid cert — vulnerable to MITM
```

---

## Architecture — MVVM vs Clean Architecture

**Query:** `mvvm clean architecture`

```
python3 scripts/search.py "mvvm clean architecture" --domain architecture -n 1
```

**Result — Clean Architecture + MVI** `Complexity: High | Team: 5+`
- **Best For:** Enterprise Android apps needing clean layers + predictable state
- **Stack:** Kotlin | Compose | Hilt | Room | Retrofit | Flow | StateFlow
- **Layers:** `presentation/ui` → `presentation/mvi` → `domain/usecase` → `domain/model` → `data/repository` → `data/source`
- **Anti-patterns to avoid:** Overengineering, unnecessary UseCases, state explosion

---

## Gradle — Ready-to-paste dependency declarations

**Query:** `compose hilt room retrofit`

```
python3 scripts/search.py "compose hilt room retrofit" --domain gradle -n 3
```

**Results:**
```toml
# libs.versions.toml
[versions]
hilt = "2.51.1"
retrofit = "2.11.0"
room = "2.7.0"

[libraries]
hilt-navigation-compose = { module = "androidx.hilt:hilt-navigation-compose", version = "1.2.0" }
retrofit = { module = "com.squareup.retrofit2:retrofit", version.ref = "retrofit" }
room-runtime = { module = "androidx.room:room-runtime", version.ref = "room" }
```

```kotlin
// build.gradle.kts
implementation(libs.hilt.navigation.compose)  // hiltViewModel() in Compose
implementation(libs.retrofit)                 // Type-safe HTTP client
implementation(libs.room.runtime)             // Local database
```

---

## Anti-Patterns — Common mistakes to avoid

**Query:** `memory leak context activity static`

```
python3 scripts/search.py "memory leak context activity static" --domain antipattern -n 2
```

**Result — Static Context Reference** `Severity: Critical`
- **Bad:** `companion object { var ctx: Context? = null }` — holds Activity forever
- **Good:** Use `applicationContext` for app-level references; use `WeakReference` if needed
- **Why bad:** Activity cannot be GC'd → OOM crash on low-memory devices

---

## Audit Commands — Scan your entire project

These slash commands read your source files and map findings to database rules:

```bash
# Scan project for security vulnerabilities
/mobile-security-audit

# Scan for performance bottlenecks
/mobile-performance-check

# Check for ANR, crash, and slow startup causes
/mobile-anr-crash-check
```

Example output from `/mobile-anr-crash-check`:
```
### High Severity Issues

**File:** app/src/main/java/com/example/MainActivity.kt:42
**Issue:** runBlocking on main thread — database query blocks UI
**Risk:** ANR after 5 seconds
**Fix:** Move to viewModelScope.launch { withContext(Dispatchers.IO) { ... } }
**Database Rule:** Threading > ANR Prevention (Severity: Critical)
```

---

## All Domains

| Domain | Example Query | Entries |
|--------|--------------|---------|
| `snippet` | `viewmodel hilt room` | 80 |
| `gradle` | `compose bom hilt room` | 78 |
| `security` | `ssl pinning biometric keystore` | 437 |
| `performance` | `anr recomposition lazy startup` | 228 |
| `antipattern` | `memory leak god activity` | 120 |
| `architecture` | `mvvm clean mvi` | 49 |
| `designpattern` | `repository factory observer` | 117 |
| `ui` | `bottom navigation list sheet` | 91 |
| `library` | `retrofit coil hilt room` | 103 |
| `testing` | `viewmodel mockk turbine` | 73 |
| `reasoning` | `e-commerce banking social` | 56 |
| `template` | `android e-commerce starter` | 18 |
| `platform android` | `compose state lifecycle` | 423 |
| `platform ios` | `swiftui combine async` | 60 |
| `platform flutter` | `bloc riverpod gorouter` | 54 |
| `platform react-native` | `redux zustand navigation` | 55 |

**Total: 2,042 entries**

---

## Install

```bash
npx mobile-best-practices init --ai claude --platform android
```

[Full documentation →](README.md)
