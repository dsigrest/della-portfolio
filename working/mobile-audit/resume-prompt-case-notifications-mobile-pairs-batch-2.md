# Resume Prompt — case-notifications Mobile Pairs for NOT-02 / 03 / 08 / 12 / 14

**Thread type:** Fresh Cowork session, `html-to-figma` skill
**Parent session:** Session 19 (2026-04-22) close-out — case-notifications forward-iterations HTML translation
**Scope:** Build 5 native-layer mobile Figma frames on page `29:43` at x=-1700 to pair with the 5 new HTML diagrams deployed today

---

## Pre-flight reads (in this order)

1. `~/CoworkWorkspace/Get-a-job/CLAUDE.md` + `~/CoworkWorkspace/CLAUDE.md` (global config)
2. `~/CoworkWorkspace/Get-a-job/SESSION-STATE.md` (session 19 entry at top — context for what just shipped)
3. `~/CoworkWorkspace/Get-a-job/BUILD-LOG.md` (session 19 entry for the 5-diagram build context)
4. `~/CoworkWorkspace/Skills/html-to-figma/SKILL.md` + any references it pulls in
5. Session 12's native-layer case-notifications rebuild precedent: grep BUILD-LOG.md for "session 12" — 10 frames rebuilt native at x=-1700 on page `29:43`
6. The 5 HTML sources to translate:
   - `~/CoworkWorkspace/Get-a-job/working/diagrams/v5/diagram-not02-inbox-row-unit-v5.html`
   - `~/CoworkWorkspace/Get-a-job/working/diagrams/v5/diagram-not03-full-inbox-redesign-v5.html`
   - `~/CoworkWorkspace/Get-a-job/working/diagrams/v5/diagram-not08-subreddit-onramps-v5.html`
   - `~/CoworkWorkspace/Get-a-job/working/diagrams/v5/diagram-not12-inbox-layout-experiments-v5.html`
   - `~/CoworkWorkspace/Get-a-job/working/diagrams/v5/diagram-not14-navigation-simplification-v5.html`

---

## Scope

Translate each of the 5 HTML diagrams into a native-layer Figma mobile frame at 375px width on page `29:43` ("1. Notifs & Inbox") in file `TArUrZsBUocaAsqetjXq7V`, positioned at x=-1700 to continue the existing case-notifications mobile cluster Session 12 established. CSS-selector layer naming is mandatory for the figma-to-html roundtrip.

**Out of scope:** the 5 new desktop HTML files already exist at x=0+ on the same page — they shipped in Session 19. This thread is ONLY the mobile pairs.

---

## Per-diagram translation notes

**NOT-02 (inbox row unit)** — canonical desktop node `707:112`. Two-column at desktop; at 375 needs stacked vertical layout (BEFORE row top, AFTER row bottom) with the 4+4 annotations below each image. Cross-highlight pairing should remain — check with Della whether tap-to-pair is useful on mobile or if static display is fine. Image slots: legacy PNG (`not02-legacy-inbox.png`, 1170×2532) + unified PNG (`not02-unified-inbox.png`, 1206×2622).

**NOT-03 (full inbox redesign)** — canonical desktop node `709:283`. Full phone screenshots at desktop are already mobile-sized (322×697 aspect). Stack vertically. Annotations (4+4) sit below their respective phones. Hotspot layer is hover-only on desktop — on mobile, consider replacing hover with persistent subtle overlays on the key numbered regions. Images pending transfer.

**NOT-08 (subreddit on-ramps)** — canonical desktop node `709:668`. Simple stacked 2-card layout at mobile, captions below each. Footer takeaway stays full-width. Images pending transfer.

**NOT-12 (inbox layout experiments)** — canonical desktop node `678:3020`. 3-up card grid at desktop; at mobile, stack vertically. "Best fit" winner badge on the Tabbed card remains. No PNG dependency — SVG schematic layout-icons are inline.

**NOT-14 (navigation simplification)** — canonical desktop node `709:1010`. Two-column at desktop with giant "5" / "3–4" watermarks behind each phone; at mobile, stack vertically and consider whether the watermark should shrink to ~80px or stay prominent. The ring-visibility fix (`isolation: isolate` + z-index layering + opaque backgrounds) must be preserved in the Figma translation — the numeral should not ghost through cards. Images pending transfer.

---

## Hard constraints

1. **Native layers only, no image fills** — Session 10 hard constraint still applies. Use auto-layout + SVG + text nodes.
2. **CSS-selector layer naming** — `.col`, `.screenshot`, `.mock`, `.hotspot-layer`, `.annotation`, `.ann-num`, etc. Match the HTML source's selector names exactly.
3. **x=-1700** — standard case-notifications mobile anchor (established Session 12). Don't re-anchor.
4. **No overlap** with existing mobile frames on page `29:43`. Verify vertical y-coords against Session 12's pairings before positioning.
5. **Two-phase MCP pattern** (Session 17 learning): mutate-and-commit → query-and-throw separately. Never throw inside a mutation — Figma rolls back writes.
6. **tidyPage rule** from global CLAUDE.md — call `await tidyPage(page)` after creating the 5 new frames, don't leave them at arbitrary coordinates.

---

## Close-out checklist

- [ ] All 5 mobile frames live on page `29:43` at x=-1700
- [ ] Each frame has CSS-selector layer names for figma-to-html roundtrip
- [ ] `get_screenshot` verification between every batch
- [ ] Handoff doc appended or new one written at `working/mobile-audit/figma-refs/mobile-pairs-not02-03-08-12-14.md` with executed node IDs
- [ ] `SESSION-STATE.md` updated with session 20 entry at top
- [ ] `BUILD-LOG.md` appended with full session 20 entry
- [ ] Any Figma plugin API lessons added to Della's running list (global CLAUDE.md Figma section)
- [ ] No image fills used — confirm with a quick scan of created frames

---

## Known landmines

- **NOT-02 hotspot positioning** — the desktop hotspot coordinates are tuned to a 520/1170px aspect. At 375 mobile, the percentages should hold but verify against a screenshot-diff.
- **NOT-14 watermark at 375** — 140px mono bold at 760px desktop = ~18% of width. At 375 the same ratio gives ~68px — may read thin. Pilot at 80–100px and ask Della.
- **NOT-03 hotspot accuracy** — hotspots were estimated from the canonical frame; may need 2–3% nudges after Della's real PNG lands. Check both desktop + mobile after PNG transfer.

---

## Mac path conversion reminder

All paths in this prompt use `~/CoworkWorkspace/Get-a-job/…` per `PATH-MAPPINGS.md`. If you see `/sessions/…` paths anywhere in a command, that's a bug — convert before showing Della.
