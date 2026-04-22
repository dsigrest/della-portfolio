"""
Flip all 8 case-sharing rows to status=verified, verify_date=2026-04-21.

Runs after Della's safety-net screenshot pass confirms no regressions.
Called once per case study; atomic openpyxl writes via tracker-helpers.
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

DIAGRAMS = [
    "shr03", "shr04", "shr05", "shr09",
    "shr13", "shr14", "shre1", "shrfw",
]


def main():
    rows = th.read_tracker(TRACKER)
    before = {r["diagram_id"]: (r.get("status"), r.get("verify_date"))
              for r in rows if r.get("diagram_id") in DIAGRAMS}

    for did in DIAGRAMS:
        th.update_row(TRACKER, did, {
            "status": "verified",
            "verify_date": TODAY,
        })
        print(f"  {did:8s} → status=verified verify_date={TODAY}")

    after = {r["diagram_id"]: (r.get("status"), r.get("verify_date"))
             for r in th.read_tracker(TRACKER) if r.get("diagram_id") in DIAGRAMS}

    print("\nBefore → After:")
    for did in DIAGRAMS:
        b = before.get(did, ("?", "?"))
        a = after.get(did, ("?", "?"))
        print(f"  {did:8s}  {b[0]:10s} ({b[1] or '-':10s})  →  {a[0]:10s} ({a[1] or '-':10s})")


if __name__ == "__main__":
    main()
