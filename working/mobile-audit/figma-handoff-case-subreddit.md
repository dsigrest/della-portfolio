# Figma Pairing Handoff — case-subreddit

**Date:** 2026-04-22
**Source thread:** case-subreddit responsive-audit (audit + CSS-fix phases complete through Round 2)
**Destination thread:** fresh Figma-pairing thread running html-to-figma against the 10 diagrams listed below

This handoff is **the only thing** the Figma thread needs to read to do its job. Don't re-run the audit, don't touch HTML/CSS, don't second-guess severity calls — they're locked and screenshot-verified.

---

## Status roster

10 diagrams audited — all L2, all CSS-only fixes inside each diagram's own `<style>` block. No L0 / L1 / L3. No new mobile HTML files. Every diagram renders the **same desktop file at 375 width** into its mobile Figma frame.

| Diagram | Round | Status | Mobile HTML to render | R1 fix | R2 fix |
|---|---|---|---|---|---|
| sub01 — survival curve | R1 + R2 | verified 2026-04-22 | `diagram-sub01-survival-curve.html` @ 375 | Pattern B — `aspect-ratio: 660/200` chart-area swap @768; SVG text 14→16 @480 | Chart hierarchy — shrunk stat-big 32→22 @480, 20 @320; tightened curve-card padding; SVG text 16→19 @320 |
| sub02 — lifecycle framework | R1 only | verified 2026-04-22 | `diagram-sub02-lifecycle-framework.html` @ 375 | Pattern C — 5-col grid → 1fr @768 | — |
| sub03 — milestone model | R1 only | verified 2026-04-22 | `diagram-sub03-milestone-model.html` @ 375 | Pattern D — `.stage-card` flex-column @480 | — |
| sub04 — strategic starting points | R1 only | verified 2026-04-22 | `diagram-sub04-strategic-starting-points.html` @ 375 | Pattern C — `.bets-container` column @768 + badge wrap | — (this is the **reference** for canonical SVG icon style) |
| sub05 — artifact alignment | R1 + R2 | verified 2026-04-22 | `diagram-sub05-artifact-alignment.html` @ 375 | Pattern C — `.cards-grid` 2×2 → 1fr @768 | Replaced 4 emojis (📊⚖🎯🎨) with inline SVGs in sub04 style |
| sub06 — threshold calibration | R1 + R2 | verified 2026-04-22 | `diagram-sub06-threshold-calibration.html` @ 375 | Pattern B — `aspect-ratio: 640/280` + 5→3→2-up detail collapse | Replaced 5 emojis (🎨✍📈👥✨) with SVG icons; shrunk detail cards; hid hint text @480; SVG text bump @480/320 |
| sub08 — creation after | R1 only | verified 2026-04-22 | `diagram-sub08-creation-after.html` @ 375 | Vertical stack `.flow-steps` + rotated ↓ arrows @480 | — |
| sub09 — distribution loop | R1 + R2 | verified 2026-04-22 | `diagram-sub09-distribution-loop.html` @ 375 | Pattern C — `.flow-row` column @768 + rotate inline arrows; hide return-arc SVG | Replaced 4 emojis (📢❤🛡⛔) with SVG icons; deadlock badge explicit `stroke="var(--red)"` |
| sub11 — text bars (three pillars) | R1 only | verified 2026-04-22 | `diagram-sub11-text-bars.html` @ 375 | Pattern C — `.pillars-grid` 3-col → 1fr @768 | — |
| sub12 — instrumentation heatmap | R1 only | verified 2026-04-22 | `diagram-sub12-instrumentation-interactive.html` @ 375 | `flex:1 .heatmap-col-header` @768; tighter cells @480/320 | — |

**Tracker state in `portfolio-site/working/mobile-audit/audit-tracker.xlsx`:**
- 10 case-subreddit rows, all `status=verified`, `verify_date=2026-04-22`, `figma_mobile_node_id=""` (that's what the Figma thread fills in)
- All 10 rows have updated `notes` documenting R1 + R2 fixes and the screenshot-verified confirmation

---

## Canonical SVG icon style (sub04 reference)

All R2 icons were built to match sub04's existing inline-SVG style. If the Figma thread needs to re-render or touch any icon, use this exact pattern:

```html
<svg width="16" height="16" viewBox="0 0 24 24" fill="none"
     stroke="currentColor" stroke-width="1.5"
     stroke-linecap="round" stroke-linejoin="round">
  <!-- shape paths -->
</svg>
```

- **Stroke width:** 1.5
- **Color:** `currentColor` — inherits from parent `.card-icon` / `.detail-icon` which sets the token color
- **Sizing:** 16×16 inside 32×32 card-icon containers; 12×12 inside 24×24 detail-icon containers
- **Exception:** sub09's deadlock badge uses explicit `stroke="var(--red)"` because `.deadlock-badge`'s parent doesn't set `color`

No emojis remain in any of the 10 subreddit diagrams (verified via Unicode grep across the diagrams folder — zero matches).

---

## Target

| Field | Value |
|---|---|
| Figma file key | `TArUrZsBUocaAsqetjXq7V` (Portfolio — Image Inventory) |
| Page name | "4. Subreddit Success" |
| Page ID | `29:40` |
| Mobile cluster anchor x | **`-1634`** (pre-computed via v0.2.1 algorithm — `leftmost.x − 1300` on page 29:40; confirmed during Session 4) |
| Mobile frame width | 375 |
| Mobile frame height | natural-height-at-375 (let the rendered HTML define it) |
| Frame naming | `sub01-mobile`, `sub02-mobile`, `sub03-mobile`, `sub04-mobile`, `sub05-mobile`, `sub06-mobile`, `sub08-mobile`, `sub09-mobile`, `sub11-mobile`, `sub12-mobile` |

**Don't run the default `tidyPage()` on this page.** Desktop frames Della has hand-positioned must not move. Place mobile frames at `x = -1634`; leave everything else alone.

---

## Per-diagram pairing spec

Resolve `desktop_y` at handoff-execute time by listing children of page `29:40` and matching by frame name prefix. Frame names in this Figma file follow the `SUB-XX` convention (uppercase prefix, double-digit ID).

Uniform template — every row uses the same structure, only the IDs and paths differ:

| Field | Value |
|---|---|
| Render width | 375 |
| Frame x | `-1634` (mobile_cluster_x) |
| Frame y | `desktop_base.y` (same row as desktop) |
| Tracker write-back | `figma_mobile_node_id = <new node id>` |

| Diagram | HTML to render | Mobile frame name | Desktop base frame name prefix |
|---|---|---|---|
| sub01 | `portfolio-site/img/diagrams/diagram-sub01-survival-curve.html` | `sub01-mobile` | `SUB-01` |
| sub02 | `portfolio-site/img/diagrams/diagram-sub02-lifecycle-framework.html` | `sub02-mobile` | `SUB-02` |
| sub03 | `portfolio-site/img/diagrams/diagram-sub03-milestone-model.html` | `sub03-mobile` | `SUB-03` |
| sub04 | `portfolio-site/img/diagrams/diagram-sub04-strategic-starting-points.html` | `sub04-mobile` | `SUB-04` |
| sub05 | `portfolio-site/img/diagrams/diagram-sub05-artifact-alignment.html` | `sub05-mobile` | `SUB-05` |
| sub06 | `portfolio-site/img/diagrams/diagram-sub06-threshold-calibration.html` | `sub06-mobile` | `SUB-06` |
| sub08 | `portfolio-site/img/diagrams/diagram-sub08-creation-after.html` | `sub08-mobile` | `SUB-08` |
| sub09 | `portfolio-site/img/diagrams/diagram-sub09-distribution-loop.html` | `sub09-mobile` | `SUB-09` |
| sub11 | `portfolio-site/img/diagrams/diagram-sub11-text-bars.html` | `sub11-mobile` | `SUB-11` |
| sub12 | `portfolio-site/img/diagrams/diagram-sub12-instrumentation-interactive.html` | `sub12-mobile` | `SUB-12` |

---

## Scripts

Use the html-to-figma skill (it owns the render-and-place logic in v0.3.0 of responsive-audit). Pass it this payload:

```json
{
  "case_study_slug": "case-subreddit",
  "figma_file_key": "TArUrZsBUocaAsqetjXq7V",
  "target_figma_page": "29:40",
  "mobile_cluster_x": -1634,
  "diagrams": [
    { "diagram_id": "sub01", "html_path": "portfolio-site/img/diagrams/diagram-sub01-survival-curve.html",             "mobile_frame_name": "sub01-mobile", "desktop_frame_name_prefix": "SUB-01" },
    { "diagram_id": "sub02", "html_path": "portfolio-site/img/diagrams/diagram-sub02-lifecycle-framework.html",        "mobile_frame_name": "sub02-mobile", "desktop_frame_name_prefix": "SUB-02" },
    { "diagram_id": "sub03", "html_path": "portfolio-site/img/diagrams/diagram-sub03-milestone-model.html",            "mobile_frame_name": "sub03-mobile", "desktop_frame_name_prefix": "SUB-03" },
    { "diagram_id": "sub04", "html_path": "portfolio-site/img/diagrams/diagram-sub04-strategic-starting-points.html",  "mobile_frame_name": "sub04-mobile", "desktop_frame_name_prefix": "SUB-04" },
    { "diagram_id": "sub05", "html_path": "portfolio-site/img/diagrams/diagram-sub05-artifact-alignment.html",         "mobile_frame_name": "sub05-mobile", "desktop_frame_name_prefix": "SUB-05" },
    { "diagram_id": "sub06", "html_path": "portfolio-site/img/diagrams/diagram-sub06-threshold-calibration.html",      "mobile_frame_name": "sub06-mobile", "desktop_frame_name_prefix": "SUB-06" },
    { "diagram_id": "sub08", "html_path": "portfolio-site/img/diagrams/diagram-sub08-creation-after.html",             "mobile_frame_name": "sub08-mobile", "desktop_frame_name_prefix": "SUB-08" },
    { "diagram_id": "sub09", "html_path": "portfolio-site/img/diagrams/diagram-sub09-distribution-loop.html",          "mobile_frame_name": "sub09-mobile", "desktop_frame_name_prefix": "SUB-09" },
    { "diagram_id": "sub11", "html_path": "portfolio-site/img/diagrams/diagram-sub11-text-bars.html",                  "mobile_frame_name": "sub11-mobile", "desktop_frame_name_prefix": "SUB-11" },
    { "diagram_id": "sub12", "html_path": "portfolio-site/img/diagrams/diagram-sub12-instrumentation-interactive.html", "mobile_frame_name": "sub12-mobile", "desktop_frame_name_prefix": "SUB-12" }
  ]
}
```

Fallback (if html-to-figma isn't available) — same byte-array transport pattern used in case-ai/case-notifications:
- `portfolio-site/working/mobile-audit/scripts/render-mobile-to-figma.py` — primary
- `populate-figma-frames-prep.py` + `populate-figma-frames.js` — manual two-step fallback
- **Do not use base64 `atob`** — validated broken in Figma plugin runtime (v0.2.2 patch pending). Use raw `Uint8Array` of JPEG bytes inline.

---

## Non-negotiables for the Figma thread

1. **Read `figma-pairing-convention.md v0.2.1`** before doing anything. The cluster anchor algorithm and naming convention are non-obvious.
2. **Tracker writes via `tracker-helpers.py` openpyxl atomic** (`update_row`). Never pandas. The Figma thread's only tracker write per diagram is `figma_mobile_node_id`.
3. **Never `tidyPage()` this page.** Della's desktop cluster is hand-positioned and must not move. Add mobile frames at `x = -1634`; leave everything else alone.
4. **Never edit the desktop cluster.** Don't reposition, rename, restyle, or reparent any `SUB-XX` frame.
5. **Byte-array transport only.** `atob` fails inside `use_figma`. Use raw `Uint8Array` of JPEG bytes inline (same pattern that shipped case-ai's 4 pairings and case-notifications' 11).
6. **One pass per diagram, then verify.** After each pairing call, re-fetch the page, confirm the mobile frame exists at the expected (x, y), confirm the IMAGE fill rendered. If the fill is empty or stretched wrong, re-render and replace; don't ship a broken fill.
7. **No HTML/CSS edits.** The 10 files are locked and screenshot-verified. If a render looks wrong, the fix is to re-render — not to tweak the source.

---

## Close-the-loop

After the Figma thread completes all 10 pairings:

1. Tracker: all 10 rows have `figma_mobile_node_id` populated; status stays `verified`.
2. Update `SESSION-STATE.md`: flip case-subreddit block from "COMPLETE — Figma pairing deferred" to "COMPLETE" with the 10 new mobile node IDs.
3. Append to `BUILD-LOG.md`: two-line entry summarizing the Figma pairing batch and the 10 node IDs created.

---

## What this thread did NOT do (so the Figma thread doesn't redo it)

- ✅ Audit (10 L2, 0 L0/L1/L3) — locked, in tracker
- ✅ Round 1 CSS fixes (all 10 diagrams) — CSS inside each diagram's `<style>` block, no structural changes
- ✅ Round 2 refinements (sub01, 05, 06, 09) — chart hierarchy rebalance + inline SVG icon replacements for all emojis
- ✅ Screenshot safety-net pass on Della's Mac — all 10 × 6 breakpoints captured and visually confirmed
- ✅ Viewer updated with Round 2 amber badges (`audit-viewer-case-subreddit.html`)
- ✅ Tracker rows all moved to `status=verified`

- ❌ Figma frame creation (this handoff doc — that's the next thread's job)
- ❌ Tracker `figma_mobile_node_id` writes (Figma thread's job)
- ❌ Any HTML or CSS edit (locked, don't touch)

---

## Version

- 2026-04-22 — initial. Source: case-subreddit responsive-audit, Rounds 1 + 2 complete.
- 2026-04-22 — **COMPLETE**. All 10 mobile Figma frames built via `use_figma` native-layer translation (no image fills; CSS-selector layer names for deterministic roundtrip). All tracker rows populated with `figma_mobile_node_id`. Page 29:40 was NOT tidied — Della's desktop cluster preserved exactly as-is.

### Final node IDs (all 10 paired)

| Diagram | Mobile node ID | desktop_y (from page 29:40) |
|---|---|---|
| sub01 — survival curve | `943:26` | (same row as SUB-01 desktop) |
| sub02 — lifecycle framework | `915:26` | (same row as SUB-02 desktop) |
| sub03 — milestone model | `922:26` | (same row as SUB-03 desktop) |
| sub04 — strategic starting points | `887:26` | (same row as SUB-04 desktop) |
| sub05 — artifact alignment | `925:26` | (same row as SUB-05 desktop) |
| sub06 — threshold calibration | `936:26` | (same row as SUB-06 desktop) |
| sub08 — creation after | `946:26` | (same row as SUB-08 desktop) |
| sub09 — distribution loop | `948:26` | (same row as SUB-09 desktop) |
| sub11 — text bars (three pillars) | `951:26` | (same row as SUB-11 desktop) |
| sub12 — instrumentation heatmap | `954:26` | (same row as SUB-12 desktop) |

All frames at `x = -1634` (mobile cluster anchor), width 375, native-rendered (no image fills). Screenshot-verified via `get_screenshot` on each node ID.

**What got built (technique notes for future reference):**
- All frames use auto-layout with `layoutMode = "VERTICAL"` and absolute-positioned children only where required (e.g., SVG overlays, badges)
- Cubic bezier curves manually pre-computed with midpoint control points for SUB-01's survival curve and SUB-06's threshold calibration (original HTML used JS generation)
- Font loading order mandatory: Inter (Regular/Medium/Semi Bold/Bold) + JetBrains Mono (Regular/Bold) — note space in "Semi Bold"
- Layer names match CSS selectors exactly (`.heatmap-cell.stall`, `.pillar-card.accent`, etc.) for deterministic figma-to-html roundtrip
- `primaryAxisSizingMode = "FIXED"` + `resizeWithoutConstraints(w, h)` before appending + `layoutAlign = "STRETCH"` is the stable sizing pattern
- Text pattern: `textAutoResize = "HEIGHT"` + `resize(w, currentHeight)` + `layoutAlign = "STRETCH"`
- Append child BEFORE setting x/y — auto-layout override otherwise stomps position
