# Resume prompt — Portfolio Figma pairing: roundtrip + site integration

**Copy the block below as the first message in a fresh Cowork thread.**

---

Portfolio Figma pairing — post-build continuation. Session 16 (Apr 22, 2026) finished building all **12 mobile Figma frames** for `case-building-portfolio`. This thread picks up the remaining downstream work: Figma → HTML roundtrip after Della polishes, live-site deploy of new HTML diagrams, and case-study-page integration for the 7 diagrams that have never been embedded.

## Current state (verified)

**Figma — all 12 mobile frames built on page `29:2` of file `TArUrZsBUocaAsqetjXq7V`, cluster anchor `x = −1325`:**

| Diagram | Figma mobile node | Status in tracker |
|---|---|---|
| port-01b | 849:14 | verified (shipped) |
| port-02c | 849:35 | verified (shipped) |
| port-03a | 838:14 | verified (shipped) |
| port-04a | 852:14 | verified (shipped) |
| port-05 | 852:95 | verified (shipped) |
| port-01a-carousel | 1083:14 | **figma-mobile-built** — HTML shipped, Figma awaits polish |
| port-01a-grid | 1085:14 | **figma-mobile-built** — HTML not shipped |
| port-01d-implication | 975:14 | **figma-mobile-built** — HTML not shipped |
| port-03a1-thumbnails | 838:14 | **figma-mobile-built** (reused desktop thumbs frame) — HTML not shipped |
| port-03b-principles | 975:24 | **figma-mobile-built** — HTML not shipped |
| port-03c-design-system | 1086:14 | **figma-mobile-built** — HTML not shipped |
| port-04b-governance | 1088:14 | **figma-mobile-built** — HTML not shipped |

**Case study page (`portfolio-site/case-building-portfolio.html`) currently embeds 6 diagrams** (port-01a-carousel, port-01b, port-02c, port-03a, port-04a, port-05). The other **6 diagrams have no `data-diagram` embed yet** — they exist only as working HTML + mobile Figma frame.

## Mandatory pre-work

1. Read `/Users/della/CoworkWorkspace/Get-a-job/CLAUDE.md` and `/Users/della/CoworkWorkspace/CLAUDE.md` for voice, verify-before-claiming, living-documents, and tidyPage-exception rules.
2. Read `/Users/della/CoworkWorkspace/Skills/figma-to-html/SKILL.md` and `/Users/della/CoworkWorkspace/Skills/diagram-deploy/SKILL.md` in full — **do not summarize**, the agent executing must read the actual files.
3. Read the tracker at `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/audit-tracker.xlsx` (sheet `audit`) and confirm the 7 `figma-mobile-built` rows match the table above.
4. **Sentinel-test the Figma write channel** before queuing any roundtrip batch. One rename-and-restore on any existing node. If writes don't land, stop.

## Work to pick up, in order

### Gate 1 — confirm Della has polished before running figma-to-html

Before starting roundtrip work, ask Della directly: "Which of the 7 figma-mobile-built frames have you polished in Figma and want translated back to HTML?" Do not guess. If the answer is "none yet," skip to the integration work below (it doesn't require polish).

### Task A — figma-to-html roundtrip (per polished frame)

For each frame Della confirms is ready:

1. Invoke the `figma-to-html` skill with the Figma node ID and the target HTML path (see table below).
2. Diff the translated HTML against the current working version. Show Della the diff before overwriting.
3. Update the tracker row: `status` → `figma-mobile-translated`, stamp `verify_date`.

| Figma mobile node | Target HTML path (working) | Target HTML path (site deploy) |
|---|---|---|
| 1083:14 | `working/diagrams/v3/diagram-port01a-carousel.html` | `portfolio-site/img/diagrams/diagram-port01a-carousel.html` (already shipped — overwrite) |
| 1085:14 | `working/diagrams/v3/diagram-port01a-dimension-weights.html` | not yet shipped |
| 975:14 | `working/diagrams/v3/diagram-port01d-implication.html` | not yet shipped |
| 838:14 | existing desktop file — **skip translation; this node is reused from desktop** | n/a |
| 975:24 | `working/diagrams/v3/diagram-port03b-principles.html` | not yet shipped |
| 1086:14 | `working/diagrams/v3/diagram-port03c-design-system.html` | not yet shipped |
| 1088:14 | `working/diagrams/v5/diagram-port04b-governance-v5.html` (note: v5/, not v3/) | not yet shipped |

### Task B — responsive audit on translated HTML

For each file touched in Task A, run the `responsive-audit` skill at the 6 standard breakpoints (1440, 1024, 768, 480, 375, 320). Fix any container/content failures inline. Update tracker `ok_*` columns.

### Task C — deploy to live site via `diagram-deploy`

For the **6 diagrams that have never shipped** (port-01a-grid, port-01d-implication, port-03a1-thumbnails, port-03b-principles, port-03c-design-system, port-04b-governance): invoke `diagram-deploy` to copy `working/diagrams/v3/*.html` (or v5/ for governance) into `portfolio-site/img/diagrams/` with the canonical filename pattern `diagram-{id}.html`.

Verify each file lands and validates (run `portfolio-site/quality-check.py`).

### Task D — embed new diagrams in `case-building-portfolio.html`

The 6 never-shipped diagrams need `data-diagram` embeds added to the case study page. **Do not bulk-rewrite the page** — it's a living document. Add 6 targeted insertions at the correct narrative positions. Ask Della first which story positions each diagram belongs in — don't guess. Suggested order based on the diagram IDs:

- **port-01a-grid** — paired with port-01a-carousel (company weights by dimension)
- **port-01d-implication** — after port-01b (downstream effect of the research insight)
- **port-03a1-thumbnails** — between port-03a and port-03b (thumbnail gallery as transition)
- **port-03b-principles** — after port-03a1 (principles distilled from the thumbnails)
- **port-03c-design-system** — after port-03b (system emerging from principles)
- **port-04b-governance** — after port-04a (governance ring pairing)

For each embed, show Della the proposed HTML snippet (copy the existing `data-diagram="port-01a-carousel"` pattern from line 59 of the case page) and the insertion line number **before editing**.

### Task E — final tracker sync + commit

1. Flip 6 rows from whatever status they end at → `shipped` after deploy + embed.
2. Run the full voice-check + quality-check on the modified case page.
3. Show Della the final diff and give her the `git add` / `git commit` commands (Mac absolute paths from `PATH-MAPPINGS.md`). **Do not commit from the sandbox.**

## Non-negotiables for this thread

- **tidyPage suspended** on the Figma file (page 29:2 uses hand-curated cluster anchors — desktop left, mobile at `x=−1325`). Additive writes only.
- **figma-to-html must reuse existing CSS selectors** as layer names — HTML overwrites should be minimal-diff, not full rewrites.
- **Verify before claiming.** Screenshot each translated diagram at 375px and 1440px after every figma-to-html run. Don't tell Della "it looks right" without a screenshot.
- **Font:** Inter, style `"Semi Bold"` **with a space**, not `"SemiBold"`. Same for `"Extra Bold"`.
- **Living-document rule** for `case-building-portfolio.html` — targeted edits only. Never delegate a full-file rewrite to an agent.
- **Skill patches known open for html-to-figma v1.1.0** (see `resume-prompt-html-to-figma-skill-patch-v1.1.0.md` in this same folder) — figma-to-html may have parallel issues worth watching for. Surface anything new.

## Deliverables in chat

- Per-translated-diagram: figma node → HTML diff summary, screenshot at 375px and 1440px, tracker row after-state.
- List of 6 deploy-and-embed files landing in `portfolio-site/img/diagrams/`.
- Final `case-building-portfolio.html` diff showing 6 new `data-diagram` embeds at their narrative positions.
- Git commands for Della to run (from her Mac, never the sandbox).
- Any skill-patch issues caught during the run — feed them into the v1.1.0 prompt.

## Context files to read if deeper history is needed

- `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/reports/figma-handoff-case-building-portfolio.md` — full Session 9 + 15 + 16 history.
- `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/resume-prompt-session16-figma-mobile-frames.md` — the prompt that kicked off Session 16 (now complete).
- `/Users/della/CoworkWorkspace/Get-a-job/BUILD-LOG.md` — running project arc.
