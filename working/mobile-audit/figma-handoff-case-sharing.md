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
