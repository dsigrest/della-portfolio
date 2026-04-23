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
| 2026-04-22 | Session 30 (late) — phone verify **FAILED** after grep-count "verify" claimed 10/10 shipped | Root cause: NOT-06/07/09/11/12 have an incomplete `body.embedded .diagram` rule — only `border-radius: 0`, missing `width: 100%; max-width: none`. Container stays locked at 760px inside the iframe. Grep counts all showed pass (`body.embedded >= 2`, script = 1, `@600 >= 1`) but the rule *content* was wrong. Della's screenshots A/B/C/E/G all show the same overflow symptom. Screenshot D (NOT-08) is a separate issue — PNG crop region is fine responsively, just wrong y-axis focus; Della handles in Figma. Screenshot G: Della has a dedicated NOT-06 mobile Figma at node `945:17` — L3 fix via `figma-to-html`. Skill reference `v4-embed-retrofit.md` patched to v0.1.1 (new Pitfall 3 + content-aware audit command + DevTools overflow JS snippet). Skill bumped v0.4.0 → v0.4.1. Next-thread kickoff prompt written at `working/mobile-audit/resume-prompt-case-notifications-phase3-container-fix.md`. |

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
- [x] **Phase 4 code-level verify (Session 30, 2026-04-22):** code-level grep confirms all 10 v5 NOT diagrams have the three-piece retrofit in HEAD — `body.embedded >= 2`, iframe-script = 1, `@media (max-width: 600px) >= 1` across NOT-02/03/04/06/07/08/09/11/12/14. Retrofit shipped cleanly.
- [ ] **Phase 4 phone verify (Della's job, pending):** hard-refresh tracker after Vercel build + real phone test of live `case-notifications.html` on della-portfolio.vercel.app to confirm visual rendering at 375/320 on an actual phone (not Chrome MCP — Chrome on macOS won't shrink below ~500px). Confirm the 6 diagram-level problems from the original phone test list (#1/#2/#3/#7/#8/#9) are resolved.
- [ ] **If any per-diagram tuning needed after phone test** — capture as Phase 5 in this progress file.
- [x] **Session 30 (2026-04-22) — v4 embed-retrofit skill reference captured:** `Skills/responsive-audit/references/v4-embed-retrofit.md` created documenting three-piece pattern (body.embedded CSS + iframe detection one-liner + `@media (max-width: 600px)` grid collapse). Wired into SKILL.md Step 0 mandatory reads (new item 5). Skill version bumped v0.3.0 → v0.4.0 with version history entry. Matches the Lessons → Skill References rule in global CLAUDE.md. Reference includes the retrofit recipe, pitfalls, verify step, code-level audit command, and per-diagram audit table covering all 10 NOT diagrams from Session 29.
- [x] **Session 30 (2026-04-22) — PNG problems #4/#5/#6 investigation:** the 4 standalone PNGs on `case-notifications.html` (`notif-ds-migration.png`, `notif-push-landing.png`, `notif-pipeline-separation.png`, `notif-unified-inbox.png`) render with `max-width: 95%` at `<=768px`, no object-fit/object-position rules, no broken CSS — they scale proportionally. Diagnosis at 375px viewport (~326px rendered width): **`notif-ds-migration`** (1440×1554, ratio 0.93) → 326×352px, near-square, legible (22.6% of original resolution). **`notif-pipeline-separation`** (1440×1561, ratio 0.92) → 326×353px, similar, legible. **`notif-push-landing`** (2340×1628, ratio 1.44) → 326×227px, three cards each ~109px wide — internal text at 14% of original resolution, very hard to read. **`notif-unified-inbox`** (2860×1468, ratio 1.95) → 326×167px, four panels each ~81px wide — internal text at 11% of original, postage-stamp-sized. **Likely mapping to Della's complaints:** #4 "cards too large vs diagram, cut off" → `notif-push-landing.png` (3 horizontal cards cramped at mobile width). #6 "same as #4" → `notif-unified-inbox.png` (4 horizontal panels even more cramped). #5 "wrong part of header PNG showing (needs community details)" → most likely NOT-08 iframe diagram (source assets `not08-legacy-subreddit.png` / `not08-unified-subreddit.png` are 1206×2622 portrait screenshots cropped via `overflow: hidden` on aspect-ratio 520/150 + 520/197 containers; the same 13% top slice of the PNG is visible at every viewport width — proportional, not a responsive bug, but Della may want a different crop region at mobile to reveal "community details" lower in the screenshot). **Fix patterns to discuss with Della before applying:** (1) for push-landing + unified-inbox — create dedicated mobile PNGs (vertical stacked layout instead of horizontal) or replace with responsive HTML diagrams that naturally stack at 600px; (2) for NOT-08 header — add `@media (max-width: 600px) { .mock.before-mock img, .mock.after-mock img { top: calc(... shift to reveal community-details slice ...) } }` or switch to `object-fit/object-position` for cleaner control. **No fixes applied this session** — investigation + diagnosis only, pending Della's preference on which pattern to use for each PNG.
- [ ] **Still deferred:** push 10 dedicated mobile Figma frames via `html-to-figma` skill (one per retrofitted v5 NOT diagram at 375px) — separate focused thread, not blocking.
- [ ] PNG fix pattern decision (Della) + apply chosen pattern for push-landing / unified-inbox / NOT-08 crop region
- [ ] Figma mobile frames queued for html-to-figma thread

### Session 30 (late, 2026-04-22) — phone verify FAILED, Phase 3 re-scoped

Della's phone test exposed that Session 29's retrofit landed inconsistently. Grep counts lied. New state of play:

- [x] **Root cause found:** 5 of 10 diagrams have `body.embedded .diagram { border-radius: 0 }` (incomplete override) instead of the full `{ width: 100%; max-width: none; border-radius: 0 }`. The `.diagram` container stays locked at 760px inside the iframe and blows through the 375/320 viewport. The inner `@media (max-width: 600px)` grid-collapse rules fire but are useless because the container never shrinks.
- [x] **Affected diagrams:** NOT-06, NOT-07, NOT-09, NOT-11, NOT-12.
- [x] **Unaffected (working):** NOT-02, NOT-03, NOT-04, NOT-08, NOT-14 — these got Thread 1's `width: 100%` conversion in commit `4d7786c` which made the standalone `.diagram` rule already mobile-compatible.
- [x] **NOT-08 screenshot-D finding:** PNG crop region is fine responsively — same 13% top slice visible at any viewport. Della prefers a different crop region ("community details further down y-axis") and will fix in Figma. No HTML change needed.
- [x] **NOT-06 screenshot-G finding:** Della has a dedicated mobile Figma at node `945:17` (stacked layout, designed for mobile). Next thread pulls it via `figma-to-html` for an L3 mobile variant instead of relying on responsive CSS.
- [x] **Skill reference patched:** `Skills/responsive-audit/references/v4-embed-retrofit.md` v0.1.0 → v0.1.1 — new Pitfall 3 (incomplete embed override) + content-aware Python audit command + DevTools/Chrome MCP JS snippet for iframe `scrollWidth` overflow measurement. Skill bumped v0.4.0 → v0.4.1 with status-header + version-history entries.
- [x] **Next-thread kickoff prompt:** `working/mobile-audit/resume-prompt-case-notifications-phase3-container-fix.md` — 3 objectives (L2 container-override fix on 5 files, L3 NOT-06 mobile from Figma node 945:17, tracker overflow verify).
- [x] **Session 31 (this thread):** L2 one-line CSS delta applied on NOT-06/07/09/11 (NOT-12 was already correctly overridden — pre-existing fix). Overflow check passed `scrollWidth - clientWidth === 0` at 375 and 320 for all 5 diagrams via Chrome MCP + Python HTTP server on Della's Mac (sidestepped the file:// restriction + Chrome's ~500px viewport floor). L3 mobile variant built from Figma node 945:17 — but node turned out to be **NOT-11 Cross-Channel Model, not NOT-06** (Session 30 misidentified the screenshot). Della confirmed mid-thread to build for NOT-11. Shipped `diagram-not11-cross-channel-v5-mobile.html`, wrapped NOT-11 embed in `case-notifications.html` with `.diagram-pair`, tracker row updated atomically. Swap rule verified at the CSS rule level (raw CSSOM inspection) + via computed style at viewport 699 (desktop:none, mobile:block). Phone re-test still Della's job.
- [ ] **Session 31 close-out:** BUILD-LOG + SESSION-STATE additive entries done, progress doc checklist updated (this block), `figma-to-html/references/node-identity-mismatch.md` captured as Lessons → Skill References output. Git commands generated for Della (file-specific `git add` per file, Mac absolute paths only). NOT-06 dedicated mobile variant still open — awaits correct node ID from Della if she wants one. Archive kickoff prompts only after Della's phone re-test confirms.

### Session 31 (2026-04-22, responsive-audit Phase 3 container fix + NOT-11 mobile variant)

**Landed (verified):**
- [x] `body.embedded .diagram` override completed on NOT-06/07/09/11 (4 one-line Edit calls). NOT-12 was already correct — content-aware audit caught the pre-existing fix; no edit needed. NOT-04 flagged by audit as technically incomplete but out-of-scope per prompt (its standalone `.diagram` rule already uses `width: 100%` so the container scales correctly at mobile; left untouched).
- [x] Content-aware Python audit from `v4-embed-retrofit.md` v0.1.1 now reports `OK` on NOT-02/03/06/07/08/09/11/12/14 (NOT-04 reports `BROKEN` on width-100% flag only, but scales correctly in practice — future cleanup, not this thread).
- [x] Chrome MCP overflow verify: 10/10 checks PASS (5 diagrams × 2 widths). Each iframe's `document.body.scrollWidth - document.body.clientWidth === 0` at 375 AND 320. Pattern for future verify: start `python3 -m http.server 8765` on the Mac (via Desktop Commander), load a local verify tracker over localhost, execute the overflow snippet via Chrome extension's javascript_tool.
- [x] NOT-11 mobile variant built from Figma node `945:17` via `figma-to-html` skill (Mode B): `img/diagrams/diagram-not11-cross-channel-v5-mobile.html` — 375×720, centered Inbox hub with "Source of Truth" badge, dashed connection arrows, 2-col Push+Email spokes with callouts, stacked Native Mobile / Mobile Web / Desktop platform matrix. `figma-source` meta stamped. Quality + voice checks clean (0 errors, 0 warnings).
- [x] `case-notifications.html` NOT-11 embed wrapped with `.diagram-pair`. Swap rule (`styles.css` L370-377) verified via CSSOM inspection AND computed style at viewport 699.
- [x] Tracker row `not11` atomic update: `mobile_file_path = img/diagrams/diagram-not11-cross-channel-v5-mobile.html`, note appended with Session 31 details. Row already had `figma_mobile_node_id = 945:17` (set by Session 30 pre-population).
- [x] `Skills/figma-to-html/references/node-identity-mismatch.md` captured — new reference per Lessons → Skill References rule documenting the "prompt claimed node X = diagram A, Figma data said node X = diagram B" failure mode with detection command + mitigation pattern.
- [x] `Skills/figma-to-html/SKILL.md` updated — Step 0 mandatory reads list extended with the new reference; version bumped 2.4.0 → 2.5.0 with version-history entry.

**Key Session 31 finding — node mismatch (captured as figma-to-html gotcha):**
Session 30's kickoff prompt said Figma node `945:17` was "NOT-06 mobile". The Figma data at that node is actually `not11 — Cross-Channel Model` — 375×720 mobile frame, Inbox hub + Push/Email spokes + Platform matrix. Screenshot confirms. Root cause likely: Session 30 was labelling phone screenshots and miscounted. The figma-to-html skill now documents this failure class so future threads check `data-name` on the resolved node before translating.

**Files touched this session:**
- `portfolio-site/img/diagrams/diagram-not06-push-to-inbox-v5.html` (1-line CSS delta)
- `portfolio-site/img/diagrams/diagram-not07-preference-architecture-v5.html` (1-line CSS delta)
- `portfolio-site/img/diagrams/diagram-not09-global-settings-v5.html` (1-line CSS delta)
- `portfolio-site/img/diagrams/diagram-not11-cross-channel-v5.html` (1-line CSS delta)
- `portfolio-site/img/diagrams/diagram-not11-cross-channel-v5-mobile.html` (new)
- `portfolio-site/case-notifications.html` (NOT-11 embed → `.diagram-pair`)
- `portfolio-site/working/mobile-audit/audit-tracker.xlsx` (atomic update on `not11` row)
- `portfolio-site/working/mobile-audit/session31-local-verify.html` (new verification harness — process doc)
- `portfolio-site/working/mobile-audit/case-notifications-responsive-fix-progress.md` (this file — checklist + Session 31 block)
- `CoworkWorkspace/Skills/figma-to-html/references/node-identity-mismatch.md` (new)
- `CoworkWorkspace/Skills/figma-to-html/SKILL.md` (Step 0 list + version bump)
- `Get-a-job/BUILD-LOG.md` (Session 31 entry prepended)
- `Get-a-job/SESSION-STATE.md` (As of header updated)

**Open for Della (phone re-test gate):**
- Hard refresh `della-portfolio.vercel.app/case-notifications.html` after push lands + Vercel rebuilds.
- Spot-check NOT-06/07/09/11/12 on phone at 375-ish. Pass = no horizontal scrollbar, content contained inside iframe width.
- NOT-11 specifically: verify mobile variant renders (stacked hub/spokes/platform matrix, not the horizontal desktop flow).
- If still broken, report specific diagram + symptom + screenshot for Session 32 scope.

**Deferred (not this thread):**
- NOT-06 dedicated mobile variant — if Della still wants one, she'll provide the correct Figma node ID. L2 container fix is in place so desktop responsive CSS handles it at mobile for now.
- NOT-04 embed override completeness (scales correctly in practice, cosmetic fix only).
- 9 remaining mobile Figma frames via `html-to-figma` (separate focused thread).
- NOT-08 PNG crop region — Della's Figma task.
