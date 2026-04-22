# Pending PNG Transfers — NOT-03, NOT-08, NOT-14

**Date:** 2026-04-22
**Status:** Diagrams deployed with `<img>` tags pointing at local paths. The PNG files don't exist yet — 6 404s live on the site until these land.
**Assets needed:** 6 PNGs into `portfolio-site/img/diagrams/assets/`
**Figma URL TTL:** ~7 days — re-fetch if past 2026-04-29.

---

## The pattern (validated on NOT-02)

1. In Chrome, with Della logged into Figma, open the DevTools console on `https://www.figma.com`
2. Paste a snippet that fetches each URL with `credentials: "include"` and triggers a blob download via `<a download>`
3. Files land in `~/Downloads/`
4. `mv` to `~/CoworkWorkspace/Get-a-job/portfolio-site/img/diagrams/assets/` with the exact filenames below

Della ran this flow for NOT-02. The NOT-02 PNGs are already in place at the Mac path above.

---

## Asset URLs (cached 2026-04-22 session 25, expires ~2026-04-29)

### NOT-03 — full inbox before/after (node `709:283`)

| Target filename | Figma asset URL | Notes |
|---|---|---|
| `not03-legacy-inbox.png` | `https://www.figma.com/api/mcp/asset/17d760e7-6022-44b7-8445-fe67f20703d0` | Full legacy mobile screen (~1170×2532) |
| `not03-unified-inbox.png` | `https://www.figma.com/api/mcp/asset/f295d805-b563-49cd-8545-f79d664a338f` | Full redesigned mobile screen (~322×697 aspect) |

### NOT-08 — subreddit header on-ramps (node `709:668`)

| Target filename | Figma asset URL | Notes |
|---|---|---|
| `not08-legacy-subreddit.png` | `https://www.figma.com/api/mcp/asset/9d93f39a-a2fb-44ca-b43f-ccfcb5bb9de5` | Legacy subreddit header banner (~520×150) |
| `not08-unified-subreddit.png` | `https://www.figma.com/api/mcp/asset/841eb14b-9941-4dda-96c4-977e11a48024` | Unified header + on-ramp (~520×197) |

### NOT-14 — navigation simplification (node `709:1010`)

| Target filename | Figma asset URL | Notes |
|---|---|---|
| `not14-legacy-nav.png` | `https://www.figma.com/api/mcp/asset/51474bb8-a9f4-4e55-af03-e65dd2fd1451` | Legacy 5-tab nav, full phone |
| `not14-unified-nav.png` | `https://www.figma.com/api/mcp/asset/bd4a3e0a-dab6-40d6-aec9-0647aa25fb47` | Redesigned 3–4 tab nav, full phone |

**Re-fetch recipe:** run `get_design_context` on each canonical node (709:283, 709:668, 709:1010). Figma Dev Mode MCP under namespace `mcp__8e95afc0-e30e-4e27-bfa2-90ccd2e7b3a9__*` is the working surface — the `mcp__Figma__*` variant errors with "enable Dev Mode MCP Server". Returned constants: `imgUnUnifiedlegacyinbox1`/`img3TabUnifiedInbox2` (NOT-03), `imgCommunityJoinedNotifUi4`/`imgCommunityPageNoNotif2` (NOT-08), `imgUnUnifiedlegacyinbox1`/`img3TabUnifiedInbox3` (NOT-14).

---

## One-liner for after Della moves the files

Once all 6 PNGs are in `~/Downloads/`:

```bash
cd ~/Downloads && \
  mv not03-legacy-inbox.png not03-unified-inbox.png \
     not08-legacy-subreddit.png not08-unified-subreddit.png \
     not14-legacy-nav.png not14-unified-nav.png \
     ~/CoworkWorkspace/Get-a-job/portfolio-site/img/diagrams/assets/
```

---

## Verification after transfer

1. Open `portfolio-site/case-notifications.html` in Chrome at the Mac absolute path
2. Scroll to the NOT-03, NOT-08, NOT-14 sections and confirm each `<img>` renders (no broken-image icon)
3. Hover annotations on NOT-03 and NOT-14 — hotspots should overlay the actual UI, not the placeholder background
4. If hotspot positions look off by a few px, flag the specific image and I'll tune the absolute-position percentages

The diagrams are structurally complete and ship-ready once the PNGs arrive.
