# Resume Prompt — case-ai ai10 + ai16 Figma polish → HTML sync

**Created:** 2026-04-22 (end of Session 22 — ai10 + ai16 deploy)
**Picks up:** after Della polishes ai10 + ai16 mobile frames in Figma
**Hands off to:** nothing — this closes the ai10/ai16 pipeline. The `.diagram-pair` embeds are already live on prod; a git push of the polished HTML ships the visual update through the existing CI → Vercel pipeline.

---

## Copy-paste this block into a fresh Cowork thread

```
SETUP
- Read ~/CoworkWorkspace/CLAUDE.md
- Read ~/CoworkWorkspace/Get-a-job/CLAUDE.md
- Read ~/CoworkWorkspace/Get-a-job/PATH-MAPPINGS.md
- Read ~/CoworkWorkspace/Get-a-job/SESSION-STATE.md
- Read ~/CoworkWorkspace/Skills/figma-to-html/SKILL.md (Skill Execution Rule — read the actual file, don't summarize)
- Read ~/CoworkWorkspace/Skills/figma-to-html/references/design-system.md (shared with html-to-figma)
- Read ~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/figma-handoff-case-ai.md (lessons 1–9 on native-layer pairing; all apply to this reverse pass)

GOAL
Translate the polish I applied in Figma for ai10 and ai16 (desktop + mobile) back into their HTML files. 4 frames → 4 HTML files. Then ship via the existing CI pipeline.

TARGETS (4 frames on Figma page 29:42 — "2. Reddit Answers MVP")
| Diagram | Desktop Figma node | Desktop HTML | Mobile Figma node | Mobile HTML |
|---|---|---|---|---|
| ai10 — Graceful Degradation | 390:2 | img/diagrams/diagram-ai10-failure-state-v4.html | 1046:8 (-420, -5262, 375×851) | img/diagrams/diagram-ai10-failure-state-v4-mobile.html |
| ai16 — A System, Not a Solution | 216:2 | img/diagrams/diagram-ai16-final-identification-v4.html | 1058:8 (-420, -467, 375×860) | img/diagrams/diagram-ai16-final-identification-v4-mobile.html |

Figma file key: TArUrZsBUocaAsqetjXq7V

WORKFLOW
1. For each of the 4 frames:
   a. get_metadata on the frame → walk layer tree, map CSS-selector layer names back to source CSS classes
   b. get_design_context on the frame → extract computed values (fills, strokes, typography, spacing, border-radius, effects)
   c. Compare against current HTML. For each delta (color, spacing, font size, border-radius, shadow, etc.), generate a targeted CSS edit. Do NOT rewrite the file.
   d. Apply edits via Edit tool, preserving animations and JS interactions in the file.
   e. Re-render the HTML at its target viewport (1280px for desktop, 375px for mobile) via Chrome MCP navigate + screenshot. Compare against the Figma frame screenshot. Confirm the delta landed.

2. After all 4 files are updated:
   a. cd ~/CoworkWorkspace/Get-a-job/portfolio-site && python3 quality-check.py → must exit 0
   b. cd ~/CoworkWorkspace/Get-a-job/portfolio-site && python3 voice-check.py → must exit 0 (if diagrams contain text changes)

3. Update audit-tracker.xlsx:
   a. For each of ai10 and ai16 rows — append " | figma_polish_applied_2026-MM-DD" to the notes column via openpyxl atomic update_row (tracker-helpers.py pattern).
   b. DO NOT change status (stays `verified`) or verify_date.
   c. DO NOT use pandas — openpyxl only, atomic writes.

4. Push (DELLA PASTES — DO NOT auto-run):
   Give Della a fenced bash block with Mac absolute paths, file-specific `git add` only (no `-A`), no inline `#` comments in the paste (they cause quoting issues):

   ```bash
   cd ~/CoworkWorkspace/Get-a-job/portfolio-site
   git status
   git add img/diagrams/diagram-ai10-failure-state-v4.html
   git add img/diagrams/diagram-ai10-failure-state-v4-mobile.html
   git add img/diagrams/diagram-ai16-final-identification-v4.html
   git add img/diagrams/diagram-ai16-final-identification-v4-mobile.html
   git add working/mobile-audit/audit-tracker.xlsx
   git commit -m "case-ai: apply Figma polish to ai10 + ai16 (desktop + mobile)"
   git push
   ```

   Watch for: mixed-workstream pollution (not-series PNGs may still be uncommitted — if Della's `git status` shows untracked or modified files outside the 5 above, flag and ask before she pushes).

5. Live verification (after CI turns green — ~2-3 min):
   a. Chrome MCP navigate to https://della-portfolio.vercel.app/case-ai.html
   b. Desktop: take screenshot at 1280, compare ai-10 and ai-16 sections against local desktop HTML.
   c. Mobile: verify swap rule fires (JS: walk CSSStyleSheet rules, find `@media (max-width: 768px)` rule applied to `.diagram-pair .mobile-variant`). Chrome window won't go below 900px — CSS-rule inspection is the fallback, not a 375px viewport resize.
   d. Fetch each of the 4 files via Chrome MCP javascript_tool (fetch with method GET, not HEAD — HEAD is blocked) and confirm byte count matches local within embed-overlay delta (~10-17B).

OUT OF SCOPE FOR THIS THREAD
- Creating NEW Figma frames (use html-to-figma for that)
- Creating NEW mobile HTML variants (the existing ones are already live)
- Running the `diagram-deploy` skill — embeds are already on prod; a git push is sufficient
- The 4 pre-existing image-fill frames (ai06 774:8, ai19 772:8, ai23 776:8, ai24 778:8) — separate future pass
- ai11 tracker drift (913:8 orphan frame) — flagged in figma-handoff-case-ai.md, not yours to fix
- not-series PNGs (NOT-03, NOT-08, NOT-14) — separate workstream; check git status but don't commit them

HARD GUARDRAILS (non-negotiable)
1. NEVER call tidyPage on Figma page 29:42. Della's desktop clusters are hand-positioned.
2. NEVER reparent, rename, or move existing Figma frames. Read-only on Figma in this direction.
3. Mac absolute paths in every terminal command — NEVER /sessions/ paths. Validate against PATH-MAPPINGS.md before emitting.
4. File-specific git add only. No `git add -A` or `git add .`. Mixed-workstream risk from not-series remains until PNGs ship.
5. No inline `#` comments inside the push-command paste block (shell quoting gotcha from Session 22).
6. Tracker writes: openpyxl atomic only, never pandas. Status stays `verified`; verify_date unchanged.
7. Targeted edits to existing HTML files. Never rewrite a file from scratch (Living Documents Rule).
8. Verify before claiming — render, screenshot, or fetch every output before telling Della it's done.

REPORT BACK
- Diff per file (what CSS changed, what stayed)
- Screenshot pairs (Figma frame vs rendered HTML) per frame — 4 pairs total
- Tracker row diff for ai10 and ai16 (notes-column append only)
- Push command block for Della to paste
- Post-push live verification: byte counts for all 4 files, swap-rule confirmation, screenshot of ai-10 and ai-16 sections on prod
- BUILD-LOG entry covering: session number, what shipped, commit SHA, any new gotchas captured to Skills/figma-to-html/references/
- SESSION-STATE.md update: move Session 22 paragraph to "Prior session", write a new Session 23 paragraph

CRASH RECOVERY
If the thread compacts mid-workflow, the next thread should:
- Re-read this file
- Read SESSION-STATE.md to see which of the 4 frames/files have been processed
- Read audit-tracker.xlsx ai10/ai16 notes to see if `figma_polish_applied_*` marker is already present
- Pick up from the first unprocessed frame
```

---

## Current state snapshot (end of Session 22)

**Live on prod (verified this session via della-portfolio.vercel.app):**
- ai10 desktop HTML — 16420B (local 16430B)
- ai10 mobile HTML — 15831B (local 15847B)
- ai16 desktop HTML — 13931B (local 13948B)
- ai16 mobile HTML — 13897B (local 13907B)

Byte deltas are embed-overlay only (Vercel injects 10-17B).

**.diagram-pair swap rule active on prod** — verified via CSSStyleSheet walk finding `@media (max-width: 768px) { .diagram-pair .desktop-variant { display: none; } .diagram-pair .mobile-variant { display: block; } }`.

**Figma state (page 29:42):**
- ai10 desktop frame `390:2` — native-layer (pre-existing)
- ai10 mobile frame `1046:8` — native-layer (Session 22 build, at -420, -5262, 375×851)
- ai16 desktop frame `216:2` — native-layer (pre-existing)
- ai16 mobile frame `1058:8` — native-layer (Session 22 build, at -420, -467, 375×860)

All 4 frames use CSS-selector layer naming → figma-to-html roundtrip will parse mechanically.

**Tracker state:** 19/19 case-ai rows `verified`. ai10 + ai16 notes contain the Session 22 marker `Step 7 of case-ai-add-ai10-ai16 pipeline`. No re-verification needed when polish is applied — status stays `verified`.

---

## Why this workflow (and not diagram-deploy)

The `.diagram-pair` embeds for ai-10 and ai-16 are already wired into `case-ai.html` and deployed to prod. The iframes point at filenames (`diagram-ai10-failure-state-v4.html`, etc.) — not frame-hashes or versioned URLs. Updating the HTML files in place and pushing will swap the rendered content on prod automatically. `diagram-deploy` creates new embeds; we don't need that. A git push through the existing CI gate (quality-check + voice-check + Lighthouse) is sufficient.

---

## Version history

- **2026-04-22** — initial. Written at the close of Session 22. 4 frames scoped (ai10 + ai16 × desktop + mobile). All 4 HTML files verified live on prod; tracker rows verified; Figma mobile frames built native-layer with CSS-selector layer naming. Next thread is the reverse-translation pass after Della's polish.
