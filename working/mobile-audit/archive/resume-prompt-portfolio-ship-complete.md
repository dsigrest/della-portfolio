# Resume prompt — Ship case-building-portfolio to completion (single pass)

**Copy the block below as the first message in a fresh Cowork thread. This supersedes `resume-prompt-portfolio-pairing-roundtrip.md` for the next execution.**

---

Finish shipping `case-building-portfolio`. Twelve diagrams were planned; six are live, six are built but unshipped with minor issues in between. This thread runs all six stages autonomously end-to-end. Della is stepping out — do not block on her unless a genuine decision gate is hit. Default to executing with the rationale captured in the final report; she'll review on return.

## Ground rules (non-negotiable)

1. **Read required files in full first.** No summarization substitutes. Mandatory reads at kickoff:
   - `/Users/della/CoworkWorkspace/CLAUDE.md`
   - `/Users/della/CoworkWorkspace/Get-a-job/CLAUDE.md`
   - `/Users/della/CoworkWorkspace/PATH-MAPPINGS.md`
   - `/Users/della/CoworkWorkspace/Skills/responsive-audit/SKILL.md`
   - `/Users/della/CoworkWorkspace/Skills/diagram-deploy/SKILL.md`
   - `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/reports/figma-handoff-case-building-portfolio.md`

2. **Verify before claiming.** Every "done" statement must be backed by an actual check — rendered screenshot, file hash, script exit code, tracker read-back. Do not tell Della something landed without verifying it yourself.

3. **Never commit from sandbox.** Give Della the Mac-absolute-path `git add` / `git commit` commands at the end. She runs them.

4. **Never use `git add -A` or `.`** — stage specific files by name only (CLAUDE.md global rule).

5. **Living-document rule for `case-building-portfolio.html`**: targeted edits only. Do not delegate full-file rewrites. Each new `data-diagram` embed is an insertion, not a regeneration.

6. **tidyPage suspended** on Figma file `TArUrZsBUocaAsqetjXq7V` page `29:2`. Additive writes only. Do not reposition existing frames.

7. **Autonomous defaults.** Every decision gate has a documented default action. Execute the default and record the rationale. Flag only genuinely ambiguous decisions in the final report for Della's post-walk review.

## Known state at thread start (verified Session 16)

**Twelve diagrams. Shipped status:**

| Diagram | HTML responsive | Figma mobile node | On live site | Embedded in case page |
|---|---|---|---|---|
| port-01a-carousel | ✓ | 1083:14 | ✓ | ✓ |
| port-01b | ✓ | 849:14 | ✓ | ✓ |
| port-02c | ✓ | 849:35 | ✓ | ✓ |
| port-03a | ✓ | 838:14 | ✓ | ✓ |
| port-04a | ✓ | 852:14 | ✓ | ✓ |
| port-05 | ✓ | 852:95 | ✓ | ✓ |
| port-01a-grid (dim-weights) | ✗ **NO @media rules** | 1085:14 | ✗ | ✗ |
| port-01d-implication | ? — **tracker path wrong**: actual file is `port-01c-implication` | 975:14 | ✗ | ✗ |
| port-03a1-thumbnails | **file does not exist** — tracker references a gallery that was never built | 838:14 (reused desktop) | ✗ | ✗ |
| port-03b-principles | ✓ | 975:24 | ✗ | ✗ |
| port-03c-design-system | ✓ | 1086:14 | ✗ | ✗ |
| port-04b-governance-v5 | ✓ | 1088:14 | ✗ | ✗ |

**Tracker:** `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/audit-tracker.xlsx`, sheet `audit`.

**Working HTML source folder:** `/Users/della/CoworkWorkspace/Get-a-job/working/diagrams/v3/` (governance at `v5/`).

**Live portfolio site:** `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/img/diagrams/` (HTML) + `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/case-building-portfolio.html` (embeds).

---

## Stage 0 — Inventory & sentinel (5 min)

**Goal:** confirm the state above is still accurate and no other thread has made changes.

1. `ls` the three canonical folders: working HTML source, live site diagrams, portfolio-site root. Diff against the state table above.
2. Read the 6 unshipped working HTMLs and count `@media` rules in each.
3. Read the tracker, confirm the 12 `case-building-portfolio` rows and their current statuses.
4. Sentinel-test the Figma write channel on node `975:14` (rename + restore). If writes don't land, continue without Figma — Stages 1–6 don't require Figma writes. Only flag in final report.

If state has shifted materially (e.g., someone else shipped port-01a-grid already), recompute scope and continue. Never abort — always finish with the best-possible ship.

---

## Stage 1 — Tracker integrity fixes (auto)

**Goal:** resolve the 2 naming discrepancies so downstream stages have clean inputs.

### Decision 1.1 — `port-01d-implication` row vs. `port-01c-implication` file

**Investigation:** read the actual HTML file's `<title>` tag and the `<meta name="figma-source">` node reference. Read `case-building-portfolio.html` for any existing `data-diagram="port-01c"` or `port-01d"` reference. Read the git log on the file (`git log --follow -- working/diagrams/v3/diagram-port01c-implication.html`) to check rename history.

**Default:** rename the tracker row from `port-01d-implication` → `port-01c-implication` and update `mobile_file_path` to the real path. Do NOT rename the file — that changes too many references.

**Override condition:** if the HTML's `<title>` explicitly says "PORT-01d" or there's evidence of a deliberate naming choice, rename the file on disk instead and update any references. Record which path you chose.

Execute the fix via openpyxl (additive write, no pandas overwrites). Verify by re-reading the tracker.

### Decision 1.2 — `port-03a1-thumbnails` ghost row

**Investigation:** search the full workspace for any `port-03a1`, `port03a1`, or `thumbnails-gallery` reference in source, commits, or build logs. Check Figma node 838:14 metadata — is it being reused intentionally, or is there an orphan expectation?

**Default:** set the tracker row's `status` to `deleted-ghost-row` and clear `figma_mobile_node_id`. Write a one-line note in the `notes` column: "Row created 2026-04-22 referencing non-existent HTML; 838:14 is the desktop port-03a node, already shipped as port-03a. No separate gallery diagram exists."

**Override condition:** if any reference exists suggesting this was a real planned diagram, leave the row alone and flag it for Della's review with a specific question: "Is port-03a1-thumbnails-gallery a diagram you still want built, or was this row created in error?"

### Stage 1 verification

Re-read the tracker. Confirm exactly 11 `case-building-portfolio` rows remain active (or 12 if port-03a1 was retained). Produce a before/after diff of the changed rows.

---

## Stage 2 — Responsive HTML fixes (auto)

**Goal:** every unshipped HTML passes a 6-breakpoint responsive audit before deploy.

### Task 2.1 — port-01a-dimension-weights.html

This file has zero `@media` rules. Add responsive rules following the established pattern from other port- diagrams.

**Pattern to replicate (from `diagram-port01a-carousel.html` and `diagram-port03c-design-system.html`):**

```css
@media (max-width: 680px) {
  body { padding: 16px; }
  .diagram { width: 100%; padding: 24px; }
  /* diagram-specific reflow rules */
}
```

**Inspect the HTML first.** The diagram is a 6-row × 6-column grid (Company + 5 dimension headers). At 375px, the grid cannot stay 6-column. Options:
- **Recommended:** stack as card-per-company (like port-01a-grid already does in its grid version) with each company's 5 weights rendered as horizontal mini-bars below its name.
- **Simpler fallback:** horizontal scroll with `overflow-x: auto` on the grid container and a minimum cell width.

**Default:** implement the recommended card-stack pattern. Use subagent: `Agent({description: "Add mobile responsive to port-01a-dim-weights", prompt: "[full file-level prompt including the file path, the pattern to copy from port-01a-carousel's @media block, and the reflow constraint]"})`. Verify with a 375px screenshot after.

### Task 2.2 — responsive-audit on the other 5

Invoke the `responsive-audit` skill for the 5 built-but-unshipped HTMLs (after Task 2.1 completes for port-01a-grid):

- `port-01a-dimension-weights.html` (post-fix)
- `port-01c-implication.html` (or `port-01d` if you renamed in Stage 1)
- `port-03b-principles.html`
- `port-03c-design-system.html`
- `port-04b-governance-v5.html`

Standard 6 breakpoints: 1440, 1024, 768, 480, 375, 320. Apply any container/content fixes the skill surfaces. Skip redesign-severity fixes (escalate in final report).

### Stage 2 verification

Re-audit post-fix. All 5 files must return `ok_375 = pass` and `ok_320 = pass` before moving on. Take a 375px screenshot of each and save to `working/mobile-audit/screenshots/port-ship-complete/`.

---

## Stage 3 — Deploy to live site (auto)

**Goal:** copy all 6 files from `working/diagrams/v3/` (or `v5/`) to `portfolio-site/img/diagrams/`.

### Files to deploy

| Source path | Destination filename on site |
|---|---|
| `working/diagrams/v3/diagram-port01a-dimension-weights.html` | `diagram-port01a-dimension-weights.html` |
| `working/diagrams/v3/diagram-port01c-implication.html` (or `port01d` per Stage 1) | match the tracker's final naming |
| `working/diagrams/v3/diagram-port03b-principles.html` | `diagram-port03b-principles.html` |
| `working/diagrams/v3/diagram-port03c-design-system.html` | `diagram-port03c-design-system.html` |
| `working/diagrams/v5/diagram-port04b-governance-v5.html` | `diagram-port04b-governance-v5.html` |

(Five files — not six. port-03a1 is resolved in Stage 1 as either a ghost row or a flagged open question; nothing to deploy for it in this run.)

Invoke the `diagram-deploy` skill per file (or batch if the skill supports it).

### Stage 3 verification

- Confirm each file exists at destination with byte-level match (diff returns 0) against source.
- Run `portfolio-site/quality-check.py` against each new file. All must pass HTML validity, a11y, link checks. Fix any failures inline before moving on.
- Take a 1440px desktop screenshot + 375px mobile screenshot of each deployed HTML rendered standalone. Save to `working/mobile-audit/screenshots/port-ship-complete/deployed/`.

---

## Stage 4 — Embed in case-building-portfolio.html (auto with default positions)

**Goal:** add 5 `data-diagram` embeds to the case study page at narrative-correct positions.

### Narrative positions (defaults — execute unless clearly wrong)

Current page (verified Session 16) has 6 existing embeds in this order: `port-01a-carousel` (line 59) → `port-01b` (69) → `port-02c` (83) → `port-03a` (102) → `port-04a` (126) → `port-05` (152).

**Default insertion positions for the 5 new embeds:**

| New diagram | Insert after existing embed | Rationale |
|---|---|---|
| `port-01a-dimension-weights` | `port-01a-carousel` (pair) | Carousel shows one company at a time; grid shows all six at once. Pair as `diagram-pair`. |
| `port-01c-implication` | `port-01b` | 01b surfaces the research insight; 01c shows the implication that flows from it. |
| `port-03b-principles` | `port-03a` | After the thumbnail survey, principles distill what the survey taught. |
| `port-03c-design-system` | `port-03b-principles` | Principles → system. Natural progression. |
| `port-04b-governance` | `port-04a` (pair) | Two views of governance — pair as `diagram-pair`. |

### Embed snippet pattern (copy from line 59 of case-building-portfolio.html)

```html
<div class="case-img-full diagram-embed" data-diagram="port-XX">
  <!-- iframe injected by runtime script at line ~263 -->
</div>
```

For paired embeds (01a-grid + 01a-carousel, 04a + 04b), use `class="case-img-full diagram-embed diagram-pair"`.

### Execution

Use targeted Edit calls per insertion (never a full-file rewrite). For each insertion:
1. Read the surrounding 20 lines of the case page to understand the existing prose/heading structure.
2. Insert the embed snippet immediately after the closing tag of the referenced existing embed.
3. Re-read the file after each insert to confirm placement didn't shift other line numbers incorrectly.

### Stage 4 verification

- Count `data-diagram=` occurrences in `case-building-portfolio.html`. Must equal **11** (6 existing + 5 new).
- Render the case page via `quality-check.py` — no broken iframe references, all `data-diagram` values map to files in `img/diagrams/`.
- Take a full-page desktop screenshot of the case page at 1440px. Save to `working/mobile-audit/screenshots/port-ship-complete/case-page-after.png`.

**If any insertion position feels narratively wrong** (e.g., reading the surrounding prose reveals the intended location was different), leave that embed uninserted and flag it in the final report with the proposed options. Don't guess on narrative — flag it.

---

## Stage 5 — Final tracker sync + quality gate (auto)

**Goal:** tracker reflects final state; nothing ships with voice or quality issues.

1. **Tracker updates (openpyxl only, additive):**
   - Flip all 5 deployed-and-embedded rows from `figma-mobile-built` → `shipped`.
   - Stamp `verify_date` = today's date (ISO).
   - Update `mobile_file_path` to the live `portfolio-site/img/diagrams/...` path.
   - If port-03a1 was flagged rather than deleted, leave its row as-is.

2. **Voice + quality checks:**
   - Run `portfolio-site/voice-check.py` on `case-building-portfolio.html`. Surface any violations (do not auto-fix voice — those are Della's call).
   - Run `portfolio-site/quality-check.py` on the whole portfolio-site. Must pass with no new errors introduced by this session's work.

3. **Tracker read-back:** open the xlsx, dump the 12 case-building-portfolio rows to confirm persisted state matches intent.

---

## Stage 6 — Git commit package for Della (auto — build, do not execute)

**Goal:** hand Della a ready-to-paste git workflow she can run when she's back.

Produce the exact commands using **Mac-absolute paths from PATH-MAPPINGS.md**. Validate each path before including (no `/sessions/` paths, no missing `CoworkWorkspace/` segments).

**Expected command block in the final report:**

```bash
cd ~/CoworkWorkspace/Get-a-job/portfolio-site

# Review the diff
git status
git diff --stat
git diff case-building-portfolio.html

# Stage by name (no -A)
git add img/diagrams/diagram-port01a-dimension-weights.html
git add img/diagrams/diagram-port01c-implication.html   # (or port01d per Stage 1 choice)
git add img/diagrams/diagram-port03b-principles.html
git add img/diagrams/diagram-port03c-design-system.html
git add img/diagrams/diagram-port04b-governance-v5.html
git add case-building-portfolio.html

# Commit
git commit -m "Ship 5 new port- diagrams to case-building-portfolio"

# Push (Della's call whether to push directly or PR)
git push origin main
```

**Do NOT run any of these.** Block this is a handoff, not an action.

---

## Final report format (Della reads this when she's back)

Keep it scannable. Structure:

1. **Headline status** — "X of 6 new diagrams shipped; Y decision gates remain."
2. **Stage-by-stage summary table** — one row per stage: what was done, default choices taken, any deviations.
3. **Open decision gates** — only items genuinely needing Della's input (narrative positions flagged in Stage 4, port-03a1 resolution if it was ambiguous, any voice-check failures). For each: the question, the options, the recommended default.
4. **Files changed** — final list with link previews using `computer://` URLs.
5. **Screenshots** — link the `port-ship-complete/` folder.
6. **Git commands** — the Mac-path-validated block above.
7. **Tracker final state** — 12-row dump showing final statuses.
8. **Anything surfaced for the `html-to-figma` v1.1.0 patch work** — feed into that separate thread.

Total report length cap: 800 words in the chat message. Everything verbose goes to the saved `working/mobile-audit/reports/session17-ship-complete.md`.

---

## Context-window preservation tactics

Della has parallel threads running. Be miserly:

- **Parallelize.** Spawn subagents for stages that don't depend on each other. Specifically: Stage 2.2's 5 responsive audits can run in 2 parallel subagents (3 + 2). Stage 3's 5 deploys can run as 1 subagent if diagram-deploy supports batches. Stage 4's 5 embed insertions should NOT parallelize — they share the same file and must be sequential.
- **Don't re-read files you already read.** Cache the state-table facts in your working memory after Stage 0.
- **Don't output full file contents.** Diffs only. Show Della what changed, not what was.
- **Hold screenshots in the filesystem**, not the chat. Reference by path.
- **When ending, close all open subagents** before writing the final report.

---

## If something breaks mid-stage

- **Minor failure** (one file fails quality-check, one embed position is genuinely ambiguous): continue the stage, flag the item in the final report, move to the next stage.
- **Major failure** (Figma MCP completely down, diagram-deploy skill missing, tracker corrupt): stop at the current stage, produce a partial report with exactly what shipped and what didn't, do not attempt recovery autonomously.
- **Between any two stages**, if context is burning, checkpoint to `working/mobile-audit/reports/session17-ship-complete.md` and continue from where you stopped in a new thread.

Execute. Della is on a walk.
