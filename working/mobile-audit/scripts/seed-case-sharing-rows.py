"""
Seed 8 case-sharing diagram rows into audit-tracker.xlsx.

Phase 1 of responsive-audit run. Status=audited, no Figma pairing yet
(deferred to separate thread).

Run from working/mobile-audit/ directory.
"""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "tracker_helpers", Path(__file__).parent / "tracker-helpers.py"
)
th = importlib.util.module_from_spec(spec)
spec.loader.exec_module(th)

TRACKER = "audit-tracker.xlsx"
TODAY = "2026-04-21"
DEFER_NOTE = "figma_pairing_deferred_to_other_thread"

ROWS = [
    {
        "diagram_id": "shr03",
        "case_study": "case-sharing",
        "file_path": "img/diagrams/diagram-shr03-research-overview-v4.html",
        "figma_node_id": "",
        "ok_1440": True, "ok_1024": True, "ok_768": True,
        "ok_480": True, "ok_375": True, "ok_320": True,
        "severity": 0,
        "root_cause": "",
        "fix_strategy": "",
        "mobile_file_path": "",
        "figma_mobile_node_id": "",
        "status": "audited",
        "audit_date": TODAY,
        "verify_date": "",
        "notes": DEFER_NOTE,
    },
    {
        "diagram_id": "shr04",
        "case_study": "case-sharing",
        "file_path": "img/diagrams/diagram-shr04-research-methodology-v4.html",
        "figma_node_id": "",
        "ok_1440": True, "ok_1024": True, "ok_768": True,
        "ok_480": True, "ok_375": False, "ok_320": False,
        "severity": 2,
        "root_cause": "min-width: 400px on .diagram causes left-edge clipping at <400px viewports; recipients track-2 cards may not be rendering — needs investigation",
        "fix_strategy": "Remove or reduce min-width at narrow viewports; verify recipients track-2 visibility post-fix",
        "mobile_file_path": "",
        "figma_mobile_node_id": "",
        "status": "audited",
        "audit_date": TODAY,
        "verify_date": "",
        "notes": DEFER_NOTE,
    },
    {
        "diagram_id": "shr05",
        "case_study": "case-sharing",
        "file_path": "img/diagrams/diagram-shr05-behavioral-model-v4.html",
        "figma_node_id": "",
        "ok_1440": True, "ok_1024": True, "ok_768": True,
        "ok_480": True, "ok_375": True, "ok_320": True,
        "severity": 0,
        "root_cause": "",
        "fix_strategy": "",
        "mobile_file_path": "",
        "figma_mobile_node_id": "",
        "status": "audited",
        "audit_date": TODAY,
        "verify_date": "",
        "notes": DEFER_NOTE,
    },
    {
        "diagram_id": "shr09",
        "case_study": "case-sharing",
        "file_path": "img/diagrams/diagram-shr09-screenshot-to-share-v4.html",
        "figma_node_id": "",
        "ok_1440": True, "ok_1024": True, "ok_768": True,
        "ok_480": True, "ok_375": True, "ok_320": True,
        "severity": 0,
        "root_cause": "",
        "fix_strategy": "",
        "mobile_file_path": "",
        "figma_mobile_node_id": "",
        "status": "audited",
        "audit_date": TODAY,
        "verify_date": "",
        "notes": DEFER_NOTE,
    },
    {
        "diagram_id": "shr13",
        "case_study": "case-sharing",
        "file_path": "img/diagrams/diagram-shr13-brand-expression-spectrum-v4.html",
        "figma_node_id": "",
        "ok_1440": True, "ok_1024": True, "ok_768": True,
        "ok_480": True, "ok_375": True, "ok_320": True,
        "severity": 0,
        "root_cause": "",
        "fix_strategy": "",
        "mobile_file_path": "",
        "figma_mobile_node_id": "",
        "status": "audited",
        "audit_date": TODAY,
        "verify_date": "",
        "notes": DEFER_NOTE,
    },
    {
        "diagram_id": "shr14",
        "case_study": "case-sharing",
        "file_path": "img/diagrams/diagram-shr14-privacy-barrier-v4.html",
        "figma_node_id": "",
        "ok_1440": True, "ok_1024": True, "ok_768": True,
        "ok_480": True, "ok_375": True, "ok_320": True,
        "severity": 0,
        "root_cause": "",
        "fix_strategy": "",
        "mobile_file_path": "",
        "figma_mobile_node_id": "",
        "status": "audited",
        "audit_date": TODAY,
        "verify_date": "",
        "notes": DEFER_NOTE,
    },
    {
        "diagram_id": "shre1",
        "case_study": "case-sharing",
        "file_path": "img/diagrams/diagram-shre1-feedback-engine-v4.html",
        "figma_node_id": "",
        "ok_1440": True, "ok_1024": True, "ok_768": True,
        "ok_480": True, "ok_375": True, "ok_320": True,
        "severity": 0,
        "root_cause": "",
        "fix_strategy": "",
        "mobile_file_path": "",
        "figma_mobile_node_id": "",
        "status": "audited",
        "audit_date": TODAY,
        "verify_date": "",
        "notes": DEFER_NOTE,
    },
    {
        "diagram_id": "shrfw",
        "case_study": "case-sharing",
        "file_path": "img/diagrams/diagram-shrfw-flywheel-v4.html",
        "figma_node_id": "",
        "ok_1440": True, "ok_1024": True, "ok_768": False,
        "ok_480": False, "ok_375": False, "ok_320": False,
        "severity": 3,
        "root_cause": "Fixed width:760px + absolute-positioned 196px cards in triangular flywheel composition cannot reflow to mobile widths without destroying loop semantic",
        "fix_strategy": "L3: new diagram-shrfw-flywheel-v4-mobile.html with vertical stacked composition; wrap in case-sharing.html with .diagram-pair (reuse existing styles.css swap rule)",
        "mobile_file_path": "",
        "figma_mobile_node_id": "",
        "status": "audited",
        "audit_date": TODAY,
        "verify_date": "",
        "notes": DEFER_NOTE,
    },
]


def main():
    for row in ROWS:
        th.upsert_row(TRACKER, row)
        print(f"  upserted {row['diagram_id']:8s} sev={row['severity']} status={row['status']}")
    final = th.read_tracker(TRACKER)
    sharing = [r for r in final if r.get("case_study") == "case-sharing"]
    print(f"\nTotal rows in tracker: {len(final)}")
    print(f"case-sharing rows: {len(sharing)}")


if __name__ == "__main__":
    main()
