#!/usr/bin/env python3
"""Bug 1 fix — eliminate the visible faint frame around iframe-embedded
diagrams by matching body bg to .diagram bg.

The previous pattern set body bg to #08090F and .diagram bg to var(--canvas)
(#0A0C16). The 2-shade differential reads as a faint frame around the
diagram inside the iframe. Matching the two eliminates the ring entirely.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIAG_DIR = ROOT / "img" / "diagrams"

def fix(path: Path) -> str:
    txt = path.read_text(encoding="utf-8")
    # Find .diagram bg
    m_diag = re.search(
        r'^\s*\.diagram\s*\{[^}]*?background:\s*([^;\n]+)\s*;',
        txt, re.MULTILINE | re.DOTALL,
    )
    if not m_diag:
        return "no-diagram-bg"
    diag_bg = m_diag.group(1).strip()

    # Find body bg
    m_body = re.search(
        r'(^\s*body\s*\{[^}]*?background:\s*)([^;\n]+)(\s*;)',
        txt, re.MULTILINE | re.DOTALL,
    )
    if not m_body:
        return "no-body-bg"
    body_bg = m_body.group(2).strip()
    if body_bg == diag_bg:
        return "already-matched"

    new_txt = txt[:m_body.start(2)] + diag_bg + txt[m_body.end(2):]
    path.write_text(new_txt, encoding="utf-8")
    return f"changed: body bg {body_bg} -> {diag_bg}"


def main():
    files = sorted(DIAG_DIR.glob("diagram-not*-v5.html"))
    for f in files:
        # skip mobile siblings
        if "-mobile" in f.name:
            continue
        result = fix(f)
        print(f"  {f.name}: {result}")


if __name__ == "__main__":
    main()
