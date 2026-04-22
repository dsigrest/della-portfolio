# Handoff — SHR UI Screens Mobile Work (SHR-01/02/06/07/08/10/11/12)

**Date:** 2026-04-22
**Source thread:** case-sharing Figma pairing close-out
**Scope:** 8 SHR UI screens that exist as Figma desktop frames + v3 HTML, but are NOT in the live case-sharing.html yet and have no mobile pairs
**Goal:** Create mobile HTML variants (where needed) and native-layer Figma mobile frames at x=-1300 on page 29:41

---

## Why this exists

During the case-sharing Figma pairing (session 10), all 8 **diagrams** embedded in `case-sharing.html` got native-layer mobile Figma frames:

| Paired | Node |
|---|---|
| shr03, shr04, shr05, shr09, shr13, shr14, shre1, shrfw | 851:8, 873:8, 881:8, 899:8, 833:8, 903:8, 906:8, 911:8 |

But page `29:41` in `TArUrZsBUocaAsqetjXq7V` also contains desktop frames for 8 **UI screen mockups** (SHR-01/02/06/07/08/10/11/12) that weren't paired. They weren't in the mobile-audit scope because they don't appear in the live case study yet. Della has confirmed she wants mobile Figma pairs for these too — they're destined for the case study, just not embedded yet.

---

## The 8 screens

All source HTML lives in `Get-a-job/working/diagrams/v3/`. All desktop Figma frames live on page `29:41` (file `TArUrZsBUocaAsqetjXq7V`, "3. Sharing & embeds").

| ID | Desktop frame name (Figma) | HTML source (v3) | Desktop y | Desktop frame node |
|---|---|---|---|---|
| shr01 | SHR-01 — Before: Default Share Sheet | `working/diagrams/v3/SHR-01-before-share-sheet-v3.html` | 120 | 233:2 |
| shr02 | SHR-02 — After: Branded Sharing | `working/diagrams/v3/SHR-02-after-branded-sharing-v3.html` | 925 | 237:2 |
| shr06 | SHR-06 — Fragmented Entry Points | `working/diagrams/v3/SHR-06-before-entry-points-v3.html` | 5457 | 289:2 |
| shr07 | SHR-07 — Contextual Share Controls | `working/diagrams/v3/SHR-07-contextual-share-controls-v3.html` | 6412 | 295:2 |
| shr08 | SHR-08 — Overflow Standardization | `working/diagrams/v3/SHR-08-overflow-standardization-v3.html` | 7553 | 299:2 |
| shr10 | SHR-10 — Cross-Platform Previews | `working/diagrams/v3/SHR-10-cross-platform-previews-v3.html` | 10272 | 308:2 |
| shr11 | SHR-11 — Preview Component Anatomy | `working/diagrams/v3/SHR-11-preview-component-anatomy-v3.html` | 11450 | 312:2 |
| shr12 | SHR-12 — Text Post Previews | `working/diagrams/v3/SHR-12-text-post-preview-v3.html` | 12435 | 316:2 |

**Why these are harder than the first batch:** they're UI mockups, not diagrams. Each has a phone-chrome frame + side-panel annotations in a `220px 1fr` grid (or similar). At 375px width, the grid collapses — there's no natural reflow. Most will need mobile-specific redesigns where the phone floats at top/center and annotations stack beneath as cards.

---

## Recommended thread structure

**Thread A (HTML) — "SHR UI screens — mobile HTML audit + variants"**
Use the `responsive-audit` skill to capture each screen at 375, classify L0/L2/L3, and author `diagram-shrXX-*-v4-mobile.html` where redesign is needed. Promote v3 → v4 in `portfolio-site/img/diagrams/` if needed (decide whether these become live in `case-sharing.html` or stay off-site for now — discuss with Della).

**Thread B (Figma) — "SHR UI screens — native-layer Figma pairings"**
Once Thread A's mobile HTML is stable, use `html-to-figma` to create `shrXX-mobile` frames on page `29:41` at x=-1300 and y=matching-desktop. Follow the exact pattern from session 10: native layers only (no image fills), CSS-selector layer names, two-phase mutate-then-query, ABSOLUTE after appendChild, atomic tracker writes via `tracker-helpers.py`.

**If Della wants 1 thread:** doable for 4 screens at a time (split 8 into two 4-screen batches). 8 in one thread risks context pressure — session 10 did 8 simple diagrams at ~80% context use; these are more complex.

---

## Thread A — detailed brief

### Inputs
- 8 HTML files listed above (v3 versions in `working/diagrams/v3/`)
- Responsive-audit skill (`.claude/skills/responsive-audit/`)
- Desktop Figma frames for visual reference (file `TArUrZsBUocaAsqetjXq7V`, page `29:41`)

### Process per screen
1. **Screenshot at 375** (responsive-audit capture phase) — confirm how v3 actually breaks at mobile width.
2. **Classify**:
   - **L0** — reflows naturally: rename to v4, ship as-is.
   - **L2** — CSS-only fix: remove `min-width`, switch grid to flex column, etc. Author v4 with the fix.
   - **L3** — needs mobile redesign: keep v4 for desktop, author `diagram-shrXX-*-v4-mobile.html` with a mobile-first composition.
3. **Screenshot-verify** the fixed/new file at 375 — confirm it renders cleanly, no overflow, readable.
4. **Run `quality-check.py`** on every new file (zero errors, zero warnings).
5. **Record in tracker** (`portfolio-site/working/mobile-audit/audit-tracker.xlsx`) via `tracker-helpers.py` openpyxl atomic writes. Add 8 new rows (case_study="case-sharing-ui-screens" or a new scope label — discuss with Della; don't pollute the existing case-sharing rows).

### Open questions for Della (resolve early in Thread A)
1. Should these 8 screens get promoted to `portfolio-site/img/diagrams/` as v4, or stay in `working/diagrams/` for now?
2. Will they eventually be iframe-embedded in `case-sharing.html`? Or inserted as flat PNG exports?
3. Tracker: new scope label or reuse "case-sharing"? Recommend new label to keep the existing 8 rows clean.

### Close-out (Thread A)
- Tracker: 8 new rows with `status=audited|fixed|verified` as appropriate.
- New file: `working/mobile-audit/handoff-shr-ui-screens-to-figma.md` — the Thread B payload, analogous to `figma-handoff-case-sharing.md v2`.
- Append session entry to `BUILD-LOG.md`.
- Update `SESSION-STATE.md`.

---

## Thread B — detailed brief

### Prereqs (from Thread A)
- All 8 screens have stable HTML at 375 width (either in v3 folder, promoted v4, or new v4-mobile).
- Tracker rows exist for the 8 screens.
- `handoff-shr-ui-screens-to-figma.md` exists with HTML paths finalized.

### Process per screen (same as session 10)
1. **Read the mobile HTML** at the path from Thread A's handoff doc.
2. **Translate to native Figma** via `mcp__*__use_figma`:
   - Frame: `shr{ID}-mobile`, 375 wide, height natural.
   - Auto-layout VERTICAL with `primaryAxisSizingMode='AUTO'`, `counterAxisSizingMode='FIXED'`.
   - Nested frames for sections (phone-chrome, annotations-stack, etc.).
   - CSS-selector layer names for figma-to-html roundtrip.
   - NO image fills. Everything as `createFrame` / `createText` / `createRectangle` / `createEllipse` / `createVector` with SOLID paints and vector paths.
3. **Position** at `x=-1300, y=<desktop.y>` (desktop y from table above).
4. **Quality gate on screen #1 only** — show Della a screenshot before proceeding to the other 7.
5. **Atomic tracker write**: `figma_mobile_node_id` via `tracker-helpers.py update_row`.

### Hard constraints (from Della, non-negotiable)
- **Native layers only, no image fills.** Every frame must be fully editable Figma primitives.
- **Never `tidyPage()` this page.** Desktop cluster is hand-positioned.
- **CSS-selector layer names** so figma-to-html roundtrip works.
- **Two-phase MCP pattern**: mutate-and-commit (no throw) → separate query-and-throw. Throwing in the mutation call rolls back writes.
- **`layoutPositioning='ABSOLUTE'` must be set AFTER `appendChild`**, not before.
- **Per-screen quality gate**: one screen shipped + screenshot-verified before doing the next 7.

### Close-out (Thread B)
- Tracker: 8 rows have `figma_mobile_node_id` populated.
- Update `handoff-shr-ui-screens-to-figma.md` with executed node IDs table.
- Append session entry to `BUILD-LOG.md`.
- Update `SESSION-STATE.md` marking the UI-screens pairing ✅ COMPLETE.

---

## Non-negotiables (both threads)

1. **Read `CoworkWorkspace/CLAUDE.md` + `Get-a-job/CLAUDE.md` first.** Voice rules, verify-before-claiming, tidy-page rules.
2. **Read `PATH-MAPPINGS.md`.** All Mac paths when showing Della terminal commands.
3. **Verify before claiming.** Screenshot every render. Check tracker writes by re-reading. Don't claim "8 screens done" without seeing all 8.
4. **Tracker writes are atomic openpyxl via `tracker-helpers.py`.** Never pandas. Never raw workbook saves.
5. **Ask Della before expanding scope.** If v4 promotion is uncertain, ask. If tracker schema needs new columns, ask.

---

## Source-of-truth files

- This brief: `portfolio-site/working/mobile-audit/handoff-shr-ui-screens.md`
- Tracker: `portfolio-site/working/mobile-audit/audit-tracker.xlsx`
- Tracker helpers: `portfolio-site/working/mobile-audit/scripts/tracker-helpers.py`
- Case-sharing prior handoff (pattern reference): `portfolio-site/working/mobile-audit/figma-handoff-case-sharing.md`
- Build log: `Get-a-job/BUILD-LOG.md`
- Session state: `Get-a-job/SESSION-STATE.md`

---

## Also out of scope (flag for Della later)

Page `29:41` also has SHR-15 / SHR-16 / SHR-17 HTML in `working/diagrams/v3/` but no desktop Figma frames for them yet. Those are a separate question — do they need Figma frames at all? Don't touch them in either Thread A or B.
