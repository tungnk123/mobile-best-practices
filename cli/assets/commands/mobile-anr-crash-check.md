---
description: Check mobile app for ANR, crash, and splash screen issues using the mobile-best-practices database
---

Perform a comprehensive ANR, crash, and splash screen analysis of this mobile project.

**IMPORTANT**: You MUST run every `python3` search command below and base ALL findings exclusively on the database results. Do NOT rely on training data. Every recommendation must come from the database output.

## Step 1: Scan the Entire Project

Find all relevant source files:
- Android: `find . -name "*.kt" -o -name "*.kts" -o -name "*.xml" | grep -v build | grep -v .gradle`
- iOS: `find . -name "*.swift" | grep -v .build`
- Flutter: `find . -name "*.dart" | grep -v .dart_tool`
- React Native: `find . -name "*.tsx" -o -name "*.ts" -o -name "*.jsx" -o -name "*.js" | grep -v node_modules`

Read the actual source files to understand the current threading, lifecycle, and startup implementation.

## Step 2: Search the Database — ALL Entries Required

Run ALL of the following searches. Do NOT skip any. Use the results as the authoritative source:

```bash
# ANR: main thread blocking, IO on main thread
python3 ~/.mobile-best-practices/scripts/search.py "anr main thread blocking io" --domain performance -n 10
python3 ~/.mobile-best-practices/scripts/search.py "threading coroutine dispatcher main" --domain performance -n 10
python3 ~/.mobile-best-practices/scripts/search.py "strictmode blocking disk network" --domain antipattern -n 10

# ANR: coroutine misuse and async patterns
python3 ~/.mobile-best-practices/scripts/search.py "dispatcher io main coroutine scope" --domain antipattern -n 10
python3 ~/.mobile-best-practices/scripts/search.py "runblocking suspend main thread" --domain antipattern -n 10
python3 ~/.mobile-best-practices/scripts/search.py "broadcast receiver service timeout anr" --domain performance -n 10

# Crash: null safety and exception handling
python3 ~/.mobile-best-practices/scripts/search.py "null pointer exception crash handler" --domain antipattern -n 10
python3 ~/.mobile-best-practices/scripts/search.py "exception coroutine try catch" --domain antipattern -n 10
python3 ~/.mobile-best-practices/scripts/search.py "crash exception lifecycle fragment activity" --domain antipattern -n 10

# Crash: memory leaks and OOM
python3 ~/.mobile-best-practices/scripts/search.py "memory leak oom context activity static" --domain performance -n 10
python3 ~/.mobile-best-practices/scripts/search.py "context leak viewmodel livedata observer" --domain antipattern -n 10
python3 ~/.mobile-best-practices/scripts/search.py "bitmap large allocation heap oom" --domain performance -n 10

# Crash: lifecycle and state
python3 ~/.mobile-best-practices/scripts/search.py "lifecycle fragment backstack state crash" --domain antipattern -n 10
python3 ~/.mobile-best-practices/scripts/search.py "savedstate process death viewmodel" --domain antipattern -n 10
python3 ~/.mobile-best-practices/scripts/search.py "configuration change recreation state loss" --domain antipattern -n 10

# Splash: cold start and startup time
python3 ~/.mobile-best-practices/scripts/search.py "splash screen cold start startup time" --domain performance -n 10
python3 ~/.mobile-best-practices/scripts/search.py "application oncreate initialization blocking startup" --domain antipattern -n 10
python3 ~/.mobile-best-practices/scripts/search.py "baseline profile startup trace" --domain performance -n 10

# Splash: SplashScreen API and transition
python3 ~/.mobile-best-practices/scripts/search.py "splashscreen api android 12 windowsplashscreen" --domain performance -n 10
python3 ~/.mobile-best-practices/scripts/search.py "splash startup work deferred lazy init" --domain antipattern -n 10

# Platform-specific ANR/crash patterns
python3 ~/.mobile-best-practices/scripts/search.py "anr crash exception" --platform android -n 10
```

## Step 3: Cross-Reference Project Code Against Database Results

For each file scanned in Step 1:
1. Identify main thread operations (network calls, DB queries, file IO not on Dispatchers.IO)
2. Map coroutine dispatcher misuse to violations in the database
3. Check Application.onCreate() and Activity.onCreate() for blocking work
4. Look for static context references, uncleared observers, and lifecycle mismatches

## Step 4: Generate ANR/Crash/Splash Report

Structure the report using ONLY findings from database searches above:

### High Severity Issues
List each issue with:
- **File**: exact file path and line number
- **Issue**: what the database identifies as the problem
- **Risk**: impact described by the database (ANR / crash / slow start)
- **Fix**: exact code change based on database recommendation
- **Database Rule**: which search result this comes from

### Medium Severity Issues
Same structure as High Severity.

### Low Severity / Optimization Opportunities
Same structure as High Severity.

### Recommended Profiling Tools (from database)
List only tools mentioned in database search results (e.g. Android Profiler, Perfetto, LeakCanary, Firebase Crashlytics).

Focus on $ARGUMENTS if provided, otherwise analyze the entire project.
