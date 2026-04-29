# case-ai (KLP / Reddit Answers MVP) — Change Outline

**Source of truth:** Figma page `29:42` — *2. Reddit Answers MVP* (Portfolio — Image Inventory).
**Live HTML:** `portfolio-site/case-ai.html`.
**Generated:** 2026-04-28 from Figma metadata (`figma-meta-klp.xml`, 4448 lines) + screenshots of key frames.

This is the section-by-section diff Claude Code will execute against. It captures the new heading hierarchy, the diagrams kept / retired / new / adapted, the Figma↔HTML link per diagram, and the order edits must land in `case-ai.html`. All file paths are absolute from the repo root.

---

## §0 Ground rules

1. **Source of truth = Figma page 29:42.** When ambiguity exists between this doc and the canvas, re-pull the canvas. Don't drift the link.
2. **HTML is preserved where it already exists.** For every kept diagram, the existing `img/diagrams/diagram-ai*-v4.html` file remains the iframe source; we only update its position in `case-ai.html` and (where retired) remove its embed block.
3. **Adapted diagrams (sticky-note flagged) get a dedicated new HTML file** that copies the source diagram's structural CSS, then specializes content. The sticky text records the source explicitly.
4. **PNGs stay PNGs.** The Overview row's product-UI screenshots are raster captures — embedded with `<img>`, not `<iframe>`. Do not rebuild them as diagrams.
5. **The Retired column on the Figma canvas is a parking lot, not part of the page.** Diagrams there are removed from the live page; their HTML files stay on disk under `img/diagrams/` (they may be referenced by other pages or cited in the build log).
6. **Mobile pairings already exist.** All 19 case-ai mobile frames are paired to Figma per `working/mobile-audit/figma-handoff-case-ai.md`. The reorganization doesn't break that pairing — it just retires some pairs.
7. **Voice rules apply** (project CLAUDE.md). All copy edits go through the self-check protocol against `voice-rules/banned-patterns.yaml`.

---

## §1 Coordination

- Della has Claude Code running concurrently. This doc is the authoritative spec — Claude Code should execute against §3 (per-section spec) and §6 (code-level changes), not against the Figma file directly.
- The `figma-handoff-case-ai.md` mobile-pairing roster in `working/mobile-audit/` remains authoritative for mobile node IDs. Don't repeat that work here.

---

## §2 New heading hierarchy

Top-to-bottom in the new layout (read directly from Figma title text nodes at x≈-4770, sorted by Y):

```
H1   Reddit Answers MVP   ← page hero (existing)
H2   Overview             ← NEW (replaces current Challenge intro)
H2   Competing user needs ← retitle of current "Quality Control" lens
H2   Proof of concept / research   ← retitle of current "Proving the Concept"
H2   Page information architecture ← retitle of current Solution
H2   Establishing principles for generated content (summary)   ← NEW (replaces Value)
H2   Identification
H3     UI to distinguish AI gen content
H2   UI to display source posts          ← retitle of current "Threaded Source Posts"
H2   Content
H3     voice
H3     content
H2   Ensuring quality                    ← consolidated quality umbrella
H3     Generating summaries: XFN workflow ← retitle of current "Prompt Design Workflow"
H3     feedback loops                     ← retitle of current "User Feedback Loops"
H3     failure states                     ← retitle of current "Failure States"
[H2  Results]                              ← preserved as-is
```

13 narrative rows on canvas + 1 final empty row (likely Results). Page ends at `failure states` content.

---

## §3 Per-section spec

For each section: heading, narrative purpose, diagrams (with Figma node IDs and HTML source paths), PNGs, and stickies. Diagrams marked **NEW** need authoring; **ADAPTED** flags adapted-from-other-HTML (sticky-noted in Figma); **KEPT** uses existing HTML; **RETIRED** removes from page.

### 3.1 Overview *(NEW H2)*

**Narrative purpose:** Open the case study with a product framing — show the KLP UI in its final form before backstory.

**PNGs (left column, x≈-4770):**
- `Screenshot 2026-04-27 at 3.53.34 PM.png`, `Screenshot 2026-04-27 at 3.41.17 PM.png`, `Screenshot 2026-04-27 at 6.16.43 PM.png` — three product UI captures (mobile + desktop frames).
- `Screenshot 2026-04-27 at 6.53.45 PM 2.png` (further down) — closing UI shot.

**Diagrams:**
- **2i-desktop** (Figma `1203:5207`, w=760) — **ADAPTED** from `diagram-ai10-failure-state-v4.html`. Sticky: *"use AI 10 as an HTML base"* (id `1203:5233`). Repurposes the BELOW THRESHOLD / ABOVE THRESHOLD comparison as the Overview hero showing how the page degrades to source posts vs. shows AI synthesis. **New file:** `img/diagrams/diagram-ai-overview-v1.html`.
- **2i-mobile** (Figma `1207:5594`, w=375) — **ADAPTED** from notifications case study, specifically `diagram-not03-full-inbox-redesign-v5.html` mobile design. Sticky: *"build from 'not03 — Full Inbox Redesign' mobile design"* (id `1207:5635`). Vertical-stacked threshold comparison. **New file:** `img/diagrams/diagram-ai-overview-v1-mobile.html`.

**Existing PNGs in `img/`:** `klp-ui-1.png`, `klp-ui-2.png`, `klp-ui-3.png`, `klp-flow-v2.png`, `klp-slide-1.png`, `klp-slide-2.png` — confirm with Della whether these are the same captures she has in Figma's Overview row, or new ones. The Figma filenames suggest fresh captures dated 2026-04-27.

---

### 3.2 Competing user needs *(retitled H2)*

**Narrative purpose:** The Googlebot-vs-humans framing — current `Quality Control` H3 promoted to H2 as the lens for the whole project.

**PNGs:** `Screenshot 2026-04-27 at 6.53.45 PM 3.png` — UI capture above the diagram.

**Diagrams:**
- **AI-09 — Two Users, One Page** (Figma `389:2`, w=760) — **KEPT**. HTML: `img/diagrams/diagram-ai09-dual-user-framework-v4.html`. Mobile: Figma `989:8`.

---

### 3.3 Proof of concept / research *(retitled H2)*

**Narrative purpose:** Reframe the "Proving the Concept" / static MVP origin story as research + proof rather than a workflow step.

**PNGs:** `Screenshot 2026-04-27 at 5.06.39 PM 1.png`, `Screenshot 2026-04-27 at 5.06.39 PM 2.png` — two captures.

**Diagrams:**
- **AI-02a — Vertical Selection** (Figma `1203:5467`, w=760) — **KEPT**. HTML: `img/diagrams/diagram-ai02a-verticals-v4.html`. Mobile: Figma `972:8`.
- **AI-02b — Static MVP Process** — **RETIRED** (right column, Figma `380:2`, x=6146). HTML stays on disk at `img/diagrams/diagram-ai02b-process-v4.html` but the iframe block is removed from `case-ai.html`.

**Reduction:** This section drops from 2 diagrams → 1.

---

### 3.4 Page information architecture *(retitled H2 — replaces current Solution)*

**Narrative purpose:** Show the dual-layer page structure (synthesis on top, source posts below) as an IA decision, not a feature.

**PNGs:** `Screenshot 2026-04-27 at 7.34.20 PM 4.png`, `Screenshot 2026-04-27 at 6.18.44 PM 2.png`, `Screenshot 2026-04-27 at 7.02.55 PM 1.png` — three captures.

**Stickies (design-intent, not adaptation):** *"what were the parts of the solution?"* (id `1221:21184`).

**Diagrams:**
- **Before vs After** (Figma `1202:5101`, w=644) — **NEW**. Two-column comparison: BEFORE = multiple competing threads (r/headphones × 2, r/BudgetAudio, r/gadgets, r/tech) for one query; AFTER = one page with AI summary + 3 sourced threads (r/headphones, r/BudgetAudiophile, r/gadgets). **New file:** `img/diagrams/diagram-ai-ia-before-after-v1.html`. No existing HTML to adapt from — this is a from-scratch authorship.

**Replaces:** the two `img-placeholder` slots in current `case-ai.html` Solution section ("page architecture" + "flow query → summary → on-ramps").

---

### 3.5 Establishing principles for generated content (summary) *(NEW H2 — replaces Value)*

**Narrative purpose:** The framework lens — what principles guided the generated content. Replaces the current `Value` section's three-way-balance framing with a principles-first articulation.

**Confirmed by Della:** this section is row 4 (4t/4i). Its diagram is **AI-13 — First Precedent**.

**Diagrams:**
- **AI-13 — First Precedent** (Figma `394:2`, w=760) — **KEPT**. HTML: `img/diagrams/diagram-ai13-transparency-framework-v4.html`. Mobile: Figma `950:8`. Repurposed from current Transparency-section opener; in the new structure, ai13 anchors the principles framework.

The current `Value` section's `ai05 — Three-Way Balance` (Figma `382:2`, x=8562), `ai06 — Evaluation Matrix` (moves to Ensuring quality), and `ai07 — Scoring Session` (retired) all leave this position.

---

### 3.6 Identification → UI to distinguish AI gen content *(H2 + H3)*

**Narrative purpose:** How AI content is visually distinguished — the design-systems precedent for AI identification at Reddit.

**Stickies (design-intent):** *"Ensure generated content is recognizeable to suers instantly"* (id `1227:21810`).

**Diagrams (in narrative order, top to bottom):**
- **AI-14 — Identification Explorations** (Figma `395:2`, w=760, row 5) — **KEPT**. HTML: `img/diagrams/diagram-ai14-identification-explorations-v4.html`. Mobile: Figma `982:8`.
- **NOT-03 v2 — Full Inbox Redesign** (Figma `1226:21284`, w=760, row 6) — **ADAPTED** from notifications case study. Sticky: *"build from 'NOT-03 v2 — Full Inbox Redesign' desktop design"* (id `1226:21472`). Used here as the visual precedent for an in-page identification pattern. **New file:** `img/diagrams/diagram-ai-identification-precedent-v1.html` — fork rather than reuse, so the AI-page version can specialize content (e.g., AI badge / synthesis chrome) without drifting the notifications-case version.

**Note:** Row 6 has no separate title text; it continues the "UI to distinguish AI gen content" H3 from row 5 with the not03 precedent as a second supporting diagram.

**RETIRED from this section** (right column on canvas):
- AI-07 — Scoring Session (`385:2`)
- AI-08 — Page Anatomy (`386:2`)
- AI-15 — The Sparkle Problem (`397:2`)
- AI-16 — Final Identification (`216:2` and `1208:5879`)
- AI-21 — Comment Truncation (`245:2`)
- AI-24 — Clarity Spectrum (`258:2`)

That's a substantial trim — current Identification section keeps `ai14, ai15, ai16` and drops all but `ai13` + `ai14` here.

---

### 3.7 UI to display source posts *(retitled H2)*

**Narrative purpose:** Threaded source posts UI — kept as a standalone section because the threaded-comments-with-truncation pattern was a Reddit first.

**PNGs:** `Screenshot 2026-04-27 at 7.47.51 PM 1.png`, `Screenshot 2026-04-27 at 7.47.51 PM 2.png`.

**Stickies (build-from / adaptation) — confirmed by Della:**
- *"build from 'ai20-mobile' mobile design"* (id `1227:21727`) → links to Figma node `983:8` (the original ai20-mobile pairing).
- *"build from 'AI-20 — Threaded Source Posts' desktop design"* (id `1227:21723`) → links to Figma node `230:2` (the original AI-20 desktop frame on canvas 29:42).

**Diagrams:**
- **AI-20 — Threaded Source Posts** (Figma `1227:21658` desktop + `1227:21731` mobile, w=760 / 375) — **KEPT, sync-from-Figma**. HTML: `img/diagrams/diagram-ai20-threaded-posts-v4.html`. Mobile pairing in tracker: Figma `983:8`.

**Interpretation:** Della duplicated the existing AI-20 desktop frame (`230:2`) and ai20-mobile (`983:8`) into row 7's new position (`1227:21658` / `1227:21731`). The stickies record the source frames so any visual tweaks Della made on the row-7 duplicates can be pulled back to `diagram-ai20-threaded-posts-v4.html` via the `figma-to-html` skill.

**Action in §6 step 4:** run `figma-to-html` on nodes `1227:21658` (desktop) and `1227:21731` (mobile). If the frames are exact duplicates of `230:2` / `983:8`, no diff lands and no work needed. If there's drift, the existing HTML gets refreshed.

**RETIRED:** `AI-21 — Comment Truncation` (was a sub-diagram, now in Retired column).

---

### 3.8 Content → voice + content *(H2 + 2 H3s)*

**Narrative purpose:** What the LLM produces — voice and content as twin lenses on the synthesis output.

**PNGs:** `Screenshot 2026-04-27 at 7.47.51 PM 3-5`, `Screenshot 2026-04-27 at 7.48.07 PM 1-2`.

**Stickies (design-intent):**
- *"what is the LLM?"* (id `1227:21815`)
- *"how should it talk? what should it say?"* (id `1229:21821`)
- *"mention linked attribution in the summary"* (id `1231:21853`) — this one sits at y≈3491, technically inside §3.6's range, but reads as a content-design note.

**Diagrams:**
- **AI-25 — Identity Explorations** (Figma `262:2`, w=760) — **KEPT** under H3 "voice". HTML: `img/diagrams/diagram-ai25-llm-identity-v4.html`. Mobile: Figma `956:8`.
- **AI-23 — Trust Spectrum** (Figma `252:2`, w=760) — **KEPT** under H3 "content". HTML: `img/diagrams/diagram-ai23-trust-comparison-v4.html`. Mobile: Figma `776:8`.

**RETIRED:**
- AI-22 — Voice Framework (`249:2`) — current intro diagram for the Voice section, dropped.
- AI-24 — Clarity Spectrum (`258:2`) — current Clarity H3, dropped.

The current `Voice` section has 4 diagrams (ai22, ai23, ai24, ai25). The new `Content` section keeps 2 (ai25 for "voice" H3, ai23 for "content" H3) and retires the framework intro + clarity diagrams.

---

### 3.9 Ensuring quality → Generating summaries: XFN workflow / feedback loops / failure states *(H2 + 3 H3s)*

**Narrative purpose:** Quality umbrella combining current `Prompt Design Workflow`, `User Feedback Loops`, and `Failure States`.

**PNGs:** `Screenshot 2026-04-27 at 6.20.00 PM 1.png`, `Screenshot 2026-04-27 at 6.53.45 PM 1+4.png`, `Screenshot 2026-04-27 at 7.02.55 PM 2+4.png`, `Screenshot 2026-04-27 at 7.03.26 PM 2.png`, `Screenshot 2026-04-27 at 7.48.07 PM 3.png`.

**Diagrams:**
- **AI-06 — Evaluation Matrix** (Figma `384:2`, w=760) — **KEPT** under H3 "Generating summaries: XFN workflow". HTML: `img/diagrams/diagram-ai06-evaluation-matrix-v4.html` + `-mobile.html`. Mobile: Figma `774:8`.
- **AI-12 — One Pattern, Three Teams** (Figma `393:2`, w=760) — **KEPT** under H3 "feedback loops". HTML: `img/diagrams/diagram-ai12-unified-feedback-v4.html`. Mobile: Figma `956:71`.
- **AI-10 — Graceful Degradation** (Figma `390:2`, w=760) — **KEPT** under H3 "failure states". HTML: `img/diagrams/diagram-ai10-failure-state-v4.html` + `-mobile.html`. Mobile: Figma `1046:8`.

**RETIRED:**
- AI-07 — Scoring Session (`385:2`) — was second diagram in current Prompt Design Workflow.
- AI-11 — The Feedback Engine (`391:2`) — was first diagram in current User Feedback Loops; ai12 carries the load now.

---

## §4 Diagram inventory

### 4.1 Kept (live in new layout — 10 diagrams)
| ID | New section | HTML file | Mobile node |
|---|---|---|---|
| AI-09 | Competing user needs | `diagram-ai09-dual-user-framework-v4.html` | `989:8` |
| AI-02a | Proof of concept / research | `diagram-ai02a-verticals-v4.html` | `972:8` |
| AI-13 | Establishing principles for generated content (summary) | `diagram-ai13-transparency-framework-v4.html` | `950:8` |
| AI-14 | Identification → UI to distinguish AI gen content | `diagram-ai14-identification-explorations-v4.html` | `982:8` |
| AI-20 | UI to display source posts | `diagram-ai20-threaded-posts-v4.html` | `983:8` (refresh from Figma) |
| AI-25 | Content → voice | `diagram-ai25-llm-identity-v4.html` | `956:8` |
| AI-23 | Content → content | `diagram-ai23-trust-comparison-v4.html` + `-mobile.html` | `776:8` |
| AI-06 | Ensuring quality → Generating summaries | `diagram-ai06-evaluation-matrix-v4.html` + `-mobile.html` | `774:8` |
| AI-12 | Ensuring quality → feedback loops | `diagram-ai12-unified-feedback-v4.html` | `956:71` |
| AI-10 | Ensuring quality → failure states | `diagram-ai10-failure-state-v4.html` + `-mobile.html` | `1046:8` |

### 4.2 New / adapted (4 to author)
| ID | Section | Source HTML to adapt | New file |
|---|---|---|---|
| Overview hero (desktop) | Overview | `diagram-ai10-failure-state-v4.html` | `diagram-ai-overview-v1.html` |
| Overview hero (mobile) | Overview | `diagram-not03-full-inbox-redesign-v5.html` mobile | `diagram-ai-overview-v1-mobile.html` |
| Before vs After | Page information architecture | None (from scratch) | `diagram-ai-ia-before-after-v1.html` |
| Identification precedent (desktop) | Identification → UI to distinguish | `diagram-not03-full-inbox-redesign-v5.html` | `diagram-ai-identification-precedent-v1.html` |

### 4.3 Retired (remove iframe blocks from `case-ai.html` — 9 diagrams)
ai02b, ai05, ai07, ai08, ai11, ai15, ai16, ai17 (placeholder), ai18 (placeholder), ai19, ai21, ai22, ai24. HTML files stay on disk under `img/diagrams/` (not deleted).

> Caveat: a count discrepancy — that list has 13 items including the 4 that were never iframe-embedded (ai17, ai18, plus the two `img-placeholder` divs in current Solution). The 9 actual iframe removals are: ai02b, ai05, ai07, ai08, ai11, ai15, ai16, ai19, ai21, ai22, ai24. Reconcile in §8.

---

## §5 Code-level changes to `case-ai.html`

### 5.1 New section blocks (insert in this order)

1. Replace the current `case-hero` + `<h2>Challenge</h2>` opener with `<h2>Overview</h2>` + Overview content (3 product PNGs as `<img class="case-img-full" src="img/screenshot-...png">` + new diagram embed for `diagram-ai-overview-v1.html`).
2. Convert current `<h3>Quality Control</h3>` → `<h2>Competing user needs</h2>`. Move ai09 here as the only diagram. Drop the first `img-placeholder` and ai08.
3. Convert current `<h3>Proving the Concept</h3>` → `<h2>Proof of concept / research</h2>`. Keep ai02a; remove ai02b iframe.
4. Replace current `<h2>Solution</h2>` block (with two `img-placeholder` divs) → `<h2>Page information architecture</h2>` + new `diagram-ai-ia-before-after-v1.html` embed.
5. Replace current `<h2>Value</h2>` block → `<h2>Establishing principles for generated content (summary)</h2>`. Move **ai13** here as the section's anchor diagram (it's repurposed from current Transparency-section opener). Remove ai05, ai07 iframes from this region; ai06 moves to Ensuring quality below.
6. Convert current `<h2>Transparency</h2>` cluster → `<h2>Identification</h2>` + `<h3>UI to distinguish AI gen content</h3>`. Keep **ai14** as the first diagram (ai13 already moved up to §3.5). Add new `diagram-ai-identification-precedent-v1.html` embed as the second diagram. Remove ai15, ai16 (and the `img-placeholder` for "Component library"), the Content Attribution block (ai19 + the `img-placeholder` for "Three attribution patterns").
7. Promote `<h3>Threaded Source Posts</h3>` → `<h2>UI to display source posts</h2>`. Keep ai20; remove ai21.
8. Replace current `<h2>Voice</h2>` cluster → `<h2>Content</h2>` with `<h3>voice</h3>` (ai25) and `<h3>content</h3>` (ai23). Remove ai22, ai24.
9. Insert new `<h2>Ensuring quality</h2>` umbrella with 3 H3s: `Generating summaries: XFN workflow` (ai06), `feedback loops` (ai12), `failure states` (ai10). Move ai06 from current Prompt Design Workflow; move ai12 from current User Feedback Loops; move ai10 from current Failure States. Remove ai07 + ai11.
10. Preserve `<h2>Results</h2>` and the metrics callout exactly as-is.

### 5.2 Iframe block pattern

Each kept diagram uses the existing pattern from current `case-ai.html`:

```html
<div class="case-img-full diagram-embed" data-diagram="ai-XX">
  <iframe src="img/diagrams/diagram-aiXX-name-v4.html" loading="lazy" scrolling="no" title="..." style="width:100%;border:none;border-radius:12px;overflow:hidden;"></iframe>
</div>
```

For paired desktop+mobile, use the existing `.diagram-pair` wrapper with `.desktop-variant` and `.mobile-variant` iframes (already used for ai06, ai10, ai16, ai19, ai23).

### 5.3 PNG block pattern (Overview row)

```html
<div class="case-img-full">
  <img src="img/[png-filename]" alt="[descriptive alt]" loading="lazy" style="width:100%;border-radius:12px;">
</div>
```

Confirm filenames against the Figma row exports — Della may need to export the Figma `Screenshot 2026-04-27 at *.png` PNGs to `img/` first.

### 5.4 CSS — `.case-card-pair` (NEW)

Della specified that paired narrative sections should render as side-by-side cards (per the reference screenshot — two dark cards labeled `CHALLENGE` / `STRATEGY` with eyebrow + body, equal widths, gap between).

**New CSS class:** `.case-card-pair` — a 2-column grid wrapping two `.case-card` children. Each card has `.card-eyebrow` (uppercase, tracked, muted) + body prose. At ≤768px, the grid collapses to a single stacked column.

```css
.case-card-pair {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--spacing-lg);
  margin: var(--spacing-2xl) 0;
}
.case-card {
  background: var(--surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: 12px;
  padding: var(--spacing-xl);
}
.card-eyebrow {
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--text-tertiary);
  margin-bottom: var(--spacing-md);
}
@media (max-width: 768px) {
  .case-card-pair { grid-template-columns: 1fr; }
}
```

**Where it applies:** **only on row 3** (the "Proof of concept / research" + "Page information architecture" pair — Figma row 3a/3b sub-rows). No other sections render as side-by-side cards unless Della explicitly asks. Both row-3 sub-sections render inside one `.case-card-pair`, with eyebrow text:

- Left card eyebrow: `PROOF OF CONCEPT`
- Right card eyebrow: `PAGE IA`

Diagrams (ai02a + Before-vs-After) appear below the card pair as visual proof points, full-width.

**Other patterns unchanged:** `.case-img-full`, `.diagram-embed`, `.diagram-pair`, `.img-placeholder` cover all other patterns. The `img-placeholder` class is removed from the page entirely (all 4 current placeholders go away).

---

## §6 Execution order (for Claude Code)

Do these in sequence; each step is verifiable.

1. **Branch off main** as `restructure/case-ai-v3` from `portfolio-site/`.
2. **Author the 4 new diagram HTML files** in §4.2 (Overview hero desktop adapted from ai10, Overview hero mobile adapted from not03 mobile, Before-vs-After from scratch, Identification precedent forked from not03 desktop). Validate each opens cleanly in a browser at 1440 / 768 / 375 widths.
2a. **Add `.case-card-pair` CSS** to `styles.css`. Test the responsive collapse at 768px against a stub before wiring into `case-ai.html`.
3. **Push the 4 new diagrams to Figma** via the `html-to-figma` skill so the canvas has matching frames at the standard mobile cluster x=-420.
4. **Sync ai20 from Figma row 7 frames** via the `figma-to-html` skill on nodes `1227:21658` (desktop) and `1227:21731` (mobile). Compare the resulting HTML to the existing `diagram-ai20-threaded-posts-v4.html`. If no diff, skip. If diff, commit the refresh as `case-ai v3: §6.4 — sync ai20 from Figma row 7`.
5. **Edit `case-ai.html`** following §5.1 in the listed order. Use the existing iframe pattern for kept diagrams. Wire in the new diagrams as iframe embeds.
6. **Export the 8 product UI PNGs** Della has in the Figma Overview / per-section rows, save to `portfolio-site/img/`. Use filenames matching the Figma layer names or Della's preferred naming.
7. **Run `python3 voice-check.py case-ai.html`** to lint copy edits.
8. **Run `python3 quality-check.py`** for HTML validity, a11y, link-check, and file-size.
9. **Take screenshots at 1440 / 768 / 375** of the rebuilt page to confirm visual structure matches the Figma layout intent.
10. **Run `recruiter-panel`** for regression scoring against case-ai baseline.
11. **Update `BUILD-LOG.md`** with the structural change summary, retired diagrams list, and new file additions.

---

## §7 Safety & rollback

Della asked for easy revert. Reinforcing the safety net so any step can be undone without re-doing prior work.

**Pre-flight (before any edits land):**
1. **Snapshot `case-ai.html`** to `older-versions/case-ai-pre-v3-restructure.html`. This is the single-file rollback target.
2. **Snapshot `styles.css`** (or whichever stylesheet gets the `.case-card-pair` addition) to `older-versions/styles-pre-v3-restructure.css`.
3. **Branch off main** as `restructure/case-ai-v3` from `portfolio-site/`. All work lands on this branch; main stays clean until final review.
4. **Tag the pre-restructure commit** as `case-ai-v2-final` so we can `git diff` against it at any point during the restructure.

**During execution (per §6 step):**
- Each of the 11 execution steps in §6 lands as its own commit. Don't squash. Commit message format: `case-ai v3: §6.{N} — {short summary}`. This makes step-level rollback trivial via `git revert <commit>`.
- New diagram HTML files (3 in §4.2) commit separately from `case-ai.html` edits. That way if a diagram needs more work, the page edits don't have to wait.
- Voice-check + quality-check + recruiter-panel results from the verification gates (§6 steps 7–10) commit alongside their step's changes for audit trail.

**Rollback ladder (escalating recovery options):**
1. **Step-level:** `git revert <commit>` on the offending §6 step's commit. Other steps stay intact.
2. **Section-level:** if a single H2 section's edits are wrong, edit `case-ai.html` to restore that section from the snapshot (`older-versions/case-ai-pre-v3-restructure.html`) — keep the rest of the new structure.
3. **File-level:** restore `case-ai.html` and `styles.css` wholesale from the `older-versions/` snapshots. New diagram HTML files stay on disk (unused) for future use.
4. **Branch-level:** abandon the `restructure/case-ai-v3` branch entirely. Main is untouched.
5. **Nuclear:** re-merge `case-ai-v1.html` from `older-versions/` if even v2 is wrong — last resort.

**What's preserved either way:**
- All retired diagram HTML files stay on disk under `img/diagrams/`. Re-embedding any one of them is a 10-line edit.
- All new diagram HTML files are additive — removing iframes doesn't break them.
- Figma canvas is the source of truth for the new structure. If this doc drifts from canvas during execution, re-pull canvas (per the howto in `figma-outline-extraction-howto.md`).
- All 19 case-ai mobile-Figma pairings stay tracked in `working/mobile-audit/audit-tracker.xlsx` regardless of which diagrams are live in the new layout.

---

## §8 Open questions

**Resolved by Della (2026-04-28):**
- ✅ §3.5 has a diagram (ai13). Confirmed via row 4t/4i pairing.
- ✅ §3.6 Identification precedent forks to a new file (`diagram-ai-identification-precedent-v1.html`) — fresh export from Figma rather than reusing `diagram-not03-full-inbox-redesign-v5.html` directly.
- ✅ §3.1 Overview PNGs are new captures (not the existing `klp-ui-*.png`). Need to be exported from Figma to `portfolio-site/img/` as part of §6 step 6.
- ✅ Rollback approach approved — see §7 hardened ladder.
- ✅ §5.4 card-pair eyebrows = `PROOF OF CONCEPT / PAGE IA`.
- ✅ §5.4 card-pair scope = row 3 only. No other sections get the side-by-side treatment unless Della explicitly asks.
- ✅ §3.7 ai20 stickies = sync row-7 duplicate frames (`1227:21658` / `1227:21731`) back to existing HTML via `figma-to-html`. No-op if frames are exact duplicates of `230:2` / `983:8`.

**Still open (low-priority — flag during execution, not blockers):**
1. **§4.3 Retired-on-disk policy:** the 11 retired diagrams' HTML files stay on disk under `img/diagrams/`. Current plan: leave them. Della to call if any should be moved to `older-versions/` or deleted.
2. **Results section preservation:** keeping current 15M WAU metric callout + handoff narrative as-is. Della to confirm no narrative tweaks during §6 step 5.
3. **Establishing principles section copy:** moving ai13 here means the section's narrative needs to bridge "principles framework" with ai13's current content (which anchors Transparency in the live page). Flag for content-pass after structural edits land — likely a separate writing session, not part of the structural restructure.

---

**Doc location:** `portfolio-site/working/planning-docs/case-ai-change-outline.md`.
**Working artifact:** `outputs/klp-figma/figma-meta-klp.xml` (raw Figma metadata, 4448 lines, source of all extractions in this doc).
