---
description: Set up a new Android project with best practices using the mobile-best-practices database
---

Set up a new Android project following mobile development best practices.

**IMPORTANT**: You MUST run every `python3` search command below and base ALL decisions exclusively on the database results. Do NOT rely on training data. Every architectural choice, dependency, and code template must come from the database output.

## Step 1: Determine App Type

App type from arguments: $ARGUMENTS

If not specified, ask the user for: app type (e-commerce, banking, social media, healthcare, delivery, fitness, education, chat), target Android min SDK, and any required features.

## Step 2: Search the Database — ALL Entries Required

Run ALL of the following searches. Do NOT skip any:

```bash
# Reasoning: get product-type specific recommendations
python3 ~/.mobile-best-practices/scripts/search.py "$ARGUMENTS" --domain reasoning -n 5
python3 ~/.mobile-best-practices/scripts/search.py "android app type recommendation" --domain reasoning -n 5

# Architecture patterns
python3 ~/.mobile-best-practices/scripts/search.py "mvvm clean architecture repository" --domain architecture -n 10
python3 ~/.mobile-best-practices/scripts/search.py "mvi android unidirectional" --domain architecture -n 5
python3 ~/.mobile-best-practices/scripts/search.py "modularization multi-module feature" --domain architecture -n 5

# Code snippets — get ALL templates
python3 ~/.mobile-best-practices/scripts/search.py "viewmodel hilt stateflow" --domain snippet -n 10
python3 ~/.mobile-best-practices/scripts/search.py "repository datasource usecase" --domain snippet -n 10
python3 ~/.mobile-best-practices/scripts/search.py "compose screen navigation route" --domain snippet -n 10
python3 ~/.mobile-best-practices/scripts/search.py "room database dao entity" --domain snippet -n 10
python3 ~/.mobile-best-practices/scripts/search.py "retrofit okhttp service" --domain snippet -n 10
python3 ~/.mobile-best-practices/scripts/search.py "hilt module provides inject" --domain snippet -n 10
python3 ~/.mobile-best-practices/scripts/search.py "datastore preferences flow" --domain snippet -n 5
python3 ~/.mobile-best-practices/scripts/search.py "paging compose lazycolumn" --domain snippet -n 5
python3 ~/.mobile-best-practices/scripts/search.py "workmanager background sync" --domain snippet -n 5
python3 ~/.mobile-best-practices/scripts/search.py "theme material3 color scheme" --domain snippet -n 5

# Gradle dependencies — get ALL declarations
python3 ~/.mobile-best-practices/scripts/search.py "compose bom material3" --domain gradle -n 10
python3 ~/.mobile-best-practices/scripts/search.py "hilt dagger ksp" --domain gradle -n 10
python3 ~/.mobile-best-practices/scripts/search.py "room ksp database" --domain gradle -n 10
python3 ~/.mobile-best-practices/scripts/search.py "retrofit okhttp serialization" --domain gradle -n 10
python3 ~/.mobile-best-practices/scripts/search.py "coil image loading" --domain gradle -n 5
python3 ~/.mobile-best-practices/scripts/search.py "navigation compose" --domain gradle -n 5
python3 ~/.mobile-best-practices/scripts/search.py "paging3 compose" --domain gradle -n 5
python3 ~/.mobile-best-practices/scripts/search.py "junit mockk turbine testing" --domain gradle -n 10
python3 ~/.mobile-best-practices/scripts/search.py "datastore preferences" --domain gradle -n 5
python3 ~/.mobile-best-practices/scripts/search.py "workmanager" --domain gradle -n 5

# Android platform best practices
python3 ~/.mobile-best-practices/scripts/search.py "compose state lifecycle" --platform android -n 10
python3 ~/.mobile-best-practices/scripts/search.py "navigation type-safe serializable" --platform android -n 10
python3 ~/.mobile-best-practices/scripts/search.py "dependency injection hilt" --platform android -n 10
python3 ~/.mobile-best-practices/scripts/search.py "coroutine flow scope dispatcher" --platform android -n 10
python3 ~/.mobile-best-practices/scripts/search.py "version catalog toml" --platform android -n 5

# Anti-patterns to avoid from day one
python3 ~/.mobile-best-practices/scripts/search.py "android architecture anti-pattern" --domain antipattern --filter-platform android -n 15
python3 ~/.mobile-best-practices/scripts/search.py "compose recomposition god class" --domain antipattern --filter-platform android -n 10
python3 ~/.mobile-best-practices/scripts/search.py "memory leak context coroutine" --domain antipattern --filter-platform android -n 10

# Performance foundations
python3 ~/.mobile-best-practices/scripts/search.py "startup baseline profile" --domain performance --filter-platform android -n 10
python3 ~/.mobile-best-practices/scripts/search.py "compose lazy image cache" --domain performance --filter-platform android -n 10

# Security foundations
python3 ~/.mobile-best-practices/scripts/search.py "android keystore encrypted api key" --domain security --filter-platform android -n 10
python3 ~/.mobile-best-practices/scripts/search.py "network certificate pinning https" --domain security --filter-platform android -n 10

# Testing setup
python3 ~/.mobile-best-practices/scripts/search.py "unit test viewmodel coroutine turbine" --domain testing --filter-platform android -n 10
python3 ~/.mobile-best-practices/scripts/search.py "compose ui test espresso" --domain testing --filter-platform android -n 10

# UI patterns
python3 ~/.mobile-best-practices/scripts/search.py "compose scaffold navigation bottom" --domain ui --filter-platform android -n 10
python3 ~/.mobile-best-practices/scripts/search.py "material3 component theme" --domain ui --filter-platform android -n 10

# Project template
python3 ~/.mobile-best-practices/scripts/search.py "$ARGUMENTS android" --domain template -n 3
python3 ~/.mobile-best-practices/scripts/search.py "android compose mvvm" --domain template -n 3
```

## Step 3: Generate Project Structure

Using ONLY the database results above:

1. **Folder Structure** — based on architecture search results
2. **libs.versions.toml** — ALL dependencies from `gradle` domain results
3. **build.gradle.kts (app)** — using version catalog references from database
4. **Hilt Application class** — from snippet results
5. **DI modules** — from snippet results
6. **Base ViewModel** — from snippet results
7. **Repository template** — from snippet results
8. **Navigation graph** — from snippet results
9. **Theme setup** — from snippet results
10. **Network module** — from snippet results
11. **Database setup** — from snippet results

## Step 4: Apply Anti-Patterns Checklist

Before delivering, verify the project avoids ALL anti-patterns from the database results in Step 2.

Provide a complete, production-ready project structure with every file fully implemented.
