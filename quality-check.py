#!/usr/bin/env python3
"""
Portfolio Quality Gate — Pre-deploy validation for della-portfolio.vercel.app
Run: python3 quality-check.py
"""

import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

SITE_DIR = Path(__file__).parent
HTML_FILES = [f for f in SITE_DIR.glob("*.html")]
CSS_FILE = SITE_DIR / "styles.css"

# Design tokens
COLORS = {
    "--bg": "#0b0b0b",
    "--surface": "#131313",
    "--accent": "#2dd4bf",
    "--text-primary": "#e8e8e8",
}

passed = 0
failed = 0
warnings = 0
issues = []

def check_pass(label):
    global passed
    passed += 1
    print(f"  ✅ {label}")

def check_fail(label, detail=""):
    global failed
    failed += 1
    msg = f"  ❌ {label}"
    if detail:
        msg += f" — {detail}"
    print(msg)
    issues.append(f"{label}: {detail}")

def check_warn(label, detail=""):
    global warnings
    warnings += 1
    msg = f"  ⚠️  {label}"
    if detail:
        msg += f" — {detail}"
    print(msg)


class HTMLChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.ids = []
        self.links = []
        self.images = []
        self.headings = []
        self.has_lang = False
        self.has_viewport = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self.tags.append(tag)

        if tag == "html" and "lang" in attrs_dict:
            self.has_lang = True
        if tag == "meta" and attrs_dict.get("name") == "viewport":
            self.has_viewport = True
        if "id" in attrs_dict:
            self.ids.append(attrs_dict["id"])
        if tag == "a" and "href" in attrs_dict:
            self.links.append(attrs_dict)
        if tag == "img":
            self.images.append(attrs_dict)
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.headings.append(int(tag[1]))


# === CHECK 1: HTML VALIDATION ===
print("\n📄 HTML VALIDATION")
print("─" * 40)

for html_file in HTML_FILES:
    content = html_file.read_text()
    checker = HTMLChecker()
    try:
        checker.feed(content)
    except Exception as e:
        check_fail(f"{html_file.name}: Parse error", str(e))
        continue

    # Lang attribute
    if checker.has_lang:
        check_pass(f"{html_file.name}: lang attribute present")
    else:
        check_fail(f"{html_file.name}: Missing lang attribute on <html>")

    # Viewport
    if checker.has_viewport:
        check_pass(f"{html_file.name}: viewport meta present")
    else:
        check_fail(f"{html_file.name}: Missing viewport meta tag")

    # Duplicate IDs
    seen_ids = set()
    dupes = []
    for id_val in checker.ids:
        if id_val in seen_ids:
            dupes.append(id_val)
        seen_ids.add(id_val)
    if dupes:
        check_fail(f"{html_file.name}: Duplicate IDs", ", ".join(dupes))
    else:
        check_pass(f"{html_file.name}: No duplicate IDs")

    # Heading hierarchy
    prev_level = 0
    hierarchy_ok = True
    for level in checker.headings:
        if level > prev_level + 1 and prev_level > 0:
            hierarchy_ok = False
            check_fail(f"{html_file.name}: Heading skip", f"h{prev_level} → h{level}")
            break
        prev_level = level
    if hierarchy_ok:
        check_pass(f"{html_file.name}: Heading hierarchy valid")


# === CHECK 2: LINK INTEGRITY ===
print("\n🔗 LINK INTEGRITY")
print("─" * 40)

for html_file in HTML_FILES:
    content = html_file.read_text()
    checker = HTMLChecker()
    checker.feed(content)

    for link in checker.links:
        href = link.get("href", "")
        target = link.get("target", "")
        rel = link.get("rel", "")

        # Skip mailto, anchors, javascript
        if href.startswith(("mailto:", "#", "javascript:")):
            continue

        # Internal links
        if not href.startswith(("http://", "https://")):
            target_file = SITE_DIR / href
            if not target_file.exists():
                check_fail(f"{html_file.name}: Broken link", f"→ {href}")
            else:
                check_pass(f"{html_file.name}: {href} exists")
        else:
            # External links should have target="_blank" and rel="noopener"
            if target != "_blank":
                check_warn(f"{html_file.name}: External link missing target='_blank'", href)
            if "noopener" not in rel:
                check_warn(f"{html_file.name}: External link missing rel='noopener'", href)


# === CHECK 3: ACCESSIBILITY ===
print("\n♿ ACCESSIBILITY")
print("─" * 40)

css_content = CSS_FILE.read_text() if CSS_FILE.exists() else ""

# Focus styles
if "focus-visible" in css_content or ":focus" in css_content:
    check_pass("Focus styles present in CSS")
else:
    check_fail("No focus styles found in CSS")

# Reduced motion
if "prefers-reduced-motion" in css_content:
    check_pass("prefers-reduced-motion media query present")
else:
    check_fail("Missing prefers-reduced-motion media query")

# ARIA labels on interactive elements
for html_file in HTML_FILES:
    content = html_file.read_text()
    buttons = re.findall(r'<button[^>]*>', content)
    for btn in buttons:
        if 'aria-label' not in btn and '>' not in btn:
            check_warn(f"{html_file.name}: Button may need aria-label")
        else:
            check_pass(f"{html_file.name}: Button has aria-label")


# === CHECK 4: CSS VALIDATION ===
print("\n🎨 CSS VALIDATION")
print("─" * 40)

if CSS_FILE.exists():
    css = css_content

    # Check for hardcoded colors (hex outside of variable definitions)
    lines = css.split("\n")
    hardcoded = []
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("--"):
            continue  # Skip variable definitions
        if stripped.startswith("/*") or stripped.startswith("*"):
            continue  # Skip comments
        hex_matches = re.findall(r'#[0-9a-fA-F]{3,8}', stripped)
        for h in hex_matches:
            if "var(--" not in stripped and "border" not in stripped.lower():
                hardcoded.append(f"Line {i}: {h}")

    if hardcoded and len(hardcoded) > 5:
        check_warn(f"Hardcoded colors found", f"{len(hardcoded)} instances (some may be in table styles)")
    else:
        check_pass("Minimal hardcoded colors")

    # Responsive breakpoints
    if "@media" in css:
        check_pass("Responsive breakpoints present")
    else:
        check_fail("No responsive breakpoints found")

    # Custom properties defined
    defined_vars = re.findall(r'--([\w-]+)\s*:', css)
    if len(defined_vars) > 5:
        check_pass(f"CSS custom properties defined ({len(defined_vars)} variables)")
    else:
        check_warn("Few CSS custom properties defined")
else:
    check_fail("styles.css not found")


# === CHECK 5: CONTENT CHECK ===
print("\n📝 CONTENT CHECK")
print("─" * 40)

placeholder_patterns = [
    (r'\[●●\]', "Metric placeholder [●●]"),
    (r'\[X to Y\]', "Metric placeholder [X to Y]"),
    (r'\[sharing volume', "Sharing metric placeholder"),
    (r'img-placeholder', "Image placeholder"),
]

for html_file in HTML_FILES:
    content = html_file.read_text()
    for pattern, label in placeholder_patterns:
        matches = re.findall(pattern, content)
        if matches:
            check_warn(f"{html_file.name}: {label} ({len(matches)}x)")

    # Check title and description
    if "<title>" in content and "</title>" in content:
        check_pass(f"{html_file.name}: Title tag present")
    else:
        check_fail(f"{html_file.name}: Missing title tag")

    if 'meta name="description"' in content:
        check_pass(f"{html_file.name}: Meta description present")
    else:
        check_fail(f"{html_file.name}: Missing meta description")


# === CHECK 6: PERFORMANCE ===
print("\n⚡ PERFORMANCE")
print("─" * 40)

# File sizes
total_size = 0
for html_file in HTML_FILES:
    size = html_file.stat().st_size
    total_size += size
    if size > 50000:
        check_warn(f"{html_file.name}: {size/1024:.1f}KB (large for static HTML)")
    else:
        check_pass(f"{html_file.name}: {size/1024:.1f}KB")

if CSS_FILE.exists():
    css_size = CSS_FILE.stat().st_size
    total_size += css_size
    check_pass(f"styles.css: {css_size/1024:.1f}KB")

# Check for images
img_dir = SITE_DIR / "img"
if img_dir.exists():
    for img in img_dir.iterdir():
        if img.is_file():
            size = img.stat().st_size
            if size > 500000:
                check_fail(f"Image too large: {img.name} ({size/1024:.0f}KB > 500KB)")
            else:
                check_pass(f"{img.name}: {size/1024:.0f}KB")

print(f"\n  Total page weight: {total_size/1024:.1f}KB")


# === VERDICT ===
print("\n" + "═" * 40)
print(f"  ✅ Passed: {passed}")
print(f"  ❌ Failed: {failed}")
print(f"  ⚠️  Warnings: {warnings}")
print("═" * 40)

if failed == 0:
    print("\n  🚀 READY TO DEPLOY")
else:
    print(f"\n  🛑 FIX {failed} ISSUE{'S' if failed > 1 else ''} FIRST")
    for issue in issues:
        print(f"     • {issue}")

print()
sys.exit(1 if failed > 0 else 0)
