#!/usr/bin/env python3
"""
Voice consistency linter for Della Sigrest's content.

Reads banned patterns from ../voice-rules/banned-patterns.yaml (single source of truth)
and checks all HTML files for violations.

Usage:
    python3 voice-check.py                  # Check all HTML files
    python3 voice-check.py case-ai.html     # Check specific file
    python3 voice-check.py --strict         # Treat warnings as errors

Exit codes:
    0 = pass (no errors, warnings OK)
    1 = fail (errors found)
"""

import re
import sys
import os
from pathlib import Path
from html.parser import HTMLParser

# ─── Configuration ───────────────────────────────────────────────────────────

PATTERNS_FILE = os.path.join(os.path.dirname(__file__), '..', 'voice-rules', 'banned-patterns.yaml')
MAX_SENTENCE_LENGTH = 35  # words
PASSIVE_VOICE_THRESHOLD_WARN = 0.40
PASSIVE_VOICE_THRESHOLD_ERROR = 0.60

# ─── Minimal YAML parser (no dependencies) ───────────────────────────────────

def parse_banned_patterns(filepath):
    """Parse the banned-patterns.yaml without PyYAML dependency."""
    patterns = []
    if not os.path.exists(filepath):
        print(f"  ⚠️  Patterns file not found: {filepath}")
        return patterns

    with open(filepath, 'r') as f:
        lines = f.readlines()

    current = {}
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#') or stripped == '' or stripped == 'patterns:':
            continue
        if stripped.startswith('- pattern:'):
            if current.get('pattern'):
                patterns.append(current)
            value = stripped.replace('- pattern:', '').strip().strip('"').strip("'")
            current = {'pattern': value, 'category': '', 'severity': 'warning', 'replacement': ''}
        elif stripped.startswith('category:'):
            current['category'] = stripped.replace('category:', '').strip().strip('"').strip("'")
        elif stripped.startswith('severity:'):
            current['severity'] = stripped.replace('severity:', '').strip().strip('"').strip("'")
        elif stripped.startswith('replacement:'):
            current['replacement'] = stripped.replace('replacement:', '').strip().strip('"').strip("'")

    if current.get('pattern'):
        patterns.append(current)

    return patterns


# ─── HTML text extractor ─────────────────────────────────────────────────────

class TextExtractor(HTMLParser):
    """Extract visible text from HTML, skipping script/style tags."""
    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.skip_tags = {'script', 'style', 'noscript'}
        self.current_skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self.current_skip += 1

    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.current_skip = max(0, self.current_skip - 1)

    def handle_data(self, data):
        if self.current_skip == 0:
            self.text_parts.append(data)

    def get_text(self):
        return ' '.join(self.text_parts)


def extract_text(html_content):
    """Extract visible text from HTML content."""
    parser = TextExtractor()
    parser.feed(html_content)
    return parser.get_text()


# ─── Passive voice detection (regex-based, no NLP dependency) ────────────────

PASSIVE_PATTERNS = [
    r'\b(?:is|are|was|were|been|being)\s+(?:\w+ly\s+)?(?:\w+ed|built|designed|made|done|shown|seen|known|given|taken|found|thought|told|written|broken|chosen|driven|spoken|stolen|worn|born|torn|sworn|grown|thrown|drawn|blown|flown|frozen|hidden|ridden|risen|shaken|forgotten|gotten|bitten|eaten|beaten|fallen|forgiven|mistaken|undertaken)\b',
]

def estimate_passive_voice_ratio(text):
    """Estimate the ratio of sentences using passive voice."""
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
    if not sentences:
        return 0.0

    passive_count = 0
    for sentence in sentences:
        for pattern in PASSIVE_PATTERNS:
            if re.search(pattern, sentence, re.IGNORECASE):
                passive_count += 1
                break

    return passive_count / len(sentences)


# ─── First person check ─────────────────────────────────────────────────────

def check_first_person(text, filename):
    """Check if case studies use first person voice."""
    issues = []
    if not filename.startswith('case-'):
        return issues

    # Look for third-person patterns that should be first-person
    third_person = re.findall(r'\b(?:The designer|The team lead|She designed|She built)\b', text, re.IGNORECASE)
    if third_person:
        for match in third_person:
            issues.append({
                'severity': 'warning',
                'message': f'Third-person reference in case study: "{match}" — use first person',
                'category': 'tone'
            })

    # Check if there's any first-person usage at all
    first_person = re.findall(r'\bI (?:designed|built|led|created|shipped|defined|partnered|prototyped|synthesized|proposed|conducted|ran)\b', text, re.IGNORECASE)
    if not first_person and 'case-building' not in filename:
        issues.append({
            'severity': 'warning',
            'message': 'No first-person action verbs found in case study — add "I designed/built/led" language',
            'category': 'tone'
        })

    return issues


# ─── Long sentence check ────────────────────────────────────────────────────

def check_sentence_length(text):
    """Flag sentences over the max word count."""
    issues = []
    sentences = re.split(r'[.!?]+', text)
    long_count = 0
    for sentence in sentences:
        words = sentence.strip().split()
        if len(words) > MAX_SENTENCE_LENGTH:
            long_count += 1

    if long_count > 3:
        issues.append({
            'severity': 'warning',
            'message': f'{long_count} sentences over {MAX_SENTENCE_LENGTH} words — consider breaking up for readability',
            'category': 'structural'
        })
    return issues


# ─── Main checker ────────────────────────────────────────────────────────────

def check_file(filepath, patterns, strict=False):
    """Run all voice checks on a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()

    text = extract_text(html_content)
    filename = os.path.basename(filepath)
    errors = []
    warnings = []

    # 1. Check banned patterns
    for p in patterns:
        try:
            matches = re.findall(p['pattern'], text, re.IGNORECASE)
        except re.error:
            continue

        if matches:
            for match in matches:
                entry = {
                    'severity': p['severity'],
                    'message': f"Banned pattern ({p['category']}): \"{match}\" → {p['replacement']}",
                    'category': p['category']
                }
                if p['severity'] == 'error' or strict:
                    errors.append(entry)
                else:
                    warnings.append(entry)

    # 2. Passive voice ratio
    passive_ratio = estimate_passive_voice_ratio(text)
    if passive_ratio > PASSIVE_VOICE_THRESHOLD_ERROR:
        errors.append({
            'severity': 'error',
            'message': f'Passive voice at {passive_ratio:.0%} (threshold: {PASSIVE_VOICE_THRESHOLD_ERROR:.0%}) — rewrite in active voice',
            'category': 'tone'
        })
    elif passive_ratio > PASSIVE_VOICE_THRESHOLD_WARN:
        warnings.append({
            'severity': 'warning',
            'message': f'Passive voice at {passive_ratio:.0%} (threshold: {PASSIVE_VOICE_THRESHOLD_WARN:.0%}) — consider more active voice',
            'category': 'tone'
        })

    # 3. First person check
    fp_issues = check_first_person(text, filename)
    for issue in fp_issues:
        if issue['severity'] == 'error' or strict:
            errors.append(issue)
        else:
            warnings.append(issue)

    # 4. Sentence length
    sl_issues = check_sentence_length(text)
    for issue in sl_issues:
        if strict:
            errors.append(issue)
        else:
            warnings.append(issue)

    return errors, warnings


# ─── Output formatting ──────────────────────────────────────────────────────

def print_results(filename, errors, warnings):
    """Print formatted results for a file."""
    if not errors and not warnings:
        print(f"  ✅ {filename}: Voice check passed")
        return

    for e in errors:
        print(f"  ❌ {filename}: {e['message']}")
    for w in warnings:
        print(f"  ⚠️  {filename}: {w['message']}")


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    strict = '--strict' in sys.argv
    specific_files = [a for a in sys.argv[1:] if not a.startswith('--')]

    # Load patterns
    patterns = parse_banned_patterns(PATTERNS_FILE)
    if not patterns:
        print("  ⚠️  No patterns loaded — check banned-patterns.yaml")

    print(f"\n🗣️  VOICE CONSISTENCY CHECK")
    print(f"{'─' * 40}")
    print(f"  Loaded {len(patterns)} patterns from banned-patterns.yaml")
    if strict:
        print(f"  Mode: STRICT (warnings treated as errors)")
    print()

    # Find files to check
    if specific_files:
        html_files = [Path(f) for f in specific_files if f.endswith('.html')]
    else:
        html_files = sorted(Path('.').glob('*.html'))

    if not html_files:
        print("  No HTML files found to check.")
        sys.exit(0)

    total_errors = 0
    total_warnings = 0

    for filepath in html_files:
        if not filepath.exists():
            print(f"  ⚠️  File not found: {filepath}")
            continue

        errors, warnings = check_file(str(filepath), patterns, strict)
        print_results(filepath.name, errors, warnings)
        total_errors += len(errors)
        total_warnings += len(warnings)

    # Summary
    print(f"\n{'═' * 40}")
    print(f"  ✅ Files checked: {len(html_files)}")
    print(f"  ❌ Errors: {total_errors}")
    print(f"  ⚠️  Warnings: {total_warnings}")
    print(f"{'═' * 40}")

    if total_errors > 0:
        print(f"\n  🛑 VOICE CHECK FAILED — fix {total_errors} error(s)")
        sys.exit(1)
    else:
        print(f"\n  ✅ VOICE CHECK PASSED")
        sys.exit(0)


if __name__ == '__main__':
    main()
