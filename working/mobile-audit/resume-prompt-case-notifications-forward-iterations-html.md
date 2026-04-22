# Resume prompt — case-notifications forward iterations → HTML (fresh thread)

Paste this as the first message in a new Cowork thread. The thread's scope is **HTML only** — translate forward-iteration Figma frames on page "1. Notifs & Inbox" into production HTML, wire into `case-notifications.html`, verify visually, and stage for deploy. Mobile pairing is a separate thread (a resume prompt for it gets drafted in Phase 4).

**Target Figma file:** `TArUrZsBUocaAsqetjXq7V` (Portfolio — Image Inventory)
**Target page:** `29:43` ("1. Notifs & Inbox")
**Website page:** `portfolio-site/case-notifications.html`
**Primary skill:** `figma-to-html`
**Supporting skills:** `codesign` (visual quality passes), `diagram-deploy` (final Phase 3 step)

---

## Why this thread exists

Case-notifications has 13 diagrams currently paired in Figma and live on the portfolio site (see `working/mobile-audit/reports/figma-handoff-case-notifications.md` — all 13 are at `x = -1700` mobile cluster + their desktop counterparts). Della has additional diagrams on page `29:43` that are either:
- **NEW** — in Figma but not yet translated to HTML or embedded in the site.
- **FORWARD ITERATIONS** — already tracked, but Della pushed newer versions in Figma (canonical = rightmost x on the canvas). The live HTML is stale relative to Figma.

Job: bring the HTML into sync with the rightmost Figma frames, one diagram at a time, with verification at every step. No mobile work in this thread.

---

## Pre-flight reads (do these in order, THEN STOP)

1. `~/CoworkWorkspace/CLAUDE.md` + `~/CoworkWorkspace/PATH-MAPPINGS.md` — global config + the path conversion rule (Mac-absolute paths for anything shown to Della).
2. `~/CoworkWorkspace/Get-a-job/CLAUDE.md` — project-specific rules (Verify Before Claiming, Living Documents, Source Verification).
3. `~/CoworkWorkspace/Get-a-job/SESSION-STATE.md` — read the top "As of" block and the "Mobile audit — case-notifications" section for current state.
4. `~/CoworkWorkspace/Skills/figma-to-html/SKILL.md` — canonical process. Read in full.
5. `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/reports/figma-handoff-case-notifications.md` — the 13 currently-tracked diagrams + conventions enforced. Anything NOT in this brief is a candidate for this thread.
6. `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/audit-tracker.xlsx` — tracker schema and current case-notifications rows.

**After pre-flight, post a short confirmation:** files loaded, count of diagrams currently tracked, your understanding of the scope (HTML only, no mobile). Do NOT start discovery until Della confirms. This gate catches context-load errors before any Figma scanning.

---

## Phase 1 — Discovery (scan Figma page, produce candidate list, await greenlight)

**Rightmost-wins rule:** On Figma page `29:43`, for any given diagram concept, Della treats the rightmost frame on the canvas (max `x`) as the canonical/latest version. Older iterations stay on the canvas for history but are not canonical.

Pipeline:
1. `get_metadata` on page `29:43`. Expect output to exceed token limit — save to tool-results and parse with Python regex (pattern documented in BUILD-LOG Session 12).
2. From the parsed frames, filter out:
   - Utility frames (animation-spec columns, note text blocks)
   - Mobile cluster frames (anything at `x = -1700`)
   - The 3 preserved mobile frames referenced in the handoff brief
3. Group remaining frames by diagram concept using name patterns (`not##`, `not-e##`, or descriptive labels). For each group, pick the frame with max `x` as canonical.
4. Cross-reference each canonical frame against the 13 entries in the handoff brief:
   - Already tracked AND node ID matches → `IN_SYNC` (skip)
   - Already tracked BUT canonical node differs → `FORWARD_ITERATION`
   - Not tracked → `NEW`
5. For every `NEW` or `FORWARD_ITERATION` candidate, check `portfolio-site/img/diagrams/` for existing HTML (match by diagram ID). Record whether HTML exists and its current version.

**Deliverable: a single markdown table posted in the thread.** Columns:

| diagram_id | canonical_figma_node | status | existing_html | action |
|---|---|---|---|---|

Status is `NEW`, `FORWARD_ITERATION`, or `IN_SYNC` (shown for completeness but will be skipped). Action is `create new HTML`, `update existing HTML`, or `skip`.

**STOP.** Wait for Della to:
- Confirm or strike rows
- Rename diagrams if needed
- Provide content/copy guidance for `NEW` diagrams that don't have a clear textual source
- Tell you where each new embed should go in `case-notifications.html` (which section, between which existing diagrams)

**Do not proceed to Phase 2 without an approved list + placement plan.**

---

## Phase 2 — Per-diagram pipeline (one at a time, checkpoint between)

For each greenlit diagram, run this pipeline **strictly in order**. Do not batch — one diagram fully through before the next starts. This keeps context flat and makes interruption/resume painless.

### 2a. Fetch canonical Figma frame
- `get_metadata` on the specific node ID (target the node, not the whole page — smaller payload).
- `get_screenshot` of the canonical frame. Save to `working/mobile-audit/figma-refs/<diagram-id>-canonical.png` for side-by-side later.

### 2b. Translate or update HTML

**If `NEW`:** Follow `figma-to-html` skill Step-by-Step Process in full. Generate `diagram-<id>-v1.html` in `portfolio-site/img/diagrams/`. Apply the conventions from the case-notifications handoff brief:
- Container width: 760px
- Canvas fill: `#0A0C16`
- Corner radius: 16px, `overflow: hidden`
- Design tokens: `#7FB5B0` (accent), `#C4B078` (gold), `#D4A574` (warm), `#C47878` (red), `#8A9EC4` (blue)
- Fonts: Inter (400/500/600/700) + JetBrains Mono (400/700)
- Embed-mode script at the bottom: `<script>if(window!==window.parent)document.body.classList.add('embedded');</script>`

**If `FORWARD_ITERATION`:** Read the existing HTML, diff against canonical Figma. Make surgical edits (prefer `Edit` over `Write`). Version bump rule:
- Cosmetic/content-only edits → edit in place, no version bump
- Structural changes (layout, new sub-components, changed data) → bump `-vN.html` → `-v(N+1).html`, move prior version to `working/older-versions/`, update the iframe src in `case-notifications.html`

### 2c. Verify HTML visually

Open the diagram HTML in a local render (browser or headless screenshot). Compare the 1440px render to the canonical Figma screenshot side-by-side in the thread. Call out any deltas and either fix or explicitly flag for Della.

Run `python3 portfolio-site/quality-check.py <path-to-diagram-html>`. If it fails, fix. If it passes, note it in the response.

### 2d. Wire into case-notifications.html

- **If an `img-placeholder` slot already exists** for this diagram, leave the HTML file alone and flag that `diagram-deploy` will wire it in Phase 3.
- **If no slot exists** (i.e., this is a genuinely NEW embed), use the Phase 1 placement plan Della approved. Add an `<iframe>` in the indicated section. Preserve the exact iframe attributes used by other diagrams in the same file (check one as a reference before editing).
- Living Documents Rule applies: additive edits to `case-notifications.html`, never a rewrite.

### 2e. Update tracker + checkpoint

- Via openpyxl (never pandas), add or update the row for this diagram in `audit-tracker.xlsx`:
  - `diagram_id`, `case_study=notifications`, `file_path` (desktop HTML), `figma_node_id` (canonical), `status=html-new` or `html-updated`
  - Preserve prior notes with `|` separator; append `\n<today>: <short action>`
- Append a one-line entry to `BUILD-LOG.md` under the active session block (do not create a new session block per diagram — all of Phase 2 shares one session).
- Post a compact summary to the thread: `<diagram_id> done: <what changed>, quality-check <pass/fail>, node <figma_id>, version <html file>`.

### Context hygiene (enforce these, not optional)

- **`get_metadata` overflow:** If it returns >200k chars, save to tool-results and parse with Python regex. Pattern from BUILD-LOG Session 12: `r'<frame id=\"([^\"]+?)\" name=\"([^\"]*?)\"[^>]*?x=\"(-?[0-9.]+)\" y=\"(-?[0-9.]+)\" width=\"([0-9.]+)\" height=\"([0-9.]+)\"'`
- **Spawn sub-agents** for the HTML generation step of any `NEW` diagram (brief them with the exact Figma node, the design tokens, and the skill path — they should read the skill themselves).
- **After every 3 diagrams**, post a compact progress summary and ask Della if she wants to continue or pause.
- **Soft budget: 6 diagrams per thread.** If the approved list is >6, stop after 6 and write a continuation prompt. If context feels heavy before 6 (>60% window), write `working/mobile-audit/CONTEXT-CHECKPOINT-<date>.md` with exact state and exit cleanly.

---

## Phase 3 — Deploy (after all Phase 2 diagrams complete)

1. Run `python3 portfolio-site/voice-check.py portfolio-site/case-notifications.html` (in case iframe additions touched copy).
2. Run `python3 portfolio-site/quality-check.py portfolio-site/case-notifications.html`.
3. Invoke the `diagram-deploy` skill to replace any remaining `img-placeholder` divs with iframe embeds for diagrams built this thread.
4. Show Della the unified diff for every changed file. No exceptions, no summaries in place of diffs.
5. Give Della the Mac-absolute git commands to commit + push (use paths from `PATH-MAPPINGS.md`). Do NOT run git from the sandbox.

Example shape of the commands (Della runs these on her Mac):

```bash
cd ~/CoworkWorkspace/Get-a-job/portfolio-site
git add img/diagrams/diagram-not##-<name>.html
git add case-notifications.html
git add working/mobile-audit/audit-tracker.xlsx
git commit -m "case-notifications: <N> forward-iteration HTML updates"
git push origin main
```

---

## Phase 4 — Handoff + close

### 4a. Handoff brief for the mobile-pair thread
Write `portfolio-site/working/mobile-audit/reports/figma-handoff-case-notifications-forward-iterations.md` with:
- Date, Figma file key, page ID
- Table of diagrams built/updated this thread: `diagram_id | desktop_html_path | canonical_figma_node | status`
- Open follow-ups (if any)
- Explicit note: "Mobile pairing not done in this thread. Next: run `html-to-figma` + `responsive-audit` per the Session 12 pattern to produce mobile Figma frames at `x = -1700`."

### 4b. Mobile-pair resume prompt
At the end of this thread, draft a new resume prompt at `portfolio-site/working/mobile-audit/resume-prompt-case-notifications-forward-iterations-mobile.md`. Template from `resume-prompt-case-building-portfolio-figma-to-html.md` inverted direction (HTML → mobile Figma native layers). Scope: only the diagrams built/updated in this thread. Cluster anchor: `x = -1700`. Follow Session 12 native-build patterns (documented in BUILD-LOG Session 12 and in this handoff brief).

### 4c. SESSION-STATE + BUILD-LOG
- Prepend a new "As of" block to `SESSION-STATE.md` documenting this session. Demote the prior "As of" to "Prior session."
- Update the "Mobile audit — case-notifications" section with a subsection covering the new/updated diagrams.
- Append a full session entry to `BUILD-LOG.md` (TOC entry + detailed log entry) following the Session 12 entry format.

---

## Non-negotiables

From `Get-a-job/CLAUDE.md`:
- **Verify Before Claiming.** Every HTML update = render it, take a screenshot, compare to Figma. "Matches the design" without a visible comparison = not done.
- **Source Verification.** Any new text/numbers in diagrams must trace to `working/planning-docs/verified-facts-registry.md` or to content Della already shipped in case-notifications. If neither, flag with `<!-- DELLA: verify -->` and ask.
- **Living Documents Rule.** `case-notifications.html` is a living doc. Additive edits only. Never regenerate from scratch. Never delegate a rewrite to an agent.
- **Voice Rules.** If this work touches case-study copy (not just diagrams), run the self-check protocol and show Della anything caught before revising.
- **Mac-absolute paths in commands.** Use `PATH-MAPPINGS.md` for every terminal command shown to Della. Never show `/sessions/...` paths.
- **No git from the sandbox.** Commands only; Della runs them.

---

## Quick reference

| Artifact | Path |
|---|---|
| Figma file key | `TArUrZsBUocaAsqetjXq7V` |
| Figma page | `29:43` ("1. Notifs & Inbox") |
| Desktop HTML folder | `portfolio-site/img/diagrams/` |
| Case study page | `portfolio-site/case-notifications.html` |
| Tracker | `portfolio-site/working/mobile-audit/audit-tracker.xlsx` |
| Session 12 handoff brief | `portfolio-site/working/mobile-audit/reports/figma-handoff-case-notifications.md` |
| figma-to-html skill | `~/CoworkWorkspace/Skills/figma-to-html/SKILL.md` |
| Mobile cluster x (for next thread) | `-1700` |
| Mac-absolute paths | See `~/CoworkWorkspace/PATH-MAPPINGS.md` |

---

## Stop conditions (exit cleanly on any of these)

- Della doesn't greenlight the Phase 1 candidate list → stop, don't touch HTML.
- Any Phase 2 diagram fails `quality-check.py` after 2 fix attempts → stop that diagram, move on, flag for Della.
- Context window exceeds 60% before Phase 2 completes → write CONTEXT-CHECKPOINT and exit.
- Figma page scan returns zero `NEW`/`FORWARD_ITERATION` candidates → post the table showing everything `IN_SYNC`, tell Della no work needed, exit.
