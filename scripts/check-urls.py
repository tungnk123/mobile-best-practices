#!/usr/bin/env python3
"""
Check all Reference URLs and Docs URLs in CSVs return HTTP 200.
Runs with concurrency to be fast. Skips empty URLs and non-http entries.
Exits with code 1 if any URL returns 4xx/5xx.
"""

import csv
import sys
import urllib.request
import urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

DATA_DIR = Path(__file__).parent.parent / "src" / "mobile-best-practices" / "data"

# (relative_path, url_column_name)
FILES_TO_CHECK = [
    ("anti-patterns.csv",           "Reference URL"),
    ("performance.csv",             "Reference URL"),
    ("security.csv",                "Reference URL"),
    ("code-snippets.csv",           "Reference URL"),
    ("code-snippets.csv",           "Source URL"),
    ("gradle-deps.csv",             "Reference URL"),
    ("architectures.csv",           "Reference URL"),
    ("design-patterns.csv",         "Reference URL"),
    ("libraries.csv",               "Reference URL"),
    ("testing.csv",                 "Reference URL"),
    ("platforms/android.csv",       "Docs URL"),
    ("platforms/ios.csv",           "Docs URL"),
    ("platforms/flutter.csv",       "Docs URL"),
    ("platforms/react-native.csv",  "Docs URL"),
]

# Domains that block bots — treat as OK even if we can't fetch them
SKIP_DOMAINS = {
    "github.com",
    "bloclibrary.dev",
    "riverpod.dev",
    "tanstack.com",
    "shopify.github.io",
    "www.w3.org",
    "www.hhs.gov",
    "portswigger.net",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; mobile-best-practices-ci/1.0)",
}

TIMEOUT = 10


def collect_urls():
    """Return list of (url, source_label) tuples."""
    seen = set()
    results = []
    for rel_path, col in FILES_TO_CHECK:
        filepath = DATA_DIR / rel_path
        if not filepath.exists():
            continue
        with open(filepath, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader, 2):
                url = row.get(col, "").strip()
                if not url or not url.startswith("http"):
                    continue
                if url in seen:
                    continue
                seen.add(url)
                results.append((url, f"{rel_path}:{col}:row{i}"))
    return results


def check_url(url, label):
    """Returns (url, label, status_code, ok)."""
    from urllib.parse import urlparse
    domain = urlparse(url).netloc.lower()
    if any(skip in domain for skip in SKIP_DOMAINS):
        return url, label, 0, True  # skip, treated as OK

    try:
        req = urllib.request.Request(url, headers=HEADERS, method="HEAD")
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            code = resp.status
            return url, label, code, code < 400
    except urllib.error.HTTPError as e:
        # Try GET if HEAD not allowed
        if e.code in (405, 403):
            try:
                req = urllib.request.Request(url, headers=HEADERS)
                with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                    code = resp.status
                    return url, label, code, code < 400
            except Exception:
                pass
        return url, label, e.code, e.code < 400
    except Exception as e:
        return url, label, 0, False


def main():
    urls = collect_urls()
    print(f"Checking {len(urls)} unique URLs (concurrency=10)...\n")

    broken = []
    ok_count = 0
    skip_count = 0

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(check_url, url, label): url for url, label in urls}
        for future in as_completed(futures):
            url, label, code, ok = future.result()
            if code == 0 and ok:
                skip_count += 1
            elif ok:
                ok_count += 1
            else:
                broken.append((url, label, code))
                print(f"  FAIL [{code}] {url}\n       ({label})")

    print(f"\n✓ OK: {ok_count}  |  skipped (bot-blocked domains): {skip_count}  |  broken: {len(broken)}")

    if broken:
        print(f"\n{len(broken)} broken URLs — fix or remove them:")
        for url, label, code in broken:
            print(f"  [{code}] {url}  ({label})")
        sys.exit(1)
    else:
        print("All URLs reachable!")


if __name__ == "__main__":
    main()
