# Resume Prompt — case-building-portfolio mobile batch 2 (Session 16)

**Purpose:** Self-contained resume prompt for a fresh Cowork thread. Paste the entire block below into a new thread after Della opens Cowork with `~/CoworkWorkspace` mounted.

**When to use this:** Session 15 landed 2 of 7 planned mobile frames (port-01d-implication → `975:14`, port-03b-principles → `975:24`) and then hit a silent Figma MCP write-channel failure. 5 frames + 1 reposition remain. Session 16 picks up from there.

---

## ▼▼▼ PROMPT TO PASTE INTO FRESH THREAD ▼▼▼

I'm resuming the case-building-portfolio mobile Figma pairing batch 2. Session 15 built 2 of 7 planned mobile frames and then the Figma MCP write channel silently failed. I need you to pick up from Session 15's state and finish the batch.

**Read these first (in order):**

1. `~/CoworkWorkspace/CLAUDE.md` — global config (voice rules, session protocol, observability rules)
2. `~/CoworkWorkspace/Get-a-job/CLAUDE.md` — project-specific extensions
3. `~/CoworkWorkspace/Get-a-job/PATH-MAPPINGS.md` — Mac absolute paths for every terminal command
4. `~/CoworkWorkspace/Get-a-job/BUILD-LOG.md` — find the Session 15 entry at the top of "Log entries" section for full context
5. `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/reports/figma-handoff-case-building-portfolio.md` — especially the "Session 15 Extension" section
6. `~/CoworkWorkspace/Skills/html-to-figma/SKILL.md` — the translation skill you'll be executing

**Pre-load these tools via ToolSearch before any work:**

```
ToolSearch(query: "use_figma get_screenshot get_metadata", max_results: 10)
ToolSearch(query: "TaskCreate TaskUpdate TaskList", max_results: 5)
```

**State at start of Session 16:**

- **Figma file:** `TArUrZsBUocaAsqetjXq7V` (Portfolio — Image Inventory)
- **Figma page:** `29:2` ("5. Building this portfolio")
- **Mobile cluster anchor:** `x = −1325` (Della's hand-curated — do NOT run `tidyPage` on this page)
- **Already built this cluster (5 from Session 9 + 2 from Session 15):**
  - Session 9: port-01b (849:14), port-02c (849:35), port-03a (838:14), port-04a (852:14), port-05 (852:95) — all `verified`
  - Session 15: port-01d-implication (**975:14**, y=4531), port-03b-principles (**975:24**, y=7408 — **misplaced, should be y=6849**)

**Work to complete (in this order):**

### 1. Sentinel-test the Figma write channel — DO NOT SKIP

Before any substantive work, run this single `use_figma` script to confirm writes are landing:

```javascript
const target = await figma.getNodeByIdAsync('975:14');
if (!target) throw new Error('Node 975:14 not found — is the right file open?');
const oldName = target.name;
const sentinel = 'WRITE_TEST_' + Date.now();
target.name = sentinel;
// return the new name so we can verify the write round-tripped
sentinel;
```

Then immediately read back with `get_metadata` on node `975:14` and confirm its name matches the returned sentinel. Then restore:

```javascript
const target = await figma.getNodeByIdAsync('975:14');
target.name = 'port-01d-implication-mobile';  // original name
```

**If the sentinel doesn't land, stop.** Do not queue diagram work. Tell Della the write channel is still broken, and pivot to (a) deploying port-01a-carousel HTML to the live site via `diagram-deploy` (Figma-free), and (b) sketching the remaining diagrams' Figma translation code as comments-only files so Session 17 can paste-and-ship once the channel is restored. Do not spend more than 15 minutes debugging — Session 15 already spent an hour on this.

### 2. Reposition port-03b-principles (975:24) from y=7408 → y=6849

Single `use_figma` call once sentinel passes:

```javascript
const node = await figma.getNodeByIdAsync('975:24');
node.y = 6849;
```

Verify with `get_screenshot` on that frame.

### 3. Build 5 remaining mobile frames

Build at their planned y-anchors, in this order (small → large to accumulate wins):

| # | Diagram | Source HTML | y-anchor | Est. height |
|---|---|---|---|---|
| 1 | port-01a-carousel | `working/diagrams/v3/diagram-port01a-carousel.html` | 2791 | ~800px |
| 2 | port-01a-grid | `working/diagrams/v3/diagram-port01a-company-grid.html` | 1051 | ~1400px |
| 3 | port-03a1-thumbnails | `working/diagrams/v3/diagram-port03a1-thumbnails-gallery.html` | 6109 | ~1400px |
| 4 | port-04b-governance | `working/diagrams/v3/diagram-port04b-governance-ring.html` | ≈11600 | ~900px |
| 5 | port-03c-design-system | `working/diagrams/v3/diagram-port03c-design-system.html` | 7938 | ~1100px (tallest) |

Build in batches of 2 per `use_figma` call (per the html-to-figma skill convention — max 2 diagrams per batch). After each batch: `get_screenshot` each new frame, verify visually, update tracker row.

**Non-negotiables (carried from Session 9 + 15):**

- **Width:** 375px, mobile cluster x = −1325
- **`tidyPage` stays OFF** — additive writes only
- **Auto-layout HUG reassert pattern** — after every `appendChild`, re-set `layoutSizingVertical = 'HUG'` on the parent or the container keeps its pre-child fixed height
- **CSS-selector layer names** — `.diagram-header h2` → `diagram-header h2`, `.company-card.ramp .weight-bar` → `company-card ramp weight-bar` etc. Required for figma-to-html roundtrip.
- **Inter font styles** — `"Inter Regular"`, `"Inter Medium"`, `"Inter Semi Bold"` (with space), `"Inter Bold"`. Preload all 4 at script start.
- **Native-layer only, no image fills** — every element a vector primitive or text node.
- **Page activation:** `await figma.setCurrentPageAsync(page)` before any read/write on non-active pages. (Page 29:2 is likely active if Della already has it open, but don't assume — activate explicitly at script start.)

### 4. Update tracker after each batch

`~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/audit-tracker.xlsx` has 7 rows for these diagrams. After each frame lands, flip its row via openpyxl:

- `status`: `figma-mobile-pending` → `figma-mobile-built`
- `figma_mobile_node_id`: write the new node ID
- `verify_date`: today's date once `get_screenshot` confirms

Use atomic openpyxl writes (not pandas) per the living-documents rule.

### 5. Deploy port-01a-carousel HTML to the live site

**Independent of Figma work** — can run in parallel. Invoke the `diagram-deploy` skill to push `working/diagrams/v3/diagram-port01a-carousel.html` into `portfolio-site/img/diagrams/` and register it in the viewer manifest. Check `case-building-portfolio.html` for an existing placeholder slot for the carousel — if none, flag to Della before adding.

### 6. Close out

- Append Session 16 entry to `~/CoworkWorkspace/Get-a-job/BUILD-LOG.md`
- Update `figma-handoff-case-building-portfolio.md` — flip all 5 pending rows to ✅, note the reposition, note the deploy
- Update `SESSION-STATE.md` if it has a case-building-portfolio block

**Success criteria:**

1. Sentinel-test passes before any build work
2. port-03b-principles is at y=6849 on canvas
3. All 5 pending mobile frames exist at their planned y-anchors with valid node IDs
4. Tracker rows all flipped to `figma-mobile-built`, `figma_mobile_node_id` populated
5. port-01a-carousel HTML deployed and reachable from live portfolio (or flagged to Della if a placeholder needs adding first)
6. BUILD-LOG + handoff doc updated

**Known gotchas from Session 15:**

- Figma MCP write channel silently no-ops (returns `"Code executed with no return value"` with no error thrown even if you `throw` inside the script). Only reliable signal is a round-trip read via `get_metadata` or `get_screenshot`.
- `get_metadata` on this page returns ~245k chars — too large for the tool response. Save to a file first (use the file-save mode of `get_metadata` if available, else chunk reads).
- Della does not have the Figma Dev Mode MCP Server setting visible in Preferences — don't ask her to toggle it again, she spent time hunting last session.

**If anything requires a decision Della needs to make**, ask once with the options laid out, then proceed on her signal. Don't loop on clarifications.

Good luck. You've got solid ground — 2 frames already live, all 7 HTML sources in place, tracker scaffolded, handoff doc accurate. Just need the Figma channel cooperating and an hour of batch work.

## ▲▲▲ END OF PROMPT TO PASTE ▲▲▲

---

## Session 15 quick-reference (for my own records, not part of the pasted prompt)

- **Carousel HTML file written:** `working/diagrams/v3/diagram-port01a-carousel.html` (session 15 new)
- **Tracker rows added:** 7 (port-01a-grid, port-01a-carousel, port-01d-implication, port-03a1-thumbnails, port-03b-principles, port-03c-design-system, port-04b-governance)
- **Tracker backup:** `audit-tracker.xlsx.bak-sess10`
- **Figma frames landed:** `975:14` (implication, y=4531), `975:24` (principles, y=7408 — needs reposition to 6849)
- **BUILD-LOG entry:** "Apr 22, 2026 (session 15 — html-to-figma case-building-portfolio scope expansion thread)"
- **Handoff doc:** `reports/figma-handoff-case-building-portfolio.md` — "Session 15 Extension" section added at top
