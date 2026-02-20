#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mobile Best Practices Search - BM25 search engine for mobile development
Usage: python search.py "<query>" [--domain <domain>] [--platform <platform>] [--stack <stack>] [--persist] [--max-results 3]

Domains: architecture, ui, template, antipattern, reasoning, library, performance, testing, security, snippet, gradle
Platforms: android, ios, flutter, react-native
Stacks: compose, jetpack-compose, material3, hilt, room, kotlin, swiftui, combine, uikit, swift, flutter, dart, bloc, riverpod, react-native, rn, hooks, typescript, redux
"""

import argparse
from core import (
    CSV_CONFIG, AVAILABLE_PLATFORMS, AVAILABLE_STACKS, MAX_RESULTS,
    _CODE_FIELDS, apply_comment_style,
    search, search_platform, search_stack, persist_blueprint
)


_COMMENT_STYLE_CHOICES = ["all", "none", "important"]
_COMMENT_STYLE_DEFAULT = "all"


def _apply_style_to_row(row: dict, style: str) -> dict:
    """Return a copy of *row* with comment style applied to code fields."""
    if style == "all":
        return row
    return {
        k: apply_comment_style(v, style) if k in _CODE_FIELDS else v
        for k, v in row.items()
    }


def format_output(result, compact=False, comment_style=_COMMENT_STYLE_DEFAULT):
    """Format results for Claude consumption (token-optimized)"""
    if "error" in result:
        return f"Error: {result['error']}"

    if compact:
        return format_compact(result, comment_style=comment_style)

    output = []
    if result.get("domain") == "platform":
        output.append(f"## Mobile Best Practices - Platform Guidelines")
        output.append(f"**Platform:** {result['platform']} | **Query:** {result['query']}")
    elif result.get("domain") == "stack":
        output.append(f"## Mobile Best Practices - Stack Search")
        output.append(f"**Stack:** {result['stack']} ({result.get('platform', '')}) | **Query:** {result['query']}")
    else:
        output.append(f"## Mobile Best Practices - Search Results")
        output.append(f"**Domain:** {result['domain']} | **Query:** {result['query']}")

    file_info = result.get('file', '')
    if file_info:
        output.append(f"**Source:** {file_info} | **Found:** {result['count']} results\n")
    else:
        output.append(f"**Found:** {result['count']} results\n")

    if comment_style != "all":
        output.append(f"**Comment style:** {comment_style}\n")

    for i, row in enumerate(result['results'], 1):
        output.append(f"### Result {i}")
        styled = _apply_style_to_row(row, comment_style)
        for key, value in styled.items():
            value_str = str(value)
            if len(value_str) > 300:
                value_str = value_str[:300] + "..."
            output.append(f"- **{key}:** {value_str}")
        output.append("")

    return "\n".join(output)


def format_compact(result, comment_style=_COMMENT_STYLE_DEFAULT):
    """Compact format: fewer tokens, same information density"""
    output = []
    domain = result.get("domain", "")
    query = result.get("query", "")
    count = result.get("count", 0)
    style_tag = f" comment={comment_style}" if comment_style != "all" else ""
    output.append(f"[{domain}] q=\"{query}\" found={count}{style_tag}")

    for i, row in enumerate(result['results'], 1):
        styled = _apply_style_to_row(row, comment_style)
        parts = []
        for key, value in styled.items():
            value_str = str(value).strip()
            if not value_str:
                continue
            if len(value_str) > 200:
                value_str = value_str[:200] + "..."
            parts.append(f"{key}: {value_str}")
        output.append(f"#{i} " + " | ".join(parts))

    return "\n".join(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mobile Best Practices Search")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--domain", "-d", choices=list(CSV_CONFIG.keys()), help="Search domain")
    parser.add_argument("--platform", "-p", choices=AVAILABLE_PLATFORMS, help="Platform-specific search (android, ios, flutter, react-native)")
    parser.add_argument("--stack", "-s", choices=AVAILABLE_STACKS, help="Stack-specific search (compose, swiftui, flutter, react-native, etc.)")
    parser.add_argument("--max-results", "-n", type=int, default=MAX_RESULTS, help="Max results (default: 3)")
    parser.add_argument("--filter-platform", "-fp", choices=AVAILABLE_PLATFORMS, help="Filter any domain results by platform")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--compact", "-c", action="store_true", help="Token-optimized compact output format")
    parser.add_argument(
        "--comment-style", "-cs",
        choices=_COMMENT_STYLE_CHOICES,
        default=_COMMENT_STYLE_DEFAULT,
        help=(
            "Code comment style in output: "
            "'all' = keep all comments (default), "
            "'none' = strip every comment, "
            "'important' = keep only comments with NOTE/WARNING/WHY/IMPORTANT/etc."
        )
    )
    parser.add_argument("--persist", action="store_true", help="Save results to architecture blueprint file")
    parser.add_argument("--project-name", "-pn", help="Project name for blueprint (default: MyApp)")
    parser.add_argument("--page", help="Generate page-specific blueprint override")

    args = parser.parse_args()
    cs = args.comment_style  # shorthand

    # Persist mode
    if args.persist:
        result = persist_blueprint(
            args.query,
            project_name=args.project_name,
            page=args.page
        )
        if args.json:
            import json
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(f"Blueprint saved to: {result['file']}")
            print(f"Sections: {', '.join(result['sections'])}")
            print(f"Total entries: {result['total_entries']}")
    # Stack search
    elif args.stack:
        result = search_stack(args.query, args.stack, args.max_results)
        if args.json:
            import json
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_output(result, compact=args.compact, comment_style=cs))
    # Platform search takes priority
    elif args.platform:
        result = search_platform(args.query, args.platform, args.max_results)
        if args.json:
            import json
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_output(result, compact=args.compact, comment_style=cs))
    else:
        result = search(args.query, args.domain, args.max_results, filter_platform=args.filter_platform)
        if args.json:
            import json
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_output(result, compact=args.compact, comment_style=cs))
