#!/usr/bin/env python3
"""
Validate all CSV files:
  - Required columns present
  - Minimum row count
  - No empty required fields
  - Severity values are valid
  - Keywords field is non-empty
  - No duplicate entries (by Name or ID)
  - Reference URL / Docs URL present for each row
  - Source URL present for Android snippets (cs.android.com)
"""

import csv
import sys
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "src" / "mobile-best-practices" / "data"

VALID_SEVERITY = {"Critical", "High", "Medium", "Low"}
VALID_PLATFORMS = {"Android", "iOS", "Flutter", "React Native", "All", "KMP", ""}

EXPECTED = {
    "architectures.csv": {
        "required": ["Name", "Platform", "Complexity", "Keywords", "Best For", "Tech Stack"],
        "min_rows": 20,
        "url_col": "Reference URL",
        "severity_col": None,
        "dedup_col": "Name",
    },
    "libraries.csv": {
        "required": ["Name", "Platform", "Category", "Keywords", "Description"],
        "min_rows": 50,
        "url_col": "Reference URL",
        "severity_col": None,
        "dedup_col": "Name",
    },
    "ui-patterns.csv": {
        "required": ["Pattern Name", "Platform", "Category", "Keywords", "Use Case"],
        "min_rows": 50,
        "url_col": "Reference URL",
        "severity_col": None,
        "dedup_col": "Pattern Name",
    },
    "anti-patterns.csv": {
        "required": ["Name", "Platform", "Category", "Severity", "Description", "Fix"],
        "min_rows": 50,
        "url_col": "Reference URL",
        "severity_col": "Severity",
        "dedup_col": "Name",
    },
    "performance.csv": {
        "required": ["Category", "Issue", "Platform", "Severity", "Description", "Do", "Dont"],
        "min_rows": 40,
        "url_col": "Reference URL",
        "severity_col": "Severity",
        "dedup_col": "Issue",
    },
    "security.csv": {
        "required": ["Category", "Threat", "Platform", "Severity", "Description", "Mitigation"],
        "min_rows": 30,
        "url_col": "Reference URL",
        "severity_col": "Severity",
        "dedup_col": "Threat",
    },
    "testing.csv": {
        "required": ["Category", "Pattern", "Platform", "Description"],
        "min_rows": 30,
        "url_col": "Reference URL",
        "severity_col": None,
        "dedup_col": "Pattern",
    },
    "reasoning-rules.csv": {
        "required": ["Product Type", "Platform", "Recommended Arch"],
        "min_rows": 25,
        "url_col": "Reference URL",
        "severity_col": None,
        "dedup_col": "Product Type",
    },
    "project-templates.csv": {
        "required": ["Template Name", "Platform", "Architecture", "Tech Stack"],
        "min_rows": 15,
        "url_col": "Reference URL",
        "severity_col": None,
        "dedup_col": "Template Name",
    },
    "code-snippets.csv": {
        "required": ["ID", "Name", "Platform", "Category", "Description", "Code"],
        "min_rows": 25,
        "url_col": "Reference URL",
        "severity_col": None,
        "dedup_col": "ID",
        "source_url_col": "Source URL",       # cs.android.com for Android snippets
        "source_url_platform": "Android",
    },
    "gradle-deps.csv": {
        "required": ["Name", "Category", "Implementation"],
        "min_rows": 40,
        "url_col": "Reference URL",
        "severity_col": None,
        "dedup_col": "Name",
    },
    "design-patterns.csv": {
        "required": ["Name", "Category", "Platform", "Intent"],
        "min_rows": 50,
        "url_col": "Reference URL",
        "severity_col": None,
        "dedup_col": "Name",
    },
}

PLATFORM_EXPECTED = {
    "platforms/android.csv": {
        "required": ["Category", "Guideline", "Description", "Do", "Severity"],
        "min_rows": 50,
        "url_col": "Docs URL",
        "severity_col": "Severity",
        "dedup_col": "Guideline",
    },
    "platforms/ios.csv": {
        "required": ["Category", "Guideline", "Description", "Do", "Severity"],
        "min_rows": 30,
        "url_col": "Docs URL",
        "severity_col": "Severity",
        "dedup_col": "Guideline",
    },
    "platforms/flutter.csv": {
        "required": ["Category", "Guideline", "Description", "Do", "Severity"],
        "min_rows": 30,
        "url_col": "Docs URL",
        "severity_col": "Severity",
        "dedup_col": "Guideline",
    },
    "platforms/react-native.csv": {
        "required": ["Category", "Guideline", "Description", "Do", "Severity"],
        "min_rows": 30,
        "url_col": "Docs URL",
        "severity_col": "Severity",
        "dedup_col": "Guideline",
    },
}


errors = []
warnings = []
total_rows = 0


def validate_file(rel_path, spec):
    global total_rows
    filepath = DATA_DIR / rel_path
    if not filepath.exists():
        errors.append(f"MISSING FILE: {rel_path}")
        return

    with open(filepath, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)

    # 1. Required columns
    for col in spec["required"]:
        if col not in headers:
            errors.append(f"{rel_path}: missing required column '{col}'")

    # 2. URL column exists
    url_col = spec.get("url_col")
    if url_col and url_col not in headers:
        errors.append(f"{rel_path}: missing URL column '{url_col}'")

    # 3. Row count
    if len(rows) < spec["min_rows"]:
        errors.append(
            f"{rel_path}: only {len(rows)} rows (expected >= {spec['min_rows']})"
        )

    # 4. Per-row validation
    seen = set()
    dedup_col = spec.get("dedup_col")
    source_url_col = spec.get("source_url_col")
    source_url_platform = spec.get("source_url_platform", "Android")

    empty_required = 0
    bad_severity = []
    missing_url = []
    missing_source_url = []
    duplicates = []

    for i, row in enumerate(rows, 2):
        # Empty required fields
        for col in spec["required"]:
            if col in row and not row[col].strip():
                empty_required += 1

        # Severity values
        sev_col = spec.get("severity_col")
        if sev_col and sev_col in row:
            sev = row[sev_col].strip()
            if sev and sev not in VALID_SEVERITY:
                bad_severity.append(f"row {i}: '{sev}'")

        # Reference URL / Docs URL present per row
        if url_col and url_col in row and not row[url_col].strip():
            missing_url.append(i)

        # Source URL for Android snippets
        if source_url_col and source_url_col in headers:
            platform = row.get("Platform", "").strip()
            if platform == source_url_platform and not row.get(source_url_col, "").strip():
                missing_source_url.append(f"row {i} ({row.get('ID', row.get('Name', '?'))})")

        # Duplicates
        if dedup_col and dedup_col in row:
            key = row[dedup_col].strip().lower()
            if key and key in seen:
                duplicates.append(f"row {i}: duplicate '{row[dedup_col]}'")
            seen.add(key)

    if empty_required > 0:
        warnings.append(f"{rel_path}: {empty_required} empty required fields")
    if bad_severity:
        errors.append(f"{rel_path}: invalid Severity values: {bad_severity[:5]}")
    if len(missing_url) > 5:
        warnings.append(f"{rel_path}: {len(missing_url)} rows missing {url_col}")
    if missing_source_url:
        warnings.append(
            f"{rel_path}: {len(missing_source_url)} Android snippets missing Source URL "
            f"(cs.android.com) — {missing_source_url[:3]}"
        )
    if duplicates:
        warnings.append(f"{rel_path}: {duplicates[:3]}")

    total_rows += len(rows)
    print(f"  OK  {rel_path} ({len(rows)} rows, {len(headers)} cols)")


print("=" * 60)
print("Mobile Best Practices — CSV Validation")
print("=" * 60)

all_specs = {**EXPECTED, **PLATFORM_EXPECTED}
for rel_path, spec in all_specs.items():
    validate_file(rel_path, spec)

print(f"\nTotal: {total_rows} entries across {len(all_specs)} CSV files")

if warnings:
    print(f"\nWarnings ({len(warnings)}):")
    for w in warnings:
        print(f"  ⚠  {w}")

if errors:
    print(f"\nErrors ({len(errors)}):")
    for e in errors:
        print(f"  ✗  {e}")
    sys.exit(1)
else:
    print("\n✓ All validations passed!")
