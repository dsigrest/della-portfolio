# case-notifications.html — Change Outline (Figma → HTML, v3)

**Status:** Spec drafted from direct Figma extractions + v2 spec preservation map. Ready for Della review. **No HTML execution begins until Della signs off and resolves the open questions in §6.**

**Source of truth:**
- v2 deployed prose: `case-notifications.html` (current state, post-v2 refactor — backup at `case-notifications.html.v2-bak`)
- v3 slide extractions: `~/CoworkWorkspace/Get-a-job/working/v3-slide-extractions.md` (all 19 slides, direct Figma fetches, captured 2026-04-28)
- v2 spec / preservation map: `working/planning-docs/case-notifications-change-outline.md`
- Verified facts: `working/planning-docs/verified-facts-registry.md`

**Target file:** `case-notifications.html` (project root). **Diagram folder:** `img/diagrams/`.

**Predecessor:** `case-notifications-change-outline.md` (v2). All v2 prose and diagrams stay; v3 is a strict rearrangement + 6 retirements + 1 new transition.

**Voice rule:** existing case-study prose preserved verbatim. Slide refinements pulled verbatim. No invention.

---

## §1 v3 position table

| Pos | Heading | v2 source row | Slide ID | Diagram | Retired? |
|---|---|---|---|---|---|
| 1 | `<h2>Summary</h2>` | Row 1 | Slide 01 (`1214:19523`) | `diagram-not03-full-inbox-redesign-v5.html` | — |
| 2 | `<h2>Challenge</h2>` + `<h3>No overarching strategy</h3>` | Row 2 | Slide 02 (`1214:19565`) | `diagram-not02b-disconnected-surfaces-v5.html` | — |
| 3 | `<h3>Three different inboxes</h3>` | Row 10 (moved to front) | Slide 03 (`1214:19787`) | `diagram-not10-three-inboxes-v5.html` | — |
| 4 | `<h3>Inbox engagement funnel</h3>` | Row 12 (moved to front) | Slide 04 (`1214:19820`) | `diagram-not-e7-sankey-flow-v5.html` | — |
| 5 | `<h2>Approach</h2>` | NEW | Slide 09 (`1214:19616`) | none (or new approach-pivot block) | — |
| 6 | `<h2>Scaleable foundation</h2>` + `<h3>Inbox row component</h3>` | Row 6 | Slide 06 (`1214:19629`) | `diagram-not02-inbox-row-unit-v5.html` | — |
| 7 | `<h3>Swipe actions</h3>` (heading rename) | Row 7 | Slide 07 (`1214:19702`) | `diagram-not02b-swipe-actions-v5.html` | — |
| 8 | `<h3>Unread system</h3>` (merged) | Rows 8 + 9 | Slide 08 (`1214:19728`) | `diagram-not04-unread-hierarchy-v5.html` + `diagram-not04b-unread-color-fix-v5.html` | — |
| 9 | `<h2>Frameworks</h2>` + `<h3>User targeting</h3>` | Row 14 | Slide 10 (`1214:19909`) | `diagram-not-e4-signal-intent-matrix-v5.html` | — |
| 10 | `<h3>Strategic pillars</h3>` | Row 16 | Slide 11 (`1214:20645`) | `diagram-not-e3-strategic-pillars-v5.html` | — |
| 11 | `<h2>1. Build Habits</h2>` + `<h3>Intelligent defaults &amp; feedback loops</h3>` | Row 17 | Slide 12 (`1214:20054`) | `diagram-not17-context-defaults-v5.html` | — |
| 12 | `<h3>Push-to-inbox connection</h3>` | Row 18 | Slide 13 (`1214:20080`) | `diagram-not06-push-to-inbox-v5.html` | — |
| 13 | `<h2>2. Enable Curation</h2>` + `<h3>Pipeline separation</h3>` | Row 19 | Slide 14 (`1214:20146`) | `diagram-not19-pipeline-entanglement-v5.html` | — |
| 14 | `<h3>Preference architecture &amp; subreddit on-ramps</h3>` (merged) | Rows 20 + 21 | Slide 15 (`1214:20255`) | `diagram-not07-preference-architecture-v5.html` + `diagram-not08-subreddit-onramps-v5.html` | — |
| 15 | `<h3>Growth flywheel</h3>` | Row 15 (relocated) | Slide 16 (`1214:19972`) | `diagram-not-e2-strategy-flywheel-v5.html` | — |
| 16 | `<h2>3. Create Focus</h2>` + `<h3>Surface consolidation</h3>` | Row 24 | Slide 17 (`1214:20314`) | `diagram-not24-surface-tradeoffs-v5.html` | — |
| 17 | `<h3>Layout experimentation</h3>` | Row 25 | Slide 18 (`1214:20390`) | `diagram-not12-inbox-layout-experiments-v5.html` (retranslate to 4 options) | — |
| 18 | `<h3>Navigation simplification &amp; unified inbox reveal</h3>` (merged) | Rows 26 + 27 | Slide 19 (`1214:20580`) | `diagram-not14-navigation-simplification-v5.html` + `diagram-not14-unified-inbox-v5.html` | — |
| 19 | Strategy recap (relocated metrics-callout) + `<h2>Results</h2>` | Rows 5 + 28 | Slide 20 (`1214:20607`) | none (metrics panel + GIF) | — |

### Retirements (v2 rows removed entirely from v3)

| v2 row | What's removed | Source line in current HTML |
|---|---|---|
| Row 3 — `<h3>Notification taxonomy gap</h3>` | h3 + paragraph + NOT-E5 diagram embed | lines 90–102 |
| Row 4 — `<h3>Decaying retention</h3>` | h3 + paragraph + NOT-E1 diagram embed | lines 104–116 |
| Row 11 — `<h2>Push paradox &amp; engagement reality</h2>` + `<h3>The push paradox</h3>` | h2 wrapper + h3 + paragraph + NOT-E6 diagram embed | lines 213–227 |
| Row 13 — `<h3>Activity prioritization</h3>` | h3 + paragraph + NOT-13 diagram embed | lines 245–257 |
| Row 22 — `<h3>Contextual suggestions</h3>` | h3 + paragraph + NOT-22 diagram embed | lines 383–395 |
| Row 23 — `<h3>Global settings</h3>` | h3 + 2 paragraphs + NOT-09 diagram embed | lines 397–411 |

HTML diagram files for retired rows stay on disk (not deleted) but are no longer embedded.

---

## §2 Per-position entries

For each position, this section specifies: heading, eyebrow, body prose (with line-number citations), impact callouts (with slide citations), and diagram source. Every claim is sourced.

---

### Position 1 — `<h2>Summary</h2>` (existing wrapper, kept)

- **eyebrow** (new): `EXECUTIVE SUMMARY` *[from Slide 01 node `1214:19523`]*
- **heading** (existing): "From fragmented legacy to unified system" — Slide 01 title may replace v2's plain `<h2>Summary</h2>` or sit beside it as a sub-eyebrow. **Open question — Della to decide.**
- **Challenge tile prose** (existing line 56, verbatim):
  > Reddit communicates with hundreds of millions of users daily across four separate systems—Chat, Messages, Mod Mail, and Notifications—fragmented across native mobile, mobile web, and desktop with no connecting architecture and a system that didn't behave as users expected.
- **Strategy tile prose** (existing line 60, verbatim):
  > I built the segmentation framework, defined the inbox vision, and led the evolution from disconnected surfaces into a **unified system that drives growth and engagement**. Every stage was validated through fully operable prototypes tested with real users—shifting internal conversations from opinion to evidence.
- **Diagram:** `diagram-not03-full-inbox-redesign-v5.html` *[from v2 spec §5 inventory]*
- **Optional augmentation:** Slide 01's 6 annotations (3 BEFORE + 3 AFTER) could be added to NOT-03 v1 if not already present. Verify on-disk diagram matches.
- **Position 1 ship criteria:**
  - Existing Summary section (lines 51–72) preserved.
  - New eyebrow added if Della approves.
  - NOT-03 diagram embed unchanged.

---

### Position 2 — `<h2>Challenge</h2>` + `<h3>No overarching strategy</h3>` (existing wrappers, kept)

- **eyebrow** (new): `THE PROBLEM` *[from Slide 02 node `1214:19565`]*
- **heading rewrite candidate:** "Four systems. Three platforms. Six years." — Slide 02 hero three-beat is staff-coded and tighter than current h3 "No overarching strategy." **Open question — Della: replace v2 h3 with this three-beat phrasing, or keep current h3 + add three-beat as visual emphasis above existing diagram?**
- **body prose** (existing line 78, verbatim):
  > Beyond fragmentation, the surfaces had no overarching user strategy: limited inventory, limited controls, no prioritization model. Push notifications, the inbox, private messages, and chat operated independently—each with a distinct content type and no shared architecture.
- **slide-derived lede** (NEW, from Slide 02 node `1214:19565`):
  > Reddit messaging had drifted across four disconnected surfaces, off the design system — hard to scale, harder to experiment.
  > **Open question — Della: insert this as a one-line lede ABOVE the existing line 78 paragraph, or replace, or skip?**
- **system cards** (4-card 2x2 grid from Slide 02; already represented in NOT-02b diagram per v2 spec §5):
  - PUSH — "Opt-in updates for off-platform reach"
  - INBOX — "Recommendations, subscriptions, activity"
  - PRIVATE MESSAGES — "1:1 and system-to-user"
  - CHAT — "1:1 and group conversations"
  *[from Slide 02 node `1214:19565`]*

  Verify on-disk `diagram-not02b-disconnected-surfaces-v5.html` includes these 4 system descriptors. Retranslate via figma-to-html if drift.
- **Diagram:** `diagram-not02b-disconnected-surfaces-v5.html` *[from v2 spec §5]*
- **Position 2 ship criteria:**
  - Existing line 78 prose preserved.
  - Eyebrow + lede inserts pending Della.
  - NOT-02b diagram verified or retranslated.

---

### Position 3 — `<h3>Three different inboxes</h3>` (relocated from v2 Row 10)

This row moves from middle of case study to front per v3 handoff Move 2.

- **eyebrow** (new): `CORE USER GROUPS · ICP` *[from Slide 03 node `1214:19787`]*
- **heading rewrite candidate:** "Three activity levels. Three problems." — Slide 03 title rephrases v2's "Three different inboxes" with sharper parallel structure. **Open question — Della: replace heading or keep both as h3 + sub-eyebrow?**
- **body prose** (existing line 201, verbatim):
  > Strategy doesn't translate without understanding who's receiving the notification. Three user journeys define the inbox experience, and each surfaces a different problem: new users see an empty state, subscribers can't customize what they see, and contributors get crowded with activity that doesn't surface what matters.
- **slide-derived lede** (NEW, from Slide 03 node `1214:19787`):
  > Each cohort shows up in the inbox differently — the system has to serve all three without trade-offs.
- **journey card content** (cohort labels + voice-of-user quotes) *[from Slide 03 node `1214:19787`]*:
  - **NEW USER** ("just getting started") — *"I don't know where to start."*
  - **Casual user** ("Seek or Scroll 1-2 times a week") — *"I don't care about these updates."*
  - **Core user** ("Daily visits or Contribution") — *"Where is my stuff??"*

  **Open question — Della: cohort labels diverge from v2 prose ("subscriber" → "Casual user", "contributor" → "Core user"). Slide is the canonical visual. Use slide labels going forward?**

- **Diagram:** `diagram-not10-three-inboxes-v5.html` *[from v2 spec §5; net-new in v2, may now be on disk]*
- **Position 3 ship criteria:**
  - Existing line 201 prose preserved (relocated to Position 3 in document order).
  - Cohort labels confirmed by Della.
  - On-disk diagram matches slide cohort labels (or retranslated).

---

### Position 4 — `<h3>Inbox engagement funnel</h3>` (relocated from v2 Row 12)

This row moves from middle of case study to front per v3 handoff Move 3.

- **eyebrow** (new): `CHANNEL PERFORMANCE · INBOX` *[from Slide 04 node `1214:19820`]*
- **heading rewrite candidate:** "The inbox drives engagement; but not for everyone" — Slide 04 title. **Open question — Della: replace v2 h3 or augment?**
- **body prose** (existing line 231, verbatim):
  > The inbox itself wasn't a discovery surface—it was a contribution surface. **7.5M DAU** enter the inbox; **47% click through**; **75% of those go on to contribute**. That funnel is shaped almost entirely by Core users—Casual, Resurrected, and New cohorts barely make it past the first step. The inbox was serving only the most engaged.
- **slide-derived insights** (NEW, from Slide 04 node `1214:19820` — annotation column):
  - Insight 1: "Daily users make up primary traffic" — "The inbox isn't serving new and casual user's needs"
  - Insight 2: "Contribution drives the most clicks" — "The more personalized content feels, the more it drives engagement"
  - Insight 3: "The inbox is a utility" — "Users expect high legibility, predictability, and easy management"
- **impact callout** (Slide 04 node `1214:19820`):
  - Metric: "2%"
  - Body: "of all comments on Reddit come from the inbox — the datapoint that shifted leadership investment."
  *[matches verified-facts: "The inbox drives 2% of all comments on Reddit"]*

  **Note:** existing line 261 prose at Position 9 also cites the 2% figure. Decide whether to dedupe or keep both — the Position 4 callout makes this datapoint visually prominent here.
- **Diagram:** `diagram-not-e7-sankey-flow-v5.html` *[from v2 spec §5, on disk]*
- **Verified facts referenced:** 7.5M DAU, 47% click, 75% contributed, 2% of all comments *[all from `verified-facts-registry.md`]*
- **Position 4 ship criteria:**
  - Existing line 231 prose preserved (relocated).
  - 3 insights from Slide 04 added if Della approves.
  - 2% callout placement decided (Position 4, Position 9, or both).

---

### Position 5 — `<h2>Approach</h2>` (NEW — no v2 prose source)

This is the new transition between Challenge framing (Positions 2–4) and the Foundation/Frameworks/Pillars work that follows. Source of truth: Slide 09 verbatim.

- **heading** (NEW): `<h2>Approach</h2>` (or no h2 — slide is heading-only with eyebrow)
- **eyebrow:** `APPROACH` *[from Slide 09 node `1214:19616`]*
- **body** — Slide 09's two numbered statements verbatim *[from Slide 09 node `1214:19616`]*:
  > **01.** Establish scalable foundation
  >
  > **02.** Optimize for key user journeys
- **No additional prose.** Slide 09 is heading-only. Della had previously stated in v2 spec line 102 the strategy lede as "establish a scaleable foundation; optimize for key user journeys" — slide is the canonical version with statement 01 visually de-emphasized (already done) and statement 02 visually emphasized (the strategic move).
- **Diagram:** none. The approach pivot IS the visual element — render as numbered statements with progressive emphasis (01 dimmed, 02 highlighted) to match slide treatment.
- **HTML structure suggestion:**
  ```html
  <section class="case-approach-pivot">
    <p class="section-eyebrow">Approach</p>
    <ol class="approach-steps">
      <li class="step-done"><span class="step-num">01</span><span class="step-text">Establish scalable foundation</span></li>
      <li class="step-active"><span class="step-num">02</span><span class="step-text">Optimize for key user journeys</span></li>
    </ol>
  </section>
  ```
- **Spelling:** Slide uses "scalable"; current case study uses "scaleable" (line 120). **Open question — Della: which is canonical?** Recommend "scalable" (slide; standard spelling). If she chooses "scaleable", apply consistently across v3 (it appears in current line 141 h2 too).
- **`[Della to write]` flag:** if Della wants connective copy beyond the two statements (e.g., a one-line transition into Position 6), it should be a sentence she writes — Slide 09 has no body prose to extract. Spec doc leaves a placeholder.

---

### Position 6 — `<h2>Scaleable foundation</h2>` + `<h3>Inbox row component</h3>` (existing, kept)

- **h2 wrapper** (existing line 141): `<h2>Scaleable foundation</h2>` (note: "scaleable" — see Position 5 spelling note)
- **eyebrow** (new): `FOUNDATION · PILLAR 1` *[from Slide 06 node `1214:19629`]*

  **Open question — Della: Slide 06 calls itself "PILLAR 1". v3 already has 3 numbered pillars (Build Habits / Enable Curation / Create Focus at Positions 11, 13, 16). Is Foundation a 4th pillar (numbered) or a pre-pillar phase? Pillar tag chips on Slides 12/13/14/15/16/17/18/19 show 3 pillars, NOT 4. Recommend treating Foundation as pre-pillar; eyebrow becomes `FOUNDATION` only (drop "PILLAR 1").**

- **heading rewrite candidate:** Slide 06 title is "Create a global inbox row component" — verb-driven, action-coded. **Open question — Della: replace v2 h3 "Inbox row component" with slide title?**
- **slide-derived lede** (NEW, from Slide 06 node `1214:19629`):
  > Scalable, reusable, on the design system — new notification types in days, not weeks.
- **body prose** (existing line 145, verbatim):
  > The inbox wasn't on Reddit's design system. Every component was a **one-off engineer build**—growing technical debt, no quality assurance, and each new feature built from scratch. I designed the inbox row component as a scalable, reusable unit intended for distributed messaging surfaces across the platform, then migrated the full surface to the design system. Every project ran through a **technical kickoff with the eng IC** picking up the work—pressure-testing edge cases, building buy-in, and aligning on decisions before a line of code was written.
- **slide annotations** (4 numbered before/after pairs, already represented in NOT-02 v2 per v2 spec §5):
  - BEFORE: 1. Inconsistent visual anchors  2. Various time stamp locations  3. Multiple metadata & action requirements  4. One-off build; no unifying system
  - AFTER: 1. Consistent visual anchor placement  2. Singular time stamp location  3. Scalable metadata slot & trailing element  4. Global design system component
  *[from Slide 06 node `1214:19629`]*
- **Diagram:** `diagram-not02-inbox-row-unit-v5.html` *[from v2 spec §5, on disk; verify v2 visual matches slide annotations]*
- **Position 6 ship criteria:**
  - Existing line 145 prose preserved.
  - Eyebrow + lede inserts pending Della.
  - NOT-02 diagram verified against slide annotations.

---

### Position 7 — `<h3>Swipe actions</h3>` → `<h3>Leverage gestures for secondary actions</h3>` (heading renamed)

- **heading rename** (recommended): "Leverage gestures for secondary actions" *[from Slide 07 node `1214:19702`]*. v2 heading "Swipe actions" is shorter; slide is more precise. **Della to confirm.**
- **eyebrow:** `ACCESSIBLE ACTIONS` *[from Slide 07 node `1214:19702`]*
- **body prose** (existing line 159, verbatim):
  > I removed the **overflow menu, icon-based message type indicators**, and segmented inbox sections that pushed content below the fold. Icons had low comprehension—I replaced them with clear, embedded copy. Swipe actions and long press handled secondary options. Engagement held steady.
- **slide-derived lede** (NEW, from Slide 07 node `1214:19702`):
  > Platform-native gestures replaced the overflow menu — actions without an extra tap, and the trailing slot freed for a flex element.
- **EXPERIMENT/RESULT microformat** *[from Slide 07 node `1214:19702`]*:
  - EXPERIMENT — "What gesture is most intuitive for users?"
  - SWIPE → "Primary secondary action"
  - ● LONG PRESS — "Access secondary menu"
  - RESULT — "swipe"

  **Open question — Della: render this as a small structured block within Position 7, or fold the SWIPE/LONG PRESS info into the prose body?** The EXPERIMENT/RESULT pattern uses a casual-warm accent color (`#d4a574`) on the slide — consistent across slides 07, 14, etc.
- **Diagram:** `diagram-not02b-swipe-actions-v5.html` *[from v2 spec §5; on disk per BUILD-LOG commit `5122b8e` — swipe-action GIF embedded]*
- **Position 7 ship criteria:**
  - Existing line 159 prose preserved.
  - Heading rename pending Della.
  - EXPERIMENT/RESULT block decision made.

---

### Position 8 — `<h3>Unread system</h3>` (MERGED — v2 Rows 8 + 9 collapse here)

- **heading rewrite candidate:** "Simplify badging with progressive disclosure" *[from Slide 08 node `1214:19728`]*. v2 split this into two h3s: "Unread hierarchy" (Row 8, line 173) and "Unread color fix" (Row 9, line 187). v3 merges per slide structure. **Della to confirm new merged heading.**
- **eyebrow:** `UNREAD SYSTEM · PROGRESSIVE DISCLOSURE` *[from Slide 08 node `1214:19728`]*
- **slide-derived lede** (NEW, from Slide 08 node `1214:19728`):
  > Every badge maps 1:1 to a visible item — users never have to do math.

  *[Note: this lede tightens v2 line 173's "Every badge mapped 1:1 to a visible item—users never had to do math." Tense shifted past→present. Slide version is canonical for v3.]*

- **body — paragraph 1** (existing line 173, verbatim — v2 Row 8):
  > I rebuilt the unread system around **progressive disclosure**: a single numeric badge at the inbox level, a dot indicator at the tab level, typography plus subtle color at the row level. Every badge mapped 1:1 to a visible item—users never had to do math.
- **body — paragraph 2** (existing line 187, verbatim — v2 Row 9):
  > The migration introduced a **less prominent unread color** and click-through dropped. I used the data to identify the cause, partnered with the design systems team to adjust, and the fix influenced design system usage beyond the inbox.
- **3-card hierarchy block** *[from Slide 08 node `1214:19728`]*:
  - LEVEL 01 · INBOX BADGE COUNT — "Aggregate count at the single entry point — exact, scannable."
  - LEVEL 02 · TAB INDICATOR — "Boolean signal — new items exist in this tab, without counting."
  - LEVEL 03 · ROW HIGHLIGHT — "Per-item read/unread via typographic weight and subtle tint shift."
- **decision callout** (the unread color fix story summarized) *[from Slide 08 node `1214:19728`]*:
  - eyebrow: DECISION
  - heading: v1 → v2
  - body: "DS migration introduced a less prominent unread color → click-through dropped → data identified the cause → v2 restored contrast → recovery beyond the inbox."

  **Recommendation: keep the existing line 187 paragraph as the surrounding prose AND render the slide's decision-callout as a visual element — they tell the same story at different levels of compression.**
- **Diagrams:**
  - `diagram-not04-unread-hierarchy-v5.html` (Row 8) *[v2 spec §5, on disk; verify v2 visual matches slide 3-card]*
  - `diagram-not04b-unread-color-fix-v5.html` (Row 9) *[v2 spec §5, on disk]*

  **Open question — Della: keep both diagrams stacked at Position 8, or commission a single combined diagram (would require new translation)?**
- **Position 8 ship criteria:**
  - Existing line 173 + line 187 prose preserved.
  - Heading merged to single h3 per Della.
  - Decision-callout rendered if Della approves.

---

### Position 9 — `<h2>Frameworks</h2>` + `<h3>User targeting</h3>` (existing wrappers, kept)

- **h2 wrapper** (existing line 243): `<h2>Frameworks</h2>` — kept.
- **heading rewrite candidate:** "Identify needs by user signal and intent" *[from Slide 10 node `1214:19909`]*. **Della to confirm.**
- **eyebrow:** `FRAMEWORK · USER TARGETING` *[from Slide 10 node `1214:19909`]*
- **slide-derived lede** (NEW, from Slide 10 node `1214:19909`):
  > We can target beneficial experiences by understanding a user's goal and what we know about them.
- **body — paragraph 1** (existing line 261, verbatim):
  > The strategy sat on **two axes: signal and intent**. By reading the signal Reddit has from a user and what they're trying to do on the platform, we could infer what experiences they were having and prioritize notification types accordingly. The inbox drives **2% of all comments on Reddit**—that figure shifted leadership investment across the board.

  *[Note: see Position 4 about whether to dedupe the 2% datapoint.]*
- **body — paragraph 2** (existing line 263, verbatim):
  > The first decision was where to start. **Comment replies were the highest-usage surface**—core users with strong opinions about their flows. Changing that experience could disrupt the one thing the inbox was actually working for. The alternative: open **net-new growth** for subreddit following and new users with completely empty inboxes. Less data, more assumptions, required research—but the upside was coverage where we had next to none.
- **2x2 matrix labels** *[from Slide 10 node `1214:19909`]*:
  - Column LOW SIGNAL — "Build understanding of user"
  - Column HIGH SIGNAL — "Deliver user preferences"
  - Row LOW INTENT — "Provide the user guidance"
  - Row HIGH INTENT — "Empower the user to achieve goals"
  - Quadrant labels: NEW USER · Casual scroller · Casual seeker · Core contributor

  **Open question — Della: quadrant labels differ from v2 NOT-E4 ("New user / Scroller / Seeker / Contributor"). Slide adds "Casual" / "Core" prefixes. Use slide labels (more specific) and retranslate diagram?**

- **Diagram:** `diagram-not-e4-signal-intent-matrix-v5.html` *[v2 spec §5, on disk; retranslate if quadrant labels updated]*
- **Verified facts:** "2% of all comments on Reddit" *[from `verified-facts-registry.md`]*
- **Position 9 ship criteria:**
  - Existing lines 261 + 263 prose preserved.
  - Slide quadrant labels confirmed; diagram retranslated if needed.

---

### Position 10 — `<h3>Strategic pillars</h3>` (existing, kept)

- **heading rewrite candidate:** "Three pillars to journey optimization" *[from Slide 11 node `1214:20645`]*. **Della to confirm.**
- **eyebrow:** `STRATEGY` *[from Slide 11 node `1214:20645`]*
- **body prose** (existing line 291, verbatim):
  > Three pillars implement the strategy across the inbox: **build habits**, **enable curation**, **create focus**. Each pillar maps to a phase of the work that follows—and each builds on what the previous phase made possible.
- **3-pillar one-liners** *[from Slide 11 node `1214:20645`]*:
  - 01 · Build habits — "Engagement loops that compound over time."
  - 02 · Enable curation — "Customized feeds surface the highest-signal content."
  - 03 · Create focus — "Reduced noise means higher quality time on platform."

  These one-liners are NEW — should be added to NOT-E3 diagram. **Verify on-disk `diagram-not-e3-strategic-pillars-v5.html` includes them; retranslate if drift.**
- **Diagram:** `diagram-not-e3-strategic-pillars-v5.html` *[v2 spec §5, on disk]*
- **Position 10 ship criteria:**
  - Existing line 291 prose preserved.
  - On-disk diagram one-liners match slide.

---

### Position 11 — `<h2>1. Build Habits</h2>` + `<h3>Intelligent defaults &amp; feedback loops</h3>` (existing, kept)

- **h2 wrapper** (existing line 303): `<h2>1. Build Habits</h2>` — kept.
- **heading rewrite candidate:** Slide 12 title is "Every notification tells you why you got it." — punchy first-person framing. v2 has "Intelligent defaults & feedback loops". **Della to choose: keep technical heading, swap for slide's voice-first heading, or use both (h3 = slide title, sub-eyebrow = "Intelligent defaults & feedback loops")?**
- **slide-derived lede** (NEW, from Slide 12 node `1214:20054`):
  > Contextual framing replaced generic copy — users engage when the system shows its reasoning.
- **body — paragraph 1** (existing line 307, verbatim):
  > Users had a **bias for action** in the inbox. The more content was framed as personally actionable, the more likely they were to engage.
- **body — paragraph 2** (existing line 309, verbatim):
  > I added copy showing *why* a user received each notification. **Click-through doubled** compared to generic framing, and the surface could support higher volume without overwhelming users.
- **body — paragraph 3** (existing line 311, verbatim):
  > I shipped **decay logic** for breaking news, recommendations, and subreddit updates: if a user doesn't open a notification type after a threshold, the system asks whether to turn it off. The ML team ran parallel experiments on signal thresholds while I defined the user-facing behavior—a **continuous dialogue** between design and engineering, each side's findings reshaping the other's approach.
- **impact callout** *[from Slide 12 node `1214:20054`]*:
  - Metric: "×2"
  - Body: "click-through on contextualized notifications vs. generic framing."
  *[matches verified-facts: "×2 click-through (contextualized framing)"]*
- **Diagram:** `diagram-not17-context-defaults-v5.html` *[v2 spec §5; net-new in v2]*
- **Position 11 ship criteria:**
  - Existing lines 307 + 309 + 311 prose preserved.
  - Heading choice resolved.
  - ×2 callout rendered.

---

### Position 12 — `<h3>Push-to-inbox connection</h3>` (existing, kept)

- **heading rewrite candidate:** "History, not just the latest." *[from Slide 13 node `1214:20080`]*. Punchy, declarative. **Della to choose.**
- **slide-derived lede** (NEW, from Slide 13 node `1214:20080`):
  > Each new push wiped older ones from the inbox; which defied user expectations and interrupted discovery. I restored the history — discovery flows stay intact mid-stream.
- **body — paragraph 1** (existing line 325, verbatim):
  > For low-subscription users, the inbox became an **onboarding engine**. Recommendations surfaced contextually; push landing experiences converted discovery into lasting signal. DAU for that cohort lifted **+1.4%**; push click-through rose **+6.4%** across 7.5M daily inbox users.
- **body — paragraph 2** (existing line 327, verbatim):
  > Only the latest push recommendation appeared in the inbox. Users expected a **history of communications**—removing older recommendations cut off discovery flows mid-stream. I restored that connection. Push good visits climbed **+1%** across 15 million daily receives.
- **impact callout** *[from Slide 13 node `1214:20080`]*:
  - Metric: "+1%"
  - Body: "push good visits — the continuity fix compounded across the full send volume."
  *[matches verified-facts: "+1% push good visits (continuity fix)"]*
- **before/after row stack** (visualization in slide; already represented in NOT-06 per v2 spec §5):
  - BEFORE — LATEST ONLY (1 of 3 visible)
  - AFTER — HISTORY PRESERVED (3 of 3 visible)
- **Diagram:** `diagram-not06-push-to-inbox-v5.html` *[v2 spec §5, on disk]*
- **Verified facts:** +1.4% DAU, +6.4% push CTR, 7.5M daily inbox users, +1% push good visits, 15M daily push receives *[from `verified-facts-registry.md`]*
- **Position 12 ship criteria:**
  - Existing lines 325 + 327 prose preserved (both paragraphs land here).
  - +1% callout rendered.

---

### Position 13 — `<h2>2. Enable Curation</h2>` + `<h3>Pipeline separation</h3>` (existing, kept)

- **h2 wrapper** (existing line 339): `<h2>2. Enable Curation</h2>` — kept.
- **heading rewrite candidate:** "Separating what you asked for from what we recommend." *[from Slide 14 node `1214:20146`]*. **Della to choose.**
- **slide-derived lede** (NEW, from Slide 14 node `1214:20146`):
  > Subscriptions used to compete with algorithmic recommendations in the backend. I rebuilt the pipeline with the ML team — user signal won over engagement metrics.
- **body prose** (existing line 343, verbatim):
  > Subreddit subscriptions were **entangled with recommendations** on the back end. The system weighted a recommended notification the same as a subscribed update—prioritizing engagement metrics (post performance, CTR) over what users had explicitly asked for. A user subscribing to r/all updates would get a viral r/PlayStation recommendation instead. I worked with the **ML team to untangle the pipeline**—they ran experiments on signal weighting while I redesigned the preference model, each side's findings reshaping the other's direction until **user signal won over algorithmic signal**.
- **before/after pipeline visualization** *[from Slide 14 node `1214:20146`]*:
  - BEFORE: SUBSCRIPTIONS + RECOMMENDATIONS → single RANKER → USER INBOX (subscriptions get drowned by recommendations)
  - AFTER: SUBSCRIPTIONS → direct path; RECOMMENDATIONS → RANKER (weighted by user signal first) → USER INBOX (subscriptions priority-routed)

  Verify on-disk `diagram-not19-pipeline-entanglement-v5.html` reflects this dual-pipeline AFTER state. v2 spec §5 says the diagram is "two parallel pipelines (User subscriptions / Discovery suggestions) feeding into a single Ranker, with the result favoring discovery over subscriptions" — that may describe the BEFORE state only. Retranslate to add the AFTER side if needed.
- **Diagram:** `diagram-not19-pipeline-entanglement-v5.html` *[v2 spec §5, on disk; possibly needs retranslation]*
- **No impact callout on this slide.** Metrics for pipeline separation roll up under Slide 16 / Position 15 (Growth flywheel).
- **Position 13 ship criteria:**
  - Existing line 343 prose preserved.
  - Diagram verified against slide before/after.

---

### Position 14 — `<h3>Preference architecture &amp; subreddit on-ramps</h3>` (MERGED — v2 Rows 20 + 21)

- **heading rewrite candidate:** "Preferences at the point of decision." *[from Slide 15 node `1214:20255`]*. Captures both v2 row 20 (architecture) and v2 row 21 (on-ramps) in one beat. **Della to choose merged heading.**
- **slide-derived lede** (NEW, from Slide 15 node `1214:20255`):
  > Subscription settings used vague and hidden under an overflow; I collaborated with eng to establish concrete options. Then, I surfaced them on the subreddit page itself.

  **Note:** slide subtitle has a typo or unusual phrasing — "Subscription settings used vague" likely should be "were vague" or "used to be vague". Captured verbatim per "preserve typos" rule. **Della to confirm or correct before publishing.**
- **body — paragraph 1** (existing line 357, verbatim — v2 Row 20):
  > The back end couldn't define what updates a user could receive from a subreddit. Options were **off, low, and frequent**—even internally, the team couldn't explain what those meant because they were wrapped in algorithmic metrics. I worked with the engineering lead through **weekly syncs on capacity and feasibility** to rearchitect preferences: **no updates, popular posts, all posts**. Eng held deep knowledge of system behavior and limitations—every conversation surfaced another constraint, but each one guided us toward a more precise model.
- **body — paragraph 2** (existing line 371, verbatim — v2 Row 21):
  > I then surfaced these preferences **on the subreddit page itself**—point of decision, not buried three screens deep.
- **before/after annotations** *[from Slide 15 node `1214:20255`]*:
  - BEFORE: 1. "Vague options set unclear expectations"  2. "Unclear path to preferences"
  - AFTER: 1. "Clearly defined update preferences"  2. "Preference visible in header"
- **Diagrams:**
  - `diagram-not07-preference-architecture-v5.html` (Row 20) *[v2 spec §5, on disk]*
  - `diagram-not08-subreddit-onramps-v5.html` (Row 21) *[v2 spec §5, on disk]*

  **Open question — Della: keep both diagrams stacked, or commission a single combined diagram (matching slide structure: subreddit-page + settings-detail per side)?**
- **Position 14 ship criteria:**
  - Existing line 357 + line 371 prose preserved.
  - Merged heading confirmed.
  - Subtitle typo resolved.
  - Diagram structure decided.

---

### Position 15 — `<h3>Growth flywheel</h3>` (relocated from v2 Row 15)

This row moves from Frameworks group → into Enable Curation group per v3 handoff Move 4.

- **heading rewrite candidate:** "The flywheel: signal compounds over time." *[from Slide 16 node `1214:19972`]*. **Della to choose.**
- **slide-derived lede** (NEW, from Slide 16 node `1214:19972`):
  > Intelligent defaults and feedback loops that auto-enroll and auto-exit users based on signal and engagement.

  *[Note: this lede adds operational mechanism detail not in v2 row 15 prose.]*
- **body prose** (existing line 277, verbatim):
  > With taxonomy and targeting in place, the system becomes a growth flywheel. Reading signal lets us deliver value; delivering value generates more signal; the loop tightens with each cycle. The inbox shifts from a passive feed to an active driver of engagement and platform understanding.
- **3-stage flywheel content** *[from Slide 16 node `1214:19972`]*:
  - 01 · **Capture signal** — Geo recs, Search, Good visits, Post views, Contribution
  - transition: "Signal feeds value"
  - 02 · **Deliver value** — User following, Keyword following, Post following, Replies, Activity insights
  - transition: "Value refines tuning"
  - 03 · **Tune experience** — App upsell, Enable push, Follow suggestions, Event reminders
  - return loop: "↻ Tuning strengthens signal"

  **Open question — Della: do you want these specific Reddit-internal mechanism names in the case study, or stay with the conceptual loop labels (Leverage signal → Deliver value → Tune experience) from v2 NOT-E2?** Slide stage 1 label is "Capture signal" (v2 had "Leverage signal").

- **Diagram:** `diagram-not-e2-strategy-flywheel-v5.html` *[v2 spec §5, on disk; retranslate to update Stage 01 label and add per-stage items if Della wants slide content reflected]*
- **Position 15 ship criteria:**
  - Existing line 277 prose preserved (relocated from Frameworks).
  - Stage labels and item names confirmed.
  - Diagram retranslated if updated.

---

### Position 16 — `<h2>3. Create Focus</h2>` + `<h3>Surface consolidation</h3>` (existing, kept)

- **h2 wrapper** (existing line 413): `<h2>3. Create Focus</h2>` — kept.
- **heading rewrite candidate:** "Three surfaces, three mental models" *[from Slide 17 node `1214:20314`]*. Slide treats this at h1 size (64px) as a Pillar 3 opener. **Della to choose: replace h3 or use as visual emphasis above h3.**
- **slide-derived lede** (NEW, from Slide 17 node `1214:20314`):
  > Inbox, private messages, and chat each demand different sort logic, engagement pattern, and navigation.
- **body — paragraph 1** (existing line 417, verbatim):
  > Why this was hard: three surfaces with different sort logic, engagement patterns, and information architecture had to merge without breaking any of them.
- **body — paragraph 2** (existing line 419, verbatim):
  > I consolidated **four messaging systems into a single inbox**. This required deprecating one internal system, migrating another, and navigating multiple intermediate states—each shipped as a fully functional experience, not a waypoint. Eng on this team were **precise and construction-oriented**—they caught edge cases I hadn't, which made the late-stage design reviews a critical part of my process for making designs airtight before handoff.
- **3-card surface trade-offs** *[from Slide 17 node `1214:20314`]*:
  - **01 · INBOX** ("Async · destination")
    - SORT: "Static, chronological"
    - ENGAGEMENT: "Asynchronous"
    - NAVIGATION: "Leads to content pages"
    - Utilities: "Mark read, preferences"
  - **02 · PRIVATE MESSAGES** ("Async · thread list")
    - SORT: "Dynamic by recency"
    - ENGAGEMENT: "Asynchronous"
    - NAVIGATION: "Displays thread detail"
    - Utilities: "Mark read, preferences"
  - **03 · CHAT** ("Sync · live thread")
    - SORT: "Dynamic by recency"
    - ENGAGEMENT: "Synchronous"
    - NAVIGATION: "Displays thread detail"
    - Utilities: "Filter, create chat, preferences"

  **CONFIRMED — 4 attribute rows on this slide, not 3.** v2 NOT-24 spec §5 listed only 3 (Sort/Engagement/Navigation). Diagram retranslation needed to add Utilities row.
- **Diagram:** `diagram-not24-surface-tradeoffs-v5.html` *[v2 spec §5; net-new in v2; retranslate to add Utilities row]*
- **CSS impact:** `.surface-tradeoffs` table needs 4 attribute rows, not 3. See §3.
- **Position 16 ship criteria:**
  - Existing lines 417 + 419 prose preserved.
  - 4-row diagram retranslation complete.

---

### Position 17 — `<h3>Layout experimentation</h3>` (existing, kept)

- **heading rewrite candidate:** "Four layouts tested, one clear fit" *[from Slide 18 node `1214:20390`]*. **Della to choose.**
- **slide-derived lede** (NEW, from Slide 18 node `1214:20390`):
  > Migrating surfaces with muscle memory meant testing layouts that balanced scan speed against mental-model load — the inbox had to behave like a switchboard, not a feed.
- **body prose** (existing line 433, verbatim):
  > I tested **chronological, nested, and tabbed layouts**. Users wanted to navigate the inbox as little as possible—scan, act, leave. The inbox wasn't a destination—it was a switchboard that guided users through their session.

  **Note:** existing prose says "chronological, nested, and tabbed layouts" — 3 options. **Slide 18 confirms 4 options were considered.** Recommend updating prose to "I tested **four layouts** — chronological, nested, group-by-type, and tabbed." or keep "3" and note that "Move chat to header" was considered separately. **Della to decide.**

- **CONFIRMED — 4 layout options on Slide 18:**
  - Card 1 · CONSIDERED — **Move chat to header** — "Simplest mental model: separate synchronous from asynchronous updates"
    - Pro: "No risk breaking user mental models"
    - Con: "Doesn't solve multi-surface problem"
  - Card 2 · CONSIDERED — **Complete unification** — "Treat chat and notifications as equals: both communicate an update to the user"
    - Pro: "One, chronological list to rule them all"
    - Con: "Net-new interaction pattern confuses some users"
  - Card 3 · CONSIDERED — **Group activity types** — "Slack-style grouping pairs existing mental models with quick organization"
    - Pro: "Reduced navigation"
    - Con: "Difficult to scan; less scalable for high volume activity"
  - Card 4 · ✓ BEST FIT — **Organize with tabs** — "Inbox as switchboard — scan, act, leave."
    - Pro: "Fastest scan — users know where to look"
    - Con: "Requires confident IA decisions upfront"
    - Rationale: "Separates notification types into tabs users can ignore or dive into. Fastest scan speed; mental model matches existing messaging patterns."
  *[from Slide 18 node `1214:20390`]*

- **decision row** *[from Slide 18 node `1214:20390`]*:
  - eyebrow: AMBIGUITY NAVIGATED
  - body: "Chose Tabbed because scan speed was the controlling constraint — inbox as switchboard, not feed."

- **Diagram:** `diagram-not12-inbox-layout-experiments-v5.html` *[v2 spec §5; on disk with 3 options; retranslate to add 4th option "Move chat to header" + update card naming]*
- **Position 17 ship criteria:**
  - Existing line 433 prose preserved (with 3→4 decision per Della).
  - 4-option diagram retranslated.
  - "AMBIGUITY NAVIGATED" decision row rendered.

---

### Position 18 — `<h3>Navigation simplification &amp; unified inbox reveal</h3>` (MERGED — v2 Rows 26 + 27)

- **heading rewrite candidate:** "Five tabs to three" *[from Slide 19 node `1214:20580`]*. Punchy, declarative. **Della to choose merged heading.**
- **slide-derived lede** (NEW, from Slide 19 node `1214:20580`):
  > Consolidating notifications and chat into a single inbox freed a slot in the bottom nav — one surface removed from the hierarchy, one slot returned to product surface experiments.
- **body — paragraph 1** (existing line 447, verbatim — v2 Row 26):
  > The unified inbox **freed a slot in the bottom tab bar**. Reddit used that space to experiment with new product surfaces and validate navigation models—a simplified 3–4 tab structure. Impact that extended well beyond the inbox.
- **body — paragraph 2** (existing line 461, verbatim — v2 Row 27):
  > The result: one inbox, two tabs (Notifications + Chat), all messaging consolidated. The mental model is finally what users expected from the start—a single source of truth where every kind of communication lands and every kind of action is one tap away.
- **before/after nav strips** *[from Slide 19 node `1214:20580`]*:
  - BEFORE — 5 TAB LAYOUT (nav strip image)
  - AFTER — 3 TAB MODEL (nav strip image, accent border)
- **impact callout** *[from Slide 19 node `1214:20580`]*:
  - Metric: "1"
  - Sub-label: "NAV SLOT FREED"
  - Body: "Consolidating four messaging surfaces into one returned a slot to the bottom nav — the downstream effect of the inbox rebuild on surface experiments."
- **Diagrams:**
  - `diagram-not14-navigation-simplification-v5.html` (Row 26) *[v2 spec §5, on disk — covers BEFORE/AFTER nav strips]*
  - `diagram-not14-unified-inbox-v5.html` (Row 27) *[v2 spec §5; net-new with GIF placeholder]*

  **Open question — Della: Slide 19 covers nav simplification with the metric callout but does NOT include the unified-inbox internal-tabs reveal (the "Notifications + Chat tabs" UI). v2 row 27 had a separate diagram (`diagram-not14-unified-inbox-v5.html`) for that. Keep both diagrams stacked at Position 18, or fold the unified inbox UI mockup into Position 19's results visual? Recommend keep separate — the inbox's two-tab UI is a distinct visual story from the bottom-nav simplification.**

- **Position 18 ship criteria:**
  - Existing line 447 + line 461 prose preserved.
  - Merged heading confirmed.
  - "1 NAV SLOT FREED" callout rendered.
  - Diagram structure (one or two) decided.

---

### Position 19 — Strategy recap (relocated metrics-callout) + `<h2>Results</h2>` (MERGED — v2 Rows 5 + 28)

This position folds the v2 Strategy section's metrics-callout (currently at lines 120–138) into the Results section. Per v3 handoff Move 1: "v2 Row 5 (Strategy) — front to back; becomes a recap before Results."

- **strategy-recap intro** (existing line 120, verbatim):
  > **Strategy:** establish a scaleable foundation; optimize for key user journeys.
  *[Note: see Position 5 spelling decision; if Della picks "scalable," update here too.]*

  **Open question — Della: relocate this Strategy lede to Position 19 as a recap, or drop it entirely (since Position 5 Approach now covers the same idea)?** Recommend dropping — Position 5 already states the strategy via Slide 09's two numbered statements, and a recap may feel redundant.

- **h2 wrapper** (existing line 473): `<h2>Results</h2>` — kept.
- **eyebrow:** `RESULTS · UNIFIED INBOX` *[from Slide 20 node `1214:20607`]*
- **heading rewrite candidate:** "Four surfaces, one scalable system" *[from Slide 20 node `1214:20607`]*. Could replace existing line 475's plain Results paragraph framing. **Della to choose.**
- **body prose — option A** (existing line 475, verbatim):
  > The segmentation framework became the foundation for notification design across Reddit. The unified inbox reshaped app navigation and enabled product experimentation in spaces that didn't exist before.

- **body prose — option B (slide-derived)**:
  > **LEARNINGS** — Framework-first scoping made the metrics inevitable — every decision mapped back to the three pillars and the signal-intent matrix.
  *[from Slide 20 node `1214:20607`]*

  **Open question — Della: keep existing line 475 paragraph, replace with slide's LEARNINGS line, or render both?** The slide closer is staff-coded and tighter; the existing paragraph is broader and outcome-framed.

- **metrics panel** *[currently at lines 120–138 (relocated from Strategy section); also present on Slide 20 node `1214:20607` with identical values]*:
  - Hero metric: "+1.3M" · INCREMENTAL DAU · "Sustained lift across the notification and inbox ecosystem."
  - Metric: "+2.7M" · DAILY GOOD VISITS · "Quality visits attributable to push and inbox channels."
  - Metric: "+6.4%" · PUSH NOTIFICATION CTR · "Click-through on contextualized push across cohorts."
  - Metric: "75%" · ABOVE TARGET · "Notifications team exceeded annual targets."
  - Metric: "1" · NAV SLOT FREED · "Unified inbox returned one tab to experimentation"

- **unified inbox GIF** *[from Slide 20 node `1214:20607`]*:
  - Asset: screen recording of unified inbox (filename in Figma: `ScreenRecording_04-24-2026_08-55-55_1`)
  - Caption: "UNIFIED INBOX · NOTIFICATIONS + MESSAGES + CHAT IN ONE SURFACE"

  This GIF is the unified-inbox reveal. If Della chose to fold the unified-inbox UI mockup from Position 18 into this Results visual (per Position 18 open question), this is where it lands.

- **Diagram:** none. Position 19 is metrics-panel + GIF — no separate diagram embed.

#### ⚠ METRIC TRACEABILITY — IMPORTANT FINDING

The 5 metrics on Slide 20 EXACTLY match the metrics already in the deployed `case-notifications.html` metrics-callout (lines 120–138). The deployed site is the source — Slide 20 mirrored it. So slide and current HTML agree.

However, ONLY ONE of these five metrics traces directly to the verified-facts registry:

| Metric (slide + current HTML) | Verified-facts registry entry | Status |
|---|---|---|
| **+6.4% PUSH NOTIFICATION CTR** | `+6.4% push CTR` | ✓ Direct match |
| +1.3M INCREMENTAL DAU | registry has `+1.4% DAU` (% lift only) | Derivable? Della to confirm relationship |
| +2.7M DAILY GOOD VISITS | registry has `+5.4% good visits` (% lift only) | Derivable? Della to confirm relationship |
| 75% ABOVE TARGET | not in registry | ⚠ Della to add or correct |
| 1 NAV SLOT FREED | not in registry but matches Slide 19 | ✓ Internally consistent |

**Resolved 2026-04-28** — Della verbally confirmed all five metrics are correct. Registry updated with new entries (Verbal — Apr 28, 2026 [CONFIRMED]) for the absolute-headcount conversions and the nav-slot figure. The "75% above target" entry was already in the registry. All Position 19 metrics now trace cleanly to either the master resume, prior verbal confirmations, or the Apr 28 verbal confirmation. v3 spec preserves the metrics as written — proceed to HTML execution without modification.

- **Position 19 ship criteria:**
  - Strategy lede decision (Position 5 vs Position 19 vs both vs drop).
  - Heading + closing prose decision.
  - Metrics panel relocated from current lines 120–138.
  - GIF asset path confirmed (Della provides filename).
  - Verified-facts registry updated to reflect the absolute-headcount metrics + above-target figure.

---

## §3 CSS additions

These are net-new CSS classes the v3 layout introduces. Existing styles in `styles.css` continue to be used; this section lists only deltas.

```css
/* Eyebrow used at the top of major sections (replaces ad-hoc eyebrow markup) */
.section-eyebrow {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.88px;
  text-transform: uppercase;
  color: var(--color-accent, #7fb5b0);
}

/* Position 5 — Approach pivot: numbered statements with progressive emphasis */
.case-approach-pivot { margin: var(--spacing-xl) 0; }
.approach-steps {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 40px;
}
.approach-steps li {
  display: flex;
  align-items: center;
  gap: 40px;
  font-weight: 700;
  letter-spacing: -1.92px;
  line-height: 1.1;
}
.approach-steps .step-num {
  font-size: 32px;
  letter-spacing: -0.64px;
}
.approach-steps .step-text { font-size: 64px; }
.approach-steps .step-done {
  color: var(--text-tertiary, rgba(224,223,228,0.4));
}
.approach-steps .step-active {
  color: var(--text-primary, #e0dfe4);
}

/* Position 16 — Surface trade-offs: 3-card grid, 4 attribute rows per card (UPDATED from v2's 3 rows) */
.surface-tradeoffs {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}
.surface-tradeoffs .card {
  background: var(--surface-1, #10121c);
  border: 1px solid var(--border-subtle, rgba(224,223,228,0.04));
  border-radius: 14px;
  padding: 32px;
}
.surface-tradeoffs .attr-rows {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.surface-tradeoffs .attr-row {
  display: flex;
  gap: 20px;
  align-items: center;
}
.surface-tradeoffs .attr-label {
  width: 152px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.88px;
  text-transform: uppercase;
  color: var(--text-tertiary);
}
.surface-tradeoffs .attr-value {
  flex: 1;
  font-size: 16px;
  color: var(--text-secondary);
}

/* Impact callout — used at Positions 4 (2%), 11 (×2), 12 (+1%), 18 (1 NAV SLOT FREED) */
.impact-callout {
  display: flex;
  gap: 24px;
  align-items: center;
  padding: 24px 32px;
  background: var(--surface-1);
  border: 1px solid var(--color-accent);
  border-radius: 10px;
}
.impact-callout .metric {
  font-size: 64px;
  font-weight: 700;
  letter-spacing: -1.92px;
  line-height: 1.1;
  color: var(--color-accent);
}
.impact-callout .body {
  flex: 1;
  font-size: 24px;
  font-weight: 600;
  letter-spacing: -0.48px;
  line-height: 1.2;
  color: var(--text-primary);
}

/* Pillar tag chips — small breadcrumb showing 3 pillars with active state */
/* OPTIONAL — only ship if Della wants visual breadcrumbs at Pillar h2 sections */
.pillar-tags { display: flex; gap: 5px; align-items: center; padding-bottom: 16px; }
.pillar-tag { padding: 3px 8px; border-radius: 3px; font-size: 8.5px; font-weight: 600; letter-spacing: 0.68px; text-transform: uppercase; border: 1px solid var(--text-tertiary); color: var(--text-tertiary); }
.pillar-tag.active { padding: 4px 11px; font-size: 12px; letter-spacing: 0.97px; border: 1.1px solid var(--color-accent); color: var(--color-accent); border-radius: 4.5px; }
```

---

## §4 5-batch execution plan

The v2 spec used 4 batches; v3 adds Position 5 (Approach) and consolidates Rows 8+9, 20+21, 26+27 — net result is roughly the same scope, executable in 5 batches with Della preview between each.

**Pre-flight (do FIRST, after Della signs off on this spec):**
```bash
cd /Users/della/CoworkWorkspace/Get-a-job/portfolio-site
# v3 working baseline already at commit 781e8f1 ("v3 pre-refactor snapshot — case-notifications.html copied to case-notifications.html.v2-bak")
# branch case-notifications-figma-rearrange-v2 is ahead of origin by 12 commits — do NOT push
git status  # confirm clean working dir
```

**Batch 1 — Positions 1–5 (Summary + Challenge + 3 different inboxes + engagement funnel + Approach NEW):**
The most novel/restructured part of the refactor. Includes:
- New eyebrow + lede inserts at Positions 1, 2, 3, 4
- Move v2 Row 10 prose (line 201) to Position 3
- Move v2 Row 12 prose (line 231) to Position 4
- Insert NEW Position 5 Approach (Slide 09) after Position 4
- Retire v2 Rows 3 (line 90–102) and 4 (line 104–116) — h3s, paragraphs, and diagram embeds removed
Single commit. Della previews in browser before continuing.

**Batch 2 — Positions 6–8 (Foundation + Scaleable + Swipe + Unread merged):**
- Existing prose stays in place (lines 145, 159, 173, 187)
- Slide 06/07/08 ledes inserted
- Position 8 merges Rows 8 + 9 (h3 collapsed to single "Unread system" or similar; both paragraphs and both diagrams land at Position 8)
- Heading renames per Della decisions
Single commit. Della previews.

**Batch 3 — Positions 9–12 (Frameworks + User targeting + Strategic pillars + Build Habits + Push-to-inbox):**
- Existing prose stays in place (lines 261, 263, 277 [relocated to Position 15 — see Batch 4], 291, 307, 309, 311, 325, 327)
- Retire v2 Row 13 (line 245–257) — Activity prioritization
- Slide ledes inserted
- ×2 callout at Position 11
- +1% callout at Position 12
- Move v2 Row 15 prose (line 277) OUT of Frameworks group — held until Batch 4
Single commit. Della previews.

**Batch 4 — Positions 13–15 (Enable Curation + Pipeline + Preferences merged + Growth flywheel relocated):**
- Existing prose stays in place (lines 343, 357, 371)
- Position 14 merges Rows 20 + 21 (both paragraphs land here)
- Move v2 Row 15 prose (line 277) INTO this group as Position 15
- Retire v2 Row 22 (line 383–395) — Contextual suggestions
- Retire v2 Row 23 (line 397–411) — Global settings
- Slide ledes inserted
- Diagram retranslations (NOT-19, NOT-07, NOT-08 merge if Della approves, NOT-E2 retitle)
Single commit. Della previews.

**Batch 5 — Positions 16–19 (Create Focus + Layout + Nav merged + Results merged):**
- Existing prose stays in place (lines 417, 419, 433, 447, 461, 475)
- Position 17 prose updated 3→4 layouts per Della decision
- Position 18 merges Rows 26 + 27 (both paragraphs land here)
- Position 19 folds metrics-callout from current lines 120–138 into Results section
- Strategy lede decision (drop / Position 19 recap / both)
- Diagram retranslations (NOT-12 4-option, NOT-24 4-row utilities)
- LEARNINGS source-strip line added to Position 19
Single commit. Della previews.

After each batch:
- Commit message: `case-notifs v3 batch N: positions X-Y`
- Run `grep -c` audit against this spec's Position table to confirm every existing line still appears (or is on the explicit retirement list).
- Run `python3 portfolio-site/voice-check.py case-notifications.html` and resolve any hits.
- Run `python3 portfolio-site/quality-check.py case-notifications.html` for HTML/a11y/links.
- Take a screenshot of the affected positions and review.

### Rollback ladder
- Misplaced paragraph → edit in place.
- Whole batch broken → `git reset --hard HEAD~1`.
- Catastrophic → `cp case-notifications.html.v2-bak case-notifications.html` (the v3 working baseline).

---

## §5 Out-of-scope

- **Mobile siblings** for the 16+ on-disk diagrams. Existing `data-mobile-pending="true"` markers stay until figma-to-html produces `-mobile.html` companions.
- **Diagram visual updates** beyond the retranslations explicitly listed (NOT-12 add 4th option, NOT-24 add Utilities row, NOT-E3 verify pillar one-liners, NOT-E4 verify quadrant labels, NOT-E2 verify stage 1 label). All other on-disk diagrams stay as-is unless drift is observed.
- **Cross-case-study consistency** — eyebrow/lede/callout patterns introduced here may eventually propagate to case-ai, case-sharing, case-subreddit, case-building-portfolio. That's a separate scope.
- **Verified-facts-registry updates** — the metric discrepancy at Position 19 needs Della to either add new entries or correct existing ones. That maintenance happens in `verified-facts-registry.md` independently of this HTML refactor.
- **Slide 09 Approach connective copy** — if Slide 09's two numbered statements aren't enough body for Position 5, any added prose comes from Della directly (per resume-prompt non-negotiable).
- **HTML execution itself** — this spec doc is the deliverable for this scope. Claude Code (or a separate Cowork thread) executes the 5-batch plan after Della signs off.
- **About-page push to main** — separate scope per resume prompt; do not touch in v3 execution.

---

## §6 Open questions for Della (consolidated)

These questions block clean HTML execution. Recommend Della answers all before Batch 1 starts.

### Critical (blocks HTML execution)

1. ~~Position 19 metric discrepancy~~ ✅ **RESOLVED 2026-04-28** — Della verbally confirmed the slide + HTML metrics are correct. Registry updated with `+1.3M incremental DAU`, `+2.7M daily good visits`, and `1 nav slot freed` as Verbal — Apr 28, 2026 [CONFIRMED]. The "75% above target" entry was already in the registry from Apr 11. All Position 19 metrics now trace.

2. **"scalable" vs "scaleable" spelling** — slide uses "scalable"; current HTML uses "scaleable" at lines 120 + 141. Pick canonical form for v3 and apply everywhere.

3. **Position 5 connective copy** — Slide 09 is heading-only. Position 5 may need a one-line transition. Della to write or skip.

4. **Position 8 unread system merge** — combine v2 Row 8 + Row 9 into single h3 (e.g., "Unread system"). Confirm merged heading text. Confirm whether to keep both diagrams stacked or commission a single combined diagram.

5. **Position 14 "Subscription settings used vague" typo** — slide subtitle has typo or unusual phrasing. Correct or preserve.

6. ~~Position 17 layout count~~ ✅ **RESOLVED 2026-04-28** — Della verbally confirmed 4 layouts. Existing line 433 prose ("chronological, nested, and tabbed layouts") needs updating during Batch 5 to reflect the four-option set: Move chat to header, Complete unification, Group activity types, Organize with tabs.

### High-priority (heading rename decisions — affects HTML structure)

For each of these, Della picks one of: (a) keep v2 heading, (b) replace with slide title, (c) render both as h3 + sub-eyebrow:

7. Position 1 Summary — slide title "From fragmented legacy to unified system"
8. Position 2 — slide three-beat "Four systems. Three platforms. Six years."
9. Position 3 — slide title "Three activity levels. Three problems."
10. Position 4 — slide title "The inbox drives engagement; but not for everyone"
11. Position 6 — slide title "Create a global inbox row component"
12. Position 9 — slide title "Identify needs by user signal and intent"
13. Position 10 — slide title "Three pillars to journey optimization"
14. Position 11 — slide title "Every notification tells you why you got it."
15. Position 12 — slide title "History, not just the latest."
16. Position 13 — slide title "Separating what you asked for from what we recommend."
17. Position 14 (merged) — slide title "Preferences at the point of decision."
18. Position 15 — slide title "The flywheel: signal compounds over time."
19. Position 16 — slide title "Three surfaces, three mental models" (slide treats at 64px h1)
20. Position 17 — slide title "Four layouts tested, one clear fit"
21. Position 18 (merged) — slide title "Five tabs to three"
22. Position 19 — slide title "Four surfaces, one scalable system"

### Structural questions

23. **Foundation as Pillar 1?** Slide 06 calls itself "PILLAR 1" but slides 12–19 show only 3 numbered pillars (Build Habits / Enable Curation / Create Focus). Recommend treating Foundation as pre-pillar; eyebrow drops "PILLAR 1".

24. **Slide 03 cohort labels** — use slide names (NEW USER / Casual user / Core user) or v2 prose names (new user / subscriber / contributor)?

25. **Slide 10 quadrant labels** — use slide names (NEW USER / Casual scroller / Casual seeker / Core contributor) or v2 NOT-E4 names (New user / Scroller / Seeker / Contributor)?

26. **Pillar tag chips** — Slides 12/13/14/15/16/17/18/19 all show 3-pillar breadcrumb chips at the top. Render in v3 HTML or skip?

27. **EXPERIMENT/RESULT microformat** at Position 7 — render as small structured block (with casual-warm accent) or fold into prose?

28. **Position 4 / Position 9 — 2% datapoint** — current line 261 cites "2% of all comments". Slide 04 also features 2% as a hero callout. Dedupe or render in both places?

29. **Position 19 strategy recap decision** — drop the v2 Strategy lede (line 120) entirely (Position 5 covers it), or relocate as a recap before Results?

30. **Position 18 unified-inbox UI** — Slide 19 covers nav simplification but not the inbox's two-tab UI reveal. Keep `diagram-not14-unified-inbox-v5.html` as a separate visual at Position 18, or fold into Position 19 Results?

### Diagram retranslation decisions

31. **NOT-E3** — verify pillar one-liners match Slide 11 ("Engagement loops that compound over time." etc.). Retranslate if drift.
32. **NOT-E4** — quadrant labels per question 25.
33. **NOT-E2** — Stage 1 label ("Capture signal" vs "Leverage signal") + per-stage item lists.
34. **NOT-12** — add 4th layout option "Move chat to header" at the start; update card naming to match slide.
35. **NOT-24** — add Utilities attribute row (4 rows total).
36. **NOT-19** — verify diagram shows both BEFORE (entangled) and AFTER (separated) pipeline states.
37. **NOT-07 + NOT-08 merge** at Position 14 — keep separate or commission combined diagram.

---

## Spec doc footer

**Slide extractions:** all 19 slides captured to `~/CoworkWorkspace/Get-a-job/working/v3-slide-extractions.md` via direct `mcp__Figma__get_design_context` calls in this thread. No subagents. Slide 01 verification confirmed direct fetches are reliable (every field matched the resume-prompt's verification anchor).

**Voice check:** run `python3 portfolio-site/voice-check.py portfolio-site/working/planning-docs/case-notifications-change-outline-v3.md` against this file before declaring done.

**Next step (after Della reviews):**
1. Della answers §6 open questions.
2. Spec is updated with her decisions baked in.
3. Spec passes voice-check.
4. Claude Code (or a separate Cowork thread) executes Batch 1.
5. BUILD-LOG entry added documenting the spec creation.

**Resume prompt:** archive `~/CoworkWorkspace/Get-a-job/sessions/resume-prompt-case-notifications-v3-spec-extraction.md` to `~/CoworkWorkspace/Get-a-job/sessions/archive/` once Della signs off on this spec.
