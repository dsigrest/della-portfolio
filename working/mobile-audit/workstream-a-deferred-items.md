# Workstream A — Deferred Items

**Created:** 2026-04-22 (Session 28 Workstream A review gate)
**Purpose:** Track polish items Della chose to defer during the review gate. Future focused threads (Figma-polish, structural-additions, etc.) can pick these up one at a time.

---

## Item 1 — sub05 Card 4 mini-UI thumbnail swap

**Status:** DEFERRED 2026-04-22 by Della's call
**Type:** Structural (net-new SVG content)
**Source:** `portfolio-site/img/diagrams/diagram-sub05-artifact-alignment.html` Card 4
**Figma reference:** `TArUrZsBUocaAsqetjXq7V` page `29:40` node `678:700` (x=914, "SUB-05a — Shared Artifacts")

**Current state:** Card 4 "Design Patterns" uses 3 color swatches.
**Target state:** Della's x=914 Figma polish replaces the 3 swatches with 3 mini-UI preview thumbnails.

**Why deferred:** Authoring ~60–90 lines of net-new SVG path data representing UI previews without a verified spec is higher-risk than the rest of the Workstream A pass. Della opted to skip during Session 28 Workstream A review gate and address in a focused follow-up thread.

**How to resume:**
1. Pull `678:700` Figma metadata via Dev Mode MCP namespace `mcp__8e95afc0-e30e-4e27-bfa2-90ccd2e7b3a9__*` (the `mcp__Figma__*` variant errors — use the alt namespace per Sessions 17/18/24/25/27).
2. Read the 3 mini-UIs in Figma's Card 4 (screenshot + layer names).
3. Author 3 SVGs in sub04's canonical style (1.5 stroke, `currentColor`, sized to fit existing Card 4 layout).
4. Swap into `diagram-sub05-artifact-alignment.html` Card 4 in place of the 3 swatches.
5. voice-check + quality-check + 6-breakpoint Playwright render.
6. Tracker note append.

---

## Item 2 — sub09 icon glyph swaps (Share / Engage / Trust)

**Status:** DEFERRED 2026-04-22 by Della's call
**Type:** Figma polish (icon glyph authoring, 3 glyphs)
**Source:** `portfolio-site/img/diagrams/diagram-sub09-distribution-loop.html` lines 299–303, 325–327, 348–351
**Figma reference:** `TArUrZsBUocaAsqetjXq7V` page `29:40` node `678:1056` (x=914, "SUB-09 — Distribution Loop")

**Current state:**
- Card 01 Share (red): megaphone glyph
- Card 02 Engage (warm): heart glyph
- Card 03 Trust (blue): shield-check glyph

**Target state (from Figma polish column):**
- Card 01 Share: play/triangle
- Card 02 Engage: infinity/rings
- Card 03 Trust: checkbox

**Why deferred:** Three net-new SVG glyphs authored from description-of-glyph rather than verified Figma path data carries aesthetic-drift risk. The current icons render cleanly with clear semantic fit (megaphone=broadcast, heart=engagement, shield-check=trust); the swap is about matching Della's polish intent, not fixing a rendering issue. Best batched with other Figma-polish items in a focused follow-up thread.

**How to resume:**
1. Pull `678:1056` Figma metadata via Dev Mode MCP namespace `mcp__8e95afc0-e30e-4e27-bfa2-90ccd2e7b3a9__*` (the `mcp__Figma__*` variant errors — use the alt namespace per Sessions 17/18/24/25/27).
2. Extract exact SVG path data for the 3 polished glyphs.
3. Preserve existing card-icon container style (16x16 viewBox 0 0 24, stroke 1.5, `currentColor`, card hue inherited from `.flow-card.{red,warm,blue}` class).
4. Swap glyph `<path>` / `<polyline>` elements inline; keep all surrounding container markup.
5. voice-check + quality-check + 6-breakpoint Playwright render.
6. Tracker note append to `sub09-distribution-loop` row.

---
