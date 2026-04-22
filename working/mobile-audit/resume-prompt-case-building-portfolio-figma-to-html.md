# Resume Prompt — case-building-portfolio Figma → HTML → Deploy

**Created:** 2026-04-22 end of Session 10 (case-building-portfolio Figma pairing shipped).
**Picks up:** Fresh Cowork thread, **after** Della has polished the 5 mobile Figma frames.
**Hands off to:** Nothing — this closes the case-building-portfolio mobile loop fully (HTML reflects Figma polish, live site deployed, tracker stamped).

**Scope:** All 5 mobile frames for case-building-portfolio (port-01b, port-02c, port-03a, port-04a, port-05). Della edits the Figma frames natively (typography, spacing, color, component refinements); this thread flows those edits back to HTML via `figma-to-html`, verifies locally, then confirms live-site state via `diagram-deploy` (the embeds are already wired — this is a "deploy current HTML" pass, not a "wire up placeholders" pass).

---

## Copy-paste this block into a fresh Cowork thread

```
Translate Della's polish on the 5 case-building-portfolio mobile Figma frames back to HTML, verify the result, then confirm the live site is current. All 5 Figma mobile frames were created native in Session 10 (Apr 22, 2026) and are now editable. Della polishes in Figma; this thread reads the polish and writes it to HTML.

SETUP (read in order):
1. Read Get-a-job/SESSION-STATE.md (case-building-portfolio section) + Get-a-job/portfolio-site/working/mobile-audit/audit-tracker.xlsx to ground current state. Tracker is authoritative. All 5 port-* rows are `status=verified`, `verify_date=2026-04-22`, `figma_mobile_node_id` populated.
2. Read Get-a-job/portfolio-site/working/mobile-audit/reports/figma-handoff-case-building-portfolio.md — full frame table with nodeIds, scope expansion history, skill-patch recommendations. This is the canonical handoff brief; THIS file (resume-prompt) is the workflow wrapper.
3. Invoke /figma-to-html. Read SKILL.md + any references/ + scripts/. Skill Execution Rule applies — do NOT paraphrase. Mode A (page URL batch) is the default; Della will paste the page URL for "5. Building this portfolio" in file TArUrZsBUocaAsqetjXq7V.
4. Read Get-a-job/CLAUDE.md and CoworkWorkspace/CLAUDE.md — voice, Verify Before Claiming, Skill Execution Rule, Living Documents Rule (tracker writes via tracker-helpers.py openpyxl only; notes append with `|` separator; NEVER rewrite), Figma Plugin tidyPage rule (NEVER tidyPage on case-study pages in file TArUrZsBUocaAsqetjXq7V — Della's clusters are hand-positioned).
5. If deploy step is needed, invoke /diagram-deploy and read SKILL.md. For case-building-portfolio, all 5 embeds are already live in case-building-portfolio.html — this is a "verify + push HTML changes" pass, not a "wire up placeholders" pass.

TARGETS
- Figma file key: TArUrZsBUocaAsqetjXq7V
- Page: "5. Building this portfolio"
- Mobile cluster anchor: x=-1325 (same y as each diagram's desktop counterpart)

Frame → HTML mapping (this is the critical bit — port-04a is special):

| Frame | Figma nodeId | HTML file to update | Note |
|---|---|---|---|
| port-01b-mobile | 849:14 | img/diagrams/diagram-port01b-insights.html | single-file responsive; polish lands in the @media (max-width: 680px) block |
| port-02c-mobile | 849:35 | img/diagrams/diagram-port02c-research-synthesis-v4.html | single-file responsive; polish lands in @media (max-width: 480px) + (max-width: 375px) blocks |
| port-03a-mobile | 838:14 | img/diagrams/diagram-port03a-thumbnails-v4.html | single-file responsive; polish lands in @media (max-width: 480px) + (max-width: 375px) blocks |
| port-04a-mobile | 852:14 | img/diagrams/diagram-port04a-governance-v4-mobile.html | SEPARATE MOBILE FILE (L3 — linear-vertical redesign); polish lands in the full file, not a media-query block. The -v4.html desktop file is out of scope. |
| port-05-mobile | 852:95 | img/diagrams/diagram-port05-recruiter-panel-v4.html | single-file responsive; polish lands in @media (max-width: 680px) + (max-width: 480px) + (max-width: 375px) blocks |

WORKFLOW
1. Della pastes the Figma page URL. figma-to-html Mode A fetches metadata, runs frame resolution (rightmost-in-row), detects which frames have changes vs. the current HTML, and translates diffs per frame.
2. For port-01b/02c/03a/05 (single-file responsive): changes go INTO the relevant @media block. Do NOT overwrite the desktop styles — only add/modify rules inside the mobile media queries. If Della's polish is structural (e.g., she moved an element in a way that can't be expressed via @media override), flag it rather than guessing.
3. For port-04a: changes go into the standalone `-v4-mobile.html` file. The desktop `-v4.html` is a separate diagram and out of scope for this pass.
4. After each translation, re-read the changed file to confirm the diff landed correctly (Verify Before Claiming rule).
5. Local verification: Della runs `python3 working/mobile-audit/scripts/screenshot-diagrams.py case-building-portfolio` on her Mac. Compare fresh screenshots against the polished Figma frames — call out any drift.
6. Tracker update (atomic, openpyxl via scripts/tracker-helpers.py): for each row that received polish, append to the notes column with `|` separator: "figma_polish_applied_2026-MM-DD". Do NOT change status, verify_date, or figma_mobile_node_id (row stays `verified`).
7. Deploy confirmation: all 5 diagrams are already embedded in portfolio-site/case-building-portfolio.html (verified Session 10). No new diagram-embed wiring needed. Invoke /diagram-deploy only if a new embed is added or if the embed format changes (not expected). Otherwise, skip diagram-deploy — the HTML files are the live source; `git push` ships them.
8. BUILD-LOG append: one paragraph matching the Session 10 tone, describing what polish was applied + any surprises.

OUT OF SCOPE — do not touch
- portfolio-site/case-building-portfolio.html — `.diagram-pair` wrapper for port-04a is live; other 4 are single iframes pointing at the responsive files. No embed changes needed.
- portfolio-site/styles.css — `.diagram-pair` swap rule at 768px is live; don't modify unless Della explicitly asks.
- img/diagrams/diagram-port04a-governance-v4.html — desktop L0 file, out of scope for mobile polish.
- audit-tracker.xlsx status column — rows are `verified`; don't flip status. Only append to notes.
- Other case studies (ai, subreddit, sharing, notifications) — out of scope.
- responsive-audit skill — no spec changes.
- html-to-figma skill — the patch recommendations from Session 10 (see handoff brief) belong in a separate skill-iteration thread, not this one.

CRASH / CONTEXT GUARDRAILS
- Don't regenerate the Figma mobile frames from scratch — they're already native. figma-to-html reads FROM Figma, writes TO local HTML.
- Don't touch the desktop port-* frames in Figma — this is mobile-only.
- Don't run responsive-audit — audit phase is done, tracker is final.
- Don't rewrite any diagram HTML file from scratch; apply targeted edits only.
- If figma-to-html errors three times on the same call, stop and report rather than falling back to a slower approach.
- Terminal commands for Della must use Mac absolute paths (/Users/della/CoworkWorkspace/...), never /sessions/... (PATH-MAPPINGS.md).

REPORT BACK
- Per-diagram summary: what polish was detected, what HTML edit was made, file diff size.
- Screenshots (or Figma MCP get_screenshot + local render comparison) showing each updated frame matches the Figma source.
- Tracker row diffs (notes column only — status/verify_date/node_id unchanged).
- BUILD-LOG paragraph appended.
- Terminal commands (Mac paths) for Della to commit + push the HTML changes, tracker, and BUILD-LOG.

Start with whichever frame Della polished least (smallest diff) — use it as the quality test. If that goes clean, batch the rest. If Della only polished a subset, translate only those — figma-to-html's rightmost-in-row algorithm will surface which ones changed.
```

---

## State of truth (fresh thread must trust this)

### Scope table

| Frame | Figma nodeId | Anchor (x, y, w×h) | HTML target | Edit target within file |
|---|---|---|---|---|
| port-01b-mobile | `849:14` | `-1325, 320, 375×674` | `portfolio-site/img/diagrams/diagram-port01b-insights.html` | `@media (max-width: 680px)` block |
| port-02c-mobile | `849:35` | `-1325, 3970, 375×635` | `portfolio-site/img/diagrams/diagram-port02c-research-synthesis-v4.html` | `@media (max-width: 480px)` + `@media (max-width: 375px)` blocks |
| port-03a-mobile | `838:14` | `-1325, 6350, 375×765` | `portfolio-site/img/diagrams/diagram-port03a-thumbnails-v4.html` | `@media (max-width: 480px)` + `@media (max-width: 375px)` blocks |
| port-04a-mobile | `852:14` | `-1325, 9354, 375×954` | `portfolio-site/img/diagrams/diagram-port04a-governance-v4-mobile.html` | Full file (separate mobile variant — L3 linear-vertical redesign; swapped in via `.diagram-pair` at 768px) |
| port-05-mobile | `852:95` | `-1325, 10607, 375×941` | `portfolio-site/img/diagrams/diagram-port05-recruiter-panel-v4.html` | `@media (max-width: 680px)` + `@media (max-width: 480px)` + `@media (max-width: 375px)` blocks |

### Figma target

| Field | Value |
|---|---|
| File key | `TArUrZsBUocaAsqetjXq7V` (Portfolio — Image Inventory) |
| Page name | "5. Building this portfolio" |
| Mobile cluster anchor | x = −1325 (same y as each diagram's desktop counterpart) |

### Deploy target (already wired)

All 5 diagrams are embedded in `portfolio-site/case-building-portfolio.html`:

- port-01b, port-02c, port-03a, port-05: single `<iframe>` inside `.case-img-full.diagram-embed` (single responsive file serves both desktop and mobile via `@media`).
- port-04a: `.diagram-pair` wrapper with two `<iframe>` children (`.desktop-variant` pointing at `-v4.html`, `.mobile-variant` pointing at `-v4-mobile.html`). Swap fires at 768px via `styles.css` (lines 370–377, existing rule — don't touch).

Because embeds are already live, **`diagram-deploy` is a no-op for this handoff** unless Della adds a new diagram or changes the embed format. The figma-to-html pass is the substantive work; `git push` of the updated HTML files ships the polish to the live site on Vercel.

### Tracker schema reminder

`portfolio-site/working/mobile-audit/audit-tracker.xlsx` (use `scripts/tracker-helpers.py`):
- `diagram_id` — e.g., `port-01b`
- `figma_mobile_node_id` — already populated (don't change)
- `status` — all 5 rows at `verified` (don't change)
- `verify_date` — `2026-04-22` (don't change)
- `notes` — APPEND with `|` separator: `"figma_polish_applied_YYYY-MM-DD"` (or more descriptive if polish was substantive)

### Where things live on Della's Mac (for terminal commands)

Repo root: `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/`

Typical post-translation commit:
```bash
cd /Users/della/CoworkWorkspace/Get-a-job/portfolio-site/
git add img/diagrams/diagram-port01b-insights.html \
        img/diagrams/diagram-port02c-research-synthesis-v4.html \
        img/diagrams/diagram-port03a-thumbnails-v4.html \
        img/diagrams/diagram-port04a-governance-v4-mobile.html \
        img/diagrams/diagram-port05-recruiter-panel-v4.html \
        working/mobile-audit/audit-tracker.xlsx
git add ../BUILD-LOG.md ../SESSION-STATE.md  # if updated
git commit -m "case-building-portfolio: apply Figma polish to 5 mobile diagrams"
git push origin main
```

(Only include the files that actually changed — if Della only polished port-02c, stage only that diagram's HTML + the tracker + logs.)

---

## Session 10 context the fresh thread should know

**What Session 10 did:**
- Ran `html-to-figma` native translation on all 5 port-* diagrams (not image-fill).
- All 5 frames are editable Figma layers with CSS-selector layer names (e.g., `.insight-num`, `.score-card.top-scorer`, `.tab-bar .tab:nth(3)`).
- Auto-layout hierarchy: root frame is VERTICAL auto-layout, `primaryAxisSizingMode=AUTO` (hugs height), `counterAxisSizingMode=FIXED` (width locked at 375). All nested frames FILL horizontal, HUG vertical.
- No `tidyPage` run — case-study pages use hand-curated cluster anchors.

**Two known translator quirks (relevant if figma-to-html roundtrips surface similar issues):**
1. `layoutSizingHorizontal` / `layoutSizingVertical` can silently drop to `FIXED` during `appendChild`. Reassert after every append if building new auto-layout structure.
2. TEXT nodes don't expose `layoutMode`. Any tree walker must guard with `'layoutMode' in n && n.layoutMode !== 'NONE'`.

Both are documented in the BUILD-LOG Session 9 entry and in `figma-handoff-case-building-portfolio.md` § Skill patch recommendations.

**What to expect on the figma-to-html side:**
- Della's polish will typically be typography scale, color token shifts, padding/gap tweaks, and alignment adjustments. These map cleanly to @media block edits in the 4 responsive files.
- For port-04a (L3 standalone mobile), polish could be more structural — linear-vertical sequence, connector widths, branch split geometry. Read the full file before editing to understand what changes are in scope.
- If Della's polish moves a frame in a way that can't be expressed via @media override on the existing desktop file (e.g., she changes the desktop-layout assumption), flag it to her before editing — the responsive pattern is "desktop is default, mobile overrides," not "two independent layouts."
