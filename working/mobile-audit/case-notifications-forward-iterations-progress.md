# case-notifications Forward-Iteration Translation — Progress Tracker

**Thread started:** 2026-04-22
**Scope:** HTML only (mobile pairing deferred to separate thread)
**Source:** Figma file `TArUrZsBUocaAsqetjXq7V`, page `29:43` ("1. Notifs & Inbox")
**Target:** `portfolio-site/case-notifications.html` (8 `img-placeholder` slots + 3 retirements)
**Soft budget:** 6 diagrams per thread

---

## Finalized batch (this thread)

### Retirements (HTML-only edits, no Figma work)

| # | Family | Current location in case-notifications.html | Reason |
|---|---|---|---|
| R1 | NOT-01 | Lines 86–94 (iframe + wrapper in "Framework" section) | Della confirmed retire; duplicate of NOT-E4 |
| R2 | NOT-05 | Lines 130–132 (placeholder div, "Inbox simplification") | Della confirmed retire |
| R3 | NOT-13 | Lines 250–252 (placeholder div, "Pinned content model") + possibly L246–248 surrounding H3 + paragraph | Della confirmed retire |

### New HTML builds (Figma → HTML via figma-to-html skill)

| # | Family | Canonical Figma node | x | Fills placeholder at | Notes |
|---|---|---|---|---|---|
| B1 | NOT-02 | `707:112` | 1731 | L103 ("Inbox row unit") | **Sample quality test — start here** |
| B2 | NOT-03 | `709:283` | 1731 | L107 ("Full-screen before and after") | |
| B3 | NOT-08 | `709:668` | 1763 | L193 ("Subreddit header on-ramps") | |
| B4 | NOT-12 | `678:3020` | 840 | L243 ("Inbox layout experiments") | |
| B5 | NOT-14 | `709:1010` | 1761 | L259 ("Navigation before and after") | Address "ring shouldn't be visible through the cards" issue during translation |

### On hold (pending Della decision)

| Family | Status | Question |
|---|---|---|
| NOT-07A | HOLD | B-version of NOT-07 (push-to-inbox continuity); Della undecided which version to ship |

### Deferred to separate thread

| Family | Why deferred |
|---|---|
| NOT-E1 | Maps to L211 placeholder ("Decay logic") — ready to build but bundled with E-series work |
| NOT-E2 through NOT-E7 | Require case study structural edits to insert new placeholders first (see `case-notifications-e-series-placement-recommendation.md`) |

---

## Per-diagram progress log

Each diagram gets a row when work starts. Status progresses: `not started` → `fetching` → `drafting` → `verifying` → `complete` → `deployed`.

| # | Family | Status | Canonical node | HTML output file | Verification | Notes |
|---|---|---|---|---|---|---|
| B1 | NOT-02 | verifying | `707:112` | `working/diagrams/v5/diagram-not02-inbox-row-unit-v5.html` | rendered at 760px, diffed vs Figma — structure + content match; CSS-recreated mocks pending PNG swap (Figma CDN 403) | Sample; awaiting Della quality greenlight. See `figma-refs/not02-sample-verification.md` |
| B2 | NOT-03 | not started | `709:283` | `img/diagrams/diagram-not03-{slug}-v5.html` | — | |
| B3 | NOT-08 | not started | `709:668` | `img/diagrams/diagram-not08-{slug}-v5.html` | — | |
| B4 | NOT-12 | not started | `678:3020` | `img/diagrams/diagram-not12-{slug}-v5.html` | — | |
| B5 | NOT-14 | not started | `709:1010` | `img/diagrams/diagram-not14-{slug}-v5.html` | — | Ring visibility fix |
| R1 | NOT-01 | not started | — | (remove iframe L86–94) | — | |
| R2 | NOT-05 | not started | — | (remove placeholder L130–132) | — | |
| R3 | NOT-13 | not started | — | (remove placeholder L250–252) | — | Check if H3+p also removed |

---

## Per-diagram pipeline reference

For every new build, follow the `figma-to-html` skill's Step 0–8 process:

- **Step 0**: Pre-reads + Della context
- **Step 1**: Fetch canonical frame via `get_screenshot` → save to `working/mobile-audit/figma-refs/not{nn}-canonical.png`
- **Step 2**: Fetch metadata via `get_metadata` (scoped to node) + variables via `get_variable_defs`
- **Step 3**: Map layer names to CSS selectors (document any conflicts)
- **Step 4**: Draft HTML using design tokens (container: 760px, `#0A0C16`, radius 16, overflow hidden; fonts: Inter + JetBrains Mono)
- **Step 5**: Stamp `<meta name="figma-source" content="node:[id] page:29:43 file:TArUrZsBUocaAsqetjXq7V">`
- **Step 6**: Take screenshot at `760px` wide for visual diff against Figma
- **Step 7**: Verify (voice-check if text; quality-check for HTML validity; visual diff)
- **Step 8**: Update case-notifications.html placeholder → iframe embed

---

## Cross-thread coordination notes

- **Mobile pairing**: All 5 new builds (NOT-02, 03, 08, 12, 14) will need mobile pairs in a later thread. Flag in handoff brief.
- **NOT-07A**: Still needs Della's version B/A decision before any work.
- **E-series**: Placement recommendation written; actual builds + structural edits to case-notifications.html deferred to separate thread.
- **NOT-06 ring visibility**: Della noted issue exists in both Figma and HTML; will need HTML fix when NOT-06 next iterates (not part of this batch — NOT-06 is current).

---

## Decisions log

| Date | Decision | Rationale |
|---|---|---|
| 2026-04-22 | Retire NOT-01, NOT-05, NOT-13 | Della confirmed after discovery; NOT-01 duplicates NOT-E4 |
| 2026-04-22 | NOT-07A held | Della undecided on A/B variant |
| 2026-04-22 | L211 placeholder = NOT-E1 | Della confirmed |
| 2026-04-22 | E-series placement = separate thread | Requires structural edits to case study, too much scope |
| 2026-04-22 | Sample-first on NOT-02 | Smallest scope of the 5 new builds |

---

## Thread-handoff checklist (fill at end of thread)

- [ ] All completed diagrams listed above with `deployed` status
- [ ] Open-state diagrams listed with clear next-step
- [ ] Mobile-pair list handed to mobile thread
- [ ] SESSION-STATE.md updated
- [ ] BUILD-LOG.md appended
- [ ] case-notifications.html final screenshot captured for records
