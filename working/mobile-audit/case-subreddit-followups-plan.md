# Case-Subreddit Followups — Plan Doc

**Created:** 2026-04-22 (Session 28 close-out, parallel Workstream A review gate thread)
**Status:** PLAN — ready to launch as one or two focused threads
**Precondition:** Workstream A shipped (commit `f57865f case-subreddit: Workstream A x=914 Figma polish (9 diagrams)` on origin/main)
**Retirable when:** both scopes (A1 and A2) complete and verified on the live site

---

## Why this exists

After Workstream A shipped, `case-subreddit` is functionally complete — 10 diagrams live, mobile-responsive, Figma-paired, linter-clean. But two followup gaps remain that would take the case study from "shipped" to "tight":

1. **Mobile Figma frames may slightly lag the polished HTML.** The x=914 Workstream A polish that just shipped changed visual details (padding, font scale, hues, pill containers, responsive breakpoints) on 5 diagrams. The corresponding mobile Figma frames were paired in earlier sessions *before* those polishes landed, so the mobile Figma representation of those 5 diagrams is one step behind the live HTML. Not broken, but out of sync.

2. **Workstream B frames (6 desktop-only Figma frames) have no HTML.** Session 17 paired 6 new Figma desktop+mobile frames (SUB-07, SUB-10a/b, SUB-11a/b, SUB-12s) but they were never authored as HTML. They live only in Figma and are not embedded in `case-subreddit.html`. They represent additional content density that could expand the case study.

Both are optional — the case study is presentable today. These scopes push it toward exhaustive.

---

## Scope A1 — Mobile Figma resync (5 frames)

**Goal:** Update the existing mobile Figma frames to match the polished HTML that shipped in Workstream A Session 28.

**Direction:** HTML → Figma (use `html-to-figma` skill, which handles this direction of the roundtrip).

**Affected diagrams and mobile node IDs:**

| Diagram | HTML file | Mobile Figma node | What changed in HTML (Workstream A) |
|---|---|---|---|
| sub05-artifact-alignment | `img/diagrams/diagram-sub05-artifact-alignment.html` | `925:26` | Per-card number hue: accent / warm / blue / resur per card index |
| sub06-threshold-calibration | `img/diagrams/diagram-sub06-threshold-calibration.html` | `936:26` | Pill-container SVG added to threshold text (rect + centered text) |
| sub08-creation-after | `img/diagrams/diagram-sub08-creation-after.html` | `946:26` | `.step-label` font-size 14px → 12px |
| sub11-text-bars | `img/diagrams/diagram-sub11-text-bars.html` | `951:26` | `.pillar-number` font-size 28 → 36, opacity 0.12 → 0.18; `.pillar-card` padding 16 → 20 |
| sub12-text-bars | `img/diagrams/diagram-sub12-text-bars.html` | (none currently — pair during resync) | Pattern C responsive collapse (`@media max-width:768 { .stalls-grid { grid-template-columns: 1fr; } }`) |

**Note on sub12-text-bars:** it has no existing mobile Figma node (`audit-tracker.xlsx figma_mobile_node_id` is empty for this row). During Scope A1, create the mobile Figma frame from the freshly responsive HTML and backfill the tracker's `figma_mobile_node_id` column.

**Figma file:** `TArUrZsBUocaAsqetjXq7V`, page `29:40` (case-subreddit diagrams page), mobile cluster at `x = -1634` (per Session 17 convention).

**Approach per diagram:**
1. Invoke `html-to-figma` skill with the HTML file + existing mobile node ID as the target.
2. For sub12-text-bars: create a new mobile frame at `x = -1634`, `width = 375`, placed below the existing mobile cluster (check sibling y-coordinates first).
3. Verify in Figma that mobile frame now renders to match HTML at 375px breakpoint.
4. Update `audit-tracker.xlsx`: for sub12-text-bars, set `figma_mobile_node_id` to new node. For all 5, append `verify_date = 2026-04-22` (or current date) and add a resync note to `notes`.

**Non-negotiables:**
- Figma Plugin API tidyPage cleanup rule (see global CLAUDE.md) — leave the page in a clean grid after any `use_figma` call.
- Dev Mode MCP alt namespace: `mcp__8e95afc0-e30e-4e27-bfa2-90ccd2e7b3a9__*` (the `mcp__Figma__*` variant errors; confirmed across Sessions 17/18/24/25/27/28).
- No HTML edits — HTML is the source of truth for this scope.

**Verification:**
- Figma `get_screenshot` on each updated mobile node ID, spot-check against the live HTML at 375px.
- No deploy needed (mobile Figma is reference, not production).

**Estimated effort:** ~1–2 hours for all 5 frames.

---

## Scope A2 — Workstream B HTML authoring (6 diagrams + their mobile)

**Goal:** Author responsive HTML for the 6 Workstream B Figma frames, then deploy to `case-subreddit.html`.

**Direction:** Figma → HTML (use `figma-to-html` skill for each desktop frame; then author mobile CSS + verify against existing Figma mobile node).

**Source frames (from `figma-handoff-case-subreddit.md` Session 17 addendum):**

| Diagram ID | Desktop Figma node | Mobile Figma node | Mobile dimensions | Status |
|---|---|---|---|---|
| sub07-single-text-input | `315:2` | `1064:26` | 375 × 863 | HTML needed |
| sub10a-disorienting-landing | `326:2` | `1068:26` | 375 × 890 | HTML needed |
| sub10b-structured-landing | `327:2` | `1072:26` | 375 × 936 | HTML needed |
| sub11a-surface-adapts-to-stage | `329:2` | `1075:26` | 375 × 981 | HTML needed |
| sub11b-contextual-depth | `330:2` | `1076:26` | 375 × 904 | HTML needed |
| sub12s-text-bars-stall-points-static | `340:2` | `1037:26` | 375 × 509 | HTML needed |

**All 6 paired at Figma `x = -1634` (mobile cluster anchor), width 375, native-rendered (no image fills).**

**Approach per diagram:**
1. `figma-to-html` skill on the desktop node → generates `img/diagrams/diagram-subNN-<slug>.html`. Follow the voice-check-friendly prose (no banned patterns, no jargon).
2. Write responsive CSS to match the existing mobile Figma frame (use Figma `get_screenshot` on the mobile node as the reference).
3. Voice-check + quality-check + 6-breakpoint Playwright render (1440/1024/768/480/375/320).
4. Append a new row to `audit-tracker.xlsx` — case_study = `case-subreddit`, status = `shipped` after deploy, both `figma_node_id` and `figma_mobile_node_id` populated.
5. Deploy to `case-subreddit.html` — add new embed section using `diagram-deploy` skill (embeds an iframe with lazy-load + matching container pattern). Decide placement with Della (most are framework/surface diagrams that extend existing narrative threads).
6. Git commit with file-specific stages, push to `origin/main`, verify on `https://della-portfolio.vercel.app/case-subreddit.html`.

**Non-negotiables:**
- Use `figma-to-html` skill per diagram — do not hand-author SVG from screenshots (too lossy).
- Dev Mode MCP alt namespace `mcp__8e95afc0-e30e-4e27-bfa2-90ccd2e7b3a9__*` for all Figma reads.
- Voice-check must pass — any prose in the diagrams goes through `portfolio-site/voice-check.py` and `voice-rules/banned-patterns.yaml`.
- Match the mobile Figma frames exactly — Della hand-built those, they are the source of truth for mobile layout. Do not reflow to what "looks right" in CSS.
- Atomic tracker writes via `scripts/tracker-helpers.py` (`th.add_row` if not present, `th.update_row` by diagram_id string — never by row index).
- No `git add -A` — file-specific stages only.
- All terminal commands use Mac absolute paths per `~/CoworkWorkspace/PATH-MAPPINGS.md`.

**Verification:**
- Per diagram: voice-check + quality-check + 6-breakpoint render.
- Post-deploy: Playwright full-page screenshots of `case-subreddit.html` at 1440 and 375, confirm all new embeds render without layout regressions on existing diagrams.
- Live site verification after Vercel deploy.

**Estimated effort:** ~1–2 hours per diagram (6 diagrams → 8–12 hours total). Can chunk into two sessions (3 diagrams each).

---

## Deferred polish items (Workstream A leftovers)

These are cosmetic-only, pickupable either inside Scope A1 (if you're already touching Figma) or in a separate focused thread. Full resume instructions live in `working/mobile-audit/workstream-a-deferred-items.md`.

**Item 1 — sub05 Card 4 mini-UI thumbnail swap**
- Replace 3 color swatches with 3 mini-UI preview SVGs.
- Figma reference: node `678:700` (x=914 polish column).

**Item 2 — sub09 icon glyph swaps (Share / Engage / Trust)**
- Swap megaphone/heart/shield-check → play/infinity/checkbox.
- Figma reference: node `678:1056` (x=914 polish column).

---

## Dependencies and order

- Scope A1 and Scope A2 are independent. Either can start first.
- Scope A1 is smaller and tighter to Workstream A — reinforces the Figma↔HTML roundtrip muscle. Low risk, fast win.
- Scope A2 is larger — adds new content density to case-subreddit. Higher impact but more authorship work.
- The two deferred items can roll into Scope A1 if you're already in Figma mode.

**Recommended order:** Scope A1 first (quick resync + finish deferred items), then Scope A2 (authorship batch, chunked 3 + 3).

---

## Key file paths (Mac absolute)

- Portfolio repo: `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/`
- Audit tracker: `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/audit-tracker.xlsx`
- Figma handoff (source of Workstream B frame list): `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/figma-handoff-case-subreddit.md`
- Workstream A deferred items: `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/workstream-a-deferred-items.md`
- Case page (embed target for Scope A2): `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/case-subreddit.html`
- Tracker helpers: `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/scripts/tracker-helpers.py`
- Voice linter: `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/voice-check.py`
- Quality linter: `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/quality-check.py`
- Global config: `/Users/della/CoworkWorkspace/CLAUDE.md`
- Project config: `/Users/della/CoworkWorkspace/Get-a-job/CLAUDE.md`
- Path mappings: `/Users/della/CoworkWorkspace/PATH-MAPPINGS.md`

---

## Context carry-forward from Workstream A Session 28

**Figma file and structure:**
- File: `TArUrZsBUocaAsqetjXq7V`
- Page: `29:40` (case-subreddit page)
- `x = 914` column = Della's x=914 polish (Workstream A source of truth for desktop polish)
- `x = 80` column = desktop-only frames (Workstream B source)
- `x = -1634` = mobile cluster (all mobile frames live here)

**Skills to use:**
- `html-to-figma` — for Scope A1 (sync polished HTML to mobile Figma)
- `figma-to-html` — for Scope A2 (author new HTML from Workstream B Figma frames)
- `responsive-audit` — for verifying Scope A2 HTML at 6 breakpoints
- `diagram-deploy` — for embedding Scope A2 HTML into `case-subreddit.html`

**Skills to NOT use:**
- `recruiter-panel` — unless Della specifically asks for a regression check on a content-changed diagram. None of these scopes rewrite Della-voiced prose significantly.

**Git safety (from Session 22 + 28):**
- No `git add -A` — file-specific stages only. Mixed-workstream branches (case-notifications + case-subreddit + Workstream B all coexist).
- No push without Della's review.
- Commit messages: prefix with `case-subreddit:` for Scope A1/A2 (both remain case-subreddit scope).
