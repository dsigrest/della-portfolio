# Resume Prompt — Case-Subreddit Embed + Figma-Polish Rollup

**Created:** 2026-04-22 (Session 31c close-out — HTML authoring for the 6 Workstream B diagrams complete, commit `c463d70` pushed to `origin/main`, Vercel rebuilt. This is the downstream kickoff — next thread embeds the 6 into `case-subreddit.html`, optionally rolls in Figma polish + deferred Workstream A items.)
**Status:** ACTIVE — ready to launch as a new thread once Della is done polishing Figma (or immediately, if no polish needed).
**Predecessor:** `resume-prompt-case-subreddit-scope-a2.md` (HTML authoring — shipped Session 31c, commit `c463d70`). That file's own predecessor is `resume-prompt-case-subreddit-followups.md` (parent, tracks both A1 and A2).
**Successor:** None (this is the terminal handoff for case-subreddit — retirement after this ships closes the case study's open scopes).
**Retirable when:** 6 Workstream B diagrams embedded in `case-subreddit.html`, full-page Playwright regression clean on existing 10 diagrams at 1440 and 375, commit pushed to `origin/main`, live on `https://della-portfolio.vercel.app/case-subreddit.html`, both predecessor resume prompts archived.
**Outcome so far (Session 31c):** 6 HTML files authored from Figma Workstream B frames — `diagram-sub07-single-text-input.html` (315:2 / 1064:26), `diagram-sub10a-disorienting-landing.html` (326:2 / 1068:26), `diagram-sub10b-structured-landing.html` (327:2 / 1072:26), `diagram-sub11a-surface-adapts-to-stage.html` (329:2 / 1075:26), `diagram-sub11b-contextual-depth.html` (330:2 / 1076:26), `diagram-sub12s-text-bars-stall-points-static.html` (340:2 / 1037:26). All voice-check PASS, quality-check clean 0/0, Playwright 6-breakpoint render clean. 6 tracker rows status=verified, both node IDs populated. Commit `c463d70` on `origin/main`.

---

## TL;DR

6 Workstream B HTML diagrams are live on the website at individual URLs but NOT embedded in `case-subreddit.html` — the case study page itself doesn't display them yet. This thread's job is to (optionally) pull Della's Figma polish back into the HTML, then embed all 6 into `case-subreddit.html` via the `diagram-deploy` skill, run full-page regression at 1440 and 375, commit, push.

Two open placements already exist (SUB-07 → line 192, SUB-10a → line 233 — both are `img-placeholder` divs waiting for the iframe swap). The other four (SUB-10b, SUB-11a, SUB-11b, SUB-12s) need placement decisions with Della inside Section 02 / Activate Growth.

Optional roll-ins if Della is already in Figma-polish mode: the two deferred Workstream A items (sub05 Card 4 mini-UI thumbnails at node `678:700`, sub09 icon glyph swaps at node `678:1056`) can ship in this thread or stay parked.

**Recommended order:** polish check first (figma-to-html Mode A auto-detection takes 2 minutes to confirm no drift), then placement decisions for the 4 unplaced diagrams, then embed + regression + push.

---

## Carry-forward from Session 31c (HTML authoring thread)

**6 files shipped to `portfolio-site/img/diagrams/` — all currently `status=verified` (not yet `status=shipped`, that flips after embed):**

| Diagram | File | Desktop node | Mobile node | Semantic theme |
|---|---|---|---|---|
| sub07-single-text-input | `diagram-sub07-single-text-input.html` | `315:2` | `1064:26` | Before — Creation (red) |
| sub10a-disorienting-landing | `diagram-sub10a-disorienting-landing.html` | `326:2` | `1068:26` | Before — Activation (red) |
| sub10b-structured-landing | `diagram-sub10b-structured-landing.html` | `327:2` | `1072:26` | After — Progressive Disclosure (teal) |
| sub11a-surface-adapts-to-stage | `diagram-sub11a-surface-adapts-to-stage.html` | `329:2` | `1075:26` | System — Progressive Disclosure (teal) |
| sub11b-contextual-depth | `diagram-sub11b-contextual-depth.html` | `330:2` | `1076:26` | Interaction — Tap to Reveal (teal) |
| sub12s-text-bars-stall-points-static | `diagram-sub12s-text-bars-stall-points-static.html` | `340:2` | `1037:26` | Measurement — Static stall points |

**Placement state on `portfolio-site/case-subreddit.html`:**

| Diagram | Current placement | Narrative context |
|---|---|---|
| SUB-07 | `img-placeholder` div line 192 (ready) | Section 01 "Raise the Creation Floor" — before "Quality Floor" h3 |
| SUB-10a | `img-placeholder` div line 233 (ready) | Section 02 "Activate Growth" — before "Progressive Disclosure" h3 |
| SUB-10b | **unplaced** | Likely pairs with 10a under Activate Growth (the "after" state) |
| SUB-11a | **unplaced** | Framework addition near existing sub11 / Progressive Disclosure |
| SUB-11b | **unplaced** | Framework addition near existing sub11 / interaction pattern |
| SUB-12s | **unplaced** | Stall points — companion to existing sub12 heatmap or as its own static beat |

**Tracker state** (`portfolio-site/working/mobile-audit/audit-tracker.xlsx`) — 6 new rows appended in Session 31c:
- All at `status=verified` with `figma_node_id` + `figma_mobile_node_id` populated
- After successful embed, flip each row to `status=shipped` with `verify_date = today` and note the embed via `th.update_row`

**Mid-thread craft fixes locked into the 6 files (don't regress):**
- SUB-07 mobile: `.mock-layout { align-items: stretch }` explicit in `@media (max-width: 768px)` — required because desktop CSS Grid's `align-items: start` carries through and kills cross-axis stretching on the flex children
- SUB-10b mobile stage-row: eyebrow-tag | content-label | eyebrow-tag layout (`STAGE 3 OF 5` mono + `First Content` 12px/500 + `CURRENT` mono, `align-items: baseline`) — don't let this get resized into a title-with-satellites
- SUB-12s insight-card: left-vertical accent stripe matching stall-card stripe pattern (`::before { top:-1; bottom:27; left:-1; width:3 }`), NOT top-horizontal

**Deferred Workstream A items (separate scope, pickupable here if in Figma-polish mode):**

| Item | Figma node | HTML affected | Complexity |
|---|---|---|---|
| sub05 Card 4 mini-UI thumbnail swap | `678:700` | `img/diagrams/diagram-sub05-artifact-alignment.html` | 3 mini-UI SVGs to replace 3 color swatches |
| sub09 icon glyph swaps | `678:1056` | `img/diagrams/diagram-sub09-distribution-loop.html` | 3 inline SVG path swaps (megaphone→play, heart→infinity, shield-check→checkbox) |

Source of truth for these: `working/mobile-audit/workstream-a-deferred-items.md`. Roll in only if Della's in Figma-polish mode and explicitly says so.

---

## Pre-flight reads (mandatory before any work)

1. `~/CoworkWorkspace/CLAUDE.md` — global voice rules, session protocol, terminal safety gate
2. `~/CoworkWorkspace/PATH-MAPPINGS.md` — sandbox↔Mac path conversion rule
3. `~/CoworkWorkspace/Get-a-job/CLAUDE.md` — verify-before-claiming, living documents rule, source verification rule
4. `~/CoworkWorkspace/Get-a-job/SESSION-STATE.md` — Session 31c block at top documents A2 authoring close-out
5. `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/case-subreddit-followups-plan.md` — original Scope A1 + A2 plan doc (still accurate for context)
6. `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/figma-handoff-case-subreddit.md` — Session 17 Workstream B addendum with frame origins + locked mobile pattern
7. `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/workstream-a-deferred-items.md` — deferred items (sub05 + sub09) parked here
8. `~/CoworkWorkspace/Skills/figma-to-html/SKILL.md` — Mode A auto-detection for the polish-check step
9. `~/CoworkWorkspace/Skills/diagram-deploy/SKILL.md` — primary skill for this scope (embed step)
10. This file — for kickoff

---

## Non-negotiables (carry forward + new)

**Carried forward from Scope A2 and prior sessions:**
- **Dev Mode MCP alt namespace:** `mcp__8e95afc0-e30e-4e27-bfa2-90ccd2e7b3a9__*`. The `mcp__Figma__*` variant errors with "enable Dev Mode MCP Server" — confirmed across Sessions 17/18/24/25/27/28/30/31c.
- **Two-phase MCP pattern** (gotcha #1): write scripts end with `figma.notify(...)`, NO throw. Read/exfiltration via separate `throw new Error('INFO::...')` call.
- **figma-source meta tag preservation** on any HTML update — the 6 files already have stamps (`node:NNN:N page:29:40 file:TArUrZsBUocaAsqetjXq7V`). Don't drop them during figma-to-html re-translation.
- **Voice-check + quality-check mandatory** on any HTML touched (run from `portfolio-site/`): `python3 voice-check.py <file>` + `python3 quality-check.py <file>`. Zero errors required; UI-mock-copy long-sentence WARNs acceptable per prior convention.
- **6-breakpoint Playwright render** on any HTML touched: 1440/1024/768/480/375/320, zero horizontal overflow required. Render script at `/sessions/<sandbox>/scratch/a2/render.py` from the predecessor thread — sandbox-local, reinstall Playwright + Chromium at thread start (`pip install playwright --break-system-packages && python3 -m playwright install chromium`).
- **Tracker writes atomic** via `scripts/tracker-helpers.py`: `th.update_row(path, diagram_id, updates)` by `diagram_id` string. Never pandas.
- **No `git add -A`.** File-specific stages only — mixed-workstream branches (case-notifications + case-subreddit + Workstream B all coexist).
- **No push without Della's review.** Commit locally, show her the diff, push only when she says so.
- **All terminal commands use Mac absolute paths** from `~/CoworkWorkspace/PATH-MAPPINGS.md`. Never emit `/sessions/...` paths.
- **Commit prefix:** `case-subreddit:` for all commits in this scope.

**New for this thread:**
- **Never delete or move the existing 10 diagrams.** The embed ADDS 6 iframes to `case-subreddit.html`, doesn't replace anything.
- **Full-page Playwright regression at 1440 and 375 before declaring done.** Capture before-embed baseline first, then post-embed. Visual diff against the existing 10 diagrams — any layout shifts on `sub01/02/03/04/05/06/08/09/11/12` are regressions, not features.
- **Lazy-load iframe pattern required.** Match the existing 10 embeds' format in `case-subreddit.html` (see lines 89-221 for template). `loading="lazy"`, `scrolling="no"`, `title="..."`, inline `style` with width/height/border-radius.
- **Living Documents rule on `case-subreddit.html`** — do NOT regenerate the whole file. Make targeted edits: replace the 2 existing `img-placeholder` divs (lines 192, 233), insert 4 new `.diagram-embed` sections at Della-approved placement points.

---

## Start here (thread kickoff flow)

1. **Read pre-flight files** (10 items above).
2. **Confirm polish state with Della.** Ask: "Did you polish any of the 6 Workstream B Figma frames since Session 31c (commit `c463d70`)?" — if yes, run `figma-to-html` skill in Mode A against page `29:40` and file `TArUrZsBUocaAsqetjXq7V` to auto-detect and re-translate drifted frames. If no polish, skip this step.
3. **If Figma-polished:** for each drifted HTML, re-run voice-check + quality-check + 6-breakpoint Playwright render. Update tracker row notes with polish-sync details.
4. **Ask Della: pick up deferred Workstream A items in this thread?** Options:
   - Yes — roll in sub05 Card 4 mini-UIs (node `678:700`) + sub09 icon glyphs (node `678:1056`) per `workstream-a-deferred-items.md`
   - No — leave parked for a focused Figma-polish thread later
5. **Placement decisions for SUB-10b, SUB-11a, SUB-11b, SUB-12s.** Ask Della one at a time or all at once:
   - Propose: SUB-10b next to SUB-10a under Activate Growth (before "Progressive Disclosure" h3), SUB-11a and SUB-11b as a pair either before or after the existing sub11 text-bars, SUB-12s before or after the existing sub12 instrumentation-interactive
   - Wait for approval — don't place blind
6. **Capture pre-embed full-page baselines** via Playwright: `case-subreddit.html` at 1440 and 375. Save to `/sessions/<sandbox>/scratch/embed/baseline/`.
7. **Run `diagram-deploy` skill** per placement decisions. Replace 2 existing `img-placeholder` divs + insert 4 new `.diagram-embed` sections at approved locations.
8. **Post-embed verification:**
   - Re-run voice-check + quality-check on `case-subreddit.html`
   - Re-capture full-page Playwright at 1440 and 375
   - Visual diff against baseline — zero layout shifts on existing 10 diagrams
   - Confirm 6 new iframes load correctly via Playwright (iframe content heights, no broken asset references)
9. **Tracker update:** flip 6 rows from `status=verified` to `status=shipped`, set `verify_date=today`, append embed note.
10. **Commit + push** per Della's cadence call (per-diagram, per-batch, or single). Commit prefix `case-subreddit:`. Show diff before push.
11. **Verify live** on `https://della-portfolio.vercel.app/case-subreddit.html` after Vercel rebuild — hard-refresh, scroll through all 16 diagrams (10 existing + 6 new), confirm embed behavior matches local.
12. **Close out** per the steps below.

---

## Key reference tables

### Existing placeholders in `case-subreddit.html` (ready for swap)

| Line | Current content | Replace with |
|---|---|---|
| 192 | `<div class="img-placeholder">Before — legacy creation flow, single text input with no guidance or preview</div>` | `.diagram-embed` iframe pointing at `img/diagrams/diagram-sub07-single-text-input.html` |
| 233 | `<div class="img-placeholder">Before — chaotic community landing page with card carousel and off-platform links</div>` | `.diagram-embed` iframe pointing at `img/diagrams/diagram-sub10a-disorienting-landing.html` |

### Embed template (match existing pattern)

```html
<div class="case-img-full diagram-embed" data-diagram="sub-NN">
  <iframe
    src="img/diagrams/diagram-subNN-slug.html"
    loading="lazy"
    scrolling="no"
    title="[descriptive title matching the diagram's narrative role]"
    style="width: 100%; height: 600px; border: none; border-radius: 12px; overflow: hidden;"
  ></iframe>
</div>
```

Height varies per diagram's intrinsic height — measure post-render and tune. For taller diagrams (sub11a at 981px mobile, sub10b at 936px mobile) consider `height: 700px` or `800px`. For shorter (sub12s at 509px mobile) consider `height: 520px` or less.

### Figma file anchor
- File key: `TArUrZsBUocaAsqetjXq7V`
- Page: `29:40` (case-subreddit)
- Desktop cluster x: `80` (Workstream B source)
- Polish cluster x: `914` (Workstream A polish column)
- Mobile cluster x: `-1634`

### HTML file locations (Mac absolute)
- 6 Workstream B HTMLs: `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/img/diagrams/diagram-sub{07,10a,10b,11a,11b,12s}*.html`
- Embed target: `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/case-subreddit.html`
- Tracker: `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/audit-tracker.xlsx`
- Tracker helpers: `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/scripts/tracker-helpers.py`
- Voice linter: `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/voice-check.py`
- Quality linter: `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/quality-check.py`

### Checkpoint commit
- `c463d70 case-subreddit: Scope A2 Workstream B — 6 new HTML diagrams authored` on `origin/main`
- Prior relevant commit: `f57865f case-subreddit: Workstream A x=914 Figma polish (9 diagrams)` (Session 28)

---

## Ship criteria

### Per-diagram (each of the 6)
- [ ] If Figma-polished: HTML re-translated via figma-to-html Mode A, figma-source meta updated, voice-check + quality-check clean, 6-breakpoint render clean
- [ ] Embedded in `case-subreddit.html` with lazy-load iframe matching existing template
- [ ] Iframe height tuned so content fits without scroll at 1440 viewport
- [ ] Tracker row flipped to `status=shipped`, `verify_date=today`, notes appended documenting embed
- [ ] Diagram visible and interactive on `https://della-portfolio.vercel.app/case-subreddit.html` after Vercel rebuild

### Scope-level (after all 6 embedded)
- [ ] Full-page Playwright screenshots at 1440 and 375 captured post-embed
- [ ] Visual diff against pre-embed baseline shows ZERO layout shifts on the existing 10 diagrams (sub01/02/03/04/05/06/08/09/11/12)
- [ ] `voice-check.py` + `quality-check.py` PASS on `case-subreddit.html`
- [ ] Commit pushed to `origin/main` with `case-subreddit:` prefix
- [ ] Vercel build green; live at `https://della-portfolio.vercel.app/case-subreddit.html`
- [ ] Della hard-refreshes + scrolls + confirms 16 diagrams render correctly on desktop and phone
- [ ] `audit-tracker.xlsx` has all 6 Workstream B rows at `status=shipped`
- [ ] This resume prompt AND both predecessors (`resume-prompt-case-subreddit-scope-a2.md`, `resume-prompt-case-subreddit-followups.md`) moved to `working/mobile-audit/archive/`

### If deferred Workstream A items rolled in
- [ ] sub05 Card 4 mini-UI thumbnails shipped — HTML + tracker note + `workstream-a-deferred-items.md` updated
- [ ] sub09 icon glyph swaps shipped — HTML + tracker note + `workstream-a-deferred-items.md` updated

---

## Close-out steps (when this thread ships)

1. Update `~/CoworkWorkspace/Get-a-job/SESSION-STATE.md` top paragraph — case-subreddit fully closed (all 16 diagrams live + embedded + regression clean).
2. Append to `~/CoworkWorkspace/Get-a-job/BUILD-LOG.md` session entry: decisions, files touched, verification, any lessons captured.
3. If new gotchas emerged during figma-to-html or diagram-deploy work, append them to `~/CoworkWorkspace/Skills/figma-to-html/references/` or `~/CoworkWorkspace/Skills/diagram-deploy/references/` per the Lessons → Skill References rule in global CLAUDE.md. Bump skill version per semver. Log the capture in BUILD-LOG.
4. Archive all three resume prompts in the chain to `working/mobile-audit/archive/`:
   - This file: `resume-prompt-case-subreddit-embed-and-polish.md`
   - `resume-prompt-case-subreddit-scope-a2.md`
   - `resume-prompt-case-subreddit-followups.md`
5. Update `working/mobile-audit/workstream-a-deferred-items.md` — if sub05 and sub09 closed this thread, mark them shipped; if still open, carry forward for a future focused thread.
6. Update `case-subreddit-followups-plan.md` Status header to COMPLETE (or archive the plan doc alongside the resume prompts — plan doc's job is done once A2 embed ships).
