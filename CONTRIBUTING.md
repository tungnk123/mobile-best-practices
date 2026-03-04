# Contributing to Mobile Best Practices

Thanks for helping grow the database! Contributions are welcome — new entries, fixes to existing ones, or improvements to the search engine and CLI.

---

## Quick Start

```bash
git clone https://github.com/tungnk123/mobile-best-practices
cd mobile-best-practices
python3 --version  # requires Python 3.x
```

Test the search engine works:

```bash
python3 src/mobile-best-practices/scripts/search.py "viewmodel hilt" --domain snippet -n 3
```

---

## Project Structure

```
src/mobile-best-practices/
├── data/                   ← Edit CSVs here (source of truth)
│   ├── anti-patterns.csv
│   ├── performance.csv
│   ├── security.csv
│   ├── code-snippets.csv
│   ├── gradle-deps.csv
│   ├── architectures.csv
│   ├── design-patterns.csv
│   ├── libraries.csv
│   ├── ui-patterns.csv
│   ├── testing.csv
│   ├── reasoning-rules.csv
│   ├── project-templates.csv
│   └── platforms/
│       ├── android.csv     ← Android/Compose guidelines
│       ├── ios.csv
│       ├── flutter.csv
│       └── react-native.csv
├── scripts/
│   ├── core.py             ← BM25 search engine (rarely needs editing)
│   └── search.py           ← CLI interface
└── references/
    ├── CODE-RULES.md
    └── CHECKLIST.md
```

> **Note:** Changes to `src/mobile-best-practices/data/` are auto-available via symlinks in `.claude/skills/`. You do not need to copy files.

---

## How to Add Entries

### 1. Anti-Patterns (`data/anti-patterns.csv`)

Columns: `Name, Platform, Category, Severity, Keywords, Description, Bad Example, Good Example, Why Bad, Fix, Reference URL`

| Column | Values | Notes |
|--------|--------|-------|
| `Platform` | `Android` \| `iOS` \| `Flutter` \| `React Native` \| `All` | |
| `Severity` | `Critical` \| `High` \| `Medium` \| `Low` | |
| `Keywords` | space-separated lowercase | Used by BM25 search — be specific |
| `Bad Example` | one-liner code or description | No newlines in CSV field |
| `Good Example` | one-liner code or description | |
| `Reference URL` | official docs URL | Required |

**Example row:**
```
Coroutine on Main Thread,Android,Threading,Critical,"runblocking coroutine main thread block","Using runBlocking on main thread blocks UI","runBlocking { api.fetch() }","viewModelScope.launch { withContext(Dispatchers.IO) { api.fetch() } }","Blocks main thread causing ANR after 5s","Replace runBlocking with viewModelScope.launch + Dispatchers.IO",https://kotlinlang.org/docs/coroutines-basics.html
```

---

### 2. Performance Rules (`data/performance.csv`)

Columns: `Category, Issue, Platform, Severity, Keywords, Description, Do, Dont, Code Good, Code Bad, Metric, Reference URL`

| Column | Notes |
|--------|-------|
| `Category` | e.g. `Threading`, `Rendering`, `Startup`, `Memory`, `Network` |
| `Metric` | Measurable target, e.g. `< 16ms per frame`, `< 0.47% ANR rate` |
| `Code Good` / `Code Bad` | Short one-liner snippets |

---

### 3. Security Practices (`data/security.csv`)

Columns: `Category, Threat, Platform, Severity, Keywords, Description, Mitigation, Code Good, Code Bad, OWASP Ref, Reference URL`

| Column | Notes |
|--------|-------|
| `OWASP Ref` | e.g. `M1 - Improper Platform Usage`, `M2 - Insecure Data Storage` (optional) |
| `Mitigation` | Concrete fix, not vague advice |

---

### 4. Code Snippets (`data/code-snippets.csv`)

Columns: `ID, Name, Platform, Category, Keywords, Description, Code, Imports, Notes, Reference URL`

| Column | Notes |
|--------|-------|
| `ID` | `snake_case` unique identifier, e.g. `room_database_setup` |
| `Code` | Use `\n` for line breaks within the CSV field (keep in double quotes) |
| `Imports` | Full import statements, `\n`-separated |

**Example:**
```
room_database,"Room Database Setup",Android,Database,"room database dao entity","Room database with DAO and Entity","@Database(entities = [User::class] version = 1)\nabstract class AppDatabase : RoomDatabase() {\n    abstract fun userDao(): UserDao\n}","import androidx.room.Database\nimport androidx.room.RoomDatabase","Use KSP not KAPT. Enable exportSchema = true.",https://developer.android.com/training/data-storage/room
```

---

### 5. Gradle Dependencies (`data/gradle-deps.csv`)

Columns: `Name, Category, Keywords, Version Catalog Key, Implementation, KSP/KAPT, Version, Notes, Reference URL`

| Column | Notes |
|--------|-------|
| `Version Catalog Key` | The `libs.xxx` key used in `build.gradle.kts` |
| `Implementation` | Full `implementation(...)` line |
| `KSP/KAPT` | KSP annotation processor line if needed (leave empty otherwise) |
| `Version` | Latest stable version at time of entry |

---

### 6. Platform Guidelines (`data/platforms/android.csv`, `ios.csv`, etc.)

Columns: `Category, Guideline, Description, Do, Dont, Code Good, Code Bad, Severity, Docs URL`

These are the most impactful entries for day-to-day AI-assisted coding. Focus on:
- Specific API usage patterns (e.g. `collectAsStateWithLifecycle` vs `collectAsState`)
- Platform idioms that AI assistants commonly get wrong
- Version-specific behavior (e.g. Android 12+ SplashScreen API)

---

## CSV Conventions

- **Delimiter:** comma (`,`)
- **Multi-value fields:** pipe-separated (`Kotlin|Compose|Hilt`)
- **Code in CSV:** inline one-liners preferred; use `\n` for multiline (field must be double-quoted)
- **Keywords:** lowercase, space-separated, include synonyms (e.g. `anr main thread block freeze`)
- **No trailing spaces** in any field
- **Reference URL:** must be a real, working URL to official docs, GitHub, or a recognized guide

---

## Quality Bar

Before submitting, verify:

- [ ] The entry does not duplicate an existing one (search first: `python3 scripts/search.py "<your keywords>" --domain <domain>`)
- [ ] `Reference URL` links to an official or authoritative source
- [ ] `Bad Example` and `Good Example` are concrete (actual code or specific API names, not vague descriptions)
- [ ] `Keywords` field includes terms a developer would naturally search for
- [ ] Severity is accurate: `Critical` = data loss / crash / ANR / security breach; `High` = significant user impact; `Medium` = code quality; `Low` = style / preference

---

## Submitting

```bash
# 1. Create a branch
git checkout -b feat/add-<topic>-entries

# 2. Edit the relevant CSV(s) in src/mobile-best-practices/data/

# 3. Test your entries appear in search
python3 src/mobile-best-practices/scripts/search.py "<your keywords>" --domain <domain> -n 5

# 4. Commit
git add src/mobile-best-practices/data/
git commit -m "feat: add <topic> entries to <domain>"

# 5. Push and open a PR
git push -u origin feat/add-<topic>-entries
gh pr create
```

---

## What's Most Needed

Current gap areas — contributions especially welcome:

| Platform | Current | Target |
|----------|---------|--------|
| iOS (SwiftUI, Swift concurrency, SwiftData) | 60 | 150+ |
| Flutter (Riverpod, GoRouter, Drift) | 54 | 120+ |
| React Native (Expo, MMKV, Reanimated) | 55 | 120+ |

Android is well-covered (423 entries). iOS, Flutter, and React Native need depth.

---

## Questions?

Open an issue or start a discussion on GitHub.
