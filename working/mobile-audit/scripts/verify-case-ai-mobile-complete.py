"""
Mark ai06, ai19, ai23 as verified after completing mobile HTML variants on 2026-04-22.

Context:
- ai06 (Evaluation Matrix): built new -v4-mobile.html from Figma node 774:8,
  wrapped iframe in .diagram-pair in case-ai.html.
- ai19 (Attribution Comparison): built new -v4-mobile.html from Figma node 772:8,
  wrapped iframe in .diagram-pair in case-ai.html.
- ai23 (Trust Comparison): already had mobile HTML + .diagram-pair; this pass
  added screenshot verification.

Verification evidence (Phase 4 of thread handoff):
- 480/375/320 standalone mobile crops: all three render cleanly
- ai06: 6 rows × 5 columns, winner column highlighted, all dots visible
- ai19: 3 rows × 5 columns, Hyperlinks winner tag preserved, grade bars render
- ai23: vertical trust spectrum, all 6 tags + HIGH/LOW trust labels visible
- Note: ai06 header "PROMPT D" text gets tight at 320px worst-case but
  data dots (actual content) remain visible; acceptable at extreme breakpoint.

Preserves prior notes (appended with '|' separator).
"""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "tracker_helpers", Path(__file__).parent / "tracker-helpers.py"
)
th = importlib.util.module_from_spec(spec)
spec.loader.exec_module(th)

TRACKER = Path(__file__).parent.parent / "audit-tracker.xlsx"
TODAY = "2026-04-22"

VERIFY_NOTE_PREFIX = (
    "VERIFIED 2026-04-22: mobile HTML variant live in case-ai.html via "
    ".diagram-pair; screenshots at 480/375/320 confirm clean render. | "
)


def main():
    rows = th.read_tracker(TRACKER)
    by_id = {r["diagram_id"]: r for r in rows}

    updates = []
    for did in ("ai06", "ai19", "ai23"):
        row = by_id.get(did)
        if not row:
            raise KeyError(f"No tracker row for {did}")
        prior_notes = row.get("notes") or ""
        new_notes = VERIFY_NOTE_PREFIX + prior_notes
        updates.append((did, {
            "status": "verified",
            "verify_date": TODAY,
            "notes": new_notes,
        }))

    print("Before:")
    for did in ("ai06", "ai19", "ai23"):
        r = by_id[did]
        print(f"  {did}: status={r.get('status')}, verify_date={r.get('verify_date') or '-'}")

    for did, upd in updates:
        th.update_row(TRACKER, did, upd)

    print("\nAfter:")
    rows_after = th.read_tracker(TRACKER)
    by_id_after = {r["diagram_id"]: r for r in rows_after}
    for did in ("ai06", "ai19", "ai23"):
        r = by_id_after[did]
        print(f"  {did}: status={r.get('status')}, verify_date={r.get('verify_date') or '-'}")


if __name__ == "__main__":
    main()
