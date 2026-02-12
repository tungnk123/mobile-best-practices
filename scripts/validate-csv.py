#!/usr/bin/env python3
"""Validate all CSV files: check headers, row counts, empty fields, and Reference URLs."""

import csv
import sys
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "src" / "mobile-best-practices" / "data"

EXPECTED = {
    "architectures.csv": {
        "required": ["Name", "Platform", "Complexity", "Keywords", "Best For", "Tech Stack"],
        "min_rows": 20,
        "url_col": "Reference URL",
    },
    "libraries.csv": {
        "required": ["Name", "Platform", "Category", "Keywords", "Description"],
        "min_rows": 50,
        "url_col": "Reference URL",
    },
    "ui-patterns.csv": {
        "required": ["Pattern Name", "Platform", "Category", "Keywords", "Use Case"],
        "min_rows": 50,
        "url_col": "Reference URL",
    },
    "anti-patterns.csv": {
        "required": ["Name", "Platform", "Category", "Severity", "Description"],
        "min_rows": 50,
        "url_col": "Reference URL",
    },
    "performance.csv": {
        "required": ["Category", "Issue", "Platform", "Severity", "Description"],
        "min_rows": 40,
        "url_col": "Reference URL",
    },
    "security.csv": {
        "required": ["Category", "Threat", "Platform", "Severity", "Description"],
        "min_rows": 30,
        "url_col": "Reference URL",
    },
    "testing.csv": {
        "required": ["Category", "Pattern", "Platform", "Description"],
        "min_rows": 30,
        "url_col": "Reference URL",
    },
    "reasoning-rules.csv": {
        "required": ["Product Type", "Platform", "Recommended Arch"],
        "min_rows": 25,
        "url_col": "Reference URL",
    },
    "project-templates.csv": {
        "required": ["Template Name", "Platform", "Architecture", "Tech Stack"],
        "min_rows": 15,
        "url_col": "Reference URL",
    },
    "code-snippets.csv": {
        "required": ["Name", "Platform", "Category", "Description", "Code"],
        "min_rows": 25,
        "url_col": "Reference URL",
    },
    "gradle-deps.csv": {
        "required": ["Name", "Category", "Implementation"],
        "min_rows": 40,
        "url_col": "Reference URL",
    },
}

PLATFORM_EXPECTED = {
    "platforms/android.csv": {"required": ["Category", "Guideline", "Description", "Do", "Severity"], "min_rows": 50, "url_col": "Docs URL"},
    "platforms/ios.csv": {"required": ["Category", "Guideline", "Description", "Do", "Severity"], "min_rows": 30, "url_col": "Docs URL"},
    "platforms/flutter.csv": {"required": ["Category", "Guideline", "Description", "Do", "Severity"], "min_rows": 30, "url_col": "Docs URL"},
    "platforms/react-native.csv": {"required": ["Category", "Guideline", "Description", "Do", "Severity"], "min_rows": 30, "url_col": "Docs URL"},
}

errors = []
warnings = []
total_rows = 0


def validate_file(rel_path, spec):
    global total_rows
    filepath = DATA_DIR / rel_path
    if not filepath.exists():
        errors.append(f"MISSING: {rel_path}")
        return

    with open(filepath, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)

    # Check required columns
    for col in spec["required"]:
        if col not in headers:
            errors.append(f"{rel_path}: missing required column '{col}'")

    # Check URL column exists
    url_col = spec.get("url_col")
    if url_col and url_col not in headers:
        warnings.append(f"{rel_path}: missing '{url_col}' column")

    # Check row count
    if len(rows) < spec["min_rows"]:
        errors.append(f"{rel_path}: only {len(rows)} rows (expected >= {spec['min_rows']})")

    # Check for empty required fields
    empty_count = 0
    for i, row in enumerate(rows, 2):
        for col in spec["required"]:
            if col in row and not row[col].strip():
                empty_count += 1
    if empty_count > 0:
        warnings.append(f"{rel_path}: {empty_count} empty required fields")

    total_rows += len(rows)
    print(f"  OK  {rel_path} ({len(rows)} rows, {len(headers)} cols)")


print("Validating CSV databases...\n")

for rel_path, spec in {**EXPECTED, **PLATFORM_EXPECTED}.items():
    validate_file(rel_path, spec)

print(f"\nTotal: {total_rows} entries across {len(EXPECTED) + len(PLATFORM_EXPECTED)} files")

if warnings:
    print(f"\nWarnings ({len(warnings)}):")
    for w in warnings:
        print(f"  - {w}")

if errors:
    print(f"\nErrors ({len(errors)}):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
else:
    print("\nAll validations passed!")
