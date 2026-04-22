# Figma Handoff — case-building-portfolio

**Date:** April 21, 2026 (fixes) → April 22, 2026 (Session 9 Figma pairing + Session 15 scope expansion)
**Scope:** Mobile responsive audit + fixes + Figma mobile pairing — originally 5 port diagrams, expanded to **12** across two html-to-figma threads.
**Status:**
- Session 9 (Apr 22 AM): ✅ All 5 original fixes verified + all 5 mobile frames translated native (`port-01b`, `port-02c`, `port-03a`, `port-04a`, `port-05`).
- Session 15 (Apr 22 PM): 🟡 **2 of 7** new mobile frames landed (`port-01d-implication` → node `975:14`, `port-03b-principles` → node `975:24`). 5 pending (`port-01a-grid`, `port-01a-carousel`, `port-03a1-thumbnails`, `port-03c-design-system`, `port-04b-governance`). Figma MCP write channel broke mid-session — pending frames deferred to session 16.

---

## Session 15 Extension — scope expansion to 12 mobile frames

**Why this extension exists:** Session 9 paired the 5 diagrams that had mobile-audit severity fixes. But the case-building-portfolio desktop page has **7 more diagrams** that need mobile Figma pairs for polish-in-Figma roundtrip parity — diagrams that were already mobile-responsive but had no dedicated Figma frame. Session 15 opened to close that gap.

### The 7 new diagrams

| # | Diagram | File | y-anchor (page 29:2) | Session 15 status |
|---|---|---|---|---|
| 1 | port-01a-grid | `working/diagrams/v3/diagram-port01a-company-grid.html` | 1051 | **pending** — Figma write channel blocked |
| 2 | port-01a-carousel | `working/diagrams/v3/diagram-port01a-carousel.html` **(new HTML this session)** | 2791 | **pending** — Figma write channel blocked |
| 3 | port-01d-implication | `working/diagrams/v3/diagram-port01d-implication.html` | 4531 | ✅ **built** — Figma node `975:14` |
| 4 | port-03a1-thumbnails | `working/diagrams/v3/diagram-port03a1-thumbnails-gallery.html` | 6109 | **pending** — Figma write channel blocked |
| 5 | port-03b-principles | `working/diagrams/v3/diagram-port03b-principles.html` | **6849 (intended)** / **7408 (actual)** | ✅ **built** — Figma node `975:24` — **misplaced, needs reposition** |
| 6 | port-03c-design-system | `working/diagrams/v3/diagram-port03c-design-system.html` | 7938 | **pending** — Figma write channel blocked |
| 7 | port-04b-governance | `working/diagrams/v3/diagram-port04b-governance-ring.html` | ≈11600 | **pending** — Figma write channel blocked |

Mobile cluster anchor stays at `x=−1325` (same as Session 9's 5 frames). Each new frame stacks at its own y-position in the cluster.

### What's new this session (port-01a-carousel HTML)

`port-01a-carousel` is a **brand-new HTML diagram** written this session — it did not exist before. It complements the existing company grid (`port-01a-grid`) with an interactive carousel navigator showing each of the 6 target companies' weight profiles across 5 dimensions:

- Ramp: 10/15/15/30/30
- Anthropic: 15/20/15/25/25
- Meta: 20/20/25/25/10
- Figma: 15/30/20/20/15
- OpenAI: 20/20/20/20/20 (max across)
- Cursor: 20/20/20/20/20 (max across)

Figma linkage embedded via `<meta name="figma-source" content="node:659:1166 page:29:2 file:TArUrZsBUocaAsqetjXq7V">`. `@media (max-width: 680px)` reflow included. **Can deploy to the live site via `diagram-deploy` without needing the Figma pair** — the Figma frame is optional polish surface.

### Figma MCP write channel failure (Session 15)

Reads kept working — `get_metadata` returned a full 245k-char snapshot of file `TArUrZsBUocaAsqetjXq7V` page `29:2`. Writes silently no-op'd: every `use_figma` script returned `"Code executed with no return value"` but produced zero changes on canvas. Rename-existing-node sentinel test confirmed asymmetry (rename of node `975:14` to `'WRITE_TEST_RENAME'` did not stick). Persisted through Figma desktop quit + reopen. Root cause not isolated.

**Session 16 must sentinel-test writes before queuing a batch:**

```javascript
// use_figma — sentinel test
const target = await figma.getNodeByIdAsync('975:14');
const oldName = target.name;
target.name = 'WRITE_TEST_' + Date.now();
// read back on canvas, then restore:
target.name = oldName;
```

If the sentinel name doesn't appear on the canvas, do not queue work. Stop and troubleshoot the channel first (or surface to Della and pivot).

### Outstanding work for Session 16

1. **Sentinel-test Figma write channel** (above). If broken, pivot — do not re-burn a session on Figma tool diagnosis.
2. **Reposition `port-03b-principles` (975:24)** from y=7408 → y=6849. One-line Figma write.
3. **Build 5 pending mobile frames** at their planned y-anchors (see table above). Each is a single `use_figma` call following the Session 9 pattern (auto-layout HUG reassert, CSS-selector layer names, Inter font tokens, native-layer vectors — no image fills).
4. **Deploy `port-01a-carousel` HTML to the live site via `diagram-deploy`** — does not require Figma; can run in parallel with any Figma work.
5. **Update tracker** after each build: flip `status` from `figma-mobile-pending` → `figma-mobile-built`, write `figma_mobile_node_id`.

### Per-diagram translator notes (Session 16 pickup)

**port-01a-grid** (L3, responsive desktop → 375px mobile): Stacked company cards with weight bars. Each card ~200h. 6 cards stacked + header ≈ 1400px total. Reuse the `glassCard` helper pattern from Session 9.

**port-01a-carousel** (new this session): Simpler than the grid — single-card carousel with nav dots. At 375px the card fills most of the width. Use the `<meta>` node ID (`659:1166`) as the Figma source.

**port-01d-implication** ✅ **already built** as `975:14` at `y=4531`. L2, no follow-up needed.

**port-03a1-thumbnails** (L2, 12-card gallery): At 375px, 2-column grid. Thumbnails are abstract color blocks — same safe-collapse logic as port-03a. ~10 rows × ~140h ≈ 1400px.

**port-03b-principles** ✅ **already built** as `975:24`, but **needs reposition** from y=7408 → y=6849 to close the gap between it and `port-03a1-thumbnails`.

**port-03c-design-system** (L3, tallest): Palette (7 swatches, 44×44 on mobile per CSS) + type scale (4 rows: 32/17/14/11px examples) + spacing blocks (3: Tight 4-8, Comfortable 16-24, Generous 48-80) + signature interaction (5 micro-bars at heights [18,28,22,36,30] + "Staggered reveals" title + desc). Largest frame — budget ~1100px height on mobile. Batch 2 use_figma helper functions (`rgb`, `fill`, `text`, `vframe`, `hframe`, `border`, `fixFrame`) were already drafted this session; see BUILD-LOG session 15 for the code sketch.

**port-04b-governance** (L2, governance ring): Desktop is a visual ring — mobile reflows to a vertical stacked list with connector ticks (not a ring — linear sequence). Same pattern as port-04a's desktop-ring→mobile-linear translation from Session 9.

---

## Session 9 (original) — 5 diagrams paired native

Below this point is the original Session 9 handoff content, preserved verbatim for reference.

---

**Scope expansion note (Apr 22):** Original handoff doc (below) scoped Figma pairing to 4 diagrams (port-02c, port-03a, port-04a, port-05), excluding port-01b because it was L0 / already responsive. Della expanded the scope to all 5 during the html-to-figma thread — port-01b still needs a Figma mobile frame for pairing consistency, even though the HTML didn't need changes. All 5 now have mobile frames.

---

## Summary

Ran `responsive-audit full case-building-portfolio` (batch-review mode per Della's direction). 5 diagrams audited across 6 breakpoints (1440, 1024, 768, 480, 375, 320). All fixes landed. Screenshot verification pending — Della to run `screenshot-diagrams.py` on her Mac, since Playwright-in-sandbox can't capture.

**Severity distribution:** L0 ×1, L2 ×3, L3 ×1

| Diagram | Severity | Fix location | File(s) changed |
|---|---|---|---|
| port-01b-insights | L0 | — | none (already responsive) |
| port-02c-research-synthesis | L2 | inside diagram `<style>` | `img/diagrams/diagram-port02c-research-synthesis-v4.html` |
| port-03a-thumbnails | L2 | inside diagram `<style>` | `img/diagrams/diagram-port03a-thumbnails-v4.html` |
| port-04a-governance | L3 | new mobile file + wrapper | `img/diagrams/diagram-port04a-governance-v4-mobile.html` (new), `case-building-portfolio.html` (wrapper) |
| port-05-recruiter-panel | L2 | inside diagram `<style>` | `img/diagrams/diagram-port05-recruiter-panel-v4.html` |

`styles.css` was **not** modified — the existing `.diagram-pair` swap rule (lines 370–377) covered port-04a's L3 swap at 768px without edits.

---

## Per-diagram fix notes

### port-01b-insights (L0)
Already responsive. No changes. Verification pending.

### port-02c-research-synthesis (L2)
**Root cause (Pattern C):** 4-column `.dimension-row` grid didn't collapse below 680px. Connector SVG sections and machine hub oversized at 480 and below.
**Fix applied:** Added `@media (max-width: 480px)` block:
- Collapsed `.dimension-row` from 4-col to 2-col grid, 10px gap
- Wrapped `.tab-bar` tabs, tightened gaps/padding
- Hid `.connector-section` and `.connector-section-bottom` (decorative SVG arrows)
- Reduced `.machine-hub` from default to 90×90, `.machine-glow` to 140×140
- Compacted `.dim-card` padding and icon size
**Preserved:** All 4 dimensions, all tabs, machine-hub animation, color palette.

### port-03a-thumbnails (L2)
**Root cause (Pattern C):** 3-column `.portfolio-grid` didn't collapse below 680px. Title (h1 36px), stats-bar, and legend oversized on mobile.
**Self-reference check:** Thumbnails are **abstract color-blocks**, not actual portfolio screenshots. Safe to collapse grid — we're not misrepresenting the portfolio contents.
**Fix applied:** Added `@media (max-width: 480px)` and `@media (max-width: 375px)` blocks:
- Collapsed `.portfolio-grid` from 3-col to 2-col at 480px
- h1 36 → 28 → 24 (at 480, then 375)
- `.stats-bar` wraps with reduced gap, stat-num 32 → 20 → 18
- `.legend` wraps
**Preserved:** All thumbnails, stats, subtitle, legend entries.

### port-04a-governance (L3)
**Root cause:** Absolute-positioned 6-node loop with hardcoded SVG connectors — physically cannot reflow. Loop topology breaks at any width below desktop.
**Fix applied:** Created `diagram-port04a-governance-v4-mobile.html` — a linear vertical sequence:

```
Set Intent (Della)
  ↓
Brief (joint)
  ↓
Generate (Claude)
  ↓
Self-Check (Claude)
  ↓
Decision Gate (joint)
  ├─ Pass → Ship
  └─ Redirect (Della) → "returns to Intent" (dashed loop-back indicator)
```

- Vertical column, connector arrows between sequential nodes
- Decision Gate branches into a 2-col grid (Redirect | Ship) with a horizontal splitter
- Loop-back rendered as a dashed-border label with `↺ returns to Intent` — avoids complex SVG flow redraw on mobile
- All 7 nodes preserved (Set Intent, Brief, Generate, Self-Check, Decision Gate, Redirect, Ship)
- Color coding preserved: Della = red left-border, Claude = accent left-border, Joint = resur left-border
- Legend preserved
- Click-to-expand interaction preserved (same JS as desktop)
- Text copy identical to desktop (titles, descriptions, detail paragraphs)

**Wrapper change in `case-building-portfolio.html`:**
```html
<div class="case-img-full diagram-embed diagram-pair" data-diagram="port-04a">
  <iframe class="desktop-variant" src="...-v4.html" ...></iframe>
  <iframe class="mobile-variant"  src="...-v4-mobile.html" ...></iframe>
</div>
```
Swap handled by existing rule in `styles.css` at 768px.

### port-05-recruiter-panel (L2)
**Root cause (Pattern C):** Each `.score-card` uses `grid-template-columns: auto 1fr auto` (company-info | 5-bar dimensions | score). Middle column compresses too far below 680px; dimension-labels become unreadable.
**Fix applied:** Added `@media (max-width: 680px)`, `(max-width: 480px)`, and `(max-width: 375px)` blocks:
- At 480, `.score-card` collapses to single column (`1fr`) — company-info stacks above dimensions stacks above score
- `.dimensions-container` stays a 5-bar flex row (intentional — the 5 dimensions are the story)
- `.score-display` flips from `flex-direction: column` to `row` with `align-items: baseline` — score-number sits inline with score-label
- Dimension labels shrink 9 → 8 → 7.5px with tighter letter-spacing
**Preserved:** All 6 score-cards, 5-bar dimension rows, top-scorer highlight, color tiers, animations.

---

## Screenshot verification (pending — Della runs locally)

`screenshot-diagrams.py` is the existing capture script at `working/mobile-audit/scripts/`. To verify fixes:

```bash
cd ~/CoworkWorkspace/Get-a-job/portfolio-site && \
python3 working/mobile-audit/scripts/screenshot-diagrams.py case-building-portfolio
```

**Note:** The script only accepts a single positional arg — the case-study slug. It iterates all 6 breakpoints and all diagrams in that case study automatically. Earlier drafts of this doc showed fictional `--diagrams` / `--breakpoints` flags — those aren't implemented.

Output lands in `working/mobile-audit/screenshots-fixed/{width}/`. Compare against pre-fix screenshots in `working/mobile-audit/screenshots/{width}/` to confirm no regressions at 1440/1024/768 and real collapse at 480/375/320.

---

## Figma handoff — COMPLETE (Apr 22, 2026)

**Target Figma file:** `TArUrZsBUocaAsqetjXq7V`
**Target page:** `5. Building this portfolio`
**Translation mode:** **Native** (not image-fill). Every frame is editable — auto-layout, text nodes, shape nodes, SVG imports, CSS-selector layer names.
**Mobile cluster anchor:** x = −1325 (same y as each diagram's desktop counterpart)

| Diagram | Figma node ID | Position | Dimensions | Source file |
|---|---|---|---|---|
| port-01b-mobile | `849:14` | x=−1325, y=320 | 375 × 674 | `diagram-port01b-insights.html` |
| port-02c-mobile | `849:35` | x=−1325, y=3970 | 375 × 635 | `diagram-port02c-research-synthesis-v4.html` |
| port-03a-mobile | `838:14` | x=−1325, y=6350 | 375 × 765 | `diagram-port03a-thumbnails-v4.html` |
| port-04a-mobile | `852:14` | x=−1325, y=9354 | 375 × 954 | `diagram-port04a-governance-v4-mobile.html` (L3 mobile variant) |
| port-05-mobile | `852:95` | x=−1325, y=10607 | 375 × 941 | `diagram-port05-recruiter-panel-v4.html` |

**Quality pattern verified on port-03a (mid-complexity), then batched:** after greenlight on diagram 1, port-01b + port-02c translated in batch 1, port-04a + port-05 in batch 2. All 5 visually verified via `get_screenshot` — no collapsed columns, no oversized frames, layer trees clean.

**Why native, not image-fill:** the `html-to-figma` skill v1.0.0 was invoked with the native path. Image-fill would have been faster but Della wanted polish-in-Figma capability — that requires real layers.

**No `tidyPage` was run.** Case-study pages on this file use hand-curated cluster anchors (desktop left, mobile at x=−1325). The global tidyPage rule is suspended for these pages — additive writes only, no repositioning of existing frames.

---

## Tracker state (as of Apr 22, 2026)

5 rows in `working/mobile-audit/audit-tracker.xlsx`, **all `status=verified, verify_date=2026-04-22`**:
- `port-01b` — severity 0, verified (L0, no fix needed; stacks cleanly at 375)
- `port-02c` — severity 2, verified (Pattern C + G; tab-bar wraps cleanly at 375 with correct URL-bar clearance)
- `port-03a` — severity 2, verified (Pattern C; 3→2 col grid collapse + h1 scale + stats-bar wrap confirmed)
- `port-04a` — severity 3, verified (L3 linear-vertical mobile variant; `.diagram-pair` swap fires correctly in case-study page)
- `port-05` — severity 2, verified (Pattern C single-column collapse + score-display row-flip; 768 desktop intact)

Verification screenshots: `working/mobile-audit/screenshots/{width}/` (captured Apr 22 08:24 via Della's local `screenshot-diagrams.py case-building-portfolio` run).

---

## Files touched

**Modified (in-place edits):**
- `portfolio-site/img/diagrams/diagram-port02c-research-synthesis-v4.html` — added 480px media query
- `portfolio-site/img/diagrams/diagram-port03a-thumbnails-v4.html` — added 480 + 375 media queries
- `portfolio-site/img/diagrams/diagram-port05-recruiter-panel-v4.html` — added 680 + 480 + 375 media queries
- `portfolio-site/case-building-portfolio.html` — port-04a wrapper → `.diagram-pair` with both iframes

**Created:**
- `portfolio-site/img/diagrams/diagram-port04a-governance-v4-mobile.html` — new L3 mobile variant
- `portfolio-site/working/mobile-audit/reports/figma-handoff-case-building-portfolio.md` — this doc

**Not modified:**
- `portfolio-site/styles.css` — existing `.diagram-pair` swap rule (lines 370–377) covered the L3 case

---

## Next steps for Della

~1. Run `screenshot-diagrams.py` locally~ — **✅ DONE Apr 22 08:24**
~2. Eyeball the 480/375/320 + 1440/1024/768 outputs~ — **✅ DONE Apr 22 (all 5 verified)**
~3. Invoke `html-to-figma` to populate Figma mobile frames~ — **✅ DONE Apr 22 (all 5 translated native)**
4. **→ NEXT:** Polish the 5 mobile frames in Figma (typography, spacing, color refinements as desired).
5. When polish is complete: open a fresh Cowork thread using **`portfolio-site/working/mobile-audit/resume-prompt-case-building-portfolio-figma-to-html.md`** as the entry prompt. That doc handles `figma-to-html` (Figma polish → HTML edits) → local verification → git push. All 5 embeds are already live in `case-building-portfolio.html`, so `diagram-deploy` is a no-op unless a new embed is added — `git push` ships the HTML to Vercel directly.

## Skill patch recommendations (for `html-to-figma` v1.0.0 → v1.1.0)

Based on this 5-diagram batch, two tightening opportunities for the skill:

1. **Default to `layoutSizingHorizontal: 'FILL'` + `layoutSizingVertical: 'HUG'` after every `appendChild`.** The initial translator set these at creation time but Figma auto-layout silently dropped them on some children, causing collapsed columns (port-01b on first pass: h=1397 with ~100px text columns wrapping to 12+ lines each). The fix is always: walk the tree post-creation and reassert sizing on every auto-layout descendant. Suggest adding a `reassertSizing(frame)` helper to the skill and calling it at the end of every translation.

2. **TEXT nodes don't expose `layoutMode`.** Any code that filters descendants by `n.layoutMode !== 'NONE'` throws `TypeError: Cannot read property 'layoutMode' of undefined` on text children. The guard must be `'layoutMode' in n && n.layoutMode !== 'NONE'`. Worth baking into the skill's default tree-walker.

Both fixes are non-destructive — they just make the first-pass translation correct more often, reducing surgical post-passes.
