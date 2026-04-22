"""
Seed 8 rows for the SHR UI screens mobile pass (shr01/02/06/07/08/10/11/12).

Each screen got a v4 responsive HTML file under Get-a-job/working/diagrams/v4/
with a recipe-based L2 fix (Recipe A: phone+annotations, Recipe B: carousel,
Recipe C: stacked grids). All 8 verified via Playwright: zero horizontal
overflow at 240/320/375, pass quality-check and voice-check.

Figma mobile pairing is deferred to Thread B — figma_mobile_node_id stays None
until Thread B executes.
"""
import importlib.util
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "tracker_helpers",
    Path(__file__).parent / "tracker-helpers.py",
)
th = importlib.util.module_from_spec(spec)
spec.loader.exec_module(th)

TRACKER = Path(__file__).parent.parent / "audit-tracker.xlsx"

TODAY = "2026-04-22"

# Shared across all 8 rows
CASE = "case-sharing"
SEVERITY = 2
STATUS = "fixed"  # audited + fix applied + mobile verified; figma pairing pending
AUDIT_DATE = TODAY
VERIFY_DATE = TODAY

BASE_ROOT_CAUSE = (
    ".diagram { min-width: 400px } + body { padding: 40px } force horizontal "
    "overflow below 400px viewports — diagram card extends past viewport and "
    "overflow: hidden clips inner content (phone placeholders, cards, grids)."
)

# Per-screen metadata
SCREENS = [
    {
        "id": "shr01",
        "file": "working/diagrams/v4/SHR-01-before-share-sheet-v4.html",
        "desktop_node": "233:2",
        "recipe": "A",
        "recipe_name": "phone + annotations",
    },
    {
        "id": "shr02",
        "file": "working/diagrams/v4/SHR-02-after-branded-sharing-v4.html",
        "desktop_node": "237:2",
        "recipe": "A",
        "recipe_name": "phone + annotations",
    },
    {
        "id": "shr06",
        "file": "working/diagrams/v4/SHR-06-before-entry-points-v4.html",
        "desktop_node": "289:2",
        "recipe": "B",
        "recipe_name": "horizontal scroll carousel",
    },
    {
        "id": "shr07",
        "file": "working/diagrams/v4/SHR-07-contextual-share-controls-v4.html",
        "desktop_node": "295:2",
        "recipe": "B",
        "recipe_name": "horizontal scroll carousel",
    },
    {
        "id": "shr08",
        "file": "working/diagrams/v4/SHR-08-overflow-standardization-v4.html",
        "desktop_node": "299:2",
        "recipe": "C",
        "recipe_name": "stacked before/after",
    },
    {
        "id": "shr10",
        "file": "working/diagrams/v4/SHR-10-cross-platform-previews-v4.html",
        "desktop_node": "308:2",
        "recipe": "C",
        "recipe_name": "hub-and-spoke / stacked grids",
    },
    {
        "id": "shr11",
        "file": "working/diagrams/v4/SHR-11-preview-component-anatomy-v4.html",
        "desktop_node": "312:2",
        "recipe": "C",
        "recipe_name": "preview + callouts grid",
    },
    {
        "id": "shr12",
        "file": "working/diagrams/v4/SHR-12-text-post-preview-v4.html",
        "desktop_node": "316:2",
        "recipe": "C",
        "recipe_name": "stacked before/after",
    },
]

FIX_STRATEGY = (
    "Apply L2 Fix Recipe {r} ({rn}) from "
    "CoworkWorkspace/Skills/responsive-audit/references/l2-fix-recipes.md. "
    "Base fix: min-width: 400px → 0 on .diagram. Add @media (max-width: 600px) "
    "and @media (max-width: 360px) progressive padding + layout tiers."
)

COMMON_NOTES = (
    "L2 Recipe {r} applied; verified Playwright 240/320/375 → 0 horizontal "
    "overflow; quality-check clean, voice-check clean. Single responsive file "
    "handles desktop + mobile (no separate -v4-mobile.html needed). Figma "
    "mobile pairing deferred to Thread B (handoff-shr-ui-screens-to-figma.md)."
)


def build_row(screen):
    return {
        "diagram_id": screen["id"],
        "case_study": CASE,
        "file_path": screen["file"],
        "figma_node_id": screen["desktop_node"],
        # L2 means desktop widths reflow fine; narrow viewports broke
        "ok_1440": True,
        "ok_1024": True,
        "ok_768": True,
        "ok_480": True,
        "ok_375": True,   # fixed, verified
        "ok_320": True,   # fixed, verified
        "severity": SEVERITY,
        "root_cause": BASE_ROOT_CAUSE,
        "fix_strategy": FIX_STRATEGY.format(r=screen["recipe"], rn=screen["recipe_name"]),
        "mobile_file_path": screen["file"],  # same file — responsive v4 handles both
        "figma_mobile_node_id": None,  # Thread B will set
        "status": STATUS,
        "audit_date": AUDIT_DATE,
        "verify_date": VERIFY_DATE,
        "notes": COMMON_NOTES.format(r=screen["recipe"]),
    }


def main():
    if not TRACKER.exists():
        print(f"ERROR: tracker not found at {TRACKER}")
        sys.exit(1)

    th.validate_schema(TRACKER)

    existing_ids = {r.get("diagram_id") for r in th.read_tracker(TRACKER)}
    wrote = 0
    skipped = 0
    for s in SCREENS:
        if s["id"] in existing_ids:
            print(f"SKIP {s['id']} — row already exists")
            skipped += 1
            continue
        row = build_row(s)
        th.append_row(TRACKER, row)
        print(f"WROTE {s['id']} (Recipe {s['recipe']}, desktop node {s['desktop_node']})")
        wrote += 1

    print(f"\nDone: {wrote} rows written, {skipped} skipped.")
    print(f"Tracker: {TRACKER}")


if __name__ == "__main__":
    main()
