# Resume Prompt — case-subreddit Responsive Audit Fix Phase

**Paused:** 2026-04-21 end of Session 4 (CSS fix phase midway).
**Picks up:** Fresh Cowork thread, fix phase for sub02–sub12.
**Hands off to:** Separate thread running `figma-to-html` / HTML-to-Figma skill once all 10 CSS fixes land (Della is batching Figma pairing externally).

---

## Copy-paste this block into a fresh Cowork thread

```
Run the responsive-audit skill on case-subreddit — fix phase, resuming from Session 4. Screenshots pre-captured at `portfolio-site/working/mobile-audit/screenshots/{1440,1024,768,480,375,320}/case-subreddit/`. Do NOT install Playwright or run screenshot-diagrams.py — the sandbox runs out of disk. Read the existing PNGs directly for pre-fix diagnosis. We are SKIPPING post-fix screenshots per Session 4 decision — verify via code walk (re-read edited file, confirm selectors match real HTML classes, walk scale math) instead.

Skill: `~/CoworkWorkspace/Skills/responsive-audit/` v0.2.1. Read `SKILL.md`, `references/severity-classification.md`, `references/common-l2-failure-patterns.md`, `references/agent-prompts.md` Prompt 3. Figma pairing is DEFERRED to a separate thread — do NOT run `render-mobile-to-figma.py`, do NOT touch Figma in this thread. Tracker: `portfolio-site/working/mobile-audit/audit-tracker.xlsx` — update via `scripts/tracker-helpers.py` openpyxl only.

State: sub01 is CSS-fixed + visually verified (status=fixed). sub02–sub12 (9 diagrams) are status=audited with root_cause + fix_strategy pre-filled. All are L2. All fixes live inside each diagram's own `<style>` block — no new files, no `styles.css` edits, no HTML structural changes.

Per-diagram workflow: read tracker row → read existing pre-fix PNG at 375 (and 320 for heatmap/chart diagrams) to confirm pattern → propose the CSS edit in chat → wait for Della's greenlight → apply → re-read the edited file and code-verify (selectors exist, math checks out) → atomic tracker update (status=fixed, verify_date=today, notes="css_fix_verified_via_code_walk; figma_pairing_deferred_to_other_thread") → move to next. Show diff between each diagram before moving on. Main thread only — no delegation.

When all 9 remaining fixes are in, run `screenshot-diagrams.py case-subreddit` on Della's Mac as a safety-net pass across all breakpoints, look at the PNGs for anything unexpected, then write the Figma handoff doc at `working/mobile-audit/figma-handoff-case-subreddit.md` (schema below) and update SESSION-STATE.md.

Start with sub02. Show the proposed CSS edit before touching the file.
```

---

## State of truth (fresh thread must trust this)

### Tracker rows (already seeded)

`portfolio-site/working/mobile-audit/audit-tracker.xlsx` has 10 case-subreddit rows:

| diagram_id | status | severity | verify_date | notes |
|---|---|---|---|---|
| sub01-survival-curve | **fixed** | 2 | 2026-04-21 | css_fix_verified_via_visual_inspection_320_375_1440; figma_pairing_deferred_to_other_thread |
| sub02-lifecycle-framework | audited | 2 | — | awaiting_css_fix_phase_resume |
| sub03-milestone-model | audited | 2 | — | awaiting_css_fix_phase_resume |
| sub04-strategic-starting-points | audited | 2 | — | awaiting_css_fix_phase_resume |
| sub05-artifact-alignment | audited | 2 | — | awaiting_css_fix_phase_resume |
| sub06-threshold-calibration | audited | 2 | — | awaiting_css_fix_phase_resume |
| sub08-creation-after | audited | 2 | — | awaiting_css_fix_phase_resume |
| sub09-distribution-loop | audited | 2 | — | awaiting_css_fix_phase_resume |
| sub11-text-bars | audited | 2 | — | awaiting_css_fix_phase_resume |
| sub12-instrumentation-interactive | audited | 2 | — | awaiting_css_fix_phase_resume |

`root_cause` and `fix_strategy` are populated in the tracker — read those columns for the per-diagram plan.

### Audit table (Della's pre-computed, mirrored here for redundancy)

| ID | Root cause | Fix |
|---|---|---|
| sub01 | Pattern B — fixed-height container around xMidYMid-meet SVG; SVG text 9-10 in 660-unit viewBox unreadable at narrow widths | **DONE** — aspect-ratio 660/200; SVG text font-size 14px @480, 16px @320 |
| sub02 | Pattern C — 5-stage horizontal row doesn't collapse; cards clip right edge at mobile | Collapse stage row to vertical stack at @768; tighten card padding |
| sub03 | Pattern D — flex card with fixed-width (50px) `.impact-section` crushes title at 375 | Stack `.stage-card` contents vertically at @480; move impact row below tags |
| sub04 | Pattern C — 2-col `.bets-grid` doesn't collapse; right card clips | Collapse `.bets-grid` to 1 col at @768 |
| sub05 | Pattern C — 2×2 grid of 4 cards doesn't collapse; right column clips | Collapse grid to 1 col at @768 |
| sub06 | Pattern B — chart area fixed height; survival curve + column bars + stage tiles. Bottom stage grid reflows fine (3+2). Chart + legend crowd | aspect-ratio on chart box; stack chart header legend; keep stage card grid as-is |
| sub08 | Minor — 3-step flow header (Identity → Visual → Preview) wraps to 2 rows at 375/320, orphan arrows; cards below stack fine | Hide arrows below 480 OR stack header items vertically without arrows |
| sub09 | Pattern C — 3-card flex row (Share/Engage/Trust) doesn't stack; connector curve breaks harmlessly once cards stack | Collapse `.loop-nodes` to 1 col at @768; hide curved SVG arrows at mobile |
| sub11 | Pattern C — 3-card grid (Priority Order / Visible Progress / Direct Navigation) doesn't stack; right card clips | Collapse grid to 1 col at @768 |
| sub12 | Works at 480, clips at 320 only — 6-col heatmap needs tighter cell padding/font at 320 | Tighten cell padding + font at @375/320; legend ("ADOPTION … Stall point") collapse to stack |

### Capture artifact to ignore

sub03's full-page screenshot at 375/480 shows cards 4-5 invisible. This is Playwright not triggering the `.reveal` IntersectionObserver on last-in-DOM cards — capture-time only, not a real mobile bug. Fix proceeds normally.

### Workflow decisions made in Session 4

1. **Skip post-fix screenshots per diagram** (sub02–sub12). Code-verify only: re-read edited file, audit selectors against real HTML classes, walk the scale math. Della's call — sub01's visual pass confirmed the pattern-based fixes are reliable on her codebase.
2. **Figma pairing deferred** to a separate thread running HTML-to-Figma. Do NOT run `render-mobile-to-figma.py` in this thread. Do NOT create Figma frames. Just update tracker with `status=fixed`, `figma_mobile_node_id` empty.
3. **One safety-net screenshot pass at the end** — Della runs `cd /Users/della/CoworkWorkspace/Get-a-job/portfolio-site && python3 working/mobile-audit/scripts/screenshot-diagrams.py case-subreddit` after all 10 fixes. Regression check only.

### Figma pairing target (for the FUTURE Figma thread — not this one)

- File: `TArUrZsBUocaAsqetjXq7V`
- Page: `29:40` ("4. Subreddit success")
- Page state: 59 children — 10 SUB-XX desktop base frames + 11 SUB-XXa variants + 18 spec frames (at x=-334) + stickies. NOT empty (previous prompts said childCount:0 — that was stale).
- Mobile cluster anchor: `x = -1634` (first-run computed via v0.2.1 algorithm: `min(leftmost_child.x) − 1300 = −334 − 1300 = −1634`)
- Frame naming: `sub01-mobile` … `sub12-mobile`
- Frame dims: 375w × natural-height-at-375
- Per-diagram Y: each mobile frame's Y = corresponding desktop base frame's Y (pull via Figma MCP at handoff-write time)

---

## Non-negotiables for the fresh thread

- **Skill Execution Rule:** read the actual skill files (`SKILL.md`, `severity-classification.md`, `common-l2-failure-patterns.md`, `agent-prompts.md` Prompt 3) — don't paraphrase.
- **Verify-Before-Claiming (code-verify variant):** after each edit, re-read the changed section of the file. Confirm new selectors resolve against real classes in the diagram's body (Pattern A guard). Walk the math where relevant (aspect-ratio, scale, font-size in rendered screen pixels).
- **Living Documents Rule:** tracker updates use `tracker-helpers.py` openpyxl (`upsert_row` / `update_row`). Never pandas.
- **Main thread only.** No sub-agent delegation. Session 1–3 drift failures justify this.
- **Scope discipline:** no `styles.css` edits, no `case-subreddit.html` edits, no new files. L2 = inside the diagram's `<style>` block.
- **Per-diagram gate:** show the proposed CSS edit in chat BEFORE touching the file. Show the diff AFTER applying, before moving to the next.

---

## Handoff to the Figma thread (after all 10 CSS fixes land)

Write `portfolio-site/working/mobile-audit/figma-handoff-case-subreddit.md` with:

1. **Status roster** — 10 rows mirroring tracker state, with file paths
2. **Target** — file ID, page ID, mobile cluster anchor x=-1634
3. **Per-diagram** — HTML path, mobile frame name, desktop base frame Y (enumerate via Figma MCP: list children of page 29:40, match by name starting with `SUB-01`…`SUB-12`, read each `.y`)
4. **Scripts** — primary `render-mobile-to-figma.py`, fallback `populate-figma-frames-prep.py` + `populate-figma-frames.js`
5. **Non-negotiables for Figma thread** — read figma-pairing-convention.md v0.2.1, openpyxl tracker writes, never tidyPage the case-study page, never edit desktop cluster
6. **Close-the-loop instruction** — Figma thread writes `figma_mobile_node_id` back into tracker

Then update SESSION-STATE.md: "case-subreddit CSS fixes complete (10/10); Figma pairing deferred to fresh thread via figma-handoff-case-subreddit.md."

---

## Version

- 2026-04-21 — initial. Session 4 paused at 1/10 CSS fixes. Sub01 done, sub02–sub12 pending.
