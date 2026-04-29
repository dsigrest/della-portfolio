# case-ai (KLP / Reddit Answers MVP) — Change Outline v2

**Status:** Spec drafted from direct case-ai.html line citations + Figma source-frame screenshots. Ready for Della review. **No HTML execution begins until Della signs off and resolves §6 open questions.**

**Predecessor:** `case-ai-change-outline.md` (v1). v1's §2 heading hierarchy and §5.1 structural-edit list are still correct. v2 supersedes v1 by adding the prose-preservation map (with case-ai.html line citations), a strict voice rule, and visual specs for the 4 new diagrams.

**Source-of-truth files:**
- v2 deployed prose: `case-ai.html` (current state — backup at `older-versions/case-ai-pre-v3-restructure.html`, tag `case-ai-v2-final`)
- Figma layout reference: page `29:42` (*2. Reddit Answers MVP*) in *Portfolio — Image Inventory* (`TArUrZsBUocaAsqetjXq7V`)
- Figma metadata extraction: `outputs/klp-figma/figma-meta-klp.xml` (4448 lines)
- Verified facts: `working/planning-docs/verified-facts-registry.md`

**Target file:** `case-ai.html` (project root). **Diagram folder:** `img/diagrams/`. **No DRAFT rehearsal file** — surgical edits land on `case-ai.html` directly. The v1-DRAFT path was discarded; archive lives at `working/discarded/case-ai-v3-DRAFT-2026-04-28.html` for reference.

---

## §0 Voice rule (NON-NEGOTIABLE)

**All prose preserved verbatim from `case-ai.html` with line citations. No invention.**

What this means:
1. The Figma canvas (`29:42`) is a **layout document**, not a prose source. The wide PNG "banner" frames pasted on the canvas are screenshots OF case-ai.html prose — Della used them to mark which v2 paragraphs belong in which v3 position. They are not new prose.
2. The 4 NEW diagram source frames in Figma (`1203:5207`, `1207:5594`, `1202:5101`, `1226:21284`) ARE the visual source of truth — they're rich product-UI mocks. The HTML diagrams must reproduce these visuals, not invent abstract diagram content.
3. If a v3 position has no v2 prose source, **leave the prose unwritten** and flag for Della in §6 — do not generate bridge prose, intro paragraphs, or section openers from training knowledge.
4. Verbatim means **character-for-character identical** to the cited line. No paraphrase, no "tightening," no "voice fixes." If a paragraph reads off in the new position, that's an open question for Della — not a license to revise.
5. Diagrams have **no chrome inside the iframe body** — no `<h1>`, no `.label`, no `.subtitle`. The case-study HTML provides the section heading. Reference: `diagram-ai13-transparency-framework-v4.html`, `diagram-ai14-identification-explorations-v4.html`, `diagram-ai20-threaded-posts-v4.html`.

**Source-verification reminder (project CLAUDE.md):** every metric, timeline, team detail must trace to `verified-facts-registry.md`. The structural restructure in v3 doesn't change any facts — just rearranges existing prose.

---

## §1 v2 → v3 position table

The v3 page hierarchy (per v1 §2) lands as 8 H2 sections with 5 H3s + Results. This table maps each v3 position to its v2 source line range and its diagram changes.

| v3 Pos | v3 Heading | v2 source | case-ai.html lines (verbatim) | Diagram(s) | Δ from v1 outline |
|---|---|---|---|---|---|
| 1 | `<h2>Overview</h2>` | NEW (no v2 source) | OPEN — see §6.1 | `diagram-ai-overview-v1.html` (paired desktop+mobile) — re-author from Figma `1203:5207` / `1207:5594` | adds prose-decision flag |
| 2 | `<h2>Competing user needs</h2>` (was `<h3>Quality Control</h3>`) | Row 2 | 189, 201, 213, 215 | ai09 (`diagram-ai09-dual-user-framework-v4.html` + mobile `989:8`) | clarifies which 4 paragraphs preserve |
| 3a | `<h2>Proof of concept / research</h2>` (was `<h3>Proving the Concept</h3>`) inside `.case-card` | Row 3a | 84, 106 | ai02a (`diagram-ai02a-verticals-v4.html` + mobile `972:8`) | inside `.case-card-pair` left card (eyebrow `PROOF OF CONCEPT`) |
| 3b | `<h2>Page information architecture</h2>` (was `<h2>Solution</h2>`) inside `.case-card` | Row 3b | 114, 120, 126 | NEW `diagram-ai-ia-before-after-v1.html` from Figma `1202:5101` | inside `.case-card-pair` right card (eyebrow `PAGE IA`); 2 `img-placeholder` divs dropped |
| 4 | `<h2>Establishing principles for generated content (summary)</h2>` (was `<h2>Value</h2>`) | Row 4 | 146 (only) | ai13 (`diagram-ai13-transparency-framework-v4.html` + mobile `950:8`) | v2 line 134 retired with ai05; bridge prose flagged in §6.2 |
| 5 | `<h2>Identification</h2>` + `<h3>UI to distinguish AI gen content</h3>` (was `<h2>Transparency</h2>` + `<h3>Identification (UI)</h3>`) | Row 5 (top of Transparency section) | 274, 288, 300, 312 | ai14 (`diagram-ai14-identification-explorations-v4.html` + mobile `982:8`) + NEW `diagram-ai-identification-precedent-v1.html` from Figma `1226:21284` | ai13 moves up to Pos 4; ai15+ai16 retired; new precedent diagram from inbox-redesign mock; precedent-bridge prose flagged in §6.3 |
| 6 | `<h2>UI to display source posts</h2>` (was `<h3>Threaded Source Posts</h3>`) | Row 6 | 374, 386, 398 | ai20 (`diagram-ai20-threaded-posts-v4.html` + mobile `983:8`, sync from Figma `1227:21658`/`1227:21731` if drift) | h3 → h2; ai21 retired |
| 7a | `<h2>Content</h2>` opener | Row 7 (Voice opener) | 406 | none | h2 retitle |
| 7b | `<h3>voice</h3>` | Row 7 (LLM as Narrator subsection) | 459, 471 | ai25 (`diagram-ai25-llm-identity-v4.html` + mobile `956:8`) | retitled from "The LLM as Narrator"; ai22 retired (line 406 already covers Voice intro) |
| 7c | `<h3>content</h3>` | Row 7 (Tone subsection) | 420 | ai23 paired (`diagram-ai23-trust-comparison-v4.html` + `-mobile.html`, mobile node `776:8`) | retitled from "Tone" (the ai23 Trust Spectrum content) |
| 8a | `<h2>Ensuring quality</h2>` umbrella | NEW (no v2 source) | OPEN — see §6.4 | none | umbrella H2 has no v2 paragraph; flag for Della |
| 8b | `<h3>Generating summaries: XFN workflow</h3>` (was `<h3>Prompt Design Workflow</h3>`) | Row 8 | 150, 152, 173, 185 | ai06 paired (`diagram-ai06-evaluation-matrix-v4.html` + `-mobile.html`, mobile `774:8`) | h3 retitle; ai07 retired |
| 8c | `<h3>feedback loops</h3>` (was `<h3>User Feedback Loops</h3>`) | Row 9 | 244, 256 | ai12 (`diagram-ai12-unified-feedback-v4.html` + mobile `956:71`) | h3 retitle (lowercase); ai11 retired |
| 8d | `<h3>failure states</h3>` (was `<h3>Failure States</h3>`) | Row 10 | 219, 221 | ai10 paired (`diagram-ai10-failure-state-v4.html` + `-mobile.html`, mobile `1046:8`) | h3 retitle (lowercase) |
| 9 | `<h2>Results</h2>` | Row 11 (final h2) | 479, 481 + metrics-callout block (483–488) + case-next block (490–496) | none (metrics-callout preserved) | unchanged |

**Retirements (iframe blocks removed from `case-ai.html`):**

| v2 lines | Section/diagram retired | Why |
|---|---|---|
| 78–80 | Challenge opener `img-placeholder` ("Diagram — user query hits Google → lands on Reddit → scattered partial answers") | Challenge section replaced by Overview (Pos 1) |
| 96–104 | ai02b iframe ("Static MVP Process") | retired per v1 §3.3 — section drops from 2 diagrams → 1 |
| 116–118 | Solution `img-placeholder` #1 ("Page architecture — synthesis summary on top...") | replaced by `diagram-ai-ia-before-after-v1.html` |
| 122–124 | Solution `img-placeholder` #2 ("Flow — search query → synthesized summary...") | redundant once new IA diagram lands |
| 132–144 | Value h2 opener + line 134 prose ("User value was foundational...") + ai05 iframe ("Three-Way Balance") | per v1 §3.5 — Value section dissolves into "Establishing principles" with ai13 anchor; the 3-way balance framing is retired |
| 175–183 | ai07 iframe ("Scoring Session") | per v1 §3.9 — was second diagram in Prompt Design Workflow |
| 191–199 | ai08 iframe ("Page Anatomy") | per v1 §3.2 — Quality Control retitled to Competing user needs, only ai09 kept |
| 246–254 | ai11 iframe ("Feedback Loop") | per v1 §3.9 — ai12 carries User Feedback Loops |
| 268–283 | Transparency h2 opener + line 274 paragraph + ai13 iframe (in original position) | ai13 MOVES to Pos 4 anchor; the line 274 paragraph is reused at the top of Pos 5 (see §2.5) |
| 302–310 | ai15 iframe ("Sparkle Reactions") | per v1 §3.6 — Identification trims to ai14 + new precedent |
| 314–331 | ai16 iframe paired ("Final Identification") | per v1 §3.6 |
| 333–339 | Scalability h3 + line 335 paragraph + `img-placeholder` ("Component library") | per v1 §3.6 — Scalability subsection removed |
| 341–349 | Content Attribution h3 + lines 343 + 349 paragraphs + `img-placeholder` ("Three attribution patterns tested") | per v1 §3.6 — Content Attribution subsection removed |
| 351–368 | ai19 paired iframe ("Attribution Comparison") | per v1 §3.6 — attribution work retired |
| 370 | Line 370 paragraph ("The study results also informed...") | follows ai19; retired with that subsection |
| 388–396 | ai21 iframe ("Comment Truncation") | per v1 §3.7 |
| 408–416 | ai22 iframe ("Voice Framework") | per v1 §3.8 |
| 418–438 | h3 Tone + line 420 paragraph + ai23 paired iframe (in original position) | line 420 MOVES to Pos 7c; ai23 paired iframe MOVES with it (see §2.7c) |
| 441–453 | h3 Clarity + line 443 paragraph + ai24 iframe + line 455 paragraph | per v1 §3.8 — Clarity retired |
| 457–471 | h3 The LLM as Narrator + lines 459 + 471 paragraphs + ai25 iframe (in original position) | lines 459 + 471 + ai25 iframe MOVE to Pos 7b (see §2.7b) |

**Diagram HTML files retained on disk (not deleted) per v1 §7:** ai02b, ai05, ai07, ai08, ai11, ai15, ai16, ai17 (placeholder), ai18 (placeholder), ai19, ai21, ai22, ai24.

---

## §2 Per-position entries (verbatim quotes + line citations)

### Pos 1 — `<h2>Overview</h2>` *(NEW)*

**v2 source:** none. Replaces `<h2>Challenge</h2>` (v2 lines 74–80) and the Challenge opener paragraph (line 76: *"**Reddit content was scattered** across posts and communities..."*).

**Body prose:** **OPEN — see §6.1.** Three options for Della to pick:
- **A. Reuse the v2 Challenge opener (line 76 verbatim)** as the Overview lede. Strong product framing already; just retitle the H2.
- **B. Write a new Overview lede** — Della provides a sentence or two; flagged as `<!-- DELLA: Overview lede -->` until she does.
- **C. No prose** — the Overview is diagram + product-UI screenshots only, no body text.

**Diagram:** `diagram-ai-overview-v1.html` (desktop) + `diagram-ai-overview-v1-mobile.html` (mobile) — paired via `.diagram-pair`. **Both must be re-authored from scratch** — the current files are abstract diagrams with title chrome and don't match the Figma source. Visual spec in §3.1.

**PNG screenshots from Figma row 1 left column (the small product UI captures, NOT the wide prose banners):** Della to confirm whether any small product UI captures from row 1 should be embedded as standalone `<img>` tags above/below the diagram. Most candidates from metadata appear to be prose screenshots (e.g., `1207:5592` is the Quality Control prose; `1202:5163` is the Solution prose) — not product UIs to embed. **Recommendation:** Overview row uses ONLY the diagram pair (which itself contains rich product UI mocks). No standalone PNGs. Della to confirm in §6.1.

**Pos 1 ship criteria:**
- [ ] Della picks A/B/C for Overview prose
- [ ] `diagram-ai-overview-v1.html` rebuilt to match Figma `1203:5207` visually
- [ ] `diagram-ai-overview-v1-mobile.html` rebuilt to match Figma `1207:5594` visually
- [ ] Both diagrams chrome-less in body (no `<h1>`, no `.label`, no `.subtitle`)
- [ ] Della confirms whether row-1 PNG embeds are needed

---

### Pos 2 — `<h2>Competing user needs</h2>`

Was: `<h3>Quality Control</h3>` (v2 line 187) inside the Value section. v3 promotes to its own H2.

**Body prose** — verbatim from `case-ai.html`:
- **Line 189:** *"Two users with competing needs: **Googlebot and humans.** Underlinking and underusing keywords hurt SEO. Overusing keywords hurt humans. I didn't know what Googlebot needed; engineers weren't familiar with Reddit's users or the SEO cohort. A healthy back-and-forth led to capturing both full sets of needs."*
- **Line 201:** *"**Framing Googlebot as a user was the breakthrough.** When I told designers we needed something for SEO, they pushed back — that's not a user need. But anthropomorphizing it as a competing set of needs instead of a technical constraint opened doors across the team."*
- **Line 213:** *"I pushed back on **resurfacing the query multiple times on the page.** SEO loved keyword repetition; it did nothing for users. The compromise: pre-populate the search bar with the user's query, as if they'd already searched Reddit. SEO got the keyword on the page; the design **reinforced the mental model** that users should be searching on Reddit directly."*
- **Line 215:** *"Keywords were embedded in **structured page elements outside the summary** — synthesis stayed natural while the page still ranked."*

**Order in v3 section:** 189 → ai09 iframe → 201 → 213 → 215. (Diagram between 1st and 2nd paragraphs, matches v2 placement.)

**Diagram:** `diagram-ai09-dual-user-framework-v4.html` (existing, KEPT). Mobile node `989:8`.

**Retired:** ai08 iframe (v2 lines 191–199) — Page Anatomy. Per v1 §3.2.

**Pos 2 ship criteria:**
- [ ] All 4 paragraphs preserved verbatim with their exact `<strong>` and `<em>` runs
- [ ] ai09 iframe retained, ai08 iframe removed
- [ ] H3 → H2 promotion
- [ ] No paragraph drift

---

### Pos 3 — `.case-card-pair` row (Pos 3a + Pos 3b side by side)

**Card-pair shell:**
```html
<div class="case-card-pair">
  <div class="case-card">
    <div class="card-eyebrow">Proof of concept</div>
    <!-- Pos 3a content -->
  </div>
  <div class="case-card">
    <div class="card-eyebrow">Page IA</div>
    <!-- Pos 3b content -->
  </div>
</div>
```

Diagrams (ai02a + new IA before-after) appear **below the card pair, full-width** — NOT inside the cards.

#### Pos 3a — `<h2>Proof of concept / research</h2>` (inside left card)

Was: `<h3>Proving the Concept</h3>` (v2 line 82) inside Challenge section.

**Body prose** — verbatim from `case-ai.html`:
- **Line 84:** *"To get the resources for dynamic generation, we had to **prove the idea first.** Chicken-and-egg: the team needed proof of concept before investing in infrastructure, but building proof of concept required building the product."*
- **Line 106:** *"We started with **static pages refreshed periodically**, targeting the verticals with the strongest source coverage and the largest audiences — maximum impact with the resources we had."*

**Diagram (placed below card pair):** `diagram-ai02a-verticals-v4.html` (existing, KEPT). Mobile node `972:8`.

**Retired:** ai02b iframe (v2 lines 96–104) — Static MVP Process.

#### Pos 3b — `<h2>Page information architecture</h2>` (inside right card)

Was: `<h2>Solution</h2>` (v2 line 112).

**Body prose** — verbatim from `case-ai.html`:
- **Line 114:** *"I designed an **LLM-powered synthesis** that consolidated content across posts and communities into a single entry point matched to the user's search intent — with source posts threaded below."*
- **Line 120:** *"The **dual-layer layout** was the core design decision. Synthesis on top gave users instant answers; source posts below let them verify and go deeper. Links across both layers created endless on-ramps into the platform — and Googlebot loved the link density. One page, both users served."*
- **Line 126:** *"The long bet: shift the mental model from appending **reddit** to a Google search toward searching Reddit directly."*

**Open question — §6.5:** v1 outline §3.4 had this card's heading as "Page information architecture" but line 120's prose says *"The **dual-layer layout** was the core **design** decision."* The v1 retitle reframes this as an IA decision rather than a design decision. Should line 120 be reworded inside the card to *"core IA decision"* — or stay verbatim? Recommend stay verbatim (voice rule); Della confirms.

**Diagram (placed below card pair):** NEW `diagram-ai-ia-before-after-v1.html` from Figma `1202:5101`. Visual spec in §3.3.

**Retired:** Both Solution `img-placeholder` divs (v2 lines 116–118 and 122–124).

#### After the card pair (still in Pos 3)

**Trailing paragraph** — verbatim:
- (none — line 126 was already inside Pos 3b. Pos 3 ends with the IA before-after diagram.)

**Pos 3 ship criteria:**
- [ ] `.case-card-pair` wraps both subsections per the shell pattern
- [ ] Eyebrows: `Proof of concept` (left) / `Page IA` (right)
- [ ] All 5 paragraphs preserved verbatim
- [ ] ai02a placed full-width below the card pair (not inside left card)
- [ ] New IA before-after diagram placed full-width below the card pair (not inside right card)
- [ ] At ≤768px, card-pair grid collapses to single column (per §5.4 v1 outline)
- [ ] ai02b iframe + 2 `img-placeholder` divs removed
- [ ] Della confirms line 120 verbatim vs. "IA decision" rewording

---

### Pos 4 — `<h2>Establishing principles for generated content (summary)</h2>`

Was: `<h2>Value</h2>` (v2 line 132).

**Body prose** — verbatim from `case-ai.html`:
- **Line 146:** *"The page was also **training users** — showing them what a search result on Reddit could look like. Ideal behavior: click into a post for more detail, or search again from the bar at the top. Both paths pull deeper into the platform."*

**Open question — §6.2:** the v1 outline notes the v2 line 134 "User value was foundational — three-way balance" prose is retired with ai05. That leaves Pos 4 with only line 146 + an unbridged transition into ai13's content. Three options for Della:
- **A. Place line 146 verbatim, no bridge** — section reads as a single paragraph + ai13. Sparse but voice-clean.
- **B. Della writes a new bridge sentence** between the H2 and line 146 to introduce the principles framework concept, then ai13. Flagged as `<!-- DELLA: principles bridge -->` until she writes.
- **C. Move line 146 below ai13** so ai13 leads the section, then line 146 closes it. Same prose, different order.

**Diagram:** ai13 (`diagram-ai13-transparency-framework-v4.html` + mobile `950:8`) — KEPT, MOVED here from v2 Transparency opener (lines 276–283).

**Retired:** Value h2 opener (line 132) wrapper + line 134 paragraph ("User value was foundational...") + ai05 iframe.

**Pos 4 ship criteria:**
- [ ] Della picks A/B/C for §6.2 bridge
- [ ] Line 146 preserved verbatim
- [ ] ai13 iframe moved here from v2 Transparency position
- [ ] ai05 iframe + line 134 paragraph removed

---

### Pos 5 — `<h2>Identification</h2>` + `<h3>UI to distinguish AI gen content</h3>`

Was: `<h2>Transparency</h2>` (v2 line 272) + `<h3>Identification (UI)</h3>` (v2 line 286).

**Body prose** — verbatim from `case-ai.html`:
- **Line 274** (under h2): *"We needed to define the **first precedent for AI-generated content at Reddit** — across the entire platform. I partnered with brand, legal, and design systems to establish what AI content would be, how it would identify itself, and how it would attribute its sources."*
- **Line 288** (under h3 UI to distinguish): *"The question was bigger than visual design: **what's a scalable, instantly recognizable, but unobtrusive signal** that content was AI-generated? User research confirmed people valued knowing — but this was peak AI backlash. The signal had to build trust without feeling like a trend."*
- **Line 300** (after ai14 iframe in v2): *"We explored icons, tags, containers, disclaimers, a talking Snoo, and text treatments. The **sparkle icon got negative reactions** — users saw it as a cliché. Like Sharing &amp; Embeds, this crossed beyond design systems into identity."*
- **Line 312** (after ai15+ai16 iframes in v2): *"We landed on **a system, not a single solution.** It scaled across surfaces depending on context, with persistent elements: same color, same name, always visually separated from other content. Flexible by surface, consistent in identity."*

**Order in v3 section:**
- H2 + line 274 (Identification opener)
- H3 + line 288 (UI to distinguish)
- ai14 iframe
- line 300 (sparkle reactions context)
- line 312 (system landed on)
- **§6.3 bridge sentence** (open question — see below)
- new precedent diagram iframe

**Open question — §6.3:** the new precedent diagram (`diagram-ai-identification-precedent-v1.html`) needs a bridge sentence introducing it as the inbox-redesign precedent applied to the AI page. Three options:
- **A. No bridge** — diagram caption (in title attribute) carries the meaning. Della writes a content-pass later.
- **B. Della writes a one-liner** — flagged as `<!-- DELLA: identification precedent bridge -->`.
- **C. Pull from notifications case study** — copy the relevant precedent description verbatim from `case-notifications.html` if she has one there. (Lower priority; check whether such prose exists before suggesting.)

**Diagrams (in order):**
1. ai14 (`diagram-ai14-identification-explorations-v4.html` + mobile `982:8`) — KEPT in same position
2. NEW `diagram-ai-identification-precedent-v1.html` from Figma `1226:21284` — re-author, visual spec in §3.4

**Retired (in this section):** ai15 iframe (v2 lines 302–310), ai16 paired iframe (lines 314–331), Scalability subsection (lines 333–339), Content Attribution subsection (lines 341–349 + ai19 + line 370).

**Pos 5 ship criteria:**
- [ ] H2 + h3 with proper hierarchy
- [ ] Lines 274, 288, 300, 312 preserved verbatim
- [ ] ai14 iframe in correct position (after line 288)
- [ ] §6.3 bridge resolved
- [ ] New precedent diagram embedded (chrome-less in body, matches Figma `1226:21284`)
- [ ] ai15, ai16 paired, ai19 paired, Scalability + Content Attribution subsections fully removed

---

### Pos 6 — `<h2>UI to display source posts</h2>`

Was: `<h3>Threaded Source Posts</h3>` (v2 line 372).

**Body prose** — verbatim from `case-ai.html`:
- **Line 374:** *"User research kept surfacing the same question: **where is this coming from?** The source posts below the synthesis were the answer — and displaying them required a new UI pattern. Posts appeared in a threaded structure with comments for the first time at Reddit."*
- **Line 386:** *"I worked with data science on **comment truncation**: the vast majority of comments fit 1–2 lines, with severe diminishing returns after that. We landed on **two comments per post** — enough to show a conversation without overwhelming the unit."*
- **Line 398:** *"The text truncation system **reused a pattern I'd built for Sharing &amp; Embeds** — already defined and validated, which made this work go faster."*

**Order in v3 section:** 374 → ai20 iframe → 386 → 398. (ai21 retired.)

**Diagram:** ai20 (`diagram-ai20-threaded-posts-v4.html` + mobile `983:8`). KEPT, with figma-to-html sync from row 7 frames `1227:21658` (desktop) and `1227:21731` (mobile) per v1 §3.7. If frames are exact duplicates of `230:2` / `983:8`, no-op; if drift, refresh HTML.

**Retired:** ai21 iframe (v2 lines 388–396).

**Pos 6 ship criteria:**
- [ ] H3 → H2 promotion
- [ ] All 3 paragraphs preserved verbatim
- [ ] ai20 iframe retained; ai21 iframe removed
- [ ] §6.4 figma-to-html sync run (likely no-op)

---

### Pos 7 — `<h2>Content</h2>` + 2 H3s

Was: `<h2>Voice</h2>` (v2 line 404) with subsections `<h3>Tone</h3>` (line 418), `<h3>Clarity</h3>` (line 441), `<h3>The LLM as Narrator</h3>` (line 457).

#### Pos 7a — `<h2>Content</h2>` opener

**Body prose** — verbatim from `case-ai.html`:
- **Line 406:** *"Defining what the LLM produced was as much a design problem as defining how it looked. I led the decisions around **tone, clarity, and the model's relationship to Reddit.**"*

**Open question — §6.6:** line 406 says *"tone, clarity, and the model's relationship to Reddit"* — but the v3 H3s are `voice` and `content`, with Clarity retired. The triple in line 406 doesn't match the v3 H3 structure. Three options:
- **A. Preserve line 406 verbatim** — accept the cosmetic mismatch ("Voice → Content" rename hides it; readers won't notice the triple is off).
- **B. Della writes a new opener** for the Content section that maps to the new H3s (voice + content). Flagged.
- **C. Trim line 406** to the first sentence only: *"Defining what the LLM produced was as much a design problem as defining how it looked."* — drops the second sentence. Modest edit; voice rule violation but small.

#### Pos 7b — `<h3>voice</h3>`

Pulled from v2 *The LLM as Narrator* subsection (line 457).

**Body prose** — verbatim from `case-ai.html`:
- **Line 459:** *"The team debated: is the LLM **Reddit, the Snoo, a character, a tool, or omnipresent?** We explored each. Giving the synthesis a product identity conflicted with how people expected results in search — is it "Answers" or is it search?"*
- **Line 471** (after ai25 iframe): *"We landed on **omnipresent narrator without a character.** It preserves scalability, smooths integration, and resolves the core tension: the synthesis isn't a separate product. It's part of the product. It is the product."*

**Order:** 459 → ai25 iframe → 471.

**Diagram:** ai25 (`diagram-ai25-llm-identity-v4.html` + mobile `956:8`). KEPT.

**Retired (in this Voice→Content remap):** ai22 iframe (Voice Framework, lines 408–416), Voice section opener at line 406 if Della picks §6.6 option B/C.

#### Pos 7c — `<h3>content</h3>`

Pulled from v2 *Tone* subsection (line 418).

**Body prose** — verbatim from `case-ai.html`:
- **Line 420:** *"**Closeness to source posts drove trust.** Broad generalizations — a consistent failure mode in early outputs — killed it immediately. Synthesizing across communities without losing the source voice was the harder question."*

**Order:** 420 → ai23 paired iframe.

**Diagram:** ai23 paired (`diagram-ai23-trust-comparison-v4.html` desktop + `-mobile.html`, mobile `776:8`). KEPT.

**Retired:** Tone H3 wrapper, Clarity H3 + line 443 paragraph + ai24 iframe + line 455 paragraph.

**Pos 7 ship criteria:**
- [ ] H2 retitle + 2 H3s in lowercase
- [ ] §6.6 opener resolved
- [ ] Lines 420, 459, 471 preserved verbatim
- [ ] ai25 + ai23 paired diagrams retained
- [ ] ai22, ai24 + Clarity subsection removed

---

### Pos 8 — `<h2>Ensuring quality</h2>` umbrella + 3 H3s

NEW umbrella H2 with 3 H3s pulled from v2 sections.

#### Pos 8a — `<h2>Ensuring quality</h2>` opener

**Open question — §6.4:** no v2 opener prose for this umbrella. Two options:
- **A. No opener prose** — section is heading + 3 H3 subsections, each with their own paragraphs. Sparse but voice-clean.
- **B. Della writes a one-liner** — flagged as `<!-- DELLA: Ensuring quality lede -->`.

#### Pos 8b — `<h3>Generating summaries: XFN workflow</h3>`

Was: `<h3>Prompt Design Workflow</h3>` (v2 line 148).

**Body prose** — verbatim from `case-ai.html`:
- **Line 150:** *"**No evaluation criteria, no feedback loop, no shared language** for how synthesis should work. Prompt iteration was one engineer, vibes-based. This team had started as a top-of-funnel SEO team and later specialized into ML — they'd **never worked with a designer before.** Kickoffs, iteration walkthroughs, design systems — all new."*
- **Line 152:** *"I bridged engineering and content design to build a **structured evaluation matrix.** There was initial resistance — engineers wanted to move fast, but output wasn't improving. I made it concrete: pulled them into creating the rubric and evaluating outputs against it. **Involvement drove buy-in.**"*
- **Line 173** (after ai06 paired iframe): *"Parameters: **sentence structure** variation, **accuracy to source** (sliding scale — reference where useful, don't replicate the post), **novel synthesized info** across posts, **length adherence**, **tone** (not mechanical, not cold — like a friend), content design guidelines (remember the human, be direct, consider i18n), and **SEO signals** (keywords, connected links)."*
- **Line 185** (after ai07 iframe in v2): *"I partnered with content design to define **evaluation dimensions**, then facilitated **scoring sessions** where our cross-functional team rated outputs against the rubric. It had to be precise enough for non-designers to apply consistently."*

**Order:** 150 → 152 → ai06 paired iframe → 173 → 185. (ai07 retired.)

**Diagram:** ai06 paired (`diagram-ai06-evaluation-matrix-v4.html` desktop + `-mobile.html`, mobile `774:8`). KEPT, MOVED here from v2 Value section.

**Retired:** ai07 iframe (Scoring Session, v2 lines 175–183).

#### Pos 8c — `<h3>feedback loops</h3>`

Was: `<h3>User Feedback Loops</h3>` (v2 line 242).

**Body prose** — verbatim from `case-ai.html`:
- **Line 244:** *"Flagged outputs surfaced where the model was weakest. The rubric **evolved based on what users actually valued** versus what we'd assumed. We shipped roughly **twice a quarter** — test with UXR, build, ship, collect data, then back to UXR with new questions. Iterations overlapped; multiple elements were in different stages of the cycle at any time."*
- **Line 256** (after ai11 iframe in v2): *"The **feedback UI was a cross-org effort**: three teams (KLPs, search, i18n) were independently building feedback patterns. I worked across pillars to define one recognizable component — users see it and know where to give their opinion. Another pattern built for this project, adopted org-wide."*

**Order:** 244 → 256 → ai12 iframe. (ai11 retired.)

**Open question — §6.7:** in v2, ai11 sat between lines 244 and 256, and ai12 came after line 256. With ai11 retired, where does ai12 land? Recommend: 244 → 256 → ai12 (ai12 closes the section, like it did in v2 after line 256). Della confirms.

**Diagram:** ai12 (`diagram-ai12-unified-feedback-v4.html` + mobile `956:71`). KEPT.

**Retired:** ai11 iframe (Feedback Loop, v2 lines 246–254).

#### Pos 8d — `<h3>failure states</h3>`

Was: `<h3>Failure States</h3>` (v2 line 217).

**Body prose** — verbatim from `case-ai.html`:
- **Line 219:** *"**Below-threshold summaries didn't appear.** Instead, the page surfaced the aggregated source posts — still valuable, still pulling users deeper into the platform."*
- **Line 221:** *"The design principle: **degradation is not failure.** The fallback — threaded sources — is the reliable baseline; synthesis is the enhancement on top."*

**Order:** 219 → 221 → ai10 paired iframe.

**Diagram:** ai10 paired (`diagram-ai10-failure-state-v4.html` desktop + `-mobile.html`, mobile `1046:8`). KEPT.

**Pos 8 ship criteria:**
- [ ] H2 umbrella in place; 3 H3s in lowercase per v1 hierarchy
- [ ] §6.4 opener decision resolved
- [ ] All 8 cited paragraphs preserved verbatim (lines 150, 152, 173, 185, 244, 256, 219, 221)
- [ ] §6.7 ai12 placement resolved
- [ ] ai06 paired moved here from v2 Value section
- [ ] ai07 + ai11 iframes removed

---

### Pos 9 — `<h2>Results</h2>`

Unchanged from v2.

**Body prose** — verbatim from `case-ai.html`:
- **Line 479:** *"The dual-layer layout kept users on pages they used to bounce from. The evaluation rubric turned vibes-based prompting into a repeatable quality system. The identification framework gave Reddit a scalable precedent for AI content. But the biggest impact was strategic: **the MVP's performance proved synthesis belonged inside search**, not as a standalone SEO product. Sending users from one search-like surface to another was the dead end that clarified the real opportunity."*
- **Line 481:** *"I handed off the framework and foundation to the next designer, and the systems I built — identification library, synthesis patterns, feedback UI, evaluation rubric, governance framework — were **inherited directly** by a new team that shipped them as Reddit Answers."*

**Metrics callout:** lines 483–488 preserved exactly (`15M weekly active users` per `verified-facts-registry.md`).

**Case-next block:** lines 490–496 preserved exactly (link to `case-sharing.html`).

**Pos 9 ship criteria:**
- [ ] No edits to lines 479–496 except as needed by the surrounding restructure
- [ ] Metrics callout intact (15M WAU per verified-facts-registry)

---

## §3 Diagram visual specs (4 NEW files to author)

These are **product-UI mocks**, not abstract diagrams. The HTML must reproduce the Figma source frame visually. Authoring agent: **call `mcp__Figma__get_screenshot` on the source node BEFORE writing markup**. Don't generate from the description below alone.

### §3.1 `diagram-ai-overview-v1.html` ← Figma `1203:5207` (760×958)

**Visual:** 2-column layout side-by-side. Each column ~50% width.

**Left column ("BELOW THRESHOLD"):**
- Pill label centered above: `BELOW THRESHOLD` in casual-tone (red/coral) chip
- Phone mock (~250–300 wide, full bezel) showing Google search results for "best sunscreen 2024":
  - Google search bar at top with profile circle on right
  - Tabs: All, Forums (active), Shopping, Images, News, Video
  - Filter chips: For face, Reddit, For dry skin, For sensitive sk...
  - 3 stacked search-result cards (reddit.com), each with: small Reddit icon, URL line, blue title, body snippet
  - Phone bottom nav: back, forward, share, home, tabs
- 2 annotation chips below the phone:
  - `Synthesis suppressed — quality below confidence threshold`
  - `Raw source posts surface as fallback`

**Right column ("ABOVE THRESHOLD"):**
- Pill label centered above: `ABOVE THRESHOLD` in cool-tone (blue/teal) chip
- Phone mock with Reddit Answers UI for same query:
  - Same Google search bar
  - Tabs: AI Mode, All (active), Shopping, Short videos, Images
  - Same filter chips
  - 1 large Reddit Answers card at top: Reddit icon + "r/beauty · 210+ comments · 9 months ago" → blue title "What's a good everyday sunscreen for your face? : r/beauty" → body text → 2 voted answer cards inside ("Top answer · 70 votes" / "47 votes")
  - Below: list of 2 source post cards with timestamps, "More results from www.reddit.com" link, Consumer Reports card
  - Phone bottom nav same as left
- 2 annotation chips below the phone:
  - `AI synthesis visible above fold with citations`
  - `Source posts linked as cited references`

**Below both columns:** centered horizontal divider with `THRESHOLD` label centered on the divider line.

**Chrome:** none in body markup. The case-ai.html `<h2>Overview</h2>` provides the section heading.

**Implementation hint:** the existing `diagram-ai10-failure-state-v4.html` already does a similar BELOW/ABOVE threshold comparison and is the recommended structural base per v1 §4.2 — fork its CSS, replace the abstract content with the product-UI mocks above. Phone bezels can use `border-radius: 36px` + drop shadow + dashed border pattern matching ai20's phone-mock convention.

---

### §3.2 `diagram-ai-overview-v1-mobile.html` ← Figma `1207:5594` (375×1866)

**Visual:** same comparison as §3.1 but **vertically stacked** (BELOW on top, ABOVE below). Single column at 375 wide.

**Top section ("BELOW THRESHOLD"):**
- Pill label, phone mock (375 wide, full content visible), 2 annotation chips below — same content as §3.1 left column.

**Middle:** horizontal divider with `THRESHOLD` label.

**Bottom section ("ABOVE THRESHOLD"):**
- Pill label, phone mock (375 wide), 2 annotation chips below — same content as §3.1 right column.

**Chrome:** none. **Note:** there's a red annotation banner at the top of the Figma source frame ("MOVE ANNOTATIONS TO SEE LINKED CHANGES") — this is Della's working note, NOT content to embed. Skip it.

**Implementation hint:** structural base from `diagram-not03-full-inbox-redesign-v5.html` mobile per v1 §4.2 — fork its CSS, replace inbox content with the AI-page mocks.

---

### §3.3 `diagram-ai-ia-before-after-v1.html` ← Figma `1202:5101` (644×346)

**Visual:** 2-column comparison.

**Left column ("BEFORE"):**
- Eyebrow: `BEFORE` in muted small-caps
- 5 stacked thread cards (vertical, ~40px tall each, dim style):
  - r/headphones · Thread 1
  - r/headphones · Thread 2
  - r/BudgetAudio · Thread
  - r/gadgets · Thread
  - r/tech · Thread
- Each card: small dot/bullet glyph at left, then the label, then a horizontal hairline below.
- Caption below the stack: `Multiple threads compete for one search query` (dim muted text)

**Right column ("AFTER"):**
- Eyebrow: `AFTER`
- A single card stack representing one consolidated page:
  - Search query display: `best budget headphones` (with small magnifier glyph)
  - Divider with eyebrow `AI SUMMARY`
  - Divider with eyebrow `SOURCE THREADS`
  - 3 source-thread bullet rows:
    - r/headphones (red dot)
    - r/BudgetAudiophile (orange dot)
    - r/gadgets (red dot)
- Caption below: `One page answers the query with sourced AI summary` (in casual-tone)

**Chrome:** none. **From-scratch authorship** — no existing HTML to fork. Use the project's design tokens (`var(--surface-elevated)`, `var(--border-subtle)`, casual-tone accent for the AFTER caption) and 12px border-radius for the cards.

**Width target:** 644px — render natively at this width per the Figma frame.

---

### §3.4 `diagram-ai-identification-precedent-v1.html` ← Figma `1226:21284` (760×784)

**Visual:** mobile-mock-centric layout showing the inbox-redesign identification pattern applied to the Reddit Answers AI page.

**Top label:** small eyebrow `BEFORE — LEGACY INBOX` (red, casual-tone, centered above the mock).

> **Open question — §6.8:** the eyebrow says "BEFORE — LEGACY INBOX" but the visual is the AFTER state of Reddit Answers (showing the AI block with sparkle icon and citations). This appears to be Della using the inbox-redesign work as the precedent and the AI page as the application of the precedent. Della should confirm: keep the "BEFORE — LEGACY INBOX" label, change to "PRECEDENT — INBOX IDENTIFICATION PATTERN", or drop the label entirely? Recommend: change to a label that explains what the precedent IS, not "BEFORE."

**Phone mock (centered, ~380 wide, full bezel):**
- Status bar: `8:37` time, `◀ Slack` left indicator, signal/wifi/battery icons (battery showing `4`)
- Address bar: `reddit.com` with refresh and share icons
- Reddit toolbar: hamburger, Snoo logo, `Log In` orange button, cloud, search, more
- Page title: `Best Dewy Setting Spray` (dark heading)
- AI summary card (this is the precedent pattern):
  - Card with red border + sparkle icon + heading: `What people on Reddit think`
  - Subtext: `Generated from these links: [1][2][3][4][5]`
  - Body: `Here's a summary of popular opinions on the best dewy setting sprays based on Reddit discussions:`
  - Heading: `Highly Recommended Dewy Setting Sprays:`
  - 4 bulleted product callouts with bold names + descriptions:
    - **Urban Decay All Nighter Extra Glow**: Praised for its dewy finish.
    - **NYX Dewy Setting Spray**: A long-time favorite for its affordability and effectiveness, though it can be quite glowy if overused.
    - **Glow Recipe Watermelon Glow Mist**: Known for its refreshing feel and dewy finish.
    - **Rare Beauty Setting Spray**: Well-received...
  - `See more ⌄` link (blue)
  - Bottom row: `Is this summary helpful?` + ✓ `Helpful` and ✗ `Unhelpful` buttons
- Below the AI card: `Best Dewy Setting Spray posts` heading + caption "Reddit posts talking about Best Dewy Setting Spray used in the summary."
- Phone bottom nav: back, forward, +, tabs (showing `30`), more

**Chrome:** none in body markup. Implementation hint: fork from `diagram-not03-full-inbox-redesign-v5.html` desktop per v1 §4.2 — but this is a **mobile-style mock** rendered at desktop width (760), so the phone bezel + mobile UI sits centered with margin space on either side.

---

## §4 Diagram inventory (10 KEPT + 4 NEW + 13 retired iframe blocks)

### §4.1 KEPT (existing HTML — no authoring needed, just iframe references)

| ID | New v3 position | HTML file | Mobile node |
|---|---|---|---|
| ai09 | Pos 2 (Competing user needs) | `diagram-ai09-dual-user-framework-v4.html` | `989:8` |
| ai02a | Pos 3a (Proof of concept / research) | `diagram-ai02a-verticals-v4.html` | `972:8` |
| ai13 | Pos 4 (Establishing principles) | `diagram-ai13-transparency-framework-v4.html` | `950:8` |
| ai14 | Pos 5 (Identification UI) | `diagram-ai14-identification-explorations-v4.html` | `982:8` |
| ai20 | Pos 6 (UI to display source posts) | `diagram-ai20-threaded-posts-v4.html` | `983:8` (sync `1227:21658`/`1227:21731`) |
| ai25 | Pos 7b (voice) | `diagram-ai25-llm-identity-v4.html` | `956:8` |
| ai23 | Pos 7c (content) | `diagram-ai23-trust-comparison-v4.html` + `-mobile.html` | `776:8` |
| ai06 | Pos 8b (Generating summaries: XFN workflow) | `diagram-ai06-evaluation-matrix-v4.html` + `-mobile.html` | `774:8` |
| ai12 | Pos 8c (feedback loops) | `diagram-ai12-unified-feedback-v4.html` | `956:71` |
| ai10 | Pos 8d (failure states) | `diagram-ai10-failure-state-v4.html` + `-mobile.html` | `1046:8` |

### §4.2 NEW (4 diagrams to author or re-author)

| ID | Position | Source | New HTML file | Spec |
|---|---|---|---|---|
| Overview hero (desktop) | Pos 1 | Figma `1203:5207` | `diagram-ai-overview-v1.html` | §3.1 — re-author from scratch (current file is wrong) |
| Overview hero (mobile) | Pos 1 | Figma `1207:5594` | `diagram-ai-overview-v1-mobile.html` | §3.2 — re-author from scratch |
| IA before-after | Pos 3b | Figma `1202:5101` | `diagram-ai-ia-before-after-v1.html` | §3.3 — re-author from scratch |
| Identification precedent | Pos 5 | Figma `1226:21284` | `diagram-ai-identification-precedent-v1.html` | §3.4 — re-author from scratch |

> **Important:** the 4 files Window 1 already wrote in §6.2 commit `22dc749` are structurally wrong (chrome inside body + abstract content where Figma shows product-UI mocks). They need to be **rewritten**, not patched. Either: (a) delete the existing files and re-author, or (b) keep them on disk for reference and write fresh files (filenames stay the same since `case-ai.html` references will point to them).

### §4.3 RETIRED (iframe blocks removed from `case-ai.html`)

ai02b, ai05, ai07, ai08, ai11, ai15, ai16, ai17 (placeholder), ai18 (placeholder), ai19, ai21, ai22, ai24. HTML files stay on disk under `img/diagrams/` (not deleted) — same policy as v1 §4.3.

Plus 4 `img-placeholder` divs (Challenge opener, Solution × 2, Scalability "Component library", Content Attribution "Three attribution patterns"). All removed.

---

## §5 Code-level changes

§5.1, §5.2, §5.3, §5.4 from v1 outline are still correct. v2 doesn't change CSS or HTML patterns — only the prose-preservation discipline and the diagram visual specs.

**Critical reinforcement:** edits to `case-ai.html` are **surgical**. Open the file, apply the structural changes per v1 §5.1 in place, and PRESERVE every cited paragraph verbatim. Don't write a DRAFT-from-scratch file — that path produced the v1-DRAFT prose drift.

The only HTML pattern v2 adds beyond v1: each preserved paragraph keeps its exact `<strong>`, `<em>`, and entity escapes (`&amp;`, `&rarr;`, etc.) as they appear in the cited line. Don't normalize to ASCII or unicode without an explicit instruction.

---

## §6 Open questions — RESOLVED 2026-04-28 (all recommendations accepted)

| # | Question | Resolution |
|---|---|---|
| 6.1 | Pos 1 Overview prose | **A — reuse v2 line 76 verbatim as the Overview lede.** Place it directly under the H2, before the diagram pair. |
| 6.2 | Pos 4 Establishing principles bridge | **A — no bridge.** Section is H2 + line 146 verbatim + ai13 iframe. Sparse, voice-clean. Content-pass deferred. |
| 6.3 | Pos 5 identification-precedent bridge sentence | **A — no bridge.** ai14 iframe → line 300 → line 312 → new precedent diagram iframe directly. The iframe `title` attribute carries the meaning. Content-pass deferred. |
| 6.4 | Pos 8a Ensuring quality opener | **A — no opener.** Section is H2 + 3 H3 subsections, each with their own paragraphs. |
| 6.5 | Pos 3b line 120 verbatim vs. "IA decision" reword | **Verbatim.** Line 120 stays exactly as it appears in case-ai.html ("core design decision"). |
| 6.6 | Pos 7a Content opener | **A — line 406 verbatim.** Triple mismatch ("tone, clarity, narrator") accepted; readers won't trip on it. |
| 6.7 | Pos 8c ai12 placement after ai11 retired | **Confirmed: 244 → 256 → ai12 iframe.** ai12 closes the feedback-loops subsection. |
| 6.8 | §3.4 precedent diagram label | **B — change label.** Use `PRECEDENT — INBOX IDENTIFICATION PATTERN` (instead of "BEFORE — LEGACY INBOX"). Frames this as the precedent the AI page applies, not a before-state. |

All §6 answers are locked. Window 1 executes against this resolved spec.

---

## §7 Execution sequence (replaces v1 §6)

The §6 sequence in v1 outline (steps 1–11) is mostly correct, with two changes:

**Change 1: §6.2 (4 new diagrams) is REDONE, not skipped.** Window 1's current files in commit `22dc749` are wrong; they need to be rewritten per §3.1–§3.4 above. Author them BEFORE editing case-ai.html so the iframes resolve when the page loads.

**Change 2: §6.5 (case-ai.html restructure) is direct, not via DRAFT.** No `working/case-ai-v3-DRAFT.html` rehearsal. Open `case-ai.html`, apply the §5.1 structural edits + §2 prose preservation, save. The next gate is the voice-check + quality-check + screenshots run.

**Step list (committed sequentially):**

| Step | Action | Commit message |
|---|---|---|
| §6.1 | (already committed `5749d95`) | Branch + snapshots + planning docs |
| §6.2 | (already committed `22dc749`) — 4 new diagrams. **Will be superseded by §6.2-redo.** | (superseded) |
| §6.2a | (already committed `3567300`) | `.case-card-pair` CSS |
| §6.2-redo | Re-author 4 new diagrams per §3.1–§3.4. Author one at a time, screenshot to verify each matches Figma source. | `case-ai v3: §6.2-redo — 4 new diagrams rebuilt from Figma sources` |
| §6.3 | Push the 4 redone diagrams to Figma via `html-to-figma` skill (page 29:42, mobile cluster x=-420). | `case-ai v3: §6.3 — 4 new diagrams pushed to Figma` |
| §6.4 | Sync ai20 from Figma row 7 (`1227:21658` desktop + `1227:21731` mobile) via `figma-to-html`. Likely no-op. | `case-ai v3: §6.4 — sync ai20 from Figma row 7` (or skip if no diff) |
| §6.5 | Edit `case-ai.html` directly per §2 + v1 §5.1. Preserve every cited paragraph verbatim. No DRAFT file. | `case-ai v3: §6.5 — case-ai.html restructured` |
| §6.6 | Export any Figma row-1 product-UI PNGs Della confirms in §6.1 ship criteria (likely zero — diagrams carry the visuals). | `case-ai v3: §6.6 — product UI PNG exports` (or skip) |
| §6.7 | `python3 voice-check.py case-ai.html` | `case-ai v3: §6.7 — voice-check pass` |
| §6.8 | `python3 quality-check.py` | `case-ai v3: §6.8 — quality-check pass` |
| §6.9 | Screenshots at 1440 / 768 / 375 to confirm visual structure | `case-ai v3: §6.9 — visual regression screenshots` |
| §6.10 | `recruiter-panel` skill regression scoring | `case-ai v3: §6.10 — recruiter-panel regression` |
| §6.11 | Append to `BUILD-LOG.md` | `case-ai v3: §6.11 — BUILD-LOG entry` |

**Stash@{0}** still pending: handle mid-stream after §6.5, before §6.11. Run `git stash show -p stash@{0}`, inspect BUILD-LOG.md diff, apply or drop based on whether the entry belongs on case-ai-v3 or case-notifs.

---

## §8 What changed from v1 (summary for Della's review)

The v1 outline got the structural plan right (heading hierarchy, diagram inventory, retirements, card-pair pattern). It got two things wrong:

1. **No prose-preservation map.** v1 §3 captured PNG filenames and diagram node IDs but never extracted the v2 case-ai.html line citations. When Window 1 hit a section without source prose (Overview), it generated new prose. v2 §1 + §2 add the line citations.

2. **No diagram visual specs.** v1 §4.2 said "ADAPTED from ai10" or "fork from not03" but didn't describe what the new diagrams should LOOK like. Window 1 authored abstract diagrams. v2 §3.1–§3.4 describe each new diagram visually based on the Figma source frames.

v2 also adds §0 voice rule (verbatim, no invention) and reframes §6 to skip the DRAFT step (which was the affordance that let prose drift in unchecked).

The notifications v3 outline already worked this way. v2 brings case-ai up to that bar.

**Doc location:** `portfolio-site/working/planning-docs/case-ai-change-outline-v2.md`.
**Predecessor:** `case-ai-change-outline.md` (v1).
**Working artifact:** `outputs/klp-figma/figma-meta-klp.xml` (Figma metadata, 4448 lines).
