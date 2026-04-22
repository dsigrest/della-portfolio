# Case-AI Mobile Completion — Thread Handoff Prompt

**Status when this was written:** 2026-04-22, after re-verification discovered that 2 of the 4 case-ai rows previously marked `fixed` were never actually mobile-ready in the live HTML. The "fixes" were Figma-only — desktop HTML + Figma mobile frame, but no HTML mobile variant and no `.diagram-pair` swap. Tracker has been corrected. This prompt handles the actual HTML finish.

**Copy this entire file into a fresh thread. Do not summarize it — paste it verbatim.**

---

## What you're doing

Finishing mobile variants for 3 case-ai diagrams so they render correctly at 480/375/320 on the live portfolio site. Two (ai06, ai19) need new mobile HTML files built from existing Figma frames. One (ai23) already has the HTML infrastructure — it just needs a verification screenshot.

**Explicit out-of-scope — do not touch any of this:**
- `ai24` — already verified 2026-04-22, reflows cleanly, leave it alone.
- `styles.css` `.diagram-pair` swap rule (lines ~365–378) — already correct, do not modify.
- Any other case study — this thread handles case-ai only.
- Any Figma canvas tidying / page reorganization — do not run `tidyPage` on the case-ai Figma page.
- Any living document (SESSION-STATE.md, BUILD-LOG.md, interview-cheat-sheets.html, recruiter-outreach-tracker.xlsx) — unrelated to this work.

---

## Step 0 — Pre-flight reads (MANDATORY, in order)

Before writing any code or making any changes, read these files in full:

1. `~/CoworkWorkspace/CLAUDE.md` — global rules (Voice, Skill Execution, Verify-Before-Claiming, File Routing).
2. `~/CoworkWorkspace/Get-a-job/CLAUDE.md` — project rules (Source Verification, Living Documents, Voice Processing).
3. `~/CoworkWorkspace/Get-a-job/portfolio-site/PATH-MAPPINGS.md` — convert any sandbox path to Mac absolute before showing Della a command.
4. `~/CoworkWorkspace/Skills/figma-to-html/SKILL.md` — the skill you will execute (do not paraphrase — read the file).
5. `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/scripts/tracker-helpers.py` — openpyxl atomic writer. Use `update_row` and `read_tracker`. Never pandas.
6. `~/CoworkWorkspace/Get-a-job/portfolio-site/case-ai.html` **lines 372–389** — this is your reference `.diagram-pair` pattern (ai23). Every new wrapper in this thread mirrors this block exactly.

If any of these don't load, stop and ask Della to remount `~/CoworkWorkspace` before proceeding.

---

## The 3 diagrams in scope

| Diagram | Tracker status (now) | What's done | What's missing |
|---|---|---|---|
| **ai06** | `audited` (verify_date cleared) | Desktop HTML at `img/diagrams/diagram-ai06-evaluation-matrix-v4.html`. Figma mobile frame at node **774:8** (position `-420, -8774`, size `375×462`). | No `-mobile.html` file. No `.diagram-pair` wrapper in `case-ai.html`. Clips at 375/320 (Prompt C/D cut off). |
| **ai19** | `audited` (verify_date cleared) | Desktop HTML at `img/diagrams/diagram-ai19-attribution-comparison-v4.html`. Figma mobile frame at node **772:8** (position `-420, 1643`, size `375×169`). | No `-mobile.html` file. No `.diagram-pair` wrapper in `case-ai.html`. Clips at 375/320 (status column cut off). |
| **ai23** | `fixed` (verify_date 2026-04-21) | Desktop HTML, mobile HTML (`-v4-mobile.html`), and `.diagram-pair` wrapper in `case-ai.html` lines 372–389 — **all already exist and correct**. | No mobile screenshot was captured in the last run (safety-net was case-sharing only). Just needs a screenshot pass to visually verify, then flip `status` to `verified`. |

**Figma file key:** `TArUrZsBUocaAsqetjXq7V`
**Figma page for case-ai:** the case-ai page (`node-id=301:2` root). Mobile cluster is left of desktop cluster, same row as each corresponding desktop frame.

---

## The workflow — exact sequence, do not reorder

### Phase 1 — Pull ai06 and ai19 mobile HTML from Figma

For each of ai06 (node 774:8) and ai19 (node 772:8):

1. Invoke the **figma-to-html** skill. The skill handles the Figma→HTML translation with CSS-selector layer names. Target output paths:
   - `portfolio-site/img/diagrams/diagram-ai06-evaluation-matrix-v4-mobile.html`
   - `portfolio-site/img/diagrams/diagram-ai19-attribution-comparison-v4-mobile.html`
2. The mobile file must include the embed-mode script at the bottom (copy from any existing `-v4-mobile.html` as reference — e.g., `diagram-ai23-trust-comparison-v4-mobile.html`):
   ```html
   <script>if(window!==window.parent)document.body.classList.add("embedded");</script>
   ```
   and matching `body.embedded { … }` CSS.
3. Sanity check: open the new mobile HTML file directly in a browser at 375px. All columns / rows should fit without horizontal scroll. Do NOT trust it fits without verifying.

### Phase 2 — Wrap iframes in `.diagram-pair` in `case-ai.html`

For each of ai06 and ai19, replace the current single-iframe block with a `.diagram-pair` wrapper. Use `case-ai.html` lines 372–389 (ai23) as the reference pattern:

```html
<div class="case-img-full diagram-embed diagram-pair" data-diagram="ai-06">
  <iframe class="desktop-variant"
          src="img/diagrams/diagram-ai06-evaluation-matrix-v4.html"
          loading="lazy" scrolling="no"
          style="width: 100%; border: none; ..." />
  <iframe class="mobile-variant"
          src="img/diagrams/diagram-ai06-evaluation-matrix-v4-mobile.html"
          loading="lazy" scrolling="no"
          style="width: 100%; border: none; ..." />
</div>
```

- **Preserve** any inline style on the existing desktop iframe (height, aspect ratio, etc.). The mobile iframe's inline style should match what makes visual sense for the mobile variant's intrinsic height (check the Figma frame dimensions — ai06 is 462px tall, ai19 is 169px tall).
- **Do NOT edit** `styles.css`. The `.diagram-pair` swap rule is already live at approximately lines 365–378.
- Before editing, **Read** the current ai06 and ai19 blocks in `case-ai.html` to capture the exact current inline style so you can preserve it on the desktop variant.

### Phase 3 — Capture screenshots for all 3 diagrams

Run:
```bash
cd ~/CoworkWorkspace/Get-a-job/portfolio-site
python3 working/mobile-audit/scripts/screenshot-diagrams.py case-ai
```

This captures each diagram standalone at all 6 breakpoints AND captures `pages/case-ai.png` at each breakpoint. Takes ~2–3 minutes.

**Critical caveat:** the standalone diagram screenshots for ai06 and ai19 will STILL clip at 375/320, because the script captures each diagram via its standalone `file://` URL and the desktop HTML's fixed 760px width has nothing to reflow. **Do not conclude the fix failed from the standalone screenshots.** The real verification is `screenshots/{375,320}/pages/case-ai.png` — those render the full case study page, where the `.diagram-pair` CSS swap fires. Look at those page-level screenshots, not the standalone diagram ones.

For ai23, the standalone screenshot `screenshots/375/case-ai/ai23-trust-comparison-v4.png` should also clip (same reason — it captures the desktop file); the verification file for ai23 is `screenshots/375/case-ai/ai23-trust-comparison-v4-mobile.png` (if the script captures it — confirm by listing the output dir).

### Phase 4 — Visual verification (verify-before-claiming)

Read the following screenshots and confirm cleanly:

- `screenshots/480/pages/case-ai.png` — ai06, ai19, ai23 all render cleanly inside the page.
- `screenshots/375/pages/case-ai.png` — same, critical breakpoint.
- `screenshots/320/pages/case-ai.png` — same, worst-case breakpoint.
- `screenshots/375/case-ai/ai23-trust-comparison-v4-mobile.png` if it exists — confirm ai23 mobile variant renders.

For each of the 3 diagrams:
- If clean at 480, 375, and 320 → proceed to Phase 5.
- If anything clips or breaks → stop. Do not mark `verified`. Report back to Della what you saw and at which breakpoint.

### Phase 5 — Atomic tracker updates

Use `tracker-helpers.py update_row`. Do not use pandas. Do not rewrite the xlsx. See the existing cleanup script at `scripts/cleanup-case-ai-rows.py` for the exact invocation pattern.

On successful verification, update:

```python
TODAY = "YYYY-MM-DD"  # the actual date you run this

# If ai06 passed:
th.update_row(TRACKER, "ai06", {
    "status": "verified",
    "verify_date": TODAY,
    "notes": "Completed 2026-XX-XX: mobile HTML built via figma-to-html from node 774:8; "
             ".diagram-pair wrapper added to case-ai.html; verified at 480/375/320 in "
             "pages/case-ai.png. | [preserve prior NEEDS FIX + Prior history from current notes]"
})
# Same pattern for ai19 (node 772:8) and ai23 (no new mobile HTML needed — just verification).
```

**Preserve prior notes.** Read the existing notes field first (via `th.read_tracker(TRACKER)`), then prepend the completion note and preserve the rest with a ` | ` separator. Do not overwrite history.

### Phase 6 — Quality gates

Run in order:

```bash
cd ~/CoworkWorkspace/Get-a-job/portfolio-site
python3 quality-check.py case-ai.html
python3 quality-check.py img/diagrams/diagram-ai06-evaluation-matrix-v4-mobile.html
python3 quality-check.py img/diagrams/diagram-ai19-attribution-comparison-v4-mobile.html
```

All three must pass. If any fails, fix the specific error and re-run — do not suppress warnings.

### Phase 7 — Report back to Della

Return a concise summary:
- 3 diagrams closed out: ai06, ai19, ai23 → all `verified`.
- Files created: 2 new `-v4-mobile.html` files.
- Files modified: `case-ai.html` (2 iframe blocks wrapped in `.diagram-pair`).
- Quality-check: pass/fail.
- Links (Mac absolute paths from PATH-MAPPINGS.md): the 3 verified page screenshots at 480/375/320.
- Any flags.

---

## Crash / context guardrails

This prompt is designed to run predictably without exhausting context. Follow these to stay safe:

1. **Do NOT read entire case-ai.html.** It's long. Use `Read` with `offset`/`limit` — lines 372–389 for the ai23 reference, then separate targeted reads for the ai06 and ai19 blocks you're replacing.
2. **Do NOT read entire desktop diagram files** (diagram-ai06-*.html, diagram-ai19-*.html). You don't need them — the mobile versions come from Figma.
3. **Do NOT run responsive-audit Mode 1.** You are NOT auditing case-ai from scratch — the audit already happened. This is targeted finish work.
4. **Delegate figma-to-html via the Skill tool**, not by reading every file in that skill folder into main context.
5. **Between Figma pulls**, checkpoint to a scratch note (e.g., `working/mobile-audit/ai-completion-scratch.md`) with: which diagram done, output path, any flags. If the thread restarts, the next thread can pick up from there.
6. **Do not spawn sub-agents** for this work. The whole job fits in one thread if you respect the read scope above.
7. **Do not open Figma MCP unless the skill needs it.** The figma-to-html skill owns that connection.
8. **Do not regenerate screenshots you already have.** Phase 3 is one screenshot-diagrams.py run, not multiple. If the run crashes midway, resume with the same command — it overwrites in place.

---

## Success criteria

When this thread is done, all of the following are true:

- ✓ `diagram-ai06-evaluation-matrix-v4-mobile.html` exists, valid HTML, embed-mode script present.
- ✓ `diagram-ai19-attribution-comparison-v4-mobile.html` exists, valid HTML, embed-mode script present.
- ✓ `case-ai.html` ai06 iframe wrapped in `.diagram-pair` (desktop + mobile variants).
- ✓ `case-ai.html` ai19 iframe wrapped in `.diagram-pair` (desktop + mobile variants).
- ✓ `screenshots/{480,375,320}/pages/case-ai.png` all render cleanly — no clipping, no overflow, all diagrams legible.
- ✓ Tracker rows ai06 / ai19 / ai23 all `status=verified` with today's `verify_date`, prior notes preserved.
- ✓ `quality-check.py` passes on all edited files.
- ✓ Della has a short summary with computer:// links to the 3 verified page screenshots.

**Do NOT** touch ai24, `styles.css`, any other case study, Figma canvas positioning, or any living document.

---

## Reference: the exact ai23 `.diagram-pair` block to mirror

Located in `case-ai.html` at lines 372–389. Read it directly — do NOT trust this snippet to match verbatim (line numbers may drift). Open the file and capture the live block, then pattern ai06 and ai19 after it.

---

*Prompt authored 2026-04-22. When the work is complete, append a line to `working/mobile-audit/BUILD-LOG.md` noting thread completion.*
