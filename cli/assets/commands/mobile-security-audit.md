---
description: Audit mobile app for security vulnerabilities using the mobile-best-practices database
---

Perform a comprehensive security audit of this mobile project.

**IMPORTANT**: You MUST run every `python3` search command below and base ALL findings exclusively on the database results. Do NOT rely on training data. Every vulnerability and recommendation must come from the database output.

## Step 1: Scan the Entire Project

Find all relevant source files:
- Android: `find . -name "*.kt" -o -name "*.kts" -o -name "*.xml" -o -name "*.gradle" -o -name "*.json" -o -name "*.properties" | grep -v build | grep -v .gradle`
- iOS: `find . -name "*.swift" -o -name "*.plist" -o -name "*.entitlements" | grep -v .build`
- Flutter: `find . -name "*.dart" -o -name "*.yaml" -o -name "AndroidManifest.xml" -o -name "*.plist" | grep -v .dart_tool`
- React Native: `find . -name "*.tsx" -o -name "*.ts" -o -name "*.js" -o -name "*.json" | grep -v node_modules`

Read the actual source files to understand the current security implementation.

## Step 2: Search the Database — ALL Entries Required

Run ALL of the following searches. Do NOT skip any. Use the results as the authoritative source:

```bash
# Authentication & session security
python3 ~/.mobile-best-practices/scripts/search.py "authentication token session jwt biometric" --domain security -n 15
python3 ~/.mobile-best-practices/scripts/search.py "oauth login credential" --domain security -n 15
python3 ~/.mobile-best-practices/scripts/search.py "session management logout token revoke" --domain security -n 10

# Data storage security
python3 ~/.mobile-best-practices/scripts/search.py "keystore keychain encrypted storage" --domain security -n 15
python3 ~/.mobile-best-practices/scripts/search.py "sharedpreferences userdefaults plaintext sensitive" --domain security -n 15
python3 ~/.mobile-best-practices/scripts/search.py "api key secret hardcoded credential" --domain security -n 15
python3 ~/.mobile-best-practices/scripts/search.py "encryption aes rsa cipher" --domain security -n 15

# Network security
python3 ~/.mobile-best-practices/scripts/search.py "ssl tls certificate pinning network" --domain security -n 15
python3 ~/.mobile-best-practices/scripts/search.py "https cleartext man-in-the-middle" --domain security -n 15
python3 ~/.mobile-best-practices/scripts/search.py "network security config trust anchor" --domain security -n 10

# Logging & data exposure
python3 ~/.mobile-best-practices/scripts/search.py "log logcat sensitive data leak" --domain security -n 15
python3 ~/.mobile-best-practices/scripts/search.py "crash report analytics pii" --domain security -n 10
python3 ~/.mobile-best-practices/scripts/search.py "clipboard screenshot task switcher" --domain security -n 10

# Code & binary security
python3 ~/.mobile-best-practices/scripts/search.py "root jailbreak detection bypass" --domain security -n 15
python3 ~/.mobile-best-practices/scripts/search.py "obfuscation proguard r8 minify" --domain security -n 10
python3 ~/.mobile-best-practices/scripts/search.py "tamper detection integrity" --domain security -n 10
python3 ~/.mobile-best-practices/scripts/search.py "reverse engineering decompile apk" --domain security -n 10

# Input & injection
python3 ~/.mobile-best-practices/scripts/search.py "input validation injection sql xss" --domain security -n 15
python3 ~/.mobile-best-practices/scripts/search.py "intent deeplink url scheme" --domain security -n 15
python3 ~/.mobile-best-practices/scripts/search.py "webview javascript interface" --domain security -n 15

# Permissions & privacy
python3 ~/.mobile-best-practices/scripts/search.py "permission runtime privacy gdpr" --domain security -n 15
python3 ~/.mobile-best-practices/scripts/search.py "location camera microphone background" --domain security -n 10

# Platform-specific security
python3 ~/.mobile-best-practices/scripts/search.py "android manifest exported broadcast" --domain security --filter-platform android -n 15
python3 ~/.mobile-best-practices/scripts/search.py "content provider sql injection cursor" --domain security --filter-platform android -n 10
python3 ~/.mobile-best-practices/scripts/search.py "ios ats app transport security" --domain security --filter-platform ios -n 15
python3 ~/.mobile-best-practices/scripts/search.py "keychain access group entitlements" --domain security --filter-platform ios -n 10
python3 ~/.mobile-best-practices/scripts/search.py "flutter dart secure storage plugin" --domain security --filter-platform flutter -n 15
python3 ~/.mobile-best-practices/scripts/search.py "react native async storage bridge" --domain security --filter-platform react-native -n 15

# OWASP Mobile Top 10 coverage
python3 ~/.mobile-best-practices/scripts/search.py "improper platform usage" --domain security -n 10
python3 ~/.mobile-best-practices/scripts/search.py "insecure data storage" --domain security -n 10
python3 ~/.mobile-best-practices/scripts/search.py "insufficient cryptography" --domain security -n 10
python3 ~/.mobile-best-practices/scripts/search.py "insecure authentication" --domain security -n 10
python3 ~/.mobile-best-practices/scripts/search.py "binary protection" --domain security -n 10

# Platform guidelines for security
python3 ~/.mobile-best-practices/scripts/search.py "security" --platform android -n 10
python3 ~/.mobile-best-practices/scripts/search.py "security" --platform ios -n 10
python3 ~/.mobile-best-practices/scripts/search.py "security" --platform flutter -n 10
python3 ~/.mobile-best-practices/scripts/search.py "security" --platform react-native -n 10
```

## Step 3: Cross-Reference Project Code Against Database Results

For each file scanned in Step 1:
1. Search for hardcoded secrets, API keys, and credentials
2. Map insecure patterns found in code to vulnerabilities identified in the database
3. Check Manifest/Info.plist/pubspec/package.json for misconfigurations

## Step 4: Generate Security Audit Report

Structure the report using ONLY findings from database searches above:

### High Severity Vulnerabilities
List each vulnerability with:
- **File**: exact file path and line number
- **Vulnerability**: what the database identifies as the issue
- **Risk**: impact described by the database
- **Remediation**: exact fix based on database recommendation
- **OWASP Category**: if applicable
- **Database Rule**: which search result this comes from

### Medium Severity Vulnerabilities
Same structure as High Severity.

### Low Severity / Best Practice Gaps
Same structure as High Severity.

### Security Checklist (from database)
Checklist items drawn directly from database search results, checked against the project.

Focus on $ARGUMENTS if provided, otherwise audit the entire project.
