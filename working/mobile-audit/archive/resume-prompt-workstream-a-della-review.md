# Resume Prompt — Workstream A Della Review Gate

**Created:** 2026-04-22 (Session 27 close-out)
**Status:** ACTIVE — awaiting Della's per-diagram decisions on 8 flagged items
**Predecessor:** `resume-prompt-workstream-a-html-updates.md` (Workstream A kickoff — Session 24+27 execution phase complete, this file picks up the review gate)
**Retirable when:** all 8 items resolved + push to `origin/main` lands

---

## TL;DR for the picking-up thread

Session 27 closed out the execution phase of Workstream A: 11 case-subreddit HTML diagrams compared element-by-element against Della's x=914 Figma polish column on page `29:40` in file `TArUrZsBUocaAsqetjXq7V`. 7 diagrams received clean CSS polish edits under automation authority (prevailing-pattern matches); 3 matched Figma already with no edits; 1 (sub01) received Della-approved structural JS edit during live workflow. All 11 are linter-clean and 6-breakpoint render-clean.

**This thread's job:** walk Della through the 8 flagged items (one per diagram with pending work), apply the edits she approves, verify per file, update tracker atomically, and commit+push when all 8 resolve.

## Non-negotiables (carry forward from Workstream A)

- **No Figma edits.** Read-only on the Figma file. Use Dev Mode MCP under namespace `mcp__8e95afc0-e30e-4e27-bfa2-90ccd2e7b3a9__*` (the `mcp__Figma__*` variant errors with "enable Dev Mode MCP Server" — same workaround confirmed across Sessions 17/18/24/25/27).
- **No `diagram-deploy` runs.** Edits go directly in `portfolio-site/img/diagrams/diagram-sub*.html`.
- **Linters per edit:** `voice-check.py` + `quality-check.py` must pass on every edited file before moving on.
- **6-breakpoint render per edit:** Playwright headless Chromium at 1440/1024/768/480/375/320, confirm zero horizontal overflow + no layout breaks.
- **Tracker writes atomic via `scripts/tracker-helpers.py` openpyxl.** Public API: `th.update_row(path, diagram_id, updates)` — takes `diagram_id` string, NOT row index. Initial Session 27 KeyError captured as gotcha.
- **No `git add -A`.** File-specific stages only — mixed-workstream branches (per Session 22 push-command-gotcha).
- **All terminal commands use Mac absolute paths** from `CoworkWorkspace/PATH-MAPPINGS.md`. Never emit `/sessions/...` paths to Della.

## Pre-flight reads (mandatory before any work)

1. `~/CoworkWorkspace/CLAUDE.md` — global voice rules, session protocol, file routing, terminal safety gate
2. `~/CoworkWorkspace/PATH-MAPPINGS.md` — sandbox↔Mac path conversion rule
3. `~/CoworkWorkspace/Get-a-job/CLAUDE.md` — project-specific rules (verify before claiming, living documents, source verification)
4. `~/CoworkWorkspace/Get-a-job/SESSION-STATE.md` — Session 27 top paragraph has the full Workstream A state
5. `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/resume-prompt-workstream-a-html-updates.md` — the original Workstream A kickoff for background on the automation-authority decision tree
6. This file — for the 8 decision items below

## The 8 decision items (one per diagram with pending work)

Walk Della through these one at a time. For each: present the flag, explain why it was not auto-applied, offer apply / skip / iterate. If apply: make the edit, run linters, render at 6 breakpoints, update tracker note, move to next.

### 1. sub02 — recruiter-panel regression check (SEMANTIC)

**What happened in Session 27:** Della approved A+B+C+D+E+F (text swap to "Stage N" eyebrows + single-word stage nouns, horizontal padding fix, accent line 100px→100%, per-stage eyebrow hue, card padding swap 16/20→20/16, border-radius 10→12). Text swap is the one that could affect recruiter-panel scoring.

**Claude's pre-assessment:** Semantic assessment only — the new eyebrow/title pattern strengthens the "Five-Stage Lifecycle Framework" signal against v3 baseline (reinforces positioning rather than weakening it). Not a regression.

**Della's decision needed:** formally re-run `recruiter-panel` skill against sub02 for a scored regression check, or accept Claude's semantic assessment and move on?

- **Apply (formal run):** invoke `recruiter-panel stages:2 company:Anthropic,Figma,Ramp` against case-subreddit
- **Skip:** accept semantic assessment, note in tracker

### 2. sub03 — "Gate:" prefix text swap (TEXT)

**Figma shows:** 5 stage descriptions carry a "Gate:" prefix. Stage 1 rewrites from "Identity, category, first description" → "Gate: community launched with identity + category".

**Why not auto-applied:** Text change, not prevailing-pattern CSS polish. Flagged for Della per authority rule.

**Della's decision needed:**
- **Apply full:** Claude rewrites all 5 stage descriptions with "Gate:" prefix + stage 1 rewrite per Figma
- **Apply partial:** Claude applies only the "Gate:" prefix addition, keeps stage 1 text as-is
- **Skip:** keep HTML text as current, note in tracker

### 3. sub05 — Card 4 visualization swap (STRUCTURAL)

**Figma shows:** Card 4 "Design Patterns" — 3 color swatches replaced with 3 mini-UI preview thumbnails.

**Why not auto-applied:** Structural HTML addition (new SVG/img elements), not CSS polish. Flagged.

**Della's decision needed:**
- **Apply:** Claude builds 3 mini-UI thumbnail SVGs matching sub04's canonical icon style (1.5 stroke, currentColor) and swaps in
- **Skip:** keep 3 color swatches, note in tracker
- **Iterate:** Della sketches what she wants the mini-UIs to represent, Claude builds from that

### 4. sub06 — "Most fail here" → pill container (STRUCTURAL)

**Figma shows:** "Most fail here" annotation wrapped in a pill container (SVG rect with rounded corners + fill).

**Why not auto-applied:** SVG rect addition = structural. Flagged.

**Della's decision needed:**
- **Apply:** Claude wraps existing annotation text in a pill container matching Figma
- **Skip:** keep annotation as-is
- **Iterate:** Della specifies exact rect dimensions + fill treatment

### 5. sub08 — step-label font-size 14→12 (SUBJECTIVE)

**Figma vs HTML:** step-label in HTML renders at 14px; Figma version appears 12px. Difference is subtle.

**Why not auto-applied:** Subjective scale call, not a prevailing-pattern match. Flagged.

**Della's decision needed:**
- **Apply:** `.step-label { font-size: 14px → 12px }`
- **Skip:** leave at 14px, note "not a regression, Figma/HTML acceptably close"

### 6. sub09 — icon glyph swaps (STRUCTURAL SVG)

**Figma shows 3 icon changes:**
- Share card: megaphone → play/triangle
- Engage card: heart → infinity/rings
- Trust card: shield-check → checkbox

**Why not auto-applied:** Glyph substitution = SVG path replacement, not stroke/fill polish. Flagged.

**Della's decision needed:**
- **Apply all 3:** Claude replaces all 3 SVGs with sub04-style 1.5-stroke currentColor versions of the new glyphs
- **Apply subset:** pick which glyphs to swap
- **Skip:** keep existing glyphs, note in tracker

### 7. sub11 — pillar-number scale + card padding (SUBJECTIVE, 2 items)

**Figma vs HTML:**
- pillar-number (01/02/03): Figma shows larger + more visible than HTML's 28px @ 0.12 opacity
- card padding: Figma scale feels more generous than HTML's 16px

**Why not auto-applied:** Both are subjective scale/opacity calls, not pattern matches. Flagged together since they're the same diagram.

**Della's decision needed:**
- **Apply both:** Claude bumps pillar-number to (propose 36px @ 0.18 opacity) + card padding 16→20
- **Apply one:** pick which
- **Skip:** leave both as-is, note "Figma/HTML acceptably close"
- **Iterate:** Della specifies exact values she wants

### 8. sub12t — missing media queries (OUT OF WORKSTREAM A SCOPE)

**Issue discovered mid-Session 27:** `diagram-sub12-text-bars.html` has NO media queries. The 3-col grid (`grid-template-columns: 1fr 1fr 1fr`) doesn't stack on mobile — cards become narrow at @480 with awkward text wrap.

**Why not auto-applied:** Out of Workstream A scope (that's responsive breakpoint work, not x=914 polish parity).

**Della's decision needed:**
- **Fix now (scope creep, ok):** Claude adds `@media (max-width: 768px) { .stalls-grid { grid-template-columns: 1fr; gap: 10px; } }` per Pattern C from `Skills/responsive-audit/references/l2-fix-recipes.md`
- **Defer to responsive-audit skill run:** Claude does NOT edit sub12t, logs a new `audit-tracker.xlsx` follow-up row with `severity=2` for a proper responsive-audit thread to pick up
- **Skip entirely:** note as known limitation, move on

## After all 8 decisions resolve

1. Final pass: re-run `voice-check.py` + `quality-check.py` on every edited file
2. Re-render 6 breakpoints via Playwright on every edited file (fresh Chromium install if sandbox got restarted)
3. If Della approved the formal `recruiter-panel` re-run for sub02: run and report scores against baseline
4. Update tracker one last time with final Session 28 note on every touched row
5. Generate Mac-absolute git commands for Della:
   ```
   cd ~/CoworkWorkspace/Get-a-job/portfolio-site
   git status
   git add img/diagrams/diagram-sub01-survival-curve.html \
           img/diagrams/diagram-sub02-lifecycle-framework.html \
           [... only the files actually edited ...]
           working/mobile-audit/audit-tracker.xlsx
   git commit -m "$(cat <<'EOF'
   case-subreddit: Workstream A x=914 Figma parity polish (11 diagrams)

   [list of edits applied]
   EOF
   )"
   git push origin main
   ```
6. Update BUILD-LOG.md + SESSION-STATE.md with Session 28 close-out entry
7. Move this resume prompt to `working/mobile-audit/archive/`

## Files touched in Session 27 (for reference)

Edited (CSS-only polish inside existing `<style>` blocks):
- `portfolio-site/img/diagrams/diagram-sub01-survival-curve.html` — padding 32→48px + bezier 10-point→3-anchor
- `portfolio-site/img/diagrams/diagram-sub02-lifecycle-framework.html` — 6-edit combo (A+B+C+D+E+F)
- `portfolio-site/img/diagrams/diagram-sub03-milestone-model.html` — border-radius + card padding
- `portfolio-site/img/diagrams/diagram-sub04-strategic-starting-points.html` — border-radius + per-bet eyebrow hue
- `portfolio-site/img/diagrams/diagram-sub05-artifact-alignment.html` — per-card number hue (1→accent, 2→warm, 3→blue, 4→resur)
- `portfolio-site/img/diagrams/diagram-sub06-threshold-calibration.html` — detail-card border-radius + accent-before radius
- `portfolio-site/img/diagrams/diagram-sub11-text-bars.html` — pillar-card border-radius + ::before corners
- `portfolio-site/img/diagrams/diagram-sub12-text-bars.html` — stall-card border-radius + ::before corners

Assessed, no edits applied (already matched Figma):
- `portfolio-site/img/diagrams/diagram-sub08-creation-after.html`
- `portfolio-site/img/diagrams/diagram-sub09-distribution-loop.html`
- `portfolio-site/img/diagrams/diagram-sub12-instrumentation-interactive.html`

Tracker writes (all via `th.update_row` or `th.append_row`):
- `portfolio-site/working/mobile-audit/audit-tracker.xlsx` — 10 existing rows appended Workstream A notes; 1 new row (`sub12-text-bars`, `figma_node_id=678:1367`) appended with full schema

## Figma reference (read-only)

File: `TArUrZsBUocaAsqetjXq7V`
Page: `29:40` (case-subreddit)
Column: x=914 (Della's polish column)
Canonical x=914 node IDs per diagram:
- sub01: `678:5`
- sub02: `678:259`
- sub03: `678:490`
- sub04: `678:625`
- sub05: `678:700`
- sub06: `678:822`
- sub08: `678:924`
- sub09: `678:1056`
- sub11: `678:1196` (HTML filename is `-sub11-text-bars.html` but content is three-pillars; filename rename deferred per Workstream A brief)
- sub12c (instrumentation): `678:1249`
- sub12t (text-bars): `678:1367`

## Gotchas already captured (don't re-discover)

1. Figma Dev Mode MCP: `mcp__Figma__*` namespace errors with "enable Dev Mode MCP Server" — use `mcp__8e95afc0-e30e-4e27-bfa2-90ccd2e7b3a9__*` instead. Confirmed across Sessions 17/18/24/25/27 — skill-reference authorship candidate per CLAUDE.md Lessons → Skill References rule.
2. `tracker-helpers.py` public API: `update_row(path, diagram_id, updates)` takes `diagram_id` string. Session 27 initially passed row index and got `KeyError: 'No row for diagram_id=39'`. Use the string.
3. If a diagram_id has no existing tracker row, use `th.append_row(path, full_row_dict)` — don't silently skip the tracker update.
4. `throw new Error('DATA:...')` at the end of a Figma mutation script rolls back all writes (Session 17 learning). Use `figma.notify()` + separate read-only verify call. Doesn't apply to this thread (no writes to Figma) but keep in mind.
5. Playwright + Chromium may need reinstall if sandbox got restarted:
   ```bash
   pip install playwright --break-system-packages
   python3 -m playwright install chromium
   ```
