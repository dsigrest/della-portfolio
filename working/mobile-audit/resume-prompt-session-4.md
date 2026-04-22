# Resume prompt — mobile audit, session 4+ (post-v0.3.0)

**Written:** 2026-04-21 end-of-session
**For:** any fresh Cowork thread picking up the mobile responsive audit
**Read this ENTIRE file before doing any work.** It encodes a full day of hard-won context.

---

## 1. One-time Mac setup (run before starting any thread)

If this hasn't been run yet on Della's Mac:

```bash
bash ~/CoworkWorkspace/setup-symlink-skills.sh
```

This replaces every skill's mirror copy at `~/.claude/skills/<name>/` with a symlink to the canonical at `~/CoworkWorkspace/Skills/<name>/`, kills the broken fswatch daemon, and deletes obsolete v0.2.x scripts. After running, edits to canonical are instantly live in Cowork — no publish step, no daemon, no "did I sync?" ritual.

**Confirm before proceeding:** `readlink ~/.claude/skills/responsive-audit` should return `/Users/della/CoworkWorkspace/Skills/responsive-audit/`. If not, Della runs the setup script first.

---

## 2. Identity and project rules (non-negotiable)

Della Sigrest — senior product designer, 4+ years Reddit, targeting staff-level roles at Ramp/Anthropic/Meta/Figma/OpenAI/Cursor. She's been burned multiple times by agent drift and Frankenstein fixes layered on top of each other. She wants clean scope, honest diagnostics, and no more band-aids.

**Mandatory prereq reads before any work:**
1. `/Users/della/CoworkWorkspace/CLAUDE.md` — workspace rules (voice, session protocol, verify-before-claiming, living documents, skill execution rule, terminal-command safety)
2. `/Users/della/CoworkWorkspace/Get-a-job/CLAUDE.md` — project rules (source verification, voice processing, quality checklist)
3. `/Users/della/CoworkWorkspace/PATH-MAPPINGS.md` — Mac absolute paths, required before emitting any terminal command
4. `/Users/della/CoworkWorkspace/Skills/responsive-audit/SKILL.md` — v0.3.0 skill

**Critical behavioral rules (will cause trust failure if violated):**
- **Verify before claiming.** Never say "it's done" without rendering the output, running the linter, taking the screenshot. Render PDFs to confirm page counts. Run scripts. Re-read edited files.
- **No delegation for fix work.** L2/L3 CSS/HTML edits stay on the main thread. Subagents have drifted every single time on judgment-heavy work. Build-to-spec UI tasks are the only safe delegation.
- **Living documents are additive only.** Update tracker rows atomically via `tracker-helpers.py` openpyxl. Never pandas `DataFrame.to_excel` — clobbers concurrent edits. Never regenerate a living HTML file from scratch.
- **Source verification.** Never fabricate metrics, timelines, or technical details. Check `working/planning-docs/verified-facts-registry.md` for any claim. "Increased" beats a fake "+12%".
- **Terminal command safety.** Every command shown to Della must use Mac absolute paths from PATH-MAPPINGS.md. Never `/sessions/*/mnt/...` sandbox paths.
- **Show diffs before shipping.** Before declaring a fix done, show what changed. Before committing, show git diff.

---

## 3. State of the responsive audit project

**Tracker (source of truth):** `portfolio-site/working/mobile-audit/audit-tracker.xlsx`

**Completed:**
- **case-notifications** — all 13 diagrams `status=fixed`. Tracker populated. Figma frames exist (some empty dark canvases from v0.2.0 — see Known Issues below).
  - Fixed: not01, not04, not06, not07, not09, not11, not-e1, not-e3, not-e4, not-e5, not-e6
  - L3 redesigns (new mobile HTML): not-e2 (flywheel→vertical), not-e7 (sankey→persistent info)

**Remaining case studies (in recommended order):**

| Case study | Figma page | Page ID | Diagram count | Audit state |
|---|---|---|---|---|
| case-subreddit | "4. Subreddit success" | `29:40` | 10 | **Audit complete** — 10 L2 classifications pre-computed, ready for fix phase |
| case-sharing | "3. Sharing & embeds" | `29:41` | 8 | Fresh — needs full audit |
| case-ai | "2. Reddit Answers MVP" | `29:42` | 19 | Fresh — needs full audit |
| case-building-portfolio | "5. Building this portfolio" | `29:2` | TBD | Fresh — needs full audit |

**Pre-computed case-subreddit audit (sub01–sub12, all L2):**

| ID | Root cause | Fix |
|---|---|---|
| sub01 survival-curve | Pattern B — `.chart-area { height: 200px }` fixed-height container, SVG `xMidYMid meet` shrinks into empty space; SVG text (9-10px in 660-unit viewBox) unreadable | `aspect-ratio: 660/200`; bump SVG label font-sizes at @480/320 |
| sub02 lifecycle-framework | Pattern C — 5-stage horizontal row doesn't collapse; cards clip right at mobile | Collapse stage row to vertical at @768; tighten card padding |
| sub03 milestone-model | Pattern D — `.stage-card` is flex with `.card-body` + fixed-width `.impact-section` on right; at 375 impact pips crowd title | Stack card contents vertically at @480; move impact row below tags |
| sub04 strategic-starting-points | Pattern C — 2-column `.bets-grid` (infrastructure \| component bet) doesn't collapse; right card clips | Collapse grid to 1 col at @768 |
| sub05 artifact-alignment | Pattern C — 2×2 grid of 4 cards doesn't collapse; right column clips | Collapse grid to 1 col at @768 |
| sub06 threshold-calibration | Pattern B — chart area fixed height; survival curve + column bars + stage tiles. Bottom stage grid reflows OK (3+2). Chart + legend crowd | `aspect-ratio` on chart box; stack chart header legend; keep stage card grid as-is |
| sub08 creation-after | Minor — 3-step flow header (Identity → Visual → Preview) wraps to 2 rows at 375/320, orphan arrows | Hide arrows below 480 OR stack header items vertically |
| sub09 distribution-loop | Pattern C — 3-card flex row (Share/Engage/Trust) doesn't stack; "No entry point" callout fine once cards stack | Collapse `.loop-nodes` to 1 col at @768; hide curved SVG arrows at mobile |
| sub11 text-bars | Pattern C — 3-card grid (Priority Order / Visible Progress / Direct Navigation) doesn't stack; right card clips | Collapse grid to 1 col at @768 |
| sub12 instrumentation-heatmap | Works at 480, clips at 320 only — 6-col heatmap needs tighter cell padding/font at 320 | Tighten cell padding + font at @375/320; legend collapse to stack |

**Capture artifact to ignore (sub03):** Playwright full-page capture didn't trigger `.reveal` IntersectionObserver on last-in-DOM cards at 375 — capture-time only, not a real mobile bug. Post-fix Chrome MCP captures will show real user view.

**Figma page state for case-subreddit:** 59 children (10 SUB-XX desktop bases + 11 variants + 18 spec frames at x=-334 + stickies). Leftmost child x=-334. Per old v0.2.1 algorithm, mobile cluster would be at x=-1634. But v0.3.0 does NOT do Figma pairing itself — html-to-figma handles it.

---

## 4. How the v0.3.0 workflow runs

responsive-audit v0.3.0 does assess + fix + comparison tracker only. Figma is a separate skill. See `Skills/responsive-audit/SKILL.md` for the full pipeline diagram.

**Per case study:**

1. **CAPTURE at 6 breakpoints via Chrome MCP** (not sandbox Playwright — see §5 Known Issues)
   - Read `Skills/responsive-audit/references/chrome-mcp-capture.md` for the navigate → resize → screenshot flow
   - Save to `portfolio-site/working/mobile-audit/screenshots/{width}/{case-study}/{diagram-id}.png`
   - Force `document.body.classList.add('embedded')` before screenshot to strip standalone page chrome

2. **CLASSIFY each failure by file location** (read `Skills/responsive-audit/references/severity-classification.md`):
   - **L0** — renders correctly at all breakpoints, no fix
   - **L1** — fix in `styles.css` or `case-*.html` (outer container)
   - **L2** — fix inside `diagram-*.html`'s own `<style>` block
   - **L3** — new `*-mobile.html` + `diagram-pair` wrapper
   - Check `Skills/responsive-audit/references/common-l2-failure-patterns.md` Patterns A–F first — they cover ~80% of L2 failures

3. **FIX** in the canonical file per severity
   - L2: edit inside the diagram's `<style>` block only. No new files. No styles.css changes. No DOM changes.
   - L3: write new `{name}-mobile.html`, wrap original + mobile in `<div class="diagram-pair">`, confirm swap rule in styles.css

4. **VERIFY via re-capture** at 480/375/320 with Chrome MCP
   - Save to `working/mobile-audit/screenshots-fixed/{width}/{case-study}/{diagram-id}-FIXED.png`
   - Visually inspect each PNG (actually look at it — don't estimate from CSS)
   - If not clean, iterate before claiming fixed

5. **TRACKER UPDATE** via `tracker-helpers.py`
   - Set `status=fixed`, `verify_date=today`, `ok_480/ok_375/ok_320=True`, `root_cause` and `fix_strategy` strings
   - Atomic openpyxl only — NEVER pandas
   - File is at `portfolio-site/working/mobile-audit/audit-tracker.xlsx`

6. **GENERATE COMPARISON TRACKER**
   ```
   cd portfolio-site
   python3 ../Skills/responsive-audit/scripts/comparison-tracker.py --case-study case-{slug}
   ```
   Output: `working/mobile-audit/comparison-tracker-{slug}-{date}.html` — self-contained, inlined PNGs, before/after pairs with approve/reject/skip UI. Show Della the file path.

7. **HAND OFF TO html-to-figma** (see `Skills/responsive-audit/references/handoff-to-html-to-figma.md`)
   - ONLY after Della approves the comparison tracker
   - Payload: `{ case_study_slug, target_figma_page, figma_file_key: "TArUrZsBUocaAsqetjXq7V", diagrams: [...] }`
   - Invoke html-to-figma skill. Do NOT call `use_figma` directly. Do NOT create Figma frames from this skill.
   - html-to-figma renders each mobile HTML into its Figma frame on the target page, mobile cluster column

That's it for responsive-audit's job. Della polishes in Figma → figma-to-html roundtrips → diagram-deploy ships.

---

## 5. Known issues and gotchas (learned the hard way)

### Sync was breaking all day
Before the setup-symlink-skills.sh ran, publishing to `~/.claude/skills/` was brittle. If you see "skill not found" or stale version, stop and tell Della to run the setup script. Do NOT attempt `publish-skill.sh` — the symlink approach makes it unnecessary.

### Sandbox Playwright is a dead end
Do NOT attempt `pip install playwright` or `python3 -m playwright install chromium` in the sandbox. Chromium needs ~400MB, sandbox has ~180MB free. v0.2.x hit this repeatedly. v0.3.0 uses Chrome MCP specifically to avoid it. `scripts/screenshot-diagrams.py` is retained as fallback but only Della runs it on her Mac, never the skill.

### figma.base64Decode has a bug on rendered JPEGs
If you somehow end up trying to pass a base64 JPEG to Figma's plugin runtime (shouldn't happen in v0.3.0 since html-to-figma handles rendering), it will reject valid JPEG strings as "Invalid base64". Use `figma.createImage(bytes)` with a Uint8Array or don't do image fills at all.

### Agent delegation drifts
Every sub-agent invoked for judgment-heavy work today drifted. Stay on main thread for: audit classification, CSS fixes, tracker updates, comparison tracker generation, html-to-figma handoff decisions. Safe to delegate: pure build-to-spec UI tasks with unambiguous acceptance criteria.

### case-notifications has 13 empty Figma frames from v0.2.0
Before v0.3.0, responsive-audit created empty dark-canvas Figma frames. Those frames still exist on page "1. Notifs & Inbox" but lack content. Fix when Della has time: delete them and re-invoke html-to-figma with the case-notifications diagram list. Or just leave them — they'll get re-populated next time she runs the pipeline end-to-end on notifs.

### Known drift in agent-prompts.md
Prompts 1 (audit), 2 (L1), 4 (L3) still have v0.1.0 property-based-severity language (CSS type classification). Prompt 3 (L2) was rewritten for v0.3.0. When following Prompts 1/2/4, treat `severity-classification.md` as source of truth and ignore the property-based descriptions. Tracked for v0.3.1 cleanup.

### Don't use old case-study resume prompts
Earlier today I generated per-case-study prompt templates that assumed v0.2.x semantics (directly calling `use_figma`, passing base64 JPEGs, etc.). Those are outdated. Use this document as the canonical resume prompt for all remaining case studies.

---

## 6. Starting a case study

After the setup script has run and you've read the mandatory prereqs (§2), use this canonical prompt pattern:

> Run responsive-audit v0.3.0 on [case-slug]. Read the resume prompt at `portfolio-site/working/mobile-audit/resume-prompt-session-4.md` first — it has the full state, rules, and known gotchas. Follow the v0.3.0 workflow (capture via Chrome MCP, classify, fix, comparison tracker, handoff to html-to-figma). Main thread only for fix work. Show diffs before claiming fixed.

**For case-subreddit specifically:** audit is pre-computed (§3). Skip the capture-and-classify phase. Go straight to fix phase using the provided classification table. Still capture before/after screenshots (Chrome MCP) so the comparison tracker works.

---

## 7. Key file paths (Mac absolute, for terminal commands)

| What | Path |
|---|---|
| Canonical skill | `/Users/della/CoworkWorkspace/Skills/responsive-audit/` |
| Mirror (symlink) | `/Users/della/.claude/skills/responsive-audit/` |
| Setup script | `/Users/della/CoworkWorkspace/setup-symlink-skills.sh` |
| Portfolio repo | `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/` |
| Tracker | `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/audit-tracker.xlsx` |
| Tracker helpers | `/Users/della/CoworkWorkspace/Skills/responsive-audit/scripts/tracker-helpers.py` |
| Comparison tracker generator | `/Users/della/CoworkWorkspace/Skills/responsive-audit/scripts/comparison-tracker.py` |
| Screenshots (before) | `portfolio-site/working/mobile-audit/screenshots/{width}/{case-study}/{diagram-id}.png` |
| Screenshots (after) | `portfolio-site/working/mobile-audit/screenshots-fixed/{width}/{case-study}/{diagram-id}-FIXED.png` |
| Figma file key | `TArUrZsBUocaAsqetjXq7V` (Portfolio — Image Inventory) |
| html-to-figma skill | `/Users/della/CoworkWorkspace/Skills/html-to-figma/` v1.0.0 |
| figma-to-html skill | `/Users/della/CoworkWorkspace/Skills/figma-to-html/` |
| diagram-deploy skill | (check `Skills/SKILLS-REGISTRY.md` if needed) |

---

## 8. Session history (so you know what's been tried)

- **Session 1 (Apr 20):** responsive-audit v0.1.0 built, POC audit ran on case-notifications. 5 delegated agents all drifted. Lesson: judgment-heavy work = main thread only.
- **Session 2 (Apr 21 morning):** v0.2.0 shipped via skill-forge. Figma pairing extended to L2, mobile-cluster-left positioning. not11 fix verified clean at 375.
- **Session 3 (Apr 21 afternoon):** v0.2.0 first-run on case-notifications. All 13 diagrams fixed, 2 L3 redesigns (not-e2 flywheel → vertical, not-e7 sankey → persistent info). Discovered v0.2.0 anomalies → patched to v0.2.1 mid-session. Then Della pushed back on the scope and the sync pain. v0.2.1 → v0.3.0 scope rewrite.
- **Session 3 end:** v0.3.0 shipped — scope narrowed, Chrome MCP capture, comparison tracker, html-to-figma handoff. Symlink-based skill sync replaces publish-skill.sh + fswatch daemon. This resume doc written.

---

## 9. If things go wrong

- **Skill appears missing from mirror:** run `bash ~/CoworkWorkspace/setup-symlink-skills.sh` again. Should be idempotent.
- **Chrome MCP not available:** stop and tell Della. Don't fall back to Playwright in sandbox. She can run `scripts/screenshot-diagrams.py` on her Mac as emergency alternative.
- **html-to-figma skill errors:** check `Skills/html-to-figma/SKILL.md` for current interface. The handoff contract in `handoff-to-html-to-figma.md` is responsive-audit's view; html-to-figma's own SKILL.md is authoritative.
- **Tracker row corruption (columns shifted):** symptom is cells containing `True`/`'fixed'`/date strings instead of their proper column values. Fix via openpyxl direct cell assignment (see Session 3 fix for not04/not06 in BUILD-LOG.md for the pattern).

---

End of resume doc. Any fresh thread reading this should have everything needed to pick up the remaining 4 case studies without losing context.
