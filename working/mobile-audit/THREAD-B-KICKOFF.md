# Thread B & C Kickoff — SHR UI Screens Figma + Deploy

**Created:** 2026-04-22 (end of Thread A)
**Two follow-on threads, independent of each other:**
- **Thread B** — Ship 8 native-layer Figma mobile frames pairing the 8 SHR UI desktop screens.
- **Thread C** — Deploy the 8 HTML v4 files into `portfolio-site/img/diagrams/` and register them in the diagram viewer.

Either can run first. Thread B needs ~80% context. Thread C is lightweight (~20%). If running the same session, do C first — it's quick and clears the tracker/viewer gap that's blocking mobile preview of the real portfolio.

**Expected context budget (Thread B):** ~80% for all 8 in one thread. Session 10 precedent supports this.

---

## Read these first (in order)

1. `CoworkWorkspace/CLAUDE.md` — global config (voice, Figma tidyPage rule, path mappings)
2. `Get-a-job/CLAUDE.md` — project-specific rules (verify-before-claiming, living documents)
3. `Get-a-job/SESSION-STATE.md` — current state of the project (session 13 header)
4. **`Get-a-job/portfolio-site/working/mobile-audit/handoff-shr-ui-screens-to-figma.md`** — the full Thread B payload (this is the spec)
5. `CoworkWorkspace/Skills/responsive-audit/references/l2-fix-recipes.md` — pattern library Thread A used
6. `Get-a-job/portfolio-site/working/mobile-audit/figma-handoff-case-sharing.md` — session 10 precedent (same pattern, different screens)

---

## What Thread A delivered

Eight v4 responsive HTML files under `Get-a-job/working/diagrams/v4/`:

- SHR-01, 02 → Recipe A (phone + annotations)
- SHR-06, 07 → Recipe B (horizontal scroll carousel)
- SHR-08, 10, 11, 12 → Recipe C (stacked grids / before-after)

All 8: zero horizontal overflow at 240/320/375, quality-check clean, voice-check clean. Single responsive files — no separate `-v4-mobile.html` variants.

Tracker rows at `portfolio-site/working/mobile-audit/audit-tracker.xlsx` — 8 rows with `case_study=case-sharing`, `status=fixed`, `figma_mobile_node_id=None` (Thread B populates).

---

## What Thread B owns

Create 8 native-layer Figma mobile frames at `x=-1300, y=<desktop.y>` on page `29:41` in file `TArUrZsBUocaAsqetjXq7V`. Each frame pairs its desktop counterpart and renders the mobile HTML v4 layout at 375px width.

Exact y-coords, recipe assignments, and layout notes are in the handoff doc table (Section: "The 8 screens — Thread B input table").

---

## First action (don't skip — per-screen quality gate)

1. Ship **shr01-mobile** only
2. Screenshot the Figma frame via `mcp__Figma__get_screenshot`
3. Open `working/diagrams/v4/SHR-01-before-share-sheet-v4.html` in browser at 375px width, screenshot
4. Compare side-by-side — layout parity on structure, spacing, typography hierarchy
5. If parity checks out, proceed to the other 7
6. If not, fix shr01-mobile before touching shr02

This gate exists because native-layer Figma work diverges from HTML in subtle ways (font rendering, shadow stacking, auto-layout quirks). Catching one divergence early prevents replicating it across 8 frames.

---

## Hard constraints (copied from handoff doc — non-negotiable)

1. Native layers only. No image fills. Every element is a `createFrame` / `createText` / `createRectangle` / `createEllipse` / `createVector` primitive.
2. **Never `tidyPage()` on page 29:41.** Desktop cluster is hand-positioned. APPEND only.
3. Frame names: `shrXX-mobile` (e.g. `shr01-mobile`).
4. CSS-selector layer names so figma-to-html roundtrip works (`.phone-placeholder`, `.annotations`, `.card`).
5. Two-phase MCP: mutate-and-commit (no throw) → separate query-and-throw.
6. `layoutPositioning='ABSOLUTE'` set AFTER `appendChild`, not before.
7. Root frame: auto-layout VERTICAL, `primaryAxisSizingMode='AUTO'`, `counterAxisSizingMode='FIXED'`, `width=375`.
8. Atomic tracker writes via `tracker-helpers.py` `update_row` — set `figma_mobile_node_id` after each pairing. Never pandas.

---

## Known landmine — shr10

The hub-and-spoke layout breaks at ≤360px in HTML (spokes overlap hub-center). Thread A left this in place. Thread B has two options:

- **(Recommended)** Redesign in Figma as stacked 2×3 grid (hub on top, 6 platform icons beneath). Flag this as an intentional divergence from HTML.
- **(Fallback)** Preserve radial layout, accept that it only reads cleanly at ≥360px.

Decide before building shr10-mobile. If redesigning, update both the Figma frame AND `SHR-10-cross-platform-previews-v4.html` so the HTML-Figma pair stays in sync.

---

## Close-out checklist (end of Thread B)

- [ ] 8 mobile frames created on page 29:41 at x=-1300
- [ ] shr01-mobile quality gate passed before proceeding
- [ ] Tracker: all 8 rows have `figma_mobile_node_id` populated
- [ ] `handoff-shr-ui-screens-to-figma.md` — executed-node-IDs table filled in (bottom of doc)
- [ ] BUILD-LOG.md session entry appended
- [ ] SESSION-STATE.md updated: SHR UI screens pairing ✅ COMPLETE
- [ ] If shr10 redesigned: both Figma frame AND v4 HTML updated

---

## If you run out of context mid-thread

Write `CONTEXT-CHECKPOINT.md` in this folder with:
- Which of the 8 frames are shipped (node IDs)
- Which are in-progress
- Which are untouched
- Any divergence decisions made (especially shr10)

Session 14 resumes from there.

---

## First message to Della (Thread B)

"Ready to kick off Thread B. I've read the handoff doc and confirmed the 8-screen table, recipe assignments, and hard constraints. Starting with shr01-mobile — I'll ship the frame, screenshot it against the HTML v4 at 375, and show you the comparison before proceeding to the other 7. Proceed?"

---

# Thread C — Deploy + viewer-register the 8 SHR UI screens

**Why this exists:** Thread A's 8 v4 HTML files live in `Get-a-job/working/diagrams/v4/`. They pass quality-check and voice-check, but they're not reachable from the live portfolio — not deployed, not in the diagram viewer, can't be previewed via the `file:///.../diagram-viewer.html?d=...` pattern Della uses to spot-check work.

Thread B won't close this gap — Thread B is Figma-only.

## The gap, concretely

| Where | SHR UI screens (8) | Port diagrams (5, for reference) |
|---|---|---|
| Tracker (`audit-tracker.xlsx`) | ✅ All 8 rows written | ✅ All 5 rows present |
| Deployed to `portfolio-site/img/diagrams/` | ❌ Not deployed | ✅ All 5 files present |
| Registered in `diagram-viewer.html` manifest | ❌ Not in `case-sharing` array | ✅ All 5 in `case-building-portfolio` array |
| Viewer URL loads | ❌ — | ✅ `?d=port05-recruiter-panel-v4` works |

## Owner

The `diagram-deploy` skill. Read `.claude/skills/diagram-deploy/SKILL.md` first — it handles the last-mile translation from `working/diagrams/` → `portfolio-site/img/diagrams/` and may have a viewer-registration helper.

If `diagram-deploy` doesn't already cover viewer-manifest registration, extend it. One-off edits to the viewer manifest will drift over time.

## Scope

For each of the 8 SHR UI screens (shr01, 02, 06, 07, 08, 10, 11, 12):

1. Copy (or translate, if the skill requires) from `Get-a-job/working/diagrams/v4/SHR-XX-*-v4.html` into `portfolio-site/img/diagrams/diagram-shrXX-*-v4.html` following the deployed naming convention (`diagram-shrXX-` prefix, lowercase).
2. Register the new entry in `portfolio-site/working/diagram-viewer.html` under the `case-sharing` array. Fields: `id`, `name`, `file`. Keep the existing shr03/04/05/09/13/14 ordering — insert new entries in sequence (shr01, shr02 go before shr03; shr06, shr07, shr08 between shr05 and shr09; shr10, shr11, shr12 after shr09 and before shr13).
3. Smoke-test each via the viewer URL at 375 width: `file:///Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/diagram-viewer.html?w=375&mode=single&d=shrXX-<slug>-v4`
4. Update the tracker: set `mobile_file_path` on each of the 8 rows to the new deployed path (`portfolio-site/img/diagrams/diagram-shrXX-*-v4.html`). Atomic writes via `tracker-helpers.py` `update_row`. Never pandas.
5. Check that the case-sharing case-study HTML page (wherever it lives in `portfolio-site/`) references these diagrams if it's supposed to — if the desktop case study was already using placeholders or inline diagrams for these 8 screens, swap those in.

## Quality gate

- Each deployed file opens via viewer URL at 375 width without broken assets, layout errors, or console warnings
- No horizontal overflow (Playwright verify at 240/320/375 — reuse `tmp/shr-verify/verify.py` with updated paths)
- `quality-check.py` still clean after deploy
- Tracker: all 8 rows have the new `mobile_file_path` populated
- Nothing committed to git — show Della the diff, let her review and push

## Close-out checklist (Thread C)

- [ ] 8 files deployed to `portfolio-site/img/diagrams/`
- [ ] 8 entries registered in `diagram-viewer.html` manifest under `case-sharing`
- [ ] Viewer URL works for all 8 screens at 375px
- [ ] Tracker rows updated with new `mobile_file_path`
- [ ] quality-check + voice-check re-run, still clean
- [ ] Della shown the diff; given terminal commands to commit + push
- [ ] BUILD-LOG.md appended
- [ ] SESSION-STATE.md updated

## First message to Della (Thread C)

"Ready to deploy the 8 SHR UI v4 files to the portfolio img/diagrams folder and register them in the viewer. I'll work through `diagram-deploy` skill, start with shr01, smoke-test it at the viewer URL, then batch the other 7. Show you the diff before any git commit. Proceed?"
