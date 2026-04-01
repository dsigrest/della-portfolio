# Portfolio UI & Tools Recommendation
## Della Sigrest — Senior Product Designer

**Research Date:** April 2026  
**Scope:** Visual quality improvements + AI-integrated design workflow tools

---

## PART 1: RECOMMENDED TOOLS FOR "PROMPT + CANVAS" WORKFLOW

### Top Recommendations (Ranked)

#### 1. **Google Stitch 2.0** — BEST FOR YOUR WORKFLOW
**Status:** Free, experimental (Google Labs)  
**Learning Curve:** Medium (easy for designers)  
**AI Connection:** Native Claude + other LLM integration via MCP server

**Why it's ideal for you:**
- **Infinite canvas** lets you combine design moodboards, competitor screenshots, code snippets, and UI components in one workspace
- **DESIGN.md export** creates plain-text design tokens (colors, typography, spacing) that Claude understands
- **MCP server** connects directly to Claude Code for seamless handoff — design in Stitch, refine with Claude
- **Two integration paths:** Export DESIGN.md for flexibility, or use MCP for real-time HTML/CSS/screenshot context
- **Zero cost** — perfect for portfolio iteration
- **Design agent** reasons across your full project history, building on previous iterations

**Setup:** Sign up at Google Labs, create project, export via DESIGN.md or use MCP credentials with Claude Code.

---

#### 2. **Cursor IDE with Visual Editor** — BEST FOR CODE-FIRST ITERATION
**Status:** Mature (v2.2 as of Dec 2025)  
**Learning Curve:** Medium-High (requires code comfort)  
**Cost:** Free or $20/month Pro

**Why consider it:**
- **Visual Editor** (new Dec 2025) lets you drag/drop HTML elements directly on the canvas while Cursor translates changes to code
- **Color pickers, typography sliders, grid manipulation** all update CSS live
- Integrated browser preview with live DOM editing
- Strong for designers who can read CSS
- Your site is already HTML/CSS/JS — Cursor understands this structure natively

**Workflow:** Open your portfolio in Cursor, click "Visual Editor," drag components, see CSS updates in real-time.

**Limitation:** Requires some code literacy; less forgiving for non-engineers than Stitch.

---

#### 3. **v0 by Vercel** — BEST FOR COMPONENT-LEVEL ITERATION
**Status:** Mature (recently moved to v0.app, Jan 2026)  
**Learning Curve:** Low (designer-friendly)  
**Cost:** Free tier exists; Premium $20/month with Figma uploads + API access  
**AI Connection:** Claude/GPT + design import capability

**Why it's valuable:**
- **Design-to-code:** Upload Figma designs or screenshots → v0 generates React/Tailwind components
- **Chat refinement:** Request changes via natural language; v0 updates with diffs
- **Instant preview:** See every iteration in real-time
- **Deploy anywhere:** Generated code exports to your own project
- **Shadcn/UI + Tailwind:** Production-ready patterns

**Best for:** Redesigning specific case card sections, hero, or CTA components. Not ideal for full-site iteration (React-only), but excellent for polish.

**Limitation:** Generates React, not vanilla HTML; requires webpack/build step for your current static site.

---

### Alternative Tools (Viable but Secondary)

| Tool | Best For | Limitations |
|------|----------|-------------|
| **Figma + Claude** | Design in Figma, generate code via Claude prompts | One-way workflow; less seamless than Stitch MCP |
| **Bolt.new** | Full-stack app building | Overkill for static portfolio; easier to drift from your existing code |
| **Lovable** | Full-stack + GitHub integration | Same scope issue; generates scaffolding you don't need |
| **Replit Agent** | Portfolio generation from scratch | Not for enhancing existing site; better for brand-new builds |
| **Claude Artifacts** | Quick HTML/CSS iteration | No visual canvas; code-only; limited design preview |

---

## PART 2: IMMEDIATE UI IMPROVEMENTS (CSS + STRUCTURE)

### DIAGNOSIS: Why It's "Falling Flat"

Your portfolio has **strong structure and solid dark-mode foundations**, but lacks:

1. **Visual hierarchy depth** — surfaces feel uniform; not enough contrast between primary/secondary content
2. **Breathing room** — dark mode sites need 20-30% more padding/margins than light mode (yours feels slightly cramped)
3. **Typographic variation** — size and weight hierarchy exists but could be more dramatic
4. **Accent color underuse** — teal (#2dd4bf) only appears on hover; could be bolder in key moments
5. **Layered depth** — surfaces lack shadow variation; everything lives at similar visual weight
6. **Motion subtlety** — animations exist but are minimal; could add more personality without being jarring

### High-Impact CSS Changes

#### 1. **Enhance Color Contrast (Accessibility + Clarity)**
**Change:** Replace secondary text grays with softer whites; add more depth layering

```css
:root {
  --text-secondary: #a0a0a0;  /* was #888 — brighter for readability */
  --text-tertiary:  #666;      /* was #555 — more visible */
  --surface-alt:    #0f0f0f;   /* new: darker alternate surface */
  --surface-bright: #1a1a1a;   /* new: brighter surface for emphasis */
}
```

**Impact:** Improves readability on dark backgrounds; adds micro-contrast layers.

---

#### 2. **Add Depth with Enhanced Shadows**
**Current:** Minimal box-shadows on hover. Surfaces feel flat.  
**Improvement:** Introduce shadow hierarchy for different interaction states

```css
:root {
  --shadow-sm:  0 2px 4px rgba(0,0,0,0.1);
  --shadow-md:  0 8px 16px rgba(0,0,0,0.15);
  --shadow-lg:  0 16px 32px rgba(0,0,0,0.2);
  --shadow-xl:  0 24px 48px rgba(0,0,0,0.25);
}

.case-card {
  box-shadow: var(--shadow-sm);
  transition: all var(--transition);
}

.case-card:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-4px);  /* slightly larger lift */
}
```

**Impact:** Cards feel more tactile; hover states are more rewarding.

---

#### 3. **Increase Padding/Margins for Dark Mode Breathing Room**
**Current:** `.case-card` content padding is `28px 32px`  
**Improvement:** Scale up by 25-30% to reduce visual density

```css
.case-card { /* was padding: 28px 32px; */ }
.case-content { 
  padding: 36px 40px;  /* +28% increase */
}

.case-body {
  padding: 80px var(--side-pad) 140px;  /* was 60px / 120px */
}

.pillar {
  padding: 48px 44px;  /* was 40px 36px */
}
```

**Impact:** Content feels less crowded; dark backgrounds need space to breathe.

---

#### 4. **Stronger Hero Typography Hierarchy**
**Current:** Hero h1 uses clamp(34px, 4.5vw, 52px) — solid but could be bolder  
**Improvement:** Increase max size + add weight variation

```css
.hero h1 {
  font-size: clamp(38px, 5vw, 56px);  /* was clamp(34px, 4.5vw, 52px) */
  font-weight: 700;
  letter-spacing: -0.04em;  /* slightly tighter for impact */
  line-height: 1.1;
}

.hero-sub {
  font-size: 18px;  /* was 17px */
  line-height: 1.8;  /* was 1.75 */
}
```

**Impact:** Hero section commands more attention; improved readability.

---

#### 5. **Accent Color as Visual Anchor**
**Current:** Teal only appears on hover. Feels hidden.  
**Improvement:** Use accent more intentionally in static contexts

```css
.case-title {
  font-size: 19px;
  font-weight: 600;
}

.case-tag {
  color: var(--accent);
  background: var(--accent-dim);  /* keep existing */
  border: 1px solid rgba(45, 212, 191, 0.2);  /* new: subtle border */
  font-weight: 700;  /* was 600 */
}

.hero-cta {
  background: transparent;  /* was no background */
  border: 1.5px solid var(--accent);  /* upgrade from border-hover */
  color: var(--accent);  /* was text-primary */
}

.hero-cta:hover {
  background: rgba(45, 212, 191, 0.08);
  border-color: var(--accent);
}
```

**Impact:** Accent color becomes more prominent; CTA stands out; brand identity strengthens.

---

#### 6. **Micro-spacing for Better Readability**
**Current:** Text margins are functional but utilitarian  
**Improvement:** Add calculated spacing between content blocks

```css
.case-body h2 {
  margin-top: 72px;  /* was 64px */
  margin-bottom: 24px;  /* was 20px */
  letter-spacing: -0.025em;
}

.case-body p {
  margin-bottom: 24px;  /* was 20px */
  line-height: 1.85;  /* was 1.8 */
}

.pillar h3 {
  margin-bottom: 12px;  /* was 8px */
  font-weight: 700;  /* increase from 600 */
}
```

**Impact:** Content feels more intentional; easier to scan.

---

#### 7. **Add Subtle Animations to Enhance Motion**
**Current:** Fade-in on scroll exists; hover states are minimal  
**Improvement:** Add entrance animations and micro-interactions

```css
.case-card {
  animation: cardEnter 0.5s ease-out forwards;
  animation-timeline: view();
  animation-range: entry 0% cover 25%;
}

@keyframes cardEnter {
  from {
    opacity: 0;
    transform: translateY(12px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.case-link {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.case-link::after {
  content: '';
  width: 4px;
  height: 1px;
  background: currentColor;
  transition: width var(--transition-fast);
}

.case-card:hover .case-link::after {
  width: 8px;
}
```

**Impact:** Page feels less static; interactions are discoverable through animation.

---

#### 8. **Refined Border & Divider Strategy**
**Current:** Borders are uniform #1e1e1e  
**Improvement:** Vary border opacity based on hierarchy

```css
:root {
  --border-soft:    rgba(255, 255, 255, 0.04);  /* new: subtle dividers */
  --border:         rgba(255, 255, 255, 0.08);  /* was #1e1e1e */
  --border-hover:   rgba(255, 255, 255, 0.12);
}

.case-card {
  border: 1px solid var(--border);
}

.case-meta-grid {
  border-top: 1px solid var(--border-soft);  /* was var(--border) */
  border-bottom: 1px solid var(--border-soft);
}
```

**Impact:** Borders feel less heavy; visual weight is better distributed.

---

### Summary of Implementation Priority

**TIER 1 (Highest Impact, 1-2 hours):**
- Adjust accent color prominence in CTA (#5)
- Increase padding on cards and sections (#3)
- Enhance color contrast for secondary text (#1)

**TIER 2 (Visual Polish, 2-3 hours):**
- Add shadow hierarchy (#2)
- Strengthen hero typography (#4)
- Refine spacing between text blocks (#6)

**TIER 3 (Delight, 1-2 hours):**
- Add scroll animations (#7)
- Refine border strategy (#8)

**Total estimated time:** 4-7 hours to implement all improvements.

---

## PART 3: RECOMMENDED WORKFLOW FOR MOVING FORWARD

### Week 1: Quick Wins with Cursor
1. Open portfolio in Cursor IDE + Visual Editor
2. Apply TIER 1 CSS improvements directly (no canvas needed; code-only)
3. Use Visual Editor to refine case card layouts, spacing, and CTA states
4. Deploy updated version to Vercel

### Week 2: Design System Layer with Stitch + Claude
1. Set up Google Stitch account (free)
2. Create a DESIGN.md file documenting your improved tokens:
   - Color palette (updated grays, accent usage)
   - Typography scale (hero, body, meta)
   - Spacing system (padding/margins)
   - Shadow hierarchy
3. Connect Stitch to Claude via MCP or export DESIGN.md
4. Use Stitch canvas to sketch component variations (hero treatments, card alternates)
5. Export changes via DESIGN.md, refine with Claude prompts, iterate in Cursor

### Week 3: Component Iteration with v0 (Optional)
1. If redesigning specific sections, upload a screenshot or Figma mockup to v0
2. Request UI variations with natural language
3. Export winning components, adapt to your HTML/CSS pattern
4. Test in Vercel deployment

### Ongoing: Maintenance
- Use Cursor's Visual Editor for quick tweaks
- Use Stitch for larger layout explorations
- Keep DESIGN.md updated as your system evolves

---

## FREQUENTLY ASKED QUESTIONS

**Q: Do I need to learn to code to use these tools?**  
A: No. Stitch is designed for designers and requires no coding. Cursor has a Visual Editor that's code-optional. v0 is also code-free.

**Q: Can I keep my existing HTML/CSS/JS?**  
A: Yes. Stitch and Cursor both work with existing codebases. v0 generates new components (React) that you'd adapt.

**Q: Will switching tools disrupt my current workflow?**  
A: No. Start with Cursor's Visual Editor (works with your current files) and add Stitch later for design explorations.

**Q: Which tool should I start with?**  
A: If you want immediate visual improvements: **Cursor Visual Editor**  
If you want to explore designs in a canvas: **Google Stitch**  
If you want to redesign specific components: **v0**

**Q: How much will this cost?**  
A: Nothing to start. Cursor has a free tier. Stitch is completely free. v0 offers a free tier (limited). Total spend to get started: $0.

---

## REFERENCES

- [Figma + Claude Code Integration (2025)](https://www.builder.io/blog/claude-code-to-figma)
- [v0 by Vercel Documentation](https://vercel.com/academy/ai-sdk/ui-with-v0)
- [Google Stitch 2.0 Canvas & MCP Integration](https://www.toolworthy.ai/tool/google-stitch-2-0)
- [Cursor Visual Editor Guide](https://cursor.com/blog/browser-visual-editor)
- [Dark Mode UI Best Practices 2025](https://www.graphiceagle.com/dark-mode-ui/)
- [Dark Mode Design Guide 2026](https://www.tech-rz.com/blog/dark-mode-design-best-practices-in-2026/)

---

**Document prepared:** April 1, 2026  
**Status:** Ready for implementation
