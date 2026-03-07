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
MAX_RESULTS = 15           # default for single-domain searches
ALL_DOMAINS_MAX_RESULTS = 30  # default for --all-domains cross-domain search

CSV_CONFIG = {
    "architecture": {
        "file": "architectures.csv",
        "search_cols": ["Name", "Platform", "Keywords", "Best For", "Tech Stack"],
        "output_cols": ["Name", "Platform", "Complexity", "Team Size", "Keywords", "Best For", "Tech Stack", "Layers", "Structure", "Anti Patterns", "Notes", "Reference URL"]
    },
    "ui": {
        "file": "ui-patterns.csv",
        "search_cols": ["Pattern Name", "Platform", "Category", "Keywords", "Use Case"],
        "output_cols": ["Pattern Name", "Platform", "Category", "Keywords", "Use Case", "Components", "Implementation Notes", "Accessibility", "Reference URL"]
    },
    "template": {
        "file": "project-templates.csv",
        "search_cols": ["Template Name", "Platform", "Architecture", "Tech Stack", "Features Included"],
        "output_cols": ["Template Name", "Platform", "Architecture", "Tech Stack", "Modules", "Folder Structure", "Features Included", "Key Dependencies", "Reference URL"]
    },
    "antipattern": {
        "file": "anti-patterns.csv",
        "search_cols": ["Name", "Platform", "Category", "Keywords", "Description"],
        "output_cols": ["Name", "Platform", "Category", "Severity", "Description", "Bad Example", "Good Example", "Fix", "Reference URL"]
    },
    "reasoning": {
        "file": "reasoning-rules.csv",
        "search_cols": ["Product Type", "Platform", "Keywords", "Key Features"],
        "output_cols": ["Product Type", "Platform", "Recommended Arch", "Recommended UI", "Color Mood", "Key Features", "Anti Patterns", "Key Dependencies", "Notes", "Reference URL"]
    },
    "library": {
        "file": "libraries.csv",
        "search_cols": ["Name", "Platform", "Category", "Keywords", "Description"],
        "output_cols": ["Name", "Platform", "Category", "Keywords", "Description", "Gradle/Pod/Pub", "Alternative", "Stars", "Notes", "Reference URL"]
    },
    "performance": {
        "file": "performance.csv",
        "search_cols": ["Category", "Issue", "Platform", "Keywords", "Description"],
        "output_cols": ["Category", "Issue", "Platform", "Severity", "Description", "Do", "Dont", "Code Good", "Code Bad", "Metric", "Reference URL"]
    },
    "testing": {
        "file": "testing.csv",
        "search_cols": ["Category", "Pattern", "Platform", "Keywords", "Description"],
        "output_cols": ["Category", "Pattern", "Platform", "Description", "Framework", "Code Example", "Anti Pattern", "Notes", "Reference URL"]
    },
    "security": {
        "file": "security.csv",
        "search_cols": ["Category", "Threat", "Platform", "Keywords", "Description"],
        "output_cols": ["Category", "Threat", "Platform", "Severity", "Description", "Mitigation", "Code Good", "Code Bad", "OWASP Ref", "Reference URL"]
    },
    "snippet": {
        "file": "code-snippets.csv",
        "search_cols": ["Name", "Category", "Keywords", "Description"],
        "output_cols": ["ID", "Name", "Platform", "Category", "Description", "Code", "Imports", "Notes", "Source URL"]
    },
    "gradle": {
        "file": "gradle-deps.csv",
        "search_cols": ["Name", "Category", "Keywords"],
        "output_cols": ["Name", "Category", "Version Catalog Key", "Implementation", "KSP/KAPT", "Version", "Notes", "Reference URL"]
    },
    "designpattern": {
        "file": "design-patterns.csv",
        "search_cols": ["Name", "Category", "Platform", "Keywords", "Intent", "Code Smell"],
        "output_cols": ["Name", "Category", "Platform", "Intent", "Code Smell", "When To Use", "Bad Example", "Good Example", "Notes", "Reference URL"]
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

# Fields across all CSV schemas that contain code
_CODE_FIELDS = frozenset({
    "Code Good", "Code Bad", "Code", "Code Example",
    "Good Example", "Bad Example",
})

# Keywords that mark a comment as "important" (used by style='important')
_IMPORTANT_WORDS = frozenset({
    "important", "note", "warning", "todo", "fixme", "why", "critical",
    "workaround", "hack", "required", "must", "never", "always",
    "deprecated", "throws", "override", "see", "param", "return",
    "caution", "security", "crash", "leak",
})


# ============ COMMENT STYLE FILTER ============

def _is_important_comment(text: str) -> bool:
    """Return True if comment text contains an importance marker word."""
    lower = text.lower()
    return any(w in lower for w in _IMPORTANT_WORDS)


def _strip_inline_comment(line: str) -> str:
    """Remove a trailing // comment, respecting quoted strings."""
    in_str, str_ch = False, ""
    i = 0
    while i < len(line):
        ch = line[i]
        if in_str:
            if ch == "\\" and i + 1 < len(line):
                i += 2
                continue
            if ch == str_ch:
                in_str = False
        elif ch in ('"', "'"):
            in_str, str_ch = True, ch
        elif ch == "/" and i + 1 < len(line) and line[i + 1] == "/":
            return line[:i].rstrip()
        i += 1
    return line


def apply_comment_style(code: str, style: str) -> str:
    """Filter comments in a code string based on the requested style.

    Styles
    ------
    'all'       — unchanged (default)
    'none'      — every comment line / block is removed; inline comments
                  are stripped from the end of code lines
    'important' — only comments whose text contains an importance marker word
                  (NOTE, WARNING, WHY, IMPORTANT, CRITICAL, …) are kept;
                  all other comments are removed; KDoc /** */ blocks are kept
                  only when their body matches as well
    """
    if style == "all" or not code:
        return code

    lines = code.split("\n")
    result: List[str] = []
    in_block = False
    block_buf: List[str] = []

    for line in lines:
        stripped = line.strip()

        # ── Block-comment: /* ... */ or /** ... */
        if not in_block and stripped.startswith("/*"):
            if "*/" in stripped:
                # Single-line block or KDoc: /** ... */ or /* ... */
                if style == "none":
                    continue
                if style == "important" and _is_important_comment(stripped):
                    result.append(line)
                continue
            else:
                # Multi-line block comment opening
                in_block = True
                block_buf = [line]
                continue

        # ── Inside a block comment
        if in_block:
            block_buf.append(line)
            if "*/" in stripped:
                in_block = False
                combined = " ".join(block_buf)
                if style == "none":
                    pass  # discard
                elif style == "important" and _is_important_comment(combined):
                    result.extend(block_buf)
                block_buf = []
            continue

        # ── Full-line // or # comment
        if stripped.startswith("//") or stripped.startswith("#"):
            if style == "none":
                continue
            if style == "important" and _is_important_comment(stripped):
                result.append(line)
            continue

        # ── Inline // comment appended to code
        if "//" in line:
            bare = _strip_inline_comment(line)
            inline_comment = line[len(bare):]
            if style == "none":
                result.append(bare)
            elif style == "important":
                if _is_important_comment(inline_comment):
                    result.append(line)   # keep comment
                else:
                    result.append(bare)   # strip comment, keep code
            else:
                result.append(line)
            continue

        result.append(line)

    # Collapse consecutive blank lines → single blank line
    final: List[str] = []
    prev_blank = False
    for ln in result:
        blank = not ln.strip()
        if blank and prev_blank:
            continue
        final.append(ln)
        prev_blank = blank

    return "\n".join(final)


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

    # ── Fuzzy helpers ──────────────────────────────────────────────────────────

    def _bigrams(self, word: str) -> set:
        """Character bigrams of a word (space-padded) for Dice similarity."""
        padded = f" {word} "
        return {padded[i:i + 2] for i in range(len(padded) - 1)}

    def expand_query(self, query: str, threshold: float = 0.60) -> str:
        """Return an expanded query string with fuzzy-matched vocabulary terms.

        For each query token absent from the BM25 vocabulary, finds the
        closest vocabulary word using Dice coefficient on character bigrams.
        If the best match exceeds *threshold* the matched word is appended to
        the query so the BM25 scorer can pick it up.  Tokens shorter than 4
        characters are skipped to avoid noisy expansions.
        """
        query_tokens = self.tokenize(query)
        vocab = set(self.idf.keys())
        extra: List[str] = []

        for token in query_tokens:
            if token in vocab or len(token) < 4:
                continue
            tok_bg = self._bigrams(token)
            best_word, best_dice = "", 0.0
            for word in vocab:
                if abs(len(word) - len(token)) > 3:
                    continue  # skip obviously different lengths early
                w_bg = self._bigrams(word)
                intersection = len(tok_bg & w_bg)
                dice = 2 * intersection / (len(tok_bg) + len(w_bg))
                if dice > best_dice:
                    best_dice, best_word = dice, word
            if best_dice >= threshold:
                extra.append(best_word)

        return (query + " " + " ".join(extra)) if extra else query

    def score_fuzzy(self, query: str, threshold: float = 0.60) -> List[Tuple[int, float]]:
        """Score with automatic fuzzy query expansion for typo tolerance."""
        return self.score(self.expand_query(query, threshold))


# ============ SEARCH FUNCTIONS ============
def _load_csv(filepath):
    """Load CSV and return list of dicts"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def _score_csv(filepath: Path, search_cols: List[str], output_cols: List[str], query: str, top_k: int, fuzzy: bool = False) -> List[Tuple[float, Dict[str, str]]]:
    """Return (normalized_score, row) pairs for the top_k hits in one CSV.

    Scores are normalised to [0, 1] by dividing by the maximum score in the
    file so that results from different corpora are comparable when merged.
    """
    if not filepath.exists():
        return []

    data = _load_csv(filepath)
    if not data:
        return []

    documents = [" ".join(str(row.get(col, "")) for col in search_cols) for row in data]
    bm25 = BM25()
    bm25.fit(documents)
    ranked = bm25.score_fuzzy(query) if fuzzy else bm25.score(query)

    candidates = [(idx, score) for idx, score in ranked[:top_k * 2] if score > 0]
    if not candidates:
        return []

    max_score = candidates[0][1]  # ranked is sorted descending
    if max_score == 0:
        return []

    hits = []
    for idx, score in candidates[:top_k]:
        row = data[idx]
        hits.append((score / max_score, {col: row.get(col, "") for col in output_cols if col in row}))
    return hits


# Common task-instruction verbs and generic nouns that carry no technical meaning
# in a best-practices database.  Stripping them before searching improves token
# coverage and ranking quality.
_TASK_WORDS = frozenset({
    # Task verbs
    "implement", "implementing", "implementation",
    "create", "creating",
    "build", "building",
    "make", "making",
    "add", "adding",
    "write", "writing",
    "setup", "set",
    "configure", "configuration",
    "handle", "handling",
    "define", "defining",
    "develop", "developing",
    "fix", "fixing",
    "update", "updating",
    "refactor", "refactoring",
    "use", "using",
    "need", "want",
    "get", "show", "display",
    "support", "integrate", "integrating",
    # Generic nouns with no domain signal
    "logic", "code", "function", "method", "class",
    "feature", "functionality", "behavior", "behaviour",
    "app", "application", "project",
    "page",
    # Stop words / prepositions / articles
    "how", "the", "for", "with", "in", "a", "an", "to", "of", "on", "at",
    "my", "our", "your", "their",
    "that", "this", "which", "when", "where",
    # Common adverbs / qualifiers with no domain signal
    "securely", "safely", "properly", "correctly", "efficiently", "quickly", "easily",
    "best", "good", "better", "right", "correct",
    # Common question words
    "what", "why", "is", "are", "do", "does", "should", "can", "could", "would",
    "between", "from", "into", "about",
})


def clean_query(query: str) -> str:
    """Strip task-instruction and generic words from a natural-language query.

    Turns 'implement logic for search viewmodel' into 'search viewmodel',
    which matches the technical vocabulary in the best-practices CSVs.
    """
    tokens = re.split(r'\s+', query.strip())
    seen: set = set()
    filtered = []
    for t in tokens:
        lower = t.lower()
        if lower not in _TASK_WORDS and lower not in seen:
            seen.add(lower)
            filtered.append(t)
    # Fallback to original query if stripping left ≤1 meaningful token
    if len(filtered) <= 1:
        return query.strip()
    return " ".join(filtered)


def _search_csv(filepath: Path, search_cols: List[str], output_cols: List[str], query: str, max_results: int, fuzzy: bool = False) -> List[Dict[str, str]]:
    """Core search function using BM25 (with optional fuzzy expansion)"""
    if not filepath.exists():
        return []

    data = _load_csv(filepath)

    # Build documents from search columns
    documents = [" ".join(str(row.get(col, "")) for col in search_cols) for row in data]

    # BM25 search (fuzzy expands query tokens to handle typos)
    bm25 = BM25()
    bm25.fit(documents)
    ranked = bm25.score_fuzzy(query) if fuzzy else bm25.score(query)

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


def search(query: str, domain: Optional[str] = None, max_results: int = MAX_RESULTS, filter_platform: Optional[str] = None, fuzzy: bool = False) -> Dict[str, Any]:
    """Main search function with auto-domain detection and optional platform filter"""
    query = clean_query(query)
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

    results = _search_csv(filepath, search_cols, output_cols, query, max_results * 3 if filter_platform else max_results, fuzzy=fuzzy)

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
        "results": results,
        "fuzzy": fuzzy,
    }


def search_platform(query: str, platform: str, max_results: int = MAX_RESULTS, fuzzy: bool = False) -> Dict[str, Any]:
    """Search platform-specific guidelines"""
    query = clean_query(query)
    if platform not in PLATFORM_CONFIG:
        return {"error": f"Unknown platform: {platform}. Available: {', '.join(AVAILABLE_PLATFORMS)}"}

    filepath = DATA_DIR / str(PLATFORM_CONFIG[platform]["file"])

    if not filepath.exists():
        return {"error": f"Platform file not found: {filepath}", "platform": platform}

    search_cols = cast(List[str], _PLATFORM_COLS["search_cols"])
    output_cols = cast(List[str], _PLATFORM_COLS["output_cols"])
    results = _search_csv(filepath, search_cols, output_cols, query, max_results, fuzzy=fuzzy)

    return {
        "domain": "platform",
        "platform": platform,
        "query": query,
        "file": PLATFORM_CONFIG[platform]["file"],
        "count": len(results),
        "results": results,
        "fuzzy": fuzzy,
    }


def search_stack(query: str, stack: str, max_results: int = MAX_RESULTS, fuzzy: bool = False) -> Dict[str, Any]:
    """Search filtered by tech stack (maps stack to platform + adds stack keywords)"""
    query = clean_query(query)
    stack_lower = stack.lower()

    if stack_lower not in STACK_MAP:
        return {"error": f"Unknown stack: {stack}. Available: {', '.join(AVAILABLE_STACKS)}"}

    platform = STACK_MAP[stack_lower]

    # Search platform guidelines first
    platform_results = search_platform(f"{query} {stack}", platform, max_results, fuzzy=fuzzy)

    # Also search across domains filtered by platform
    domain_results = search(f"{query} {stack}", filter_platform=platform, max_results=max_results, fuzzy=fuzzy)

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


def search_all_domains(query: str, max_results: int = ALL_DOMAINS_MAX_RESULTS, fuzzy: bool = False, filter_platform: Optional[str] = None, min_norm_score: float = 0.5, min_token_coverage: float = 0.5) -> Dict[str, Any]:
    """Search across ALL domains and return top results ranked by normalised BM25 score.

    Each domain's scores are normalised to [0, 1] before merging so results
    from small and large CSVs are comparable.  Two quality filters are applied:

    - *min_norm_score* (default 0.5): result must score >= 50% of the best hit
      in its own domain.
    - *min_token_coverage* (default 0.5): at least half of the unique query
      tokens must actually appear in the result's searchable text, preventing
      entries that only incidentally share one common word from surfacing.

    Each result row includes a ``"Domain"`` key (first field).
    """
    query = clean_query(query)
    # Pre-compute query token set for coverage check
    _bm25_tmp = BM25()
    query_tokens = set(_bm25_tmp.tokenize(query))
    n_query_tokens = len(query_tokens) if query_tokens else 1

    all_hits: List[Tuple[float, Dict[str, str]]] = []

    for domain, config in CSV_CONFIG.items():
        filepath = DATA_DIR / str(config["file"])
        search_cols = cast(List[str], config["search_cols"])
        output_cols = cast(List[str], config["output_cols"])

        if not filepath.exists():
            continue
        data = _load_csv(filepath)
        if not data:
            continue

        # Build searchable text per row for coverage check
        row_texts = [" ".join(str(row.get(col, "")) for col in search_cols) for row in data]

        # Fetch more candidates per domain so cross-domain merge has good coverage
        hits = _score_csv(filepath, search_cols, output_cols, query, max_results * 2, fuzzy=fuzzy)

        for norm_score, row in hits:
            if norm_score < min_norm_score:
                continue  # skip weak incidental matches

            # Find this row's index to check token coverage against its search text
            # Match by first output column value for a lightweight lookup
            row_idx = next(
                (i for i, d in enumerate(data) if all(d.get(c, "") == row.get(c, "") for c in output_cols[:2] if c in row)),
                None
            )
            if row_idx is not None:
                doc_tokens = set(_bm25_tmp.tokenize(row_texts[row_idx]))
                coverage = len(query_tokens & doc_tokens) / n_query_tokens
                if coverage < min_token_coverage:
                    continue  # too few query tokens matched this entry

            # Optional platform filter
            if filter_platform:
                fp = filter_platform.lower().replace("android-xml", "android")
                if not any(fp in str(v).lower() for k, v in row.items() if k.lower() == "platform"):
                    continue
            tagged = {"Domain": domain}
            tagged.update(row)
            all_hits.append((norm_score, tagged))

    # Fallback: coverage filter was too strict (e.g. a generic word like "screen"
    # inflates n_query_tokens so domain-specific terms score below 50% coverage).
    # Retry with at-least-1-token requirement so high-scoring domain entries surface.
    if not all_hits and min_token_coverage > 1.0 / n_query_tokens:
        return search_all_domains(
            query,
            max_results=max_results,
            fuzzy=fuzzy,
            filter_platform=filter_platform,
            min_norm_score=min_norm_score,
            min_token_coverage=1.0 / n_query_tokens,
        )

    # Sort by normalised score descending, then take top N
    all_hits.sort(key=lambda x: x[0], reverse=True)
    results = [row for _, row in all_hits[:max_results]]

    return {
        "domain": "all",
        "query": query,
        "count": len(results),
        "results": results,
        "fuzzy": fuzzy,
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
