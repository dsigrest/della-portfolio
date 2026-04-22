# Resume Prompt — case-notifications mobile audit

Paste the block below into a fresh Cowork thread to continue the mobile-breakpoint fix work. Everything needed to pick up cleanly is either in this prompt or referenced by path.

---

## Copy-paste this:

```
Continue the case-notifications mobile-breakpoint fix work from yesterday.

CONTEXT
I'm auditing 56 diagrams across my portfolio for mobile responsiveness. Yesterday (Apr 21, 2026) we built the responsive-audit skill + project infrastructure + ran POC on case-notifications (13 diagrams: 6 live + 7 not-e* orphans). Agent delegation for the L2 fix phase produced unreliable results — only 2 of 13 diagrams came out clean on visual review. The rest need rework in the main thread, one at a time, with me verifying via diagram-viewer after each.

STATE OF TRUTH
The tracker xlsx is authoritative. Read it first:
- ~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/audit-tracker.xlsx

Per-diagram status + my verification notes are in that file. 2 rows are `fixed`, 11 rows are `fix_in_progress` with my specific feedback on what's broken. Two of the 11 are now severity 3 (L3): not-e2 (flywheel — radial, can't stack) and not-e7 (sankey — hover broken on touch, needs persistent info display).

KEY FILES
- Skill: ~/CoworkWorkspace/Skills/responsive-audit/ (SKILL.md, references/, scripts/, evals/, learnings.md)
- Project rules: ~/CoworkWorkspace/CLAUDE.md + ~/CoworkWorkspace/Get-a-job/CLAUDE.md (read both before acting)
- Severity rubric: ~/CoworkWorkspace/Skills/responsive-audit/references/severity-classification.md — severity is classified by WHICH FILE the fix lives in (L1 outer, L2 inside diagram, L3 new mobile file)
- Diagram viewer utility (for my visual verification): ~/CoworkWorkspace/Get-a-job/portfolio-site/working/diagram-viewer.html — open in Chrome, pick diagram from dropdown, hit 375 preset
- Tracker helpers (openpyxl atomic writes, never pandas): ~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/scripts/tracker-helpers.py
- Screenshot script: ~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/scripts/screenshot-diagrams.py
- Canonical L2 pattern (read for reference): ~/CoworkWorkspace/Get-a-job/portfolio-site/img/diagrams/diagram-not01-segmentation-matrix-v4.html — look at the @media blocks right before </style>

WHAT TO DO
1. Read the tracker. Sort by status — 11 diagrams have status=fix_in_progress with my notes on what's broken.
2. Work the 11 diagrams ONE AT A TIME in the main thread. No sub-agent delegation for the fix work — every agent I delegated yesterday drifted. Main thread only.
3. For each diagram:
   a. Read the HTML file (look at structure, identify why my note says it's broken)
   b. Edit the diagram's internal <style> block to fix (remove or replace the agent's prior @media rules if they're the problem; add new ones that address the specific issue in my tracker note)
   c. Re-screenshot at 480/375/320 to portfolio-site/working/mobile-audit/screenshots-fixed/{width}/{diagram-id}-FIXED.png
   d. Look at the 375 screenshot (you have vision — actually LOOK at the image) and tell me what you see
   e. Update the tracker row: status=fixed (only if visually clean) or keep fix_in_progress (if still broken)
   f. Wait for my confirmation before moving to the next diagram
4. Start with the most-broken L2 reworks first — my tracker notes on not11 and not09 say "completely broken." Fix those first, then work down from there.
5. For the 2 L3 reclassifications (not-e2 flywheel, not-e7 sankey), use the html-connection-pattern: create {name}-mobile.html, wrap existing + mobile iframe in <div class="diagram-pair"> on case-notifications.html, ensure styles.css has the display swap at 768px. Pair in Figma via MCP (same row as desktop on the case-notifications Figma page, to the right) — but ONLY after I approve the mobile design proposal first.

CRITICAL RULES (non-negotiable)
- Verify-before-claiming: render the screenshot and actually look at it before marking anything fixed. I learned yesterday that "I think it looks right" is not verification.
- Living documents: update tracker rows via openpyxl only (scripts/tracker-helpers.py). Never use pandas DataFrame.to_excel — it clobbers concurrent edits.
- No delegation for fix work. Main thread only until we regain confidence in the pattern.
- Show me diffs before claiming a fix is done. I want to see what changed in the file.
- Pause and confirm before running scripts that modify multiple files.

AGENT DRIFT LESSONS FROM YESTERDAY (5 separate failures — do not repeat)
1. Build agent drifted on severity semantics (defined by CSS property instead of file location) and wrote spec + tracker path to the wrong folder — surgical-fixed.
2. Evaluate agent scored against fabricated criteria ("HTML nesting depth," "SQL export") that weren't in the spec.
3. POC audit agent wrote tracker rows with its own column order instead of the declared schema.
4. Fix agent claimed 12 diagrams done but only edited 10, skipped screenshots for all, wrote to made-up tracker files, hallucinated a "no screenshot environment" restriction.
5. Diagram-viewer agent hardcoded paths relative to portfolio root, forgetting the viewer lives in /working/. Fixed.

Agents today struggle with: complex semantic rubrics, stateful multi-file operations, judgment calls, file-location reasoning, and echoing back rules accurately. Pure build-to-spec UI tasks work fine. When in doubt — main thread.

FIRST ACTION
Read the tracker to confirm current state. Then open diagram-not11-cross-channel-v4.html (my note: "completely broken, didn't scale, diagram on top of itself") and the 375 screenshot-fixed image for it. Report what you see structurally — don't touch anything yet. I'll greenlight the fix approach.
```

---

## Optional extras to paste if helpful

- If you want to reference the approved skill spec: `~/CoworkWorkspace/Skills/responsive-audit-workspace/iteration-1/spec.md`
- If you want to reference yesterday's audit report: `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/reports/audit-case-notifications-2026-04-21.md`
- If you want to reference the kickoff prompts for Threads 2–5 (other case studies): `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/threads-kickoff.md`

## Order of operations for the remaining work

Severity-sorted so worst-broken diagrams get fixed first (improvement most visible):

1. **not11** — "completely broken, didn't scale" (L2 rework)
2. **not09** — "very broken, 2 cols cut off, horizontals clipped" (L2 rework)
3. **not-e2** — reclassified L3 (flywheel → vertical sequence mobile variant)
4. **not-e7** — reclassified L3 (sankey → persistent info mobile variant)
5. **not07** — vertical but can't scroll (L2 rework)
6. **not-e1** — cohort decay chart hierarchy messed up (L2 rework)
7. **not-e3** — strategic pillars top cut off (L2 rework)
8. **not-e5** — taxonomy horizontal elements hidden (L2 rework)
9. **not-e4** — intent matrix axis labels broken (L2 rework)
10. **not06** — before/after scroll element cut off at bottom (L2 rework)
11. **not-e6** — butterfly chart hierarchy off (L2 rework)

Plan on roughly 30–45 min per diagram with you in the loop (screenshot → review → tweak → verify). That's 5–8 focused hours of work across the 11. Reasonable split: one session hits 5–6 L2 reworks, next session handles the 2 L3 redesigns + remaining L2s + Figma pairing.
