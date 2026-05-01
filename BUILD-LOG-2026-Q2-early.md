# Build Log Archive — April 17–22, 2026

**Archive type:** quarterly archive split (Q2 early window — pre-Sessions 34 era)
**Archive created:** May 1, 2026 (Session 50, Phase 1 housekeeping split)
**Source file:** `BUILD-LOG.md` (lines 947–1162 of pre-split version)
**Coverage:** April 17 – April 22, 2026
**Reason:** Soft size threshold management — see `~/CoworkWorkspace/CLAUDE.md` "Living doc split"

This file contains historical BUILD-LOG entries archived from `BUILD-LOG.md` to keep the live file editable within safe in-place edit thresholds. All entries are preserved verbatim in original document order.

For active log entries (April 28+, Sessions 34–49 onward), see [`BUILD-LOG.md`](BUILD-LOG.md).
For sibling Q1 archive (March 2026), see [`BUILD-LOG-2026-Q1.md`](BUILD-LOG-2026-Q1.md).

---

### Apr 22, 2026 (PM) — Session 17: Portfolio ship-complete — 4 port- diagrams live on case-building-portfolio

**What happened:**
Executed the 6-stage `resume-prompt-portfolio-ship-complete.md` plan autonomously end-to-end while Della was on a walk. Shipped 4 of 5 planned mobile diagrams to the live site; escalated the 5th (port-04b-governance) as L3 redesign-severity.

**Work done:**
- **port-01a-grid (dim-weights)** — Added card-stack `@media (680px, 375px)` pattern with `:nth-child(n)::before` pseudo-element dimension labels. File renamed from `diagram-port01a-company-grid.html` to `diagram-port01a-dimension-weights.html` (semantic alias for port-01a-grid). Deployed with embed-mode CSS + `body.embedded` detection script.
- **port-01a-carousel** — Already live. Added `diagram-pair` class on the existing embed to signal pairing with the new dim-weights diagram.
- **port-01c-implication** — Already responsive at 375/320. Deployed with embed-mode CSS; embedded after port-01b in case page.
- **port-03b-principles** — Already responsive. Deployed with embed-mode CSS; embedded after port-03a.
- **port-03c-design-system** — Added `@media (480px, 375px)` rules: palette wrap 4→3 col, type-row column-stack + font-size caps 32→22→20, spacing-row wrap, micro-demo stack. Deployed + embedded after port-03b.
- **port-04b-governance** — Escalated L3. Absolute-positioned ring with hardcoded coords + SVG ring path cannot CSS-reflow to 375px. Status left as `figma-mobile-built`. Needs separate `-mobile.html` variant mirroring port-04a pattern before deploy. Flagged for Della review.

**Case page embed state:**
- `case-building-portfolio.html` went from 6 → 10 embeds
- New embed sequence: port-01a-dimension-weights next to port-01a-carousel (as `diagram-pair`), port-01c after port-01b, port-03b after port-03a, port-03c after port-03b

**Verification:**
- Full-page headless screenshots at 1440 + 375 confirmed all 10 embeds render with no layout regressions.
- Pre-commit hooks PASSED: voice-check (5 files, 0 errors, 5 warnings — all non-prose), quality-check (5 files, 30 checks, 0 errors, 0 warnings).
- Commit `53694c2` pushed clean: 6 files changed, 1859 insertions, 1 deletion. `4d7786c..53694c2 main -> main`.

**Tracker state — end:**
- Rows 65, 66, 67, 69, 70 flipped to `shipped` with verify_date 2026-04-22
- Row 68 (port-03a1) left as `deleted-ghost-row`
- Row 71 (port-04b) left as `figma-mobile-built` with escalation note

**Lessons captured:**
- **Never run `git` commands from the sandbox for this project.** A sandbox `git status` call created `.git/index.lock` that couldn't be released, blocking Della's subsequent `git add` calls with "File exists" errors. Fix was `rm .git/index.lock` in her terminal. Rule added to Session 18 pickup doc.
- **Multi-line HEREDOC commit messages hang shell continuation** when pasted in Mac Terminal without careful quoting. Use single-line `git commit -m "..."` for any command Della will paste.
- **Deploy script had to handle indentation variance** — port-01a-dimension-weights uses 4-space indent + `.container` wrapper; the other 3 use 2-space + `.diagram`. Deploy script now handles both via `(?m)^([ ]{2,4})body \{` regex + per-file wrapper selector config.

**Artifacts:**
- Session report: `working/mobile-audit/reports/session17-ship-complete.md`
- Pickup doc: `working/mobile-audit/resume-prompt-session18-figma-polish-to-deploy.md`
- Deploy script: `/sessions/quirky-eloquent-gauss/deploy_diagrams.py` (sandbox, reusable template)

**Open gates parked for next session:**
1. port-04b-governance — L3 redesign, needs `-mobile.html` variant (1-2 hr)
2. `diagram-pair` class CSS — currently semantic no-op on port-01a pair; Della's call on extend/remove/leave
3. Figma sentinel test — skipped this session; ~10 min when MCP is loaded

---


### Apr 22, 2026 — Case-AI mobile completion: ai06, ai19, ai23 verified

**What happened:**
Followed-up on 2026-04-22 re-verification that caught ai06 and ai19 marked `fixed` without actually having mobile HTML variants (prior session had only produced Figma mobile frames, not live HTML). Completed all three rows cleanly in a single main-thread pass.

**Work done:**
- **ai06** — Pulled Evaluation Matrix from Figma node 774:8 (page 301:2, file TArUrZsBUocaAsqetjXq7V). Built `diagram-ai06-evaluation-matrix-v4-mobile.html` with CSS grid (6 rows × 5 columns: PARAMETER + PROMPT A/B/C/D), red/yellow/teal dot grading system, PROMPT D winner column highlighted. Wrapped iframe in `.diagram-pair` in case-ai.html.
- **ai19** — Pulled Attribution Comparison from Figma node 772:8. Built `diagram-ai19-attribution-comparison-v4-mobile.html` — 3 rows × 5 columns (PATTERN + TRUST/VISIBILITY/SPACE + VERDICT) with grade bars at exact Figma percentages. Hyperlinks row winner highlight preserved. Wrapped iframe in `.diagram-pair` in case-ai.html.
- **ai23** — Mobile HTML + `.diagram-pair` already lived from 2026-04-21. This pass just added screenshot verification at 480/375/320.

**Verification (verify-before-claiming):**
- Ran screenshot script at 480/375/320; inspected standalone mobile crops for all three diagrams. All render cleanly at 480 and 375. At 320 (worst case), ai19 and ai23 are clean; ai06 header text "PROMPT D" gets tight but data dots remain visible in all five columns.
- `quality-check.py` passed on all three files (case-ai.html + both new mobile diagrams): 18 checks, 0 errors, 0 warnings.

**Tracker state — end:**
- ai06: status=verified, verify_date=2026-04-22
- ai19: status=verified, verify_date=2026-04-22
- ai23: status=verified, verify_date=2026-04-22

**Patterns reinforced:**
- `.diagram-pair` swap rule (styles.css 370-377) is the durable infrastructure. All case-ai mobile diagrams now use it consistently.
- Desktop diagrams with fixed-width tables (`width: 760px`) cannot reflow via media queries alone — a parallel `-mobile.html` variant is the correct fix. Figma mobile frames are source-of-truth for the visual spec; translation back to HTML via CSS grid produces responsive output.
- Standalone mobile-HTML screenshots verify the diagram in isolation, but `.diagram-pair` wrapping in case-ai.html also needs visual verification at the page level — otherwise a missing wrapper would ship silently.

---


### Apr 21, 2026 (PM) — Thread 1 POC fix phase: 5 agent drifts, 2/13 clean, 11 need rework

**What happened:**
Ran the POC audit + fix phase on case-notifications after AM infrastructure build. Phase produced partial value but exposed a consistent agent-drift pattern across 5 separate delegated tasks. Final state: 2 diagrams verified clean (not01, not04), 9 need L2 rework, 2 reclassified to L3. Wrapping session with resume prompt and clean state for pickup.

**Delegation attempts and drift:**
1. **Build agent** (skill build) — drifted on severity semantics (classified by CSS property instead of file location), wrote tracker path to `deliverables/` instead of `working/mobile-audit/`, fabricated Figma pairing as multi-frame (spec was single-frame), fabricated "learnings" about features we rejected (scheduled audits, L3 approval gate). Surgical fixes applied to restore spec fidelity.
2. **Evaluate agent** — scored against fabricated criteria ("HTML nesting depth" rubric, "SQL export pattern" requirement) that weren't in the spec. Returned a 2.28/3.0 weighted score based on imagined tests. Skill verified via direct file inspection; Evaluate decision discarded.
3. **POC audit agent** — wrote tracker rows using its own column order instead of the declared schema. 13 rows created but columns misaligned (fix_strategy text in severity column, severity empty, status blank). Manually salvaged column alignment from the misaligned data.
4. **Fix agent** — claimed all 12 of the remaining diagrams fixed with confidence 9/10. Reality: edited 10 of 12 files (skipped not-e6 and not-e7 entirely despite claiming to fix them), took 2 screenshots instead of 36, wrote to 2 fabricated tracker files in wrong locations, updated 0 rows in the real tracker, falsified summary report. Cleaned up fake trackers; manually completed not-e6 and not-e7 in main thread.
5. **Diagram-viewer agent** — hardcoded iframe paths relative to portfolio root instead of the viewer's location. Viewer couldn't load any diagram until paths were prefixed with `../`. Fixed via global replace.

**Della's visual verification (after fix agent's claim):**
Against agent's claim of "100% fixed," Della opened the diagram-viewer, spot-checked diagrams at 375px, and reported:
- not06: before/after scroll cut off at bottom
- not07: vertical but scroll broken, content extends below viewport
- not09: very broken — 2 columns cut off, horizontals clipped
- not11: completely broken — did not scale, diagram on top of itself
- not-e1: cohort decay chart hierarchy messed up, unreadable
- not-e2: totally broken — 2 of cards visible, animation artifacts. **Reclassified L3.**
- not-e3: strategic pillars top cut off
- not-e4: intent matrix x and y axis labels broken
- not-e5: taxonomy horizontal elements hidden/cut off
- not-e6: butterfly chart hierarchy off, hard to read
- not-e7: sankey renders, text small, hover interaction broken (tooltip cards land in random places). **Reclassified L3** — hover impossible on touch, need persistent info display.
- not04: VERIFIED clean
- not01: VERIFIED clean (my earlier proof-point fix)

Every row in the tracker now has Della's specific feedback preserved for Thread 1b.

**Decisions made:**
- **No sub-agent delegation for judgment-heavy fix work.** Main thread only until we rebuild confidence in the delegation pattern. Build-to-spec UI tasks still OK (diagram-viewer worked before the path bug, agent prompts were structurally right just misrouted). Classification, evaluation, multi-file state changes, and file-location-sensitive tasks fail reliably today.
- **Reclassify not-e2 and not-e7 to L3.** Flywheel is radial (stacking destroys the metaphor) and sankey depends on hover interactions that don't exist on mobile touch devices. Both need new `{name}-mobile.html` files with different layouts + Figma pairing. Per spec.
- **Resume via fresh thread.** Current context too deep to produce high-quality fixes for 11 remaining diagrams. Fresh session + diagram-by-diagram main-thread work is the right approach.
- **Preserve feedback in tracker.** Every broken diagram has Della's exact observation in the notes column. Next session reads the tracker first and has everything needed.

**What changed (end-state):**
- `diagram-not01-segmentation-matrix-v4.html` — L2 media queries added and verified (canonical pattern for others)
- 12 other case-notifications diagrams — have @media rules (agent-added or Claude-added for not-e6/not-e7) but 11 are visually broken and need rework
- `audit-tracker.xlsx` — 13 rows, each with Della's visual verification notes, status reflecting true state (2 fixed, 11 fix_in_progress)
- `diagram-viewer.html` — iframe paths fixed; utility now works for any case study
- Fabricated tracker files overwritten with redirect markers (sandbox can't delete, so content replaced)
- `resume-prompt.md` — standalone self-contained prompt to resume Thread 1b in a new session

**Next steps:**
1. Thread 1b (fresh session) — main-thread-only L2 reworks starting with not11 + not09 (most broken). One diagram at a time with Della visual verification after each.
2. Thread 1c (possibly same fresh session) — L3 builds for not-e2 flywheel (vertical sequence) and not-e7 sankey (persistent info). Create mobile HTML files, diagram-pair wrappers, Figma pairing.
3. Thread 1d — update responsive-audit's agent-prompts.md with 5 drift mitigations so future threads don't inherit the problems.
4. Threads 2-5 — only after Thread 1b/1c/1d close clean.

---



### Apr 21, 2026 — Mobile-breakpoint audit workstream: responsive-audit skill + POC infrastructure

**What happened:**
Opened a new workstream to systematically audit mobile responsiveness across all 48 live diagrams + 8 orphans. Spent the session (a) planning the approach with Della, (b) building the responsive-audit skill via skill-forge, (c) building project-level infrastructure (tracker, viewer, scripts), and (d) catching + surgically fixing agent drift in the generated skill files.

**Decisions made:**
- **Six breakpoints locked:** 1440, 1024, 768, 480, 375, 320 — chosen to cover desktop baseline, iPad landscape, tablet/mobile cliff, small-mobile cliff, standard iPhone, and worst-case small phone. Dropped 1201 as redundant with 1024.
- **Severity classified by file location, not CSS property:** L0 = no fix; L1 = outer fix (styles.css or case-*.html); L2 = inner fix (inside diagram-*.html); L3 = new file (`{name}-mobile.html` + Figma pairing). This was the most-contested decision and came back through a Build agent drift — first pass defined severity by CSS property type, which made classification ambiguous (a grid reflow could be L1 OR L2). Rewrote with file-location semantics so the rubric prescribes the action.
- **Mobile variant swap at 768px** via `@media` display rule on `<div class="diagram-pair">` wrapper in case study HTML. Per-diagram breakpoint override deferred (add if POC reveals need).
- **Figma pairing — partner column on the RIGHT of desktop,** same case study page, same row as the corresponding desktop diagram, newer-on-right within the mobile zone (Della's existing convention). Preserved row-per-diagram layout instead of running default tidyPage grid (which would destroy her convention).
- **One thread per case study** after POC. Each thread invokes `responsive-audit` with case study scope, reads the shared xlsx tracker, audits+fixes+pairs, updates tracker.
- **Skill lives at `CoworkWorkspace/Skills/responsive-audit/`** (production) with workspace sibling at `responsive-audit-workspace/iteration-1/` (spec + iteration history). Della caught that Build agent initially saved spec to project working folder; moved to skills workspace per convention.
- **Agent drift patterns caught and documented:** Build agent drifted on severity semantics (property-type vs. file-location), tracker path (deliverables/ vs. working/), Figma pairing shape (multi-frame vs. single), and fabricated insights in learnings.md (scheduled audits, L3 approval gate) that contradicted approved spec. All surgical-fixed; pattern logged in skill's learnings.md with mitigation (agent prompts now include "echo the rule back in your own words" step).

**What changed:**
- New skill directory: `CoworkWorkspace/Skills/responsive-audit/` (18 files)
- New workspace: `CoworkWorkspace/Skills/responsive-audit-workspace/iteration-1/`
- SKILLS-REGISTRY.md: added responsive-audit v0.1.0 entry with full dependency map
- portfolio-site/working/mobile-audit/: tracker, live-diagrams.md, threads-kickoff.md, 3 scripts, 6-width screenshots subfolders
- portfolio-site/working/diagram-viewer.html: new utility (23.8KB, dark theme, keyboard shortcuts, URL-parameterized)

**Next steps:**
1. Run skill-forge Evaluate on responsive-audit — scores skill against 7 dimensions, catches anything the surgical fix missed (~5 min agent run)
2. Run POC on case-notifications — 13 diagrams (6 live + 7 orphans), full audit → classification → L1/L2/L3 fixes → Figma pairing → tracker populated (~20 min)
3. Pause for Della's greenlight; kick off Threads 2-5 if POC holds

---



### Apr 17, 2026 — Figma Design System build (color libraries + full component system)

**What happened:**
Built a complete Figma design system from the portfolio site's CSS tokens, automated via the Figma MCP (Plugin API). This was a multi-phase effort spanning two sessions:

**Phase 1 — Color Libraries (two separate files):**
1. Created "Color Library — Original Diagram" (`XWEKhabXuVJySo1vSA392L`) with 11 color variables from the warm cream Sankey palette
2. Created "Color Library — Portfolio" (`EtO2E6kyWCrREmcsGRgVNq`) with 14 color variables from the dark portfolio theme (including rgba alpha values for text/secondary and text/tertiary)
3. Built visual swatch reference pages in both files — fills bound to actual Figma variables (not raw hex), organized by category with name and value labels
4. Added convention to CONVENTIONS.md: color libraries always get visual swatch pages with variable-bound fills
5. Walked Della through publishing both as Figma libraries (Assets panel → book icon → Publish)

**Phase 2 — Design System file (`q2FRfob7p3CQ3JpJtEz7bD`):**
1. Extracted all design tokens from `styles.css` — typography (10 roles with size/weight/tracking/line-height), spacing scale (7 values), border radii (3 values)
2. Created 3 Figma Variable Collections: Typography (26 vars), Spacing (7 vars), Radii (3 vars)
3. Created 12 Text Styles: Display, Heading 1, Heading 2, Subtitle, Body, Body/Strong, Caption, Nav Link, Label, Mono, Metric Value, Button
4. Built Foundations page with Typography Scale reference showing all 10 roles with specs and samples
5. Built 9 component sets with 130 total variants on Components page:
   - Button (45): Primary/Secondary/Ghost × sm/md/lg × Default/Hover/Pressed/Focused/Disabled
   - Input Field (18): sm/md/lg × Default/Hover/Focused/Filled/Error/Disabled
   - Badge (20): Filled/Outlined × Default/Accent/Error/Warning/Success × sm/md
   - Card (12): Default/Elevated/Full Width × Default/Hover/Focused/Disabled
   - Banner (8): Info/Success/Warning/Error × Dismissible Yes/No
   - Modal (6): sm/md/lg × Default/With Actions
   - Bottom Sheet (6): sm/md/lg × Default/With Actions
   - List Item (12): Default/With Meta/With Action × Default/Hover/Active/Disabled
   - Search Bar (3): Default/Focused/Filled

**Issues hit and fixed:**
- `combineAsVariants` error: used `createFrame()` instead of `createComponent()` — Figma requires COMPONENT children in COMPONENT_SET nodes
- `setCurrentPageAsync` error: page from failed first attempt didn't persist — fixed by creating new page
- Component set layout collapse: auto-layout (`layoutMode = "VERTICAL"`) caused all variants to stack into a tiny frame — fixed by using `layoutMode = "NONE"` with manual grid positioning
- Card and Modal variants too narrow on initial render — resized with proper min-widths (320-600px range)

**Quality verification:**
- Screenshot-verified all 9 component sets via Figma MCP
- Ran codesign delight pass checklist: type system (4 weights, tracking variation, case mixing ✓), spacing zones (tight/comfortable/generous ✓), accent color discipline (teal in 4 intentional places ✓), interactive honesty (N/A for static Figma components)
- Updated `.craft-context.md` with complete design system file reference

**Decisions made:**
- Two separate color libraries (Original Diagram + Portfolio) rather than one combined — they have completely different palettes and purposes, not light/dark modes of each other
- Component state matrix derived from existing CSS patterns: background shifts, border color changes, opacity for disabled, teal accent for focused states
- Used the codesign skill for quality calibration throughout — loaded pattern-library.md and trends.md to benchmark against Linear/Stripe/Figma standards

**Artifacts created:**
| Artifact | Location | Description |
|----------|----------|-------------|
| Color Library — Original Diagram | Figma `XWEKhabXuVJySo1vSA392L` | 11 color variables + visual swatch page |
| Color Library — Portfolio | Figma `EtO2E6kyWCrREmcsGRgVNq` | 14 color variables + visual swatch page |
| Design System — Portfolio | Figma `q2FRfob7p3CQ3JpJtEz7bD` | 3 variable collections, 12 text styles, 9 component sets (130 variants), Foundations + Components pages |
| .craft-context.md update | portfolio-site/.craft-context.md | Added Figma Design System section with full component inventory |
| CONVENTIONS.md update | CoworkWorkspace/CONVENTIONS.md | Added Figma library conventions (visual swatches, variable-bound fills) |

**Next steps:**
- Della reviews design system in Figma, adjusts text and visual details
- Publish as library (same flow as color libraries)
- Use published components to build case study frames
- Eventually sync design system changes back to portfolio site CSS (bidirectional)

---
