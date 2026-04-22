# Resume Prompt — case-notifications mobile audit (Session 3)

Paste the block below into a fresh Cowork thread to continue. Everything needed to pick up cleanly is in this prompt or referenced by path.

**Copy-paste this:**

```
Continue the case-notifications mobile-breakpoint fix work.

CONTEXT

I'm auditing 56 diagrams across my portfolio for mobile responsiveness. Session 1 (Apr 20): built the responsive-audit skill v0.1.0 via skill-forge + ran POC audit on case-notifications — 13 diagrams (6 live + 7 not-e* orphans). Delegated L2 fix phase drifted hard; only 2 of 13 came out clean.

Session 2 (Apr 21): worked not11 in main thread. CSS fix verified visually clean at 480/375/320. Discovered the skill's Figma pairing was L3-only and the "vertical stack below case study page" positioning didn't match my actual Figma file. Built responsive-audit v0.2.0 via skill-forge v0.3.0: extended Figma pairing to L2, replaced positioning with mobile-cluster-left / desktop-cluster-right row layout per my sketch. Skill Evaluate scored 2.575 (ship threshold 2.4). Not yet published to mirror.

Session 3 starts here. The first-run test of v0.2.0's Figma pairing is not11.

STATE OF TRUTH

The tracker xlsx is authoritative. Read it first:
- ~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/audit-tracker.xlsx

Current state (as of end of Session 2):
- 2 rows status=fixed: not01, not04 (both verified clean by me at 375, no Figma mobile frames yet — backfill pending)
- 11 rows status=fix_in_progress:
  - not11 — CSS fix applied + visually verified clean. Pending Figma pairing (first-run test of v0.2.0).
  - not09, not07, not06, not-e1, not-e3, not-e4, not-e5, not-e6 — still broken, need L2 rework in main thread with my per-diagram notes
  - not-e2 — reclassified L3 (flywheel → needs vertical sequence mobile variant)
  - not-e7 — reclassified L3 (sankey → needs persistent info display mobile variant)

Known tracker-data issue: rows not04 and not06 have column-shift corruption (file_path and figma_node_id cells contain True/timestamp values). Status/severity/notes columns are correct. Fix before next tracker mutation.

FIRST ACTION

Do NOT start fixing diagrams. Do these three things in order:

1. Confirm responsive-audit v0.2.0 is published to mirror:
   - Canonical: ~/CoworkWorkspace/Skills/responsive-audit/SKILL.md should show `version: 0.2.0`
   - Mirror: ~/.claude/skills/responsive-audit/SKILL.md should also show 0.2.0
   - If mirror is missing or stale, Della needs to run: bash /Users/della/CoworkWorkspace/Skills/publish-skill.sh responsive-audit
   - Do not proceed until versions match.

2. Use not11 as the first-run test of v0.2.0's Figma pairing:
   - The CSS is already applied and verified (don't re-touch the HTML)
   - Follow references/figma-pairing-convention.md exactly
   - Figma file: https://www.figma.com/design/TArUrZsBUocaAsqetjXq7V/Portfolio-%E2%80%94-Image-Inventory (case-notifications page)
   - Resolve mobile cluster anchor X per the algorithm (first run: desktop_base.x - 800)
   - Create frame named "not11-mobile" at (mobile_cluster_x, desktop_base.y), width=375
   - Do NOT run default tidyPage() on the case-study page
   - Show me the result before touching the tracker
   - If the 800px anchor default lands wrong (cluster too close to desktop, or cluster too far left), flag it — we may need to patch to v0.2.1

3. Fix the tracker corruption on not04 and not06 via openpyxl before any tracker mutation. Use scripts/tracker-helpers.py patterns.

Only after all three → move on.

ORDER OF OPERATIONS (after first action completes)

Severity-sorted, worst-first:

A. Figma work (queues up fast once v0.2.0 pattern is proven on not11):
   - not11 Figma pairing (first-run test — do first)
   - Backfill Figma frames for not01, not04 (already CSS-fixed, no mobile frame yet)

B. L2 reworks (main thread, one at a time):
   1. not09 — "very broken, 2 cols cut off, horizontals clipped"
   2. not07 — "vertical but can't scroll, content extends beyond viewport"
   3. not06 — "before/after horizontal comparison cut off at bottom"
   4. not-e1 — "cohort decay chart hierarchy messed up, unreadable"
   5. not-e3 — "strategic pillars top cut off"
   6. not-e4 — "intent matrix axis labels broken"
   7. not-e5 — "taxonomy horizontal elements hidden/cut off"
   8. not-e6 — "butterfly chart hierarchy off, hard to read"
   Each one: CSS fix → re-screenshot → visually verify at 375 → create Figma mobile frame → update tracker. Confirm with me between each.

C. L3 redesigns (main thread + my design approval):
   9. not-e2 — flywheel → vertical sequence mobile variant (new -mobile.html + diagram-pair wrapper)
   10. not-e7 — sankey → persistent info display mobile variant

Plan ~30–45 min per L2 with me in the loop. ~60–90 min per L3 (design proposal → my approval → build → Figma pair). That's ~7–10 focused hours across the 10.

KEY FILES

- Skill canonical: ~/CoworkWorkspace/Skills/responsive-audit/ (SKILL.md, references/, scripts/, evals/, learnings.md) — v0.2.0
- Project rules: ~/CoworkWorkspace/CLAUDE.md + ~/CoworkWorkspace/Get-a-job/CLAUDE.md (read both before acting)
- Path mappings: ~/CoworkWorkspace/PATH-MAPPINGS.md (read before emitting any terminal command)
- Severity rubric: ~/CoworkWorkspace/Skills/responsive-audit/references/severity-classification.md — severity is classified by WHICH FILE the fix lives in (L1 outer, L2 inside diagram HTML, L3 new mobile file)
- Figma pairing (v0.2.0): ~/CoworkWorkspace/Skills/responsive-audit/references/figma-pairing-convention.md — mobile cluster left, desktop cluster right, one base mobile frame per diagram at (mobile_cluster_x, desktop_base.y)
- L2 agent prompt (v0.2.0): ~/CoworkWorkspace/Skills/responsive-audit/references/agent-prompts.md Prompt 3 — canonical source for L2 fix semantics
- Tracker helpers: ~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/scripts/tracker-helpers.py (openpyxl atomic writes, never pandas)
- Screenshot script: ~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/scripts/screenshot-diagrams.py
- Diagram viewer (for my visual verification): ~/CoworkWorkspace/Get-a-job/portfolio-site/working/diagram-viewer.html
- Canonical L2 pattern (reference example, already fixed): ~/CoworkWorkspace/Get-a-job/portfolio-site/img/diagrams/diagram-not01-segmentation-matrix-v4.html — look at @media blocks before </style>
- Session 2's successful L2 rework: ~/CoworkWorkspace/Get-a-job/portfolio-site/img/diagrams/diagram-not11-cross-channel-v4.html — same pattern, richer (breaks hub-and-spokes absolute positioning, hides desktop SVG at mobile, inline callouts)

CRITICAL RULES (non-negotiable)

- Verify-before-claiming: render the screenshot and actually look at it before marking anything fixed. "I think it looks right" is not verification.
- Living documents: update tracker rows via openpyxl only (scripts/tracker-helpers.py). Never use pandas DataFrame.to_excel — it clobbers concurrent edits.
- No delegation for fix work. Main thread only for L2/L3 CSS/HTML edits. The v0.2.0 L2 agent prompt is correct but unproven; don't trust it with my portfolio yet.
- Figma pairing CAN use Figma MCP directly from main thread — this isn't delegation, it's a direct tool call. Pair via use_figma, not sub-agents.
- Show me diffs before claiming a fix is done.
- Pause and confirm before running scripts that modify multiple files.
- Never run default tidyPage() on a case-study Figma page. Use helperPositionMobileFrameInRow per figma-pairing-convention.md.

LESSONS FROM SESSIONS 1 + 2 (do not repeat)

Session 1 drifts (5 delegated agents, all failed in some way):
1. Build agent drifted on severity semantics (property-based vs file-location) and wrote tracker to wrong folder.
2. Evaluate agent scored against fabricated criteria.
3. Audit agent wrote tracker rows with its own column order, not the declared schema.
4. Fix agent claimed 12 diagrams done but actually edited 10, skipped all screenshots, fabricated restrictions.
5. Diagram-viewer agent hardcoded paths relative to portfolio root, forgetting the viewer lives in /working/.

Pattern: agents struggle with complex semantic rubrics, stateful multi-file operations, judgment calls, file-location reasoning, and accurate rule echo-back. Pure build-to-spec UI tasks work. Judgment-heavy work stays in main thread.

Session 2 discoveries:
6. agent-prompts.md Prompt 3 (L2) told agents to create a SEPARATE stylesheet file per breakpoint. severity-classification.md says L2 = edit inside the diagram HTML's own <style> block. Two incompatible workflows. Rewrote Prompt 3 in v0.2.0. Prompts 2 (L1) and 4 (L3) still have this property-based-severity drift plus a "pause-for-approval" drift in Prompt 4 that conflicts with l3_approval_gate=end_to_end. Flagged as KNOWN DRIFT in agent-prompts.md for v0.3.0 reconciliation.
7. v0.1.0's "mobile frames 100px below case study page" positioning didn't match Della's actual Figma file. I invented a positioning convention without looking at the real file. Lesson: pin Figma conventions to observed file state, not invented defaults. First real Figma operation on not11 will validate (or invalidate) the 800px cluster anchor.

DEFERRED TO v0.3.0

Flagged in responsive-audit/learnings.md:
- Reconcile Prompt 2 (L1) with file-location severity
- Reconcile Prompt 4 (L3) with file-location severity + end-to-end approval gate + add Figma pairing step
- data-mobile-breakpoint per-diagram override
- Empirical validation of 800px cluster anchor default

Do not touch these in Session 3 unless the not11 first-run exposes something critical. Scope this session to: publish v0.2.0 → test Figma pairing on not11 → work the remaining queue.

GREENLIGHT CHECK BEFORE STARTING

Before any action in this session, the assistant should:
1. Confirm workspace is mounted (CLAUDE.md loaded)
2. Confirm PATH-MAPPINGS.md has been read
3. Confirm v0.2.0 is published to mirror (or flag that it isn't, and show me the publish command)
4. Report the tracker current state (which rows fixed / in_progress / blocked)
5. Wait for my "go" before touching Figma or any diagram HTML
```

---

## Optional extras to paste if helpful

- Skill-forge loop output from Session 2: `~/CoworkWorkspace/Skills/responsive-audit/learnings.md` (entry dated 2026-04-21 — "v0.2.0 spec update")
- Session 2 Evaluate report (scored 2.575): in the same learnings.md entry
- Session 1 audit report: `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/reports/audit-case-notifications-2026-04-21.md`
- Original Figma sketch for the mobile cluster layout: IMG_4826.HEIC (uploaded Session 2)

---

## Session 2 artifacts recap (for context on what v0.2.0 touched)

Files changed in canonical skill dir:
- SKILL.md — version bump, Mode 1 steps 6–7 updated, sub-agent bullets, success checklist, limitations, version history
- references/config.json — pairing mode renamed, pairing description rewritten, mobile_cluster_anchor_rule added, changelog entry
- references/figma-pairing-convention.md — full rewrite (cluster layout, 6-step algorithm, new helper, backfill section, 5 failure scenarios)
- references/agent-prompts.md — Prompt 3 (L2) fully rewritten to match file-location severity + Figma pairing; KNOWN-DRIFT header added for Prompts 1, 2, 4
- learnings.md — append entry: "2026-04-21 — v0.2.0 spec update — main-thread skill-forge"

Files NOT changed (untouched in Session 2):
- Prompts 1, 2, 4 in agent-prompts.md — property-based severity drift + L3 approval-gate drift flagged but deferred
- references/severity-classification.md — already at 0.2.0 from a prior pass
- references/breakpoint-rubric.md, html-connection-pattern.md, tracker-schema.md, fix-patterns-*.md — unchanged
- scripts/ — unchanged
- evals/ — unchanged

Saved 2026-04-21 at end of Session 2.
