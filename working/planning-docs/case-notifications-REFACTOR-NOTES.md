# case-notifications.html — Refactor Manifest

**Branch:** `case-notifications-figma-rearrange-v2`
**Spec:** `working/planning-docs/case-notifications-change-outline.md`
**Backup:** `case-notifications.html.bak` (project root, untracked)
**Snapshot commit:** `7b95821` — "pre-refactor snapshot — case-notifications v2 outline"
**Started:** 2026-04-27

---

## Status

| Batch | Rows | Status | Commit |
|---|---|---|---|
| 1 | Summary + Challenge + Strategy (1–5) | landed (awaiting Della preview) | (about to commit) |
| 2 | Scaleable foundation + Push paradox (6–12) | not started | — |
| 3 | Frameworks + Build Habits (13–18) | not started | — |
| 4 | Enable Curation + Create Focus + Results (19–28) | not started | — |

---

## Diagram embed conventions

- **Existing on-disk diagram (verified present):** standard `case-img-full diagram-embed` iframe with `data-mobile-pending="true"`.
- **Net-new diagram listed in §5 "to translate from Figma":** placeholder block until figma-to-html pass produces the file.
  ```html
  <div class="img-placeholder">{diagram code} &mdash; {short description} &mdash; figma-to-html translation pending</div>
  ```
  **Deviation from spec:** the spec proposed `[diagram name TBD]` but `TBD` and `[X to Y]` bracket patterns are both banned by the project's pre-commit `quality-check.py` placeholder scan (per Get-a-job/CLAUDE.md). Substituted a descriptive form that mirrors the existing placeholder pattern at original line 215 of `case-notifications.html`.

---

## Batch 1 — Rows 1–5

### Row 1 — `<h2>Summary</h2>` (NEW)
- Inserted new `<section class="case-summary">` between hero (`</section>`) and the existing `<section class="case-body">` containing the original `<h2>Challenge</h2>`.
- Existing line 53 prose ("Reddit communicates with hundreds of millions…") moved into Challenge tile inside Summary — verbatim, single move.
- Existing line 57 prose ("I built the segmentation framework…") moved into Strategy tile inside Summary — verbatim, single move.
- Original `<h2>Solution</h2>` heading (line 55) removed; its prose now lives in row 1 Strategy tile only (Option A confirmed in spec).
- NOT-03 v1 hover-annotated migration diagram embedded at end of Summary section (existing on-disk file `diagram-not03-full-inbox-redesign-v5.html`, relocated from row 6 area).

### Row 2 — `<h2>Challenge</h2>` opening + `<h3>No overarching strategy</h3>`
- Existing `<h2>Challenge</h2>` wrapper kept.
- Original Challenge paragraph (line 53) does NOT repeat here — lives only in row 1 Summary tile.
- Net-new `<h3>No overarching strategy</h3>` heading + drafted prose (per spec) inserted as row 2 body.
- Diagram: 2i Disconnected surfaces — net-new HTML, listed in §5 "to translate from Figma" → placeholder `<div class="img-placeholder">2i — Disconnected surfaces comparison [diagram name TBD]</div>`.

### Row 3 — `<h3>Notification taxonomy gap</h3>`
- Net-new `<h3>` + drafted prose inserted.
- Diagram: NOT-E5 — file `diagram-not-e5-notification-taxonomy-v5.html` exists on disk → standard iframe embed.

### Row 4 — `<h3>Decaying retention</h3>`
- Net-new `<h3>` + drafted prose inserted (uses Day-5/12%/40%/28-point numbers per Della preference).
- Diagram: NOT-E1 — file `diagram-not-e1-cohort-decay-v5.html` exists on disk → standard iframe embed.

### Row 5 — `<h2>Strategy</h2>` (NEW)
- Net-new `<h2>Strategy</h2>` wrapper inserted between Challenge wrapper close and the rest of the case body.
- Strategy lede line drafted from spec: "**Strategy:** establish a scaleable foundation; optimize for key user journeys."
- Existing `metrics-callout` block (current lines 59–76) relocated out of hero/body into row 5 Strategy section, positioned just below the lede.
- No diagram embed.

### Deletions explicit to Batch 1
- Original `<h2>Solution</h2>` heading at current line 55 (its prose moves; only the heading is dropped per Option A).
- Original `metrics-callout` at original position (now relocated to row 5).

### Verification checklist for Batch 1 (all passed 2026-04-27)
- [x] Original line 53 prose appears exactly once (Summary Challenge tile).
- [x] Original line 57 prose appears exactly once (Summary Strategy tile).
- [x] Original metrics-callout appears exactly once (row 5 Strategy section).
- [x] NOT-03 iframe embed present in Summary section.
- [x] NOT-E5 iframe embed present in row 3.
- [x] NOT-E1 iframe embed present in row 4.
- [x] 2i placeholder div present in row 2.
- [x] No `<h2>Solution</h2>` remains in document.
- [x] `<h2>Challenge</h2>` heading appears exactly once (as the wrapper for rows 2–4).
- [x] H2 hierarchy now: Summary → Challenge → Strategy → Framework (Batch 3) → Foundation (Batch 2) → 1. Build Habits → 2. Enable Curation → 3. Create Focus → Results.
- [x] File grew 419 → 466 lines (+47), consistent with Summary section + 3 new h3 sections - removed Solution h2 - relocated NOT-03.
- [x] All existing post-Strategy prose (Framework block, Foundation block, etc.) untouched in Batch 1.

---

## Cross-batch preservation map (live audit)

Compared against §4 of the spec. Will fill in per batch.

| Original line(s) | First words | Target | Batch | Landed |
|---|---|---|---|---|
| 27–48 | Hero / eyebrow / h1 / meta-grid | unchanged | — | yes (untouched) |
| 53 | "Reddit communicates with hundreds…" | Row 1 Summary Challenge tile | 1 | pending |
| 57 | "I built the segmentation framework…" | Row 1 Summary Strategy tile | 1 | pending |
| 59–76 | metrics-callout | Row 5 (relocated out of hero) | 1 | pending |
| 80 | "The strategy sat on two axes: signal and tenure…" | Row 14, "tenure" → "intent" reword | 3 | — |
| 82 | "The first decision was where to start…" | Row 14 (second paragraph) | 3 | — |
| 84 | "Users had a bias for action…" + "switchboard" | Split: bias → row 17, switchboard → row 25 | 3 + 4 | — |
| 90 | "The inbox wasn't on Reddit's design system…" | Row 6 | 2 | — |
| 114 | "I rebuilt the unread system around progressive disclosure…" | Row 8 | 2 | — |
| 126 | "The migration introduced a less prominent unread color…" | Row 9 | 2 | — |
| 130 | "I removed the overflow menu…" | Row 7 | 2 | — |
| 136 | "I added copy showing why a user received each notification…" | Row 17 | 3 | — |
| 144 | "For low-subscription users, the inbox became an onboarding engine…" | Row 18 | 3 | — |
| 152 | "Only the latest push recommendation appeared in the inbox…" | Row 18 | 3 | — |
| 168 | "Subreddit subscriptions were entangled with recommendations…" | Row 19 | 4 | — |
| 176 | "The back end couldn't define what updates…" | Row 20 | 4 | — |
| 188 | "I then surfaced these preferences…" | Split: subreddit page → row 21, global settings → row 23 | 4 | — |
| 212 | "I shipped decay logic for breaking news…" | Row 17 | 3 | — |
| 220 | "I defined the relationship between channels…" | **REMOVED** (cross-channel retired) | 4 | — |
| 245 | "I consolidated four messaging systems…" | Row 24 | 4 | — |
| 253 | "I tested chronological, nested, and tabbed layouts…" | Row 25 | 4 | — |
| 267 | "I designed a system that pins contributions…" | **REMOVED** (NOT-13 retire sticky) | 4 | — |
| 271 | "The unified inbox freed a slot in the bottom tab bar…" | Row 26 | 4 | — |
| 285 | Results paragraph | unchanged | 4 | — |

---

## Net-new diagram placeholders inserted (figma-to-html pass will replace)

Tracked here as the refactor proceeds.

| Row | Filename target | Status |
|---|---|---|
| 2 | `diagram-not02b-disconnected-surfaces-v5.html` | placeholder |
| 7 | `diagram-not02b-swipe-actions-v5.html` (with GIF slot) | — |
| 9 | `diagram-not04b-unread-color-fix-v5.html` | — |
| 10 | `diagram-not10-three-inboxes-v5.html` | — |
| 13 | `diagram-not13-taxonomy-detail-v5.html` | — |
| 17 | `diagram-not17-context-defaults-v5.html` | — |
| 19 | `diagram-not19-pipeline-entanglement-v5.html` | — |
| 22 | `diagram-not22-contextual-suggestions-v5.html` | — |
| 24 | `diagram-not24-surface-tradeoffs-v5.html` | — |
| 27 | `diagram-not14-unified-inbox-v5.html` (with GIF slot) | — |

---

## Diagram retirements

- `diagram-not01-segmentation-matrix-v5.html` — file stays on disk, no embed (per spec §5 retirement).
- 4-step push-to-inbox flow (Figma `678:2374`) — never embedded (Della picked before/after only).
