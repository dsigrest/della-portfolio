# Resume Prompt — case-ai add ai10 + ai16 (full pipeline)

**Use this prompt when:** Della wants to bring two case-ai diagrams that currently exist only as source HTML in `working/diagrams/v3/` — `ai10` (Graceful Degradation — failure state) and `ai16` (A System, Not a Solution — final identification system) — all the way through to live, paired, polished case-ai entries matching the rest of the case study.

**Paste this entire file as the opening message of a fresh Cowork thread.**

---

## Context (what's already done — do not redo)

- Case-ai has 19 diagrams currently live in `portfolio-site/case-ai.html`. All have desktop + mobile HTML in `portfolio-site/img/diagrams/` (v4 naming). All 19 have paired Figma frames (desktop + mobile native-layer) on page `29:42` of Figma file `TArUrZsBUocaAsqetjXq7V`. Mobile cluster anchored at `x = -420`. Sessions 10–14 built this out.
- `ai10` and `ai16` were always intended to be part of case-ai but were never promoted from the working-diagrams exploration tree. Current state in `case-ai.html`:
  - Line 222: `<div class="img-placeholder">Failure state — suppressed synthesis, source posts displayed with threaded comments as fallback</div>` → this is the ai10 slot
  - Line 298: `<div class="img-placeholder">Final identification system — persistent elements (color, name, separation) applied across multiple Reddit surfaces</div>` → this is the ai16 slot
- Source HTML (v3, most current) already exists:
  - `working/diagrams/v3/diagram-ai10-failure-state.html` (568 lines, title: "Graceful Degradation")
  - `working/diagrams/v3/diagram-ai16-final-identification.html` (448 lines, title: "A System, Not a Solution")
- Both use the same token palette as the rest of case-ai (`--canvas #0A0C16`, `--accent #7FB5B0`, `--casual #D4A574`, `--resur #C4B078`, `--new-seg #8A9EC4`, `--red #C47878`).

**This thread's job is the FULL pipeline for these two diagrams** — not just Figma pairing. HTML promotion, desktop polish, responsive audit, Figma desktop + mobile frames, `.diagram-pair` wiring in `case-ai.html`, tracker rows, quality gates, live verify, docs.

---

## Pre-flight reads (mandatory, in order)

1. `~/CoworkWorkspace/CLAUDE.md` — global voice + session rules
2. `~/CoworkWorkspace/Get-a-job/CLAUDE.md` — project-specific rules (source verification, verify-before-claiming, living documents)
3. `~/CoworkWorkspace/Get-a-job/PATH-MAPPINGS.md` — Mac absolute paths (mandatory before any terminal command shown to Della)
4. `~/CoworkWorkspace/Get-a-job/SESSION-STATE.md` — current state (should read "Session 14 complete, case-ai all 19 mobile frames paired — ai10 + ai16 still pending site integration")
5. `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/figma-handoff-case-ai.md` — node-ID table for all 19 existing pairs, technique notes
6. `~/CoworkWorkspace/Get-a-job/BUILD-LOG.md` — Session 10 (case-ai Figma pair foundation), Session 14 (native-layer pass) technique playbooks
7. `~/CoworkWorkspace/Skills/html-to-figma/SKILL.md` — v1.0.0+ native-layer translation
8. `~/CoworkWorkspace/Skills/responsive-audit/SKILL.md` — mobile audit + fix pipeline
9. `~/CoworkWorkspace/Skills/diagram-deploy/SKILL.md` — wiring finished diagrams into the case-study page
10. `~/CoworkWorkspace/Get-a-job/portfolio-site/case-ai.html` — read the 3 existing `.diagram-pair` patterns (line 154 = ai-06, line 319 = ai-19, line 390 = ai-23) so your wiring matches exactly

---

## Task summary (two diagrams, full pipeline each)

For `ai10` (failure state) and `ai16` (final identification):

1. **Promote source HTML** → `v4` in `img/diagrams/`
2. **Desktop polish pass** (if source needs it — verify against v4 quality bar set by ai06/ai19/ai23)
3. **Responsive audit** → produces `-v4-mobile.html` variant
4. **Replace placeholder in `case-ai.html`** with `.diagram-pair` wrapper (desktop + mobile iframes)
5. **Build Figma desktop frame** on page `29:42` (match position convention with neighbors)
6. **Build Figma mobile frame** at `x = -420` on page `29:42` (native-layer translation)
7. **Add tracker rows** to `working/mobile-audit/audit-tracker.xlsx` via `tracker-helpers.py`
8. **Quality gates**: `quality-check.py` + `voice-check.py`
9. **Live verify** after push (Chrome DevTools device emulation at 320/375/414/430/500 widths — do NOT rely on Chrome MCP `browser_batch` for this; see SESSION-STATE note about 500px floor)
10. **Close the loop**: update BUILD-LOG (Session 15), SESSION-STATE, figma-handoff-case-ai.md

---

## Step 1 — Source material review + greenlight gate

Read both source files in full:
- `working/diagrams/v3/diagram-ai10-failure-state.html`
- `working/diagrams/v3/diagram-ai16-final-identification.html`

Also read older versions for context (do NOT promote these — just confirm v3 is the intended current):
- `working/diagrams/v1-originals/diagram-ai16-final-identification.html`
- `working/diagrams/v2/diagram-ai10-failure-state.html`
- `working/diagrams/v2/diagram-ai16-final-identification.html`
- `working/diagrams/v2-upgraded/diagram-ai16-final-identification.html`
- `working/diagrams/diagram-ai10-failure-state.html` (loose copy, 325 lines — likely outdated)
- `working/diagrams/diagram-ai16-final-identification.html` (loose copy, 345 lines — likely outdated)
- `deliverables/diagram-ai16-final-identification.html` (345-line deliverable — verify if current)

**Before promoting anything, show Della:**
- A quick summary of each v3 diagram (what it shows, dimensions, visual technique — e.g., "ai10 is a 760px-wide failure-state narrative with 4 stacked panels showing synthesis suppression → source fallback; uses the same token palette as ai06/ai11")
- A side-by-side quality comparison: does v3 meet the bar set by `diagram-ai06-evaluation-matrix-v4.html` and `diagram-ai23-trust-comparison-v4.html`? Call out anything that looks underbaked (thin strokes, placeholder text, missing mobile-specific media queries, etc.)
- A recommendation on whether v3 is ready to promote as-is, or whether a desktop polish pass is warranted first (invoke `codesign` skill for polish if so)
- Get explicit greenlight before touching `img/diagrams/` or `case-ai.html`

---

## Step 2 — Promote HTML → `img/diagrams/`

For each approved diagram:

```bash
cd ~/CoworkWorkspace/Get-a-job
cp working/diagrams/v3/diagram-ai10-failure-state.html \
   portfolio-site/img/diagrams/diagram-ai10-failure-state-v4.html
cp working/diagrams/v3/diagram-ai16-final-identification.html \
   portfolio-site/img/diagrams/diagram-ai16-final-identification-v4.html
```

Naming convention: `diagram-ai<NN>-<kebab-slug>-v4.html` — matches neighbors (`diagram-ai09-dual-user-framework-v4.html`, `diagram-ai11-feedback-loop-v4.html`).

If the v3 source has an `<h1>` or body title that differs from the intended diagram id, keep the filename but DO NOT rename the `<title>` — the v4 file is self-contained.

---

## Step 3 — Desktop polish pass (only if Step 1 greenlight flagged it)

If the v3 diagram doesn't match the v4 quality bar:
1. Invoke `codesign` skill with a targeted brief — e.g., "bring `diagram-ai10-failure-state-v4.html` to parity with `diagram-ai06-evaluation-matrix-v4.html` — keep the composition, tighten typography, fix any stroke/radius inconsistencies."
2. Show Della the before/after rendered at full-width.
3. Do NOT invent new content or change the diagram's concept — polish is strictly visual refinement of the existing composition.

Skip this step if Della greenlit v3 as-is.

---

## Step 4 — Responsive audit (mobile variant)

Invoke the `responsive-audit` skill scoped to these two diagrams only:
- Input: the two new `*-v4.html` files in `img/diagrams/`
- Expected output: `*-v4-mobile.html` files in the same folder, following the breakpoint convention used by `diagram-ai06-evaluation-matrix-v4-mobile.html`, `diagram-ai19-attribution-comparison-v4-mobile.html`, `diagram-ai23-trust-comparison-v4-mobile.html`
- The skill handles capture at 6 breakpoints, classifies failures, applies fixes, and hands off to Della for approval
- **Do not skip the mobile-specific media queries.** Case-ai mobile diagrams ship with `@media (max-width: 480px)` rules that restructure layout (stack horizontal rows, shrink padding, reduce font sizes). The audit must produce a mobile HTML that degrades gracefully at 320px.

---

## Step 5 — Wire `.diagram-pair` into `case-ai.html`

Replace the two `<div class="img-placeholder">` blocks with `.diagram-pair` wrappers matching the ai-06/ai-19/ai-23 pattern.

**Current state — line 222:**
```html
<div class="case-img-full">
  <div class="img-placeholder">Failure state — suppressed synthesis, source posts displayed with threaded comments as fallback</div>
</div>
```

**Replace with:**
```html
<div class="case-img-full diagram-embed diagram-pair" data-diagram="ai-10">
  <iframe
    class="desktop-variant"
    src="img/diagrams/diagram-ai10-failure-state-v4.html"
    loading="lazy"
    scrolling="no"
    title="Failure state — suppressed synthesis, source posts displayed with threaded comments as fallback"
    style="width: 100%; border: none; border-radius: 12px; overflow: hidden;"
  ></iframe>
  <iframe
    class="mobile-variant"
    src="img/diagrams/diagram-ai10-failure-state-v4-mobile.html"
    loading="lazy"
    scrolling="no"
    title="Failure state (mobile) — stacked fallback panels"
    style="width: 100%; border: none; border-radius: 12px; overflow: hidden;"
  ></iframe>
</div>
```

**Current state — line 298:**
```html
<div class="case-img-full">
  <div class="img-placeholder">Final identification system — persistent elements (color, name, separation) applied across multiple Reddit surfaces</div>
</div>
```

**Replace with:**
```html
<div class="case-img-full diagram-embed diagram-pair" data-diagram="ai-16">
  <iframe
    class="desktop-variant"
    src="img/diagrams/diagram-ai16-final-identification-v4.html"
    loading="lazy"
    scrolling="no"
    title="Final identification system — persistent elements applied across Reddit surfaces"
    style="width: 100%; border: none; border-radius: 12px; overflow: hidden;"
  ></iframe>
  <iframe
    class="mobile-variant"
    src="img/diagrams/diagram-ai16-final-identification-v4-mobile.html"
    loading="lazy"
    scrolling="no"
    title="Final identification system (mobile) — persistent elements, compact layout"
    style="width: 100%; border: none; border-radius: 12px; overflow: hidden;"
  ></iframe>
</div>
```

**Verify the `data-diagram` values don't collide with existing ones.** The existing `data-diagram` values in case-ai.html follow `ai-NN` format (two-digit zero-padded). Grep before committing to confirm.

---

## Step 6 — Figma desktop frame on `29:42`

Page `29:42` of file `TArUrZsBUocaAsqetjXq7V` holds all case-ai desktop frames. Naming convention: `AI-NN — <Title>` (e.g., `AI-19 — Attribution Comparison`).

For each new diagram:
1. Read the desktop frame positions of nearby frames (`AI-09`, `AI-11`, `AI-14`, `AI-15`) to determine where `AI-10` slots in visually on the canvas. Same for `AI-16` relative to `AI-15` and `AI-19`.
2. Invoke `html-to-figma` skill with `mode: native` on the new `*-v4.html` file. Target: create a new frame on page `29:42`, named `AI-10 — Graceful Degradation` and `AI-16 — Final Identification`.
3. Use `get_metadata` on the neighbor frames to look up their `x`/`y` to position the new frame in narrative order.
4. **Do NOT run `tidyPage` on `29:42`.** The case-ai cluster is hand-positioned. Place new frames at intentional coordinates and leave every other frame alone.
5. Verify via `get_screenshot`.

---

## Step 7 — Figma mobile frame at `x = -420`

Mobile cluster anchor on page `29:42` is `x = -420` (locked by Session 4 v0.2.1 algorithm, respected by all 19 existing mobile frames).

For each new diagram:
1. Invoke `html-to-figma` skill with `mode: native` on the new `*-v4-mobile.html` file.
2. Name: `ai10-mobile` and `ai16-mobile` (matches the mobile-naming convention from Sessions 10–14).
3. Place at `x = -420`, `y` matching the corresponding desktop frame's `y` on the page.
4. CSS-selector layer names throughout (e.g., `.failure-panel.suppressed`, `.identification-card.persistent`) — required for `figma-to-html` roundtrip.
5. Verify via `get_screenshot` before updating tracker.

See Session 14 BUILD-LOG entry for the 9 native-build technique notes (font styles with spaces, `layoutMode='NONE'` for non-linear composition, atob() runtime workaround, setCurrentPageAsync requirement, etc.).

---

## Step 8 — Tracker rows

Add two rows to `working/mobile-audit/audit-tracker.xlsx` via `tracker-helpers.py` (openpyxl-atomic — never pandas):

```bash
cd ~/CoworkWorkspace/Get-a-job/portfolio-site
python3 -c "
import importlib.util
spec = importlib.util.spec_from_file_location('th', 'working/mobile-audit/scripts/tracker-helpers.py')
th = importlib.util.module_from_spec(spec)
spec.loader.exec_module(th)

# Upsert ai10
th.upsert_row('working/mobile-audit/audit-tracker.xlsx', 'ai10', {
    'case_study': 'case-ai',
    'diagram_title': 'Graceful Degradation — failure state',
    'desktop_file': 'img/diagrams/diagram-ai10-failure-state-v4.html',
    'mobile_file': 'img/diagrams/diagram-ai10-failure-state-v4-mobile.html',
    'figma_desktop_node_id': '<NEW_DESKTOP_ID>',
    'figma_mobile_node_id': '<NEW_MOBILE_ID>',
    'status': 'complete',
})

# Upsert ai16
th.upsert_row('working/mobile-audit/audit-tracker.xlsx', 'ai16', {
    'case_study': 'case-ai',
    'diagram_title': 'A System, Not a Solution — final identification',
    'desktop_file': 'img/diagrams/diagram-ai16-final-identification-v4.html',
    'mobile_file': 'img/diagrams/diagram-ai16-final-identification-v4-mobile.html',
    'figma_desktop_node_id': '<NEW_DESKTOP_ID>',
    'figma_mobile_node_id': '<NEW_MOBILE_ID>',
    'status': 'complete',
})
"
```

**Before running: check the tracker's actual column schema with `th.read_tracker(...)` — mirror the existing case-ai rows exactly.** Session 14 flagged `ai11` for tracker drift; don't introduce new drift.

---

## Step 9 — Quality gates (mandatory, do not skip)

```bash
cd ~/CoworkWorkspace/Get-a-job/portfolio-site

# HTML/CSS/a11y validator
python3 quality-check.py

# Voice linter (runs against voice-rules/banned-patterns.yaml)
python3 voice-check.py case-ai.html
```

Both must pass before committing. If either flags an issue, fix it before proceeding.

---

## Step 10 — Show diffs + push

Never commit without Della's explicit approval. After all Steps 1–9 are clean:

1. `git diff` the modified files — show Della the full diff of `case-ai.html` plus the two new `img/diagrams/*-v4*.html` files.
2. Confirm: "Ready to commit and push to `main`?"
3. On approval:
   ```bash
   cd ~/CoworkWorkspace/Get-a-job/portfolio-site
   git add case-ai.html img/diagrams/diagram-ai10-failure-state-v4.html img/diagrams/diagram-ai10-failure-state-v4-mobile.html img/diagrams/diagram-ai16-final-identification-v4.html img/diagrams/diagram-ai16-final-identification-v4-mobile.html
   git commit -m "case-ai: add ai10 (graceful degradation) and ai16 (final identification) with mobile pairs"
   ```
   Show Della the push command — do not push from sandbox.

---

## Step 11 — Live verification

After Della pushes and Cloudflare/GitHub Pages re-deploys:

1. Open Chrome, navigate to the live case-ai URL.
2. Use **Chrome DevTools device emulation** (not Chrome MCP `browser_batch`, per SESSION-STATE note about 500px floor) at widths: 320, 375, 414, 430, 500, 768, 1024, 1440.
3. At each width, scroll through case-ai and confirm:
   - The ai10 and ai16 embeds render correctly
   - The correct variant shows (mobile ≤500px, desktop >500px — or whatever the case-ai `.diagram-pair` CSS breakpoint actually is — verify by reading the CSS)
   - No layout shift, no clipping, no scrollbars inside the iframes
4. Take screenshots at 320 and 1440 for each diagram — save to `working/mobile-audit/case-ai-ai10-ai16-live-verify/` and show Della.
5. If anything looks wrong, fix and re-deploy.

---

## Step 12 — Close the loop

1. **`figma-handoff-case-ai.md`**: append a new entry listing the two new node IDs and their status. The current version should already have the 19-row table from Session 14; extend it to 21 rows.
2. **`BUILD-LOG.md`**: append a Session 15 entry following the Session 10/11/12/14 pattern. Include:
   - Narrative (1–2 paragraphs)
   - Figma state table for the two new entries
   - Any new technique quirks discovered
   - Files touched (list all 5 new HTML files + `case-ai.html` + tracker + handoff doc)
   - Why this matters (case-ai now fully complete, 21/21 diagrams with desktop + mobile + Figma pairs)
   - Next steps (if any open items surfaced)
3. **`SESSION-STATE.md`**: update the case-ai block to say "21/21 complete, all mobile-paired, all Figma-paired." Bump "Last updated" header.
4. **Tracker**: confirm both new rows have `figma_mobile_node_id` AND `figma_desktop_node_id` populated.
5. Show Della the final commit diff, the live verification screenshots, and the BUILD-LOG/SESSION-STATE updates in one summary message.

---

## Hard constraints (non-negotiable)

1. **Native layers only for Figma.** Every Figma frame must be real auto-layout + text + vectors + rectangles, fully editable. No `createImage` + fill. (Same rule as Sessions 10–14.)
2. **No `tidyPage` on page `29:42`.** The case-ai cluster is hand-positioned. New frames at intentional coordinates; everything else untouched.
3. **No edits to existing `AI-*` desktop frames or existing mobile frames.** Only adding new ones.
4. **No fabrication.** If v3 HTML is missing content, ask Della — do not invent metrics, captions, or visual elements. Source Verification Rule applies.
5. **Tracker writes via `tracker-helpers.py` openpyxl.** Never pandas.
6. **CSS-selector layer names throughout Figma builds.** Required for roundtrip.
7. **Verify every frame with `get_screenshot` before moving on.** Per-diagram verify-then-update rhythm (Session 14 pattern).
8. **Mutate-then-query pattern for `use_figma`.** Don't throw `DATA:` in the same call as mutations; it rolls them back. (Session 10 BUILD-LOG has the rationale.)
9. **Mac absolute paths in every terminal command.** No `/sessions/*` paths ever shown to Della. PATH-MAPPINGS.md is the source of truth.
10. **Verify-before-claiming.** Render, screenshot, run linters. Don't tell Della "ai10 is live" until you've loaded the live URL and seen it render.

---

## If you discover mid-task that v3 isn't current

If Della indicates the "most current" source is somewhere else (e.g., the 345-line `deliverables/diagram-ai16-final-identification.html`, or a new version she sketched elsewhere), stop and ask which source to promote before doing anything. Do NOT merge versions on autopilot.

---

## Starter message to kick off

After pasting this prompt, wait for Della to either:
- (a) confirm v3 is the intended source for both, or
- (b) point you at a different source file

Then proceed with Step 1 (source review) and present the greenlight gate before touching anything.
