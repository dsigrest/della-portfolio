# Resume prompt — Workstream A: case-subreddit HTML updates to match x=914 Figma

**Copy the block below as the first message in a fresh Cowork thread.**

---

Workstream A kickoff — update the live case-subreddit HTML diagrams to match the polished x=914 Figma styling on page `29:40`. Session 17 shipped the mobile Figma batch (Workstream B) — 6 new native-layer mobile frames at x=-1634. This thread is Workstream A: the HTML-side companion that never ran.

**Background.** Della hand-polished the x=914 frames on Figma page `29:40` (file `TArUrZsBUocaAsqetjXq7V`, "4. Subreddit Success"). These polished frames are the source of truth for visual styling. The live HTMLs in `portfolio-site/img/diagrams/` still reflect the older desktop styling — primarily carrying visual elements Della deliberately stripped during polish. This thread closes the gap: make each live HTML match its x=914 Figma counterpart.

**Goal.** For each of the 11 case-subreddit diagrams, compare the live HTML against its x=914 Figma frame and update the HTML to match. Primarily this is about **removing elements Della stripped** — not adding. Could also include spacing tweaks, type-scale shifts, or color adjustments the polish introduced.

**Scope — 11 diagrams.** Figma frame names and node IDs (x=914 column on page `29:40`, verified via read-only introspection on 2026-04-22):

| # | Figma node ID | Figma frame name | y | Live HTML |
|---|---|---|---|---|
| 1 | `678:5` | SUB-01a — The 21-Day Cliff | 318 | `portfolio-site/img/diagrams/diagram-sub01-survival-curve.html` |
| 2 | `678:259` | SUB-02a — Lifecycle Framework | 1674 | `portfolio-site/img/diagrams/diagram-sub02-lifecycle-framework.html` |
| 3 | `678:490` | SUB-03a — Milestone Model | 2525 | `portfolio-site/img/diagrams/diagram-sub03-milestone-model.html` |
| 4 | `678:625` | SUB-04a — Strategic Starting Points | 3514 | `portfolio-site/img/diagrams/diagram-sub04-strategic-starting-points.html` |
| 5 | `678:700` | SUB-05a — Shared Artifacts | 4351 | `portfolio-site/img/diagrams/diagram-sub05-artifact-alignment.html` |
| 6 | `678:822` | SUB-06a — Threshold Calibration | 5309 | `portfolio-site/img/diagrams/diagram-sub06-threshold-calibration.html` |
| 7 | `678:924` | SUB-08b — Creation After | 7735 | `portfolio-site/img/diagrams/diagram-sub08-creation-after.html` |
| 8 | `678:1056` | SUB-09c — Distribution Loop | 8534 | `portfolio-site/img/diagrams/diagram-sub09-distribution-loop.html` |
| 9 | `678:1196` | SUB-11t — Three Pillars | 15430 | `portfolio-site/img/diagrams/diagram-sub11-text-bars.html` ⚠️ legacy filename (actual content is three-pillars, not text-bars) |
| 10 | `678:1249` | SUB-12c — Instrumentation Heatmap | 16145 | `portfolio-site/img/diagrams/diagram-sub12-instrumentation-interactive.html` |
| 11 | `678:1367` | SUB-12t — Text Bars | 17134 | `portfolio-site/img/diagrams/diagram-sub12-text-bars.html` |

All 11 x=914 frames confirmed present on page `29:40`. Dimensions are 760 wide with variable height (190–600). Node IDs above are stable and can be used directly in `get_screenshot` / `get_metadata` calls.

**Legacy filename flag (do NOT fix in this thread):** `diagram-sub11-text-bars.html` contains the three-pillars diagram, not text-bars content. This predates the current Figma naming. Leave the filename alone in Workstream A — just polish the contents to match `SUB-11t — Three Pillars`. A separate filename-hygiene thread can handle the rename + iframe reference sweep.

**Workflow per diagram (one at a time, no batch edits):**

1. **Read the x=914 Figma frame.** Use `get_screenshot` + `get_design_context` (or `get_metadata` for structure) to inventory what's present. Note what's missing compared to the live HTML — that's the strip list.
2. **Read the live HTML file** and render it to a screenshot (render-at-1440 or headless Chromium to match desktop). Store both screenshots for diff.
3. **Produce a visual diff summary** — what exists in the HTML that's NOT in the x=914 Figma. Share it with Della before touching the HTML. Do not edit on autopilot.
4. **Get explicit approval** on the strip list per diagram. Della may want to keep some things even if Figma doesn't have them, or the frame may be mid-polish.
5. **Edit the HTML** (inside the diagram's own `<style>` block — no structural rewrites, no new HTML files). Save.
6. **Screenshot-verify the updated HTML** at 1440, 1024, 768, 480, 375, 320. Regression check against `working/mobile-audit/audit-tracker.xlsx` — all 10 case-subreddit rows are `status=verified` at 6 breakpoints; don't ship anything that breaks an existing pass.
7. **Update tracker** via `scripts/tracker-helpers.py` (openpyxl atomic). Append a note to the relevant row: `Workstream A — polished to match Figma x=914 frame [frame-id] on [date]`. Do NOT change `status` away from `verified` unless a breakpoint regressed.
8. **Move to the next diagram.** Do not batch.

**Non-negotiables:**

1. **No edits to Figma.** This thread is HTML-only. The x=914 frames are the reference; they don't change.
2. **No structural HTML changes.** CSS edits inside the existing `<style>` block only. Removing elements means removing the corresponding HTML tags — but no new layouts, no framework additions, no inline script changes.
3. **Per-diagram approval gate.** Never strip elements without showing Della the diff summary and getting an explicit go-ahead. Session 17's Workstream B had a pattern-approval gate at frame #1; this thread uses the same pattern at each of the 11 diagrams.
4. **Preserve voice-check.py + quality-check.py passes.** After each HTML edit, run both linters. Don't ship a regression.
5. **Regression-check recruiter panel.** If any text content changes as part of the polish (not just visual stripping), run `recruiter-panel` on `case-subreddit.html` before declaring the diagram done. Score baseline is in `working/planning-docs/recruiter-panel-eval.md`.
6. **Tracker writes via `scripts/tracker-helpers.py` openpyxl atomic.** Never pandas. Living-documents rule.
7. **No `diagram-deploy` runs yet.** This thread updates source HTMLs. Deploy to live site is a separate thread (or confirmed via a lightweight `git push` after all 11 pass).

**Mandatory pre-work:**

- Read `/Users/della/CoworkWorkspace/CLAUDE.md` and `/Users/della/CoworkWorkspace/Get-a-job/CLAUDE.md` — voice rules, verify-before-claiming, living-documents rule, terminal-command safety check.
- Read `/Users/della/CoworkWorkspace/PATH-MAPPINGS.md` — all terminal commands must use Mac absolute paths.
- Read `/Users/della/CoworkWorkspace/Get-a-job/SESSION-STATE.md` — Session 17 top block summarizes Workstream B state and flags this thread as Workstream A.
- Read `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/figma-handoff-case-subreddit.md` — includes the Session 17 addendum with mobile pattern + hue palette + build-protocol learnings.
- If Della's voice-rules linter is involved (any text changes): `cd portfolio-site && python3 voice-check.py [file]`.

**Verification before reporting done (per diagram):**

- Live HTML visually matches x=914 Figma frame at desktop breakpoint — Della confirms via side-by-side screenshot comparison.
- `voice-check.py`, `quality-check.py` pass.
- All 6 breakpoint screenshots render without regression from the Session 11 verified state.
- Tracker row updated with Workstream A note.
- `recruiter-panel` score on `case-subreddit.html` unchanged or improved (if text touched).

**Deliverables in chat:**

- Per-diagram visual diff summary (before → after screenshots side-by-side).
- Per-diagram strip list — explicit, reviewed by Della before HTML edit.
- Final updated tracker row dump (11 rows with Workstream A notes appended).
- Any Figma-side anomalies discovered (frame missing, partial polish, naming mismatch) — flagged as a follow-up for Della to address in Figma directly, not fixed in this thread.
- A brief session close-out entry written directly into `BUILD-LOG.md` labeled Workstream A, matching the Session 17 entry's structure. Additive, no rewrites. Use the session number assigned at thread start (whatever comes after the current top of SESSION-STATE.md).

**Out of scope for this thread:**

- Any Figma edits (desktop or mobile, any page).
- New mobile HTML files or responsive-audit work.
- Deploy to production (separate thread after all 11 pass).
- Touching case-subreddit.html itself — only the 11 diagram HTMLs.
- Any other case study (case-ai, case-notifications, case-sharing, case-building-portfolio).
- **HTML filename renames.** `diagram-sub11-text-bars.html` contains three-pillars content but keeps its legacy name for this thread. Rename sweep is a separate follow-up.

**Stop conditions — surface to Della and wait, don't self-resolve:**

- Any x=914 frame doesn't exist on page `29:40` or the mapping above is wrong.
- An HTML edit would require structural changes (new layout, new framework) — that's a re-design, not a polish-pass.
- `recruiter-panel` regresses on any diagram.
- Any breakpoint regresses from the Session 11 verified state.
- Any ambiguity in the strip list — Della's call, not the thread's.
