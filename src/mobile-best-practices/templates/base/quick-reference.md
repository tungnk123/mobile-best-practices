# Quick Reference

## Search Examples

```bash
# Code snippets (Android)
python3 {SKILL_PATH}/scripts/search.py "viewmodel hilt" --domain snippet

# Gradle dependencies
python3 {SKILL_PATH}/scripts/search.py "compose room hilt" --domain gradle -n 5

# Architecture
python3 {SKILL_PATH}/scripts/search.py "mvvm clean architecture" --domain architecture

# Platform guidelines
python3 {SKILL_PATH}/scripts/search.py "compose state" --platform android

# Anti-patterns
python3 {SKILL_PATH}/scripts/search.py "android compose" --domain antipattern

# Performance
python3 {SKILL_PATH}/scripts/search.py "startup recomposition" --domain performance

# Security
python3 {SKILL_PATH}/scripts/search.py "encryption token storage" --domain security

# Product recommendation
python3 {SKILL_PATH}/scripts/search.py "e-commerce" --domain reasoning
```

## Anti-Patterns to ALWAYS Avoid

**All Platforms:** God classes, hardcoded strings/colors, no error handling, memory leaks, blocking main thread, hardcoded API keys, no tests.

**Android:** Business logic in Activities, GlobalScope, collectAsState (use collectAsStateWithLifecycle), KAPT (use KSP), Toast (use Snackbar).

**iOS:** Force unwrapping (!!), retain cycles ([weak self]), @ObservedObject for creation (use @StateObject).

**Flutter:** setState for complex state, logic in build(), not disposing controllers, non-const constructors.

**React Native:** Prop drilling, missing useEffect cleanup/deps, ScrollView for long lists.
