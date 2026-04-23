# Resume prompt — case-sharing close-out

**Goal:** Verify case-sharing is fully paired (HTML + Figma) and close it out in the tracker + status docs. Optionally: per-screen Figma polish if Della wants it.

**Written:** April 22, 2026 (Session 23, post-iframe-fix)

---

## Context (read these first — in this order)

1. `~/CoworkWorkspace/CLAUDE.md` and `~/CoworkWorkspace/Get-a-job/CLAUDE.md` — auto-loaded, contains voice rules + non-negotiables
2. `~/CoworkWorkspace/Get-a-job/PATH-MAPPINGS.md` — required before any terminal command
3. `~/CoworkWorkspace/Get-a-job/SESSION-STATE.md` — Session 23 close-out is the current top paragraph; the iframe-clip fix pushed via commit `d10c24b` on April 22
4. `~/CoworkWorkspace/Get-a-job/BUILD-LOG.md` — Session 14 Thread C close-out (`img/diagrams/diagram-shrXX-<slug>-v4.html` deployed) + Session 18 Thread B close-out (8 native-layer Figma mobile frames on page `29:41` at x=-1300) + Session 21 close-out (shr10 deploy sync)
5. `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/handoff-shr-ui-screens-to-figma.md` — Thread B executed node IDs table

---

## Current state (as of Session 23)

**HTML:** 8 SHR UI responsive v4 files deployed at `~/CoworkWorkspace/Get-a-job/portfolio-site/img/diagrams/diagram-shrXX-<slug>-v4.html`. Single-file responsive pattern using 3 recipes (A: phone + annotations; B: horizontal carousel; C: stacked before/after). Renders clean at 320 / 375 / 1440. No separate `-mobile.html` variants, no `.diagram-pair` wrap needed — Session 21 explicitly decided this.

**Figma:** 8 native-layer mobile frames shipped on page `29:41` ("3. Sharing & embeds") at x=-1300 in file `TArUrZsBUocaAsqetjXq7V`. Frame node IDs:
- `shr01-mobile` = `1011:8`
- `shr02-mobile` = `1028:8`
- `shr06-mobile` = `1041:8`
- `shr07-mobile` = `1043:8`
- `shr08-mobile` = `1047:8`
- `shr10-mobile` = `1066:8` (redesigned to 2×3 stacked grid in Session 18 Thread B + HTML v4 sync in Session 21)
- `shr11-mobile` = `1073:8`
- `shr12-mobile` = `1077:8`

**Tracker:** rows 57–64 in `portfolio-site/working/mobile-audit/audit-tracker.xlsx`. Per Session 18 close-out, these rows have `figma_mobile_node_id` populated, `status=verified`, `verify_date=2026-04-22`.

**Iframe fix (Session 23):** auto-resize script on `case-sharing.html` now uses `ResizeObserver` on the inner `.diagram` — narrow-viewport clipping resolved across all embedded diagrams. Commit `d10c24b` live on della-portfolio.vercel.app.

---

## What to do in this thread

### Step 1 — Verify close-out state (always)

Read the 8 case-sharing SHR UI tracker rows via openpyxl and confirm for each:
- `figma_mobile_node_id` matches the node-ID table above
- `mobile_file_path` is blank (intentional — single-file responsive, no `-mobile.html` variant)
- `status=verified`
- `verify_date=2026-04-22`
- `notes` references "Thread B" or "Thread C"

**If any row is inconsistent:** flip it to the expected state via atomic `update_row` (openpyxl append, never pandas overwrites — see `portfolio-site/working/mobile-audit/scripts/tracker-helpers.py`). Add date-stamped note.

**If all 8 rows match:** no tracker edits needed. Report state as clean.

### Step 2 — Sanity-check deployed files against Figma node IDs (always)

For each of the 8 SHR UI frames, open the Figma mobile node via `use_figma` and spot-check for egregious drift against the deployed HTML at 375. If drift is within visual tolerance (same layout, same copy, same vibe), no action. If there's a significant mismatch (e.g., a component was edited in Figma but not reflected in HTML), flag it in a short drift report at `working/mobile-audit/reports/case-sharing-figma-drift.md`.

Prior context: the 8 Figma mobile frames were built native-layer to mirror the deployed HTMLs. No intentional drift has been logged. This step is defense-in-depth, not expected to find much.

### Step 3 — Update status docs (if all clean)

Once verified, make targeted edits (**never rewrite** — Living Documents Rule):
- `SESSION-STATE.md` — remove case-sharing from any "outstanding" rollup mentions; if there's a mobile-responsiveness status table, mark case-sharing as ✅ CLOSED
- `BUILD-LOG.md` — append a short close-out session entry noting case-sharing fully paired and verified
- `working/mobile-audit/handoff-shr-ui-screens-to-figma.md` — update the STATUS header to note verification pass complete

### Step 4 (OPTIONAL — only if Della explicitly asks) — Per-screen Figma polish

The 8 Figma mobile frames are functional native-layer builds. If Della wants them polished to final-presentation quality (tighter padding, refined typography, color accents matching the deployed HTML's interactive states), this is a `figma-to-html` / `html-to-figma` roundtrip operation:

1. Screenshot each deployed HTML at 375 via Playwright (reference target)
2. Open each Figma mobile frame and compare visually
3. Update Figma frames to match — adjust via `use_figma` with `tidyPage` afterward per CLAUDE.md non-negotiable
4. Screenshot each updated Figma frame via `get_screenshot` for Della approval
5. If Della wants HTML updated back to match Figma polish: invoke `figma-to-html` skill per-frame

**Do not do Step 4 unless Della explicitly asks.** Session 21 decided the current state is shippable.

---

## Constraints

- **Mac-absolute-path rule:** All terminal commands use `~/CoworkWorkspace/Get-a-job/...` paths. Sandbox paths (`/sessions/...`) NEVER shown to Della.
- **Verify before claiming:** Don't report "case-sharing is closed out" without actually reading the tracker rows + confirming the node IDs match.
- **Tracker edits atomic:** openpyxl `load_workbook` → `update_row` → `save`. Never pandas; never full-file rewrites.
- **Living Documents Rule:** `SESSION-STATE.md`, `BUILD-LOG.md`, and `handoff-shr-ui-screens-to-figma.md` get targeted edits, never rewrites.
- **Voice rules apply to any user-facing prose** written into status docs.

---

## Expected output

A fresh thread should close this in under 30 minutes if all 8 tracker rows are already verified:

- Tracker verified clean (report pass/fail per row)
- Figma spot-check clean (report drift or no-drift)
- Three status doc updates (SESSION-STATE, BUILD-LOG, handoff doc)
- A one-paragraph summary to Della: "case-sharing is fully closed out — 8 SHR UI Figma mobile frames verified, tracker rows 57–64 all at status=verified, handoff doc updated. Optional figma polish path documented but not executed."

If drift is found or any rows are inconsistent, surface the delta before making silent fixes — let Della decide.

---

## Not in scope for this thread

- **Not-series diagrams** (not02/03/08/12/14) — separate PNG-transfer thread (`resume-prompt-case-notifications-png-transfer.md`)
- **Case-notifications mobile pairs batch 2** — separate thread (`resume-prompt-case-notifications-mobile-pairs-batch-2.md`)
- **case-subreddit `.diagram-pair` wiring** — separate thread (Session 14 rollup)
- **case-building-portfolio `.diagram-pair` wiring for port-01a/port-03a1/port-03c/port-04b** — separate thread (`resume-prompt-session16-figma-mobile-frames.md` or similar)
- **Iframe-gotchas skill reference capture** (per Session 23 Lessons → Skill References rule) — separate skill-maintenance thread

Keep this thread narrowly scoped to case-sharing close-out only. If adjacent issues surface, log them to the appropriate resume-prompt file; do not expand scope.
