# Figma Handoff — case-building-portfolio

**Date:** April 21, 2026 (fixes) → **April 22, 2026 (verification + Figma pairing complete)**
**Scope:** Mobile responsive audit + fixes + Figma mobile pairing for **all 5** port diagrams (case-building-portfolio meta case study)
**Status:** ✅ All 5 fixes verified. ✅ All 5 mobile frames translated into Figma (native layers, CSS-selector names). Tracker updated with `figma_mobile_node_id` for every row.

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
