# case-notifications.html — Change Outline (Figma → HTML, v2)

**Status:** All rows visually audited. All decisions resolved. Paste-ready for Claude Code.

**Source of truth:** Figma node `29:43` in file `TArUrZsBUocaAsqetjXq7V` — "Portfolio — Image Inventory" canvas, "1. Notifs & Inbox" page. 27-row vertical column.
**Target file:** `case-notifications.html` (project root).
**Diagram folder:** `img/diagrams/`.
**Working folder:** `working/planning-docs/` for this doc + the in-progress refactor manifest.

## Ground rule

Existing case-study prose is preserved verbatim and rearranged into the new structure. **The only prose deletions** are the two items explicitly marked retire on the Figma canvas:
1. `<h3>Pinned contributions</h3>` block (current lines 265–267). Sticky on NOT-13: *"retire; never shipped."*
2. The cross-channel coordination paragraph (current line 220). NOT-11 v2 also retired (sticky: *"retire?"* — Della confirmed).

Everything else moves; nothing else is dropped.

---

## §1 Per-row spec

Every row's heading, prose source, diagram source, and any treatment notes. No deferred decisions.

---

### Row 1 — `<h2>Summary</h2>` (NEW — executive summary block)

A new opening section between the hero/meta and the `<h2>Challenge</h2>` body. Sits above all current case-study prose.

**Structure:** Summary header, paired Challenge | Strategy tiles (existing prose verbatim), then NOT-03 v1 hover-annotated visual TL;DR.

```html
<section class="case-summary">
  <h2>Summary</h2>
  <div class="summary-pair">
    <div class="summary-tile">
      <h3>Challenge</h3>
      <p>[existing line 53 paragraph verbatim — "Reddit communicates with hundreds of millions..."]</p>
    </div>
    <div class="summary-tile">
      <h3>Strategy</h3>
      <p>[existing line 57 paragraph verbatim — "I built the segmentation framework..."]</p>
    </div>
  </div>
  <div class="case-img-full diagram-embed" data-diagram="not-03" data-mobile-pending="true">
    <iframe src="img/diagrams/diagram-not03-full-inbox-redesign-v5.html" loading="lazy" scrolling="no" title="Full Inbox Redesign — hover-annotated before/after with 4 paired bullets" style="width: 100%; border: none; border-radius: 12px; overflow: hidden;"></iframe>
  </div>
</section>
```

**CSS expectation:** `.summary-pair` is a 2-column flex/grid on desktop, stacks to 1-column at the mobile breakpoint. `.summary-tile` carries the existing card/quote styling (or a new minimal one).

The Strategy heading replaces the current page's "Solution" heading. The original Solution `<h2>` (current line 55) goes away — its prose lives inside this Summary tile.

**Diagram:** NOT-03 v1 hover-annotated migration diagram (Figma node `273:2`). HTML file already on disk. Includes "HOVER ANNOTATIONS TO SEE LINKED CHANGES" interaction, Before/Legacy vs After/Unified wireframes, 5 paired bullets each side, Technical-kickoffs callout footer.

**`metrics-callout` (current lines 59–76) leaves the hero** and lands in row 5.

---

### Row 2 — `<h2>Challenge</h2>` opening + `<h3>No overarching strategy</h3>`

The existing `<h2>Challenge</h2>` (current line 51) is **kept** as the wrapper for rows 2–4. The current Challenge paragraph (line 53) **already lives in the Summary tile (row 1)**; it does NOT repeat here. Row 2's body is a new beat that expands the problem.

**Prose** (drafted from Figma row text):
> Beyond fragmentation, the surfaces had no overarching user strategy: limited inventory, limited controls, no prioritization model. Push notifications, the inbox, private messages, and chat operated independently — each with a distinct content type and no shared architecture.

**Diagram:** **2i — Disconnected surfaces comparison** (Figma node `1170:766` desktop / `1173:966` mobile). Net-new HTML diagram, 4-column desktop / vertical-stacked mobile: Push Notifications | Inbox | Private Messages | Chat, each with a UI mockup + bullet captions describing its independent content/channel role.

→ HTML to translate from Figma. Filename: `diagram-not02b-disconnected-surfaces-v5.html` + `-mobile.html`.

---

### Row 3 — `<h3>Notification taxonomy gap</h3>`

**Prose** (drafted):
> The four surfaces also had no shared notion of *what* a notification is. Across the platform, every type — from push recommendations to comment replies — flowed through the same pipe with the same weight. Without a taxonomy, there was no way to prioritize, no way to set delivery rules, no way to reason about what users should see.

**Diagram:** **NOT-E5 — Three Categories of Notifications** (Figma node `508:35`). HTML file already on disk: `diagram-not-e5-notification-taxonomy-v5.html`. Discovery / Following / Conversation with example chips.

→ Embed at row 3.

---

### Row 4 — `<h3>Decaying retention</h3>`

**Prose** (drafted, pulls Day-5/12%/40%/28-point numbers directly from the diagram per Della's preference):
> The inbox had a structural retention problem. By day 5 of the post-cohort window, inbox notification usage drops to 12% while overall Reddit retention holds at 40% — a 28-point gap that compounds across 7.5M daily inbox users. That gap is the opportunity the notification strategy targets.

**Diagram:** **NOT-E1 — Cross-Platform Cohort Decay** (Figma node `409:2`). HTML file already on disk: `diagram-not-e1-cohort-decay-v5.html`. Retention curves with key-insight callout.

→ Embed at row 4.

---

### Row 5 — `<h2>Strategy</h2>` (the reveal — new wrapper)

A new `<h2>` between Challenge and the rest of the case study. Holds the strategy framing line + the metrics-callout (relocated out of the hero).

**Prose** (drafted from Figma row text):
> **Strategy:** establish a scaleable foundation; optimize for key user journeys.

The existing Solution paragraph (current line 57) **does not repeat here** — it lives only in the row 1 Summary tile (Option A confirmed).

**Visual:** the existing `metrics-callout` block (current lines 59–76) — relocated out of the hero into this section, positioned just below the Strategy framing line.

```html
<section class="case-strategy">
  <h2>Strategy</h2>
  <p class="strategy-lede"><strong>Strategy:</strong> establish a scaleable foundation; optimize for key user journeys.</p>
  <div class="metrics-callout">
    <!-- existing metrics-callout markup, moved verbatim from hero -->
  </div>
</section>
```

→ No diagram embed.

---

### Row 6 — `<h2>Scaleable foundation</h2>` opening + `<h3>Inbox row component</h3>`

The current `<h2>Foundation</h2>` (line 86) is **renamed to `<h2>Scaleable foundation</h2>`**. Wraps rows 6–10.

**Prose** (existing line 90 verbatim):
> The inbox wasn't on Reddit's design system. Every component was a one-off engineer build—growing technical debt, no quality assurance, and each new feature built from scratch. I designed the inbox row component as a scalable, reusable unit intended for distributed messaging surfaces across the platform, then migrated the full surface to the design system. Every project ran through a technical kickoff with the eng IC picking up the work—pressure-testing edge cases, building buy-in, and aligning on decisions before a line of code was written.

**Diagram:** **NOT-02 v2** (Figma node `707:112`). HTML file on disk: `diagram-not02-inbox-row-unit-v5.html`. **Verify v2 visual matches** (4 numbered annotation pairs + HOVER ANNOTATIONS treatment); if older, retranslate from Figma via the figma-to-html skill.

**NOT-03 is removed from this row** — already used in row 1 Summary.

---

### Row 7 — `<h3>Swipe actions</h3>` (reframed from "Inbox simplification")

**Prose** (existing line 130 verbatim):
> I removed the overflow menu, icon-based message type indicators, and segmented inbox sections that pushed content below the fold. Icons had low comprehension—I replaced them with clear, embedded copy. Swipe actions and long press handled secondary options. Engagement held steady.

**Diagram:** **7i — EASY ACCESS SWIPE ACTIONS** (Figma node `1173:1127` desktop / `1173:1230` mobile). Net-new HTML diagram with a single notification card AND a screen placeholder area where Della will fill in a GIF showing the swipe interaction. Build the HTML container with the placeholder; Della inserts the GIF asset later.

→ HTML to translate from Figma. Filename: `diagram-not02b-swipe-actions-v5.html`. Container should have a labeled `<div class="gif-placeholder">` slot.

---

### Row 8 — `<h3>Unread hierarchy</h3>`

**Prose** (existing line 114 verbatim):
> I rebuilt the unread system around progressive disclosure: a single numeric badge at the inbox level, a dot indicator at the tab level, typography plus subtle color at the row level. Every badge mapped 1:1 to a visible item—users never had to do math.

**Diagram:** **NOT-04 v2** (Figma node `745:29`). HTML file on disk: `diagram-not04-unread-hierarchy-v5.html`. **Verify v2 visual matches** (3-column hover-annotated breakdown: Inbox / Tab / Row, with footer icons); retranslate from Figma if older.

---

### Row 9 — `<h3>Unread color fix</h3>`

**Prose** (existing line 126 verbatim):
> The migration introduced a less prominent unread color and click-through dropped. I used the data to identify the cause, partnered with the design systems team to adjust, and the fix influenced design system usage beyond the inbox.

**Diagram:** **9i — Unread color before/after** (Figma node `1176:1630` desktop / `1176:1597` mobile). Net-new HTML diagram, two-card before/after: "Unread v1: Low contrast hides unread content" vs "Unread v2: Higher contrast restores engagement." The colored rectangles in the cards ARE the actual content (literal color samples), not placeholders.

→ HTML to translate from Figma. Filename: `diagram-not04b-unread-color-fix-v5.html`.

---

### Row 10 — `<h3>Three different inboxes</h3>`

**Prose** (drafted; row 4 confirmed approved):
> Strategy doesn't translate without understanding who's receiving the notification. Three user journeys define the inbox experience, and each surfaces a different problem: new users see an empty state, subscribers can't customize what they see, and contributors get crowded with activity that doesn't surface what matters.

**Diagram:** **10i — Three user journeys** (Figma node `1176:1726` desktop / `1176:1764` mobile). Net-new HTML diagram, 3-column user-journey comparison with full mobile inbox UI mockups: NEW USER (empty state — "The inbox is empty") | SUBSCRIBER (a few notifications — "The inbox is hard to customize") | CONTRIBUTOR (many notifications — "The inbox is crowded").

→ HTML to translate from Figma. Filename: `diagram-not10-three-inboxes-v5.html`.

**This row has no equivalent in the current case study — it is a net-new connecting beat.**

---

### Row 11 — `<h2>Push paradox &amp; engagement reality</h2>` opening + `<h3>The push paradox</h3>`

New `<h2>` wrapper between Scaleable foundation and Frameworks. Wraps rows 11–12.

**Prose** (drafted — net-new):
> Anecdotally, users reported push notifications as overwhelming and annoying. But the data told a different story — push recommendations were a key DAU driver with strong click-through. The behavior contradicted the sentiment, and any push strategy had to live in that tension.

**Diagram:** **NOT-E6 — Butterfly Chart** (Figma node `710:1163`). HTML file on disk: `diagram-not-e6-butterfly-chart-v5.html`. Inbox-above / push-below dual-axis bars across Comment reply, Post reply, Recommendations, Subscriptions.

---

### Row 12 — `<h3>Inbox engagement funnel</h3>`

**Prose** (drafted — net-new):
> The inbox itself wasn't a discovery surface — it was a contribution surface. 7.5M DAU enter the inbox; 47% click through; 75% of those go on to contribute. That funnel is shaped almost entirely by Core users — Casual, Resurrected, and New cohorts barely make it past the first step. The inbox was serving only the most engaged.

**Diagram:** **NOT-E7 — Sankey Flow** (Figma node `816:17`). HTML file on disk: `diagram-not-e7-sankey-flow-v5.html`. 7.5M → 47% click → 75% contributed, with Core/Casual/Resurrected/New cohort segmentation.

---

### Row 13 — `<h2>Frameworks</h2>` opening + `<h3>Activity prioritization</h3>`

New `<h2>` wrapper. Wraps rows 13–16.

**Prose** (drafted — net-new):
> The first principle of the framework: prioritize activity outside of "how well" a post is performing. The inbox should surface what's directly related to the user — something they asked for, something they need to know — not whatever the algorithm thinks is hot.

**Diagram:** **13i — Notification Taxonomy (detailed cut)** (Figma node `1176:2010` desktop / `1176:2090` mobile). Net-new HTML diagram. Same 3-category structure as NOT-E5 but with 2 examples per category and more detailed labels: Discovery (Popular content, Breaking news) / Following (Subreddit following, Comment following) / Conversation (Post replies, Comment replies).

→ HTML to translate from Figma. Filename: `diagram-not13-taxonomy-detail-v5.html`.

---

### Row 14 — `<h3>User targeting</h3>` (Signal × Intent matrix)

**Prose** (existing line 80 reworded — `tenure` → `intent`, plus existing line 82 verbatim):

> The strategy sat on two axes: signal and intent. By reading the signal Reddit has from a user and what they're trying to do on the platform, we could infer what experiences they were having and prioritize notification types accordingly. The inbox drives 2% of all comments on Reddit — that figure shifted leadership investment across the board.
>
> The first decision was where to start. Comment replies were the highest-usage surface — core users with strong opinions about their flows. Changing that experience could disrupt the one thing the inbox was actually working for. The alternative: open net-new growth for subreddit following and new users with completely empty inboxes. Less data, more assumptions, required research — but the upside was coverage where we had next to none.

**Diagram:** **NOT-E4 — Signal × Intent Matrix** (Figma node `455:35`). HTML file on disk: `diagram-not-e4-signal-intent-matrix-v5.html`. Quadrants: New user / Scroller / Seeker / Contributor.

**NOT-01 is retired** (sticky says duplicate of NOT-E4). The file `diagram-not01-segmentation-matrix-v5.html` stays on disk but isn't embedded.

---

### Row 15 — `<h3>Growth flywheel</h3>`

**Prose** (drafted — net-new):
> With taxonomy and targeting in place, the system becomes a growth flywheel. Reading signal lets us deliver value; delivering value generates more signal; the loop tightens with each cycle. The inbox shifts from a passive feed to an active driver of engagement and platform understanding.

**Diagram:** **NOT-E2 — Strategy Flywheel** (Figma node `449:35`). HTML file on disk: `diagram-not-e2-strategy-flywheel-v5.html`. 3-node loop: Leverage signal → Deliver value → Tune experience.

---

### Row 16 — `<h3>Strategic pillars</h3>`

**Prose** (drafted — net-new):
> Three pillars implement the strategy across the inbox: **build habits**, **enable curation**, **create focus**. Each pillar maps to a phase of the work that follows — and each builds on what the previous phase made possible.

**Diagram:** **NOT-E3 — Strategic Pillars** (Figma node `678:3238`). HTML file on disk: `diagram-not-e3-strategic-pillars-v5.html`. 3-card layout: Build habits / Enable curation / Create focus, each with a one-liner.

This row is the visual anchor that introduces the three pillars before the case study steps through them as the next three `<h2>` sections.

---

### Row 17 — `<h2>1. Build Habits</h2>` opening + `<h3>Intelligent defaults &amp; feedback loops</h3>`

The existing `<h2>1. Build Habits</h2>` (line 132) is **kept**. Wraps rows 17–18.

**Prose** (existing line 84 + line 136 + line 212, merged in this order):

> Users had a bias for action in the inbox. The more content was framed as personally actionable, the more likely they were to engage.
>
> I added copy showing *why* a user received each notification. Click-through doubled compared to generic framing, and the surface could support higher volume without overwhelming users.
>
> I shipped decay logic for breaking news, recommendations, and subreddit updates: if a user doesn't open a notification type after a threshold, the system asks whether to turn it off. The ML team ran parallel experiments on signal thresholds while I defined the user-facing behavior — a continuous dialogue between design and engineering, each side's findings reshaping the other's approach.

**Diagram:** **17i — Without context vs With context** (Figma node `1176:2158` desktop / `1176:2261` mobile). Net-new HTML diagram, hover-annotated before/after of two notification cards reframed with contextual copy.

→ HTML to translate from Figma. Filename: `diagram-not17-context-defaults-v5.html`.

**The current static `<img src="img/notif-ds-migration.png">` (lines 138–140) is replaced by this 17i diagram embed.**
**The `<h3>Recommendations as onboarding</h3>` block (lines 142–148) is merged into row 18 (its prose continues there).**
**The `<h3>Feedback loops</h3>` block (lines 210–216) is dissolved — its paragraph is merged into row 17 prose above.**

---

### Row 18 — `<h3>Push-to-inbox connection</h3>`

**Prose** (existing line 144 + line 152, merged):

> For low-subscription users, the inbox became an onboarding engine. Recommendations surfaced contextually; push landing experiences converted discovery into lasting signal. DAU for that cohort lifted +1.4%; push click-through rose +6.4% across 7.5M daily inbox users.
>
> Only the latest push recommendation appeared in the inbox. Users expected a history of communications — removing older recommendations cut off discovery flows mid-stream. I restored that connection. Push good visits climbed +1% across 15 million daily receives.

**Diagram:** **NOT-06 — Before/After history preservation** (Figma node `678:2498`). HTML file on disk: `diagram-not06-push-to-inbox-v5.html`. **Verify v2 visual matches** (BEFORE — LATEST ONLY 1 of 3 visible vs AFTER — HISTORY PRESERVED 3 of 3 visible); retranslate from Figma if older.

The 4-step push-to-inbox flow diagram (`678:2374`) is **NOT used** — Della picked the before/after impact visual only.

**Static `<img src="img/notif-push-landing.png">` (line 146) is removed** (replaced by reorg into row 18 with the NOT-06 diagram).

---

### Row 19 — `<h2>2. Enable Curation</h2>` opening + `<h3>Pipeline separation</h3>`

The existing `<h2>2. Enable Curation</h2>` (line 164) is **kept**. Wraps rows 19–23.

**Prose** (existing line 168 verbatim):
> Subreddit subscriptions were entangled with recommendations on the back end. The system weighted a recommended notification the same as a subscribed update — prioritizing engagement metrics (post performance, CTR) over what users had explicitly asked for. A user subscribing to r/all updates would get a viral r/PlayStation recommendation instead. I worked with the ML team to untangle the pipeline — they ran experiments on signal weighting while I redesigned the preference model, each side's findings reshaping the other's direction until user signal won over algorithmic signal.

**Diagram:** **19i — Pipeline entanglement** (Figma node `1176:3267` desktop / `945:17` mobile). Net-new HTML diagram showing two parallel pipelines (User subscriptions / Discovery suggestions) feeding into a single Ranker, with the result favoring discovery over subscriptions.

→ HTML to translate from Figma. Filename: `diagram-not19-pipeline-entanglement-v5.html`.

**Static `<img src="img/notif-pipeline-separation.png">` (lines 170–172) is removed** (replaced by 19i embed).

**The cross-channel paragraph (current line 220) is REMOVED entirely.** NOT-11 v2 is also retired (sticky `"retire?"`). The existing `not-11` `diagram-pair` block (lines 222–239) and its surrounding `<h3>Cross-channel coordination</h3>` heading (line 218) are deleted.

---

### Row 20 — `<h3>Preference architecture</h3>`

**Prose** (existing line 176 verbatim):
> The back end couldn't define what updates a user could receive from a subreddit. Options were off, low, and frequent — even internally, the team couldn't explain what those meant because they were wrapped in algorithmic metrics. I worked with the engineering lead through weekly syncs on capacity and feasibility to rearchitect preferences: no updates, popular posts, all posts. Eng held deep knowledge of system behavior and limitations — every conversation surfaced another constraint, but each one guided us toward a more precise model.

**Diagram:** **NOT-07 v2** (Figma node `709:739`). HTML file on disk: `diagram-not07-preference-architecture-v5.html`. **Verify v2 visual matches** (legacy dropdown → redesigned page with no/low/frequent labels); retranslate from Figma if older.

---

### Row 21 — `<h3>Subreddit on-ramps</h3>`

**Prose** (existing line 188, first half — split):
> I then surfaced these preferences on the subreddit page itself — point of decision, not buried three screens deep.

**Diagram:** **NOT-08 v2** (Figma node `709:668`). HTML file on disk: `diagram-not08-subreddit-onramps-v5.html`. Two subreddit cards (r/williamsburg with bell + Joined, r/Seattle with Joined) showing on-ramp affordances.

---

### Row 22 — `<h3>Contextual suggestions</h3>`

**Prose** (drafted — net-new):
> Beyond the subreddit page, recommendation surfaces also gained on-ramps. Push notifications and inbox cards offered subscription suggestions tied to the user's recent activity — turning a passive recommendation into an active subscription opportunity at the moment of engagement.

**Diagram:** **22 — Contextual suggestions HTML container** (Figma references `PNupsell_communityVisit` + `inbox_rpl3`). Build a small HTML diagram container matching the rest of the case study's `diagram-embed` pattern. Inside it, lay out the two UI examples (push notification upsell + inbox row variant) with brief captions.

→ HTML to translate from Figma references. Filename: `diagram-not22-contextual-suggestions-v5.html`.

---

### Row 23 — `<h3>Global settings</h3>`

**Prose** (existing line 188, second half — split, plus a connecting line):

> …and simplified subscription management in global settings.
>
> The flat list replaced a nested per-community drill-down — every community and its alert state visible in one view.

**Diagram:** **NOT-09 v2** (Figma node `709:863`). HTML file on disk: `diagram-not09-global-settings-v5.html`. **Verify v2 visual matches** (nested per-community vs flat list with alert-level icons); retranslate from Figma if older.

---

### Row 24 — `<h2>3. Create Focus</h2>` opening + `<h3>Surface consolidation</h3>`

The existing `<h2>3. Create Focus</h2>` (line 241) is **kept**. Wraps rows 24–27.

**Prose** (drafted lead-in + existing line 245 verbatim):

> Why this was hard: three surfaces with different sort logic, engagement patterns, and information architecture had to merge without breaking any of them.
>
> I consolidated four messaging systems into a single inbox. This required deprecating one internal system, migrating another, and navigating multiple intermediate states — each shipped as a fully functional experience, not a waypoint. Eng on this team were precise and construction-oriented — they caught edge cases I hadn't, which made the late-stage design reviews a critical part of my process for making designs airtight before handoff.

**Diagram:** **24i — Surface trade-offs** (Figma node `1176:3313` desktop / `1176:3351` mobile). Net-new HTML diagram, three-column comparison: INBOX (Static chronological / Async / Different pages) | PRIVATE MESSAGES (Dynamic by recency / Async / Thread details) | CHAT (Dynamic by recency / Synchronous / Thread details).

→ HTML to translate from Figma. Filename: `diagram-not24-surface-tradeoffs-v5.html`.

**Static `<img src="img/notif-unified-inbox.png">` (lines 247–249) is removed** (replaced by row 27 reveal).

---

### Row 25 — `<h3>Layout experimentation</h3>`

**Prose** (existing line 253 + line 84 "switchboard" sentence salvaged):
> I tested chronological, nested, and tabbed layouts. Users wanted to navigate the inbox as little as possible — scan, act, leave. The inbox wasn't a destination — it was a switchboard that guided users through their session.

**Diagram:** **NOT-12 v2** (Figma node `678:3020`). HTML file on disk: `diagram-not12-inbox-layout-experiments-v5.html`. **Verify v2 visual matches** (HOVER EACH LAYOUT FOR TRADE-OFFS, three columns with Best Fit badge on Tabbed); retranslate from Figma if older.

---

### Row 26 — `<h3>Navigation simplification</h3>`

**Prose** (existing line 271 verbatim):
> The unified inbox freed a slot in the bottom tab bar. Reddit used that space to experiment with new product surfaces and validate navigation models — a simplified 3–4 tab structure. Impact that extended well beyond the inbox.

**Diagram:** **NOT-14 v1** (Figma node `379:2`). HTML file on disk: `diagram-not14-navigation-simplification-v5.html`. The 5-tab → 3-4 tab navigation simplification visual.

---

### Row 27 — `<h3>Unified inbox reveal</h3>`

**Prose** (drafted — net-new):
> The result: one inbox, two tabs (Notifications + Chat), all messaging consolidated. The mental model is finally what users expected from the start — a single source of truth where every kind of communication lands and every kind of action is one tap away.

**Diagram:** **NOT-14 v2 — Unified inbox mockup** (Figma node `1176:2685`). Net-new HTML diagram — full-fidelity mobile mockup of the unified inbox showing Notifications + Chat tabs, mixed feed, and simplified bottom nav. The mockup includes a screen placeholder area where Della will fill in a GIF/screen recording of the inbox in action later.

→ HTML to translate from Figma. Filename: `diagram-not14-unified-inbox-v5.html`. Container should have a labeled `<div class="gif-placeholder">` slot in the screen area.

---

### Row 28 — `<h2>Results</h2>` (current line 283 — kept verbatim)

No change to current Results section.

---

## §2 Heading hierarchy summary

```
<h1>Notifications & Inbox</h1>  (existing hero)
[meta-grid] (existing)
<h2>Summary</h2>  (NEW - row 1)
  <h3>Challenge</h3>  (existing line 53 prose)
  <h3>Strategy</h3>  (existing line 57 prose)
  [NOT-03 v1 diagram]
<h2>Challenge</h2>  (renamed scope - rows 2-4)
  <h3>No overarching strategy</h3>  (row 2)
  <h3>Notification taxonomy gap</h3>  (row 3)
  <h3>Decaying retention</h3>  (row 4)
<h2>Strategy</h2>  (NEW - row 5)
  [strategy lede + metrics-callout relocated from hero]
<h2>Scaleable foundation</h2>  (renamed from "Foundation" - rows 6-10)
  <h3>Inbox row component</h3>  (row 6)
  <h3>Swipe actions</h3>  (row 7)
  <h3>Unread hierarchy</h3>  (row 8)
  <h3>Unread color fix</h3>  (row 9)
  <h3>Three different inboxes</h3>  (row 10)
<h2>Push paradox & engagement reality</h2>  (NEW - rows 11-12)
  <h3>The push paradox</h3>  (row 11)
  <h3>Inbox engagement funnel</h3>  (row 12)
<h2>Frameworks</h2>  (NEW - rows 13-16)
  <h3>Activity prioritization</h3>  (row 13)
  <h3>User targeting</h3>  (row 14)
  <h3>Growth flywheel</h3>  (row 15)
  <h3>Strategic pillars</h3>  (row 16)
<h2>1. Build Habits</h2>  (kept - rows 17-18)
  <h3>Intelligent defaults & feedback loops</h3>  (row 17)
  <h3>Push-to-inbox connection</h3>  (row 18)
<h2>2. Enable Curation</h2>  (kept - rows 19-23)
  <h3>Pipeline separation</h3>  (row 19)
  <h3>Preference architecture</h3>  (row 20)
  <h3>Subreddit on-ramps</h3>  (row 21)
  <h3>Contextual suggestions</h3>  (row 22)
  <h3>Global settings</h3>  (row 23)
<h2>3. Create Focus</h2>  (kept - rows 24-27)
  <h3>Surface consolidation</h3>  (row 24)
  <h3>Layout experimentation</h3>  (row 25)
  <h3>Navigation simplification</h3>  (row 26)
  <h3>Unified inbox reveal</h3>  (row 27)
<h2>Results</h2>  (kept verbatim)
```

---

## §3 Explicit deletions

Only the items below are removed. Everything else moves; nothing else is dropped.

**Prose deletions:**
- Lines 218–239: `<h3>Cross-channel coordination</h3>` heading + paragraph + `not-11` diagram-pair embed.
- Lines 265–267: `<h3>Pinned contributions</h3>` heading + paragraph.
- Lines 78–84: original `<h2>Framework</h2>` block — **but** all its prose lands elsewhere (see preservation map below). The `<h2>` wrapper is what's removed; no prose is lost from this block.
- Lines 86, 88, 112, 128, 132 (sub), 142, 174, 196, 210, 218: section/sub-section header tags get rewritten or removed per the new hierarchy. Their prose all lives in the new structure.

**Static-image replacements (the `<img>` blocks go away; their content is replaced by the listed Figma diagram):**
- Lines 138–140 `notif-ds-migration.png` → row 17's 17i diagram.
- Lines 146–148 `notif-push-landing.png` → folded into row 18 alongside NOT-06.
- Lines 170–172 `notif-pipeline-separation.png` → row 19's 19i diagram.
- Lines 247–249 `notif-unified-inbox.png` → row 27's NOT-14 v2 diagram.

**Diagram retirements (HTML files stay on disk; not embedded):**
- `diagram-not01-segmentation-matrix-v5.html` — duplicate of NOT-E4 per Figma sticky.
- The 4-step `NOT-06 push-to-inbox flow` (Figma node `678:2374`) — Della chose before/after only.

---

## §4 Preservation map

Audit. Every existing prose block lands somewhere.

| Current line | First words | New row |
| --- | --- | --- |
| 27–48 | Hero / eyebrow / h1 / meta-grid | unchanged, in place |
| 53 | "Reddit communicates with hundreds…" | Row 1 Summary tile (Challenge) |
| 57 | "I built the segmentation framework…" | Row 1 Summary tile (Strategy) |
| 59–76 | metrics-callout | Row 5 (relocated out of hero) |
| 80 | "The strategy sat on two axes: signal and tenure…" | Row 14, "tenure" → "intent" reword |
| 82 | "The first decision was where to start. Comment replies were the highest-usage surface…" | Row 14 (second paragraph) |
| 84 | "Users had a bias for action…" + "switchboard" | Split: bias → row 17, switchboard → row 25 |
| 90 | "The inbox wasn't on Reddit's design system…" | Row 6 |
| 114 | "I rebuilt the unread system around progressive disclosure…" | Row 8 |
| 126 | "The migration introduced a less prominent unread color…" | Row 9 |
| 130 | "I removed the overflow menu, icon-based message type indicators…" | Row 7 |
| 136 | "I added copy showing *why* a user received each notification…" | Row 17 |
| 144 | "For low-subscription users, the inbox became an onboarding engine…" | Row 18 |
| 152 | "Only the latest push recommendation appeared in the inbox…" | Row 18 |
| 168 | "Subreddit subscriptions were entangled with recommendations…" | Row 19 |
| 176 | "The back end couldn't define what updates…" | Row 20 |
| 188 | "I then surfaced these preferences on the subreddit page itself…" | Split: subreddit page → row 21, global settings → row 23 |
| 212 | "I shipped decay logic for breaking news…" | Row 17 |
| 220 | "I defined the relationship between channels…" | **REMOVED** (per Della) |
| 245 | "I consolidated four messaging systems…" | Row 24 |
| 253 | "I tested chronological, nested, and tabbed layouts…" | Row 25 |
| 267 | "I designed a system that pins contributions…" | **REMOVED** (NOT-13 retire sticky) |
| 271 | "The unified inbox freed a slot in the bottom tab bar…" | Row 26 |
| 285 | Results paragraph | unchanged |

---

## §5 Diagram inventory & file work

### Already on disk, embed unchanged (verify v2 visual; retranslate from Figma if older)
- `diagram-not02-inbox-row-unit-v5.html` — row 6
- `diagram-not04-unread-hierarchy-v5.html` — row 8
- `diagram-not06-push-to-inbox-v5.html` — row 18
- `diagram-not07-preference-architecture-v5.html` — row 20
- `diagram-not08-subreddit-onramps-v5.html` — row 21
- `diagram-not09-global-settings-v5.html` — row 23
- `diagram-not12-inbox-layout-experiments-v5.html` — row 25
- `diagram-not14-navigation-simplification-v5.html` — row 26 (v1)

### Already on disk, embed in NEW row positions
- `diagram-not03-full-inbox-redesign-v5.html` — row 1 (Summary)
- `diagram-not-e1-cohort-decay-v5.html` — row 4
- `diagram-not-e2-strategy-flywheel-v5.html` — row 15
- `diagram-not-e3-strategic-pillars-v5.html` — row 16
- `diagram-not-e4-signal-intent-matrix-v5.html` — row 14
- `diagram-not-e5-notification-taxonomy-v5.html` — row 3
- `diagram-not-e6-butterfly-chart-v5.html` — row 11
- `diagram-not-e7-sankey-flow-v5.html` — row 12

### To translate from Figma (net-new HTML diagrams)
- `diagram-not02b-disconnected-surfaces-v5.html` (row 2, from Figma `1170:766`/`1173:966`)
- `diagram-not02b-swipe-actions-v5.html` (row 7, from Figma `1173:1127`/`1173:1230` — includes GIF placeholder slot)
- `diagram-not04b-unread-color-fix-v5.html` (row 9, from Figma `1176:1630`/`1176:1597`)
- `diagram-not10-three-inboxes-v5.html` (row 10, from Figma `1176:1726`/`1176:1764`)
- `diagram-not13-taxonomy-detail-v5.html` (row 13, from Figma `1176:2010`/`1176:2090`)
- `diagram-not17-context-defaults-v5.html` (row 17, from Figma `1176:2158`/`1176:2261`)
- `diagram-not19-pipeline-entanglement-v5.html` (row 19, from Figma `1176:3267`/`945:17`)
- `diagram-not22-contextual-suggestions-v5.html` (row 22, container for `PNupsell_communityVisit` + `inbox_rpl3` references)
- `diagram-not24-surface-tradeoffs-v5.html` (row 24, from Figma `1176:3313`/`1176:3351`)
- `diagram-not14-unified-inbox-v5.html` (row 27, from Figma `1176:2685` — includes GIF placeholder slot)

The figma-to-html skill handles each translation. Mobile siblings (`-mobile.html`) follow.

### Retired (file stays on disk, not embedded)
- `diagram-not01-segmentation-matrix-v5.html`

---

## §6 Diagram embed pattern (staged rollout to avoid 404s)

**Default for now:** single-iframe embed with `data-mobile-pending="true"` marker. Once the figma-to-html skill produces the `-v5-mobile.html` siblings, a follow-up edit converts to `diagram-pair`.

```html
<div class="case-img-full diagram-embed" data-diagram="not-XX" data-mobile-pending="true">
  <iframe
    src="img/diagrams/diagram-notXX-NAME-v5.html"
    loading="lazy"
    scrolling="no"
    title="…descriptive…"
    style="width: 100%; border: none; border-radius: 12px; overflow: hidden;"
  ></iframe>
</div>
```

`not-11` was the only existing pair; that whole block is removed (cross-channel retired) so no special-case handling needed.

---

## §7 Safety, rollback, and staged execution

### §7.1 Pre-flight (do this FIRST)
```bash
cd /Users/della/CoworkWorkspace/Get-a-job/portfolio-site
cp case-notifications.html case-notifications.html.bak
git add -A && git commit -m "pre-refactor snapshot — case-notifications v2 outline"
git checkout -b case-notifications-figma-rearrange-v2
```

### §7.2 Staged execution (do not run all 27 rows in one shot)

The previous attempt failed because it tried to do everything in one mega-pass and lost track of what landed where. This time, group rows into 4 batches with a Della checkpoint between each:

**Batch 1 — Rows 1–5 (Summary + Challenge + Strategy):** the most novel/restructured part of the refactor. Single commit. Della previews in browser before continuing.

**Batch 2 — Rows 6–12 (Scaleable foundation + Push paradox):** existing prose moves into new wrappers; new beats (rows 10–12) inserted. Single commit. Della previews.

**Batch 3 — Rows 13–18 (Frameworks + Build Habits):** mostly relocations + the new Frameworks h2 block. Single commit. Della previews.

**Batch 4 — Rows 19–28 (Enable Curation + Create Focus + Results):** final stretch including cross-channel deletion and Pinned deletion. Single commit. Della previews.

After each batch: commit with message like `case-notifs batch N: rows X-Y`. Run a `grep -c` audit against the §4 Preservation map to confirm every existing line still appears (or is in the explicit-removal list).

### §7.3 Rollback ladder
- Misplaced paragraph → edit in place.
- Whole batch broken → `git reset --hard HEAD~1`.
- Whole branch broken → `git checkout main && git branch -D case-notifications-figma-rearrange-v2`.
- Catastrophic → `cp case-notifications.html.bak case-notifications.html`.

### §7.4 Refactor manifest
Maintain `working/planning-docs/case-notifications-REFACTOR-NOTES.md`. Append per batch: every paragraph relocation, every new heading inserted, every diagram embed added/removed. Cross-check against §4 preservation map at the end.

---

## §8 What to tell Claude Code

Open a fresh Claude Code session in `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site` and send this:

> Refactor `case-notifications.html` per the spec in `working/planning-docs/case-notifications-change-outline.md`. Read the whole spec first. Then:
>
> 1. Run §7.1 pre-flight (backup + git checkpoint + branch).
> 2. Execute Batch 1 only (rows 1–5). Commit. Stop and ping me to preview before Batch 2.
> 3. After my green light, continue Batch 2, then 3, then 4 — each with a commit and a checkpoint.
> 4. For diagrams listed in §5 "to translate from Figma": skip net-new diagram HTML files in this pass — leave a `<div class="img-placeholder">[diagram name TBD]</div>` block where each lives. The figma-to-html translation pass happens separately. Existing on-disk diagrams get embedded normally.
> 5. Maintain the refactor manifest in `working/planning-docs/case-notifications-REFACTOR-NOTES.md` as you go.
