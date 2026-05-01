# Build Log Archive — March 2026

**Archive type:** quarterly archive split (Q1)
**Archive created:** May 1, 2026 (Session 50, Phase 1 housekeeping split)
**Source file:** `BUILD-LOG.md` (lines 1165–1262 of pre-split version)
**Coverage:** March 12 – March 16, 2026
**Reason:** Soft size threshold management — see `~/CoworkWorkspace/CLAUDE.md` "Living doc split"

This file contains historical BUILD-LOG entries archived from `BUILD-LOG.md` to keep the live file editable within safe in-place edit thresholds. All entries are preserved verbatim in original document order.

For active log entries (April 28+, Sessions 34–49 onward), see [`BUILD-LOG.md`](BUILD-LOG.md).
For sibling Q2-early archive (April 17–22), see [`BUILD-LOG-2026-Q2-early.md`](BUILD-LOG-2026-Q2-early.md).

---

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
