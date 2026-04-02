#!/usr/bin/env python3
"""
Voice Consistency Checker — Della Sigrest Portfolio

Checks HTML files against banned-patterns.yaml to enforce voice consistency.
No external dependencies — uses only Python stdlib.

Usage:
    python3 voice-check.py                  # Check all HTML files
    python3 voice-check.py case-ai.html     # Check specific file
    python3 voice-check.py --strict         # Treat warnings as errors

Exit codes: 0 = pass, 1 = violations found
"""

import re
import sys
import os
import glob

# --- Config ---
YAML_PATH = os.path.join(os.path.dirname(__file__), "voice-rules", "banned-patterns.yaml")
PASSIVE_WARN_THRESHOLD = 0.40
PASSIVE_ERROR_THRESHOLD = 0.60
MAX_SENTENCE_WORDS = 35
CASE_STUDY_PREFIXES = ["case-"]

# --- YAML Parser (no PyYAML dependency) ---
def parse_banned_patterns(filepath):
    """Parse banned-patterns.yaml without PyYAML."""
    patterns = []
    if not os.path.exists(filepath):
        print(f"WARNING: {filepath} not found — skipping banned pattern checks")
        return patterns

    with open(filepath, "r") as f:
        lines = f.readlines()

    current = {}
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#") or stripped == "" or stripped == "patterns:":
            continue

        if stripped.startswith("- pattern:"):
            if current:
                patterns.append(current)
            value = stripped.split("- pattern:", 1)[1].strip().strip('"').strip("'")
            current = {"pattern": value}
        elif stripped.startswith("category:") and current:
            current["category"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("severity:") and current:
            current["severity"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("replacement:") and current:
            current["replacement"] = stripped.split(":", 1)[1].strip().strip('"').strip("'")

    if current:
        patterns.append(current)

    return patterns

# --- HTML Text Extractor ---
def extract_visible_text(html_content):
    """Extract visible text from HTML, skipping script/style tags."""
    # Remove script and style blocks
    text = re.sub(r"<script[^>]*>.*?</script>", "", html_content, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<style[^>]*>.*?</style>", "", html_content, flags=re.DOTALL | re.IGNORECASE)
    # Remove HTML comments
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    # Remove HTML tags
    text = re.sub(r"<[^>]+>", " ", text)
    # Decode common entities
    text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    text = text.replace("&nbsp;", " ").replace("&mdash;", "—").replace("&ndash;", "–")
    text = text.replace("&#8217;", "'").replace("&rsquo;", "'").replace("&lsquo;", "'")
    text = text.replace("&rdquo;", '"').replace("&ldquo;", '"')
    # Collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text

# --- Passive Voice Detector ---
PASSIVE_PATTERN = re.compile(
    r"\b(is|are|was|were|been|being|be)\s+(being\s+)?"
    r"(accepted|accomplished|achieved|added|adjusted|administered|affected|allowed|"
    r"analyzed|applied|approved|arranged|assessed|assigned|avoided|balanced|based|"
    r"believed|broken|brought|built|called|caused|changed|chosen|closed|combined|"
    r"compared|completed|composed|concerned|conducted|confirmed|connected|considered|"
    r"controlled|converted|convinced|created|damaged|decided|defined|delivered|"
    r"demonstrated|deployed|described|designed|determined|developed|directed|"
    r"discovered|discussed|displayed|distributed|documented|done|driven|dropped|"
    r"employed|enabled|encouraged|enhanced|ensured|established|evaluated|examined|"
    r"exceeded|executed|expanded|expected|experienced|explained|explored|expressed|"
    r"extended|facilitated|featured|fixed|focused|followed|forced|formed|found|"
    r"generated|given|gone|governed|grouped|grown|guided|handled|held|helped|hidden|"
    r"identified|ignored|implemented|improved|included|increased|influenced|informed|"
    r"inspired|installed|integrated|intended|introduced|investigated|involved|issued|"
    r"joined|judged|justified|kept|known|launched|led|left|limited|linked|located|"
    r"lost|made|maintained|managed|measured|met|modified|monitored|motivated|moved|"
    r"named|needed|neglected|noted|observed|obtained|offered|opened|operated|"
    r"optimized|ordered|organized|outlined|overcome|owned|paid|perceived|performed|"
    r"permitted|placed|planned|positioned|powered|prepared|presented|prevented|"
    r"prioritized|processed|produced|programmed|promoted|proposed|protected|proved|"
    r"provided|published|purchased|pursued|put|raised|reached|realized|received|"
    r"recognized|recommended|recorded|reduced|referred|reflected|regarded|rejected|"
    r"related|released|removed|replaced|reported|represented|required|researched|"
    r"resolved|respected|restricted|retained|revealed|reviewed|revised|rewarded|run|"
    r"saved|scheduled|secured|seen|selected|sent|separated|served|set|shared|shifted|"
    r"shipped|shown|simplified|solved|sorted|specified|spent|split|started|stated|"
    r"stored|strengthened|structured|studied|submitted|suggested|summarized|supported|"
    r"surrounded|taken|targeted|taught|tested|thought|told|tracked|trained|"
    r"transferred|transformed|translated|treated|turned|understood|unified|updated|"
    r"upgraded|used|utilized|validated|valued|viewed|visited|wanted|warned|watched|"
    r"weakened|widened|won|worked|written)\b",
    re.IGNORECASE,
)

def check_passive_voice(text):
    """Return passive voice ratio and matches."""
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
    if not sentences:
        return 0.0, []

    passive_sentences = []
    for s in sentences:
        if PASSIVE_PATTERN.search(s):
            passive_sentences.append(s[:80] + "..." if len(s) > 80 else s)

    ratio = len(passive_sentences) / len(sentences)
    return ratio, passive_sentences

# --- First Person Check ---
def check_first_person(text, filename):
    """Check that case studies use first person voice."""
    is_case_study = any(filename.startswith(prefix) for prefix in CASE_STUDY_PREFIXES)
    if not is_case_study:
        return []

    issues = []
    # Check for third-person patterns that should be first-person
    third_person = re.findall(r"\b(The designer|The team lead|She designed|She built|She led)\b", text, re.IGNORECASE)
    if third_person:
        issues.append(f"Third-person voice found in case study: {', '.join(set(third_person))}")
    return issues

# --- Long Sentence Check ---
def check_sentence_length(text):
    """Flag sentences over MAX_SENTENCE_WORDS words."""
    sentences = re.split(r"[.!?]+", text)
    long_sentences = []
    for s in sentences:
        words = s.strip().split()
        if len(words) > MAX_SENTENCE_WORDS:
            preview = " ".join(words[:10]) + "..."
            long_sentences.append(f"({len(words)} words) {preview}")
    return long_sentences

# --- Main Check ---
def check_file(filepath, patterns, strict=False):
    """Run all checks on a single HTML file. Returns (errors, warnings)."""
    errors = []
    warnings = []

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    text = extract_visible_text(content)
    filename = os.path.basename(filepath)

    # 1. Banned patterns
    for p in patterns:
        try:
            regex = re.compile(p["pattern"], re.IGNORECASE)
        except re.error:
            warnings.append(f"Invalid regex in banned-patterns.yaml: {p['pattern']}")
            continue

        matches = regex.findall(text)
        if matches:
            severity = p.get("severity", "error")
            msg = f"[{p['category']}] '{p['pattern']}' found ({len(matches)}x) → {p.get('replacement', 'Remove')}"
            if severity == "error" or strict:
                errors.append(msg)
            else:
                warnings.append(msg)

    # 2. Passive voice
    ratio, passive_examples = check_passive_voice(text)
    if ratio >= PASSIVE_ERROR_THRESHOLD:
        errors.append(f"Passive voice at {ratio:.0%} (threshold: {PASSIVE_ERROR_THRESHOLD:.0%})")
        for ex in passive_examples[:3]:
            errors.append(f"  Example: {ex}")
    elif ratio >= PASSIVE_WARN_THRESHOLD:
        warnings.append(f"Passive voice at {ratio:.0%} (threshold: {PASSIVE_WARN_THRESHOLD:.0%})")

    # 3. First person (case studies only)
    fp_issues = check_first_person(text, filename)
    errors.extend(fp_issues)

    # 4. Sentence length
    long = check_sentence_length(text)
    for l in long:
        warnings.append(f"Long sentence: {l}")

    return errors, warnings

def main():
    strict = "--strict" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--strict"]

    # Load patterns
    patterns = parse_banned_patterns(YAML_PATH)
    print(f"Loaded {len(patterns)} banned patterns from {YAML_PATH}")

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

    for filepath in files:
        if not os.path.exists(filepath):
            print(f"WARNING: {filepath} not found, skipping")
            continue

        errors, warnings = check_file(filepath, patterns, strict)
        total_errors += len(errors)
        total_warnings += len(warnings)

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
    print(f"SUMMARY: {len(files)} files checked, {total_errors} errors, {total_warnings} warnings")
    print(f"{'='*60}")

    if total_errors > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
