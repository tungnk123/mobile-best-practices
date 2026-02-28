---
description: Analyze mobile app for performance issues using the mobile-best-practices database
---

Perform a comprehensive performance analysis of this mobile project.

**IMPORTANT**: You MUST run every `python3` search command below and base ALL findings exclusively on the database results. Do NOT rely on training data. Every recommendation must come from the database output.

## Step 1: Scan the Entire Project

Find all relevant source files:
- Android: `find . -name "*.kt" -o -name "*.kts" -o -name "*.xml" | grep -v build | grep -v .gradle`
- iOS: `find . -name "*.swift" | grep -v .build`
- Flutter: `find . -name "*.dart" | grep -v .dart_tool`
- React Native: `find . -name "*.tsx" -o -name "*.ts" -o -name "*.jsx" -o -name "*.js" | grep -v node_modules`

Read the actual source files to understand the current implementation.

## Step 2: Search the Database — ALL Entries Required

Run ALL of the following searches. Do NOT skip any. Use the results as the authoritative source:

```bash
# Core performance rules — ALL platforms
python3 ~/.mobile-best-practices/scripts/search.py "startup cold warm launch" --domain performance -n 15
python3 ~/.mobile-best-practices/scripts/search.py "memory leak allocation heap" --domain performance -n 15
python3 ~/.mobile-best-practices/scripts/search.py "ui rendering frame drop jank" --domain performance -n 15
python3 ~/.mobile-best-practices/scripts/search.py "image loading cache bitmap" --domain performance -n 15
python3 ~/.mobile-best-practices/scripts/search.py "network http caching request" --domain performance -n 15
python3 ~/.mobile-best-practices/scripts/search.py "battery cpu wakelock background" --domain performance -n 15
python3 ~/.mobile-best-practices/scripts/search.py "list scroll lazy virtualize" --domain performance -n 15
python3 ~/.mobile-best-practices/scripts/search.py "database query index room" --domain performance -n 15
python3 ~/.mobile-best-practices/scripts/search.py "threading coroutine main dispatcher" --domain performance -n 15
python3 ~/.mobile-best-practices/scripts/search.py "apk size binary proguard shrink" --domain performance -n 10

# Android-specific performance
python3 ~/.mobile-best-practices/scripts/search.py "recomposition compose lambda" --domain performance --filter-platform android -n 15
python3 ~/.mobile-best-practices/scripts/search.py "derivedStateOf remember stable" --domain performance --filter-platform android -n 15
python3 ~/.mobile-best-practices/scripts/search.py "baseline profile startup trace" --domain performance --filter-platform android -n 10
python3 ~/.mobile-best-practices/scripts/search.py "viewmodel stateflow flow" --platform android -n 10

# iOS-specific performance
python3 ~/.mobile-best-practices/scripts/search.py "swiftui view body redraw" --domain performance --filter-platform ios -n 15
python3 ~/.mobile-best-practices/scripts/search.py "instruments time profiler" --domain performance --filter-platform ios -n 10

# Flutter-specific performance
python3 ~/.mobile-best-practices/scripts/search.py "widget rebuild const build" --domain performance --filter-platform flutter -n 15
python3 ~/.mobile-best-practices/scripts/search.py "flutter devtools timeline" --domain performance --filter-platform flutter -n 10

# React Native-specific performance
python3 ~/.mobile-best-practices/scripts/search.py "flatlist keyExtractor memo" --domain performance --filter-platform react-native -n 15
python3 ~/.mobile-best-practices/scripts/search.py "bridge hermes turbo module" --domain performance --filter-platform react-native -n 10

# Performance-related anti-patterns
python3 ~/.mobile-best-practices/scripts/search.py "performance anti-pattern slow blocking" --domain antipattern -n 15
python3 ~/.mobile-best-practices/scripts/search.py "memory leak context activity" --domain antipattern -n 10

# Platform-specific performance guidelines
python3 ~/.mobile-best-practices/scripts/search.py "performance optimize" --platform android -n 10
python3 ~/.mobile-best-practices/scripts/search.py "performance optimize" --platform ios -n 10
python3 ~/.mobile-best-practices/scripts/search.py "performance optimize" --platform flutter -n 10
python3 ~/.mobile-best-practices/scripts/search.py "performance optimize" --platform react-native -n 10
```

## Step 3: Cross-Reference Project Code Against Database Results

For each file scanned in Step 1:
1. Map patterns found in code to violations identified in the database results
2. Identify missing optimizations the database recommends

## Step 4: Generate Performance Report

Structure the report using ONLY findings from database searches above:

### Critical Issues (High Severity)
List each issue with:
- **File**: exact file path and line number
- **Issue**: what the database says is wrong
- **Fix**: exact code change based on database recommendation
- **Database Rule**: which search result this comes from

### Warnings (Medium Severity)
Same structure as Critical Issues.

### Optimization Opportunities (Low Severity)
Same structure as Critical Issues.

### Profiling Tools (from database)
List only tools mentioned in database search results.

Focus on $ARGUMENTS if provided, otherwise analyze the entire project.
