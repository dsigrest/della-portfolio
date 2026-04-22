"""
Regenerate live-diagrams.md from case study iframe srcs.

Idempotent: safe to run any time. Writes to portfolio-site/working/mobile-audit/live-diagrams.md.
Run from portfolio-site/ root:
    python3 working/mobile-audit/scripts/derive-live-diagrams.py
"""
import re
from pathlib import Path
from datetime import date

CASES = {
    "case-ai.html": "case-ai",
    "case-notifications.html": "case-notifications",
    "case-sharing.html": "case-sharing",
    "case-subreddit.html": "case-subreddit",
    "case-building-portfolio.html": "case-building-portfolio",
}

def main():
    root = Path(__file__).resolve().parents[3]  # portfolio-site/
    out = root / "working/mobile-audit/live-diagrams.md"
    diagrams_dir = root / "img/diagrams"

    lines = [
        "# Live Diagrams Manifest",
        "",
        f"**Auto-derived from case study iframe `src` references. Last regenerated: {date.today().isoformat()}**",
        "",
        "This file is the canonical list of diagrams currently embedded in live case study pages. Orphan diagrams (present in `img/diagrams/` but not referenced) are listed separately at the bottom.",
        "",
        "Regenerate via: `python3 working/mobile-audit/scripts/derive-live-diagrams.py`",
        "",
    ]

    all_refs = set()
    for f, case in CASES.items():
        p = root / f
        if not p.exists():
            continue
        srcs = re.findall(r'src="(img/diagrams/[^"]+\.html)"', p.read_text())
        lines.append(f"## {case} ({len(srcs)} diagrams)")
        lines.append("")
        for s in srcs:
            diagram_id = Path(s).stem.replace("diagram-", "")
            lines.append(f"- `{s}` — id: `{diagram_id}`")
            all_refs.add(Path(s).name)
        lines.append("")

    on_disk = {p.name for p in diagrams_dir.glob("*.html")}
    orphans = sorted(on_disk - all_refs)
    lines.append(f"## Orphans — present in `img/diagrams/` but not referenced ({len(orphans)})")
    lines.append("")
    lines.append("Della's note: these will be added to case studies. Audit them as standalone files; skip container-level analysis since they have no live embed context yet.")
    lines.append("")
    for o in orphans:
        lines.append(f"- `img/diagrams/{o}`")
    lines.append("")

    total_live = len(all_refs)
    lines.append("---")
    lines.append("")
    lines.append(f"**Totals:** {total_live} live diagrams · {len(orphans)} orphans · {total_live + len(orphans)} in-scope")
    lines.append("")

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines))
    print(f"Wrote {out.relative_to(root)} — {total_live} live, {len(orphans)} orphans")

if __name__ == "__main__":
    main()
