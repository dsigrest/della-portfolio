# Figma Handoff — case-notifications Mobile Diagrams

**Date:** 2026-04-22
**Figma file:** `TArUrZsBUocaAsqetjXq7V` (Portfolio — Image Inventory)
**Page:** 1. Notifs & Inbox (id `29:43`)
**Mobile cluster anchor:** `x = -1700`

---

## Scope

All 13 notifications case study diagrams now have paired mobile (375px wide) Figma frames. Frames are native-layer, fully editable, and use CSS-selector layer naming so Della can polish in Figma and have changes round-trip back to HTML via the `figma-to-html` skill.

## Status summary

| Category | Count | Diagrams |
|---|---|---|
| PROPER (preserved, not rebuilt) | 2 | not01, not04 |
| PROPER (existing native rebuild, preserved) | 1 | not-e4 |
| Rebuilt this batch (native mobile) | 10 | not06, not07, not09, not11, not-e1, not-e2, not-e3, not-e5, not-e6, not-e7 |

Total: 13 diagrams, all with mobile Figma frames tracked in `audit-tracker.xlsx`.

## Node map

| Diagram | Desktop HTML | Mobile Figma node | Height | Status |
|---|---|---|---|---|
| not01 — Push Bloat Current State | `diagram-not01-push-bloat-current-v5.html` | `720:23` | 880 | fixed (preserved) |
| not04 — Notification Goal Alignment | `diagram-not04-notification-goal-alignment-v5.html` | `720:24` | 778 | fixed (preserved) |
| not06 — Push-to-Inbox Continuity | `diagram-not06-push-to-inbox-continuity-v5.html` | `907:17` | 800 | rebuilt-mobile-native |
| not07 — Preference Architecture | `diagram-not07-preference-architecture-v5.html` | `918:2` | 1131 | rebuilt-mobile-native |
| not09 — Global Settings Rebuild | `diagram-not09-global-settings-rebuild-v5.html` | `926:2` | 1127 | rebuilt-mobile-native |
| not11 — Cross-Channel Model | `diagram-not11-cross-channel-model-v5.html` | `945:17` | 720 | rebuilt-mobile-native |
| not-e1 — Cohort Decay | `diagram-not-e1-cohort-decay-v5.html` | `949:17` | 408 | rebuilt-mobile-native |
| not-e2 — Strategy Flywheel | `diagram-not-e2-strategy-flywheel-v4-mobile.html` | `953:17` | 564 | rebuilt-mobile-native |
| not-e3 — Strategic Pillars | `diagram-not-e3-strategic-pillars-v5.html` | `955:17` | 582 | rebuilt-mobile-native |
| not-e4 — Signal × Intent Matrix | `diagram-not-e4-signal-intent-matrix-v5.html` | `865:17` | 338 | fixed (preserved) |
| not-e5 — Notification Taxonomy | `diagram-not-e5-notification-taxonomy-v5.html` | `961:17` | 466 | rebuilt-mobile-native |
| not-e6 — Butterfly Chart | `diagram-not-e6-butterfly-chart-v5.html` | `964:2` | 315 | rebuilt-mobile-native |
| not-e7 — Sankey Flow | `diagram-not-e7-sankey-flow-v4-mobile.html` | `965:2` | 561 | rebuilt-mobile-native |

## Conventions enforced

- Root frame width: 375px (iPhone 14 Pro mobile width)
- Root fill: `#0A0C16` (canvas), radius 16px, clips content
- Frame names match CSS selectors (`.stage`, `.category-row.discovery`, `.stage-item:nth(1)`, etc.)
- Animated elements placed at full visibility (not opacity 0) so Della can see them in Figma
- SVGs inserted via `createNodeFromSvg` — editable as vectors
- Design tokens match desktop: accent `#7FB5B0`, gold `#C4B078`, warm `#D4A574`, red `#C47878`, blue `#8A9EC4`
- JetBrains Mono for numeric/technical labels, Inter for titles and body

## Round-trip workflow

1. **Edit in Figma** — Della polishes spacing, typography, color, layout directly on any frame.
2. **Sync to HTML** — invoke `figma-to-html` skill with diagram ID and node ID. The skill maps CSS-selector layer names back to the HTML source.
3. **Deploy** — invoke `diagram-deploy` skill to push updated HTML to the portfolio site case-notifications pages.

## Known follow-ups

- **not-e5 example cards** — titles with 2–3 line wrap make card heights uneven within a row; Della may want to tighten title character counts or reduce font size one step.
- **not-e7 dropout text** — "25% drop off — clicked but didn't contribute" wraps to 2 lines in the narrow mobile frame; shortening to "clicked, no contribute" would keep it single-line.
- **not-e6 butterfly chart** — rendered as single SVG vector. Individual bars/labels are editable as vector sub-nodes but not structured as separate named frames (would require a refactor if Della wants to restyle per-category).

## Files updated

- `portfolio-site/working/mobile-audit/audit-tracker.xlsx` — 10 rows updated with new node IDs, verify dates, and status
- Figma file `TArUrZsBUocaAsqetjXq7V` page `29:43` — 10 new mobile frames added at `x = -1700` cluster
