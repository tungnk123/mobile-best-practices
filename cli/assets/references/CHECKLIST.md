# Pre-Delivery Checklist

Before delivering mobile code, verify all applicable items.

## Architecture
- [ ] Proper separation of concerns (UI / ViewModel / Repository / DataSource)
- [ ] Dependency injection configured (Hilt for Android)
- [ ] Repository pattern for data access
- [ ] Sealed interface for UI state (Loading, Success, Error, Empty)
- [ ] One-shot events via Channel (not SharedFlow replay=0)

## Compose (Android)
- [ ] collectAsStateWithLifecycle (NOT collectAsState)
- [ ] LazyColumn with stable keys and contentType
- [ ] rememberSaveable for user input state
- [ ] Proper Modifier ordering (clickable before padding)
- [ ] Material3 components (Scaffold, TopAppBar, NavigationBar)
- [ ] @Preview for all screens with sample data

## Gradle (Android)
- [ ] Version Catalog (libs.versions.toml) for all dependencies
- [ ] Compose BOM managing Compose versions
- [ ] KSP for annotation processing (not KAPT)
- [ ] Correct configurations (implementation vs api vs testImplementation)

## Performance
- [ ] Lists use lazy/virtualized components with keys
- [ ] Images cached and sized appropriately (Coil with size())
- [ ] No work on main thread (network, DB, heavy computation)
- [ ] derivedStateOf for computed values

## Security
- [ ] No hardcoded secrets/API keys
- [ ] Sensitive data in secure storage (EncryptedSharedPreferences/Keychain)
- [ ] HTTPS for all network calls
- [ ] Input validation on user inputs
- [ ] R8/ProGuard enabled for release builds

## Testing
- [ ] Unit tests for ViewModels (runTest + Turbine + MockK)
- [ ] Mocked dependencies in tests
- [ ] Error states tested
- [ ] Compose UI tests for critical screens

## Accessibility
- [ ] contentDescription on Images and IconButtons
- [ ] Sufficient color contrast
- [ ] Touch targets minimum 48dp
- [ ] Screen reader navigation works
