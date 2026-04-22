# Resume prompt — Session 16 Figma mobile frame builds

**Copy the block below as the first message in a fresh Cowork thread.**

---

Session 16 follow-up — build the pending mobile Figma frames for the `case-building-portfolio` case study, plus one reposition.

**Background.** Session 15 opened to close the gap on 7 mobile Figma frames. It landed 2 (`port-01d-implication` = node `975:14`; `port-03b-principles` = node `975:24`, but misplaced at y=7408) before the Figma MCP write channel appeared broken mid-session. Session 16 (today) sentinel-tested the write channel on `975:14` — writes **work**. Rename to a marker landed on canvas per `get_metadata`, then restore to `port-01d-implication` also confirmed. No diagnostic work needed; proceed directly to builds.

**File + page:** `TArUrZsBUocaAsqetjXq7V`, page `29:2` (`5. Building this portfolio`). Mobile cluster anchor: `x=−1325`.

**Outstanding Figma work**

1. **Reposition `port-03b-principles`** (node `975:24`) from y=7408 → y=6849. One-line `use_figma` call.

2. **Build 5 new mobile frames.** Native layers, no image fills. Source HTML and y-anchors:

| # | Frame name | Source HTML | y-anchor | Complexity |
|---|---|---|---|---|
| 1 | `port-01a-grid` | verify location — Session 15 handoff referenced `working/diagrams/v3/` but that folder doesn't exist; check `img/diagrams/` first | 1051 | L3 |
| 2 | `port-01a-carousel` | `img/diagrams/diagram-port01a-carousel.html` (shipped live in Session 16) | 2791 | L2 |
| 3 | `port-03a1-thumbnails` | verify location (same caveat as #1) | 6109 | L2 |
| 4 | `port-03c-design-system` | verify location (same caveat) | 7938 | L3 — largest |
| 5 | `port-04b-governance` | verify location (same caveat) | ≈11600 | L2 |

3. **Update tracker** at `working/mobile-audit/audit-tracker.xlsx` — for each new frame flip `status` from `figma-mobile-pending` → `figma-mobile-built` and write `figma_mobile_node_id`. Use `openpyxl` (per global CLAUDE.md living-documents rule — never pandas overwrites).

**Mandatory pre-work**

- Read `/Users/della/CoworkWorkspace/Skills/html-to-figma/SKILL.md` in full. If delegating to an agent, the agent must read the actual skill file — do not summarize.
- Read `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/reports/figma-handoff-case-building-portfolio.md` — contains per-diagram translator notes.
- Read `/Users/della/CoworkWorkspace/CLAUDE.md` and `/Users/della/CoworkWorkspace/Get-a-job/CLAUDE.md` for voice, verify-before-claiming, and tidyPage-exception rules.

**Non-negotiable Figma rules for this file**

- **tidyPage is suspended** for case-study pages on this file. They use hand-curated cluster anchors (desktop left, mobile at `x=−1325`). Additive writes only. Do NOT reposition existing frames except for the explicit `port-03b` move in task 1.
- **Session 15 skill patches to apply** (not yet in html-to-figma v1.0.0):
  1. After every `appendChild`, reassert `layoutSizingHorizontal: 'FILL'` + `layoutSizingVertical: 'HUG'` on auto-layout descendants. First-pass translations silently drop these, causing collapsed columns.
  2. TEXT nodes don't expose `layoutMode`. Any filter like `n.layoutMode !== 'NONE'` must guard with `('layoutMode' in n && n.layoutMode !== 'NONE')`.
- **Font:** Inter, style `"Semi Bold"` **with a space**, not `"SemiBold"`. Same for `"Extra Bold"`.
- **Native layers only** — no image fills. Polish-in-Figma requires real editable nodes.
- **Sentinel-test the write channel first** in this new thread before queuing a batch. One rename-and-restore on any existing node. If writes don't land, stop and surface — don't burn the session on MCP diagnostics.

**Verification before reporting done**

- `get_screenshot` each new frame to spot-check rendering — no collapsed columns, no oversized elements, text wraps cleanly at 375px.
- `get_metadata` on each to confirm position matches the target y-anchor.
- Confirm tracker was actually updated (open the xlsx and read the rows — don't just trust the script's success log).
- For `port-03b`: `get_metadata` to verify y=6849 after the reposition.

**Deliverables in chat**

- Frame-by-frame table: name, `node_id`, position (x, y), dimensions, screenshot link.
- Updated tracker row dump (the 5 flipped rows).
- Any source-file path corrections found (the handoff has stale `working/diagrams/v3/` references).
- Any skill-patch issues surfaced — useful input for `html-to-figma` v1.1.0.
