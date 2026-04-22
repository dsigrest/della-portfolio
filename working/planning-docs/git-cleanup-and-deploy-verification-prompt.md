# Git Cleanup + Deploy Verification — Thread Handoff Prompt

Use this prompt to kick off a fresh Cowork thread. It handles two linked tasks: (1) pushing the backlog of accumulated local changes up through origin/main cleanly, and (2) confirming the case-ai mobile updates are actually live on della-portfolio.vercel.app at 480/375/320.

Copy everything between the horizontal rules into the new thread as your first message.

---

I need you to clean up a backlog of uncommitted local changes in the portfolio-site repo, push everything that should ship, and then verify case-ai mobile diagrams render correctly on the live site. Context: an earlier thread (2026-04-22) finished the case-ai mobile work (ai06, ai19, ai23) and committed just that scope — but it left behind 20+ modified files and several untracked files from prior sessions that had accumulated without being pushed. The branch is also 2+ commits ahead of origin/main from work that was committed but never pushed.

## Pre-flight reads — MANDATORY before any git action

1. `~/CoworkWorkspace/CLAUDE.md` — universal config. Re-read the git safety protocol and the terminal command safety check.
2. `~/CoworkWorkspace/Get-a-job/CLAUDE.md` — project-specific extensions. Re-read verify-before-claiming.
3. `~/CoworkWorkspace/PATH-MAPPINGS.md` — Mac absolute paths. All terminal commands must use `/Users/della/CoworkWorkspace/...` paths, never `/sessions/...`. No exceptions.
4. `~/CoworkWorkspace/Get-a-job/SESSION-STATE.md` — look for the "Pending: commit and push" section to understand what each accumulated workstream was working on. The groupings there are the right mental model for commit scoping.
5. `~/CoworkWorkspace/Get-a-job/portfolio-site/.gitignore` — confirm `mnt/`, `.DS_Store`, and `sessions/` are excluded before doing anything else. If any are missing, add them and stage the `.gitignore` as part of the first cleanup commit.

## Part 1 — Audit the backlog

Run these in Terminal via Bash tool, report results back plainly:

```
cd /Users/della/CoworkWorkspace/Get-a-job/portfolio-site
git fetch origin
git status
git log origin/main..HEAD --oneline
git diff --stat origin/main..HEAD
git diff --stat  # unstaged
```

Classify every modified + untracked file into one of four buckets:

- **A. Real work from prior sessions that should ship** — e.g., diagram HTML files with `-v4.html` suffix that were edited for mobile fixes, `case-*.html` files with diagram-pair wraps, `styles.css` if it has real rule additions. Cross-reference against the "Pending: commit and push" section in SESSION-STATE.md to understand what was meant to ship.
- **B. Local-only files that should NEVER ship** — `mnt/`, `.DS_Store`, sandbox-leak files, personal scratch work. These should be excluded by `.gitignore` or left untracked.
- **C. Ambiguous — surface to Della** — preview HTML files, `L2-responsive-tracker.xlsx` at the repo root, `diagram-viewer.html`, `.craft-context.md`. Don't guess. Present each to Della and ask if it should ship, stay local, or move to `working/`.
- **D. Already gone** — files that exist in git but were removed locally (should show as deleted in git status). Verify each before staging a deletion.

Present the classification as a table to Della before staging anything. Do not `git add .` — ever. Stage files by name, in the groups you propose.

## Part 2 — Commit strategy

Group bucket A files by workstream (case study or project focus) and produce one commit per group. Draft commit messages in advance; show Della all of them before executing. Suggested groupings based on SESSION-STATE.md's pending section:

1. **Session 3 leftovers** — `not11` mobile fix + session-3 resume prompt
2. **Session 4 case-ai responsive fixes** — ai06/ai19/ai24 desktop `-v4.html` CSS additions, `styles.css` `.diagram-pair` rule
3. **Session 4 AI diagram Figma sync** — remaining AI `-v4.html` changes that removed outcome/callout sections
4. **Session 5 case-building-portfolio** — port-02c/03a/05/04a diagrams + `case-building-portfolio.html` + tab-bar fix
5. **Session 6 case-sharing** — shrfw mobile + any other case-sharing follow-ups
6. **Session 7 case-subreddit R1+R2** — 10 sub-* diagrams with CSS + SVG icon replacements, `audit-viewer-case-subreddit.html`, tracker + handoff brief
7. **Session 3 not-e2/e7 L3 redesigns** — if not already committed, the new `-v4-mobile.html` files for flywheel + sankey
8. **`.gitignore` cleanup** — if any entries need adding, ship first so subsequent `git status` is clean

Some of these may already be committed (on the 2-commits-ahead state). Run `git log origin/main..HEAD --oneline` first and skip any group whose commit is already present. Don't double-commit.

Each commit should follow the style in `git log -20`. Do NOT add `Co-Authored-By: Claude` unless Della asks. The portfolio-site history doesn't use that pattern.

## Part 3 — Push

Once all commits are in place locally:

```
cd /Users/della/CoworkWorkspace/Get-a-job/portfolio-site
git log origin/main..HEAD --oneline  # show Della exactly what's about to ship
git push origin main
```

Do NOT push from the sandbox. Present the final `git push` command for Della to run in her Terminal. She'll run it and confirm.

## Part 4 — Wait for Vercel

della-portfolio.vercel.app is wired to auto-deploy on push to main. Wait ~60–90s after push, then verify:

```
curl -I https://della-portfolio.vercel.app/case-ai.html
```

Expect HTTP 200. If 404 or 500, stop and report — the deploy may have failed.

## Part 5 — Verify case-ai mobile is live

Two checks, both required:

**5a. Markup check.** Confirm the live HTML has the `.diagram-pair` wrapper for ai06 and ai19:

```
curl -s https://della-portfolio.vercel.app/case-ai.html | grep -E 'class="case-img-full diagram-embed diagram-pair" data-diagram="ai-(06|19|23)"'
```

Expect three matching lines. If fewer, the deploy is stale or the wrap didn't land.

**5b. Visual check at mobile breakpoints.** Use the Chrome MCP tools (`mcp__Claude_in_Chrome__*`) to:

1. Navigate to `https://della-portfolio.vercel.app/case-ai.html`
2. `resize_window` to 480 × 900, screenshot the page, scroll to ai06, screenshot the diagram
3. Repeat at 375 × 800 — this is the critical breakpoint
4. Repeat at 320 × 800 — worst case
5. For each breakpoint, screenshot ai06, ai19, and ai23 individually (scroll to each)

For each of the 9 diagram screenshots (3 diagrams × 3 breakpoints), confirm:
- All columns render inside the viewport (no horizontal clipping)
- Winner column highlight preserved on ai06 and ai19
- Trust spectrum gradient + 6 signal tags visible on ai23

If anything clips or breaks, stop and report to Della with the specific breakpoint and diagram. Do not claim "live and verified" unless all 9 screenshots render clean.

## Part 6 — Report back

Close the thread with:

1. Summary of what shipped — one line per commit.
2. Final `git log origin/main..HEAD --oneline` output showing everything merged to origin.
3. Live-site verification status — markup check pass/fail, visual check pass/fail per diagram.
4. Any ambiguous files (bucket C) surfaced during audit — with Della's resolution on each.
5. Any files still intentionally uncommitted (bucket B+C that stay local) — so next session knows they're intentional, not forgotten.

Also: update `~/CoworkWorkspace/Get-a-job/SESSION-STATE.md`:
- Remove or update the "Pending: commit and push" section — anything that's now pushed should be struck through or removed.
- Add a new "Pending" entry for whatever ambiguous files Della wants to hold.

## Non-negotiables

- **Mac paths only.** Every terminal command you show Della uses `/Users/della/CoworkWorkspace/...`. Reject any `/sessions/...` path on sight.
- **No `git add .`** — ever. Stage files by name, in groups.
- **No force push.** `git push` only, no `--force`, no `-f`.
- **Never push from the sandbox.** Always give Della the commands to run in her Terminal.
- **Don't commit `mnt/` or `.DS_Store`.** If they're not gitignored yet, fix `.gitignore` first.
- **Verify before claiming "live."** Both markup check AND visual check must pass. If you can't run the Chrome MCP tools because the extension isn't connected, ask Della to install it rather than skipping the check.

## Crash guardrails

- If `git status` shows hundreds of modified files unexpectedly, stop — something is wrong (possibly sandbox leak). Report to Della before doing anything.
- If you hit a merge conflict on push (branch diverged from origin), stop and report — don't force-resolve.
- If a commit you made doesn't make it onto origin after `git push`, stop — re-check state before retrying.
- Don't touch anything outside `~/CoworkWorkspace/Get-a-job/portfolio-site/` during this thread. If another workspace folder needs a push, that's a separate thread.
