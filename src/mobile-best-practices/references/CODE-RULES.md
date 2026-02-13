# Code Generation Rules

When generating mobile code, ALWAYS follow these rules.

## Android Default Stack (Jetpack Compose)

```
Architecture:  MVVM + Clean Architecture + Repository Pattern
DI:            Hilt (@HiltViewModel, @Inject, @Module)
UI:            Jetpack Compose + Material3
State:         StateFlow + sealed interface UiState
Events:        Channel<Event> for one-shot (navigation, snackbar)
Navigation:    Navigation Compose with @Serializable type-safe routes
Network:       Retrofit + Moshi + OkHttp
Database:      Room + KSP
Image:         Coil (AsyncImage)
Async:         Coroutines + Flow (viewModelScope, Dispatchers.IO)
Testing:       JUnit5 + MockK + Turbine + Compose Test
Build:         Version Catalog (libs.versions.toml) + KSP
```

## Always Use Sealed Interface for UiState

```kotlin
sealed interface HomeUiState {
    data object Loading : HomeUiState
    data class Success(val items: List<Item>) : HomeUiState
    data class Error(val message: String) : HomeUiState
    data object Empty : HomeUiState
}
```

## Always Use @HiltViewModel Pattern

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

## Always Use collectAsStateWithLifecycle

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

## Follow Platform Conventions

| Platform | Stack |
|----------|-------|
| **Android** | Jetpack Compose + Hilt + Room + Retrofit + Coil + Navigation Compose |
| **iOS** | SwiftUI + Combine/async-await + SwiftData/CoreData + URLSession + Kingfisher |
| **Flutter** | BLoC/Riverpod + Dio + Drift/Hive + GoRouter + CachedNetworkImage |
| **React Native** | Redux Toolkit/Zustand + Axios/React Query + MMKV + React Navigation + FastImage |

## Anti-Patterns to ALWAYS Avoid

**All Platforms:**
- God classes (500+ lines)
- Hardcoded strings/colors
- No error handling
- Memory leaks
- Blocking main thread
- Hardcoded API keys
- Storing secrets in plain preferences/UserDefaults
- No tests

**Android Specific:**
- Business logic in Activities/Fragments
- Direct database access in UI layer
- GlobalScope for coroutines (use viewModelScope)
- collectAsState without lifecycle (use collectAsStateWithLifecycle)
- Not handling process death (use SavedStateHandle)
- KAPT instead of KSP (KSP is 2x faster)
- Hardcoded versions in build.gradle (use Version Catalog)
- Toast for user feedback (use Snackbar with SnackbarHostState)

**iOS Specific:**
- Force unwrapping optionals (!!)
- Retain cycles in closures (missing [weak self])
- @ObservedObject for ViewModel creation (use @StateObject)
- NavigationView instead of NavigationStack

**Flutter Specific:**
- setState for complex state management
- Business logic in build methods
- Not disposing controllers
- Non-const constructors for static widgets
- Column/Row instead of LazyColumn for long lists

**React Native Specific:**
- Prop drilling through many layers
- Missing useEffect cleanup
- Missing useEffect dependencies
- ScrollView for long lists (use FlatList/FlashList)
- Inline styles in render (use StyleSheet.create)
