# Resume Prompt — case-ai Figma Pairing Refresh

**Created:** 2026-04-22 end of Session 9 (case-ai mobile completion shipped).
**Picks up:** Fresh Cowork thread, Figma pairing refresh for ai06 + ai19.
**Hands off to:** Nothing — this closes the case-ai mobile audit fully (all 19 rows `verified`, all Figma frames aligned with live HTML).

**Scope is narrower than a typical "pair ALL diagrams" thread.** Only 2 frames (ai06 @ 774:8, ai19 @ 772:8). ai23 is already paired from Session 4. ai24 is out of scope.

---

## Copy-paste this block into a fresh Cowork thread

```
Refresh the Figma mobile frames for ai06 and ai19 so the Figma canvas matches the native-CSS-grid HTML shipped in Session 9. The existing frames hold JPEG image fills from the Session 4 render — they render correctly but can't be edited natively in Figma. This thread replaces those image fills with native Figma layers while preserving the image-fill versions as backups.

SETUP (read in order):
1. Read Get-a-job/SESSION-STATE.md (case-ai section, lines ~100–125) + Get-a-job/portfolio-site/working/mobile-audit/audit-tracker.xlsx to ground current state. Tracker is authoritative over SESSION-STATE. All 4 case-ai Figma frames have `figma_mobile_node_id` populated from Session 4; ai06/ai19/ai23 are `status=verified` (2026-04-22); ai24 is also verified (earlier in Session 6).
2. Read Get-a-job/portfolio-site/working/mobile-audit/resume-prompt-case-ai-figma-pairing.md (THIS FILE — state of truth + scope tables below the code block). No separate figma-handoff-case-ai.md exists; this pickup doc IS the handoff.
3. Invoke /html-to-figma. Read SKILL.md + any references/ + scripts/. Skill Execution Rule applies — do NOT paraphrase. Mode: node replacement (refreshing existing frames at 774:8 and 772:8, not creating new frames).
4. Read CoworkWorkspace/Skills/responsive-audit/references/figma-pairing-convention.md v0.2.1 — cluster-left anchor convention (x=-420 for case-ai), Y-align to desktop row, naming. Both target frames already exist at the correct (x,y); this thread only replaces their fills.
5. Read Get-a-job/CLAUDE.md and CoworkWorkspace/CLAUDE.md — voice, verify-before-claiming, Skill Execution Rule, Living Documents Rule (tracker writes via tracker-helpers.py openpyxl only, notes preserved with `|` separator), Figma Plugin tidyPage rule. NEVER tidyPage on case-study pages in file TArUrZsBUocaAsqetjXq7V — Della's desktop clusters are hand-positioned. Add/refresh mobile frames at x=-420; leave everything else alone.

TARGETS
- Figma file key: TArUrZsBUocaAsqetjXq7V
- Page: "2. Reddit Answers MVP" (node 29:42)
- ai06 → node 774:8, source HTML portfolio-site/img/diagrams/diagram-ai06-evaluation-matrix-v4-mobile.html, anchor x=-420 y=-8774, frame dims 375×462
- ai19 → node 772:8, source HTML portfolio-site/img/diagrams/diagram-ai19-attribution-comparison-v4-mobile.html, anchor x=-420 y=1643, frame dims 375×169

WORKFLOW
1. For each frame, preserve the existing image fill as a backup sibling node named `ai06-mobile-imageref` / `ai19-mobile-imageref`. Do NOT delete the image fill before native layers are in and verified.
2. Replace the target frame's image fill with native Figma layers built from the HTML via html-to-figma. Layer names use CSS selectors per html-to-figma convention.
3. Byte-array transport only. `atob()` fails in the Figma plugin runtime (validated case-notifications + case-ai Session 4). Use raw `Uint8Array` of JPEG bytes inline for any image passes.
4. Visually verify each refreshed frame via Figma MCP screenshot — compare against the HTML render at 375 width. If colors, spacing, or typography drift from the HTML in a way Della would catch, stop and report. Do not ship a drifted frame.
5. Tracker update (atomic, openpyxl via scripts/tracker-helpers.py): update_row for ai06 and ai19 — append a note to the existing notes column using `|` separator: "figma_refreshed_to_native_layers_2026-MM-DD". Do NOT change status, verify_date, or figma_mobile_node_id.
6. Append a short entry to portfolio-site/BUILD-LOG.md describing what changed. One paragraph, matching the tone of the Apr 22 Session 9 entry.

OUT OF SCOPE — do not touch
- Any HTML file in img/diagrams/*-v4-mobile.html — done, verified, live.
- case-ai.html — `.diagram-pair` wrappers are live and correct.
- styles.css — `.diagram-pair` swap rule at lines 370–377 is live.
- audit-tracker.xlsx status column — rows are `verified`; don't flip status.
- ai24 (node 778:8) — out of scope.
- ai23 (node 776:8) — out of scope unless html-to-figma flags drift.
- Other case studies — out of scope.
- Responsive-audit skill — no spec changes.

CRASH / CONTEXT GUARDRAILS
- Don't read case-ai.html or any -v4.html desktop diagram file (they're large and not needed).
- Don't regenerate mobile-breakpoint screenshots of case-ai — visual verification was completed Session 9.
- Don't run responsive-audit Mode 1 — audit phase is done, tracker is final.
- Don't re-translate HTML→Figma from scratch if the frame already has native layers — reconcile drift only, no destructive replace.
- If html-to-figma errors three times on the same call, stop and report rather than falling back to a slower approach.
- Terminal commands for Della must use Mac absolute paths (/Users/della/CoworkWorkspace/...), never /sessions/... (PATH-MAPPINGS.md).

REPORT BACK
- Figma MCP screenshots of both refreshed frames (ai06 and ai19) with native layers.
- Tracker row diff for ai06 and ai19 (notes column only — status/verify_date/node_id unchanged).
- BUILD-LOG paragraph appended.
- Terminal commands (Mac paths) for Della to commit and push the tracker + BUILD-LOG changes.

Start with ai19 — it's the smaller frame (375×169) and faster to verify. If ai19 goes clean, ai06 (375×462) uses the same pattern.
```

---

## State of truth (fresh thread must trust this)

### Scope table

| Diagram | HTML source | Figma target node | Anchor (x, y, w×h) | Image-fill backup name |
|---|---|---|---|---|
| ai06 — Evaluation Matrix | `portfolio-site/img/diagrams/diagram-ai06-evaluation-matrix-v4-mobile.html` | `774:8` | `-420, -8774, 375×462` | `ai06-mobile-imageref` |
| ai19 — Attribution Comparison | `portfolio-site/img/diagrams/diagram-ai19-attribution-comparison-v4-mobile.html` | `772:8` | `-420, 1643, 375×169` | `ai19-mobile-imageref` |

### Figma target

| Field | Value |
|---|---|
| File key | `TArUrZsBUocaAsqetjXq7V` (Portfolio — Image Inventory) |
| Page name | "2. Reddit Answers MVP" |
| Page node ID | `29:42` (also appears as `301:2` in some queries — same canvas, different traversal) |
| Mobile cluster anchor x | `-420` (locked Session 4 via v0.2.1 algorithm: `leftmost_child.x − 1300 = 880 − 1300`) |
| Mobile frame width | 375 |
| Mobile frame Y | same row as desktop base frame (already set; do not move) |

### Tracker state (before this thread runs)

All 4 case-ai L2/L3 rows have `figma_mobile_node_id` populated from Session 4. All are `status=verified, verify_date=2026-04-22`. This thread only modifies the **notes** column on ai06 and ai19:

| diagram_id | status | verify_date | figma_mobile_node_id | Notes change |
|---|---|---|---|---|
| ai06-evaluation-matrix | verified | 2026-04-22 | 774:8 | Append `\| figma_refreshed_to_native_layers_2026-MM-DD` |
| ai19-attribution-comparison | verified | 2026-04-22 | 772:8 | Append `\| figma_refreshed_to_native_layers_2026-MM-DD` |
| ai23-trust-comparison | verified | 2026-04-22 | 776:8 | — (already native, out of scope) |
| ai24-clarity-spectrum | verified | 2026-04-22 | 778:8 | — (out of scope per Della) |

### What Session 9 produced (inputs to this thread)

- `portfolio-site/img/diagrams/diagram-ai06-evaluation-matrix-v4-mobile.html` — **new** native CSS grid, 4-prompt vertical stack, preserves winner column highlight
- `portfolio-site/img/diagrams/diagram-ai19-attribution-comparison-v4-mobile.html` — **new** compact 2-row header + 3-col status grid
- `portfolio-site/case-ai.html` — `.diagram-pair` wrappers added for `ai-06` and `ai-19` (matching the existing `ai-23` wrap)
- All 9 verification screenshots captured at 480/375/320 — ai06/ai19/ai23 visually clean
- `quality-check.py` pass on `case-ai.html`

### Figma frames state (before this thread runs)

Each of 774:8 and 772:8 currently contains a JPEG image fill from Session 4 (rendered from the HTML at 375 width, pasted as `IMAGE` fill with `scaleMode: FILL`). They render correctly on the canvas but can't be edited natively — any color/typography polish would require re-rendering. This thread's job is to swap those fills for native layers so Della can edit directly.

---

## Non-negotiables for the fresh thread

- **Skill Execution Rule:** read `html-to-figma/SKILL.md` + references + scripts. Don't paraphrase the skill to an agent.
- **Verify-before-claiming:** Figma MCP screenshot every refreshed frame. Compare side-by-side with the HTML render at 375. If anything drifts, stop.
- **Living Documents Rule:** tracker writes via `tracker-helpers.py` openpyxl (`update_row`). Never pandas. Notes preserved with `|` separator, never clobbered.
- **Mac paths only** for terminal commands Della will run (PATH-MAPPINGS.md). Reject any `/sessions/...` path.
- **No tidyPage on page 29:42.** Della's desktop cluster is hand-positioned; mobile frames already at `x=-420`. Leave canvas positions alone.
- **Main thread only** for Figma pairing judgment work — no sub-agent delegation.

---

## Handoff close

When this thread completes:

1. Tracker: ai06 and ai19 rows have the refresh note appended. Status/verify_date unchanged.
2. BUILD-LOG: one paragraph in the Apr 2026 block documenting the Figma refresh + that ai06/ai19 now edit natively in Figma.
3. SESSION-STATE: case-ai block updated from "COMPLETE — Session 9, Figma pairing refresh queued" to "COMPLETE — Session 9 + Figma refresh (date)". The "Figma pairing refresh" line in Open items gets removed (done).
4. No git commits from the Figma thread directly — Della runs commit/push in Terminal per Mac-path convention.

---

## Version

- 2026-04-22 — initial. Created end of Session 9 after case-ai mobile completion shipped. Supersedes the prior `case-ai-figma-pairing-prompt.md` draft (removed).
