# Resume Prompt — case-notifications PNG Transfer + Clean Commit

**Thread type:** Fresh Cowork session
**Parent session:** Session 19 (2026-04-22) — NOT-02/03/08/12/14 diagrams deployed but 6 PNGs still pending transfer; pre-commit hooks blocked the commit
**Goal:** Get the 6 pending PNGs from Figma → portfolio-site/img/diagrams/assets/, then run clean commit + push. Should take ~10–15 min if Figma Dev Mode MCP is available.

---

## Why this is a fresh thread

The parent thread's Figma Dev Mode MCP wasn't connected (needed Figma desktop with Dev Mode MCP Server enabled). Della confirmed the MCP runs fine in her other threads, so a fresh start should pick it up. If it doesn't, fall back to manual export from Figma desktop (File > Export frame as PNG).

---

## Pre-flight reads

1. `~/CoworkWorkspace/CLAUDE.md` + `~/CoworkWorkspace/Get-a-job/CLAUDE.md` (global + project config)
2. `~/CoworkWorkspace/Get-a-job/PATH-MAPPINGS.md` (mandatory before any terminal commands)
3. `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/figma-refs/pending-png-transfers.md` (the recipe, filenames, expected paths)
4. `~/CoworkWorkspace/Get-a-job/SESSION-STATE.md` (session 19 context — what shipped, what's blocked)

---

## Verify Figma MCP is live

First call: `mcp__Figma__get_screenshot` (no args) or `get_metadata` against file `TArUrZsBUocaAsqetjXq7V`. If it returns "Dev Mode MCP Server" error, ask Della to enable it:

> Figma desktop app → upper-left menu → Preferences → Enable Dev Mode MCP Server → restart Cowork.

If she can't or doesn't want to, fall back to **manual export** (below).

---

## Path A — MCP-powered transfer (preferred)

### Step 1: Re-fetch asset URLs

For each of the 3 nodes, call `get_design_context` and extract the asset URLs:

- **NOT-03** node `709:283` (file `TArUrZsBUocaAsqetjXq7V`) — expect 2 image references: `not03-legacy-inbox.png` (~1170×2532), `not03-unified-inbox.png` (~322×697 aspect)
- **NOT-08** node `709:668` — expect 2: `not08-legacy-subreddit.png` (~520×150), `not08-unified-subreddit.png` (~520×197)
- **NOT-14** node `709:1010` — expect 2: `not14-legacy-nav.png`, `not14-unified-nav.png` (both full phone)

Figma MCP returns `localhost:3845/assets/...` URLs that map to `figma.com/api/mcp/asset/...`. Use the `figma.com` URLs in the Chrome download snippet.

### Step 2: Give Della a Chrome console snippet

Same pattern that worked for NOT-02. Something like:

```javascript
const urls = {
  'not03-legacy-inbox.png': 'https://figma.com/api/mcp/asset/...',
  'not03-unified-inbox.png': 'https://figma.com/api/mcp/asset/...',
  'not08-legacy-subreddit.png': 'https://figma.com/api/mcp/asset/...',
  'not08-unified-subreddit.png': 'https://figma.com/api/mcp/asset/...',
  'not14-legacy-nav.png': 'https://figma.com/api/mcp/asset/...',
  'not14-unified-nav.png': 'https://figma.com/api/mcp/asset/...'
};
for (const [name, url] of Object.entries(urls)) {
  const blob = await (await fetch(url, { credentials: 'include' })).blob();
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = name;
  a.click();
}
```

Della runs this in DevTools on `https://www.figma.com` (logged in). All 6 files land in `~/Downloads/`.

### Step 3: Move to assets folder

```
cd ~/Downloads && \
  mv not03-legacy-inbox.png not03-unified-inbox.png \
     not08-legacy-subreddit.png not08-unified-subreddit.png \
     not14-legacy-nav.png not14-unified-nav.png \
     ~/CoworkWorkspace/Get-a-job/portfolio-site/img/diagrams/assets/
```

---

## Path B — Manual export fallback

If MCP won't come up:

1. Della opens Figma desktop, file `Portfolio — Image Inventory` (key `TArUrZsBUocaAsqetjXq7V`), page `29:43`
2. For each canonical node (707:112, 709:283, 709:668, 709:1010), select the legacy + unified image inside, right-click → Export selection → PNG 2x
3. Rename downloaded files to match the 6 target filenames above
4. Run the same `mv` one-liner

---

## Step 4: Verify + commit + push

```
cd ~/CoworkWorkspace/Get-a-job/portfolio-site
ls img/diagrams/assets/   # should show 8 files total: NOT-02 (2) + NOT-03 (2) + NOT-08 (2) + NOT-14 (2)
python3 quality-check.py img/diagrams/diagram-not02-inbox-row-unit-v5.html \
        img/diagrams/diagram-not03-full-inbox-redesign-v5.html \
        img/diagrams/diagram-not08-subreddit-onramps-v5.html \
        img/diagrams/diagram-not12-inbox-layout-experiments-v5.html \
        img/diagrams/diagram-not14-navigation-simplification-v5.html
# expect: SUMMARY: 5 files, 30 checks run, 0 errors, 0 warnings

python3 voice-check.py img/diagrams/diagram-not14-navigation-simplification-v5.html
# expect: PASS (may have WARN on long sentence, that's fine)
```

Then the commit + push — UPDATED add list (NOT-02 PNGs now in assets/, 6 new PNGs arriving):

```
cd ~/CoworkWorkspace/Get-a-job/portfolio-site
git add img/diagrams/diagram-not02-inbox-row-unit-v5.html \
        img/diagrams/diagram-not03-full-inbox-redesign-v5.html \
        img/diagrams/diagram-not08-subreddit-onramps-v5.html \
        img/diagrams/diagram-not12-inbox-layout-experiments-v5.html \
        img/diagrams/diagram-not14-navigation-simplification-v5.html \
        img/diagrams/assets/ \
        working/mobile-audit/figma-refs/pending-png-transfers.md \
        working/mobile-audit/resume-prompt-case-notifications-mobile-pairs-batch-2.md \
        working/mobile-audit/case-notifications-forward-iterations-progress.md
git commit -m "case-notifications: deploy NOT-02/03/08/12/14 diagrams + PNGs + mobile-pair handoff"
git push
```

Note: `git add img/diagrams/assets/` catches all 8 PNGs (NOT-02's already-moved pair + the 6 new transfers) in one line.

---

## Final verification

After push lands:

1. Open `~/CoworkWorkspace/Get-a-job/portfolio-site/case-notifications.html` in Chrome
2. Scroll through all 5 embedded diagrams (NOT-02, 03, 08, 12, 14) — no broken-image icons, hotspots overlay actual UI (not placeholder)
3. If NOT-03 or NOT-14 hotspots look a few % off from where they should sit on the real phone screens, flag to Della and we'll tune the absolute-position percentages in a follow-up

---

## Context carryover flags

- **NOT-07A decision:** ARCHIVED 2026-04-22. Della chose NOT-07 (partial/row-level) — isolates the label-design insight, scans in 5s. NOT-07A full-screen variant stays in Figma as exploration only. Tracker already updated.
- **Mobile-pair thread** (`resume-prompt-case-notifications-mobile-pairs-batch-2.md`) — still pending, different thread, different scope.
- **E-series thread** — placement recommendation exists but no kickoff prompt yet. Separate thread when ready.
- **NOT-06 ring visibility fix** — deferred, not blocking.
- **Figma URL TTL:** cached URLs from 2026-04-22 expire ~2026-04-29. If you're past that, re-fetch via `get_design_context`.

---

## Close-out checklist

- [ ] 6 PNGs moved into `img/diagrams/assets/`
- [ ] Quality check passes 5/5 clean
- [ ] Voice check passes NOT-14 (WARN on long sentence is acceptable)
- [ ] Commit lands without hook bypass
- [ ] `git push` succeeds
- [ ] Visual verification in Chrome — no 404s, hotspots aligned
- [ ] SESSION-STATE.md updated with session 20 entry (tight — just "PNG transfer + clean commit")
- [ ] BUILD-LOG.md appended with session 20 entry
- [ ] This resume prompt can be deleted once the commit lands (or moved to `working/mobile-audit/archive/`)

---

## Mac path conversion reminder

All paths use `~/CoworkWorkspace/Get-a-job/…` per `PATH-MAPPINGS.md`. If any `/sessions/…` path appears in a command, convert before showing Della.
