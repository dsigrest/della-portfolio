# Handoff — SHR UI Screens → Figma Mobile Pairings (Thread B)

**Date:** 2026-04-22
**Source thread:** Thread A (SHR UI screens mobile HTML pass)
**Scope:** 8 SHR UI screens — shr01, shr02, shr06, shr07, shr08, shr10, shr11, shr12
**Goal:** Create native-layer Figma mobile frames at x=-1300 on page `29:41` (file `TArUrZsBUocaAsqetjXq7V`), one per screen, matching the HTML v4 responsive render at 375px width.

---

## What Thread A delivered

All 8 v4 files are responsive — a single HTML file handles desktop + mobile via recipe-based L2 CSS fixes (no separate `-v4-mobile.html` variants).

**Verification (Playwright, sandbox Chromium):**
- Zero horizontal overflow at viewports 240 / 320 / 375 on every file.
- `quality-check.py` — 0 errors, 0 warnings across all 8.
- `voice-check.py` — 0 errors (2 false-positive warnings from cross-element sentence concatenation — not real voice issues).
- Tracker: 8 rows written to `portfolio-site/working/mobile-audit/audit-tracker.xlsx` (case_study=`case-sharing`, status=`fixed`).

**The pattern library.** All 8 fixes came from `CoworkWorkspace/Skills/responsive-audit/references/l2-fix-recipes.md` — 3 recipes (A: phone + annotations, B: horizontal scroll carousel, C: stacked grids). Future case studies using the same archetypes (case-notifications, case-ai, case-subreddit) should drop these recipes in, not rebuild from scratch.

---

## The 8 screens — Thread B input table

| ID | Desktop node | Desktop y | HTML v4 (responsive) | Recipe | Mobile layout notes |
|---|---|---|---|---|---|
| shr01 | 233:2 | 120 | `working/diagrams/v4/SHR-01-before-share-sheet-v4.html` | A | Phone centered at top, 4 annotation cards stacked below, 3-stat bar → 1-col at mobile. |
| shr02 | 237:2 | 925 | `working/diagrams/v4/SHR-02-after-branded-sharing-v4.html` | A | Same structure as shr01 (branded sharing variant). |
| shr06 | 289:2 | 5457 | `working/diagrams/v4/SHR-06-before-entry-points-v4.html` | B | Horizontal scroll carousel of 4 cards. Do NOT stack vertically — preserve the swipe/scroll affordance. Each card 220px wide at mobile. |
| shr07 | 295:2 | 6412 | `working/diagrams/v4/SHR-07-contextual-share-controls-v4.html` | B | Same as shr06 (3-card scroll carousel + before/after comparison strip beneath). |
| shr08 | 299:2 | 7553 | `working/diagrams/v4/SHR-08-overflow-standardization-v4.html` | C | Before/after stacked vertically at mobile with rotated arrow connector between. |
| shr10 | 308:2 | 10272 | `working/diagrams/v4/SHR-10-cross-platform-previews-v4.html` | C | Hub-and-spoke. **Known limitation:** at ≤320px, spokes overlap the hub — Thread B should consider a stacked-grid alternative layout for the Figma mobile frame (hub on top, 6 platform icons as a 2×3 grid beneath). |
| shr11 | 312:2 | 11450 | `working/diagrams/v4/SHR-11-preview-component-anatomy-v4.html` | C | Preview component centered + 4 numbered signal callouts. Callouts-top grid collapses to 1fr at mobile; preview-component caps at 280px and glow backdrop sizes down. |
| shr12 | 316:2 | 12435 | `working/diagrams/v4/SHR-12-text-post-preview-v4.html` | C | Before/after text-post preview mockups stacked vertically with rotated arrow; 3-stat bar → 1-col at mobile. |

---

## Hard constraints (non-negotiable)

1. **Native layers only, no image fills.** Every mobile frame must be fully editable Figma primitives (`createFrame` / `createText` / `createRectangle` / `createEllipse` / `createVector` with SOLID paints and vector paths).
2. **Never `tidyPage()` on page 29:41.** The desktop cluster is hand-positioned. Only APPEND new mobile frames; never reposition existing.
3. **Position** each mobile frame at `x=-1300, y=<desktop.y>` (see table above for y-coords).
4. **Frame names** use the `shrXX-mobile` pattern (e.g. `shr01-mobile`, `shr02-mobile`).
5. **CSS-selector layer names** inside frames so the figma-to-html roundtrip works (e.g. `.phone-placeholder`, `.annotations`, `.card`).
6. **Two-phase MCP pattern**: mutate-and-commit (no throw) → separate query-and-throw. Throwing in the mutation call rolls back the writes.
7. **`layoutPositioning='ABSOLUTE'` must be set AFTER `appendChild`**, not before.
8. **Auto-layout VERTICAL** on the root mobile frame with `primaryAxisSizingMode='AUTO'`, `counterAxisSizingMode='FIXED'`, width=375.
9. **Per-screen quality gate**: ship shr01-mobile first, screenshot-verify it against the HTML v4 at 375, then proceed to the other 7. Session 10 precedent — 8 frames in one thread is feasible at ~80% context use.
10. **Atomic tracker writes** via `tracker-helpers.py` `update_row` — set `figma_mobile_node_id` after each successful pairing. Never pandas.

---

## Recipe-by-recipe translation notes

### Recipe A (shr01, shr02)

HTML structure at mobile (viewport ≤ 600px):
```
.diagram (card, 100% width, rounded 16px)
  .title-area (padding 32px 24px 0)
    .label (teal uppercase)
    h1 (24px)
    p.subtitle
  .content-area (VERTICAL, gap: 24px, padding: 28px 24px 32px)
    .phone-placeholder (centered, 190×340 max)
    .annotations (VERTICAL stack)
      .annotation-card × 4 (glass + numbered)
  .stat-bar (VERTICAL, gap 1px, margin: 0 24px 32px)
    .stat-item × 3 (1-col)
```

Figma translation:
- Root mobile frame = vertical auto-layout, width=375
- phone-placeholder = frame 190×340 with aspect-ratio visual (solid dark fill + dashed border via stroke + text "Custom share sheet")
- annotation-card = glass frame with number badge (ellipse) + title + body
- stat-item = rectangle with large stat + micro-label

### Recipe B (shr06, shr07)

HTML structure at mobile:
```
.diagram (card)
  .title-area (padding 32px 24px 0)
  .scroll-container
    .cards-row (HORIZONTAL flex, gap: 14px, overflow-x: auto)
      .card × N (flex: 0 0 220px)  ← KEEP HORIZONTAL, do not stack
```

Figma translation:
- Root mobile frame = vertical auto-layout, width=375
- cards-row = horizontal auto-layout frame (no vertical stack), fit width 375 with overflow clipping hidden — user scrolls in a real browser; in Figma static mobile frame, show the first card fully + second card peeking (that's the affordance). Fade gradient at right edge.
- Each card = frame with placeholder (UI surface dashed rectangle) + icon + title + body copy.

### Recipe C (shr08, shr10, shr11, shr12)

HTML structure at mobile — varies per screen:
- **shr08 / shr12** (before/after stack): vertical stack of 2 columns with rotated 90° arrow connector between.
- **shr10** (cross-platform hub-and-spoke): **suggested redesign** at mobile — instead of radial spokes (which overlap at narrow widths), stack: hub centered on top, then 2×3 grid of platform icons beneath.
- **shr11** (preview anatomy): callouts-top 1fr stack + centered preview-component (cap 280px) with hotspot dots + callouts-bottom stack.

Figma translation:
- Root mobile frame = vertical auto-layout, width=375
- Before/after columns become stacked frames with labels ("BEFORE" red dot, "AFTER" teal dot) and UI placeholder boxes
- Arrow connector = ellipse + rotated vector path between columns
- Stat bars: 1-col vertical stack of stat rectangles

---

## Known limitations flagged for Thread B follow-up

1. **shr10 hub-and-spoke at mobile.** The HTML uses absolute positioning on 4 spokes around a central hub. At ≤320px viewport, the spokes overlap the hub. The v4 HTML file shrinks the hub and nudges spoke positions but doesn't solve it fully — the spoke layout is genuinely broken below 360px. Thread B should either (a) translate this as a stacked grid in Figma (hub + 2×3 platforms beneath, 6 icons total instead of 4), or (b) preserve the radial layout with the understanding that it only reads cleanly at ≥360px and flag as a separate redesign task.
2. **shr11 hotspot positioning.** Hotspots 1/2/3 are absolute-positioned over the preview component. In Figma, translate these as small ellipse frames with accent fill + outer shadow ring, positioned ABSOLUTE (post-appendChild) at the same visual locations as the HTML.

---

## Close-out checklist (Thread B)

- [ ] shr01-mobile frame created, screenshot-verified against v4 HTML at 375, quality gate ✅
- [ ] 7 remaining mobile frames created (shr02, shr06, shr07, shr08, shr10, shr11, shr12)
- [ ] Tracker updated: each row has `figma_mobile_node_id` populated
- [ ] This doc updated with executed-node-IDs table (append below)
- [ ] BUILD-LOG.md session entry appended
- [ ] SESSION-STATE.md marks SHR UI screens pairing ✅ COMPLETE

---

## Executed node IDs (Thread B fills in)

_Thread B: update this table as each mobile frame ships._

| ID | figma_mobile_node_id | Shipped | Verified against HTML | Notes |
|---|---|---|---|---|
| shr01 | TBD | — | — | — |
| shr02 | TBD | — | — | — |
| shr06 | TBD | — | — | — |
| shr07 | TBD | — | — | — |
| shr08 | TBD | — | — | — |
| shr10 | TBD | — | — | — |
| shr11 | TBD | — | — | — |
| shr12 | TBD | — | — | — |

---

## References

- `CoworkWorkspace/Skills/responsive-audit/references/l2-fix-recipes.md` — the recipe library used in Thread A
- `portfolio-site/working/mobile-audit/handoff-shr-ui-screens.md` — the original brief that spawned both threads
- `portfolio-site/working/mobile-audit/figma-handoff-case-sharing.md` — session 10 precedent for native-layer Figma pairings (same pattern)
- `portfolio-site/working/mobile-audit/audit-tracker.xlsx` — source of truth for row state
- `portfolio-site/working/mobile-audit/scripts/tracker-helpers.py` — openpyxl atomic writes

---

## Thread C — ✅ COMPLETE (Session 14, 2026-04-22)

**Deploy + viewer-register the 8 SHR UI screens.** Delivered independent of Thread B, which remains pending.

- 8 v4 files deployed to `portfolio-site/img/diagrams/diagram-shrXX-<slug>-v4.html` with embed-mode CSS + iframe-detection script (`body.embedded` pattern, matches shr03–shr05).
- 8 entries registered in `working/diagram-viewer.html` under `case-sharing` array, ordered shr01/02 before shr03 → shr06/07/08 between shr05 and shr09 → shr10/11/12 between shr09 and shr13.
- 8 `img-placeholder` divs in `case-sharing.html` swapped to `diagram-embed` iframe wrappers with accessible `title` attrs. Auto-resize iframe script already present (untouched).
- Tracker (`audit-tracker.xlsx`): all 8 rows now have `mobile_file_path=img/diagrams/diagram-shrXX-<slug>-v4.html`. Atomic writes via `tracker-helpers.py` `update_row` (loaded with `importlib.util.spec_from_file_location` because of the hyphen in the filename).
- `quality-check.py` + `voice-check.py` — 0 errors across all 9 touched files.
- Final 375px visual smoke-test via viewer URL deferred to Della (no Playwright in sandbox this session).

**Three `img-placeholder` divs remain in `case-sharing.html`** — intentionally out of Thread C scope: custom share sheet v1, v2, and the publisher embed tool. Those are net-new artifacts, not Thread A deliveries.

---
