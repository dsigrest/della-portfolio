#!/usr/bin/env python3
"""
Audit script for responsive diagram analysis.
This guides the visual inspection process.
"""

import sys
from pathlib import Path

# Diagram list with file paths
DIAGRAMS = {
    "not01": {
        "name": "not01-segmentation-matrix-v5",
        "case_study": "case-notifications",
        "file_path": "img/diagrams/diagram-not01-segmentation-matrix-v5.html",
        "type": "matrix"
    },
    "not04": {
        "name": "not04-unread-hierarchy-v5",
        "case_study": "case-notifications",
        "file_path": "img/diagrams/diagram-not04-unread-hierarchy-v5.html",
        "type": "hierarchy"
    },
    "not06": {
        "name": "not06-push-to-inbox-v5",
        "case_study": "case-notifications",
        "file_path": "img/diagrams/diagram-not06-push-to-inbox-v5.html",
        "type": "flow"
    },
    "not07": {
        "name": "not07-preference-architecture-v5",
        "case_study": "case-notifications",
        "file_path": "img/diagrams/diagram-not07-preference-architecture-v5.html",
        "type": "architecture"
    },
    "not09": {
        "name": "not09-global-settings-v5",
        "case_study": "case-notifications",
        "file_path": "img/diagrams/diagram-not09-global-settings-v5.html",
        "type": "ui"
    },
    "not11": {
        "name": "not11-cross-channel-v5",
        "case_study": "case-notifications",
        "file_path": "img/diagrams/diagram-not11-cross-channel-v5.html",
        "type": "matrix"
    },
    "not-e1": {
        "name": "not-e1-cohort-decay-v5",
        "case_study": "orphan-not-e",
        "file_path": "img/diagrams/diagram-not-e1-cohort-decay-v5.html",
        "type": "chart"
    },
    "not-e2": {
        "name": "not-e2-strategy-flywheel-v5",
        "case_study": "orphan-not-e",
        "file_path": "img/diagrams/diagram-not-e2-strategy-flywheel-v5.html",
        "type": "flywheel"
    },
    "not-e3": {
        "name": "not-e3-strategic-pillars-v5",
        "case_study": "orphan-not-e",
        "file_path": "img/diagrams/diagram-not-e3-strategic-pillars-v5.html",
        "type": "pillars"
    },
    "not-e4": {
        "name": "not-e4-signal-intent-matrix-v5",
        "case_study": "orphan-not-e",
        "file_path": "img/diagrams/diagram-not-e4-signal-intent-matrix-v5.html",
        "type": "matrix"
    },
    "not-e5": {
        "name": "not-e5-notification-taxonomy-v5",
        "case_study": "orphan-not-e",
        "file_path": "img/diagrams/diagram-not-e5-notification-taxonomy-v5.html",
        "type": "tree"
    },
    "not-e6": {
        "name": "not-e6-butterfly-chart-v5",
        "case_study": "orphan-not-e",
        "file_path": "img/diagrams/diagram-not-e6-butterfly-chart-v5.html",
        "type": "butterfly"
    },
    "not-e7": {
        "name": "not-e7-sankey-flow-v5",
        "case_study": "orphan-not-e",
        "file_path": "img/diagrams/diagram-not-e7-sankey-flow-v5.html",
        "type": "sankey"
    },
}

BREAKPOINTS = [1440, 1024, 768, 480, 375, 320]

def print_audit_guide():
    """Print guidance for manual visual audit."""
    print("""
=== RESPONSIVE AUDIT GUIDE ===

For each diagram, look at screenshots in this order:
  1. 1440px (desktop full)
  2. 1024px (tablet landscape)  
  3. 768px (tablet portrait)
  4. 480px (mobile landscape)
  5. 375px (mobile portrait)
  6. 320px (mobile portrait - tight)

Ask these questions:
  - Is content visible and legible?
  - Are all visual elements showing?
  - Is there unwanted horizontal scroll?
  - Is content clipped or cut off?
  - Do grid/layout elements collapse properly below 768px?
  - Do text labels scale appropriately?
  - Is the diagram's design intent preserved?

Classification rules (from severity-classification.md):
  
  L0: Everything renders correctly at all 6 breakpoints
  L1: Fix lives in styles.css OR case-*.html (outer layer)
       - Example: iframe is oversized or has wrong aspect ratio
       - Example: outer container needs max-width or padding
  L2: Fix lives inside diagram HTML file (inner layer)
       - Example: grid inside diagram doesn't reflow below 768
       - Example: SVG text too small at mobile sizes
  L3: Requires new {name}-mobile.html file (structural redesign)
       - Example: butterfly chart can't work on narrow widths
       - Example: diagram loses meaning if key dimension changes
""")

if __name__ == "__main__":
    print_audit_guide()
    print("\nDiagrams to audit:")
    for key, info in DIAGRAMS.items():
        print(f"  {key}: {info['name']} ({info['type']})")
