#!/usr/bin/env python3
"""
Voice Consistency Checker — Della Sigrest Portfolio

Checks HTML and Markdown files against banned-patterns.yaml and Register 3
rules to enforce voice consistency.
No external dependencies — uses only Python stdlib.

Usage:
    python3 voice-check.py                  # Check all HTML files
    python3 voice-check.py case-ai.html     # Check specific file
    python3 voice-check.py file.md          # Check markdown file
    python3 voice-check.py --strict         # Treat warnings as errors

Exit codes: 0 = pass, 1 = violations found

Checks:
  1. Banned patterns (from banned-patterns.yaml)
  2. Passive voice ratio
  3. First-person voice (case studies)
  4. Sentence length
  5. Register 3: paragraph length (case studies, max 3 sentences)
  6. Verbal transcription detection (direct quotes in case studies)
  7. Meta-narration patterns (case studies)
  8. Stat duplication (case studies)
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

# --- Text Extractors ---
def extract_visible_text_html(html_content):
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


def extract_visible_text_md(md_content):
    """Extract visible text from Markdown, stripping formatting."""
    text = md_content
    # Remove image placeholders
    text = re.sub(r"\[IMAGE PLACEHOLDER:[^\]]*\]", "", text)
    # Remove markdown headers (but keep the text)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    # Remove bold/italic markers
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    # Remove horizontal rules
    text = re.sub(r"^---+\s*$", "", text, flags=re.MULTILINE)
    # Remove markdown link syntax
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # Collapse whitespace but preserve paragraph breaks (double newline)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # For non-paragraph checks, collapse to single spaces
    return text.strip()


def extract_visible_text(content, filepath):
    """Route to the correct extractor based on file type."""
    if filepath.endswith(".md"):
        return extract_visible_text_md(content)
    else:
        return extract_visible_text_html(content)

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


# --- Register 3 Checks (case studies only) ---

MAX_SENTENCES_PER_PARAGRAPH = 3

def check_paragraph_length(text, filename):
    """Flag paragraphs exceeding Register 3 max (3 sentences) in case study files."""
    is_case_study = any(filename.startswith(prefix) for prefix in CASE_STUDY_PREFIXES)
    if not is_case_study:
        return []

    issues = []
    # For markdown: split on double-newline (natural paragraph breaks)
    # For HTML-extracted text: paragraphs separated by multiple spaces (from <p> tags)
    if filename.endswith(".md"):
        paragraphs = re.split(r"\n\n+", text)
    else:
        paragraphs = re.split(r"\s{3,}", text)
    for para in paragraphs:
        para = para.strip()
        if len(para) < 20:
            continue
        # Count sentences (split on . ! ? followed by space or end)
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", para) if len(s.strip()) > 10]
        if len(sentences) > MAX_SENTENCES_PER_PARAGRAPH:
            preview = " ".join(para.split()[:15]) + "..."
            issues.append(f"Paragraph has {len(sentences)} sentences (max {MAX_SENTENCES_PER_PARAGRAPH} for Register 3): {preview}")
    return issues


def check_direct_quotes(text, filename):
    """Detect verbal transcription leaking into case study prose as direct quotes."""
    is_case_study = any(filename.startswith(prefix) for prefix in CASE_STUDY_PREFIXES)
    if not is_case_study:
        return []

    issues = []
    # Find quoted phrases — these often indicate verbal input pasted directly
    # Match "quoted text" and 'quoted text' (but not single apostrophes in contractions)
    double_quotes = re.findall(r'"([^"]{5,})"', text)
    # Curly quotes
    curly_quotes = re.findall(r'\u201c([^\u201d]{5,})\u201d', text)
    # Straight single quotes used as speech markers (not contractions)
    # Only match if preceded by space/start and followed by space/end
    single_quotes = re.findall(r"(?:^|\s)'([^']{10,})'(?:\s|$|[.,;])", text)

    all_quotes = double_quotes + curly_quotes + single_quotes
    for q in all_quotes:
        # Skip image placeholder descriptions and technical terms
        if q.startswith("IMAGE PLACEHOLDER") or len(q.split()) <= 2:
            continue
        preview = q[:60] + "..." if len(q) > 60 else q
        issues.append(f"Direct quote found (verbal transcription?): \"{preview}\"")
    return issues


# Meta-narration patterns — phrases that narrate the story rather than showing it
META_NARRATION_PATTERNS = [
    (r"\bMy first job was\b", "My first job was"),
    (r"\bWhat we built was\b", "What we built was"),
    (r"\bWhat I learned was\b", "What I learned was"),
    (r"\bThe lesson here is\b", "The lesson here is"),
    (r"\bThis is where I\b", "This is where I"),
    (r"\bThis taught me\b", "This taught me"),
    (r"\bI realized that\b", "I realized that"),
    (r"\bThe takeaway is\b", "The takeaway is"),
    (r"\bLet me explain\b", "Let me explain"),
    (r"\bHere's what happened\b", "Here's what happened"),
    (r"\bThe story is\b", "The story is"),
    (r"\bTo put it simply\b", "To put it simply"),
    (r"\bIn other words\b", "In other words"),
    (r"\bThe point is\b", "The point is"),
]

def check_meta_narration(text, filename):
    """Flag meta-narration patterns that tell rather than show."""
    is_case_study = any(filename.startswith(prefix) for prefix in CASE_STUDY_PREFIXES)
    if not is_case_study:
        return []

    issues = []
    for pattern, label in META_NARRATION_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            issues.append(f"Meta-narration detected: \"{label}\" — show, don't narrate")
    return issues


def check_stat_duplication(text, filename):
    """Flag numbers/stats that appear more than once in body text."""
    is_case_study = any(filename.startswith(prefix) for prefix in CASE_STUDY_PREFIXES)
    if not is_case_study:
        return []

    issues = []
    # Find significant numbers (with context like %, pp, M, K, or day/week references)
    stats = re.findall(r"\b(\d+(?:\.\d+)?)\s*(%|pp|percentage points?|M\b|K\b)", text)
    # Also match patterns like "day 7", "~10", "90%"
    stats += re.findall(r"[~≈]?(\d+(?:\.\d+)?)\s*(%|pp|percentage points?)", text)

    # Count occurrences of each stat+unit pair
    from collections import Counter
    stat_counts = Counter(stats)
    for (num, unit), count in stat_counts.items():
        if count > 1:
            issues.append(f"Stat appears {count}x: {num}{unit} — each stat should appear once in Register 3")
    return issues

# --- Main Check ---
def check_file(filepath, patterns, strict=False):
    """Run all checks on a single HTML file. Returns (errors, warnings)."""
    errors = []
    warnings = []

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    text = extract_visible_text(content, filepath)
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

    # 5. Register 3: Paragraph length (case studies)
    para_issues = check_paragraph_length(text, filename)
    for p in para_issues:
        warnings.append(f"Register 3: {p}")

    # 6. Direct quote / verbal transcription detection (case studies)
    quote_issues = check_direct_quotes(text, filename)
    for q in quote_issues:
        errors.append(f"Verbal transcription: {q}")

    # 7. Meta-narration patterns (case studies)
    meta_issues = check_meta_narration(text, filename)
    for m in meta_issues:
        errors.append(f"Register 3: {m}")

    # 8. Stat duplication (case studies)
    stat_issues = check_stat_duplication(text, filename)
    for s in stat_issues:
        warnings.append(f"Register 3: {s}")

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
        print("No HTML or Markdown files found to check.")
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
