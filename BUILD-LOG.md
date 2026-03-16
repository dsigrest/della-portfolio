# Build Log — Della Sigrest Portfolio

**Started:** March 12, 2026
**Last updated:** March 16, 2026
**Status:** Active

## Project context

A portfolio website for Della Sigrest, Senior Product Designer (previously Reddit). The site showcases 4 case studies spanning systems thinking, AI product design, growth strategy, and 0→1 leadership. Built collaboratively with AI (Claude) as both a speed strategy and a meta case study for how AI fits into a senior designer's practice. Static HTML/CSS/JS deployed on Vercel.

## Current status

Site is live at `https://della-portfolio.vercel.app`. All 6 pages built (home, about, 4 case studies). Images have been replaced with labeled placeholders pending confidentiality review. Dev tooling is set up: GitHub repo (`dsigrest/della-portfolio`), Vercel auto-deploy on push, Homebrew + GitHub CLI installed on local Mac. Cowork is now connected directly to the project folder, so future edits write to the live files without manual copying.

Next up: Della reviews screenshots for redaction needs, approved images get swapped back in, then mobile QA, copy editing, and resume PDF.

## Open questions & blockers

- [ ] Which screenshots are safe to publish? Need Della's review for confidential content — *added Mar 16*
- [ ] Should the "AI in My Practice" section be a standalone page or a blog-style post? — *added Mar 13*
- [ ] How to handle confidential work visuals (redacted screenshots vs. abstract diagrams vs. skip entirely) — *added Mar 13*
- [ ] How much process detail should each case study include? Current draft leans strategic — *added Mar 13*
- [ ] Resume PDF — needs to be created and linked — *added Mar 12*
- [ ] Custom domain setup — *added Mar 12*
- [x] Vercel deployment — *added Mar 12, resolved Mar 16: deployed to della-portfolio.vercel.app*
- [x] Dev tooling (git, GitHub CLI, Homebrew) — *added Mar 16, resolved Mar 16: all installed and working*
- [x] Working directory connection — *added Mar 16, resolved Mar 16: Cowork now edits files in-place*

## Artifacts

| Artifact | Path / Link | Description | Date |
|----------|-------------|-------------|------|
| Live site | https://della-portfolio.vercel.app | Vercel deployment, auto-deploys on push | Mar 16 |
| GitHub repo | https://github.com/dsigrest/della-portfolio | Private repo, main branch | Mar 16 |
| index.html | portfolio-site/index.html | Home: hero, 4 pillars, 4 case study cards | Mar 12 |
| about.html | portfolio-site/about.html | Career narrative, links, "what I'm looking for" | Mar 12 |
| case-notifications.html | portfolio-site/case-notifications.html | Case study 1: Notifications & Inbox (Systems Thinking) | Mar 12 |
| case-ai.html | portfolio-site/case-ai.html | Case study 2: KLP/AI (AI Product Design) | Mar 13 |
| case-sharing.html | portfolio-site/case-sharing.html | Case study 3: Sharing & Embeds (Growth Loops) | Mar 13 |
| case-subreddit.html | portfolio-site/case-subreddit.html | Case study 4: Subreddit Success (0→1 Leadership) | Mar 13 |
| styles.css | portfolio-site/styles.css | Shared design system: tokens, layout, responsive, animations | Mar 12 |
| vercel.json | portfolio-site/vercel.json | Clean URLs, image caching headers, security headers | Mar 16 |
| SVG: Inbox Framework | portfolio-site/img/diagram-inbox-framework.svg | 5-cohort × 3-pillar matrix with priority heat map | Mar 13 |
| SVG: Sharing Flywheel | portfolio-site/img/diagram-sharing-flywheel.svg | Circular Share→Preview→Visit→Engage cycle | Mar 13 |
| SVG: AI Governance | portfolio-site/img/diagram-ai-governance.svg | 3-layer trust stack diagram | Mar 13 |
| SVG: Community Lifecycle | portfolio-site/img/diagram-community-lifecycle.svg | 5 stages with drop-off percentages | Mar 13 |
| Project Plan | Portfolio Website Project Plan.md | Original comprehensive project plan (superseded) | Mar 12 |
| Visual Pattern Criteria | VISUAL_PATTERN_CRITERIA.md | Screenshot classification system for image curation | Mar 13 |
| BUILD-LOG.md | portfolio-site/BUILD-LOG.md | This file — also serves as future "AI in My Practice" source | Mar 12 |

## Log entries

### Mar 16, 2026 — Vercel deployment + dev tooling + placeholder swap

**What happened:**
Massive infrastructure session. Got the site from local files to live on the internet, set up the full development workflow, and swapped all images to placeholders for confidentiality review.

Step by step:
1. Rebuilt the entire portfolio-site from conversation history (previous session's VM had reset, so all local files were gone — but everything was preserved in the conversation)
2. Created `vercel.json` with clean URL config, image caching headers, and security headers
3. Walked Della through installing Homebrew, GitHub CLI, and authenticating with GitHub — first time using Terminal for this workflow
4. Created GitHub repo `dsigrest/della-portfolio` via `gh repo create` and pushed all files
5. Connected to Vercel — site went live at `della-portfolio.vercel.app`
6. Della flagged confidentiality concerns about screenshots — smart call
7. Replaced all image references across 4 case study files with labeled placeholder divs
8. Added CSS styles for placeholder boxes (`.img-placeholder`, `.img-placeholder-grid`)
9. Walked through the copy-replace-push workflow (initial confusion about files being in separate locations)
10. Connected Cowork directly to the `portfolio-site` folder so future edits are in-place

**Decisions made:**
- Made GitHub repo public initially (standard for portfolio sites), then Della asked about security — explained that public means viewable but not editable. She switched it to private.
- Replaced ALL images with placeholders rather than selectively — Della wanted to review everything before any screenshots went public. This was the right conservative approach.
- Established the iteration loop: Claude edits files → Della runs `git add . && git commit -m "msg" && git push` → Vercel auto-deploys in ~15 seconds

**What changed:**
- New files: `vercel.json`
- Modified: `styles.css` (added placeholder CSS), all 4 case study HTML files (images → placeholders)
- Infrastructure: GitHub repo created, Vercel connected, local dev tools installed

**Next steps:**
- Della reviews screenshots for redaction needs
- Swap approved images back into case studies
- Mobile QA pass
- Copy editing pass
- Resume PDF creation and integration

---

### Mar 13, 2026 — All case studies + image integration + SVG diagrams

**What happened:**
- Completed all 4 case study pages (Notifications, KLP/AI, Sharing & Embeds, Subreddit Success)
- AI scanned ~600 screenshots across Apple Photos to identify the 30 most relevant images
- Created a visual pattern classification system (VISUAL_PATTERN_CRITERIA.md) to systematically sort screenshots
- Built 4 custom SVG diagrams matching the site's design system for strategic frameworks that had no screenshot equivalent
- Integrated all images and SVGs into case study HTML with responsive grid layouts
- Generated self-contained preview HTML for reviewing in browser (workaround for file:// CSS loading issues)

**Decisions made:**
- Della delegated image curation entirely to AI: "Just pick the best ones" — this is a notable trust signal and worth documenting for the meta case study
- Created SVG diagrams rather than leaving framework sections image-free — the diagrams serve double duty as both portfolio visuals and demonstrations of the AI collaboration
- Used responsive CSS Grid for image layouts (2-col for pairs, 3-col for series) rather than full-width stacking

**What changed:**
- 4 new HTML files: case-ai.html, case-sharing.html, case-subreddit.html (case-notifications.html updated)
- 4 new SVG files in img/
- 30 PNG screenshots copied to img/ (from Apple Photos)
- BUILD-LOG.md updated with Phase 4

**AI pattern observed:**
Image curation at scale was a strong AI use case — scanning hundreds of images and matching them to narrative beats. But the accuracy of selection still needs human review (especially for confidentiality), which Della correctly flagged in the next session.

---

### Mar 12, 2026 — Project kickoff: strategy, visual direction, and site foundation

**What happened:**
Three phases in one session:

**Phase 1 — Strategy:** AI reviewed the full career materials packet and generated a comprehensive project plan. Original recommendation was Framer, but Della pivoted to building with AI using static HTML — better signal for AI-forward positioning and zero platform lock-in. This pivot also created the meta case study opportunity.

**Phase 2 — Visual direction:** AI generated three complete style previews as self-contained HTML files:
- Option A: Dark Minimal (indigo/purple accent, spacious)
- Option B: Light Clean (structured cards, editorial feel)
- Option C: Bold Editorial (orange accent, Space Grotesk, big numbers)

Della mixed and matched: Option B's layout + Option A's dark palette + teal accent (no purple). This cross-pollination decision is a great example of where human taste is essential — AI can generate distinct options but the synthesis across options required Della's eye.

**Phase 3 — Site build:** Built the foundational site structure:
- Design system with CSS custom properties (tokens for colors, spacing, typography)
- Home page with hero, 4 value pillars, 4 case study cards
- About page with career narrative
- Notifications & Inbox case study (first complete case study)
- Responsive breakpoints, scroll animations, mobile nav

**Decisions made:**
- Static HTML over Framer: AI-forward signal + no platform lock-in
- Teal (#2dd4bf) accent over purple: taste decision by Della
- Vercel over Netlify: signal alignment with target companies (Vercel signals modern frontend awareness)
- Case study structure: Context → Insight → System → Experiments/Details → Outcome → Reflection (strategic framing over process documentation)
- Footer includes "designed collaboratively with AI" — transparency as a feature

**What changed:**
- Created: index.html, about.html, case-notifications.html, styles.css, BUILD-LOG.md
- Created: 3 style preview HTML files (in parent folder)
- Created: Portfolio Website Project Plan.md

---

## Patterns observed

### Where AI accelerates
1. **Content synthesis → structure**: Turning a messy packet of career materials into a coherent site architecture in a single pass
2. **Style exploration**: Generating multiple distinct, production-quality visual directions in minutes, with real content
3. **Boilerplate elimination**: CSS resets, responsive grids, animation observers, nav toggles — all correct on first pass
4. **Consistent voice**: Maintaining the same tone and positioning language across 6 pages
5. **Image curation at scale**: Scanning hundreds of screenshots and matching them to narrative context
6. **SVG diagram generation**: Creating custom visuals that match an existing design system
7. **Infrastructure guidance**: Walking a non-engineer through Terminal, git, GitHub CLI, and Vercel setup step by step

### Where human judgment is essential
1. **Taste decisions**: Color vetoes, layout cross-pollination, what "feels right"
2. **Strategic framing**: Deciding the build process is itself a case study
3. **Career signal reasoning**: Choosing Vercel over Netlify for audience perception
4. **Content accuracy**: Verifying metrics and claims against source materials
5. **What to leave out**: CPO vision as sidebar, not case study
6. **Confidentiality awareness**: Flagging that screenshots need review before going public — AI had no way to assess this risk
7. **Trust calibration**: Knowing when to delegate fully ("just pick the best ones") vs. when to review carefully (image redaction)

### Failure modes encountered
1. **File:// protocol CSS loading**: Browser security blocks cross-file CSS references. Workaround: inlined CSS preview files. Real fix: Vercel deployment.
2. **VM session persistence**: Working directory resets between Cowork sessions. All code must be in the mounted project folder to persist.
3. **File sync confusion**: Edits in Cowork's working folder vs. the user's local git repo are separate locations. Solved by mounting the project folder directly.
4. **Screenshot path errors**: Complex folder structures with inconsistent naming required multiple attempts to find correct paths.
