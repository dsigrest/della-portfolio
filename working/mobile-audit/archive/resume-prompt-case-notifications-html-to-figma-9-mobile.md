# Resume Prompt — case-notifications 9 Mobile Figma Frames via `html-to-figma`

**Created:** 2026-04-22 (Session 31 case-notifications Phase 3 close-out — responsive CSS + NOT-11 mobile variant landed as commits `6b5a4d5` + the `.flow` / `.stat-strip` delta. This kickoff hands off pushing the 9 remaining v5 NOT diagrams' mobile-equivalent Figma frames via the `html-to-figma` skill.)
**Status:** ACTIVE — awaiting a fresh thread to execute.
**Predecessor:** None — this is a new scope. Relies on the progress docs + BUILD-LOG entries from Sessions 28–31 for historical context.
**Successor:** omit — terminal handoff for this workstream.
**Retirable when:** all 9 mobile Figma frames exist on the Portfolio Image Inventory file at their assigned mobile-cluster coordinates, each layer tree uses CSS-selector names, each has an animation spec companion frame (if the skill produces one), and the tracker's `figma_mobile_node_id` column is populated for every v5 NOT row.

**Outcome summary:** Session 31 shipped L2 responsive CSS + an L3 NOT-11 mobile HTML variant pulled from pre-existing Figma node `945:17`. The other 9 v5 NOT diagrams have correct mobile HTML but no Figma mobile frame yet. This thread reverses the direction: HTML → Figma, creating new mobile frames so Della can polish visually and round-trip back via `figma-to-html` in a later thread.

---

## TL;DR

Nine v5 NOT diagrams have landed as mobile-ready HTML (single-file responsive with `body.embedded` + grid-collapse `@media (max-width: 600px)`). They don't yet have dedicated mobile Figma frames. This thread uses the `html-to-figma` skill to create one frame per diagram on the same Portfolio Image Inventory file where NOT-11's mobile frame (`945:17`) already lives, positioning each new frame in the mobile cluster (left of the desktop cluster, same row as the corresponding desktop frame).

Expected duration: 90–120 minutes if the html-to-figma skill runs clean per-diagram. Bottleneck is the Figma MCP: frames must be created sequentially via `use_figma` under the alt-namespace `mcp__8e95afc0-...__*` (the `mcp__Figma__*` namespace errors with "enable Dev Mode MCP Server" — confirmed across Sessions 17/18/24/25/27/28/31). Do not batch in parallel.

Chunking recommendation: 3 diagrams per sub-batch. After each 3, re-run `get_metadata` on the parent page to confirm the mobile-cluster column stays coherent (anchor `desktop_base.x - 800` per responsive-audit v0.2.0). Checkpoint and show Della before starting the next batch.

---

## Carry-forward from Sessions 28–31 (what shipped)

Thread state matters for this scope. The mobile HTML files are the source of truth for the Figma translation — their CSS and structure are the input. Confirm the latest version of each file is the one being translated.

**Diagrams in scope (9):**

| Diagram ID | Source HTML file (latest v5) | Grid class collapsed @600 | Special notes |
|---|---|---|---|
| NOT-02 | `img/diagrams/diagram-not02-inbox-row-unit-v5.html` | `.comparison` 2→1 | Pattern proof — verified locally by Della (Session 29) |
| NOT-03 | `img/diagrams/diagram-not03-full-inbox-redesign-v5.html` | `.comparison` 2→1 | Standard retrofit |
| NOT-04 | `img/diagrams/diagram-not04-unread-hierarchy-v5.html` | `.levels-grid` 3→1 | Also hides `.level-labels`; per-card `::before` pseudo injects "1 — Inbox / 2 — Tab / 3 — Row". Embed override uses base `.diagram { width: 100%; max-width: 760px }` — already mobile-safe. |
| NOT-06 | `img/diagrams/diagram-not06-push-to-inbox-v5.html` | `.comparison-strip` 2→1 AND `.flow` column-stacks + `.flow-arrow` hidden (post-Session-31 delta) | 3-card hover flow (PUSH SENT / USER TAPS / INBOX STATE) stacks vertically at 600px |
| NOT-07 | `img/diagrams/diagram-not07-preference-architecture-v5.html` | `.pref-columns` 1fr-auto-1fr → 1fr | Also hides `.transform-arrow` |
| NOT-08 | `img/diagrams/diagram-not08-subreddit-onramps-v5.html` | `.comparison` 2→1 | PNG crop region is Della's Figma task (re-export with different `top:` value) — not in scope here |
| NOT-09 | `img/diagrams/diagram-not09-global-settings-v5.html` | `.compare-area` 2→1 AND `.stat-strip` flex-wraps to 2×2 (post-Session-31 delta) | 4-item structure stats wrap to 2 rows of 2 at 600px |
| NOT-12 | `img/diagrams/diagram-not12-inbox-layout-experiments-v5.html` | `.three-up` 3→1 | Full retrofit |
| NOT-14 | `img/diagrams/diagram-not14-navigation-simplification-v5.html` | `.comparison` 2→1 | Standard retrofit |

**Already done — do NOT re-create:**
- NOT-11 mobile Figma frame at node `945:17` on file `TArUrZsBUocaAsqetjXq7V` — Della built this manually; Session 31 translated it INTO HTML via `figma-to-html`. It's the one counter-example where the direction was Figma → HTML. All 9 above go the opposite direction.

**Tracker state (audit-tracker.xlsx `not11` row as of Session 31):**
- `figma_mobile_node_id = 945:17`
- `mobile_file_path = img/diagrams/diagram-not11-cross-channel-v5-mobile.html`
- Status: `rebuilt-mobile-native`

After this thread, the other 9 v5 NOT tracker rows should have `figma_mobile_node_id` populated with the newly-created node IDs from `html-to-figma`, and notes appended with the date + node ID.

**Figma file + page context:**
- File key: `TArUrZsBUocaAsqetjXq7V` (Portfolio — Image Inventory)
- The case-notifications mobile frames live on the same page as the desktop frames. NOT-11 mobile at `945:17` has `x=-1263, y=12162, width=375, height=720`. The mobile-cluster anchor is at approximately `x = -1263` on that page. Other mobile frames on the same page should align vertically at `x ≈ -1263` (or `desktop_base.x - 800` per responsive-audit config).
- Desktop frames for NOT-02 through NOT-14 live at `x ≈ +437` (typical). Each mobile frame pairs with one desktop frame on the same y-coordinate (or within 100px per the figma-to-html frame-resolution algorithm's row grouping).

---

## Pre-flight reads (mandatory before any work)

1. `/Users/della/CoworkWorkspace/CLAUDE.md` — global voice rules, session protocol, Terminal Command Safety Check, Skill Execution Rule, Figma Plugin API Page Tidying Rule (`tidyPage` function)
2. `/Users/della/CoworkWorkspace/PATH-MAPPINGS.md` — sandbox↔Mac path conversion rule; Figma file key
3. `/Users/della/CoworkWorkspace/Get-a-job/CLAUDE.md` — Living Documents Rule, Verify Before Claiming Rule
4. `/Users/della/CoworkWorkspace/Get-a-job/SESSION-STATE.md` — Session 31 close-out header describes the exact state of the 9 HTML files being translated
5. `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/case-notifications-responsive-fix-progress.md` — full history of the responsive-audit workstream; Session 31 block describes the deltas that landed in the last hour
6. `/Users/della/CoworkWorkspace/Skills/html-to-figma/SKILL.md` — the skill that does the translation; read end-to-end before invoking (do not paraphrase to an agent)
7. `/Users/della/CoworkWorkspace/Skills/html-to-figma/references/` — every file; pay special attention to any `plugin-api-gotchas.md` or Figma node-creation patterns
8. `/Users/della/CoworkWorkspace/Skills/figma-to-html/references/node-identity-mismatch.md` — inverse-direction lesson from Session 31 applies here too: after creating each node, re-fetch `get_metadata` to confirm the frame's `name` matches the claimed diagram ID before moving on
9. `/Users/della/CoworkWorkspace/Skills/responsive-audit/references/v4-embed-retrofit.md` — the three-piece retrofit pattern; the HTML being translated follows this pattern
10. This file — scope definition + 9-row diagram roster

---

## Non-negotiables (carry forward from global + project rules)

- **Figma Dev Mode MCP alt namespace is `mcp__8e95afc0-e30e-4e27-bfa2-90ccd2e7b3a9__*`.** The `mcp__Figma__*` variant errors with "enable Dev Mode MCP Server". Confirmed across 7+ sessions; graduated from "try this" to documented fallback.
- **Figma Plugin API Page Tidying Rule from global CLAUDE.md applies.** Every `use_figma` call that creates or modifies frames on a page MUST call the `tidyPage(page)` function at the end to reposition all top-level children into a clean non-overlapping grid. The exact function is in global CLAUDE.md — copy it verbatim, don't rewrite from memory.
- **Page activation is required before reading `page.children`.** Always `await figma.setCurrentPageAsync(page)` before any read/modify. Without this, `page.children` returns empty on non-active pages.
- **Never delete or reparent existing frames.** Especially NOT-11's mobile at `945:17` and every desktop NOT frame. Create new frames alongside — don't mutate existing ones.
- **Node-identity verification after creation.** For every newly-created frame, re-fetch via `get_metadata` to confirm `name` matches the claimed diagram ID (e.g., "not06 — Push-to-Inbox Continuity (Mobile)"). Log the node ID for the tracker update.
- **Tracker writes are atomic openpyxl via `scripts/tracker-helpers.py`.** Never pandas. Call `th.update_row(path, diagram_id, {'figma_mobile_node_id': ..., 'notes': existing + append})`.
- **Mac absolute paths only in terminal commands.** Never `/sessions/...`.
- **File-specific `git add` per file; no `git add -A`.**
- **No commits from sandbox.** All git commands go to Della.
- **Skill execution — read files, don't summarize.** If delegating to an agent, the agent prompt must include the literal path of `Skills/html-to-figma/SKILL.md` and its `references/` files with "read before starting."
- **Animation spec companion (if html-to-figma produces one).** Per the responsive-audit v0.2.0 convention, each mobile frame gets an animation spec companion frame adjacent. Preserve this pattern.

---

## Start here (thread kickoff flow)

1. Read the pre-flight files (above, in order).
2. Confirm the 9 HTML source files are at their latest state — `cd /Users/della/CoworkWorkspace/Get-a-job/portfolio-site && git log --oneline -10 img/diagrams/` should show the Session 31 commits `6b5a4d5` and the `.flow` / `.stat-strip` delta as the most recent touches on the relevant files.
3. Ask Della these three upfront (cap at three):
   - Confirm the target Figma page for the mobile frames — should they go on the same page as the desktop NOT frames (inferred from NOT-11's mobile at `945:17`), or on a separate mobile-only page? The responsive-audit v0.2.0 convention says same-page-with-mobile-cluster, so default to that unless Della says otherwise.
   - Should the animation spec companion frames be created this thread, or deferred? NOT-11's mobile (`945:17`) doesn't appear to have one — confirm whether that's the convention or an oversight.
   - Batch size and approval cadence — 3 per sub-batch then show-and-wait, or all 9 end-to-end with a final review?
4. For each of the 9 diagrams (in the order of the roster table above):
   - Invoke the `html-to-figma` skill with the source HTML path + target page ID + desktop frame's y-coordinate (for row alignment).
   - Skill produces a new mobile frame; capture its node ID.
   - Re-fetch `get_metadata` on the new node to verify `name` matches the claimed diagram ID.
   - `tidyPage(page)` at the end of each `use_figma` call to keep the canvas clean.
   - Update the corresponding tracker row atomically: `figma_mobile_node_id = <new node ID>`, append notes with date + source file path.
5. After each sub-batch, run the "Ship criteria per frame" checklist below. If anything fails, resolve before starting the next batch.
6. After all 9 are done, run the scope-level ship criteria. Re-fetch page metadata to confirm all 10 mobile frames (NOT-11's `945:17` + 9 new) align in a single mobile cluster column.
7. Close out per the close-out steps below.

---

## Key reference tables

### Figma file + page

- **File key:** `TArUrZsBUocaAsqetjXq7V`
- **File name:** Portfolio — Image Inventory
- **Target page:** same page as NOT-11 mobile (`945:17`). Fetch via `get_metadata(fileKey=..., nodeId="945:17")` and inspect the `.parent` or page reference.

### NOT-11 mobile anchor (reference — do not modify)

| Property | Value |
|---|---|
| Node ID | `945:17` |
| Frame name | `not11 — Cross-Channel Model` |
| x | -1263 |
| y | 12162 |
| width | 375 |
| height | 720 |

Other 9 mobile frames should align at `x ≈ -1263` and at y-coordinates matching their desktop-frame siblings on the same page.

### Per-diagram source HTML roster (re-confirmed before translation)

| # | Diagram ID | Source HTML (Mac absolute) | Desktop frame name (Figma pattern) |
|---|---|---|---|
| 1 | NOT-02 | `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/img/diagrams/diagram-not02-inbox-row-unit-v5.html` | `NOT-02 — Inbox Row Unit` (check Figma for exact) |
| 2 | NOT-03 | `.../img/diagrams/diagram-not03-full-inbox-redesign-v5.html` | `NOT-03 — Full Inbox Redesign` |
| 3 | NOT-04 | `.../img/diagrams/diagram-not04-unread-hierarchy-v5.html` | `NOT-04 — Unread Hierarchy` |
| 4 | NOT-06 | `.../img/diagrams/diagram-not06-push-to-inbox-v5.html` | `NOT-06 — Push-to-Inbox Continuity` |
| 5 | NOT-07 | `.../img/diagrams/diagram-not07-preference-architecture-v5.html` | `NOT-07 — Preference Architecture` |
| 6 | NOT-08 | `.../img/diagrams/diagram-not08-subreddit-onramps-v5.html` | `NOT-08 — Subreddit On-ramps` |
| 7 | NOT-09 | `.../img/diagrams/diagram-not09-global-settings-v5.html` | `NOT-09 — Global Settings Rebuild` |
| 8 | NOT-12 | `.../img/diagrams/diagram-not12-inbox-layout-experiments-v5.html` | `NOT-12 — Inbox Layout Experiments` |
| 9 | NOT-14 | `.../img/diagrams/diagram-not14-navigation-simplification-v5.html` | `NOT-14 — Navigation Simplification` |

### Tracker update pattern per diagram

```python
import importlib.util
spec = importlib.util.spec_from_file_location('tracker_helpers', '/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/scripts/tracker-helpers.py')
th = importlib.util.module_from_spec(spec)
spec.loader.exec_module(th)

TRACKER = '/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/audit-tracker.xlsx'

# Per diagram — load current notes, append session note
rows = th.read_tracker(TRACKER)
current = next(r for r in rows if r['diagram_id'] == 'not02')  # swap ID per diagram
existing_notes = current.get('notes') or ''
append = f' | 2026-04-22 (Session 32): Mobile Figma frame created via html-to-figma from {source_path}. Node: {new_node_id}. Cluster x=-1263, y={y_coord}.'
th.update_row(TRACKER, 'not02', {
    'figma_mobile_node_id': new_node_id,
    'notes': existing_notes + append,
})
```

---

## Ship criteria

### Per-frame ship criteria

A mobile Figma frame is "shipped" when:

- [ ] Frame exists on the target page at the expected `x ≈ -1263` and y-coordinate within 100px of its desktop sibling
- [ ] Frame name matches the pattern `notXX — <Diagram Title> (Mobile)` or consistent with NOT-11's `not11 — Cross-Channel Model` convention
- [ ] Layer tree uses CSS-selector names (`.hub`, `.spoke.push`, `.platform-cell:nth(1)`, etc.) — not generic Figma defaults like "Frame 47"
- [ ] Visual fidelity matches the HTML source rendered at 375px width (within ±2px tolerance on major element positions)
- [ ] `get_metadata` on the new node returns the expected frame name and dimensions
- [ ] Tracker row updated atomically with `figma_mobile_node_id` + appended note
- [ ] (Optional if animation spec convention is adopted) Animation spec companion frame created adjacent to the mobile frame

### Scope-level ship criteria

- [ ] All 9 diagrams in the roster have new mobile frames created (NOT-02/03/04/06/07/08/09/12/14)
- [ ] All 10 mobile frames (9 new + NOT-11's `945:17`) align vertically at `x ≈ -1263` on the target page
- [ ] `tidyPage` called at the end of every `use_figma` call — page canvas is clean, no overlapping frames
- [ ] Tracker rows for all 9 have `figma_mobile_node_id` populated
- [ ] SESSION-STATE and BUILD-LOG updated with this session's close-out
- [ ] No Figma edits to existing frames (desktop frames + NOT-11 mobile untouched)
- [ ] This resume prompt archived to `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/archive/`

---

## When you're done (close-out steps)

1. Update `/Users/della/CoworkWorkspace/Get-a-job/SESSION-STATE.md` top paragraph — prepend a "Session XX close-out — 9 mobile Figma frames shipped via html-to-figma" block summarizing frame count, node IDs, page placement. Session 31 narrative stays preserved below.
2. Append to `/Users/della/CoworkWorkspace/Get-a-job/BUILD-LOG.md` with full session entry: per-diagram node ID captured, any html-to-figma gotchas surfaced, tracker writes performed, `tidyPage` behaviors observed.
3. If the thread surfaced a new html-to-figma gotcha (e.g., frame-name inheritance bug, auto-layout edge case, tidyPage interaction with pre-existing frames), capture it to `/Users/della/CoworkWorkspace/Skills/html-to-figma/references/` per the Lessons → Skill References rule in global CLAUDE.md. Bump skill version per semver. Log the capture in BUILD-LOG.
4. Archive this resume prompt:
   - `git mv /Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/resume-prompt-case-notifications-html-to-figma-9-mobile.md /Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/archive/`
5. (Optional) If Della wants to round-trip the new mobile frames back through `figma-to-html` after polishing, the resulting HTML updates would land as a follow-up scope — note that as a deferred item here, not in scope for this thread.

---

## Voice-check note

**Voice-check:** full lint via `portfolio-site/voice-check.py` against `voice-rules/banned-patterns.yaml` (32 banned patterns loaded) — run the lint before any in-place edit to confirm full pass.
