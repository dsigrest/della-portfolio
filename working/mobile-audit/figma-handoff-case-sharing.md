# Figma Pairing Handoff — case-sharing

**Date:** 2026-04-21
**Source thread:** case-sharing responsive-audit (audit + CSS-fix phases complete)
**Destination thread:** fresh Figma-pairing thread running html-to-figma against the diagrams listed below

This handoff is **the only thing** the Figma thread needs to read to do its job. Don't re-run the audit, don't touch HTML/CSS, don't second-guess severity calls — they're locked.

---

## Status roster

8 diagrams audited. 6 L0 reflow naturally (no Figma pairing needed). 2 require new mobile frames in Figma.

| Diagram | Severity | Status | Mobile HTML to render | Notes |
|---|---|---|---|---|
| shr03 — research overview | L0 | audited → verified after safety-net | n/a | Reflows cleanly, no new asset |
| shr04 — research methodology | **L2** | **fixed** (code-verified) | n/a (CSS-only fix) — render the **same desktop file** at 375 width into the mobile frame | Two L2 bugs fixed in `diagram-shr04-research-methodology-v4.html`: removed `min-width:400px` (mobile clipping) and replaced broken `.flow-row:nth-of-type(N)` selectors with class-based `.flow-row.track-1` / `.track-2` (Recipients cards were silently invisible at every breakpoint) |
| shr05 — behavioral model | L0 | audited → verified after safety-net | n/a | |
| shr09 — screenshot to share | L0 | audited → verified after safety-net | n/a | |
| shr13 — brand expression spectrum | L0 | audited → verified after safety-net | n/a | |
| shr14 — privacy barrier | L0 | audited → verified after safety-net | n/a | |
| shre1 — feedback engine | L0 | audited → verified after safety-net | n/a | |
| shrfw — flywheel | **L3** | **fixed** (code-verified) | `img/diagrams/diagram-shrfw-flywheel-v4-mobile.html` | New mobile variant: vertical 3-card composition with left rail spine (Share→Engage→Trust accent gradient) and a return-arc hook captioned "↺ Removes friction · returns to Share". `case-sharing.html` iframe wrapped in `.diagram-pair` (reused existing styles.css swap rule, did not modify it) |

**Tracker state in `portfolio-site/working/mobile-audit/audit-tracker.xlsx`:**
- 8 case-sharing rows present (50 rows total)
- shr04, shrfw: `status=fixed`, `verify_date=2026-04-21`, `figma_mobile_node_id=""` (this is what the Figma thread fills in)
- 6 L0 rows: `status=audited` until Della's safety-net screenshot pass moves them to `verified`

---

## Target

| Field | Value |
|---|---|
| Figma file key | `TArUrZsBUocaAsqetjXq7V` (Portfolio — Image Inventory) |
| Page name | "3. Sharing & embeds" |
| Page ID | `29:41` |
| Mobile cluster anchor x | **Compute at runtime via v0.2.1 algorithm** (see below — do NOT hardcode) |
| Mobile frame width | 375 |
| Mobile frame height | natural-height-at-375 (let the rendered HTML define it) |
| Frame naming | `shr04-mobile`, `shrfw-mobile` |

### Mobile cluster anchor — v0.2.1 algorithm

Run this at the start of the Figma thread, on page `29:41`:

1. Activate page: `await figma.setCurrentPageAsync(page_29_41)`
2. List `page.children`, filter to top-level frames (skip stickies, skip text-only nodes)
3. `leftmost_x = min(child.x for child in frames)`
4. **First-run anchor:** `mobile_cluster_x = leftmost_x − 1300`
5. **Sanity check before placing frames:** scan for any existing element whose `x + width > mobile_cluster_x`. If yes, the cluster would collide — push anchor further left in 200px increments until clear (manual override pattern, same as case-notifications which used `x = -1700`).
6. Existing `*-mobile` frames? Check by name suffix. None should exist for case-sharing (this is the first pairing pass for this page). If any do, the algorithm fell into "subsequent run" mode — read `figma-pairing-convention.md v0.2.1` for that branch.

**Don't run the default `tidyPage()` on this page.** Desktop frames Della has hand-positioned must not move. Place mobile frames at the computed anchor x; let desktop frames stay where they are.

---

## Per-diagram pairing spec

Resolve `desktop_y` at handoff-execute time by listing children of page `29:41` and matching by frame name. Frame names in this Figma file follow the `SHR-XX` convention (uppercase prefix, double-digit ID).

### shr04 — research methodology (L2)

| Field | Value |
|---|---|
| HTML to render | `portfolio-site/img/diagrams/diagram-shr04-research-methodology-v4.html` |
| Render width | 375 |
| Mobile frame name | `shr04-mobile` |
| Desktop base frame name (for Y lookup) | `SHR-04` (or whatever Della named it — match by `name.startsWith("SHR-04")`) |
| Frame x | mobile_cluster_x (computed above) |
| Frame y | `desktop_base.y` (same row as desktop) |
| Tracker write-back | `figma_mobile_node_id = <new node id>` |

### shrfw — flywheel (L3)

| Field | Value |
|---|---|
| HTML to render | `portfolio-site/img/diagrams/diagram-shrfw-flywheel-v4-mobile.html` ⚠️ **the new mobile file, not the desktop** |
| Render width | 375 |
| Mobile frame name | `shrfw-mobile` |
| Desktop base frame name (for Y lookup) | `SHR-FW` (or whatever Della named it — match by `name.startsWith("SHR-FW")`) |
| Frame x | mobile_cluster_x (computed above) |
| Frame y | `desktop_base.y` (same row as desktop) |
| Tracker write-back | `figma_mobile_node_id = <new node id>` |

---

## Scripts

The Figma thread should use the html-to-figma skill (it owns the render-and-place logic in v0.3.0 of responsive-audit). Pass it this payload:

```json
{
  "case_study_slug": "case-sharing",
  "figma_file_key": "TArUrZsBUocaAsqetjXq7V",
  "target_figma_page": "29:41",
  "diagrams": [
    {
      "diagram_id": "shr04",
      "html_path": "portfolio-site/img/diagrams/diagram-shr04-research-methodology-v4.html",
      "mobile_frame_name": "shr04-mobile",
      "desktop_frame_name_prefix": "SHR-04"
    },
    {
      "diagram_id": "shrfw",
      "html_path": "portfolio-site/img/diagrams/diagram-shrfw-flywheel-v4-mobile.html",
      "mobile_frame_name": "shrfw-mobile",
      "desktop_frame_name_prefix": "SHR-FW"
    }
  ]
}
```

If html-to-figma isn't available or fails, fallback path is the same one used in case-ai/case-subreddit:
- `portfolio-site/working/mobile-audit/scripts/render-mobile-to-figma.py` — primary
- `populate-figma-frames-prep.py` + `populate-figma-frames.js` — manual two-step fallback

---

## Non-negotiables for the Figma thread

1. **Read `figma-pairing-convention.md v0.2.1`** before doing anything. The cluster anchor algorithm and naming convention are non-obvious.
2. **Tracker writes via `tracker-helpers.py` openpyxl atomic** (`update_row`). Never pandas. The Figma thread's only tracker write per diagram is `figma_mobile_node_id`.
3. **Never `tidyPage()` this page.** Della's desktop cluster is hand-positioned and must not move. Add mobile frames to the left of the cluster; leave everything else alone.
4. **Never edit the desktop cluster.** Don't reposition, rename, restyle, or reparent any `SHR-XX` frame.
5. **`atob` byte-array transport.** Per session 4 learnings: base64 transport via `atob` fails inside `use_figma`. Use raw `Uint8Array` of JPEG bytes inline (same pattern that shipped ai19/ai06/ai23/ai24).
6. **One pass per diagram, then verify.** After each pairing call, re-fetch the page, confirm the mobile frame exists at the expected (x, y), confirm the IMAGE fill rendered. If the fill is empty or stretched wrong, re-render and replace; don't ship a broken fill.

---

## Close-the-loop

After the Figma thread completes both pairings:

1. Tracker: shr04 and shrfw rows have `figma_mobile_node_id` populated; status stays `fixed` (becomes `verified` only after Della's safety-net screenshot pass confirms no regression on either).
2. Update `SESSION-STATE.md`: add a "case-sharing — COMPLETE" block mirroring the case-notifications/case-ai entries, with the two new mobile node IDs and a confirmation that the L0 six were verified by safety-net.
3. Append to `BUILD-LOG.md`: two-line entry summarizing the audit (6 L0 / 1 L2 / 1 L3) and the two Figma node IDs created.

---

## What this thread did NOT do (so the Figma thread doesn't redo it)

- ✅ Audit (6 L0 / 1 L2 / 1 L3 / 0 blocked) — locked, in tracker
- ✅ shr04 CSS fix — `min-width` removed + `nth-of-type` selectors replaced with `track-1`/`track-2` classes (touches HTML for the class hooks, but stays inside the single diagram file)
- ✅ shrfw L3 mobile HTML created — `diagram-shrfw-flywheel-v4-mobile.html`
- ✅ shrfw `case-sharing.html` wrapper updated to `.diagram-pair` with desktop-variant + mobile-variant iframes
- ✅ `quality-check.py` passed on all 3 changed files (zero errors, zero warnings)
- ✅ Tracker rows for shr04 and shrfw moved to `status=fixed`

- ❌ Live screenshot capture (deferred to Della's safety-net pass on her Mac: `cd /Users/della/CoworkWorkspace/Get-a-job/portfolio-site && python3 working/mobile-audit/scripts/screenshot-diagrams.py case-sharing`)
- ❌ Figma frame creation (this handoff doc — that's the next thread's job)
- ❌ Tracker `figma_mobile_node_id` writes (Figma thread's job)
- ❌ Moving L0 rows to `verified` (waits on safety-net pass)

---

## Version

- 2026-04-21 — initial. Source: case-sharing responsive-audit, Phase 2 batch.
- 2026-04-22 — **pairing executed, scope expanded to all 8 diagrams** (native-layer only, no image fills per Della's hard constraint). All 8 diagrams now have editable Figma frames on page `29:41`, positioned at x=-1300 with y matching each desktop counterpart. Tracker column `figma_mobile_node_id` populated for all 8.
- 2026-04-29 — **restructure-scope inventory captured** (Session 39 kickoff). 13 in-scope rows including SHR-09b (new) and 5 retired families (SHR-07, SHR-09, SHR-11, SHR-12, SHR-FW). Multi-column canvas filtering pattern documented and wired into figma-to-html v2.8.0 as `references/multi-column-canvas.md`. Future case-study restructures inherit the convention via skill Step 0 reads.

### Executed mobile node IDs (page 29:41)

| Diagram | Mobile node ID | Notes |
|---|---|---|
| shr03 — research overview | `851:8` | Native translation of hub-and-spoke; 2 L0 bonus (scope expansion) |
| shr04 — research methodology | `873:8` | L2 required; vertical flow of 4 cards, track labels intact |
| shr05 — behavioral model | `881:8` | 3 spoke cards stacked vertically with static illustration zones |
| shr09 — screenshot to share | `899:8` | 4 numbered circles vertical with connector lines between |
| shr13 — brand expression spectrum | `833:8` | L0 first-built; established CSS-selector naming pattern |
| shr14 — privacy barrier | `903:8` | "Privacy" word + 3 static red rings + 3 red-accent cards |
| shre1 — feedback engine | `906:8` | 3 step-circles w/ colored dots, vertical connector arrows, loop label |
| shrfw — flywheel | `911:8` | L3 required; rail-spine gradient (teal→warm→blue), 3 cards with rail-nodes, return-arc hook + caption |

**Hard constraint honored:** every frame is fully editable native Figma layers (frames, ellipses, rectangles, text, vectors). No image fills. Della can finesse mobile presentation without roundtripping to HTML first.

**Layer naming:** CSS-selector convention maintained (`.fw-card.fw-card--share`, `.rail-node`, `.spoke-badge.motivators`, etc.) so figma-to-html roundtrip works.

**Not yet done (Della's safety-net pass):** 6 L0 rows still `status=audited`; moves to `verified` after screenshot regression confirms no visual drift.

---

## 2026-04-29 — Restructure scope (Session 39)

**Context:** case-sharing.html restructure kickoff. Della reorganized the canvas in Figma since Apr 22 — added new diagrams (SHR-09b), retired some old ones (SHR-07, SHR-09, SHR-11, SHR-12, SHR-FW), placed others in new positions or duplicated rows. The Apr 22 handoff covers 8 diagrams (mobile-only); this section captures the full restructure inventory of 13 rows including desktop node IDs and out-of-scope retired families.

### Multi-column canvas — the gap that almost re-broke this thread

The Apr 21 pairing-convention algorithm (compute mobile anchor as `leftmost_x − 1300`) handles the mobile cluster placement well. What's NEW for the restructure pass is that the canvas now has multiple parallel columns at distinct x-bands:

- **Mobile column** (in-scope, anchor x ≈ -1300)
- **Desktop column** (in-scope, anchor x ≈ 380)
- **Retired column** (out of scope, x ∈ [-16500, -13900]) — old iterations + 5 retired diagram families
- **Screen bank** (out of scope, x ≈ 18500–19300)
- **Page wrapper** (the giant "Group 2" container at x = -10955, w = 3304, h = 36215)

The figma-to-html skill's rightmost-in-row algorithm (v2.7.0) groups by `(family, y_bucket)` and picks `max(x)` per group. On a single-column canvas this is correct. On this multi-column canvas it picked retired frames from the Retired column when their y-coordinates happened to fall between in-scope rows. The kickoff thread re-derived the x-band filtering pattern manually after Della corrected the inventory row-by-row.

**Captured into figma-to-html v2.8.0** as `references/multi-column-canvas.md`. Future threads inherit the filter automatically.

### Restructure-scope inventory (13 rows, sorted top-to-bottom by y)

Each row has a desktop frame at x ≈ 380 and a mobile frame at x ≈ -1300, both at the same y.

| Row | Family | Desktop node | Mobile node | y | HTML pair (v4) |
|---|---|---|---|---|---|
| 1 | SHR-01 | `233:2` | `1011:8` | -1183 | `diagram-shr01-before-share-sheet-v4.html` |
| 2 | SHR-02 | `237:2` | `1028:8` | 1136 | `diagram-shr02-after-branded-sharing-v4.html` |
| 3 | SHR-03 | `254:2` | `851:8` | 3496 | `diagram-shr03-research-overview-v4.html` |
| 4 | SHR-05 | `276:2` | `881:8` | 5801 | `diagram-shr05-behavioral-model-v4.html` |
| 5 | SHR-04 | `272:2` | `873:8` | 7699 | `diagram-shr04-research-methodology-v4.html` |
| 6 | SHR-06 | `289:2` | `1041:8` | 10198 | `diagram-shr06-before-entry-points-v4.html` |
| 7 | SHR-08 (1st placement) | `299:2` | `1047:8` | 12162 | `diagram-shr08-overflow-standardization-v4.html` |
| 8 | SHR-09b | `1339:1116` | `1339:1135` | 14780 | **NEW — no v4 HTML; build using NOT-07 as template** |
| 9 | SHR-13 | `318:2` | `833:8` | 17700 | `diagram-shr13-brand-expression-spectrum-v4.html` |
| 10 | SHR-10 | `1345:281` | `1066:8` | 19664 | `diagram-shr10-cross-platform-previews-v4.html` |
| 11 | SHR-14 | `321:2` | `903:8` | 22545 | `diagram-shr14-privacy-barrier-v4.html` |
| 12 | SHR-08 (2nd placement, revisit) | `1345:708` | `1345:727` | 24978 | re-uses `diagram-shr08-overflow-standardization-v4.html` (same v4 file embedded in two case-study sections) |
| 13 | SHR-E1 | `621:8` | `906:8` | 28613 | `diagram-shre1-feedback-engine-v4.html` |

### Retired column (out of scope, x ≈ -14000 to -16500)

These families exist on the canvas but are NOT in the main-column restructure. **Do not pull design context from them.**

| Family | Retired desktop | Retired mobile | Why retired |
|---|---|---|---|
| SHR-07 | `295:2` | `1043:8` | Removed from case-sharing.html restructure scope |
| SHR-09 | `303:2` | `899:8` | Replaced by SHR-09b in the new layout |
| SHR-11 | `312:2` | `1073:8` | Removed from case-sharing.html restructure scope |
| SHR-12 | `316:2` | `1077:8` | Removed from case-sharing.html restructure scope |
| SHR-FW | `634:5` | `911:8` | Flywheel removed from new Result section |

Their v4 HTML files remain in `portfolio-site/img/diagrams/` for now; the restructure scope determines whether they get deleted or stay as orphan files at close-out.

### Lineage state at restructure start

All 16 existing case-sharing v4 HTML files (shr01–shr14, shre1, shrfw) **lack `<meta name="figma-source">` lineage tags.** The Figma frames themselves are originally `html-to-figma` outputs from prior sessions (per Apr 22 entry). Della has since deleted/adjusted/replaced individual layers in some frames but never added net-new layers — structure preserved → `figma-to-html` pass translates cleanly with `restore-strip-adjust` discipline (per skill v2.7.0 Step 0).

**Hybrid pattern noted by Della:** several diagrams have flat PNGs nested inside the editable html-to-figma wrapper. Those PNGs stay PNGs on the return trip — only the surrounding wrapper retranslates. Per-row notes flag which diagrams hit this pattern as they ship.

**Lineage tag contract for restructure:** every v5 file written in this scope MUST carry `<meta name="figma-source" content="node:<NODE_ID> page:29:41 file:TArUrZsBUocaAsqetjXq7V">` after roundtripping. This unblocks change detection on subsequent passes.

### Page sanctity rules (still in force from Apr 22)

1. **NEVER call `tidyPage()` on this canvas.** Della's clusters are hand-positioned. Mobile at x=-1300, desktop at x=380. Don't move anything.
2. **NEVER reparent, rename, or move existing frames.** If a frame needs rebuilding, delete → recreate at same (x, y) with the same name.
3. **NEVER add new frames outside the established naming convention.** New variant diagrams use the `SHR-NNx` pattern (e.g. `SHR-09b - desk`, `SHR-09b - mobile`).
4. **NEVER pull design context from a frame in the Retired column** (x < -10000) — those are old iterations, not Della's current intent.
5. **html-to-figma pushes go to x=380 desktop / x=-1300 mobile bands.** When establishing a Figma frame for a new diagram, anchor at these x-coordinates with y matching the desired row position in the column.

### Per-diagram restructure translator notes (append per row as restructure progresses)

*Empty at handoff write — populate as each row ships.*

- **SHR-01** — pending
- **SHR-02** — pending
- **SHR-03** — pending
- **SHR-05** — pending
- **SHR-04** — pending
- **SHR-06** — pending
- **SHR-08 (row 7, 1st placement)** — pending
- **SHR-09b** — pending. Likely fills one of three current case-sharing.html placeholder slots (Custom share sheet v1, v2, Embed tool) — confirm intent at first design-context pull. Build using NOT-07 as the v5 template.
- **SHR-13** — pending
- **SHR-10** — pending
- **SHR-14** — pending
- **SHR-08 (row 12, 2nd placement)** — re-uses the v4 file from row 7. No separate HTML. iframe embedded twice in case-sharing.html under different sections.
- **SHR-E1** — pending
