# case-notifications — E-Series Placement Recommendation

**Date:** 2026-04-22
**Scope:** Where NOT-E1 through NOT-E7 should live in `case-notifications.html`
**Status:** Recommendation only — not yet actioned. Actual insertion + copy work deferred to a separate thread.

---

## Summary

Of the 7 E-series diagrams, **one already has a confirmed home** (NOT-E1 → existing L211 "Decay logic" placeholder). The remaining 6 need new slots carved into the case study structure. This document maps each to a recommended section, explains the narrative logic, and flags where Della will need to write new copy or approve a structural change.

---

## Current case study skeleton

```
Challenge                    (L51–53)
Solution                     (L55–76 — includes metrics callout)
Framework                    (L78–94 — currently holds NOT-01, being retired)
Foundation                   (L96–132)
  — Design system migration  (L98–108 → NOT-02 + NOT-03 slots)
  — Unread system redesign   (L110–124 → NOT-04 live)
  — Inbox simplification     (L126–132 → NOT-05 slot, being retired)
1. Build Habits              (L134–164)
  — Contextualizing          (L136–142)
  — Recs as onboarding       (L144–150)
  — Push-to-inbox connection (L152–164 → NOT-06 live)
2. Enable Curation           (L166–226)
  — Pipeline separation      (L168–174)
  — Preference architecture  (L176–204 → NOT-07 live, NOT-08 slot, NOT-09 live)
  — Feedback loops           (L206–212 → NOT-E1 slot, confirmed)
  — Cross-channel coord      (L214–226 → NOT-11 live)
3. Create Focus              (L228–260)
  — Surface consolidation    (L230–236)
  — Layout experimentation   (L238–244 → NOT-12 slot)
  — Pinned contributions     (L246–252 → NOT-13 slot, being retired)
  — Navigation simplification (L254–260 → NOT-14 slot)
Results                      (L262–264)
```

---

## Recommendations per E-series diagram

### NOT-E1 — Cohort Decay ✅ CONFIRMED

- **Placement:** L211 placeholder ("Decay logic") in `2. Enable Curation > Feedback loops`
- **Action:** Fill existing placeholder — no structural edit needed
- **Copy edit:** Possibly update L208–211 description to match the final diagram's framing
- **Ready to build.** Deferred to E-series thread only because of bundling.

### NOT-E2 — Strategy Flywheel

- **Recommended placement:** `Solution` section, **immediately after the metrics callout** (insert between L76 and L78, before the `Framework` H2)
- **Why:** Flywheel diagrams are best as "the whole system in one picture" visuals. Showing the full loop at the top of the case study gives readers the end-state mental model before you take them through how it was built. It visually bridges Solution (what I did) and Framework (how the strategy was structured).
- **Alternative:** `Results` section, framed as "the system that now compounds." Weaker because the narrative already has a clear segmentation-framework diagram (NOT-E4) planned for Framework; two high-level overviews in one case study feels redundant.
- **Copy needed:** Della would write 1–2 sentences introducing the flywheel — something like "The system I built behaves as a compounding loop: X drives Y drives Z." Flag for separate thread.

### NOT-E3 — Strategic Pillars

- **Recommended placement:** **Replaces NOT-01's current slot** at L86–94 (after retiring NOT-01), OR inserted as a **new standalone block immediately before `1. Build Habits`** (around L133).
- **Why:** If "Strategic Pillars" shows the three pillars (Build Habits / Enable Curation / Create Focus), it works beautifully as a visual index for the three numbered sections that follow. Readers hit the diagram and immediately understand the structure of the next several sections.
- **Which slot?**
  - **Replacing L86–94 (Framework):** cleaner — reuses an iframe slot, no net structural change. But Framework is about the signal × tenure matrix, not the pillars, so this may not fit thematically.
  - **New block before L134:** stronger narratively — the pillars preview what's coming. Requires a new H2 or a transitional block.
- **Flag for Della:** If E3 is semantically the three-pillar framework, the "new block before 1. Build Habits" option is stronger. If E3 is actually the segmentation framework under a different name, it goes in the retired NOT-01 slot.

### NOT-E4 — Signal × Intent Matrix

- **Recommended placement:** **Directly replaces NOT-01 at L86–94** in the `Framework` section
- **Why:** NOT-01 was "signal × tenure matrix"; NOT-E4 is "signal × intent matrix." Different axes, but same structural role — a 2×2 framework at the case study's strategic spine. This is the cleanest retirement: kill the old iframe, drop in the E4 iframe, update the body copy's axes.
- **Copy edit required:** L80 currently reads "The strategy sat on two axes: signal and tenure." If E4's axes are signal × intent, that sentence plus the paragraph following need a rewrite.
- **Flag for Della:** Confirm the new axes match what's in E4. If the new framework is actually signal × tenure re-skinned, L80 copy may not need changes.

### NOT-E5 — Notification Taxonomy

- **Recommended placement:** `Foundation` section, as a **new H3 subsection between L96 "Foundation" and L98 "Design system migration"**
- **Why:** A notification taxonomy is foundational vocabulary — it defines what types of notifications exist before you describe how they were redesigned. Placing it at the top of Foundation lets every subsequent subsection refer to the taxonomy without redefining it.
- **Alternative:** Could also sit in `2. Enable Curation > Preference architecture` as a visual aid for the rearchitected "no updates / popular posts / all posts" model. Weaker placement — preference architecture is already visually covered by NOT-07.
- **Copy needed:** Della writes a new subsection heading + 1 short paragraph introducing the taxonomy.

### NOT-E6 — Butterfly Chart

- **Recommended placement:** `Results` section, inserted **between L264 (current Results paragraph) and L266 (section close)**
- **Why:** Butterfly charts are quantitative comparison visuals — ideal for showing before/after metric shifts. Results is exactly where quantitative impact should live. The current Results section is one short paragraph; adding a data visual strengthens it considerably.
- **Copy needed:** Della writes 1–2 sentences introducing what the butterfly compares (likely: notification category performance pre/post redesign).
- **Note:** The mobile handoff brief flagged E6 as a single-SVG vector — fine for static embed, but means per-bar interactivity (hover, filter) isn't on the table without a refactor.

### NOT-E7 — Sankey Flow

- **Recommended placement:** `Results` section, **immediately after NOT-E6**, as a second results visual
- **Why:** Sankey flows show volume and pathways — good for "where do notifications flow in the unified system?" or "how does user attention move across the inbox + push + email channels?" Paired with E6, the Results section goes from one paragraph to a strong quantitative close: one chart shows category-level impact (E6), one shows system-level flow (E7).
- **Alternative:** `2. Enable Curation > Cross-channel coordination` (L214–226). Weaker — NOT-11 already covers cross-channel conceptually; adding a second diagram there muddies the narrative.
- **Copy needed:** 1–2 sentences introducing the flow — what's sourced, what's destination, what the width represents.

---

## Structural edits required (summary)

| Edit | Location | Type |
|---|---|---|
| Retire NOT-01 iframe | L86–94 | delete |
| Replace with NOT-E4 iframe | L86–94 (reuse slot) | swap |
| Update body copy for new axes | L80–82 | rewrite |
| Insert NOT-E2 (flywheel) | between L76 and L78 | new block + H3 or standalone |
| Insert NOT-E3 (pillars) | between L132 and L134 (preferred) OR L86–94 (alt) | new block |
| Insert NOT-E5 (taxonomy) | between L96 and L98 | new H3 subsection |
| Retire NOT-05 placeholder | L130–132 | delete |
| Fill NOT-E1 (decay) | L210–212 | swap to iframe |
| Retire NOT-13 placeholder | L250–252 (+ H3 at L246) | delete |
| Insert NOT-E6 (butterfly) | between L264 and L266 | new block |
| Insert NOT-E7 (sankey) | immediately after E6 | new block |

---

## Open questions for Della

1. **E4 axes:** Signal × intent, or is it actually signal × tenure renamed? Determines whether L80–82 copy needs rewriting.
2. **E3 semantics:** Three pillars (preferred narrative-replacement role for retired NOT-01) OR different framework? Determines slot.
3. **E2 and E3 coexistence:** If both belong above `1. Build Habits`, do we want two strategic-overview visuals back-to-back (flywheel + pillars), or does one make the other redundant?
4. **Results section depth:** Are you comfortable expanding Results from one paragraph to include two data visuals? (Strong rec: yes — Results is currently thin for the scale of impact demonstrated.)
5. **Copy for new sections:** Della writes the framing sentences for each new diagram, or shall Claude draft them for her review (voice-checked)?

---

## Proposed sequencing for the E-series thread

1. Della reviews this doc and answers the 5 open questions
2. Claude drafts copy for new blocks (voice-checked, presented for approval)
3. Della approves or revises copy
4. Claude executes structural edits on `case-notifications.html`
5. Claude builds the 7 E-series HTML diagrams via `figma-to-html` (E1 first as sample)
6. Claude stamps iframes, runs quality checks, screenshots final result
7. Handoff to mobile-pair thread
