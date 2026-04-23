# case-notifications Mobile Responsive Fix — Progress Tracker

**Workstream:** Mobile breakpoint failures on case-notifications diagrams
**Thread opened:** 2026-04-22
**Current status:** Partial fix shipped (commit 4d7786c), incomplete on phone — widening scope
**Living tracker:** `portfolio-site/working/mobile-audit/audit-tracker.xlsx` (openpyxl atomic appends only)

---

## The problem

Della tested the portfolio on her phone after commit 4d7786c and enumerated 9 specific mobile responsiveness failures across what looks like 8+ diagrams on case-notifications. The first fix attempt (5 diagrams edited, width property + padding media queries) was:

- **Mechanically correct** — quality + voice checks passed, hooks clean, push succeeded
- **Scope too narrow** — only audited 5 of the ~9 broken diagrams
- **Insufficient on edited diagrams** — aspect-ratio mismatches and PNG cropping still visible at phone width
- **Never verified on actual render** — Verify-Before-Claiming rule violated (no Chrome MCP capture before declaring done)

---

## Thread 1 (prior) — what shipped

**Commit:** `4d7786c`
**Files edited (5 diagrams in `portfolio-site/img/diagrams/`):**

| # | File | Change |
|---|---|---|
| 1 | `diagram-not02-inbox-row-unit-v5.html` | `.diagram { width: 760px }` → `width: 100%; max-width: 760px` + media queries @ 768 / 400 |
| 2 | `diagram-not03-full-inbox-redesign-v5.html` | Same pattern |
| 3 | `diagram-not04-unread-hierarchy-v5.html` | Same + larger media-query block for title/levels/illustration/labels |
| 4 | `diagram-not08-subreddit-onramps-v5.html` | Same pattern |
| 5 | `diagram-not14-navigation-simplification-v5.html` | Same pattern |

**Gates passed:** quality-check (0 errors, 0 warnings), voice-check (0 errors, 3 pre-existing warnings)

**What the fix targeted:** Fixed-width container anti-pattern (Pattern C from `common-l2-failure-patterns.md`) — `.diagram { width: 760px }` prevented shrinking below 760px at any viewport.

**Why it wasn't enough:** The width fix let containers shrink, but it didn't address (a) aspect-ratio mismatches between Before/After PNG mocks at mobile, (b) PNG crop positioning that breaks when container scales, (c) cramped 3-col layout on NOT-04, (d) illegible watermark numbers, (e) other diagrams entirely (NOT-06/07/12/E2).

---

## The 9 problems Della identified (from phone test)

With probable diagram-ID mapping — **confirm each via Chrome MCP capture at 375/320 before fixing:**

| # | Symptom | Probable diagram(s) | Suspected root cause |
|---|---|---|---|
| 1 | Mobile Before/After frames render at different sizes | NOT-02 / NOT-03 / NOT-08 / NOT-14 | `aspect-ratio` values differ between `.before-mock` and `.after-mock` (e.g. NOT-08 uses 520/150 vs 520/197) — matched on desktop, visually off at phone width |
| 2 | Diagram cut off on right side | NOT-07 preference-architecture (likely) | Fixed-width or non-responsive inner UI |
| 3 | Same as #2 | NOT-06 push-to-inbox OR NOT-12 inbox-layout-experiments | Same class of fix-width issue |
| 4 | Not centered, cards too large vs diagram, cut off | NOT-E2 strategy-flywheel (likely) | Card sizing not responsive; flywheel center not shrinking |
| 5 | Wrong part of header PNG showing (needs community details) | NOT-08 | PNG `top:` / `height:` positioning breaks when container scales |
| 6 | Same as #4 | Second cards/flywheel diagram (possibly NOT-E1 or another NOT-E) | Same class |
| 7 | Totally cut off on right, "looks like an OLD diagram" | NOT-06 push-to-inbox | May still be a v4 template that was never rebuilt to v5 — possible L3 (rebuild), not L2 (CSS fix) |
| 8 | 3-column too cramped, margins too tight | NOT-04 unread hierarchy | Internal padding/gap shrink incomplete at mobile — need tighter gap + reduced internal padding on `.level-card` |
| 9 | "5" and "3" ghost watermark numbers illegible | NOT-04 | Watermark opacity too low or font-size doesn't scale |

**Important:** Diagram mapping above is inferred from prior context + screenshot descriptions. Phase 1 Chrome MCP capture is what actually confirms it.

---

## The 4-phase plan (do in order — do NOT skip)

### Phase 1 — Capture + comparison tracker
- Invoke `responsive-audit` skill
- Use Chrome MCP (not sandbox Playwright — see `references/chrome-mcp-capture.md`) to screenshot each diagram on the LIVE portfolio at 375 and 320
- Include NOT-02, 03, 04, 06, 07, 08, 12, 14, and any NOT-E* currently embedded in case-notifications
- Build a single comparison tracker HTML (see `references/comparison-tracker.md`) showing current-state renders side-by-side
- **STOP and show Della the tracker before Phase 2**

### Phase 2 — Classify
- Each failure gets L1 (container / styles.css), L2 (internal CSS in one diagram), or L3 (new mobile HTML / rebuild)
- Confirm Della's diagram-ID mapping from the table above against actual renders
- NOT-06 specifically: check if it's a v4 file that escaped the v5 rebuild — if yes, L3
- Update `audit-tracker.xlsx` with one row per diagram (openpyxl only, never pandas)

### Phase 3 — Fix in diagnosis order (not file order)
- **First pass:** aspect-ratio normalization at mobile — clears #1 across NOT-02/03/08/14 in one pattern
- **Second pass:** internal content (NOT-04 cramped 3-col + watermark legibility, NOT-08 PNG positioning, NOT-07/12 UI scaling)
- **Third pass:** any L3 rebuild (NOT-06 if confirmed)
- Every edit: inline diff shown to Della before committing

### Phase 4 — Chrome MCP re-verify BEFORE declaring done
- Re-capture each fixed diagram at 375 and 320
- Append to comparison tracker as "after" column
- Show Della visual before/after per diagram
- Only then: commit, push, update tracker rows to `verified`

**Deferred to later thread:** Figma mobile frame updates via `html-to-figma` skill. Do NOT touch Figma in this thread.

---

## Non-negotiable rules (pulled from CLAUDE.md)

- **Path safety:** Show Mac paths only (use `PATH-MAPPINGS.md` conversion). Never show `/sessions/` in terminal commands.
- **Living documents:** Targeted edits to existing HTML only — never rewrite diagram files from scratch.
- **Skill execution:** If using the responsive-audit skill, READ its files (not summarize them). If delegating to an agent, the agent prompt must include the actual skill file paths with "read before starting."
- **Verify before claiming:** Chrome MCP every fix before telling Della it's done. Previous thread skipped this.
- **Voice + quality gates:** Pre-commit runs `quality-check.py` + `voice-check.py`. Expect those gates.
- **Git hygiene:** File-specific `git add <path>` per file. Never `git add -A` or `git add .`.

---

## Mandatory reads for the next thread (in order)

1. `~/CoworkWorkspace/CLAUDE.md`
2. `~/CoworkWorkspace/PATH-MAPPINGS.md`
3. `~/CoworkWorkspace/Get-a-job/CLAUDE.md`
4. **This file** (`portfolio-site/working/mobile-audit/case-notifications-responsive-fix-progress.md`)
5. `~/CoworkWorkspace/Skills/responsive-audit/SKILL.md`
6. `~/CoworkWorkspace/Skills/responsive-audit/references/common-l2-failure-patterns.md`
7. `~/CoworkWorkspace/Skills/responsive-audit/references/chrome-mcp-capture.md`
8. `~/CoworkWorkspace/Skills/responsive-audit/references/comparison-tracker.md`

---

## Progress log

| Date | Event | Outcome |
|---|---|---|
| 2026-04-22 | Thread 1 edited 5 diagrams, committed `4d7786c`, pushed | Mechanical fix correct; phone verification failed — scope too narrow + aspect-ratio mismatches + PNG cropping remain |
| 2026-04-22 | Della enumerated 9 problems after phone test | This doc created; next thread picks up from Phase 1 |
| 2026-04-22 | Thread 2 built Phase 1 comparison tracker (live-iframe version) | `comparison-tracker-case-notifications-2026-04-22.html` — 10 iframe diagrams × 375/320 each, pulled from live Vercel build. Pivoted from PNG capture because Chrome on Mac enforces ~500px viewport minimum. Awaiting Della's mapping confirmation before Phase 2. |

---

## Phase 1 output — where to review

**File:** `portfolio-site/working/mobile-audit/comparison-tracker-case-notifications-2026-04-22.html`
**Why iframes instead of PNG screenshots:** Chrome on macOS won't shrink its viewport below ~500px (`resize_window` succeeds but `innerWidth` stays clamped). Live iframes at fixed pixel widths bypass this — the iframe constrains its content to the iframe's width, so mobile media queries inside the diagram fire correctly regardless of the outer browser width. Side benefit: Della can scroll/interact inside each diagram instead of staring at static PNGs.
**Iframe source:** `https://della-portfolio.vercel.app/img/diagrams/diagram-{id}-v5.html` (the live deploy, which is what her phone actually sees).

**Important hypothesis to confirm in Phase 2:** case-notifications.html has 10 iframe diagrams (NOT-02, 03, 04, 06, 07, 08, 09, 11, 12, 14) — **no NOT-E\* flywheel diagrams**. This contradicts the original Problem-Match table, which assumed NOT-E2 was the flywheel. Della's problems #4, #5, #6 (the "cards + flywheel" complaints, and the "wrong header PNG showing") are more likely pointing to one of these:
- An iframe diagram with embedded cards (NOT-11 cross-channel is the leading candidate)
- A PNG image on the page itself — `notif-push-landing.png` (Discovery / Following / Conversation cards) or `notif-unified-inbox.png` (4-panel progression)

Phase 2 starts by having Della scroll the tracker and point at the exact diagrams matching each of her 9 problems.

---

## Phase 2 — retrofit summary (2026-04-22, Thread 2)

**Root cause (identified in Thread 2):** The v5 NOT diagrams lack the v4 responsive pattern used on AI/SHR/portfolio case studies. That pattern has three pieces:

1. `@media` rules that **restructure** (collapse multi-col grids to 1fr), not just cosmetically pad
2. `body.embedded` CSS block that strips body chrome when the diagram is iframed
3. A one-line iframe detection script: `if(window!==window.parent)document.body.classList.add("embedded")`

Commit 4d7786c from Thread 1 addressed only half of piece #1 (container width). The full retrofit was missing.

**Applied to all 10 v5 NOT diagrams (NOT-02 as pattern proof + 9 more):**

| Diagram | Class collapsed | Had embed before? | Notes |
|---|---|---|---|
| NOT-02 | `.comparison` 2→1 | No | Pattern proof — verified locally by Della |
| NOT-03 | `.comparison` 2→1 | No | Full retrofit |
| NOT-04 | `.level-labels` hidden + `.levels-grid` 3→1 | Yes | Labels hidden (would break visual pairing when stacked); per-card `::before` pseudo injects "1 — Inbox / 2 — Tab / 3 — Row" at mobile. `.flow-arrows` hidden. |
| NOT-06 | `.comparison-strip` 2→1 | Yes | Media queries were entirely absent |
| NOT-07 | `.pref-columns` (1fr auto 1fr)→1fr | Yes | `.transform-arrow` hidden at mobile (horizontal arrow doesn't make sense stacked) |
| NOT-08 | `.comparison` 2→1 | No | Full retrofit |
| NOT-09 | `.compare-area` 2→1 | Yes | Media queries were entirely absent |
| NOT-11 | `.platform-matrix` 3→1 | Yes | Media queries were entirely absent |
| NOT-12 | `.three-up` 3→1 | No | Full retrofit, media queries entirely absent |
| NOT-14 | `.comparison` 2→1 | No | Full retrofit |

**Collapse breakpoint:** 600px across the board. Above 600px the layouts remain as designed; at 600px and below, multi-column grids collapse to single column.

**Gates:** `quality-check.py` on all 9 retrofitted files → 54 checks, 0 errors, 0 warnings. `voice-check.py` on all 9 → 0 errors, 5 pre-existing long-sentence warnings in diagram text content (not introduced by this work).

**Deferred to separate threads:**
- Figma mobile frames — once these are live-verified, push via `html-to-figma` skill
- Problem #4/#5/#6 from Della's phone test — may map to the 4 static PNG images on case-notifications.html (notif-ds-migration.png, notif-push-landing.png, notif-pipeline-separation.png, notif-unified-inbox.png) rather than iframe diagrams. Investigate in next thread if still broken after commit.

---

## Thread-handoff checklist (fill as work progresses)

- [x] Phase 1 built — comparison tracker HTML shows all 10 iframe diagrams at 375/320
- [x] NOT-02 pattern proof — Della verified locally before committing
- [x] Phase 2 — 9 remaining v5 NOT diagrams retrofitted with same pattern (NOT-03, 04, 06, 07, 08, 09, 11, 12, 14)
- [x] Quality + voice gates — all 9 files pass
- [x] Della commits + pushes to Vercel (pushed 2026-04-22, Session 29)
- [x] BUILD-LOG.md appended
- [x] SESSION-STATE.md updated
- [ ] **Phase 4 (next thread):** hard-refresh tracker after Vercel build, visual-verify all 10 v5 diagrams at 375/320 look correct on phone
- [ ] **If any per-diagram tuning needed** — capture as Phase 5 in this progress file
- [ ] **Deferred:** PNG image problems #4/#5/#6 on case-notifications.html (may map to `notif-ds-migration.png`, `notif-push-landing.png`, `notif-pipeline-separation.png`, `notif-unified-inbox.png`). Investigate in next thread IF still broken on phone after commit lands.
- [ ] **Deferred:** capture v4 embed-retrofit pattern into `Skills/responsive-audit/references/v4-embed-retrofit.md` per Lessons→Skill References rule. Wire into SKILL.md Step 0 reads. Bump skill version minor (v0.3.x → v0.4.0).
- [ ] **Deferred:** push 10 dedicated mobile Figma frames via `html-to-figma` skill (one per retrofitted v5 NOT diagram at 375px) — separate focused thread, not blocking
- [ ] Della confirmed diagram-ID mapping
- [ ] Phase 2 classification in `audit-tracker.xlsx`
- [ ] Phase 3 fixes applied, diffs shown
- [ ] Phase 4 Chrome MCP re-verify passed
- [ ] Commit + push with hooks passing
- [ ] Tracker rows marked `verified`
- [ ] SESSION-STATE.md updated
- [ ] BUILD-LOG.md appended
- [ ] Figma mobile frames queued for html-to-figma thread
