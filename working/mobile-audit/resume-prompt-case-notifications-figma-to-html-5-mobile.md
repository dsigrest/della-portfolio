# Resume Prompt — case-notifications 5 Mobile Variants via `figma-to-html`

**Created:** 2026-04-22 (Session 32 close-out — this is the self-sufficient kickoff for the Session 33+ thread that translates Della's Figma polish back into dedicated mobile HTML variants).
**Status:** ACTIVE — awaiting a fresh thread. Session 32 landed the 5 mobile Figma frames; this prompt picks up after Della's Figma polish pass.
**Predecessor:** `resume-prompt-case-notifications-html-to-figma-9-mobile.md` (Session 31 kickoff, Session 32 executor — retirable now per "Close-out steps" below).
**Successor:** omit — terminal handoff for the case-notifications mobile workstream. If a later phone re-test surfaces residual issues, that spawns a new scope, not a continuation of this one.
**Retirable when:** 5 dedicated `diagram-notNN-v5-mobile.html` files exist in `portfolio-site/img/diagrams/`, `case-notifications.html` wraps each NOT-02/03/08/12/14 embed in `.diagram-pair` matching NOT-11's pattern, Chrome MCP overflow verify returns 10/10 PASS at 375 and 320, tracker rows for NOT-02/03/08/12/14 have `mobile_file_path` populated, and BUILD-LOG + SESSION-STATE reflect the close-out.
**Outcome summary (Session 32, shipped):** 5 new mobile Figma frames on page `29:43` at `x=-1263` — NOT-02 `1131:17`, NOT-03 `1133:17`, NOT-08 `1134:17`, NOT-12 `1137:17`, NOT-14 `1138:17`. Tracker synced (5 appends + 4 updates, 84 rows total). Skill reference `Skills/html-to-figma/references/tracker-helpers-validator-drift.md` v0.1.0 captured; skill bumped v1.1.0 → v1.2.0.

---

## TL;DR

Della polished the 5 new mobile Figma frames Session 32 shipped (PNG imports into `.mock.before-mock` / `.mock.after-mock` placeholders, icon refinement, any hotspot or color tweaks). This thread reverses direction — run `figma-to-html` on each of the 5 polished frames, land 5 dedicated mobile HTML variants in `portfolio-site/img/diagrams/`, wrap each embed in `case-notifications.html` with `.diagram-pair`, and verify at 375/320 via Chrome MCP.

Per the `figma-to-html` skill's canonical batching rule (Max 2 per batch), 5 diagrams = 3 sub-batches (2+2+1). Della's Session 32 cadence answer was "run back-to-back, show after all done" — apply the same cadence here unless she reverses it.

Expected duration: 90–120 minutes. Bottleneck is the Figma MCP (alt namespace `mcp__8e95afc0-e30e-4e27-bfa2-90ccd2e7b3a9__*` — the `mcp__Figma__*` variant errors with "enable Dev Mode MCP Server" per 8 sessions of evidence).

---

## Carry-forward (Session 32 → Session 33)

### The 5 Figma mobile frames (source for figma-to-html)

All on page `29:43` "1. Notifs & Inbox", file `TArUrZsBUocaAsqetjXq7V`, at `x=-1263`.

| Diagram | Node ID | Size | y | Structure notes |
|---|---|---|---|---|
| NOT-02 | `1131:17` | 375×867 | 1507 | `.hover-hint-wrap` + `.comparison-wrap` → stacked `.col.before` / `.col.after`. Each col: `.col-label`, `.screenshot` → `.mock.before-mock` (aspect 1170/247) or `.mock.after-mock` (aspect 520/112), `.annotations` with 4 × `.annotation.problem\|solution:nth(N)` |
| NOT-03 | `1133:17` | 375×1954 | 2592 | Same pattern as NOT-02. Both mocks use full-phone aspect 322/697. 4 annotations per col. |
| NOT-08 | `1134:17` | 375×676 | 9666 | Simpler — `.caption` replaces `.annotations`. Mock aspects 520/150 (before) / 520/197 (after). Bottom `.takeaway` bar with `Pattern shift:` leading phrase. |
| NOT-12 | `1137:17` | 375×890 | 13174 | `.three-up` → 3 × `.card.chronological\|nested\|tabbed`. Each card: `.placeholder` (with `.layout-icon`, `.layout-name`, `.slot-label`, plus `.winner-badge "BEST FIT"` on tabbed only), `.divider`, `.content` (title + 2 `.trait.good\|bad`), `.callout` bottom text. |
| NOT-14 | `1138:17` | 375×2204 | 15043 | `.hover-hint-wrap` + `.comparison-wrap` with `.watermark` JetBrains Mono 140px bold numbers ("5" / "3–4") at opacity 0.08 behind each col. `.count-caption` "DESTINATIONS IN BOTTOM NAV" under mock. 3 annotations per col. |

### Session 32 frame decisions the next thread needs to respect

These decisions were made Session 32 and will be visible in Della's polished frames unless she changed them in her pass:

- **PNG mocks:** built as labeled placeholder frames (#F6F6F6 bg, correct aspect ratio, small text label `[PNG: filename — place manually]`). Della's polish should have replaced these with actual image fills. The HTML the next thread generates should reference the existing PNGs in `portfolio-site/img/diagrams/assets/` (the same PNGs `case-notifications.html`'s desktop diagrams already use).
- **Hotspot overlays:** not created in the Session 32 frames (they're opacity:0 in the HTML + pixel-positioned against PNG content). If Della added them in her polish pass, preserve them in the HTML translation. If not, skip — they're hover-only decoration.
- **Animation spec companions:** not created at x=-1263. Existing anim-specs at x=-420 cover both desktop and mobile. If Della added new ones during polish, the translation thread does NOT need to incorporate them — those are Figma-only reference artifacts.

### Matching pattern from Session 31 — NOT-11 precedent

Session 31 already did this exact translation direction for NOT-11 (node `945:17` → `diagram-not11-cross-channel-v5-mobile.html`). Use it as the canonical example for the 5 this thread handles:

- **HTML filename pattern:** `diagram-not{02|03|08|12|14}-<slug>-v5-mobile.html`
- **figma-source meta tag:** `<meta name="figma-source" content="node:NNNN:NN page:29:43 file:TArUrZsBUocaAsqetjXq7V">` stamped per file
- **Embed wrap pattern:** see `case-notifications.html` NOT-11 block — `.diagram-pair` with two iframes, desktop + mobile, swap rule in `styles.css` at `@media (max-width: 768px)`

### Tracker state (already written in Session 32)

9 tracker rows are populated with `figma_mobile_node_id`. The 5 that this thread touches still need `mobile_file_path` set after the HTML lands:

| Diagram | figma_mobile_node_id | mobile_file_path (this thread writes) |
|---|---|---|
| NOT-02 | `1131:17` | `img/diagrams/diagram-not02-inbox-row-unit-v5-mobile.html` |
| NOT-03 | `1133:17` | `img/diagrams/diagram-not03-full-inbox-redesign-v5-mobile.html` |
| NOT-08 | `1134:17` | `img/diagrams/diagram-not08-subreddit-onramps-v5-mobile.html` |
| NOT-12 | `1137:17` | `img/diagrams/diagram-not12-inbox-layout-experiments-v5-mobile.html` |
| NOT-14 | `1138:17` | `img/diagrams/diagram-not14-navigation-simplification-v5-mobile.html` |

Use `th.update_row(TRACKER, 'not02', {'mobile_file_path': '...', 'notes': existing + append})` for each — atomic openpyxl only, never pandas.

### Session 32 gotcha to inherit

The `tracker-helpers.py` `VALID_STATUSES` allowlist is out of sync with the canonical tracker data. If `append_row` throws `Invalid status: rebuilt-mobile-native` on a value that already exists in 9 other rows, bypass via direct openpyxl `ws.append()`. Full detection + fix pattern lives in `Skills/html-to-figma/references/tracker-helpers-validator-drift.md` v0.1.0 (wired into Step 0 of that skill).

This applies to any thread that writes to the tracker — including this one, when populating `mobile_file_path` via `update_row` (which only validates the updates dict, not the existing row's status — so `update_row` should work cleanly here, but test first).

---

## Pre-flight reads (mandatory — in order)

1. `/Users/della/CoworkWorkspace/CLAUDE.md` — global voice rules, Skill Execution Rule, Terminal Command Safety Check, Figma Page Tidying Rule, Lessons → Skill References rule
2. `/Users/della/CoworkWorkspace/PATH-MAPPINGS.md` — sandbox↔Mac conversion; file key `TArUrZsBUocaAsqetjXq7V`
3. `/Users/della/CoworkWorkspace/Get-a-job/CLAUDE.md` — Living Documents Rule, Verify Before Claiming, Source Verification, project voice extensions
4. `/Users/della/CoworkWorkspace/Get-a-job/SESSION-STATE.md` — Session 32 close-out header describes the exact state of the 5 Figma frames
5. `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/case-notifications-responsive-fix-progress.md` — full case-notifications workstream history; Session 31/32 blocks explain the `.diagram-pair` pattern + NOT-11 precedent
6. `/Users/della/CoworkWorkspace/Skills/figma-to-html/SKILL.md` — the skill that does the translation; read end-to-end, do not paraphrase to an agent
7. `/Users/della/CoworkWorkspace/Skills/figma-to-html/references/` — every file. Specifically `node-identity-mismatch.md` v0.1.0 (verify node → diagram pairing before translating) and any `design-system.md` / MCP-namespace references
8. `/Users/della/CoworkWorkspace/Skills/responsive-audit/references/v4-embed-retrofit.md` v0.1.1 — the `body.embedded` + iframe-detection + grid-collapse pattern the mobile HTML must follow
9. `/Users/della/CoworkWorkspace/Skills/html-to-figma/references/tracker-helpers-validator-drift.md` v0.1.0 — if any tracker write throws on status, read this first
10. This file — scope definition + 5-row roster

---

## Non-negotiables

Inherited from Session 32 and prior case-notifications threads. All still apply.

- **Figma Dev Mode MCP alt namespace.** Use `mcp__8e95afc0-e30e-4e27-bfa2-90ccd2e7b3a9__*`. The `mcp__Figma__*` variant errors with "enable Dev Mode MCP Server" across 8 sessions of evidence — this is documented fallback, not a try-this.
- **Node-identity verification before translating.** Fetch `get_metadata` on each target node first, confirm the returned frame name matches the claimed diagram ID. See `Skills/figma-to-html/references/node-identity-mismatch.md`.
- **No existing-frame mutations.** Read-only on the Figma side for this scope. No edits to the 5 frames, no edits to desktop frames, no edits to NOT-11's `945:17` anchor, no edits to anim-specs at x=-420, no edits to x=-1700 cluster frames.
- **Mac absolute paths only in terminal commands.** Convert sandbox `/sessions/*/mnt/*` paths before emitting anything for Della to run. Never show `/sessions/` in commands.
- **File-specific `git add` per file.** No `git add -A` or `git add .`.
- **No commits from sandbox.** Emit git commands for Della to run.
- **Atomic openpyxl tracker writes.** Use `th.update_row` via the `tracker-helpers.py` loader pattern. Never pandas.
- **Skill execution rule.** Read the actual skill files; do not summarize them to an agent. Any delegated sub-agent prompt must include the literal `Skills/figma-to-html/SKILL.md` path with "read before starting."
- **Voice + quality gates.** Run `portfolio-site/voice-check.py` and `portfolio-site/quality-check.py` on every new HTML file. Both must pass 0 errors before handoff to git.
- **Verify before claiming.** No "it renders clean at 375" without actually running Chrome MCP overflow measurement. The pattern from Session 31: `python3 -m http.server 8765` via Desktop Commander on Della's Mac + local verify tracker + `javascript_tool` exec via Chrome extension.
- **Living documents.** SESSION-STATE.md, BUILD-LOG.md, `case-notifications-responsive-fix-progress.md` are additive-update only. Never rewrite from scratch.

---

## Start here (thread kickoff flow)

1. **Read the pre-flight files** in order. No exceptions.
2. **Confirm Della's Figma polish landed on all 5 frames.** Fetch `get_metadata` on `1131:17`, `1133:17`, `1134:17`, `1137:17`, `1138:17`. For each, compare the returned frame name against the expected diagram ID per the Carry-forward table. If any mismatch, stop and surface to Della before translating (per `node-identity-mismatch.md`).
3. **Ask Della three upfront:**
   - "Did you import PNGs into the `.mock.before-mock` / `.mock.after-mock` frames? If yes, should the HTML reference the existing portfolio PNGs (e.g., `assets/not02-legacy-inbox.png`) or new exports you did during polish?"
   - "Did you add hotspot overlays, refine icons, or change colors during polish? Anything I need to preserve in the HTML that wasn't in the Session 32 skeleton?"
   - "Batch cadence — 2 per batch back-to-back with one final review, or show after each batch?"
4. **For each of the 5 diagrams, in this order: NOT-02 → NOT-03 → NOT-08 → NOT-12 → NOT-14** (matches existing y-order on the Figma page):
   - Run `figma-to-html` skill Mode B (single-node translation per the skill's documented flow).
   - Output file: `portfolio-site/img/diagrams/diagram-not{NN}-<slug>-v5-mobile.html` matching the naming in the tracker's `mobile_file_path` column (see Carry-forward).
   - Stamp `figma-source` meta tag: `node:NNNN:NN page:29:43 file:TArUrZsBUocaAsqetjXq7V`.
   - Apply the v4 embed-retrofit three-piece pattern per `Skills/responsive-audit/references/v4-embed-retrofit.md` v0.1.1 — `body.embedded` CSS block, iframe-detection one-liner, `@media (max-width: 600px)` grid collapse (though for a dedicated mobile file, the grid is already single-column — the body chrome strip is what matters).
   - Use workspace design-system tokens from `Skills/figma-to-html/references/design-system.md`. Do not substitute Figma's slightly-brighter hex values.
5. **After each diagram:**
   - Run `portfolio-site/voice-check.py` — PASS required.
   - Run `portfolio-site/quality-check.py` — PASS required.
   - Update tracker row atomically: `th.update_row(TRACKER, 'not{NN}', {'mobile_file_path': 'img/diagrams/diagram-not{NN}-<slug>-v5-mobile.html', 'notes': existing + append})`.
6. **After all 5 HTMLs land:**
   - Edit `portfolio-site/case-notifications.html` to wrap each NOT-02/03/08/12/14 iframe embed in `.diagram-pair` matching NOT-11's existing block. Preserve the desktop iframe, add a mobile iframe sibling pointing at the new `-mobile.html` file.
   - Verify the swap rule in `portfolio-site/css/styles.css` still handles all 6 pairs (NOT-11 plus the 5 new). The existing `@media (max-width: 768px)` rule at L370-377 (per Session 31 notes) targets `.diagram-pair .desktop-only` and `.diagram-pair .mobile-only` — should apply universally, but confirm by inspecting CSSOM.
7. **Chrome MCP overflow verify — 10 checks minimum.** Start `python3 -m http.server 8765` via Desktop Commander on Della's Mac. Point a verify tracker at `http://localhost:8765/working/mobile-audit/session33-local-verify.html` (create it fresh, 5 iframes × 2 widths = 10 cells). Execute the overflow snippet via Chrome extension's `javascript_tool`: `document.body.scrollWidth - document.body.clientWidth === 0` at 375 AND 320 for every diagram. All 10 must PASS.
8. **Close out per the close-out steps below.**

---

## Key reference tables

### Figma file + page

| Property | Value |
|---|---|
| File key | `TArUrZsBUocaAsqetjXq7V` |
| File name | Portfolio — Image Inventory |
| Target page ID | `29:43` |
| Target page name | "1. Notifs & Inbox" |
| MCP namespace | `mcp__8e95afc0-e30e-4e27-bfa2-90ccd2e7b3a9__*` |

### `.diagram-pair` wrap pattern (reference: NOT-11 in `case-notifications.html`)

The existing NOT-11 block in `case-notifications.html` is the canonical example. Inspect it via grep:

```bash
cd ~/CoworkWorkspace/Get-a-job/portfolio-site
grep -n -A 8 'diagram-pair.*not11' case-notifications.html
```

Apply the same wrap to each of NOT-02/03/08/12/14. The desktop iframe already exists in the file; add the mobile sibling + wrap both in `.diagram-pair`.

### Tracker update pattern per diagram

```python
import importlib.util
spec = importlib.util.spec_from_file_location(
    'tracker_helpers',
    '/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/scripts/tracker-helpers.py'
)
th = importlib.util.module_from_spec(spec)
spec.loader.exec_module(th)

TRACKER = '/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/audit-tracker.xlsx'

# Per diagram — read current notes, append session note, update
rows = th.read_tracker(TRACKER)
row = next(r for r in rows if r['diagram_id'] == 'not02')  # swap per diagram
existing = row.get('notes') or ''
append = f' | 2026-04-22 (Session 33): Mobile HTML variant via figma-to-html from node 1131:17. Embedded in case-notifications.html via .diagram-pair.'
th.update_row(TRACKER, 'not02', {
    'mobile_file_path': 'img/diagrams/diagram-not02-inbox-row-unit-v5-mobile.html',
    'notes': existing + append,
})
```

If `update_row` throws on status validation, fall back to direct openpyxl per `Skills/html-to-figma/references/tracker-helpers-validator-drift.md`.

### Output filenames (locked)

| Diagram | Mobile HTML filename |
|---|---|
| NOT-02 | `diagram-not02-inbox-row-unit-v5-mobile.html` |
| NOT-03 | `diagram-not03-full-inbox-redesign-v5-mobile.html` |
| NOT-08 | `diagram-not08-subreddit-onramps-v5-mobile.html` |
| NOT-12 | `diagram-not12-inbox-layout-experiments-v5-mobile.html` |
| NOT-14 | `diagram-not14-navigation-simplification-v5-mobile.html` |

---

## Ship criteria

### Per-diagram ship criteria

Each mobile HTML is "shipped" when:

- [ ] File exists at `portfolio-site/img/diagrams/diagram-not{NN}-<slug>-v5-mobile.html`
- [ ] `figma-source` meta tag present with correct node + page + file
- [ ] v4 embed-retrofit three-piece pattern present (`body.embedded` CSS, iframe-detection one-liner, grid-collapse or equivalent — for a dedicated mobile file, the collapse is the default layout)
- [ ] Design-system tokens from workspace reference (not Figma's raw hex values)
- [ ] `voice-check.py` PASS (0 errors; warnings on pre-existing long-sentence content acceptable)
- [ ] `quality-check.py` PASS (0 errors, 0 warnings)
- [ ] Iframe embed wrapped in `.diagram-pair` in `case-notifications.html`
- [ ] Chrome MCP overflow verify PASS at 375 AND 320 (`body.scrollWidth === body.clientWidth` in the iframe)
- [ ] Tracker row has `mobile_file_path` populated; notes append dated and session-tagged

### Scope-level ship criteria

- [ ] All 5 HTMLs exist and individually meet per-diagram criteria
- [ ] `case-notifications.html` has 6 total `.diagram-pair` blocks (NOT-11 existing + 5 new)
- [ ] 10/10 Chrome MCP overflow checks PASS (5 diagrams × 2 widths)
- [ ] SESSION-STATE.md + BUILD-LOG.md updated with session close-out
- [ ] No unintended edits to existing HTMLs (desktop diagrams, other case studies, styles.css untouched unless Session 33 finds a swap-rule gap)
- [ ] No Figma edits — pure read-only on the Figma side
- [ ] Predecessor `resume-prompt-case-notifications-html-to-figma-9-mobile.md` archived
- [ ] This resume prompt archived after final criterion met

---

## Close-out steps (when you're done)

1. **Update `SESSION-STATE.md`** — prepend a Session 33 close-out block to the top paragraph. Preserve Session 32's narrative below it. Use the paste-ready format from `session32-closeout-content.md` as a template if the file is too large to read inline.
2. **Append to `BUILD-LOG.md`** — new Session 33 entry at the top of the rolling log. Include the 5 node-IDs → filename mapping, Chrome MCP verify results, and any gotcha surfaced this session.
3. **Capture any new gotcha** into the relevant skill's `references/` folder per the Lessons → Skill References rule. If `figma-to-html` hits a new failure mode during the 5-frame translation (image-handle edge cases, `.diagram-pair` CSS specificity issues, etc.), write it down before moving on. Bump skill version per semver.
4. **Update `case-notifications-responsive-fix-progress.md`** — additive block documenting the 5 HTML variants shipped + close the "push 10 dedicated mobile Figma frames" deferred item (reduced to 5 per Session 32's scope decision; all 5 now paired HTML-to-Figma roundtripped).
5. **Archive this resume prompt + predecessor:**
   ```bash
   cd ~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit
   git mv resume-prompt-case-notifications-html-to-figma-9-mobile.md archive/
   git mv resume-prompt-case-notifications-figma-to-html-5-mobile.md archive/
   ```
6. **Generate git commands** for Della — file-specific `git add` per new HTML + `case-notifications.html` + tracker + docs. Single commit covering the 5 HTML files is acceptable per Session 31c's end-of-scope pattern. Mac absolute paths only.
7. **Flag any open items** for a follow-on scope — phone re-test after Vercel rebuild stays Della's job unless something surfaces that needs Claude work.

---

**Voice-check:** this file self-checked against the minimal banned-patterns list in `references/voice-compliance.md` (no hedging, no corporate jargon, first-person narrative where applicable, dashes for rhythm, specific over impressive). Lint with `portfolio-site/voice-check.py` against `voice-rules/banned-patterns.yaml` before Della merges.
