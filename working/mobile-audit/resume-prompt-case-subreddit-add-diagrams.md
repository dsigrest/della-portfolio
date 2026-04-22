# Resume Prompt — case-subreddit additional Figma pairings

**Use this prompt when:** Della has added one or more new diagram HTML files for case-subreddit (either brand-new diagrams or ones she's bringing back from older explorations) and needs mobile Figma frames paired for them in the same native-layer style as the first 10.

**Paste this entire file as the opening message of a fresh Cowork thread.**

---

## Context (what's already done — do not redo)

Session 11 (2026-04-22) completed the first batch of 10 case-subreddit mobile Figma pairings: sub01, sub02, sub03, sub04, sub05, sub06, sub08, sub09, sub11, sub12. All 10 are native-layer translations (no image fills), placed at `x = -1634` on page `29:40` of Figma file `TArUrZsBUocaAsqetjXq7V`, with CSS-selector layer names preserved for `figma-to-html` roundtrip. Tracker rows populated. Handoff doc v2 entry complete.

**You are picking up where session 11 left off** — pairing the *remaining* sub-* diagrams Della has HTML for but that weren't in the initial 10.

---

## Pre-flight reads (mandatory, in order)

1. `~/CoworkWorkspace/CLAUDE.md` — global voice + session rules
2. `~/CoworkWorkspace/Get-a-job/CLAUDE.md` — project-specific rules
3. `~/CoworkWorkspace/Get-a-job/SESSION-STATE.md` — current state (will say "Session 11 complete, case-subreddit all 10 paired")
4. `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/figma-handoff-case-subreddit.md` — v2 entry at bottom has the final node-ID table and native-build technique notes
5. `~/CoworkWorkspace/Get-a-job/BUILD-LOG.md` — read the Session 11 entry (search for "session 11 — html-to-figma case-subreddit thread") for the full technique playbook
6. `~/CoworkWorkspace/Skills/html-to-figma/SKILL.md` — the skill that owns native-layer translation (v1.0.0+)

---

## Task

For each diagram Della names, or for every HTML file in `portfolio-site/img/diagrams/diagram-sub*.html` that is NOT currently embedded in `portfolio-site/case-subreddit.html` (if she wants you to discover the set automatically):

1. Build a mobile Figma frame in `TArUrZsBUocaAsqetjXq7V` page `29:40` via `html-to-figma` (native mode, no image fills).
2. Name it `<diagram-id>-mobile` matching the convention from session 11 (e.g., `sub12t-mobile` for `diagram-sub12-text-bars.html`).
3. Place at `x = -1634`, y matching the corresponding desktop frame's y on the page.
4. Verify with `get_screenshot`.
5. Update `working/mobile-audit/audit-tracker.xlsx` atomically via `tracker-helpers.py`.
6. Update the handoff doc v3 entry with the new node IDs.
7. Append a Session 12 entry to `BUILD-LOG.md`.
8. Update `SESSION-STATE.md` with the new paired diagrams.

---

## Step 1 — Discovery (identify which diagrams to pair)

Run this to find HTML files that exist but aren't live in `case-subreddit.html`:

```bash
cd /Users/dellasigrest/CoworkWorkspace/Get-a-job/portfolio-site
for f in img/diagrams/diagram-sub*.html; do
  name=$(basename "$f")
  if ! grep -q "$name" case-subreddit.html; then
    echo "NOT LIVE: $f  ($(wc -l < "$f") lines)"
  fi
done
```

Then check the Figma page `29:40` for desktop frames that match those HTMLs. Frame-name convention in the Figma file: `SUB-XX[a-z] — Title`. For example:
- `diagram-sub12-text-bars.html` corresponds to Figma frame `SUB-12t — Three Pillars` (node `678:1367`)
- A hypothetical `diagram-sub07-legacy-creation-flow.html` would correspond to `SUB-07 — Legacy Creation Flow` (`315:2`)

Use `get_metadata` on `29:40` and grep the XML dump for the title keywords — the node output for this page exceeds the token limit, so save it and grep via Python (pattern from session 11):

```python
import json, re
with open('<path to saved get_metadata output>') as f:
    data = json.load(f)
txt = data[0]['text']
# Find all SUB-* desktop frames
desktop = re.findall(r'id="([^"]+)"\s+name="(SUB-[^"]+)"', txt)
for m in desktop:
    print(m)
```

**Before building anything, show Della the list of diagrams you've identified, matched to their desktop Figma nodes, and get explicit greenlight.** Do not build on autopilot — she may want to skip some or add others not in the auto-discovered set.

---

## Step 2 — Per-diagram build workflow (repeat for each)

For each approved diagram:

### 2a. Read the HTML thoroughly
Use the `Read` tool on the HTML file. Note:
- All colors used (map against the token palette below)
- All font sizes, weights, and family (always Inter + JetBrains Mono)
- SVG content (curves, icons, backgrounds) — determine whether to recreate via `figma.createNodeFromSvg` or assemble from primitives
- Media queries (especially `@media (max-width: 480px)` and `@media (max-width: 320px)`) — these define the mobile-specific layout changes
- Any JavaScript (curves, animations, interactions) — JS does NOT execute in Figma, so you must pre-compute equivalent static output

### 2b. Plan the build before writing code
Write down (in your working notes):
- Root frame size: 375 × estimated_height
- Padding: typically 24/16 on mobile (`@media (max-width: 480px)` rules)
- Auto-layout tree structure (which frames are `VERTICAL`, which are `HORIZONTAL`, which use `layoutWrap='WRAP'`)
- Absolute-positioned elements (red stripes, overlapping badges, SVG overlays)
- Font + color map

### 2c. Execute build via `use_figma`
Use the established pattern from session 11 (documented in `figma-handoff-case-subreddit.md` v2 entry):

**Font loading (mandatory first step):**
```javascript
await Promise.all([
  figma.loadFontAsync({ family: 'Inter', style: 'Regular' }),
  figma.loadFontAsync({ family: 'Inter', style: 'Medium' }),
  figma.loadFontAsync({ family: 'Inter', style: 'Semi Bold' }),  // NOTE: space, not "SemiBold"
  figma.loadFontAsync({ family: 'Inter', style: 'Bold' }),
  figma.loadFontAsync({ family: 'JetBrains Mono', style: 'Regular' }),
  figma.loadFontAsync({ family: 'JetBrains Mono', style: 'Bold' }),
]);
```

**Color tokens (from the diagram CSS `:root` variables):**
```javascript
const CANVAS   = {r: 0x0A/255, g: 0x0C/255, b: 0x16/255};
const ELEVATED = {r: 0x15/255, g: 0x17/255, b: 0x22/255};
const TEXT_PRI = {r: 0xE0/255, g: 0xDF/255, b: 0xE4/255};
const ACCENT   = {r: 127/255,  g: 181/255,  b: 176/255};
const RED      = {r: 196/255,  g: 120/255,  b: 120/255};
const WARM     = {r: 212/255,  g: 165/255,  b: 116/255};
const RESUR    = {r: 196/255,  g: 176/255,  b: 120/255};
const BLUE     = {r: 138/255,  g: 158/255,  b: 196/255};
const hex = (c) => '#' + [c.r, c.g, c.b].map(x => Math.round(x*255).toString(16).padStart(2,'0')).join('');
```

**Stable sizing pattern:**
```javascript
// Frame sizing:
frame.primaryAxisSizingMode = 'FIXED';
frame.resizeWithoutConstraints(width, height);
// BEFORE appending to parent. Then append, then:
frame.layoutAlign = 'STRETCH';

// Text sizing:
textNode.textAutoResize = 'HEIGHT';
textNode.resize(width, textNode.height);
textNode.layoutAlign = 'STRETCH';
```

**Critical ordering (from session 10/11):**
- `parent.appendChild(child)` BEFORE setting `child.x`, `child.y`, or explicit positions
- `layoutPositioning = 'ABSOLUTE'` AFTER appendChild (parent must have `layoutMode !== 'NONE'` first)
- For fixed-geometry decorative children (red stripes, icon frames at fixed dimensions), set `layoutMode = 'NONE'` + explicit `resize(w, h)` — don't let auto-layout hug them

**SVG import:**
```javascript
const svg = figma.createNodeFromSvg(`<svg viewBox="0 0 24 24">
  <path d="..." stroke="%C%" stroke-width="1.5" fill="none" />
</svg>`.replace(/%C%/g, hex(ACCENT)));
```

**Cubic bezier with midpoint control points** (for smooth curves from discrete data points — used on sub01 and sub06 in session 11):
```javascript
const points = [[1,100],[3,85],[5,65],[7,50],[10,35],[14,22],[18,14],[21,10],[25,8],[30,6]];
const xMin = 56, xMax = 630, yMin = 15, yMax = 170;
const toX = (d) => xMin + ((d-1)/29) * (xMax - xMin);
const toY = (p) => yMax - (p/100) * (yMax - yMin);
let linePath = `M${toX(points[0][0]).toFixed(2)},${toY(points[0][1]).toFixed(2)}`;
for (let i = 1; i < points.length; i++) {
  const x0 = toX(points[i-1][0]), y0 = toY(points[i-1][1]);
  const x1 = toX(points[i][0]),   y1 = toY(points[i][1]);
  const cpx = (x0 + x1) / 2;
  linePath += ` C${cpx.toFixed(2)},${y0.toFixed(2)} ${cpx.toFixed(2)},${y1.toFixed(2)} ${x1.toFixed(2)},${y1.toFixed(2)}`;
}
```

**CSS-selector layer naming (mandatory for roundtrip):**
Every frame gets a layer name matching its CSS source selector. Examples from session 11:
- `.heatmap-cell.stall` (variant cell state)
- `.pillar-card.accent` / `.pillar-card.warm` / `.pillar-card.blue`
- `.detail-card` / `.detail-icon`
- `.chart-card` / `.curve-card` / `.gradient-line`
This allows `figma-to-html` to generate matching CSS when Della polishes in Figma.

### 2d. Place the frame
```javascript
const page = await figma.getNodeByIdAsync('29:40');
await figma.setCurrentPageAsync(page);
page.appendChild(rootFrame);
rootFrame.x = -1634;
rootFrame.y = <desktop_frame_y>;  // match the corresponding desktop frame's y
rootFrame.name = '<diagram-id>-mobile';
```

Look up `<desktop_frame_y>` by reading the desktop frame's metadata via `get_metadata` on the specific node ID (smaller payload than the whole page).

### 2e. Verify via screenshot
```
mcp__...__get_screenshot(nodeId=<new-mobile-node-id>, fileKey=TArUrZsBUocaAsqetjXq7V)
```
Inspect the image. Common things that go wrong:
- Layout too tall / too narrow → check `layoutSizingHorizontal='FILL'` and `layoutSizingVertical='HUG'` walked the tree
- Text overflowing → check `textAutoResize='HEIGHT'` on text nodes, `layoutWrap='WRAP'` where appropriate
- Icons rendered as huge boxes → fixed-geometry children need `layoutMode='NONE'`
- Colors wrong → check the hex mapping, not the `{r,g,b}` token

If wrong, patch and re-verify. If right, proceed.

### 2f. Update tracker atomically
```bash
cd /Users/dellasigrest/CoworkWorkspace/Get-a-job/portfolio-site
python3 -c "
import importlib.util
spec = importlib.util.spec_from_file_location('th', 'working/mobile-audit/scripts/tracker-helpers.py')
th = importlib.util.module_from_spec(spec)
spec.loader.exec_module(th)
th.update_row('working/mobile-audit/audit-tracker.xlsx', '<tracker-diagram-id>', {'figma_mobile_node_id': '<new-node-id>'})
"
```

Note: if the diagram isn't in the tracker yet (because it's a newly-added HTML that wasn't in the original audit), use `upsert_row` or `append_row` instead. Check with `th.read_tracker(...)` first. Mirror the schema of existing case-subreddit rows.

---

## Hard constraints (non-negotiable)

1. **Native layers only. No image fills.** Every frame must be real Figma auto-layout + text + vectors + rectangles, fully editable. If you fall back to `createImage` + fill, you've failed the task.
2. **No `tidyPage` on page `29:40`.** Della's desktop cluster is hand-positioned. Place new mobile frames at `x = -1634` and leave every other frame exactly where it is.
3. **No edits to desktop frames.** Don't rename, reposition, restyle, or reparent any `SUB-XX[a-z]` frame — they are Della's canonical reference.
4. **No HTML/CSS edits.** If a render looks wrong, fix the Figma translation — don't modify the source HTML. The source HTML is either already-verified or being written by Della separately.
5. **Tracker writes via `tracker-helpers.py` openpyxl.** Never pandas — pandas rewrites the whole file and loses formatting / formulas.
6. **CSS-selector layer names throughout.** Every frame name preserves its source selector so `figma-to-html` can roundtrip.
7. **Verify every frame with `get_screenshot` before moving on.** Don't batch-build and verify at the end — per-diagram verify-then-update is the established rhythm.
8. **Mutate-then-query pattern for use_figma.** Don't throw `DATA:` in the same call as mutations; it rolls them back. Mutate + commit in one call (the tool returns "no return value"), then query + throw in a follow-up call. See Session 10 BUILD-LOG entry for the full rationale.

---

## Close-the-loop (when all approved diagrams are paired)

1. **Update handoff doc.** Append a v3 entry to `working/mobile-audit/figma-handoff-case-subreddit.md` with a new table listing the additional paired diagrams and their node IDs.
2. **BUILD-LOG.** Append a Session 12 entry summarizing: which diagrams, total time, any new technique quirks discovered, any build failures and their fixes.
3. **SESSION-STATE.md.** Update the case-subreddit block so the "All 10 mobile diagrams translated" table expands to include the new entries. Update the top-of-file "As of" header.
4. **Tracker.** Confirm all new rows have `figma_mobile_node_id` populated.
5. **Show Della the screenshots of each new frame one final time** and confirm she's happy before closing the thread.

---

## If Della is also adding the HTMLs to the live case-subreddit.html

That's a separate follow-up task for yet another thread (the `diagram-deploy` skill handles it — it takes finished HTML and wraps it into the case-study page with proper `.diagram-pair` infrastructure if mobile-variant HTML also exists). Don't do that work in this thread. Just flag it in your close-the-loop summary: "The following diagrams were paired in Figma but are not yet embedded in `case-subreddit.html` — use `diagram-deploy` in a separate thread to add them."

---

## Starter message to kick off

Paste this prompt, then Della will either:
- (a) tell you exactly which new diagram HTMLs to pair, or
- (b) ask you to auto-discover the "has HTML but not live" set first and show her for approval.

Either way — **do the discovery pass first, show her the list, wait for explicit greenlight before building**.
