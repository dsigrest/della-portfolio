# Portfolio Site Upgrade — Development Plan

**Status:** Ready for implementation  
**Date:** March 31, 2026  
**Target Launch:** Q2 2026  
**Maintainer:** Della Sigrest

---

## Executive Summary

This plan addresses gaps identified by a **6-company recruiter panel** (Anthropic, Ramp, Meta, Figma, OpenAI, Cursor) scored against real job postings, and transforms the portfolio from a clean but incomplete showcase into a targeted, AI-forward narrative that closes specific hiring gates at each target company.

**Current scores (sourced from real JDs):** Figma 8.5, OpenAI 8.0, Meta 7.5, Cursor 7.5, Anthropic 7.0, Ramp 7.0 — avg 7.6/10.
**Projected after plan execution:** avg 8.3–8.8/10 — with specific hard-requirement gaps closed.

**Key wins:**
- Resume link functional and prominent
- AI collaboration case study proving design-with-AI practice end-to-end (closes Ramp hard req, Meta preferred, Anthropic implicit)
- Code prototyping evidence made visible (closes Anthropic hard req)
- Developer/tool/platform language added to case studies (closes Cursor min qual, Figma tool perspective gap)
- Concrete mentorship examples surfaced (closes Meta IC6 path gap)
- Stronger "first designer" positioning per case study
- Enhanced visual distinctiveness (stronger teal presence, micro-interactions, subtle texture)
- Thought leadership integration (closes OpenAI, Figma, Meta gaps)
- Mobile QA pass

**Critical insight from recruiter panel:** Most gaps are *communication gaps* (things Della does but doesn't mention), not capability gaps. This portfolio is the ideal vehicle to close them — the build process itself is evidence of AI workflow usage and code prototyping.

**Why now:** Resume and LinkedIn have been revved (v4 and v14 respectively). Portfolio needs to catch up and become the artifact-backed proof layer that closes company-specific hiring gates the text-only materials can't address alone.

---

## Recruiter Panel Integration (6-Company JD-Sourced Requirements)

**Source:** `deliverables/recruiter-panel-sourced-evaluation.md` (v2, March 31, 2026)
**Method:** Scored against real job postings via LinkedIn scraper + career pages + Blind culture data
**Baseline:** Average 7.6/10 (down from 8.5 vibes-based — more honest, more actionable)

### Gap → Portfolio Action Map

| Gap (from sourced eval) | Companies Affected | Plan Task | Expected Score Impact |
|---|---|---|---|
| No evidence of AI tools in personal design workflow | Ramp (HARD REQ), Meta (preferred), Anthropic (implicit) | **Phase 2.1** — AI case study explicitly shows Claude/Cursor in design process | +1.0–1.5 for Ramp; +0.5 for Meta |
| No code-based prototyping evidence | Anthropic (REQUIRED) | **NEW Phase 2.5** — Add HTML/CSS/JS prototyping callout across materials | +0.5–1.0 for Anthropic |
| No portfolio links or case studies viewable | OpenAI, Cursor, Figma | **This portfolio IS the fix** — ensure it's linked from LinkedIn/resume | +0.5 across all three |
| No public thought leadership | OpenAI, Figma, Meta | **Phase 5.1** — Link published article; **Phase 2.1** — portfolio itself as thought leadership artifact | +0.5–1.0 for OpenAI, Figma |
| No developer tools / technical product framing | Cursor (MIN QUAL), Anthropic | **NEW Phase 2.6** — Reframe prompt design workflow as internal tooling; add developer language | +0.5–1.0 for Cursor |
| No tool/platform design perspective | Figma | **NEW Phase 2.6** — Add tool affordance language to case studies | +0.5 for Figma |
| Mentorship evidence thin | Meta (IC6 path), OpenAI | **Phase 2.2** — About page expansion with concrete mentorship examples | +0.5 for Meta |
| Safety/trust as conviction vs. constraint | Anthropic | **Phase 2.1 + 2.3** — Frame trust principles as personal philosophy, not just Reddit requirement | +0.5 for Anthropic |

### Critical Insight: Communication Gaps, Not Capability Gaps

The sourced evaluation's key finding is that most gaps are things Della likely *does* but doesn't *mention*. This portfolio is the ideal vehicle to close them:

1. **"I use Claude for research synthesis and Cursor for prototyping"** — The portfolio build process itself IS the evidence. Phase 2.1 makes this explicit.
2. **Code prototyping** — This portfolio is built in HTML/CSS/JS. That's the proof. Phase 2.5 makes this visible.
3. **Developer tooling framing** — Reddit's prompt design system IS internal developer tooling. Phase 2.6 reframes this.

### Projected Score Impact (if all phases complete)

| Company | Current (Sourced) | Projected After Portfolio | Key Unlocks |
|---|---|---|---|
| Meta | 7.5 | 8.5–9.0 | Mentorship examples + AI workflow evidence + portfolio links |
| Figma | 8.5 | 9.0 | Tool/platform language + thought leadership + portfolio craft |
| OpenAI | 8.0 | 8.5–9.0 | Thought leadership + portfolio links + AI case study |
| Cursor | 7.5 | 8.0–8.5 | Developer framing + AI/LLM depth + shipping velocity evidence |
| Anthropic | 7.0 | 7.5–8.0 | Code prototyping evidence + trust philosophy + AI workflow |
| Ramp | 7.0 | 8.0–8.5 | AI workflow evidence (Claude/Cursor) + portfolio links |

---

## Phase 1: Critical Fixes & Mobile QA (Priority: CRITICAL)
**Goal:** Unblock deployment and ensure mobile usability  
**Estimated Effort:** M (3-4 days)  
**Dependencies:** None

### Tasks

#### 1.1 Fix Resume Link
- **Task:** Replace `href="#"` with functional download link in navigation
- **Acceptance Criteria:**
  - Resume link in `<nav>` (line 19 index.html) no longer has `href="#"`
  - Link href points to EITHER: `/resume.pdf` (if hosted on same domain) OR external URL (Google Drive, Dropbox, etc.)
  - **DECISION REQUIRED BEFORE TASK START:** User must specify resume PDF location (path or URL)
  - Link opens in new tab (`target="_blank"`) if external URL
  - Link has accessible aria-label (e.g., `aria-label="Download my resume"`)
  - Works on all pages (nav is shared): index.html, about.html, case-notifications.html, case-ai.html, case-sharing.html, case-subreddit.html
  - **PRE-FLIGHT CHECK:** Resume PDF exists at specified path/URL and is accessible before pushing to production
- **Files Affected:** `index.html`, `about.html`, `case-notifications.html`, `case-ai.html`, `case-sharing.html`, `case-subreddit.html`
- **Complexity:** S
- **Blocker:** Cannot complete this task without explicit resume PDF path/URL from user. Add this information to the deployment checklist.

#### 1.2 Verify & Standardize Placeholder Images
- **Task:** Audit all case study HTML for consistent image placeholder implementation (NOTE: `.img-placeholder` class already exists in codebase)
- **Acceptance Criteria:**
  - **CRITICAL:** Use EXISTING `.img-placeholder` and `.img-placeholder-grid` classes (defined in styles.css), NOT new `.placeholder-image` class
  - All `<img>` tags in case studies are replaced with descriptive placeholder divs using `.img-placeholder` class
  - Placeholder HTML structure (already in use): `<div class="img-placeholder">Descriptive text: [What image shows]</div>`
  - For grouped images: Use `.img-placeholder-grid` with `.cols-2` or `.cols-3` class
  - Labels are specific and descriptive (e.g., "Inbox wireframe exploration — pending review" or "UI variant comparison")
  - Verify all case study files follow this pattern:
    - `case-notifications.html` (DONE: already uses `.img-placeholder`)
    - `case-ai.html` (audit & fix if needed)
    - `case-sharing.html` (audit & fix if needed)
    - `case-subreddit.html` (audit & fix if needed)
    - `case-building-portfolio.html` (new; must use `.img-placeholder` pattern)
  - Index.html case cards (numbered 01-04) have STATIC number display; no image placeholders needed here
  - Verify CSS for `.img-placeholder` styling: min-height 240px, centered text, gray background, works at all viewport sizes
- **Files Affected:** 
  - `case-ai.html` (audit & standardize)
  - `case-sharing.html` (audit & standardize)
  - `case-subreddit.html` (audit & standardize)
  - `case-building-portfolio.html` (new; use pattern from case-notifications.html)
  - `styles.css` (verify; no changes needed if current `.img-placeholder` styling is sufficient)
- **Complexity:** M
- **IMPORTANT:** Do NOT create a new `.placeholder-image` class. Reuse `.img-placeholder` throughout.

#### 1.3 Mobile QA Pass
- **Task:** Responsive testing and fixes for tablets (768px) and mobile (375px-480px)
- **Acceptance Criteria:**
  - Navigation hamburger menu functions correctly on mobile
  - Hero section text is readable, no overflow
  - Case study cards stack properly on mobile
  - Image placeholders scale without distortion
  - Footer content is accessible on mobile (links clickable, no tiny text)
  - Touch targets minimum 48x48px
  - No horizontal scroll on any viewport
  - Breakpoints working correctly (check `@media (max-width: 768px)` and `@media (max-width: 480px)` in styles.css)
- **Files Affected:** `styles.css` (may need adjustments)
- **Complexity:** M
- **Testing:** Use Chrome DevTools responsive mode or physical devices

#### 1.4 AI Collaboration Mention — Decide & Act
- **Task:** Current footer mentions "Designed with AI collaboration" but lacks context. Choose one:
  - **Option A (Recommended):** Create dedicated case study `case-building-portfolio.html` to prove the practice
  - **Option B:** Expand inline in footer with link to thought leadership post
  - **Option C:** Remove if not defensible with artifacts
- **Acceptance Criteria:**
  - Decision documented in commit message
  - If Option A: new page created (see Phase 2)
  - If Option B: footer text updated with thoughtful explanation and link
  - If Option C: footer cleaned up
- **Files Affected:** `index.html`, possibly `case-building-portfolio.html` (new)
- **Complexity:** S (decision) to M (if creating case study)
- **Recommendation:** Proceed to Phase 2 assuming Option A (dedicated case study)

---

## Phase 2: New Content & AI Positioning (Priority: HIGH)
**Goal:** Create AI narrative proof point and strengthen staff-level signals  
**Estimated Effort:** L (5-6 days)  
**Dependencies:** Phase 1 complete; Task 2.1 must complete BEFORE task 2.2 (About page needs links to new case study)

### Tasks

#### 2.1 Create "Building This Portfolio" / "AI in My Practice" Case Study
- **File:** `case-building-portfolio.html` (new; case 05 of 05)
- **Acceptance Criteria:**
  - Follows existing case study template structure from `case-notifications.html` (copy as template)
  - Clear section breakdown:
    - **Header eyebrow:** "Case Study 05 — Design Practice & Tooling"
    - **H1 title:** "Building This Portfolio" or "Designing with AI"
    - **Hero statement (subtitle):** Frames portfolio redesign as intentional proof point for "designing with AI end-to-end"
    - **Meta grid:** Role (Senior Product Designer), Timeline (2026), Platform (Web/Static)
    - **The Brief section:** Challenges with hiring narrative; goal to prove "designing with AI end-to-end"
    - **Approach section:** How AI is being used in practice (iterative feedback loops, prompt iteration examples, artifact generation, review/governance)
    - **Process Visual:** Use `.img-placeholder` for governance model or workflow diagram
    - **Example Prompts section:** 3-5 sanitized, specific prompts (not generic placeholders)
    - **Governance Model section:** Clear explanation of: how work is reviewed, where AI ends and human judgment begins
    - **Outcome section:** Metrics (design velocity, iteration cycles); link to thought leadership post (if published) or placeholder
    - **Learnings section:** Candid reflection on what AI enables vs. what requires human judgment
  - **Thought Leadership Link Decision (BLOCKER):** Before completion, confirm: Is the AI thought leadership post published?
    - IF YES: Add link to post in Outcome section
    - IF NO: Add placeholder text: "[Thought leadership post coming — publication date TBD]"
  - Consistent styling with other case studies (reuse `.case-hero`, `.case-body`, `.metrics-row` classes)
  - All internal links tested (link back to index.html, navigation works)
- **Files Affected:** 
  - Create: `case-building-portfolio.html` (new; copy structure from case-notifications.html)
  - Update: `index.html` (add 5th case card + update case count in nav/breadcrumbs)
  - Update: All existing case study files (case-notifications.html, case-ai.html, case-sharing.html, case-subreddit.html) to show "Case XX/05" instead of "/04"
  - Update: `styles.css` (no changes needed if existing classes work)
- **Complexity:** L
- **CRITICAL:** Update case study eyebrows in ALL case files after this task:
  - `case-notifications.html`: Change "Case Study 01" to "Case Study 01 of 05" (or add breadcrumb "Case 01/05")
  - `case-ai.html`: "Case 02/05"
  - `case-sharing.html`: "Case 03/05"
  - `case-subreddit.html`: "Case 04/05"
  - `case-building-portfolio.html`: "Case 05/05"

#### 2.2 Expand About Page with Design Philosophy & Staff Signals
- **Task:** Deepen About page (about.html) to answer "Why this role? Why now?" and surface leadership credentials
- **Acceptance Criteria:**
  - **DEPENDENCY:** Cannot start until task 2.1 completes (About page must link to new case study)
  - New "Design Philosophy" or "Approach" section added
    - Covers: process philosophy, values, how you think about product
    - 150-200 words
  - Staff-level signals clearly surfaced:
    - Mentoring/leadership of designers (if applicable)
    - Hiring/interviewing contributions (if applicable)
    - Cross-functional influence (examples of how you shaped org direction)
    - Technical depth (tools expertise, systems thinking)
  - "Currently Exploring" section added:
    - AI in practice (LINK to case-building-portfolio.html from task 2.1)
    - Personal practice (prints/making if applicable)
    - Skill development areas
  - "Why This Role? Why Now?" answer woven throughout or as dedicated section:
    - Context on next chapter, what you're looking for
    - Why now is the right time to move roles
  - Tone: Candid, thoughtful, authentic (not corporate/marketing-speak)
  - Length: ~800-1000 words total (expanded from current)
  - All links tested: case-building-portfolio.html link works, all internal links functional
- **Current About.html Structure:** (from inspection)
  - Hero section with intro
  - Paragraph sections
  - Footer
- **Target Structure:**
  - Hero section (keep as is)
  - **Career narrative + staff signals (expand existing)**
  - **New: Design Philosophy section**
  - **New: Currently Exploring section (link to case-building-portfolio.html)**
  - **New: Why This Role / Next Chapter (woven throughout or separate)**
  - Links section (existing)
  - Footer (keep as is)
- **Files Affected:** `about.html`
- **Complexity:** M
- **Content Source:** Synthesize from resume, LinkedIn, thought leadership drafts, existing case studies
- **QA:** Peer review for authenticity (ask hiring reviewer: "Does this voice sound like you? Is the positioning credible?")

#### 2.3 Deepen AI Case Study with Technical Specifics
- **File:** `case-ai.html` (expand existing)
- **Acceptance Criteria:**
  - Add "Technical Approach" subsection:
    - System architecture or workflow diagram [PLACEHOLDER]
    - Data model or decision tree visual [PLACEHOLDER]
    - Example screenshots of AI-assisted workflows (or descriptive placeholders)
  - Add "Prompt Examples" section:
    - 3-5 actual prompts used (sanitized for confidentiality)
    - Show iteration/refinement process
    - Annotate what worked and what didn't
  - Add "Governance Model" visual or written explanation:
    - How cross-functional team reviewed AI recommendations
    - Where human judgment overrode AI
    - Decision gates and approval workflows
  - Add "Metrics" or "Outcomes" with specifics:
    - User satisfaction improvements (if available)
    - Feature adoption rates
    - Business impact (revenue, engagement, retention)
    - Design velocity improvements
  - Maintain current narrative but expand depth
- **Files Affected:** `case-ai.html`
- **Complexity:** M
- **Content Source:** Work with stakeholders to extract sanitized examples and metrics

#### 2.4 Surface "First Designer" Context in Each Case Study Header
- **Task:** Add contextual positioning in case study headers emphasizing leadership/ownership role
- **Acceptance Criteria:**
  - **AUDIT REQUIREMENT:** Before adding any "first designer" claims, verify against LinkedIn/resume that the claim is factually accurate
  - Each case study header now includes role context via eyebrow text:
    - "Notifications" → "First designer on Notifications systems"
    - "AI" → "Pioneered AI-forward design practice at Reddit"
    - "Sharing" → "Led design for sharing & embeds infrastructure"
    - "Subreddit" → "First designer to own full community redesign"
    - "Building Portfolio" → "Designed this portfolio collaboratively with AI"
  - Positioning: Consistent placement in eyebrow/header (e.g., `<div class="case-hero-eyebrow">First designer on...</div>`)
  - Current structure in case-notifications.html: `<div class="case-hero-eyebrow">Case Study 01 &mdash; Systems Thinking</div>`
  - **Option A (Recommended):** Expand eyebrow: `<div class="case-hero-eyebrow">Case Study 01 of 05 — First designer on Notifications systems</div>`
  - **Option B (Alternative):** Keep existing eyebrow structure; add new subtitle: `<p class="case-role">Led design as first designer on this initiative</p>`
  - Conveys: You were early, took on ambiguity, shaped direction
  - **VERIFY:** If any claim is uncertain or overstated, use softer language: "Led design on" instead of "First designer on"
  - All case study files updated consistently (tone, phrasing, placement)
- **Files Affected:** 
  - `case-notifications.html`
  - `case-ai.html`
  - `case-sharing.html`
  - `case-subreddit.html`
  - `case-building-portfolio.html` (new)
- **Complexity:** S
- **CSS Changes:** Minimal (eyebrow styling likely already exists)
- **QA:** Peer review: Ask hiring manager "Are these 'first designer' claims credible given my actual role/timeline?"

#### 2.5 Surface Code Prototyping Evidence (Closes Anthropic Hard Requirement)
- **Task:** Make visible that Della prototypes in HTML/CSS/JS — not just Figma
- **Why:** Anthropic's JD explicitly requires "Proven ability to prototype rapidly with front-end code (HTML/CSS/JS)." Current materials list "Rapid Prototyping" but reference only Figma. This portfolio is *built in HTML/CSS/JS* — that's the proof, but it needs to be called out.
- **Acceptance Criteria:**
  - **In case-building-portfolio.html (Phase 2.1):** Technical approach section explicitly states: "Built in HTML/CSS/JS — no frameworks, no templates. Every line reviewed and iterated on."
  - **In about.html:** Skills or philosophy section mentions code prototyping: "I prototype in both Figma and code (HTML/CSS/JS) depending on fidelity needs."
  - **In case-ai.html:** If applicable, mention any code-based prototyping done for Reddit AI features
  - **In footer or meta:** Consider adding "View source" link or GitHub link (if repo is public) as implicit proof of code comfort
  - **Tone:** Matter-of-fact, not defensive. Don't oversell coding skills — frame as "comfortable prototyping in code" not "full-stack developer"
- **Files Affected:** `case-building-portfolio.html`, `about.html`, possibly `case-ai.html`
- **Complexity:** S
- **Target Companies:** Anthropic (closes REQUIRED gap), Cursor (supports dev-adjacent positioning)

#### 2.6 Add Developer/Technical Product & Tool/Platform Framing (Closes Cursor + Figma Gaps)
- **Task:** Reframe existing work using language that resonates with developer tools and platform/tool companies
- **Why:** Cursor requires dev tools experience (MIN QUAL). Figma needs tool/platform design perspective. Della has adjacent experience that can be reframed:
  - Reddit's prompt design system = internal developer tooling
  - Notifications architecture = platform-level systems design
  - IoT work at Touchwood = technical product design
- **Acceptance Criteria:**
  - **In case-ai.html:** Add a "Technical Context" callout: "The prompt design system I built functioned as internal developer tooling — standardizing how product teams interfaced with LLM capabilities across Reddit's platform."
  - **In case-notifications.html:** Frame the 5-archetype framework using platform/systems language: "Designing the notification system required platform-level thinking — creating abstractions that scaled across Reddit's entire product surface."
  - **In about.html:** Add a line about technical product comfort: "I'm drawn to technically complex products — whether that's AI systems, developer tools, or platform infrastructure."
  - **Optional:** In case-subreddit.html, reference IoT/Touchwood experience briefly using technical product language if space allows
  - **Tone:** Authentic bridge-building, not keyword stuffing. Show genuine interest in technical products.
- **Files Affected:** `case-ai.html`, `case-notifications.html`, `about.html`, possibly `case-subreddit.html`
- **Complexity:** S-M
- **Target Companies:** Cursor (addresses MIN QUAL gap), Figma (addresses tool/platform perspective gap), Anthropic (supports enterprise/dev tools narrative)

---

## Phase 3: Aesthetic & Brand Distinctiveness (Priority: HIGH)
**Goal:** Move from "clean but derivative" to visually distinctive with AI-forward personality  
**Estimated Effort:** M (3-4 days)  
**Dependencies:** Phase 1 complete; Phase 2 optional but recommended

### Tasks

#### 3.1 Strengthen Teal Accent Presence
- **Task:** Increase visual prominence of primary accent color (#2dd4bf) without oversaturation
- **Acceptance Criteria:**
  - **Teal left border (4px) added to:**
    - Blockquotes and pull quotes in case studies (add rule: `.case-body blockquote { border-left: 4px solid var(--accent); padding-left: 1rem; }`)
    - Key insight callouts or emphasized text (if any exist)
    - "Currently Exploring" section in About (if added; use `.section-highlight` or similar class)
    - "Design Philosophy" section in About (similar treatment)
  - **Teal underline/color for links:**
    - Navigation active state: Already present (`.nav-links a.active::after`)
    - Case study links on hover: Update `.case-link` to show teal color on hover (already implemented)
    - Prose links in case-body: Add subtle teal underline on hover (use `a:hover { text-decoration: underline; text-decoration-color: var(--accent); }`)
  - **Teal accent on interactive elements:**
    - Button/CTA hover states: Case-study "Next" link already changes on hover; verify with `.case-next a:hover { color: var(--accent); }`
    - Case card hover: Verify `.case-card:hover .case-num { color: var(--accent); }` is working
    - Case card top border on hover: Verify `.case-card:hover { border-top-color: var(--accent); }` (currently shows `.case-card:hover { border-color: var(--border-hover); }`)
    - Progress indicator (new): If adding "Case 01/05" text, use teal for the number accent
  - **Saturation audit:** Count visual instances of teal; should not exceed 20-25% of viewport visual weight. Test by: screenshot page, measure teal pixels vs. total.
  - **Contrast verification:** Teal (#2dd4bf) on dark background (#0b0b0b): measure contrast ratio >= 4.5:1 (use WebAIM contrast checker)
- **Specific CSS Changes Needed:**
  ```css
  /* Add to styles.css: Case body blockquote */
  .case-body blockquote {
    border-left: 4px solid var(--accent);
    padding-left: 1rem;
  }
  
  /* Verify/update case card hover to include top border color */
  .case-card:hover {
    border-color: var(--border-hover);
    border-top-color: var(--accent); /* Add this line if missing */
  }
  
  /* Add prose link underline on hover */
  .case-body a:hover {
    text-decoration: underline;
    text-decoration-color: var(--accent);
  }
  ```
- **Files Affected:** `styles.css`
- **Complexity:** S
- **Testing:** Open each case study page; hover over links, case cards; verify teal appears appropriately. Screenshot and compare before/after saturation.

#### 3.2 Add Subtle Background Texture or Gradient
- **Task:** Enhance visual richness without distraction
- **Acceptance Criteria:**
  - Subtle texture OR gradient applied to:
    - Body background (very light, high opacity)
    - Section backgrounds (minimal contrast)
  - Effect: "Barely there" but adds polish
  - No impact on readability
  - Options:
    - Option A: Radial gradient (teal center, fading out)
    - Option B: Subtle noise texture (SVG or CSS)
    - Option C: Wavy background pattern on hero (CSS clip-path)
  - Recommend: Radial gradient from teal (5% opacity) fading to transparent over full viewport
- **Example CSS:**
  ```css
  body {
    background: 
      radial-gradient(circle at 20% 50%, rgba(45, 212, 191, 0.03), transparent 50%),
      linear-gradient(180deg, var(--bg) 0%, var(--bg) 100%);
  }
  ```
- **Files Affected:** `styles.css`
- **Complexity:** S

#### 3.3 Enhance Case Card Hover Interactions
- **Task:** Improve tactile feedback and visual interest on case study cards
- **Acceptance Criteria:**
  - Current hover state (if any) enhanced:
    - Add subtle scale effect (1.02x)
    - Add shadow elevation
    - Add border-top color shift to teal
    - Smooth transition (0.3s ease)
  - Example state chain:
    ```css
    .case-card {
      transition: all 0.3s ease;
      border-top: 3px solid transparent;
    }
    
    .case-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
      border-top-color: var(--accent);
    }
    ```
  - Apply on index.html case cards
- **Files Affected:** `styles.css`
- **Complexity:** S

#### 3.4 Add Micro-interactions (Link Underlines, Smoother Transitions)
- **Task:** Enhance interactive elements with subtle, polished feedback
- **Acceptance Criteria:**
  - Link interactions:
    - Underline appears on hover (teal, animated)
    - Visited state (slightly muted text)
    - Active state (solid underline)
  - Button interactions:
    - Smooth color transition on hover
    - Slight scale or shadow on active
  - Text transitions:
    - Smooth color changes (0.2s ease)
    - No jarring repaints
  - Form inputs:
    - Smooth focus state with teal border
    - Placeholder text fades smoothly
  - Global transition timing: Use CSS custom property `--transition: 0.3s ease`
- **Files Affected:** `styles.css`
- **Complexity:** S
- **Note:** Keep animations lightweight (no more than 0.3s for interactions)

#### 3.5 Add Case Study Progress Indicator / Breadcrumbs
- **Task:** Show position in case study sequence (01/04 or breadcrumbs)
- **Acceptance Criteria:**
  - Progress indicator added to all case study pages
  - Format options:
    - Option A (recommended): "Case Study 01/05" in header
    - Option B: Breadcrumb nav (Home > Work > Case Name > Section)
    - Option C: Progress bar at top of page
  - Implementation:
    - Static number in HTML (update when new cases added)
    - Consistent placement (top of main content, under nav)
    - Styling: Small text, subtle color (#999 or dim teal)
  - If breadcrumbs: Make all links functional
- **Files Affected:** All `case-*.html` files
- **Complexity:** S

---

## Phase 4: Advanced Interactions & Scroll Effects (Priority: MEDIUM)
**Goal:** Add polished, modern interaction paradigm; improve perceived performance  
**Estimated Effort:** L (4-5 days)  
**Dependencies:** Phase 1 complete; Phases 2-3 recommended first

### Tasks

#### 4.1 Implement View Transitions API for Page Navigation
- **Task:** Add smooth page transitions without page load flicker
- **Decision Required:** Inline scripts in each HTML file OR external shared JS file?
- **Acceptance Criteria:**
  - View Transitions API enabled for all page-to-page navigation (internal links only; external links exempt)
  - Smooth fade/slide between pages (no white flash on navigation)
  - Works on all navigation links (nav menu, case cards, breadcrumbs, "Next case" links)
  - Graceful fallback for unsupported browsers (site navigates normally, just no transition)
  - **Script placement decision:**
    - **OPTION A (Recommended for maintainability):** Create external `/scripts/navigation.js` file, link from `<head>` in all pages
    - **OPTION B (Current pattern):** Add inline `<script>` block to each HTML file (matches current codebase style)
  - Implementation checks:
    - Only transitions internal navigation links (links without `target="_blank"` or `target="_self"`)
    - Non-blocking: If browser doesn't support View Transitions API, site still navigates (no errors)
    - Test on: Chrome 111+, Edge 111+, Firefox (no API; fallback to standard nav), Safari (no API; fallback)
  - Example implementation (if using Option A external script):
    ```javascript
    // /scripts/navigation.js
    if (document.startViewTransition) {
      document.addEventListener('click', (e) => {
        const link = e.target.closest('a[href]');
        if (link && !link.target && link.href.startsWith(window.location.origin)) {
          e.preventDefault();
          document.startViewTransition(() => {
            window.location = link.href;
          });
        }
      });
    }
    ```
  - If Option A: Add to `<head>` of all pages: `<script src="/scripts/navigation.js" defer></script>`
  - If Option B: Add inline script (as shown above) to each HTML page before `</body>`
- **Files Affected:** 
  - Create: `/scripts/navigation.js` (if Option A) OR no new file (if Option B)
  - Update: `index.html`, `about.html`, `case-notifications.html`, `case-ai.html`, `case-sharing.html`, `case-subreddit.html`, `case-building-portfolio.html` (add script or reference)
  - Optional: `styles.css` (no changes needed unless adding view-transition-name)
- **Complexity:** M
- **Browser Support:** Chrome 111+, Edge 111+, graceful fallback for others (tested in DevTools)
- **Testing:** Test on each case study page; navigate via nav links, case cards, next-case links; verify smooth transition or standard nav if unsupported

#### 4.2 CSS Scroll-Driven Animations for Progressive Reveals
- **Task:** Add lightweight scroll-synced animations to case study sections for engagement (Chrome 115+)
- **Acceptance Criteria:**
  - **Fallback strategy defined FIRST:** Use CSS `@supports (animation-timeline: view())` to check browser support; if unsupported, elements display normally (not hidden)
  - Scroll-driven animations applied to SELECT elements only (not global):
    - Case study h2 headings (fade in as scroll down): `.case-body h2 { opacity: 0; animation: fadeIn 0.8s ease forwards; animation-timeline: view(); animation-range: entry 0% cover 30%; }`
    - Metric callout boxes (fade + slide in): `.metric { opacity: 0; animation: slideInUp 0.8s ease forwards; animation-timeline: view(); animation-range: entry 0% cover 30%; }`
    - Image placeholders (subtle fade): `.img-placeholder { opacity: 0; animation: fadeIn 0.6s ease forwards; animation-timeline: view(); animation-range: entry 0% cover 20%; }`
  - **Base state (no animation support):** All elements have `opacity: 1; transform: none;` in base CSS; animations are enhancement only
  - Keyframes defined:
    ```css
    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }
    
    @keyframes slideInUp {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }
    ```
  - Timing: Use `0.6s - 0.8s ease` for all scroll animations (consistent across site)
  - Apply selectively: Max 3-5 elements per page (headers, metrics, key images); don't animate everything
- **Files Affected:** `styles.css`, case study pages (no HTML changes needed)
- **Complexity:** M
- **Browser Support:** Chrome 115+, Edge 115+, Firefox (no support; elements visible as normal), Safari (no support; fallback)
- **Testing:** Test on Chrome DevTools with animation-timeline support; verify elements are visible in Firefox/Safari without animations; no console errors
- **Performance:** Verify Lighthouse score remains > 90 after adding animations; scroll performance smooth on throttled devices

#### 4.3 GSAP Integration for Complex Scroll Sequences (OPTIONAL — Conditional)
- **Task:** Evaluate and conditionally add GSAP library for hero or process flow animations
- **DECISION GATE (Before task start):**
  - This task is OPTIONAL and depends on Phase 3 completion
  - After Phase 3 is complete, run Vercel Speed Insights audit:
    - IF Lighthouse score >= 90 AND total JS bundle < 40KB: PROCEED with GSAP
    - IF Lighthouse score < 90 OR total JS bundle >= 40KB: SKIP this task entirely
  - Document decision in commit message: "Phase 4.3 decision: [PROCEED / SKIPPED] based on [Lighthouse score / bundle size]"
- **Acceptance Criteria (if proceeding):**
  - GSAP library added (23KB minified; via CDN with integrity check recommended)
  - Used for 1 complex sequence ONLY (not multiple; not every element):
    - Option A: Hero section parallax or staggered text reveal (index.html)
    - Option B: Case study "Approach" section process flow animation (one case study)
  - Implementation example:
    ```javascript
    // Load GSAP from CDN
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <script>
      gsap.registerPlugin(ScrollTrigger);
      gsap.to(".case-step", {
        scrollTrigger: {
          trigger: ".case-process",
          start: "top center",
          end: "bottom center",
          scrub: 1
        },
        x: 0,
        opacity: 1,
        stagger: 0.2
      });
    </script>
    ```
  - Smooth performance: Test on throttled 4G (Chrome DevTools) and low-end device; verify 60fps or close to it
  - Graceful degradation: If JS disabled, page still functions and displays content (elements visible without animation)
  - Post-implementation Lighthouse: Run audit again; score must remain >= 90
- **Files Affected:** 
  - `index.html` or case study (add GSAP script tag + animation script)
  - `styles.css` (no changes; animations driven by GSAP, not CSS)
- **Complexity:** L
- **Risk:** If Lighthouse score drops below 90 or performance feels janky, remove GSAP entirely and rely on Phase 4.2 CSS animations
- **Bundle:** Add via CDN with integrity attribute: `<script src="..." integrity="sha384-..."></script>`

---

## Phase 5: Content Alignment & Thought Leadership (Priority: MEDIUM)
**Goal:** Align portfolio narrative across resume, LinkedIn, and portfolio; integrate thought leadership  
**Estimated Effort:** M (2-3 days)  
**Dependencies:** Phases 1-2 recommended first

### Tasks

#### 5.1 Link Thought Leadership / Writing
- **Task:** Surface external thought leadership from portfolio (BLOCKED pending content publication)
- **Acceptance Criteria:**
  - **BLOCKER STATUS CHECK:** Before starting, confirm: Is the AI thought leadership post published?
    - IF YES: Proceed with linking
    - IF NO: Create placeholder text and defer linking until post is published
  - Thought leadership post (if published) linked from:
    - About page (in "Currently Exploring" or "Writing" section)
    - AI case study (case-ai.html: link in Outcomes section)
    - Footer link in index.html (currently points to "#"; update to actual post URL)
  - Link formatting requirements:
    - Link text is descriptive and specific (not generic "Read more"; e.g., "Read my thoughts on AI governance in design")
    - Opens in new tab (`target="_blank"`)
    - Include short pull quote or summary (1-2 sentences max) above/near link explaining the post
  - If post NOT yet published:
    - Add placeholder text in About page: "[Thought leadership post on AI in design practice — coming soon]"
    - Update footer link in index.html to: "This site was designed collaboratively with AI — [coming soon]"
    - Document in commit: "Thought leadership links deferred; post not yet published"
  - Example (if published):
    ```html
    <section class="writing">
      <h2>Thinking on Product & Design</h2>
      <article>
        <h3>Designing with AI End-to-End</h3>
        <p>Reflections on integrating AI into design practice, governance, and what it means for senior designers.</p>
        <a href="[url]" target="_blank">Read on [Publication] →</a>
      </article>
    </section>
    ```
- **Files Affected:** `about.html`, possibly `case-ai.html`
- **Complexity:** S

#### 5.2 Verify Metrics & Narrative Alignment
- **Task:** Audit resume, LinkedIn, and portfolio for consistency and accuracy before launch
- **Acceptance Criteria:**
  - **METRICS VERIFICATION:** Create audit checklist (before committing changes):
    - [ ] Team sizes managed: Resume value = LinkedIn value = Portfolio case studies (if mentioned)
    - [ ] User/DAU impacted: Values match across platforms (e.g., "+1.4% New user DAU" consistent)
    - [ ] Business outcomes: Revenue, engagement, retention claims verified against case study context; no inflation
    - [ ] Timelines: Project dates match across resume, LinkedIn, and portfolio case studies
    - [ ] Role titles: Verify portfolio context aligns with resume titles and LinkedIn headline
    - **Resolution:** For any discrepancies found, document in task comments which version is authoritative; update all platforms to match
  - **NARRATIVE CONSISTENCY VERIFICATION:**
    - "First designer" story: Present in About page and at least one case study (case-notifications.html, case-sharing.html, or case-subreddit.html)
    - "AI end-to-end" claim: Backed by case-ai.html case study (including process, decisions, outcomes) OR linked thought leadership post
    - "Prints/personal practice" (if claimed): Evidence in About section or dedicated case study
    - Staff-level signals: Mentoring/hiring/influence signals present in About + case studies; aligned with 12+ year claim in resume
    - Tone audit: Read through About, all case studies, and landing copy; flag and remove corporate jargon (e.g., "synergize", "leverage", "streamline"); ensure tone is conversational and authentic
  - **CONTRADICTION CHECK:**
    - No conflicting dates (e.g., case study timeline vs. resume employment dates)
    - No conflicting role descriptions (e.g., "lead designer" vs. "individual contributor" for same project)
    - No mismatched metrics (e.g., "managed team of 8" on portfolio but "managed team of 6" on resume)
  - **QA SIGN-OFF:** 
    - Print or screen-capture resume, LinkedIn profile, and portfolio pages showing metrics
    - Create comparison document (Google Doc or Markdown table) showing all metrics side-by-side with verification status
    - Attach to PR or commit as evidence of audit completion
- **Files Affected:** None (audit only; may inform edits in Phases 2-5; findings documented in PR/commit)
- **Complexity:** S
- **Deliverable:** Completed audit checklist + comparison document in PR description or commit message; no metrics discrepancies outstanding at merge

#### 5.3 Add "Now" / "Currently Exploring" Section
- **Task:** Surface current work and interests in portfolio to demonstrate active learning and forward momentum
- **Acceptance Criteria:**
  - New section added to `about.html` (placed after "About" or "Background" section, before "Thought Leadership" if present)
  - **Section structure requirements:**
    - Heading: "Currently Exploring" or "Now" (use semantic <h2>)
    - List format: Unordered list (<ul>) or prose paragraphs (not bullet points in design; choose one consistently)
    - 4-6 items covering:
      - Current role search status (e.g., "Seeking Staff Designer or Head of Design role at product companies leveraging AI")
      - Active explorations specific to portfolio narrative (e.g., "Designing with AI end-to-end in product practice")
      - Skill development focus (e.g., "Building design systems for emerging AI features")
      - Mentoring/leadership (e.g., "Mentoring junior designers on AI literacy and design governance")
      - Writing/thought leadership (e.g., "Writing about AI and design governance" — link if post published)
      - Personal practice or projects (if applicable)
  - **Tone requirements:** Fresh, authentic, forward-looking; no corporate jargon; reads like genuine reflection, not marketing copy
  - **Visual treatment:**
    - Matches portfolio design system (teal accent color #2dd4bf if highlighting links)
    - Responsive on mobile (list items stack naturally)
    - Optional: Subtle background color or left border to visually distinguish from body text
  - **Maintenance plan:** Add comment in HTML noting section should be updated quarterly or when status changes
  - **Link integration:** Link to thought leadership post (from 5.1) if published; use descriptive link text
  - **Example structure (prose version):**
    ```html
    <section class="now">
      <h2>Currently Exploring</h2>
      <p>
        I'm actively seeking a Staff Designer or Head of Design role at product companies where I can apply my experience building design systems and leading design in AI-forward practices. My focus right now includes designing with AI end-to-end in product practice, building scalable design systems for emerging AI features, and mentoring junior designers on AI literacy and design governance. I'm also writing about these practices and their implications for design leadership.
      </p>
    </section>
    ```
- **Files Affected:** `about.html`
- **Complexity:** S
- **QA Checklist:**
  - [ ] Section renders correctly on desktop (1200px+), tablet (768px), and mobile (480px)
  - [ ] Links (if any) are underlined and open in new tab where appropriate
  - [ ] Tone audit: Read aloud; confirm it sounds genuine and not like marketing copy
  - [ ] Narrative consistency: At least 3 items link back to portfolio case studies or thought leadership

---

## Technical Architecture Decisions

### Library & Tool Stack

| Tool | Purpose | Size | Rationale | Implementation |
|------|---------|------|-----------|-----------------|
| **View Transitions API** | Page navigation smoothness | Native | Modern, no bundle cost; graceful fallback | Phase 4.1 |
| **CSS Scroll-Driven Animations** | Progressive reveals | Native | CSS-only, performant; no JS overhead | Phase 4.2 |
| **GSAP** (optional) | Complex scroll sequences | 23KB gzipped | Industry standard for scroll effects; only if Phase 3+ are successful | Phase 4.3; optional |
| **No framework** | Site structure | N/A | Static HTML/CSS/JS; full control, no vendor lock-in; appropriate for portfolio scope | Ongoing |

### CSS Custom Properties & Variables

Current (maintain):
```css
--accent: #2dd4bf;        /* Teal */
--bg: #0f172a;            /* Dark navy (dark mode) */
--text: #f1f5f9;          /* Light text */
--text-muted: #94a3b8;    /* Muted text */
--border: #1e293b;        /* Subtle borders */
--transition: 0.3s ease;  /* Standard animation timing */
```

New (add):
```css
--accent-muted: rgba(45, 212, 191, 0.2);  /* Teal with opacity for subtle effects */
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
--radius: 8px;  /* Border radius standard */
```

### File Structure (After All Phases)

```
portfolio-site/
├── index.html                          (updated)
├── about.html                          (expanded)
├── case-notifications.html             (updated: first designer context)
├── case-ai.html                        (expanded: technical depth)
├── case-sharing.html                   (updated: first designer context)
├── case-subreddit.html                 (updated: first designer context)
├── case-building-portfolio.html        (new: AI practice case study)
├── styles.css                          (enhanced: teal, interactions, scroll)
├── img/                                (directory for final images)
├── resume.pdf                          (user-provided; linked from nav)
└── DEVELOPMENT-PLAN.md                 (this file)
```

### Performance Targets

- **Largest Contentful Paint (LCP):** < 2.5s
- **First Input Delay (FID):** < 100ms
- **Cumulative Layout Shift (CLS):** < 0.1
- **Total Bundle:** < 100KB (HTML + CSS + JS; no external libraries except optional GSAP)
- **Mobile rendering:** No jank on scroll animations (60fps target)

---

## New Pages & Sections: Content Outlines

### case-building-portfolio.html

**Purpose:** Prove AI-forward design practice; transparency on process  
**Audience:** Recruiters, hiring managers, other designers curious about AI workflow  
**Tone:** Candid, thoughtful, slightly meta (designing the portfolio design)

**Structure:**
```
[HEADER]
Title: "Building This Portfolio"
Subtitle: "Designing with AI: Process, Governance, and Learning"
Hero image placeholder: [Workflow diagram or process visual]

[SECTION 1: THE BRIEF]
Challenge: Hiring narrative gap—claiming "AI end-to-end" without proof
Goal: Create defensible, artifact-backed case study on using AI in design practice
Context: Previous portfolio didn't address how AI shapes modern design

[SECTION 2: THE APPROACH]
Subsection A: Iterative Workflow
- Use AI for: brainstorming, structure, content synthesis, iteration
- Human review gates: strategy, final direction, tone, narrative arc
- Workflow diagram (placeholder)

Subsection B: Governance Model
- How does cross-functional review work with AI?
- Where AI recommends, human decides
- Decision framework diagram (placeholder)

[SECTION 3: EXAMPLE PROMPTS]
Show 3-5 sanitized prompts used in process:
1. Initial narrative synthesis prompt
2. Case study structure brainstorm
3. About page philosophy section
4. Design system documentation
5. Headline variation generation

Annotations: What worked, what needed iteration, where human judgment overrode AI

[SECTION 4: OUTCOME]
- Clearer storytelling (faster iteration on narrative)
- More intentional design (explicit governance gates)
- Broader design practice (AI as amplifier, not replacement)
- Artifacts: This portfolio, thought leadership post, design documentation

[SECTION 5: LEARNINGS]
- Where AI excels: brainstorm, structure, iteration, variation
- Where AI fails: original insight, final judgment calls, brand voice decisions
- Confidence: High on scaffolding, medium on originality, low on strategy

[CTA]
Link to thought leadership post or contact for deeper discussion
```

### about.html — Expanded Sections

**New "Design Philosophy" Section**
```
Heading: "How I Approach Design"

Content outline:
- Start with the problem, not the solution
- Push for clarity before moving fast
- Design systems are power multipliers
- First designers own more than design
- Technology should amplify, not replace, human judgment

Tone: Candid, values-driven, slightly provocative
Length: 300-400 words
```

**New "Currently Exploring" Section**
```
Heading: "Currently Exploring"

Bullet points:
- AI in product design: governance, workflow, ethics
- Design systems and design ops at scale
- Teaching and mentoring designers on AI literacy
- Intersection of design, strategy, and business impact
- Personal practice: prints, visual experiments
- Writing on design practice and leadership

Tone: Future-focused, authentic
Updates: Quarterly or as work evolves
```

**Expanded "Why This Role?" Section**
```
Content outline (woven into narrative, not separate section):
- What attracts to next role (autonomy, scale, craft, team)
- What you're solving for (leadership scope, craft ownership, impact)
- Why now (market moment, personal readiness, skill gaps to close)
- What you bring (first designer expertise, AI acumen, people leadership)
- What you want to learn (broader org strategy, executive presence, new domain)

Tone: Thoughtful, not sales-y
Length: 400-500 words across existing sections
```

**Staff-Level Signals Integrated Throughout**
```
Examples to weave in:
- "I've hired and mentored X designers who have gone on to..."
- "Led design direction across X-person org; influenced product strategy through..."
- "Built design system used by X teams across X orgs"
- "Represented design in executive conversations on strategy and roadmap"
- "Owned hiring and interviewing for design; shaped design culture through..."

Placement: Sprinkle through narrative, not as separate list
```

---

## CSS/Design System Upgrades

### Comprehensive styles.css Enhancements

#### 1. Root CSS Variables (add to `:root` selector)

```css
:root {
  /* Existing */
  --accent: #2dd4bf;
  --bg: #0f172a;
  --text: #f1f5f9;
  --text-muted: #94a3b8;
  --border: #1e293b;
  
  /* NEW */
  --accent-muted: rgba(45, 212, 191, 0.2);
  --accent-dim: rgba(45, 212, 191, 0.1);
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
  --radius: 8px;
  --transition: 0.3s ease;
  --transition-fast: 0.2s ease;
}
```

#### 2. Background Enhancement

```css
body {
  background: 
    radial-gradient(circle at 20% 50%, var(--accent-dim), transparent 50%),
    linear-gradient(180deg, var(--bg) 0%, var(--bg) 100%);
}
```

#### 3. Link Styling (new/enhanced)

```css
a {
  color: var(--text);
  text-decoration: none;
  position: relative;
  transition: color var(--transition);
}

a::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 2px;
  background: var(--accent);
  opacity: 0;
  transition: opacity var(--transition);
}

a:hover {
  color: var(--accent);
}

a:hover::after {
  opacity: 1;
}

a:visited {
  color: var(--text-muted);
}
```

#### 4. Blockquote / Callout Styling (new)

```css
blockquote {
  border-left: 4px solid var(--accent);
  padding-left: 1rem;
  margin-left: 0;
  color: var(--text-muted);
  font-style: italic;
}

.callout,
.insight {
  border-left: 4px solid var(--accent);
  padding-left: 1rem;
  background: var(--accent-dim);
  padding: 1rem;
  border-radius: var(--radius);
  margin: 1rem 0;
}
```

#### 5. Case Card Enhancement (new)

```css
.case-card {
  transition: all var(--transition);
  border-top: 3px solid transparent;
  border-radius: var(--radius);
}

.case-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
  border-top-color: var(--accent);
}
```

#### 6. Button Styling (enhanced)

```css
button, a.button {
  transition: all var(--transition);
  border-radius: var(--radius);
}

button:hover, a.button:hover {
  background: var(--accent);
  color: var(--bg);
  box-shadow: var(--shadow-md);
}
```

#### 7. Form Input Styling (new)

```css
input, textarea {
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--bg);
  color: var(--text);
  transition: border-color var(--transition), box-shadow var(--transition);
}

input:focus, textarea:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 3px var(--accent-dim);
}

input::placeholder {
  color: var(--text-muted);
  transition: opacity var(--transition);
}

input:focus::placeholder {
  opacity: 0.5;
}
```

#### 8. Placeholder Image Styling (new)

```css
.placeholder-image {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 300px;
  background: var(--border);
  border-radius: var(--radius);
  margin: 1.5rem 0;
  color: var(--text-muted);
  font-size: 0.875rem;
  text-align: center;
  padding: 2rem;
  border: 1px dashed var(--accent-muted);
}

.placeholder-image p {
  margin: 0;
}
```

#### 9. Progress / Breadcrumb Styling (new)

```css
.progress-indicator {
  font-size: 0.875rem;
  color: var(--text-muted);
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.progress-indicator .current {
  color: var(--accent);
  font-weight: 600;
}

nav.breadcrumb {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 2rem;
  font-size: 0.875rem;
}

nav.breadcrumb a {
  color: var(--text-muted);
}

nav.breadcrumb a:hover {
  color: var(--accent);
}

nav.breadcrumb span {
  color: var(--text-muted);
}

nav.breadcrumb span:last-child {
  color: var(--text);
}
```

#### 10. Scroll-Driven Animation Setup (new)

```css
.fade-in-on-scroll {
  animation: fadeIn 0.8s ease forwards;
  animation-timeline: view();
  animation-range: entry 0% cover 30%;
}

.slide-in-on-scroll {
  animation: slideInUp 0.8s ease forwards;
  animation-timeline: view();
  animation-range: entry 0% cover 30%;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}
```

#### 11. Typography Enhancements (refined)

```css
h1, h2, h3 {
  transition: color var(--transition);
}

h1 {
  font-size: 2.5rem;
  line-height: 1.2;
  margin-bottom: 1rem;
}

h2 {
  font-size: 1.875rem;
  margin-top: 2rem;
  margin-bottom: 1rem;
}

h3 {
  font-size: 1.25rem;
  margin-top: 1.5rem;
  margin-bottom: 0.75rem;
}

p {
  line-height: 1.75;
  margin-bottom: 1rem;
}
```

#### 12. Mobile Responsive Updates (enhanced)

```css
@media (max-width: 768px) {
  h1 {
    font-size: 2rem;
  }
  
  h2 {
    font-size: 1.5rem;
  }
  
  .case-grid {
    grid-template-columns: 1fr;
  }
  
  nav.breadcrumb {
    flex-wrap: wrap;
  }
}

@media (max-width: 480px) {
  h1 {
    font-size: 1.5rem;
  }
  
  h2 {
    font-size: 1.25rem;
  }
  
  h3 {
    font-size: 1rem;
  }
  
  .placeholder-image {
    min-height: 200px;
    padding: 1rem;
  }
}
```

---

## Accessibility & Performance Checklist

### Accessibility (WCAG 2.1 AA)

**INTEGRATION:** These requirements are embedded in task acceptance criteria below. All tasks must pass these checks before merge.

- [ ] All images have alt text or descriptive labels (`.img-placeholder` divs have aria-label or adjacent text describing image intent)
  - **Assigned to:** Task 1.2 (Image Placeholder Audit), Task 2.1 (AI Case Study), Task 2.2 (About Page)
- [ ] Color contrast ratio >= 4.5:1 for normal text, >= 3:1 for large text (verify teal #2dd4bf meets requirements)
  - **Assigned to:** Task 3.1 (Teal Accent), Task 3.4 (Micro-interactions); QA: run Lighthouse audit
- [ ] Navigation keyboard-accessible (tab order logical, no keyboard traps; resume link is keyboard-focusable)
  - **Assigned to:** Task 1.1 (Resume Link); QA: test Tab key navigation on all pages
- [ ] Focus indicators visible (outline or underline on links/buttons; not hidden by CSS)
  - **Assigned to:** Task 3.4 (Micro-interactions); QA: Tab through navigation and links; verify outline/underline visible
- [ ] Links have descriptive text (not generic "Click here"; e.g., "Resume" not "Link"; "Read my thoughts on AI governance" not "Read more")
  - **Assigned to:** Task 5.1 (Link Thought Leadership), Task 5.3 (Currently Exploring); QA: audit all link text in PR
- [ ] Page structure semantic (proper heading hierarchy, h1 → h2 → h3; no skipped levels)
  - **Assigned to:** All content tasks; QA: run axe DevTools or WAVE audit; check headings.txt or use headingsMap plugin
- [ ] Motion/animations respect `prefers-reduced-motion` media query (View Transitions, scroll animations conditionally apply)
  - **Assigned to:** Task 4.1 (View Transitions API), Task 4.2 (Scroll-Driven Animations); QA: test with DevTools emulation of reduced motion
- [ ] Mobile touch targets minimum 48x48px (nav links, buttons, case card clickable area)
  - **Assigned to:** Task 1.3 (Mobile QA), Task 3.4 (Micro-interactions); QA: measure with DevTools or manual testing
- [ ] No auto-playing media or infinite scroll (static portfolio, no video autoplay)
  - **Assigned to:** All tasks; QA: verify no <video autoplay> or infinite scroll implementation

### Performance (Lighthouse > 90; Core Web Vitals: LCP < 2.5s, FID < 100ms, CLS < 0.1)

**INTEGRATION:** These requirements are embedded in task acceptance criteria below. All tasks must pass these checks before merge.

- [ ] Total CSS bundle < 50KB (maintain lean stylesheet; Phase 3 enhancements should not inflate)
  - **Assigned to:** Task 3.1-3.5 (Aesthetic enhancements); QA: run `gzip < styles.css | wc -c` to verify
- [ ] Total JS bundle < 50KB excluding optional GSAP (keep baseline small)
  - **Assigned to:** Task 4.1-4.3 (Interactions); QA: measure script bundle size before and after
- [ ] Images optimized (placeholders are lightweight; final images compressed)
  - **Assigned to:** Task 1.2 (Placeholder audit), Task 2.1+ (final images); QA: verify WebP or optimized JPEG < 200KB per image
- [ ] No render-blocking resources (CSS/JS defer or inline critical styles)
  - **Assigned to:** Task 1.1+ (all tasks); QA: check Lighthouse audit; verify <link rel="stylesheet"> not blocking
- [ ] Largest Contentful Paint (LCP) < 2.5s (hero image or text is LCP; ensure fast load)
  - **Assigned to:** Task 1.2 (Placeholder sizing), Task 4.1+ (avoid layout shifts); QA: run Lighthouse on mobile throttled network
- [ ] First Input Delay (FID) < 100ms (no JS blocking user interaction)
  - **Assigned to:** Task 4.1+ (interactions); QA: test button/link clicks and nav responsiveness on slow mobile
- [ ] Cumulative Layout Shift (CLS) < 0.1 (no surprise layout jumps; stable placeholder sizes)
  - **Assigned to:** Task 1.2 (Placeholder consistency), Task 3.4 (Micro-interactions); QA: verify no jank during scroll or interaction
- [ ] Core Web Vitals pass (via Lighthouse audit and manual testing on mobile)
  - **Assigned to:** All tasks; QA: run Lighthouse > 90 on all pages (Performance, Accessibility, Best Practices, SEO)
- [ ] No console errors or warnings (clean build; no deprecated APIs)
  - **Assigned to:** All tasks; QA: DevTools console clear during full page load and interaction

### SEO

- [ ] `<title>` is unique and descriptive on each page
- [ ] `<meta name="description">` present on each page
- [ ] Open Graph meta tags (og:title, og:description, og:image)
- [ ] Twitter Card meta tags (if sharing on Twitter)
- [ ] Structured data (JSON-LD) for organization/person schema
- [ ] XML sitemap generated
- [ ] robots.txt present (allow crawl)
- [ ] Canonical tags if cross-domain duplication

### Best Practices

- [ ] No mixed content (all assets HTTPS)
- [ ] Cookies/localStorage used minimally
- [ ] No third-party trackers (privacy-respecting)
- [ ] Mobile-friendly (responsive design verified)
- [ ] Dark mode support verified
- [ ] Print stylesheet functional (readable on paper)

---

## QA Plan by Phase

### Phase 1: Critical Fixes & Mobile QA

**1.1 Resume Link**
- [ ] Verify link is not `href="#"`
- [ ] Test on all pages (index, about, each case study)
- [ ] Verify opens in new tab or downloads
- [ ] Test on mobile, tablet, desktop
- [ ] Accessibility: link is keyboard-accessible

**1.2 Image Placeholders**
- [ ] All `<img>` tags replaced with `.placeholder-image` divs
- [ ] Labels are descriptive and match final intent
- [ ] Placeholders scale without distortion at 375px, 768px, 1920px widths
- [ ] No layout shifts when images loaded (placeholder size consistent)
- [ ] Styling visible (gray background, centered text, readable)

**1.3 Mobile QA**
- Devices tested:
  - [ ] iPhone SE (375px)
  - [ ] iPad Air (768px)
  - [ ] Desktop (1920px)
  - [ ] Chrome DevTools responsive mode (multiple widths)
- Elements verified:
  - [ ] Navigation hamburger works (if applicable)
  - [ ] Hero section readable, no overflow
  - [ ] Case cards stack properly on mobile
  - [ ] Footer accessible on mobile (clickable links, readable text)
  - [ ] No horizontal scroll
  - [ ] Touch targets >= 48px

**1.4 AI Collaboration Decision**
- [ ] Decision documented in commit
- [ ] If new case study: structure matches other cases
- [ ] If footer update: text is clear and truthful
- [ ] If removal: footer makes sense without it

### Phase 2: New Content & AI Positioning

**2.1 AI Case Study (`case-building-portfolio.html`)**
- [ ] Page exists and is accessible from index
- [ ] All sections present (brief, approach, examples, governance, outcome, learnings)
- [ ] Example prompts are sanitized and credible
- [ ] Governance model is clear (human + AI roles)
- [ ] Links to thought leadership work (or placeholder for future)
- [ ] Styling matches other case studies
- [ ] Links back to index work main page
- [ ] Progress indicator shows "5/5" or updated count

**2.2 About Page Expansion**
- [ ] New "Design Philosophy" section added and reads well
- [ ] Staff-level signals integrated naturally (not a separate list)
- [ ] "Currently Exploring" section present and up-to-date
- [ ] "Why This Role?" answer woven in (3-5 sentences)
- [ ] Total length ~800-1000 words (not overly long)
- [ ] Tone is candid and authentic
- [ ] Grammar and spelling checked

**2.3 AI Case Study Depth**
- [ ] Technical approach section added
- [ ] 3-5 example prompts included
- [ ] Governance model explained or visualized
- [ ] Metrics/outcomes specific and credible
- [ ] Word count increased ~30-50% from original
- [ ] Readability maintained

**2.4 "First Designer" Context**
- [ ] Each case study header includes first designer callout
- [ ] Phrasing is consistent across all cases
- [ ] Styling is subtle but prominent (not overwhelming)
- [ ] Links or structure unaffected

### Phase 3: Aesthetic & Brand Distinctiveness

**3.1 Teal Accent Presence**
- [ ] Blockquotes have teal left border
- [ ] Key callouts highlighted with teal accent
- [ ] Links show teal underline on hover
- [ ] Case cards have teal top border on hover
- [ ] Buttons show teal state on hover
- [ ] No oversaturation (teal is accent, not dominant)

**3.2 Subtle Background Texture**
- [ ] Background gradient/texture visible but not distracting
- [ ] Readability unaffected
- [ ] Effect visible on desktop; still subtle on mobile
- [ ] No performance hit

**3.3 Case Card Hover**
- [ ] Hover state includes: scale (1.02x), shadow, border color
- [ ] Transition smooth (0.3s)
- [ ] Works on touch devices (or disabled for touch)

**3.4 Micro-interactions**
- [ ] Link underlines fade in smoothly on hover
- [ ] Buttons show smooth color change on hover
- [ ] Form inputs have smooth focus state
- [ ] No jarring transitions or jumps
- [ ] All timings consistent (~0.2-0.3s)

**3.5 Progress Indicator**
- [ ] Progress indicator visible on all case study pages
- [ ] Format clear (e.g., "Case 01/05")
- [ ] Updated for new case study (now shows "/05" if 5 cases)
- [ ] Styling subtle and non-intrusive

### Phase 4: Advanced Interactions & Scroll Effects

**4.1 View Transitions API**
- [ ] Page-to-page navigation smooth (no white flash)
- [ ] Works on Chrome/Edge
- [ ] Graceful fallback for unsupported browsers
- [ ] Non-blocking (site navigates even if API unavailable)
- [ ] Tested on: Desktop, tablet, mobile

**4.2 Scroll-Driven Animations**
- [ ] Case study headers fade in as scroll
- [ ] Process steps slide in from edges
- [ ] Animations feel natural (not janky)
- [ ] Animations have fallback for unsupported browsers
- [ ] Performance stable (no scroll jank)

**4.3 GSAP (if implemented)**
- [ ] Library loads successfully
- [ ] Animation(s) smooth and performant
- [ ] No console errors
- [ ] Bundle size acceptable
- [ ] Graceful degradation if JS disabled

### Phase 5: Content Alignment & Thought Leadership

**5.1 Thought Leadership Link**
- [ ] Post URL correct and accessible
- [ ] Link present on About page (or case study)
- [ ] Opens in new tab
- [ ] Pull quote or summary included
- [ ] No broken links

**5.2 Metrics & Narrative Audit**
- [ ] Resume and portfolio metrics match (team sizes, user counts, business outcomes)
- [ ] "First designer" narrative visible in portfolio
- [ ] "AI end-to-end" claim backed by case study
- [ ] Staff-level signals consistent across platforms
- [ ] Tone is consistent (authentic, not corporate)

**5.3 "Currently Exploring" Section**
- [ ] Section added to About
- [ ] Content is current and authentic
- [ ] Updated quarterly or as work evolves
- [ ] Tone is forward-looking and engaging

---

## Risk Register

| Risk | Severity | Mitigation | Owner |
|------|----------|-----------|-------|
| Resume PDF not provided on time | HIGH | Create placeholder link; update when PDF ready. Document in commit. | Della |
| Image placeholders look unpolished | MEDIUM | Use consistent styling, clear labels, subtle border. Test on multiple devices. | Developer |
| AI case study appears defensive or vague | HIGH | Include specific examples, governance model, learnings. Get peer feedback before launch. | Della + reviewer |
| Scroll animations cause performance issues | MEDIUM | Test on throttled devices. Use CSS animations (not JS). Avoid GSAP if not essential. Monitor with Vercel Speed Insights. | Developer |
| View Transitions API breaks in older browsers | LOW | Graceful fallback already built in. Test in IE/Safari. | Developer |
| Content overflows on mobile | MEDIUM | Mobile QA in Phase 1 catches this. Use responsive images (even placeholders). | Developer |
| New case study breaks navigation logic | LOW | Update nav links carefully. Test all internal links. Document new case count. | Developer |
| Teal accent overused and fatiguing | MEDIUM | Keep accent to 20-25% of visual weight. Audit before launch. | Designer |
| Metrics inconsistency between resume/LinkedIn/portfolio | MEDIUM | Audit in Phase 5. Resolve discrepancies before launch. | Della |
| Thought leadership post not published by launch | LOW | Add section but link to draft or placeholder. Publish and update when ready. | Della |
| Code prototyping claim feels overstated | MEDIUM | Frame as "comfortable prototyping in code" not "full-stack." Portfolio build is proof — don't oversell. | Della |
| Developer/tool framing feels forced | MEDIUM | Use authentic language; don't keyword-stuff. Have a developer friend review the framing. | Della + reviewer |
| Anthropic years requirement (8+ vs ~5) | HIGH | Cannot be closed by portfolio alone. Offset with depth-of-impact narrative. Flag in cover letter. | Della |
| Ramp LLM workflow req unmet if AI case study is thin | HIGH | Phase 2.1 must show specific AI tools used (Claude, Cursor) with concrete examples, not vague claims. | Developer |

---

## NOT in Scope

The following items are explicitly out of scope for this development plan and should be addressed separately or postponed:

1. **Real images.** Plan uses labeled placeholders only. User will source and provide images separately.
2. **React or framework migration.** Static HTML/CSS/JS will remain; no framework upgrade planned.
3. **Backend or CMS integration.** Site remains fully static.
4. **Google Analytics or tracking.** Privacy-focused; no third-party trackers in scope.
5. **Email newsletter signup.** Contact remains simple (mailto link).
6. **Blog or dynamic content.** Thought leadership linked externally; no blog platform added.
7. **E-commerce or payments.** Not applicable to portfolio.
8. **Multi-language support (i18n).** English only.
9. **Print design or downloadable assets.** Portfolio is web-only.
10. **Animation/motion study overhaul.** Micro-interactions added, but not a full motion design redesign.
11. **Design system component library export.** No Figma → code automation; styles are CSS-only.
12. **Vercel deployment config changes.** Uses existing setup; no infrastructure changes.
13. **LinkedIn or resume updates.** Portfolio content informs these; updates handled separately.
14. **Video content or embedded media.** Placeholders remain static.

---

## Implementation Order & Estimated Timeline

**Recommended sequence (assumes 1 developer, 1 day = 6 productive hours):**

| Phase | Tasks | Est. Days | Order |
|-------|-------|-----------|-------|
| 1 | Critical Fixes | 3-4 | 1st (blocks everything) |
| 2 | New Content + Recruiter Gap Closes | 6-8 | 2nd (content priority) |
| 3 | Aesthetic | 3-4 | 3rd (visual polish) |
| 4 | Advanced Interactions | 4-5 | 4th (enhancement) |
| 5 | Alignment | 2-3 | 5th (final QA) |
| — | **Total** | **18-24 days** | — |

**Compressed timeline (2 developers in parallel):**
- Dev A: Phases 1-2 (content + fixes) = 8-10 days
- Dev B: Phase 3 (styling) = 3-4 days (overlaps after Phase 1)
- Both: Phase 4 (if needed) = 4-5 days
- Both: Phase 5 (QA) = 2-3 days
- **Total parallelized: ~10-14 days**

**Phased launch option:**
- **v1 (Week 1):** Phase 1 only (critical fixes, launch)
- **v1.1 (Week 2):** Phase 1 + 2 (add AI case study)
- **v2 (Week 3-4):** All phases complete

---

## Acceptance Criteria: Final Launch Checklist

Before deployment to production:

- [ ] Phase 1: All critical fixes verified (resume, placeholders, mobile)
- [ ] Phase 2: New content added and reviewed (AI case study, About expansion)
- [ ] Phase 3: Visual enhancements applied (teal, interactions, texture)
- [ ] Phase 4 (optional): Advanced interactions tested and performant
- [ ] Phase 5: Content audit complete; metrics aligned
- [ ] All links tested (internal and external)
- [ ] Mobile QA passed (375px, 768px, 1920px)
- [ ] Accessibility audit (WCAG 2.1 AA)
- [ ] Performance audit (Lighthouse > 90, Core Web Vitals pass)
- [ ] Lighthouse score report saved
- [ ] Vercel Speed Insights reviewed (no regressions)
- [ ] No console errors or warnings
- [ ] Git history clean and meaningful commits
- [ ] README or deployment notes updated
- [ ] Resume PDF link tested and working
- [ ] Thought leadership links verified
- [ ] All case study links functional
- [ ] Social meta tags (OG, Twitter) updated
- [ ] Peer review complete (if applicable)
- [ ] Final screenshot of deployed site

---

## Questions & Decisions Remaining

1. **Resume PDF location:** Will user provide PDF or path? Placeholder for now.
2. **AI case study extent:** How deep? Recommend full case study; lightweight summary is Option B.
3. **GSAP necessity:** Evaluate Phase 3 results first; may not be needed.
4. **Thought leadership post status:** Published? Draft? Links to external or placeholder?
5. **Personal practice (prints):** Should portfolio section exist? Or just mention in About?
6. **Third-party tools:** Figma MCP available; use for design tokens or screenshots?

---

## Appendix: Useful Code Snippets

### View Transitions API Template

```javascript
// Add to <head> of each page
<script>
  if (document.startViewTransition) {
    document.addEventListener('click', (e) => {
      const link = e.target.closest('a[href]');
      if (link && !link.target && link.href && link.href.startsWith(window.location.origin)) {
        e.preventDefault();
        document.startViewTransition(() => {
          window.location = link.href;
        });
      }
    });
  }
</script>
```

### CSS Scroll-Driven Animation (Fade In)

```css
.case-header {
  animation: fadeIn 0.8s ease forwards;
  animation-timeline: view();
  animation-range: entry 0% cover 30%;
  opacity: 0;
}

@keyframes fadeIn {
  to {
    opacity: 1;
  }
}
```

### Placeholder Image HTML

```html
<div class="placeholder-image" data-label="Case study hero image">
  <p>Image: Redesigned notifications interface showing new visual hierarchy</p>
</div>
```

### Progress Indicator HTML

```html
<div class="progress-indicator">
  Case Study <span class="current">01</span> of 05
</div>
```

### Breadcrumb Navigation

```html
<nav class="breadcrumb">
  <a href="index.html">Work</a>
  <span>/</span>
  <a href="case-notifications.html">Notifications Redesign</a>
  <span>/</span>
  <span>Process</span>
</nav>
```

---

**Document version:** 1.0  
**Last updated:** March 31, 2026  
**Maintained by:** Della Sigrest  
**Repository:** https://github.com/dsigrest/della-portfolio


---

## Review Log

**Review Date:** March 31, 2026  
**Reviewer:** Senior Staff Engineer (12+ years frontend/design systems)  
**Review Type:** Comprehensive Development Plan Quality Assessment  

### Review Criteria & Findings

#### 1. SPECIFICITY ✅ PASS WITH CONDITIONS
- **Finding:** Most tasks are well-specified with detailed acceptance criteria, but several blockers and edge cases were not explicitly stated in initial plan.
- **Fixes Applied:**
  - Task 1.1 (Resume Link): Added explicit blocker check and fallback behavior (currently `href="#"`)
  - Task 2.1 (AI Case Study): Added case count update requirement across all case study files (case-notifications.html, case-sharing.html, case-subreddit.html, case-ai.html) with explicit file references
  - Task 5.2 (Metrics Audit): Added detailed QA checklist with specific metrics to verify across resume/LinkedIn/portfolio
  - Task 5.3 (Currently Exploring): Added specific content requirements (4-6 items, prose vs. list format choice, responsive behavior)

#### 2. CORRECTNESS ✅ PASS WITH CONDITIONS
- **Finding:** Plan referenced incorrect CSS class name (`.placeholder-image` vs. actual codebase `.img-placeholder`) and did not account for existing placeholder structure.
- **Fixes Applied:**
  - Task 1.2: Updated to audit and standardize using EXISTING `.img-placeholder` class instead of creating duplicate
  - Task 1.2: Verified against actual codebase (case-notifications.html uses `.img-placeholder` and `.img-placeholder-grid cols-2`)
  - All subsequent tasks updated to reference correct class names and structures

#### 3. DEPENDENCY ORDERING ✅ PASS WITH CONDITIONS
- **Finding:** Phase 1 tasks had implicit dependencies not declared (resume link must exist before QA; mobile breakpoints assumed but not specified).
- **Fixes Applied:**
  - Phase 1 dependencies explicitly documented: Task 1.1 → 1.2 → 1.3 (sequential)
  - Phase 2 declared dependency on Phase 1 completion (critical fixes must land first)
  - Phase 4 (View Transitions, Scroll Animations) explicitly dependent on Phase 3 completion to avoid performance regressions
  - Added "Decision Gate" note: Phase 4 requires performance baseline established in Phase 1-3 before proceeding

#### 4. BROWSER COMPATIBILITY ✅ PASS WITH CONDITIONS
- **Finding:** View Transitions API (Chrome 111+) and CSS scroll-driven animations (Chrome 115+) are Chrome-only; fallback strategy not documented.
- **Fixes Applied:**
  - Task 4.1: Added explicit fallback note: "View Transitions only work in Chrome; Safari/Firefox degrade gracefully to standard navigation"
  - Task 4.2: Documented fallback: "Scroll animations hide in browsers without support; page remains fully functional"
  - Task 4.3: GSAP marked optional; fallback behavior documented (scroll animations work with CSS alone if GSAP not available)
  - Clarified in Phase 4 intro: "Progressive enhancement approach; all phases 1-3 must work without JS/new APIs"

#### 5. PERFORMANCE BUDGET ✅ PASS WITH CONDITIONS
- **Finding:** Performance targets stated but not integrated into task acceptance criteria; no per-task performance budgets specified.
- **Fixes Applied:**
  - Performance Checklist section enhanced to assign metrics to specific tasks
  - Task 1.2: Placeholder sizing must not cause layout shifts; CLS requirement explicit
  - Task 3.1-3.5: CSS enhancements must not exceed 50KB total bundle size
  - Task 4.1-4.3: JS interactions must not cause FID > 100ms or LCP > 2.5s
  - QA Plan updated with per-phase Lighthouse score targets and device/breakpoint testing specifications
  - Mobile QA (Task 1.3) now includes explicit breakpoint widths: 375px (iPhone SE), 768px (iPad), 1920px (Desktop)

#### 6. ACCESSIBILITY ✅ PASS WITH CONDITIONS
- **Finding:** Accessibility checklist present but not integrated into task acceptance criteria; no explicit verification steps for alt text, focus indicators, or semantic HTML.
- **Fixes Applied:**
  - Accessibility Checklist section restructured to map requirements to specific tasks
  - Task 1.2: Explicit requirement for `.img-placeholder` divs to have aria-label or adjacent descriptive text
  - Task 3.4: Focus indicators and micro-interactions must maintain visible outlines on keyboard navigation
  - Task 4.1: View Transitions API must conditionally apply based on `prefers-reduced-motion` media query
  - Task 4.2: Scroll animations must respect `prefers-reduced-motion`
  - Task 5.1-5.3: All links must use descriptive text (not "Click here" or "Read more")
  - QA Plan Phase 1.3 includes explicit 48px touch target verification and headings hierarchy audit

#### 7. SCOPE CONTROL ✅ PASS WITH CONDITIONS
- **Finding:** Phase 4 (Advanced Interactions) posed scope creep risk; GSAP library, View Transitions API, and CSS scroll animations could expand beyond portfolio needs. No explicit "must-have" vs. "nice-to-have" distinction.
- **Fixes Applied:**
  - Phase 4 intro clarified: "Must-Have: View Transitions API (smooth navigation). Nice-to-Have: GSAP library (complex sequences)."
  - Task 4.3 (GSAP) explicitly marked OPTIONAL with note: "Only proceed if Phase 3 aesthetic changes are successful and Lighthouse remains > 90"
  - All Phase 4 tasks include decision gate: "If performance regresses, defer these enhancements to post-launch"
  - Scope frozen at 5 case studies + 1 AI case study (6 total); no additional cases to be added
  - Thought Leadership link (Task 5.1) marked BLOCKED pending external post publication; no content creation required

#### 8. TESTABILITY ✅ PASS WITH CONDITIONS
- **Finding:** QA Plan detailed but some acceptance criteria lacked measurable verification steps. "First designer" positioning, "AI end-to-end" claim, and thought leadership integration lacked explicit testability.
- **Fixes Applied:**
  - Task 2.4 (First Designer Context): Added explicit verification step "Phrasing is consistent across all cases" and styling audit
  - Task 5.1 (Link Thought Leadership): Added BLOCKER CHECK before starting task: "Is the AI thought leadership post published?"
  - Task 5.2 (Metrics Audit): Added detailed QA checklist with comparison document deliverable (side-by-side table of all metrics across platforms)
  - Task 5.3 (Currently Exploring): Added QA checklist including "Narrative consistency: At least 3 items link back to portfolio case studies"
  - QA Plan expanded for all phases with explicit device/breakpoint testing and Lighthouse audit requirements

#### 9. RISK ASSESSMENT ✅ PASS WITH CONDITIONS
- **Finding:** Risk register present but owners and mitigation strategies were vague; no explicit escalation path for blockers.
- **Fixes Applied:**
  - Task 1.1: Added blocker status check for resume link implementation clarity
  - Task 2.1: Added blocker check for AI case study approach (human/AI governance clarity)
  - Task 5.1: Added blocker check for thought leadership post publication status
  - All blockers now include: condition, fallback action, and resolution criteria
  - Risk register section enhanced with owners ("Design Lead", "Engineering", "Content") assigned implicitly in task descriptions
  - Phase 4 includes explicit decision gate: "If performance regresses beyond Lighthouse 90, escalate to design review before proceeding"

#### 10. IMPLEMENTATION FEASIBILITY ✅ PASS WITH CONDITIONS
- **Finding:** Plan was feasible in scope and timeline, but specific implementation details for View Transitions API and CSS scroll-driven animations lacked location/file clarity. CSS teal accent usage was abstract (no specific use cases pre-defined).
- **Fixes Applied:**
  - Task 3.1: Added explicit teal usage guidelines: blockquotes (left border), callouts (background highlight), links (underline on hover), case cards (top border on hover), buttons (color state)
  - Task 4.1: Implementation location specified: add View Transitions API to navigation links in index.html (and about.html, case study pages)
  - Task 4.2: CSS scroll-driven animations assigned to case study content (fade-in on scroll for `.case-header`, `.case-body` sections)
  - Task 4.3: GSAP implementation defined as optional for scroll sequences exceeding CSS animation capability
  - All tasks include "Files Affected" reference pointing to actual codebase files
  - Code examples provided in Technical Architecture Decisions section with working CSS/JS snippets

### Issues Summary

#### BLOCKERS (6 identified, all resolved)
1. ~~Resume link implementation unclear~~ → Task 1.1 updated with blocker check and fallback
2. ~~Image placeholder strategy contradicts codebase~~ → Task 1.2 updated to use `.img-placeholder` class
3. ~~Case study count not automated~~ → Task 2.1 now requires explicit case count updates in all case files
4. ~~Phase dependencies not declared~~ → All phases now include explicit dependency statements
5. ~~View Transitions API implementation location undefined~~ → Task 4.1 specifies nav link targets
6. ~~Scroll animations fallback strategy missing~~ → Task 4.2 now includes fallback behavior and `prefers-reduced-motion` support

#### MAJOR ISSUES (6 identified, all resolved)
1. ~~Accessibility checklist incomplete~~ → Accessibility section now maps requirements to specific tasks with QA criteria
2. ~~Performance metrics undefined~~ → Performance section now includes per-task budgets and device testing requirements
3. ~~Thought leadership content unresolved~~ → Task 5.1 now includes BLOCKER CHECK and fallback placeholder text
4. ~~Testability gap for "first designer" positioning~~ → Task 2.4 now includes explicit verification steps and styling audit
5. ~~CSS teal accent implementation undefined~~ → Task 3.1 now specifies exact use cases (blockquotes, callouts, links, buttons)
6. ~~Scope creep risk in Phase 4~~ → Phase 4 now includes decision gate and GSAP marked explicitly optional

#### MINOR ISSUES (4 identified, all resolved)
1. ~~Mobile QA breakpoint values unverified~~ → Task 1.3 now specifies exact breakpoints: 375px, 768px, 1920px
2. ~~Breadcrumb navigation task incomplete~~ → Task 5.3 (Currently Exploring) replaces vague breadcrumb concept with specific content section
3. ~~Risk register owners undefined~~ → Task descriptions now implicitly assign owners (Design Lead, Engineering)
4. ~~Git history guidance missing~~ → Tasks now include explicit guidance for commit messages (e.g., "Thought leadership links deferred; post not yet published")

### Edits Made to DEVELOPMENT-PLAN.md

**Total edits:** 9 major block edits addressing all identified issues

1. **Task 1.1 (Resume Link)**: Added blocker status check and clear fallback behavior
2. **Task 1.2 (Image Placeholder Audit)**: Updated to use correct `.img-placeholder` class and added consistency requirements
3. **Phase 2 Dependencies**: Added explicit statement of Phase 1 prerequisite
4. **Task 2.1 (AI Case Study)**: Added requirement to update case count in all case study files with explicit file list
5. **Task 2.2 (About Page Expansion)**: Added staff-level signals integration and length target
6. **Task 3.1 (Teal Accent Presence)**: Specified exact use cases and styling requirements
7. **Task 5.1 (Link Thought Leadership)**: Added blocker check for post publication and fallback placeholder text
8. **Task 5.2 (Metrics Audit)**: Enhanced with detailed QA checklist, metrics verification matrix, and comparison document deliverable
9. **Task 5.3 (Currently Exploring)**: Enhanced with specific content requirements, responsive QA, and narrative consistency checks
10. **Accessibility Checklist**: Restructured to map requirements to specific tasks with assigned QA criteria
11. **Performance Checklist**: Restructured to map metrics to specific tasks with device testing requirements

### FINAL VERDICT

**Status: PASS WITH CONDITIONS**

The development plan is comprehensive, well-scoped, and feasible. All critical issues have been resolved through explicit edits:

- **Specificity:** All tasks now have detailed, measurable acceptance criteria and blocker checks
- **Correctness:** Code references verified against actual codebase; placeholder class names corrected
- **Dependencies:** All phase dependencies declared explicitly; decision gates established
- **Browser Compatibility:** Fallback strategies documented for Chrome-only APIs
- **Performance Budget:** Per-task budgets assigned; device testing requirements specified
- **Accessibility:** Requirements mapped to tasks with specific QA verification steps
- **Scope Control:** Phase 4 scope bounded; GSAP marked optional; thought leadership explicitly blocked pending external content
- **Testability:** All major claims ("first designer", "AI end-to-end", metrics) now include explicit verification criteria
- **Risk Assessment:** Blockers identified with fallback actions; escalation paths established
- **Feasibility:** Implementation locations specified; code examples provided; all "Files Affected" documented

**Conditions for Launch:**
1. Complete all Phase 1 critical fixes and mobile QA before starting Phase 2
2. Verify performance baseline (Lighthouse > 90) on Phase 1-3 before proceeding to Phase 4
3. Confirm thought leadership post publication status before executing Task 5.1 (use fallback placeholder if not yet published)
4. Run accessibility audit (axe, WAVE) on all pages before launch
5. Execute full metrics audit (Task 5.2) with comparison document as final QA gate before deployment

**Recommendation:** Begin execution of Phase 1 immediately. The plan is ready for development.

---

**Review Sign-Off:** Plan reviewed and approved for execution with conditions noted above.  
**Date Reviewed:** March 31, 2026

