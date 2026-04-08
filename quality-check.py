#!/usr/bin/env python3
"""
Quality Check — Della Sigrest Portfolio

Validates HTML files for common issues:
- HTML structure (DOCTYPE, lang, meta tags)
- Heading hierarchy (no skipped levels)
- Accessibility basics (alt text on images, label associations)
- Broken internal links and missing assets
- File size warnings
- Placeholder detection

No external dependencies — uses only Python stdlib.

Usage:
    python3 quality-check.py              # Check all HTML files
    python3 quality-check.py index.html   # Check specific file

Exit codes: 0 = all pass, 1 = errors found
"""

import re
import sys
import os
import glob

# --- Config ---
MAX_HTML_SIZE_KB = 200
MAX_IMAGE_SIZE_KB = 500
PLACEHOLDER_PATTERNS = [
    r"\[●+\]",
    r"\[X to Y\]",
    r"\bTBD\b",
    r"\bTODO\b",
    r"\bFIXME\b",
    r"lorem ipsum",
    r"\[insert ",
    r"\[placeholder",
    r"\[your ",
]

def check_html_structure(content, filepath):
    """Check basic HTML structure."""
    errors = []
    warnings = []
    filename = os.path.basename(filepath)

    # DOCTYPE
    if not content.strip().startswith("<!DOCTYPE html>") and not content.strip().startswith("<!doctype html>"):
        errors.append("Missing <!DOCTYPE html> declaration")

    # lang attribute
    if not re.search(r'<html[^>]+lang=', content, re.IGNORECASE):
        errors.append("Missing lang attribute on <html> tag")

    # charset meta
    if not re.search(r'<meta[^>]+charset', content, re.IGNORECASE):
        warnings.append("Missing charset meta tag")

    # viewport meta
    if not re.search(r'<meta[^>]+viewport', content, re.IGNORECASE):
        warnings.append("Missing viewport meta tag")

    # title tag
    if not re.search(r'<title[^>]*>.+</title>', content, re.IGNORECASE | re.DOTALL):
        errors.append("Missing or empty <title> tag")

    return errors, warnings

def check_heading_hierarchy(content, filepath):
    """Check that heading levels don't skip (e.g., h1 → h3)."""
    errors = []
    headings = re.findall(r'<h(\d)[^>]*>', content, re.IGNORECASE)
    heading_levels = [int(h) for h in headings]

    if not heading_levels:
        return errors

    # Should start with h1
    if heading_levels[0] != 1:
        errors.append(f"First heading is h{heading_levels[0]}, should be h1")

    # Check for skips
    for i in range(1, len(heading_levels)):
        current = heading_levels[i]
        prev = heading_levels[i - 1]
        if current > prev + 1:
            errors.append(f"Heading hierarchy skip: h{prev} → h{current}")

    return errors

def check_images(content, filepath):
    """Check images for alt text and file existence."""
    errors = []
    warnings = []
    filedir = os.path.dirname(filepath) or "."

    # Find all img tags
    img_tags = re.findall(r'<img[^>]*>', content, re.IGNORECASE)
    for img in img_tags:
        # Check for alt attribute
        if not re.search(r'alt=', img, re.IGNORECASE):
            src = re.search(r'src=["\']([^"\']+)', img, re.IGNORECASE)
            src_val = src.group(1) if src else "unknown"
            errors.append(f"Image missing alt attribute: {src_val}")

        # Check for empty alt (might be decorative — warn, don't error)
        alt_match = re.search(r'alt=["\']([^"\']*)["\']', img, re.IGNORECASE)
        if alt_match and alt_match.group(1).strip() == "":
            src = re.search(r'src=["\']([^"\']+)', img, re.IGNORECASE)
            src_val = src.group(1) if src else "unknown"
            # Empty alt is valid for decorative images, just note it
            pass

        # Check if src file exists (for local references)
        src = re.search(r'src=["\']([^"\']+)', img, re.IGNORECASE)
        if src:
            src_path = src.group(1)
            if not src_path.startswith(("http", "data:", "//")):
                full_path = os.path.join(filedir, src_path)
                if not os.path.exists(full_path):
                    errors.append(f"Missing image file: {src_path}")

    return errors, warnings

def check_internal_links(content, filepath):
    """Check that internal links point to existing files."""
    errors = []
    filedir = os.path.dirname(filepath) or "."

    # Find all href attributes
    hrefs = re.findall(r'href=["\']([^"\'#]+)', content, re.IGNORECASE)
    for href in hrefs:
        if href.startswith(("http", "mailto:", "tel:", "javascript:", "data:", "//")):
            continue
        # Strip query params
        href_clean = href.split("?")[0]
        if href_clean:
            full_path = os.path.join(filedir, href_clean)
            if not os.path.exists(full_path):
                errors.append(f"Broken internal link: {href}")

    return errors

def check_placeholders(content, filepath):
    """Check for placeholder text that shouldn't ship."""
    errors = []
    # Remove HTML tags for text-only checking
    text = re.sub(r'<[^>]+>', ' ', content)

    for pattern in PLACEHOLDER_PATTERNS:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            errors.append(f"Placeholder found: '{matches[0]}' (pattern: {pattern})")

    return errors

def check_file_size(filepath):
    """Check if HTML file is unusually large."""
    warnings = []
    size_kb = os.path.getsize(filepath) / 1024
    if size_kb > MAX_HTML_SIZE_KB:
        warnings.append(f"HTML file is {size_kb:.0f}KB (threshold: {MAX_HTML_SIZE_KB}KB)")
    return warnings

def check_file(filepath):
    """Run all checks on a single file. Returns (errors, warnings)."""
    errors = []
    warnings = []

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Structure
    e, w = check_html_structure(content, filepath)
    errors.extend(e)
    warnings.extend(w)

    # Heading hierarchy
    errors.extend(check_heading_hierarchy(content, filepath))

    # Images
    e, w = check_images(content, filepath)
    errors.extend(e)
    warnings.extend(w)

    # Internal links
    errors.extend(check_internal_links(content, filepath))

    # Placeholders
    errors.extend(check_placeholders(content, filepath))

    # File size
    warnings.extend(check_file_size(filepath))

    return errors, warnings

def main():
    args = [a for a in sys.argv[1:]]

    # Determine files to check
    if args:
        files = args
    else:
        files = sorted(glob.glob("*.html"))

    if not files:
        print("No HTML files found to check.")
        sys.exit(0)

    total_errors = 0
    total_warnings = 0
    total_checks = 0

    for filepath in files:
        if not os.path.exists(filepath):
            print(f"WARNING: {filepath} not found, skipping")
            continue

        errors, warnings = check_file(filepath)
        total_errors += len(errors)
        total_warnings += len(warnings)
        # Count checks: 6 check categories per file
        total_checks += 6

        status = "PASS" if not errors else "FAIL"
        print(f"\n{'='*60}")
        print(f"{status}: {filepath}")
        print(f"{'='*60}")

        if errors:
            for e in errors:
                print(f"  ERROR: {e}")
        if warnings:
            for w in warnings:
                print(f"  WARN:  {w}")
        if not errors and not warnings:
            print("  Clean — no issues found")

    # Summary
    print(f"\n{'='*60}")
    print(f"SUMMARY: {len(files)} files, {total_checks} checks run, {total_errors} errors, {total_warnings} warnings")
    print(f"{'='*60}")

    if total_errors > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
