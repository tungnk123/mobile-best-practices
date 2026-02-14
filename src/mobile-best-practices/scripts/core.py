#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mobile Best Practices Core - BM25 search engine for mobile development best practices
"""

import csv
import json
import re
from pathlib import Path
from math import log
from datetime import datetime
from typing import List, Dict, Any, Tuple, Optional, Union, cast
from itertools import islice

# ============ CONFIGURATION ============
DATA_DIR = Path(__file__).parent.parent / "data"
MAX_RESULTS = 3

CSV_CONFIG = {
    "architecture": {
        "file": "architectures.csv",
        "search_cols": ["Name", "Platform", "Keywords", "Best For", "Tech Stack"],
        "output_cols": ["Name", "Platform", "Complexity", "Team Size", "Keywords", "Best For", "Tech Stack", "Layers", "Structure", "Anti Patterns", "Notes"]
    },
    "ui": {
        "file": "ui-patterns.csv",
        "search_cols": ["Pattern Name", "Platform", "Category", "Keywords", "Use Case"],
        "output_cols": ["Pattern Name", "Platform", "Category", "Keywords", "Use Case", "Components", "Implementation Notes", "Accessibility"]
    },
    "template": {
        "file": "project-templates.csv",
        "search_cols": ["Template Name", "Platform", "Architecture", "Tech Stack", "Features Included"],
        "output_cols": ["Template Name", "Platform", "Architecture", "Tech Stack", "Modules", "Folder Structure", "Features Included", "Key Dependencies"]
    },
    "antipattern": {
        "file": "anti-patterns.csv",
        "search_cols": ["Name", "Platform", "Category", "Keywords", "Description"],
        "output_cols": ["Name", "Platform", "Category", "Severity", "Description", "Bad Example", "Good Example", "Why Bad", "Fix"]
    },
    "reasoning": {
        "file": "reasoning-rules.csv",
        "search_cols": ["Product Type", "Platform", "Keywords", "Key Features"],
        "output_cols": ["Product Type", "Platform", "Recommended Arch", "Recommended UI", "Color Mood", "Key Features", "Anti Patterns", "Key Dependencies", "Notes"]
    },
    "library": {
        "file": "libraries.csv",
        "search_cols": ["Name", "Platform", "Category", "Keywords", "Description"],
        "output_cols": ["Name", "Platform", "Category", "Keywords", "Description", "Gradle/Pod/Pub", "Alternative", "Stars", "Notes"]
    },
    "performance": {
        "file": "performance.csv",
        "search_cols": ["Category", "Issue", "Platform", "Keywords", "Description"],
        "output_cols": ["Category", "Issue", "Platform", "Severity", "Description", "Do", "Dont", "Code Good", "Code Bad", "Metric"]
    },
    "testing": {
        "file": "testing.csv",
        "search_cols": ["Category", "Pattern", "Platform", "Keywords", "Description"],
        "output_cols": ["Category", "Pattern", "Platform", "Description", "Framework", "Code Example", "Anti Pattern", "Notes"]
    },
    "security": {
        "file": "security.csv",
        "search_cols": ["Category", "Threat", "Platform", "Keywords", "Description"],
        "output_cols": ["Category", "Threat", "Platform", "Severity", "Description", "Mitigation", "Code Good", "Code Bad", "OWASP Ref"]
    },
    "snippet": {
        "file": "code-snippets.csv",
        "search_cols": ["Name", "Category", "Keywords", "Description"],
        "output_cols": ["ID", "Name", "Platform", "Category", "Description", "Code", "Imports", "Notes"]
    },
    "gradle": {
        "file": "gradle-deps.csv",
        "search_cols": ["Name", "Category", "Keywords"],
        "output_cols": ["Name", "Category", "Version Catalog Key", "Implementation", "KSP/KAPT", "Version", "Notes"]
    },
    "designpattern": {
        "file": "design-patterns.csv",
        "search_cols": ["Name", "Category", "Platform", "Keywords", "Intent", "Code Smell"],
        "output_cols": ["Name", "Category", "Platform", "Intent", "Code Smell", "When To Use", "Structure", "Bad Example", "Good Example", "Notes"]
    }
}

PLATFORM_CONFIG = {
    "android": {"file": "platforms/android.csv"},
    "android-xml": {"file": "platforms/android.csv"},
    "ios": {"file": "platforms/ios.csv"},
    "flutter": {"file": "platforms/flutter.csv"},
    "react-native": {"file": "platforms/react-native.csv"}
}

_PLATFORM_COLS = {
    "search_cols": ["Category", "Guideline", "Description", "Do", "Dont"],
    "output_cols": ["Category", "Guideline", "Description", "Do", "Dont", "Code Good", "Code Bad", "Severity", "Docs URL"]
}

AVAILABLE_PLATFORMS = list(PLATFORM_CONFIG.keys())

# Stack-to-platform mapping for --stack search
STACK_MAP = {
    "compose": "android",
    "jetpack-compose": "android",
    "material3": "android",
    "hilt": "android",
    "room": "android",
    "kotlin": "android",
    "viewbinding": "android-xml",
    "xml": "android-xml",
    "swiftui": "ios",
    "combine": "ios",
    "uikit": "ios",
    "swift": "ios",
    "flutter": "flutter",
    "dart": "flutter",
    "bloc": "flutter",
    "riverpod": "flutter",
    "react-native": "react-native",
    "rn": "react-native",
    "hooks": "react-native",
    "typescript": "react-native",
    "redux": "react-native",
}

AVAILABLE_STACKS = list(STACK_MAP.keys())


# ============ BM25 IMPLEMENTATION ============
class BM25:
    """BM25 ranking algorithm for text search"""

    def __init__(self, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.corpus: List[List[str]] = []
        self.doc_lengths: List[int] = []
        self.avgdl: float = 0.0
        self.idf: Dict[str, float] = {}
        self.doc_freqs: Dict[str, int] = {}
        self.N: int = 0

    def tokenize(self, text):
        """Lowercase, split, remove punctuation, filter short words"""
        text = re.sub(r'[^\w\s]', ' ', str(text).lower())
        return [w for w in text.split() if len(w) > 2]

    def fit(self, documents):
        """Build BM25 index from documents"""
        self.corpus = [self.tokenize(doc) for doc in documents]
        self.N = len(self.corpus)
        if self.N == 0:
            return
            
        self.doc_lengths = [len(doc) for doc in self.corpus]
        self.avgdl = sum(self.doc_lengths) / self.N

        for doc in self.corpus:
            seen = set()
            for word in doc:
                if word not in seen:
                    self.doc_freqs[word] = self.doc_freqs.get(word, 0) + 1
                    seen.add(word)

        for word, freq in self.doc_freqs.items():
            self.idf[word] = log((self.N - freq + 0.5) / (freq + 0.5) + 1)

    def score(self, query: str) -> List[Tuple[int, float]]:
        """Score all documents against query"""
        query_tokens = self.tokenize(query)
        scores = []

        for idx, doc in enumerate(self.corpus):
            doc_score: float = 0.0
            doc_len = self.doc_lengths[idx]
            term_freqs = {}
            for word in doc:
                term_freqs[word] = term_freqs.get(word, 0) + 1

            for token in query_tokens:
                if token in self.idf:
                    tf = term_freqs.get(token, 0)
                    idf = self.idf[token]
                    numerator = tf * (self.k1 + 1)
                    denominator = tf + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)
                    doc_score = doc_score + (idf * numerator / denominator)  # type: ignore

            scores.append((idx, doc_score))

        return sorted(scores, key=lambda x: x[1], reverse=True)


# ============ SEARCH FUNCTIONS ============
def _load_csv(filepath):
    """Load CSV and return list of dicts"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def _search_csv(filepath: Path, search_cols: List[str], output_cols: List[str], query: str, max_results: int) -> List[Dict[str, str]]:
    """Core search function using BM25"""
    if not filepath.exists():
        return []

    data = _load_csv(filepath)

    # Build documents from search columns
    documents = [" ".join(str(row.get(col, "")) for col in search_cols) for row in data]

    # BM25 search
    bm25 = BM25()
    bm25.fit(documents)
    ranked = bm25.score(query)

    # Get top results with score > 0
    results = []
    for idx, score in islice(ranked, int(max_results)):
        if score > 0:
            row = data[idx]
            results.append({col: row.get(col, "") for col in output_cols if col in row})

    return results


def detect_domain(query):
    """Auto-detect the most relevant domain from query"""
    query_lower = query.lower()

    domain_keywords = {
        "architecture": ["mvvm", "mvi", "viper", "bloc", "clean", "architecture", "repository", "coordinator", "redux", "tca", "layer", "module"],
        "ui": ["button", "navigation", "bottom sheet", "tab", "list", "card", "dialog", "modal", "drawer", "scaffold", "appbar", "toolbar"],
        "template": ["project", "template", "setup", "scaffold", "starter", "boilerplate", "create", "new app", "init"],
        "antipattern": ["anti-pattern", "antipattern", "mistake", "bad practice", "wrong", "avoid", "smell", "god class", "leak"],
        "reasoning": ["ecommerce", "e-commerce", "banking", "fintech", "social", "healthcare", "delivery", "fitness", "education", "food", "chat", "streaming"],
        "library": ["library", "dependency", "package", "retrofit", "hilt", "room", "coil", "ktor", "alamofire", "dio", "riverpod", "redux"],
        "performance": ["performance", "memory", "battery", "startup", "render", "fps", "lag", "slow", "optimize", "profil", "baseline"],
        "testing": ["test", "unit test", "ui test", "espresso", "xctest", "mockito", "junit", "widget test", "integration"],
        "security": ["security", "encrypt", "keychain", "keystore", "proguard", "obfuscate", "ssl", "pin", "biometric", "auth token"],
        "snippet": ["snippet", "code", "example", "template code", "viewmodel code", "compose screen", "room setup", "hilt module", "bottom nav", "paging", "datastore", "theme code"],
        "gradle": ["gradle", "dependency", "implementation", "ksp", "kapt", "version catalog", "libs.", "bom", "plugin", "classpath"],
        "designpattern": ["design pattern", "pattern", "factory", "observer", "strategy", "builder pattern", "adapter pattern", "decorator", "facade", "singleton pattern", "command pattern", "state pattern", "mediator", "proxy pattern", "composite", "code smell", "refactor pattern", "visitor", "chain of responsibility", "template method", "repository pattern", "mapper"]
    }

    scores = {domain: sum(1 for kw in keywords if kw in query_lower) for domain, keywords in domain_keywords.items()}
    best = max(scores, key=scores.__getitem__)
    return best if scores[best] > 0 else "architecture"


def search(query: str, domain: Optional[str] = None, max_results: int = MAX_RESULTS, filter_platform: Optional[str] = None) -> Dict[str, Any]:
    """Main search function with auto-domain detection and optional platform filter"""
    if domain is None:
        domain = detect_domain(query)

    config = CSV_CONFIG.get(domain, CSV_CONFIG["architecture"])
    # Ensure file is treated as string for Path concatenation
    filepath = DATA_DIR / str(config["file"])

    if not filepath.exists():
        return {"error": f"File not found: {filepath}", "domain": domain}

    # Cast config values to expected types
    search_cols = cast(List[str], config["search_cols"])
    output_cols = cast(List[str], config["output_cols"])

    results = _search_csv(filepath, search_cols, output_cols, query, max_results * 3 if filter_platform else max_results)

    # Filter by platform if specified
    if filter_platform and results:
        filter_lower = filter_platform.lower()
        # Aliases for filtering
        if filter_lower == "android-xml":
            filter_lower = "android"

        results = [r for r in results if any(
            filter_lower in str(v).lower()
            for k, v in r.items()
            if k.lower() == "platform"
        )]
        results = list(islice(results, int(max_results)))

    return {
        "domain": domain,
        "query": query,
        "file": config["file"],
        "count": len(results),
        "results": results
    }


def search_platform(query: str, platform: str, max_results: int = MAX_RESULTS) -> Dict[str, Any]:
    """Search platform-specific guidelines"""
    if platform not in PLATFORM_CONFIG:
        return {"error": f"Unknown platform: {platform}. Available: {', '.join(AVAILABLE_PLATFORMS)}"}

    filepath = DATA_DIR / str(PLATFORM_CONFIG[platform]["file"])

    if not filepath.exists():
        return {"error": f"Platform file not found: {filepath}", "platform": platform}

    search_cols = cast(List[str], _PLATFORM_COLS["search_cols"])
    output_cols = cast(List[str], _PLATFORM_COLS["output_cols"])
    results = _search_csv(filepath, search_cols, output_cols, query, max_results)

    return {
        "domain": "platform",
        "platform": platform,
        "query": query,
        "file": PLATFORM_CONFIG[platform]["file"],
        "count": len(results),
        "results": results
    }


def search_stack(query: str, stack: str, max_results: int = MAX_RESULTS) -> Dict[str, Any]:
    """Search filtered by tech stack (maps stack to platform + adds stack keywords)"""
    stack_lower = stack.lower()

    if stack_lower not in STACK_MAP:
        return {"error": f"Unknown stack: {stack}. Available: {', '.join(AVAILABLE_STACKS)}"}

    platform = STACK_MAP[stack_lower]

    # Search platform guidelines first
    platform_results = search_platform(f"{query} {stack}", platform, max_results)

    # Also search across domains filtered by platform
    domain_results = search(f"{query} {stack}", filter_platform=platform, max_results=max_results)

    # Merge results
    all_results: List[Any] = []
    if platform_results.get("results"):
        all_results.extend(platform_results["results"])
    if domain_results.get("results"):
        all_results.extend(domain_results["results"])

    final_results = list(islice(all_results, int(max_results)))

    return {
        "domain": "stack",
        "stack": stack,
        "platform": platform,
        "query": query,
        "count": len(final_results),
        "results": final_results
    }


def persist_blueprint(query, output_dir=None, project_name=None, page=None):
    """Generate and persist architecture blueprint from search results"""
    if output_dir is None:
        output_dir = Path.cwd() / "architecture-blueprint"

    output_dir = Path(output_dir)

    # Run multi-domain search
    domains_to_search = ["reasoning", "architecture", "snippet", "gradle", "performance", "security", "antipattern"]
    all_results: Dict[str, Any] = {}

    for domain in domains_to_search:
        result = search(query, domain=domain, max_results=5)
        if result.get("results"):
            all_results[domain] = result["results"]

    # Detect platform
    platform = "android" # default
    for kw in ["android-xml", "android", "ios", "flutter", "react-native", "react native"]:
        if kw in query.lower():
            platform = kw.replace(" ", "-")
            break

    # Get platform guidelines
    platform_result = search_platform(query, platform, max_results=5)
    if platform_result.get("results"):
        all_results["platform"] = platform_result["results"]

    # Generate blueprint markdown
    pname = project_name or "MyApp"
    lines = [
        f"# Architecture Blueprint - {pname}",
        f"",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Query:** {query}",
        f"**Platform:** {platform}",
        f"",
    ]

    if "reasoning" in all_results:
        lines.append("## Product Recommendation")
        for r in all_results["reasoning"][:1]:
            for k, v in r.items():
                lines.append(f"- **{k}:** {v}")
        lines.append("")

    if "architecture" in all_results:
        lines.append("## Architecture")
        for r in all_results["architecture"][:2]:
            for k, v in r.items():
                lines.append(f"- **{k}:** {v}")
            lines.append("")

    if "gradle" in all_results:
        lines.append("## Dependencies")
        for r in all_results["gradle"]:
            name = r.get("Name", "")
            impl = r.get("Implementation", "")
            lines.append(f"- **{name}:** `{impl}`")
        lines.append("")

    if "performance" in all_results:
        lines.append("## Performance Rules")
        for r in all_results["performance"][:3]:
            issue = r.get("Issue", "")
            do = r.get("Do", "")
            lines.append(f"- **{issue}:** {do}")
        lines.append("")

    if "security" in all_results:
        lines.append("## Security Checklist")
        for r in all_results["security"][:3]:
            threat = r.get("Threat", "")
            mitigation = r.get("Mitigation", "")
            lines.append(f"- **{threat}:** {mitigation}")
        lines.append("")

    if "antipattern" in all_results:
        lines.append("## Anti-Patterns to Avoid")
        for r in all_results["antipattern"][:3]:
            name = r.get("Name", "")
            fix = r.get("Fix", "")
            lines.append(f"- **{name}:** {fix}")
        lines.append("")

    if "platform" in all_results:
        lines.append(f"## {platform.title()} Best Practices")
        for r in all_results["platform"][:5]:
            guideline = r.get("Guideline", "")
            desc = r.get("Do", "")
            lines.append(f"- **{guideline}:** {desc}")
        lines.append("")

    content = "\n".join(lines)

    # Write files
    if page:
        pages_dir = output_dir / "pages"
        pages_dir.mkdir(parents=True, exist_ok=True)
        filepath = pages_dir / f"{page}.md"
    else:
        output_dir.mkdir(parents=True, exist_ok=True)
        filepath = output_dir / "MASTER.md"

    filepath.write_text(content, encoding="utf-8")

    return {
        "file": str(filepath),
        "sections": list(all_results.keys()),
        "total_entries": sum(len(v) for v in all_results.values()),
    }
