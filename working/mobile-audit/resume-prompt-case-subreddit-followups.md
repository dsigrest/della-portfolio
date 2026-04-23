# Resume Prompt — Case-Subreddit Followups

**Created:** 2026-04-22 (Session 28 close-out, parallel Workstream A review gate thread)
**Status:** A1 COMPLETE (2026-04-22 Session 30) + A2 HTML AUTHORING COMPLETE (2026-04-22 Session 31c) — all 6 Workstream B HTML files shipped, voice + quality + 6-breakpoint render clean, 6 tracker rows verified. **Embed to `case-subreddit.html` via `diagram-deploy` explicitly DEFERRED** per Della Session 31c call (authorship-only scope). Both this parent file and `resume-prompt-case-subreddit-scope-a2.md` stay active until the embed lands. Retirable only after a future thread (a) runs `diagram-deploy` to embed all 6 into `case-subreddit.html`, (b) does full-page regression screenshots at 1440/375 confirming no regressions on existing 10 diagrams, (c) commits + pushes to `origin/main` and verifies on `della-portfolio.vercel.app`.
**Predecessor:** `archive/resume-prompt-workstream-a-della-review.md` (Workstream A complete, commit `f57865f` on origin/main)
**Successor for A2:** `resume-prompt-case-subreddit-scope-a2.md` (self-sufficient kickoff — includes A1 carry-forward state inline)
**A1 outcome (shipped):** sub05 `925:26` (card hues), sub06 `936:26` (pill container), sub08 `946:26` (step-label 14→12), sub11 `951:26` (pillar-number 28→36 + opacity 0.12→0.18), sub12-text-bars NEW `1123:26` (sub12t-mobile, 375×414 at x=-1634 y=17723). Tracker updated. No HTML edits, no git commits. See `resume-prompt-case-subreddit-scope-a2.md` ("Carry-forward from A1" section) for full state.
**Retirable when:** both Scope A1 (mobile Figma resync) and Scope A2 (Workstream B HTML) complete and verified on live site. A1 done — retire after A2 ships.

---

## TL;DR for the picking-up thread

`case-subreddit` is shipped — 10 diagrams live, mobile-responsive, Figma-paired. Two optional followup scopes remain to take the case study from "shipped" to "tight":

- **Scope A1 — Mobile Figma resync (5 frames):** the x=914 polish that shipped in Workstream A Session 28 changed visual details on sub05/06/08/11/12-text-bars. Mobile Figma frames for these were paired *before* those polishes landed, so mobile Figma is one step behind live HTML. Direction: HTML → Figma via `html-to-figma` skill.
- **Scope A2 — Workstream B HTML authoring (6 diagrams):** Session 17 paired 6 Figma desktop+mobile frames (SUB-07, SUB-10a/b, SUB-11a/b, SUB-12s) but they never had HTML counterparts. They live only in Figma and are not embedded in `case-subreddit.html`. Direction: Figma → HTML via `figma-to-html` skill, then deploy.

**This thread's job:** pick one scope (or both), execute per the plan doc, verify per file, commit + push when each diagram completes.

---

## Pre-flight reads (mandatory before any work)

1. `~/CoworkWorkspace/CLAUDE.md` — global voice rules, session protocol, Figma Plugin API tidyPage rule, terminal safety gate
2. `~/CoworkWorkspace/PATH-MAPPINGS.md` — sandbox↔Mac path conversion rule
3. `~/CoworkWorkspace/Get-a-job/CLAUDE.md` — verify before claiming, living documents rule, source verification rule
4. `~/CoworkWorkspace/Get-a-job/SESSION-STATE.md` — Session 28 close-out state
5. `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/case-subreddit-followups-plan.md` — the full plan doc for both scopes (read this — it has the frame tables, node IDs, verification steps)
6. `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/figma-handoff-case-subreddit.md` — Session 17 addendum with Workstream B frame details
7. `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/workstream-a-deferred-items.md` — two deferred Workstream A polish items (sub05 Card 4 mini-UIs, sub09 icon glyphs); pickupable inside Scope A1 if touching Figma
8. This file — for kickoff and scope selection

## Non-negotiables (carry forward from Workstream A)

- **Dev Mode MCP alt namespace:** `mcp__8e95afc0-e30e-4e27-bfa2-90ccd2e7b3a9__*` (the `mcp__Figma__*` variant errors with "enable Dev Mode MCP Server" — confirmed across Sessions 17/18/24/25/27/28).
- **Figma Plugin API tidyPage:** every `use_figma` call that creates or modifies frames must leave the page in a clean non-overlapping grid. Include the `tidyPage` helper from global CLAUDE.md.
- **Linters per edit:** `voice-check.py` + `quality-check.py` must pass on every edited or authored HTML file before moving on.
- **6-breakpoint render per new/edited HTML:** Playwright headless Chromium at 1440/1024/768/480/375/320, confirm zero horizontal overflow + no layout breaks.
- **Tracker writes atomic via `scripts/tracker-helpers.py` openpyxl.** Public API: `th.update_row(path, diagram_id, updates)` — takes `diagram_id` string, NOT row index. Use `th.add_row` for Workstream B new rows.
- **No `git add -A`.** File-specific stages only — mixed-workstream branches.
- **All terminal commands use Mac absolute paths** from `~/CoworkWorkspace/PATH-MAPPINGS.md`. Never emit `/sessions/...` paths.
- **No Figma writes outside your declared scope.** Scope A1 writes to 5 mobile nodes (plus 1 new one for sub12-text-bars). Scope A2 reads only — HTML is the output, Figma mobile frames for B are already built.

## Start here (thread kickoff flow)

1. Read the plan doc: `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/case-subreddit-followups-plan.md`
2. Ask Della which scope to tackle (A1, A2, or both back-to-back). If she wants both: recommend A1 first (smaller, tighter turnaround).
3. For A1: walk through each of the 5 frames (plan doc has the full table), use `html-to-figma` skill per frame, verify via `get_screenshot` after each, update tracker, commit when all 5 done.
4. For A2: walk through each of the 6 frames, use `figma-to-html` skill per frame, pair to existing mobile Figma node, voice-check + quality-check + 6-breakpoint render, deploy to `case-subreddit.html` with `diagram-deploy` skill, update tracker, commit + push per diagram (or batched 2–3 at a time).
5. Close out when the chosen scope completes: update `SESSION-STATE.md` top paragraph, append to `BUILD-LOG.md`, archive this resume prompt.

## Key frame tables (quick reference — full details in plan doc)

### Scope A1 — 5 frames to resync (HTML → Figma)

| Diagram | HTML file | Mobile Figma node |
|---|---|---|
| sub05-artifact-alignment | `img/diagrams/diagram-sub05-artifact-alignment.html` | `925:26` |
| sub06-threshold-calibration | `img/diagrams/diagram-sub06-threshold-calibration.html` | `936:26` |
| sub08-creation-after | `img/diagrams/diagram-sub08-creation-after.html` | `946:26` |
| sub11-text-bars | `img/diagrams/diagram-sub11-text-bars.html` | `951:26` |
| sub12-text-bars | `img/diagrams/diagram-sub12-text-bars.html` | *(create new)* |

### Scope A2 — 6 frames to author HTML for (Figma → HTML + deploy)

| Diagram ID | Desktop Figma node | Mobile Figma node |
|---|---|---|
| sub07-single-text-input | `315:2` | `1064:26` |
| sub10a-disorienting-landing | `326:2` | `1068:26` |
| sub10b-structured-landing | `327:2` | `1072:26` |
| sub11a-surface-adapts-to-stage | `329:2` | `1075:26` |
| sub11b-contextual-depth | `330:2` | `1076:26` |
| sub12s-text-bars-stall-points-static | `340:2` | `1037:26` |

**Figma file:** `TArUrZsBUocaAsqetjXq7V`, page `29:40`, mobile cluster at `x = -1634`.

## Ship criteria per scope

### Scope A1 ships when
- All 5 mobile Figma frames match the polished HTML at 375px (verified via `get_screenshot`)
- `audit-tracker.xlsx` updated with resync notes on all 5 rows, sub12-text-bars `figma_mobile_node_id` populated
- Figma page is tidy (tidyPage called after all writes)
- (Optional) deferred Workstream A items rolled in: sub05 Card 4 mini-UIs or sub09 icon glyphs (see `workstream-a-deferred-items.md`)

### Scope A2 ships when
- 6 new HTML files authored, voice-check + quality-check clean, 6-breakpoint Playwright render clean
- All 6 embedded in `case-subreddit.html` with lazy-load iframe pattern
- `audit-tracker.xlsx` has 6 new rows, all `status = shipped` with both desktop and mobile node IDs populated
- Commit pushed to `origin/main`, live on `https://della-portfolio.vercel.app/case-subreddit.html`
- Full-page screenshots at 1440 and 375 confirm no regressions on existing 10 diagrams

## When you're done (close-out steps)

1. Update `~/CoworkWorkspace/Get-a-job/SESSION-STATE.md` top paragraph with completion status
2. Append to `~/CoworkWorkspace/Get-a-job/BUILD-LOG.md` with session entry (decisions, files touched, verification, lessons)
3. If only one scope completed, keep this resume prompt active and update its `Status` header. If both scopes completed, move this file to `working/mobile-audit/archive/`.
4. Update `working/mobile-audit/workstream-a-deferred-items.md` if any deferred items were picked up.
