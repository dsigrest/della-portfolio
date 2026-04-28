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
| 1 | Summary + Challenge + Strategy (1–5) | landed | `aa0aee0` |
| 2 | Scaleable foundation + Push paradox (6–12) | landed | `d9abc38` |
| 3 | Frameworks + Build Habits (13–18) | landed | `b0198d2` |
| 4 | Enable Curation + Create Focus + Results (19–28) | landed (awaiting Della preview) | (about to commit) |

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

## Batch 2 — Rows 6–12

### Row 6 — `<h2>Scaleable foundation</h2>` opening + `<h3>Inbox row component</h3>`
- Renamed existing `<h2>Foundation</h2>` → `<h2>Scaleable foundation</h2>`.
- Renamed `<h3>Design system migration</h3>` → `<h3>Inbox row component</h3>`.
- Existing line 90 prose ("The inbox wasn't on Reddit's design system…") preserved verbatim under new heading.
- NOT-02 embed retained in place; added `data-mobile-pending="true"` per §6.

### Row 7 — `<h3>Swipe actions</h3>`
- Renamed `<h3>Inbox simplification</h3>` → `<h3>Swipe actions</h3>` AND moved up to sit between row 6 and row 8 (was after Unread color paragraph in original).
- Existing line 130 prose ("I removed the overflow menu…") preserved verbatim.
- 7i placeholder inserted (figma-to-html pending; container will include GIF placeholder slot).

### Row 8 — `<h3>Unread hierarchy</h3>`
- Renamed `<h3>Unread system redesign</h3>` → `<h3>Unread hierarchy</h3>`.
- Existing line 114 prose ("I rebuilt the unread system around progressive disclosure…") preserved verbatim.
- NOT-04 embed retained; added `data-mobile-pending="true"`.

### Row 9 — `<h3>Unread color fix</h3>` (NEW heading for orphaned prose)
- Net-new `<h3>Unread color fix</h3>` heading wraps the existing line 126 prose ("The migration introduced a less prominent unread color…").
- 9i placeholder inserted (figma-to-html pending).

### Row 10 — `<h3>Three different inboxes</h3>` (net-new connecting beat)
- Net-new `<h3>` + drafted prose verbatim from spec (3-journey framing: new user / subscriber / contributor).
- 10i placeholder inserted (figma-to-html pending).

### Row 11 — `<h2>Push paradox &amp; engagement reality</h2>` opening + `<h3>The push paradox</h3>`
- New `<h2>` wrapper for rows 11–12, sits between Scaleable foundation (rows 6–10) and the still-untouched-this-batch `<h2>1. Build Habits</h2>`.
- Drafted prose verbatim from spec.
- NOT-E6 embed (existing on-disk file `diagram-not-e6-butterfly-chart-v5.html`).

### Row 12 — `<h3>Inbox engagement funnel</h3>`
- Drafted prose verbatim from spec (7.5M / 47% / 75% / Core/Casual/Resurrected/New).
- NOT-E7 embed (existing on-disk file `diagram-not-e7-sankey-flow-v5.html`).

### Verification checklist for Batch 2 (all passed 2026-04-28)
- [x] `<h2>Foundation</h2>` removed.
- [x] `<h3>Design system migration</h3>` / `<h3>Unread system redesign</h3>` / `<h3>Inbox simplification</h3>` all removed.
- [x] All 9 new headings present exactly once: `<h2>Scaleable foundation</h2>`, `<h3>Inbox row component</h3>`, `<h3>Swipe actions</h3>`, `<h3>Unread hierarchy</h3>`, `<h3>Unread color fix</h3>`, `<h3>Three different inboxes</h3>`, `<h2>Push paradox &amp; engagement reality</h2>`, `<h3>The push paradox</h3>`, `<h3>Inbox engagement funnel</h3>`.
- [x] All 4 preserved-prose anchors found exactly once: "one-off engineer build", "less prominent unread color", "overflow menu". ("progressive disclosure" appears twice — once in row 8 prose, once in NOT-04 iframe `title=` attribute; both are expected.)
- [x] All 4 diagram embeds present (NOT-02, NOT-04, NOT-E6, NOT-E7) with `data-mobile-pending="true"`.
- [x] 4 placeholder divs added (rows 7, 9, 10) plus row 2 from Batch 1 = 4 net-new placeholders. (Pre-existing Decay logic placeholder at row 17/Feedback loops still untouched — Batch 3 territory.)
- [x] H2 hierarchy after Batch 2: Summary → Challenge → Strategy → Framework (still in old position, dissolves in Batch 3) → Scaleable foundation → Push paradox & engagement reality → 1. Build Habits → 2. Enable Curation → 3. Create Focus → Results.
- [x] File grew 466 → 514 lines (+48), consistent with new section structure.

### Notes
- The old `<h2>Framework</h2>` (singular) at line 135 is in an awkward position after Batch 2 (sits between Strategy and Scaleable foundation). This is transient — Batch 3 dissolves it: its prose splits across rows 14 and 17 + Strategy section, and a new `<h2>Frameworks</h2>` (plural) wrapper appears between Push paradox and 1. Build Habits.

---

## Batch 3 — Rows 13–18

### Row 13 — `<h2>Frameworks</h2>` opening + `<h3>Activity prioritization</h3>`
- New `<h2>Frameworks</h2>` (plural) wrapper inserted between Push paradox (rows 11–12) and 1. Build Habits.
- Drafted prose verbatim from spec.
- 13i placeholder inserted (figma-to-html pending).

### Row 14 — `<h3>User targeting</h3>` (Signal × Intent matrix)
- Existing line 80 prose with 2 wording substitutions: "tenure" → "intent", "how long they've been on the platform" → "what they're trying to do on the platform".
- Existing line 82 prose preserved verbatim.
- NOT-E4 embed (existing on-disk file).

### Row 15 — `<h3>Growth flywheel</h3>`
- Drafted prose verbatim from spec.
- NOT-E2 embed (existing on-disk file).

### Row 16 — `<h3>Strategic pillars</h3>`
- Drafted prose verbatim from spec.
- NOT-E3 embed (existing on-disk file).

### Row 17 — `<h2>1. Build Habits</h2>` opening + `<h3>Intelligent defaults &amp; feedback loops</h3>`
- `<h2>1. Build Habits</h2>` kept as wrapper.
- Old `<h3>Contextualizing notifications</h3>` heading removed; its prose merged into row 17 below.
- New merged 3-paragraph body from existing line 84 (first 2 sentences only — switchboard sentence held for row 25), line 136, line 212.
- 17i placeholder inserted (figma-to-html pending).
- Static `<img src="img/notif-ds-migration.png">` removed.

### Row 18 — `<h3>Push-to-inbox connection</h3>`
- `<h3>Push-to-inbox connection</h3>` kept; old `<h3>Recommendations as onboarding</h3>` heading folded in (its prose became the first paragraph of the merged row 18 body).
- New merged 2-paragraph body from existing line 144 + line 152.
- NOT-06 embed retained; added `data-mobile-pending="true"`.
- Static `<img src="img/notif-push-landing.png">` removed.

### Other Batch 3 changes (cross-section)
- Old `<h2>Framework</h2>` (singular) block deleted from its transient post-Batch-2 position between Strategy and Scaleable foundation.
- Old `<h3>Feedback loops</h3>` heading + paragraph + decay-logic placeholder div deleted from Enable Curation section (its paragraph merged into row 17).

### Verification checklist for Batch 3 (all passed 2026-04-28)
- [x] Old `<h2>Framework</h2>` (singular) absent.
- [x] Old h3s removed: `<h3>Contextualizing notifications</h3>`, `<h3>Recommendations as onboarding</h3>`, `<h3>Feedback loops</h3>`.
- [x] All 7 new headings present exactly once: `<h2>Frameworks</h2>`, `<h3>Activity prioritization</h3>`, `<h3>User targeting</h3>`, `<h3>Growth flywheel</h3>`, `<h3>Strategic pillars</h3>`, `<h3>Intelligent defaults &amp; feedback loops</h3>`, `<h3>Push-to-inbox connection</h3>`.
- [x] Row 14 reword: "signal and tenure" absent (0); "signal and intent" present (1); old "how long they.ve been on the platform" absent; new "trying to do on the platform" present (1).
- [x] Static images deleted: `notif-ds-migration.png` (0); `notif-push-landing.png` (0).
- [x] All 4 diagram embeds present (NOT-E2, NOT-E3, NOT-E4, NOT-06) with `data-mobile-pending="true"`.
- [x] All preserved prose anchors land: "bias for action" (row 17), "I added copy showing" (row 17), "I shipped decay logic" (row 17), "For low-subscription users" (row 18), "Only the latest push recommendation" (row 18), "The first decision was where to start" (row 14).
- [x] 6 placeholders total (rows 2, 7, 9, 10, 13, 17). Old "Decay logic..." placeholder gone.
- [x] H2 hierarchy now matches spec §2: Summary → Challenge → Strategy → Scaleable foundation → Push paradox & engagement reality → Frameworks → 1. Build Habits → 2. Enable Curation → 3. Create Focus → Results.
- [x] File grew 514 → 550 lines (+36 net), consistent with 4 new sub-sections + 4 new embeds - removed old Framework block - removed Feedback loops block - 2 deleted static images.
- [x] "switchboard" still present once (line 384) in current row-25 prose — held for Batch 4 reword per spec.

---

## Batch 4 — Rows 19–28

### Row 19 — `<h2>2. Enable Curation</h2>` opening + `<h3>Pipeline separation</h3>`
- `<h2>2. Enable Curation</h2>` kept as wrapper.
- Existing line 168 prose preserved verbatim.
- Static `notif-pipeline-separation.png` removed.
- 19i placeholder inserted (figma-to-html pending).

### Row 20 — `<h3>Preference architecture</h3>`
- Existing line 176 prose preserved verbatim.
- NOT-07 embed retained; added `data-mobile-pending="true"`.

### Row 21 — `<h3>Subreddit on-ramps</h3>` (NEW heading)
- New heading wraps split-out first half of existing line 188 prose: "I then surfaced these preferences on the subreddit page itself—point of decision, not buried three screens deep."
- NOT-08 embed retained; added `data-mobile-pending="true"`.

### Row 22 — `<h3>Contextual suggestions</h3>` (NEW)
- Drafted prose verbatim from spec.
- 22 placeholder inserted (figma-to-html pending; container will host push upsell + inbox row variant).

### Row 23 — `<h3>Global settings</h3>` (NEW heading)
- New heading wraps split-out second half of existing line 188 prose plus a new connecting line: "…and simplified subscription management in global settings." + "The flat list replaced a nested per-community drill-down—every community and its alert state visible in one view."
- NOT-09 embed retained; added `data-mobile-pending="true"`.

### Row 24 — `<h2>3. Create Focus</h2>` opening + `<h3>Surface consolidation</h3>`
- `<h2>3. Create Focus</h2>` kept as wrapper.
- New lead-in paragraph from spec ("Why this was hard…") + existing line 245 prose preserved verbatim.
- Static `notif-unified-inbox.png` removed (replaced by row 27 reveal).
- 24i placeholder inserted (figma-to-html pending).

### Row 25 — `<h3>Layout experimentation</h3>`
- Existing line 253 prose first 2 sentences preserved; third sentence reworked to absorb the line 84 "switchboard" salvage from Batch 3: "The inbox wasn't a destination—it was a switchboard that guided users through their session."
- NOT-12 embed retained; added `data-mobile-pending="true"`.

### Row 26 — `<h3>Navigation simplification</h3>`
- Existing line 271 prose preserved verbatim.
- NOT-14 embed retained (v1, the simplification visual); added `data-mobile-pending="true"`.

### Row 27 — `<h3>Unified inbox reveal</h3>` (NEW)
- Drafted prose verbatim from spec ("The result: one inbox, two tabs (Notifications + Chat)…").
- NOT-14 v2 placeholder inserted (figma-to-html pending; container will include GIF placeholder slot for inbox-in-action recording).

### Row 28 — `<h2>Results</h2>`
- Untouched. Existing line 285 prose preserved verbatim.

### Explicit deletions in Batch 4
- `<h3>Cross-channel coordination</h3>` heading + paragraph + NOT-11 diagram-pair block (per spec §3 + Della's "retire?" sticky on NOT-11 v2).
- `<h3>Pinned contributions</h3>` heading + paragraph (per spec §3 + NOT-13 "retire; never shipped" sticky).
- 2 static images: `notif-pipeline-separation.png`, `notif-unified-inbox.png`.

### Verification checklist for Batch 4 (all passed 2026-04-28)
- [x] Final H2 inventory matches spec §2 exactly: 10 H2s in order — Summary, Challenge, Strategy, Scaleable foundation, Push paradox & engagement reality, Frameworks, 1. Build Habits, 2. Enable Curation, 3. Create Focus, Results.
- [x] Final H3 count: 27 (matches spec §2 exactly).
- [x] All explicit deletions confirmed: `<h3>Cross-channel coordination</h3>` (0), `<h3>Pinned contributions</h3>` (0), "pins contributions to the top" (0), `notif-pipeline-separation.png` (0), `notif-unified-inbox.png` (0), `diagram-not11-cross-channel` (0).
- [x] All 9 new Batch 4 headings present exactly once.
- [x] All preserved prose anchors land: "entangled with recommendations" (row 19), "off, low, and frequent" (row 20), "on the subreddit page itself" (row 21), "simplified subscription management in global settings" (row 23), "four messaging systems" (row 24), "chronological, nested, and tabbed" (row 25), "freed a slot in the bottom tab bar" (row 26), "segmentation framework became the foundation" (row 28 Results).
- [x] Switchboard sentence salvaged into row 25 with new wording ("The inbox wasn't a destination — it was a switchboard that guided users through their session.").
- [x] 16 unique diagram embeds in final file; 10 placeholders for net-new diagrams.
- [x] File line count: 549.

---

## Cross-batch preservation map (live audit)

Compared against §4 of the spec. Will fill in per batch.

| Original line(s) | First words | Target | Batch | Landed |
|---|---|---|---|---|
| 27–48 | Hero / eyebrow / h1 / meta-grid | unchanged | — | yes (untouched) |
| 53 | "Reddit communicates with hundreds…" | Row 1 Summary Challenge tile | 1 | yes |
| 57 | "I built the segmentation framework…" | Row 1 Summary Strategy tile | 1 | yes |
| 59–76 | metrics-callout | Row 5 (relocated out of hero) | 1 | yes |
| 80 | "The strategy sat on two axes: signal and tenure…" | Row 14, "tenure" → "intent" reword | 3 | yes |
| 82 | "The first decision was where to start…" | Row 14 (second paragraph) | 3 | yes |
| 84 | "Users had a bias for action…" + "switchboard" | Split: bias → row 17, switchboard → row 25 | 3 + 4 | yes (both halves landed) |
| 90 | "The inbox wasn't on Reddit's design system…" | Row 6 | 2 | yes |
| 114 | "I rebuilt the unread system around progressive disclosure…" | Row 8 | 2 | yes |
| 126 | "The migration introduced a less prominent unread color…" | Row 9 | 2 | yes |
| 130 | "I removed the overflow menu…" | Row 7 | 2 | yes |
| 136 | "I added copy showing why a user received each notification…" | Row 17 | 3 | yes |
| 144 | "For low-subscription users, the inbox became an onboarding engine…" | Row 18 | 3 | yes |
| 152 | "Only the latest push recommendation appeared in the inbox…" | Row 18 | 3 | yes |
| 168 | "Subreddit subscriptions were entangled with recommendations…" | Row 19 | 4 | yes |
| 176 | "The back end couldn't define what updates…" | Row 20 | 4 | yes |
| 188 | "I then surfaced these preferences…" | Split: subreddit page → row 21, global settings → row 23 | 4 | yes |
| 212 | "I shipped decay logic for breaking news…" | Row 17 | 3 | yes |
| 220 | "I defined the relationship between channels…" | **REMOVED** (cross-channel retired) | 4 | yes (deleted) |
| 245 | "I consolidated four messaging systems…" | Row 24 | 4 | yes |
| 253 | "I tested chronological, nested, and tabbed layouts…" | Row 25 (third sentence reworked to absorb switchboard salvage) | 4 | yes |
| 267 | "I designed a system that pins contributions…" | **REMOVED** (NOT-13 retire sticky) | 4 | yes (deleted) |
| 271 | "The unified inbox freed a slot in the bottom tab bar…" | Row 26 | 4 | yes |
| 285 | Results paragraph | unchanged | 4 | yes (untouched) |

---

## Net-new diagram placeholders inserted (figma-to-html pass will replace)

Tracked here as the refactor proceeds.

| Row | Filename target | Status |
|---|---|---|
| 2 | `diagram-not02b-disconnected-surfaces-v5.html` | placeholder |
| 7 | `diagram-not02b-swipe-actions-v5.html` (with GIF slot) | placeholder |
| 9 | `diagram-not04b-unread-color-fix-v5.html` | placeholder |
| 10 | `diagram-not10-three-inboxes-v5.html` | placeholder |
| 13 | `diagram-not13-taxonomy-detail-v5.html` | placeholder |
| 17 | `diagram-not17-context-defaults-v5.html` | placeholder |
| 19 | `diagram-not19-pipeline-entanglement-v5.html` | placeholder |
| 22 | `diagram-not22-contextual-suggestions-v5.html` | placeholder |
| 24 | `diagram-not24-surface-tradeoffs-v5.html` | placeholder |
| 27 | `diagram-not14-unified-inbox-v5.html` (with GIF slot) | placeholder |

---

## Diagram retirements

- `diagram-not01-segmentation-matrix-v5.html` — file stays on disk, no embed (per spec §5 retirement).
- 4-step push-to-inbox flow (Figma `678:2374`) — never embedded (Della picked before/after only).

---

# v3 Refactor Manifest

**Spec:** `working/planning-docs/case-notifications-change-outline-v3.md`
**Working baseline:** `case-notifications.html.v2-bak` (committed at `781e8f1`)
**Started:** 2026-04-28

## v3 Status

| Batch | Positions | Status | Commit |
|---|---|---|---|
| 1 | Summary + Challenge + 3 inboxes (relocated) + engagement funnel (relocated + 2% callout) + Approach pivot (NEW) | landing | (pending) |
| 2 | Foundation + Scalable + Swipe + Unread merged (6–8) | not started | — |
| 3 | Frameworks + Build Habits + Push-to-inbox (9–12) | not started | — |
| 4 | Enable Curation + Pipeline + Preferences merged + Flywheel (13–15) | not started | — |
| 5 | Create Focus + Layout + Nav merged + Results merged (16–19) | not started | — |

---

## v3 Batch 1 — Positions 1–5 (Apr 28, 2026)

### CSS additions to styles.css (per v3 spec §3)

- `.section-eyebrow` — eyebrow above section headings.
- `.case-approach-pivot` + `.approach-steps` (`.step-done`, `.step-active`) — Position 5 numbered statements with progressive emphasis.
- `.impact-callout` (`.metric` + `.body`) — Position 4 (2%). Future use at Positions 11 (×2), 12 (+1%), 18 (1 NAV SLOT FREED).
- Mobile breakpoint added (`max-width: 768px`) for approach-steps + impact-callout — stack vertically and scale down typography.

Skipped per kickoff: `.surface-tradeoffs` (Batch 5), `.pillar-tags` (deferred per default policy §6.26).

### HTML changes — case-notifications.html

| Change | Position | v2-bak source | v3 outcome |
|---|---|---|---|
| Eyebrow inserted | P1 | new | `EXECUTIVE SUMMARY` (Slide 01 `1214:19523`) above `<h2>Summary</h2>` |
| Lede inserted | P1 | new | "From fragmented legacy to unified system" (Slide 01 title) between `<h2>Summary</h2>` and `<div class="summary-pair">` |
| Eyebrow inserted | P2 | new | `THE PROBLEM` (Slide 02 `1214:19565`) above `<h2>Challenge</h2>` |
| Lede 1 inserted | P2 | new | "Four systems. Three platforms. Six years." (Slide 02 hero) between h3 and existing line-78 prose |
| Lede 2 inserted | P2 | new | "Reddit messaging had drifted across four disconnected surfaces, off the design system — hard to scale, harder to experiment." (Slide 02 subtitle) |
| Retired | v2 Row 3 | lines 90–102 | h3 `Notification taxonomy gap` + paragraph + NOT-E5 diagram embed all removed. `diagram-not-e5-notification-taxonomy-v5.html` stays on disk; not embedded. |
| Retired | v2 Row 4 | lines 104–116 | h3 `Decaying retention` + paragraph + NOT-E1 diagram embed all removed. `diagram-not-e1-cohort-decay-v5.html` stays on disk; not embedded. |
| Relocated | P3 (Three different inboxes) | from lines 199–211 → after P2 NOT-02b diagram | h3 + prose + NOT-10 diagram moved to front. |
| Eyebrow inserted | P3 | new | `CORE USER GROUPS · ICP` (Slide 03 `1214:19787`) above relocated h3 |
| Lede inserted | P3 | new | "Each cohort shows up in the inbox differently — the system has to serve all three without trade-offs." (Slide 03 subtitle) between h3 and existing line-201 prose |
| Relocated | P4 (Inbox engagement funnel) | from lines 229–241 → after P3 NOT-10 diagram | h3 + prose + NOT-E7 diagram moved to front. |
| Eyebrow inserted | P4 | new | `CHANNEL PERFORMANCE · INBOX` (Slide 04 `1214:19820`) above relocated h3 |
| Lede inserted | P4 | new | "Users had a bias for action — the more content felt personally actionable, the more likely they engaged." (Slide 04 subtitle) between h3 and existing line-231 prose |
| Impact callout inserted | P4 | new | metric `2%` + body "of all comments on Reddit come from the inbox — the datapoint that shifted leadership investment." (Slide 04 callout) below NOT-E7 diagram |
| NEW section inserted | P5 (Approach pivot) | new | `<section class="case-approach-pivot">` after `</section>` of `case-strategy` and before `<h2>Scalable foundation</h2>`. Contents: eyebrow `APPROACH`, two `<ol>` steps — 01 step-done "Establish scalable foundation", 02 step-active "Optimize for key user journeys" (Slide 09 `1214:19616`) |
| Spelling | line 120 (case-strategy lede) | "scaleable foundation" | → "scalable foundation" |
| Spelling | line 141 (Position 6 h2) | `<h2>Scaleable foundation</h2>` | → `<h2>Scalable foundation</h2>` |

### Diagrams — Batch 1 status

- **Embedded (unchanged):** NOT-03 (P1), NOT-02b (P2), NOT-10 (P3 relocated), NOT-E7 (P4 relocated).
- **Removed embeds:** NOT-E5 (Row 3 retired), NOT-E1 (Row 4 retired). Files remain on disk.
- **Drift flagged for follow-up (deferred per kickoff §6.31–§6.37):**
  - NOT-02b: Slide 02 has 4 system descriptors (PUSH / INBOX / PRIVATE MESSAGES / CHAT) with one-line captions. Verify on-disk diagram includes them.
  - NOT-10: Slide 03 cohort labels (`NEW USER / Casual user / Core user`) per §6.24 default. Verify diagram matches.
  - NOT-E7: Slide 04 has 3 numbered insights in annotation column not in v2 prose. Diagram may need annotation column added.

### Open questions for Della (Batch 1 review)

1. **Lede styling**: ledes inserted as plain `<p>` (no class). Della to decide if a `.section-lede` class is wanted later (italic, accent color, or larger size).
2. **Heading swap (§6.7–§6.10)**: per default policy, kept v2 h2/h3 AND added slide titles as ledes. Della reviews voice and decides whether to swap headings.
3. **Three-beat lede formatting (P2)**: "Four systems. Three platforms. Six years." rendered as a single paragraph. Slide treats each beat on its own line at h1 size. May want `<br>` or custom class.
4. **2% datapoint dedupe (§6.28)**: rendered at P4 as impact callout. Existing line 261 prose at P9 also cites "2% of all comments". Della reviews dedupe after Batch 3.
5. **case-strategy interlude**: stays in place between P4 and P5 in Batch 1 (lines 118–139, with line 120 spelling updated). Eventually relocates to P19 in Batch 5. Della reviews narrative flow at preview.

---

## v3 Batch 1.5 — Slide-voice heading swap, Positions 1–5 (Apr 28, 2026)

Retroactive policy: slide-voice headings replace v2 structural labels at h2/h3. Decision driven by Della's localhost preview after Batch 1 — slide titles read as more skimmable than the v2 labels.

| Change | Position | Before | After |
|---|---|---|---|
| h2 swap | P1 | `<h2>Summary</h2>` | `<h2>From fragmented legacy to unified system</h2>` (Slide 01 `1214:19523` verbatim) |
| h3 swap | P2 | `<h3>No overarching strategy</h3>` | `<h3>Four systems. Three platforms. Six years.</h3>` (Slide 02 `1214:19565` three-beat) |
| h3 swap | P3 | `<h3>Three different inboxes</h3>` | `<h3>Three activity levels. Three problems.</h3>` (Slide 03 `1214:19787`) |
| h3 swap | P4 | `<h3>Inbox engagement funnel</h3>` | `<h3>The inbox drives engagement; but not for everyone</h3>` (Slide 04 `1214:19820` — semicolon preserved) |
| h2 unchanged | P5 | `<h2>Approach</h2>` | unchanged (Slide 09 is heading-only) |

No `id` attribute updates needed — none of the swapped headings carried `id` attributes; only `#main` anchor exists in the page.

### Open questions for Della (Batch 1.5 review)

1. **Duplicate heading/lede at P1**: h2 line 53 reads "From fragmented legacy to unified system"; lede line 54 reads the same. Batch 1.5 was heading-only per kickoff scope. Della to decide: drop the duplicate `<p>` lede, swap it to a different phrase, or leave as-is (CSS could differentiate).
2. **Duplicate heading/lede at P2**: h3 line 80 reads "Four systems. Three platforms. Six years."; lede line 82 reads the same. Same disposition options as P1.

---

## v3 Batch 2 — Positions 6–8 (Apr 28, 2026)

### CSS additions to styles.css

- `--accent-warm: #d4a574` token added to `:root` for casual-warm accent (EXPERIMENT/RESULT eyebrow chips). Designed for reuse at Position 17 in Batch 5.
- `.microformat` + `.experiment-result` modifier — container block.
- `.microformat-eyebrow` + `.microformat-tag` — chip + lead-in eyebrow line. `.microformat-tag` uses `--accent-warm`.
- `.microformat-mechanics` — 2-column grid; `.mechanic-card` + `.mechanic-tag` + `.mechanic-body` + `.mechanic-dot` (dot uses `--accent-warm`).
- Mobile breakpoint at 640px collapses `.microformat-mechanics` to single column.
- `.hierarchy-cards` — 3-column grid; `.hierarchy-card` + `.hierarchy-eyebrow` (uses `--accent`) + `.hierarchy-body`.
- Mobile breakpoint at 768px collapses `.hierarchy-cards` to single column.
- `.decision-callout` — left-bordered (using `--accent`); `.decision-eyebrow` + `.decision-heading` + `.decision-body`.

### HTML changes — case-notifications.html

| Change | Position | Before | After |
|---|---|---|---|
| Eyebrow inserted | P6 | none | `Foundation` (`.section-eyebrow`) above `<h2>Scalable foundation</h2>`. "PILLAR 1" suffix from slide dropped per Della's resolved decision (Foundation = pre-pillar; 3 numbered pillars come after). |
| h3 swap | P6 | `<h3>Inbox row component</h3>` | `<h3>Create a global inbox row component</h3>` (Slide 06 `1214:19629` verbatim) |
| Lede inserted | P6 | none | "Scalable, reusable, on the design system — new notification types in days, not weeks." (Slide 06 subtitle) between h3 and existing prose |
| Eyebrow inserted | P7 | none | `Accessible actions` (`.section-eyebrow`) above h3 |
| h3 swap | P7 | `<h3>Swipe actions</h3>` | `<h3>Leverage gestures for secondary actions</h3>` (Slide 07 `1214:19702` verbatim) |
| Lede inserted | P7 | none | "Platform-native gestures replaced the overflow menu — actions without an extra tap, and the trailing slot freed for a flex element." (Slide 07 subtitle) |
| Microformat block inserted | P7 | none | EXPERIMENT/RESULT structured block: eyebrow chip "Experiment · What gesture is most intuitive for users?" → 2 mechanic cards (Swipe → / ● Long press) → eyebrow chip "Result · swipe". Placed between existing prose and NOT-02b diagram. (Slide 07 verbatim) |
| Eyebrow inserted | P8 | none | `Unread system · Progressive disclosure` (`.section-eyebrow`) above merged h3 |
| h3 MERGE | P8 | TWO h3s — `<h3>Unread hierarchy</h3>` (v2 Row 8) + `<h3>Unread color fix</h3>` (v2 Row 9) | ONE h3 — `<h3>Simplify badging with progressive disclosure</h3>` (Slide 08 `1214:19728` verbatim) |
| Lede inserted | P8 | none | "Every badge maps 1:1 to a visible item — users never have to do math." (Slide 08 subtitle, present-tense; intentional duplicate of past-tense line in existing prose body — slide voice canonical) |
| Hierarchy 3-card block inserted | P8 | none | 3 cards (Level 01 Inbox badge count / Level 02 Tab indicator / Level 03 Row highlight) with body text per Slide 08 verbatim. Placed between NOT-04 diagram and prose paragraph 2. |
| Decision callout inserted | P8 | none | Eyebrow `Decision` + heading `v1 → v2` + body "DS migration introduced a less prominent unread color → click-through dropped → data identified the cause → v2 restored contrast → recovery beyond the inbox." (Slide 08 verbatim). Placed between prose paragraph 2 and NOT-04b diagram. |
| Existing prose preserved | P6, P7, P8 | — | All 4 existing prose paragraphs verbatim (P6 "The inbox wasn't on Reddit's design system…", P7 "I removed the overflow menu…", P8 paragraph 1 "I rebuilt the unread system…", P8 paragraph 2 "The migration introduced a less prominent unread color…"). |

### Diagrams — Batch 2 status

- **Embedded (unchanged):** NOT-02 (P6), NOT-02b-swipe (P7), NOT-04 (P8), NOT-04b (P8). Both NOT-04 diagrams remain stacked at merged P8 per kickoff.
- **No diagram retranslations in this batch** — slide annotation drift (NOT-02 4-pair structure, NOT-04 3-card hierarchy, NOT-04b color swatches) deferred to a separate diagram-pass scope.

### Position 8 placement decision

Spec offered "between two prose paragraphs OR after both — Della to review". Chose:
- **Hierarchy 3-card block:** between NOT-04 diagram and prose paragraph 2. Reinforces paragraph 1's progressive-disclosure concept as a compact structured visual after the diagram's deeper visualization.
- **Decision callout:** between prose paragraph 2 and NOT-04b diagram. Acts as TL;DR header for the color-fix story; NOT-04b diagram then shows the actual swatches.

Final P8 order: eyebrow → h3 → lede → prose 1 → NOT-04 → 3-card hierarchy → prose 2 → decision callout → NOT-04b. Della reviews at preview.

### Open questions for Della (Batch 2 review)

1. **EXPERIMENT/RESULT mechanic-tag color**: rendered with `--text-primary` (white). Slide may use `--accent` (teal) for SWIPE → and ● LONG PRESS chips — only the framing eyebrows (EXPERIMENT, RESULT, dot before LONG PRESS) use `--accent-warm`. If chips should be teal, easy follow-up.
2. **P8 placement**: 3-card hierarchy after NOT-04 vs. before. Decision callout before NOT-04b vs. after. Della reviews at preview; trivial reorder if needed.
3. **Foundation eyebrow casing**: written as "Foundation" in source; CSS renders uppercase via `.section-eyebrow`. Matches Batch 1 pattern.
4. **Mechanic-tag arrows**: rendered "Swipe →" (right arrow) per slide. Consider whether the dot before "Long press" should be a true bullet or kept as `&bull;`.

