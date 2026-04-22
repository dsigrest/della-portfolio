"""
Clean up tracker state for 4 case-ai rows after 2026-04-22 re-verification.

Prior session marked ai06/ai19/ai23/ai24 status=fixed with notes claiming
visual verification, but re-inspection of the screenshot corpus revealed:
- ai06: clips at 375/320 (no mobile HTML file exists; only Figma frame)
- ai19: clips at 375/320 (same — Figma frame only, no HTML)
- ai23: proper .diagram-pair + mobile HTML exists, but no mobile screenshot
  was captured in the current pass (safety-net was case-sharing only)
- ai24: genuinely reflows correctly at 375/320 (verified)

Action:
- ai24 → status=verified (confirmed clean by fresh inspection)
- ai06 → status=audited (downgrade — needs HTML mobile variant)
- ai19 → status=audited (downgrade — needs HTML mobile variant)
- ai23 → stay status=fixed (infrastructure correct, just needs screenshot verify)

The case-ai-mobile-completion-prompt.md handoff doc explains the remaining
work for a separate thread.
"""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "tracker_helpers", Path(__file__).parent / "tracker-helpers.py"
)
th = importlib.util.module_from_spec(spec)
spec.loader.exec_module(th)

TRACKER = "audit-tracker.xlsx"
TODAY = "2026-04-22"

# Preserve prior notes; prepend re-verification diagnostic.
AI06_NOTES = (
    "NEEDS FIX 2026-04-22: re-verification found clipping at 375/320 — 5 columns "
    "(Parameter + Prompt A/B/C/D) overflow because .diagram has fixed width:760px "
    "and no -mobile.html variant exists. Figma mobile frame at 774:8 was prior "
    "session's only mobile output. To finish: follow ai23 pattern (create "
    "-v4-mobile.html via figma-to-html from node 774:8, wrap iframe in "
    ".diagram-pair in case-ai.html). See case-ai-mobile-completion-prompt.md. | "
    "Prior 2026-04-21: Verified visually at 480/375/320 — all 4 prompt columns + "
    "param column fit; PROMPT D header wraps to 2 lines at 320, all dots visible. "
    "Figma mobile frame paired at (-420, -8774, 375x462) via byte-array transport. "
    "HTML-to-Figma translation complete; native layers replacing image fill; "
    "image backup at ai06-mobile-imageref."
)

AI19_NOTES = (
    "NEEDS FIX 2026-04-22: re-verification found clipping at 375/320 — 5 columns "
    "(Pattern + Trust/Visibility/Space + status) overflow because .diagram has "
    "fixed-width desktop layout and no -mobile.html variant exists. Figma mobile "
    "frame at 772:8 was prior session's only mobile output. To finish: follow "
    "ai23 pattern (create -v4-mobile.html via figma-to-html from node 772:8, "
    "wrap iframe in .diagram-pair in case-ai.html). See "
    "case-ai-mobile-completion-prompt.md. | Prior 2026-04-21: Verified visually "
    "at 480/375/320 — all 5 columns visible at every breakpoint, Hyperlinks "
    "Winner highlight preserved. Figma mobile frame paired at (-420, 1643, "
    "375x169) via byte-array transport. HTML-to-Figma translation complete; "
    "native layers replacing image fill; image backup at ai19-mobile-imageref."
)

UPDATES = [
    ("ai06", {
        "status": "audited",
        "verify_date": "",  # clear — verification failed
        "notes": AI06_NOTES,
    }),
    ("ai19", {
        "status": "audited",
        "verify_date": "",
        "notes": AI19_NOTES,
    }),
    ("ai24", {
        "status": "verified",
        "verify_date": TODAY,
    }),
    # ai23: leave as status=fixed. Will flip to verified once completion thread
    # runs screenshot-diagrams.py case-ai and visually confirms mobile variant.
]


def main():
    before = {r["diagram_id"]: (r.get("status"), r.get("verify_date"))
              for r in th.read_tracker(TRACKER)
              if r.get("diagram_id") in ("ai06", "ai19", "ai23", "ai24")}

    for diagram_id, updates in UPDATES:
        th.update_row(TRACKER, diagram_id, updates)
        print(f"  {diagram_id}: {updates}")

    after = {r["diagram_id"]: (r.get("status"), r.get("verify_date"))
             for r in th.read_tracker(TRACKER)
             if r.get("diagram_id") in ("ai06", "ai19", "ai23", "ai24")}

    print("\nBefore → After:")
    for did in ("ai06", "ai19", "ai23", "ai24"):
        b = before.get(did, ("?", "?"))
        a = after.get(did, ("?", "?"))
        print(f"  {did:8s}  {b[0]:10s} ({b[1] or '-':10s})  →  {a[0]:10s} ({a[1] or '-':10s})")


if __name__ == "__main__":
    main()
