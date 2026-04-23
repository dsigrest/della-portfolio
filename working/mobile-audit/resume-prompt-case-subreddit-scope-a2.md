# Resume Prompt — Case-Subreddit Scope A2 (Workstream B HTML Authoring)

**Created:** 2026-04-22 (Scope A1 close-out — this is the self-sufficient kickoff for the A2 thread)
**Status:** HTML AUTHORING COMPLETE (2026-04-22 Session 31c) — all 6 Workstream B HTML files shipped, voice + quality + 6-breakpoint Playwright render clean, 6 tracker rows appended (status=verified, both node IDs populated). **Embed to `case-subreddit.html` via `diagram-deploy` explicitly DEFERRED** per Della Session 31c kickoff call. Retirable only after a future thread runs the embed step + full-page regression + commit push.
**Predecessor:** `resume-prompt-case-subreddit-followups.md` (parent, A1 complete)
**Retirable when:** all 6 Workstream B diagrams have HTML authored, voice/quality-check clean, 6-breakpoint render clean, embedded in `case-subreddit.html`, committed to `origin/main`, and live on Vercel.

---

## TL;DR

Scope A1 shipped 2026-04-22 — 5 mobile Figma frames resynced to Workstream A x=914 HTML polish (see "Carry-forward from A1" below for the full state). Scope A2 is the authorship batch: **6 Workstream B Figma frames → HTML → deploy to `case-subreddit.html`**. These 6 live in Figma only (native-layer desktop + mobile paired in Session 17) but have no HTML counterparts. Each needs a new `diagram-subNN-<slug>.html` file, responsive CSS matching the mobile frame, linter-clean, 6-breakpoint render clean, then embedded and deployed.

**This thread's job:** author HTML for the 6 frames (figma-to-html direction), verify per-file, embed + deploy via `diagram-deploy`, commit + push. Recommend chunking into two batches of 3 to keep context manageable.

---

## Carry-forward from A1 (what shipped 2026-04-22)

Scope A1 was executed in the parent thread. State here is factual — use this to regression-check if anything looks off during A2.

**A1 mobile frames modified/created (page 29:40):**

| Diagram | Mobile node | Change |
|---|---|---|
| sub05-artifact-alignment | `925:26` | 4 `.card-number` fills (925:37/60/84/111) → per-card hue accent/warm/blue/resur (`#7FB5B0` / `#D4A574` / `#8A9EC4` / `#C4B078`). Surgical fill update. |
| sub06-threshold-calibration | `936:26` | Added pill-container RECTANGLE inside `.chart-container` (936:40). Deleted split text nodes 936:67/68 ("Most fail" + "here"), replaced with consolidated "Most fail here" centered inside pill. Scale: 311/640=0.486. Pill at Figma (23.3, 44.7, 40.8, 7.8), radius 3.9, red fill at 0.14 opacity. |
| sub08-creation-after | `946:26` | 3 `.step-label` text nodes (946:32/38/44) fontSize 14→12. |
| sub11-text-bars | `951:26` | 3 `.pillar-number` (951:30/51/62) fontSize 28→36, fill opacity 0.12→0.18. Auto-layout VERTICAL parents grew card heights automatically. |
| sub12-text-bars | **NEW `1123:26`** | Built new native-layer mobile frame `sub12t-mobile` at x=-1634, y=17723, 375×414. 3 stall cards (red/warm/blue) matching Pattern C responsive collapse. Absolute-positioned left stripes, glass fills, percent-width bar fills via Pattern A horizontal auto-layout. |

**Tracker state:** `audit-tracker.xlsx` has all 5 rows updated via `th.update_row` atomic writes. sub12-text-bars row now has `figma_mobile_node_id = 1123:26`. All 5 have `verify_date = 2026-04-22` and A1 resync notes appended.

**No HTML edits and no git commits landed in A1.** Figma mutations are external to the repo; tracker writes are local-only until Della commits.

**Naming clarification — three different "sub12" diagrams (don't conflate):**
- `sub12-instrumentation-interactive.html` ↔ `sub12-mobile` (954:26) — heatmap, already deployed
- `sub12s-text-bars-stall-points-static.html` ↔ `sub12s-mobile` (1037:26) — Workstream B, **A2 will author HTML for this**
- `sub12-text-bars.html` ↔ `sub12t-mobile` (1123:26) — A1-created, animated stall points (deployed in case-subreddit.html already)

**Mobile cluster roster post-A1 (all frames at x=-1634, sorted by y):**

| y | node | name | height |
|---|---|---|---|
| 318 | 943:26 | sub01-mobile | 302 |
| 1674 | 915:26 | sub02-mobile | 847 |
| 2525 | 922:26 | sub03-mobile | 963 |
| 3514 | 887:26 | sub04-mobile | 645 |
| 4351 | 925:26 | sub05-mobile | 844 |
| 5309 | 936:26 | sub06-mobile | 517 |
| 6578 | 1064:26 | sub07-mobile | 863 |
| 7735 | 946:26 | sub08-mobile | 597 |
| 8534 | 948:26 | sub09-mobile | 643 |
| 10977 | 1068:26 | sub10a-mobile | 890 |
| 11966 | 1072:26 | sub10b-mobile | 936 |
| 13368 | 1075:26 | sub11a-mobile | 981 |
| 14400 | 1076:26 | sub11b-mobile | 904 |
| 15430 | 951:26 | sub11-mobile | 533 |
| 16145 | 954:26 | sub12-mobile (instrumentation heatmap) | 370 |
| 17134 | 1037:26 | sub12s-mobile (Workstream B static) | 509 |
| **17723** | **1123:26** | **sub12t-mobile (A1 new, text-bars animated)** | **414** |

**Deferred items unchanged:** sub05 Card 4 mini-UI thumbnails + sub09 icon glyph swaps still open per `workstream-a-deferred-items.md`. Not picked up in A1; available for a focused Figma-polish thread or opportunistic roll-in during A2.

**Thread-orchestration lesson from A1 (not in `plugin-api-gotchas.md` — this is about agent delegation, not the API):**
When a spawned agent reports a Figma file-access error, sanity-check with a direct `use_figma` sentinel read before escalating. Agents can misread API quirks (or `"Code executed with no return value"` messages) as auth failures. The A1 thread lost ~30 minutes to this before taking over execution directly.

---

## Pre-flight reads (mandatory before any work)

1. `~/CoworkWorkspace/CLAUDE.md` — global voice rules, session protocol, terminal safety gate
2. `~/CoworkWorkspace/PATH-MAPPINGS.md` — sandbox↔Mac path conversion rule
3. `~/CoworkWorkspace/Get-a-job/CLAUDE.md` — verify before claiming, living documents rule, source verification rule
4. `~/CoworkWorkspace/Get-a-job/SESSION-STATE.md` — current state (session 30 block documents A1)
5. `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/case-subreddit-followups-plan.md` — Scope A2 section has the frame table and approach
6. `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/figma-handoff-case-subreddit.md` — Session 17 addendum has the Workstream B build-protocol learnings (locked mobile pattern, semantic hue palette, gotcha capture)
7. `~/CoworkWorkspace/.claude/skills/figma-to-html/SKILL.md` — primary skill for this scope
8. `~/CoworkWorkspace/.claude/skills/diagram-deploy/SKILL.md` — for embed + deploy
9. `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/workstream-a-deferred-items.md` — two deferred items still available (sub05 Card 4 mini-UIs, sub09 icon glyphs); NOT in A2 scope but can roll in if opportunistic
10. This file — kickoff + A1 carry-forward

---

## Non-negotiables (carry forward from A1 and prior sessions)

- **Dev Mode MCP alt namespace:** `mcp__8e95afc0-e30e-4e27-bfa2-90ccd2e7b3a9__*` (the `mcp__Figma__*` variant errors with "enable Dev Mode MCP Server" — confirmed across Sessions 17/18/24/25/27/28 and A1).
- **No `tidyPage()` on page `29:40`.** Della's desktop clusters at x=914 (Workstream A) and x=80 (Workstream B source) are hand-positioned. APPEND-ONLY — never reposition, rename, reparent, or delete any existing frame. (Gotcha #10 in `html-to-figma/references/plugin-api-gotchas.md`.)
- **Figma is read-only for A2.** This scope produces HTML from Figma. The Figma frames (desktop + mobile) are already built — do not modify them.
- **Two-phase MCP pattern** (gotcha #1): write scripts end with `figma.notify(...)` — NO throw. Read/exfiltration via separate `throw new Error('INFO::' + JSON.stringify(...))` call. "Code executed with no return value" is a red herring — it doesn't mean writes failed.
- **Sanity-check before escalating Figma errors.** If a delegated agent reports a file-access/permissions error, verify with a direct sentinel read before taking the claim at face value. (A1 lesson.)
- **Voice-check is mandatory.** Any Della-voiced prose in each HTML diagram goes through `portfolio-site/voice-check.py` + `voice-rules/banned-patterns.yaml`. No banned patterns, no hedging, no corporate jargon. Match the 12 voice rules in `~/CoworkWorkspace/CLAUDE.md`.
- **Quality-check is mandatory.** Each new HTML runs through `portfolio-site/quality-check.py` — HTML validity, a11y, links, file sizes.
- **6-breakpoint responsive render per new HTML:** Playwright headless Chromium at 1440/1024/768/480/375/320. Zero horizontal overflow, no layout breaks, matches the mobile Figma frame at 375.
- **Mobile Figma is the source of truth for mobile layout.** Della hand-built those 6 mobile frames (see locked pattern in `figma-handoff` Session 17 addendum). Match exactly — do not reflow to what "looks right" in CSS.
- **Tracker writes atomic** via `scripts/tracker-helpers.py`: `th.add_row(path, row_dict)` for new rows, never pandas. Each of the 6 gets a new row with `case_study = 'case-subreddit'`, both `figma_node_id` and `figma_mobile_node_id` populated, `status = 'shipped'` after deploy.
- **No `git add -A`.** File-specific stages only — mixed-workstream branches (case-notifications, case-subreddit A1/A2, Workstream B all coexist).
- **No push without Della's review.** Commit locally, show her the diff, push only when she says so.
- **Commit prefix:** `case-subreddit:` for all Scope A2 commits.
- **All terminal commands use Mac absolute paths** from `~/CoworkWorkspace/PATH-MAPPINGS.md`. Never emit `/sessions/...` paths.

---

## Start here (thread kickoff flow)

1. Read the pre-flight files.
2. Skim the plan doc Scope A2 section: `working/mobile-audit/case-subreddit-followups-plan.md`.
3. Ask Della:
   - Batch size (3 + 3 or all 6)?
   - Commit cadence (per diagram, per batch, or all at end)?
   - Placement on `case-subreddit.html` — are there existing placeholders or does she want to decide placement for each?
4. Per diagram (sequential inside a batch):
   - `get_design_context(fileKey='TArUrZsBUocaAsqetjXq7V', nodeId=<desktop node>)` to pull reference code + screenshot
   - Run `figma-to-html` skill against the desktop node → generates `portfolio-site/img/diagrams/diagram-sub{NN}-<slug>.html`
   - Author responsive CSS: `get_screenshot` on the mobile node, match the locked pattern from Session 17 addendum (eyebrow → H1 → subhead → stylized product preview → 4 glass callouts → footer insight) where applicable
   - Run voice-check + quality-check
   - Render 6 breakpoints via Playwright; confirm no horizontal overflow, no layout breaks
   - Append tracker row via `th.add_row`
   - `diagram-deploy` skill to embed in `case-subreddit.html` (decide placement with Della if she didn't pre-specify)
   - Git commit (file-specific stages, `case-subreddit:` prefix), push per her cadence
5. After all 6 complete: full-page Playwright screenshots of `case-subreddit.html` at 1440 and 375 — confirm no regressions on existing 10 diagrams (sub01/02/03/04/05/06/08/09/11/12), paying attention to the 5 A1-modified frames above.
6. Close out per the close-out steps below.

---

## Key frame tables (quick reference — full details in plan doc + figma-handoff Session 17 addendum)

### Scope A2 — 6 frames to author HTML for (Figma → HTML + deploy)

| # | Diagram ID | Desktop node | Mobile node | Mobile dims | Semantic theme |
|---|---|---|---|---|---|
| 1 | sub07-single-text-input | `315:2` | `1064:26` | 375 × 863 | Input surface pattern |
| 2 | sub10a-disorienting-landing | `326:2` | `1068:26` | 375 × 890 | Before state / problem |
| 3 | sub10b-structured-landing | `327:2` | `1072:26` | 375 × 936 | After state / system |
| 4 | sub11a-surface-adapts-to-stage | `329:2` | `1075:26` | 375 × 981 | Framework / stage-adaptive |
| 5 | sub11b-contextual-depth | `330:2` | `1076:26` | 375 × 904 | Contextual depth pattern |
| 6 | sub12s-text-bars-stall-points-static | `340:2` | `1037:26` | 375 × 509 | Stall points (static version) |

**Figma file:** `TArUrZsBUocaAsqetjXq7V`, page `29:40`. Desktop cluster at `x = 80`, mobile cluster at `x = -1634` (all 6 already paired).

### Locked mobile pattern (from Session 17 addendum — applies to all 6)

- **Structure:** eyebrow → H1 → subhead → stylized product preview → 4 glass callouts → footer insight
- **Glass callout:** fill `textPri` at 0.035 opacity; stroke `textPri` at 0.08 opacity, 1px weight; corner radius 10; padding 14/16/14/16 (T/R/B/L); vertical gap 6px; top accent stripe 2px tall, full width, hue at 0.5 opacity
- **Number row:** JetBrains Mono Bold 9px (numeric token) + Inter Medium 11px (label)
- **Description:** Inter Regular 10px at 0.5 opacity

### Semantic hue palette (cross-frame, from Session 17)

- **red `#C47878`** — before state / problem / legacy flow (use for sub10a, stall point "biggest")
- **warm `#D4A574`** — takeaway / insight / key skip
- **teal `#7FB5B0`** — after state / system / new flow (use for sub10b, sub11b sustained)
- **blue `#8A9EC4`** — interaction / critical / tap-to-reveal (use for sub07 input, sub11a stage-adaptive)

---

## Ship criteria per diagram

A diagram is "shipped" when:

- [ ] HTML file exists at `portfolio-site/img/diagrams/diagram-sub{NN}-<slug>.html`, authored via `figma-to-html`
- [ ] Responsive CSS matches the mobile Figma frame at 375px (verified via `get_screenshot` on the mobile node + Playwright capture of the HTML at 375)
- [ ] `voice-check.py` passes on the file
- [ ] `quality-check.py` passes on the file
- [ ] Playwright render at 1440/1024/768/480/375/320 — no horizontal overflow, no layout breaks
- [ ] Tracker has a new row for this diagram, `status = shipped`, both `figma_node_id` and `figma_mobile_node_id` populated, `verify_date` = today, notes documenting author/verify
- [ ] Embedded in `case-subreddit.html` via `diagram-deploy` (lazy-load iframe pattern)
- [ ] Git commit with file-specific stages (new HTML + updated case-subreddit.html + updated tracker), `case-subreddit:` prefix
- [ ] Pushed to `origin/main`, Vercel deploy succeeds, live at `https://della-portfolio.vercel.app/case-subreddit.html` (verified by fresh fetch)

## Scope-level ship criteria (after all 6)

- [ ] All 6 diagrams meet per-diagram criteria above
- [ ] Full-page Playwright screenshots of `case-subreddit.html` at 1440 and 375 confirm no regressions on existing 10 diagrams — visual diff against pre-A2 baseline
- [ ] `audit-tracker.xlsx` has 6 new rows, all `status = shipped`, both node ID columns populated for each
- [ ] SESSION-STATE.md and BUILD-LOG.md updated
- [ ] Both resume prompts (`resume-prompt-case-subreddit-followups.md` and `resume-prompt-case-subreddit-scope-a2.md`) archived to `working/mobile-audit/archive/`

---

## When you're done (close-out steps)

1. Update `~/CoworkWorkspace/Get-a-job/SESSION-STATE.md` top paragraph — case-subreddit now fully shipped (A1 + A2 complete, Workstream B integrated, 16 diagrams live).
2. Append to `~/CoworkWorkspace/Get-a-job/BUILD-LOG.md` with session entry: decisions, files touched, verification, lessons captured, any new gotchas for `plugin-api-gotchas.md` or `figma-to-html` references.
3. If new gotchas/learnings emerged during figma-to-html work, append them to `~/CoworkWorkspace/.claude/skills/figma-to-html/references/` per the Lessons → Skill References rule in `~/CoworkWorkspace/CLAUDE.md`. Bump skill version per semver. Log the capture in BUILD-LOG.
4. Archive both resume prompts:
   - `working/mobile-audit/resume-prompt-case-subreddit-followups.md` → `working/mobile-audit/archive/`
   - `working/mobile-audit/resume-prompt-case-subreddit-scope-a2.md` → `working/mobile-audit/archive/`
5. Update `working/mobile-audit/workstream-a-deferred-items.md` if any of the two deferred items (sub05 Card 4, sub09 glyph swap) were picked up opportunistically during A2.
