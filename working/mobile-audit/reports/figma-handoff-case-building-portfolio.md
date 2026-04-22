# Figma Handoff — case-building-portfolio

**Date:** April 21, 2026 (fixes) → **April 22, 2026 (verification complete)**
**Scope:** Mobile responsive audit + fixes for 5 port diagrams (case-building-portfolio meta case study)
**Status:** ✅ All 5 fixes verified Apr 22 via fresh screenshots. Tracker flipped to `status=verified`. Figma pairing ready to invoke — this doc is the entry point for the `html-to-figma` thread.

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

## Figma handoff (when ready to pair)

**Target Figma page:** `case-building-portfolio` (same page used for existing port-* desktop frames).

**Mobile frames to create** (in the left mobile cluster, same row as the corresponding desktop frame):
1. `port-02c-mobile` — render `diagram-port02c-research-synthesis-v4.html` at 375px wide
2. `port-03a-mobile` — render `diagram-port03a-thumbnails-v4.html` at 375px wide
3. `port-04a-mobile` — render `diagram-port04a-governance-v4-mobile.html` at 375px wide (this is the NEW L3 file, not the desktop version)
4. `port-05-mobile` — render `diagram-port05-recruiter-panel-v4.html` at 375px wide

port-01b does not need a mobile frame — already responsive (L0), same desktop file renders correctly at 375.

**Invocation when ready:**
```
html-to-figma push port-02c,port-03a,port-04a,port-05 \
  --page case-building-portfolio \
  --width 375 \
  --cluster mobile
```

The html-to-figma skill will:
- Take a live rendered screenshot of each HTML file at 375px
- Create a new frame in the mobile cluster on the case-building-portfolio page
- Position it on the same row as the existing desktop frame
- Never reposition or modify the existing desktop cluster (per Della's tidyPage exception note for case-study pages)

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
3. **→ NEXT:** invoke `html-to-figma push port-02c,port-03a,port-04a,port-05 --page case-building-portfolio --width 375 --cluster mobile` in a fresh thread to populate Figma mobile frames (port-01b not needed, L0).
4. Polish in Figma → `figma-to-html` → `diagram-deploy` → site live with mobile-responsive case-building-portfolio.

## Notes for the html-to-figma thread

- **Target case study page** on Figma file `TArUrZsBUocaAsqetjXq7V`: find the `case-building-portfolio` page (same page used for existing port-* desktop frames).
- **Byte-array transport, not base64.** Known `atob` failure in Figma plugin runtime (validated twice on case-notifications + case-ai threads). Render JPEG → dump raw bytes as JSON int array → inline as `Uint8Array` in the `use_figma` script → `figma.createImage(bytes)`.
- **No `tidyPage` on the case study page.** Desktop cluster is never modified. Mobile frames go into the left mobile cluster at the same y as their desktop counterpart. Mobile cluster anchor pattern: `leftmost_top_level_x − 1300` (validated on case-ai session 4).
- **port-04a source is the `-v4-mobile.html` file, not the desktop.** This is the only L3 — make sure the render uses the mobile variant.
