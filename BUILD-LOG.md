# AI-Collaborative Portfolio Build Log

**Project:** Portfolio website for Della Sigrest
**AI Tool:** Claude (Anthropic)
**Build started:** March 12, 2026

---

## Purpose of this log

This document tracks every significant decision, prompt, and iteration in building this portfolio site collaboratively with AI. The goal is transparency about what AI did well, where human judgment was essential, and what this process reveals about AI-native design workflows in 2026.

This log will become the basis for the "AI in My Practice" case study section of the portfolio itself.

---

## Session 1 — March 12, 2026

### Phase 1: Strategy & Planning

**What happened:**
- AI reviewed the full career materials packet (canonical narrative, proof bank, case study story spines, LinkedIn copy, resume system) to understand positioning
- AI researched current portfolio platform landscape (Framer vs Webflow vs Readymag vs static HTML)
- AI generated a comprehensive project plan including site architecture, page-by-page content guidance, case study template, visual direction, timeline, and competitive benchmarks

**Key decisions made by the human:**
- Decided to build the site *with* AI rather than solo in Framer — both for speed and as a meta case study
- Identified that the AI-build process itself would be portfolio content

**What AI did well:**
- Synthesized a large packet of career materials into a coherent site architecture in a single pass
- Generated a case study template grounded in industry standards (scrollable long-form, not slide deck)
- Identified the narrative arc across case studies (each proves a different value pillar)

**What required human judgment:**
- The decision to use the process itself as a case study (strategic framing)
- Whether to use a platform (Framer) vs static HTML (chose HTML for AI-forward signal + zero lock-in)

---

### Phase 2: Visual Direction

**What happened:**
- AI generated three complete visual style previews as HTML files:
  - Option A: Dark Minimal — quiet, spacious, indigo accent
  - Option B: Light Clean — structured, editorial, black/white
  - Option C: Bold Editorial — high contrast, orange accent, Space Grotesk, big numbers
- Each preview used real positioning copy and case study content

**Key decision made by the human:**
- Selected Option B's layout (structured cards, 2-column pillar grid, eyebrow + CTA hero) with Option A's dark color palette
- Vetoed purple as accent color
- Selected Vercel for deployment (signal alignment with target companies)

**What AI did well:**
- Generated three distinct, production-quality visual directions in minutes
- Used real content so the human could evaluate tone, not just aesthetics
- Each direction had internally consistent design logic (type scale, spacing, color relationships)

**What required human judgment:**
- Mixing layout from one option with color from another (cross-pollination)
- The purple veto (taste/brand preference)
- Deployment platform choice (career signal reasoning)

---

### Phase 3: Site Build — Foundation

**What happened:**
- AI built the core site structure: shared CSS, index page, about page, first case study (Notifications & Inbox)
- Design system tokens established: teal accent (#2dd4bf), dark surface palette, Inter typeface, consistent spacing/radius
- Responsive grid implemented (desktop, tablet, mobile breakpoints)
- Scroll-triggered fade-in animations added
- Case study template established with: hero, meta grid, section headings, metric callout cards, image placeholders, next-case-study navigation

**Architecture:**
```
portfolio-site/
├── index.html          (home: hero + pillars + case study cards)
├── about.html          (narrative + links)
├── case-notifications.html  (case study 1 — full)
├── styles.css          (shared design system)
└── BUILD-LOG.md        (this file)
```

**Content decisions:**
- Case study copy written from the career materials proof bank, not invented
- Metrics cited only where explicitly documented in source materials
- Image placeholders marked with descriptive labels for what should go there
- Footer includes "This site was designed collaboratively with AI" with link to this log

**Pending:**
- [x] Case study 2: Keyword Landing Pages / AI
- [x] Case study 3: Sharing & Embeds
- [x] Case study 4: Subreddit Success
- [x] Actual screenshots / diagrams to replace placeholders
- [ ] Resume PDF download
- [ ] Custom domain setup
- [ ] Vercel deployment
- [ ] Mobile QA pass
- [ ] Copy editing pass

---

### Phase 4: All Case Studies + Image Integration

**What happened:**
- All four case studies written and structured: Notifications & Inbox, KLP/AI, Sharing & Embeds, Subreddit Success
- AI scanned ~600 screenshots across Apple Photos to identify the 30 most relevant images for the four case studies
- Images classified using a visual pattern criteria doc (ui-reddit, slack, slides-data, personal) to ensure only portfolio-relevant screenshots were selected
- 4 custom SVG diagrams created to match the site's dark design system — these visualize strategic frameworks that had no screenshot equivalent:
  - **Inbox 2.0 Strategy Framework**: 5-cohort × 3-pillar matrix with priority heat map
  - **Sharing Flywheel**: circular Share→Preview→Visit→Engage cycle with 3-stage annotations
  - **3-Layer AI Content Governance**: stacked trust layers (Visual ID, Tone/Voice, Prompt Design)
  - **Community Lifecycle Framework**: 5 stages with drop-off percentages and funnel bar
- All placeholder `[bracketed description]` divs replaced with actual `<img>` tags across all 4 case study files
- Image layouts use responsive CSS Grid (2-column and 3-column grids depending on content type)

**Image selection per case study:**
- **Notifications** (9 images + 1 SVG): wireframe exploration, Figma base design, variant explorations (×2), live UI, analytics dashboard
- **KLP/AI** (5 images + 1 SVG): KLP product UI (×3), strategy slides (×2)
- **Sharing** (6 images + 1 SVG): share UI variations across the share flow
- **Subreddit** (4 images + 1 SVG): creation form, filled form, growth tools, mod tools

**Key decisions made by the human:**
- "Just pick the best ones" — delegated screenshot curation to AI
- Confirmed SVG diagram creation for missing strategic framework visuals

**What AI did well:**
- Image curation at scale: scanned hundreds of screenshots and selected contextually relevant ones
- Created SVG diagrams that are visually consistent with the site's design system (same bg color, teal accent, Inter font, border-radius)
- Matched images to narrative beats within each case study

**What required human judgment:**
- Whether the selected images accurately represent the work (pending review)
- Whether SVG diagrams faithfully capture the strategic frameworks (pending review)
- Visual density: how many images per section feels right vs. overwhelming

---

## Patterns observed so far

### Where AI accelerates
1. **Content synthesis → structure**: Turning a messy packet of career materials into a coherent site architecture
2. **Style exploration**: Generating multiple distinct visual directions in parallel, with real content
3. **Boilerplate elimination**: CSS resets, responsive grids, animation observers, nav toggles — all generated correctly on first pass
4. **Consistent voice**: Maintaining the same tone and positioning language across multiple pages

### Where human judgment is essential
1. **Taste decisions**: Color vetoes, layout mixing, what "feels right"
2. **Strategic framing**: Deciding the build process is itself a case study
3. **Career signal reasoning**: Choosing Vercel over Netlify for audience perception
4. **Content accuracy**: Verifying metrics and claims against source materials
5. **What to leave out**: Knowing that CPO vision work should be a sidebar, not a case study

### Open questions
- How much process detail should each case study include? (Current draft leans toward strategic framing over process documentation)
- Should the "AI in My Practice" section be a standalone page or a blog-style post?
- How to handle confidential work visuals (redacted screenshots vs. abstract diagrams vs. skip entirely)
