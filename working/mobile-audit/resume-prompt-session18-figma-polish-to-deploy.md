# Resume Prompt — Session 18: Figma Polish → HTML Sync → Deploy

**Created:** 2026-04-22 (end of Session 17 — portfolio ship-complete)
**For:** Next session, after Della polishes the case-building-portfolio mobile Figma frames
**Entry state:** 4 mobile diagrams shipped to live site (commit `53694c2`). 5th diagram (port-04b-governance) escalated L3 and pending redesign. Figma mobile frames exist for all 6 diagrams but haven't been polished yet.

---

## Session Goal

Close the Figma→HTML→deploy loop for the case-building-portfolio mobile diagrams after Della finishes polishing them in Figma. Specifically:

1. Pull Figma polish back into HTML (figma-to-html skill)
2. Re-deploy updated HTMLs to `portfolio-site/img/diagrams/` (diagram-deploy skill)
3. Verify embeds render correctly in `case-building-portfolio.html` on desktop + mobile
4. Commit + push
5. Flip tracker rows from `shipped` to `shipped-polished` (or equivalent) and stamp verify dates

This is the back half of the Figma↔HTML roundtrip. Session 17 handled HTML→Figma + first deploy. Session 18 handles Figma→HTML + polish deploy.

---

## Pre-flight

1. Read `CoworkWorkspace/CLAUDE.md` and `Get-a-job/CLAUDE.md` (auto)
2. Read `PATH-MAPPINGS.md` before any terminal command
3. Read this file
4. Read `working/mobile-audit/reports/session17-ship-complete.md` for full context on what shipped
5. Read the `figma-to-html` skill — Della's polish cycle depends on that skill working correctly
6. Read the `diagram-deploy` skill — last-mile step

---

## Figma ↔ HTML node map (from tracker)

These are the 6 diagrams in scope for this session, with their Figma mobile node IDs and current deployed HTML paths:

| # | diagram_id | Figma mobile node | Deployed HTML (live) | Status |
|---|---|---|---|---|
| 1 | port-01a-grid (dim-weights) | `1085:14` | `img/diagrams/diagram-port01a-dimension-weights.html` | shipped |
| 2 | port-01a-carousel | `1083:14` | `img/diagrams/diagram-port01a-company-grid.html` (existing) | shipped |
| 3 | port-01c-implication | `975:14` | `img/diagrams/diagram-port01c-implication.html` | shipped |
| 4 | port-03b-principles | `975:24` | `img/diagrams/diagram-port03b-principles.html` | shipped |
| 5 | port-03c-design-system | `1086:14` | `img/diagrams/diagram-port03c-design-system.html` | shipped |
| 6 | port-04b-governance | `1088:14` | — (not deployed, L3 escalation) | figma-mobile-built |

Source of truth: `working/mobile-audit/audit-tracker.xlsx` — columns `figma_mobile_node_id` and `mobile_file_path`.

Figma file ID is in `working/mobile-audit/figma-refs/` — check there for the file key. If Della gives you just a node ID, the figma-to-html skill knows how to resolve it.

---

## The flow

### Step 1: Ask Della what's ready

Before touching anything, confirm which of the 6 Figma frames she wants pulled. She may have polished all six, or only a subset. Default assumption: pull only the ones she names. Do NOT pull all six speculatively — that can overwrite in-progress polish with older HTML.

If she says "pull everything," still show her the list and confirm.

### Step 2: For each diagram, run figma-to-html

The skill handles: reading the Figma node, detecting what changed vs. the HTML, generating the updated HTML, and writing it to the working folder (NOT directly to `img/diagrams/` — that's the deploy step).

Output location per diagram: `portfolio-site/working/mobile-audit/html-updates/diagram-[id].html` (or wherever the skill writes; follow the skill).

Do not skip reading the skill file before delegating — "Skill Execution Rule" in CLAUDE.md.

### Step 3: Visual diff before deploy

For each updated HTML:
1. Render the pre-polish version (the live deployed file) at 1440 / 768 / 375
2. Render the post-polish version at the same breakpoints
3. Show Della a side-by-side or before/after so she can confirm the Figma polish landed correctly

If anything looks wrong (lost styles, broken layout, unexpected changes), STOP and flag before deploying.

### Step 4: Deploy

Use the `diagram-deploy` skill. It handles:
- Copying the updated HTML to `portfolio-site/img/diagrams/`
- Injecting `body.embedded` CSS overrides + the `window !== window.parent` detection script
- Confirming the file lands with the correct name

Watch out for the two gotchas from Session 17:
1. **Indentation variance**: port-01a-dimension-weights uses 4-space indent; the others use 2-space. The deploy regex must handle both. Session 17's deploy script is at `/sessions/quirky-eloquent-gauss/deploy_diagrams.py` in the sandbox — that version already handles this.
2. **Wrapper selector variance**: port-01a-dimension-weights uses `.container`; others use `.diagram`. Per-file override required in the embed-mode CSS.

### Step 5: Verify the live embed

After deploy, open `case-building-portfolio.html` in a headless browser at 1440 + 375 and take full-page screenshots. Confirm:
- All 10 embeds still render (6 original + 4 from Session 17)
- Updated diagrams show the polish (compare against the visual diff from Step 3)
- No visual regressions on other embeds

Screenshots go in `working/mobile-audit/screenshots/session18-figma-polish/`.

### Step 6: Tracker update

Use `openpyxl` (never pandas — destructive on this file). Update rows that got polished:
- If a new status makes sense (`shipped-polished`?), confirm with Della before adding
- Otherwise bump `verify_date` to today and append a note like "2026-04-22: Figma polish synced to HTML and redeployed"

Pattern script template at `/sessions/quirky-eloquent-gauss/tracker_update.py` from Session 17 — copy and modify.

### Step 7: Commit + push

**IMPORTANT: Don't run git from the sandbox for this project.** Session 17 had a stale `.git/index.lock` problem because of it. Give Della the commands to run in her terminal, using Mac absolute paths from PATH-MAPPINGS.md.

Template commit message (single line, no multi-line HEREDOC stuck in shell continuation):

```
cd ~/CoworkWorkspace/Get-a-job/portfolio-site
git status
git diff
git add [specific files, not -A]
git commit -m "Session 18: sync Figma mobile polish to HTML for [diagram list]"
git push
```

Pre-commit hooks will run `voice-check.py` + `quality-check.py`. Should pass (no prose changes, only HTML diagram polish) but flag if warnings appear.

---

## Open gates from Session 17 (still parked)

1. **port-04b-governance L3 redesign** — absolute-positioned ring + SVG path can't CSS-reflow. Needs a separate `-mobile.html` variant mirroring the port-04a pattern. Estimated 1-2 hours in Figma + HTML. This is a separate workstream from Session 18's polish loop — don't bundle.

2. **`diagram-pair` class CSS** — currently added as semantic metadata on the port-01a pair (carousel + dim-weights) with no CSS backing. Della's call: (a) leave as no-op semantic hook, (b) remove, or (c) extend the site stylesheet to render pairs side-by-side on desktop ≥1024px. Ask her at the start of Session 18 which route she wants.

3. **Figma sentinel test** — not run in Session 17. ~10 min when MCP is loaded. Low priority.

---

## Known gotchas (inherited from Session 17)

From `Get-a-job/CLAUDE.md` + BUILD-LOG:

- **Never run `git` commands from the sandbox for this project.** Creates stale `.git/index.lock`. Give Della terminal commands.
- **Multi-line HEREDOC commit messages can hang shell continuation.** Use single-line `-m "..."` for any command Della will paste.
- **openpyxl only for the tracker.** Pandas `to_excel` destroys formatting and existing rows.
- **Living documents** (the case page, the tracker, the overview) are edited in-place — never regenerated from scratch.
- **Verify before claiming.** Don't tell Della the polish landed without rendering screenshots and showing her.

---

## Deliverables checklist (end of Session 18)

- [ ] Updated HTMLs in `img/diagrams/` for each polished diagram
- [ ] Visual diffs shown to Della before deploy
- [ ] Screenshots in `working/mobile-audit/screenshots/session18-figma-polish/`
- [ ] Tracker updated via openpyxl for polished rows
- [ ] Single clean commit pushed to main
- [ ] Live site verified — `case-building-portfolio.html` still renders 10 embeds correctly
- [ ] Session report at `working/mobile-audit/reports/session18-figma-polish-sync.md`
- [ ] BUILD-LOG entry appended

---

## If Della opens the session with a different ask

This pickup assumes the next session is the Figma-polish-sync loop. If Della shows up with a different priority (interviews, port-04b redesign, new case study, etc.), park this doc and take her priority. This file will still be here when the polish cycle is ready.

---

## Related docs

- `reports/session17-ship-complete.md` — full Session 17 write-up
- `resume-prompt-portfolio-ship-complete.md` — the Session 17 plan (for historical reference)
- `resume-prompt-case-building-portfolio-figma-to-html.md` — earlier iteration of the same loop, pre-Session 17
- `resume-prompt-session16-figma-mobile-frames.md` — when the mobile Figma frames were first built
- `CoworkWorkspace/Skills/figma-to-html/SKILL.md` — the skill to execute
- `CoworkWorkspace/Skills/diagram-deploy/SKILL.md` — the skill to execute
