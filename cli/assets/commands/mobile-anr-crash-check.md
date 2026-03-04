---
description: Check mobile app for ANR, crash, and splash screen issues
---

Perform a comprehensive ANR, crash, and splash screen analysis of my mobile application:

1. **Check for ANR Causes**:
   - Identify main thread blocking operations (network, disk, database calls)
   - Review coroutine dispatcher usage (IO work on Dispatchers.Main)
   - Check for StrictMode violations
   - Look for deadlocks or long-running synchronous operations
   - Review BroadcastReceiver and Service timeout risks

2. **Check for Crash Patterns**:
   - Find unhandled NullPointerException / null safety issues
   - Review lifecycle-related crashes (Fragment back stack, Activity recreation)
   - Check for OutOfMemoryError from memory leaks or large allocations
   - Look for context leaks (static references to Activity/Fragment)
   - Review exception handling in coroutines and callbacks
   - Check for crashes specific to Android version compatibility

3. **Check for Splash Screen Issues**:
   - Review cold start time and blocking initialization in Application.onCreate()
   - Check SplashScreen API usage (Android 12+ compatibility)
   - Identify heavy work done before the first frame is drawn
   - Review Baseline Profiles and startup trace configuration
   - Check for splash screen → main activity transition issues

4. **Review Against Best Practices**:
   - Use the mobile-best-practices skill to search performance domain for ANR/startup rules
   - Use the mobile-best-practices skill to search antipattern domain for crash patterns
   - Check platform-specific guidelines for threading and lifecycle

5. **Generate ANR/Crash/Splash Report**:
   - List all issues found with severity ratings (high/medium/low)
   - Provide fix recommendations with code examples
   - Suggest profiling tools (Android Profiler, Perfetto, LeakCanary, Firebase Crashlytics)
   - Reference relevant documentation

Focus on $ARGUMENTS if provided, otherwise analyze the entire project.
