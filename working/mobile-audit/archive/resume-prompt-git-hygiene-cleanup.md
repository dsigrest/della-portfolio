# Resume Prompt — portfolio-site Git Hygiene Cleanup

**Created:** 2026-04-22 (Session 31 close-out — Session 31's Phase 3 container fix + NOT-11 mobile variant landed as commit `6b5a4d5` on `origin/main`. This kickoff hands off the triage of pre-existing working-tree noise accumulated from prior threads that never finished committing cleanly.)
**Status:** ACTIVE — awaiting a fresh thread to execute.
**Predecessor:** None — this is a new scope.
**Successor:** omit.
**Retirable when:** every item in the Key reference table below is resolved (committed, restored, stashed, or gitignored), and `git status` shows a clean working tree (plus any intentionally-untracked items under `.gitignore`).

---

## TL;DR

The portfolio-site working tree at `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/` has accumulated uncommitted modifications and untracked files from multiple prior threads — mostly working docs (resume prompts, screenshots, reports) that belong in `working/` but never got staged, plus a handful of tracked-file modifications with unclear provenance. **Session 31 (responsive-audit Phase 3) already shipped cleanly as commit `6b5a4d5` — do not touch anything from that commit.**

This thread's job: triage every remaining noise item. For each, decide (a) stage + commit as legitimate prior-thread work, (b) `git restore` to match HEAD, (c) `git stash` for later review, or (d) add to `.gitignore` if it shouldn't ever be tracked. Group related items into focused commits — don't land one mega-commit. End state: clean `git status` (working tree clean, or only intentional gitignored items remaining).

Expected duration: 45–90 minutes depending on how much Della wants to preserve vs discard. The work is judgment-heavy (provenance detective work), not mechanically heavy.

---

## Pre-flight reads (mandatory before any work)

1. `/Users/della/CoworkWorkspace/CLAUDE.md` — global voice rules, session protocol, Terminal Command Safety Check, Skill Execution Rule
2. `/Users/della/CoworkWorkspace/PATH-MAPPINGS.md` — sandbox↔Mac path conversion rule; portfolio git repo path
3. `/Users/della/CoworkWorkspace/Get-a-job/CLAUDE.md` — Living Documents Rule, Verify Before Claiming Rule
4. `/Users/della/CoworkWorkspace/Get-a-job/SESSION-STATE.md` — "As of" header describes Session 31 close-out; prior session narratives preserved below give context for most of the noise items
5. `/Users/della/CoworkWorkspace/Get-a-job/BUILD-LOG.md` — Session 28/29/30/31 entries describe which threads created which working docs
6. This file — noise-item catalog + triage decision tree

---

## Non-negotiables (carry forward from global + project rules)

- **Mac absolute paths only in terminal commands.** Every `git` / `cd` / `rm` / `mv` command shown to Della uses `/Users/della/CoworkWorkspace/...` paths from PATH-MAPPINGS. Never emit `/sessions/...` paths.
- **File-specific `git add` per file.** Never `git add -A`, `git add .`, or `git add -u`. Every item goes through explicit staging after a decision is made.
- **Read before edit.** Before deciding fate on any modified file, read the current content AND the HEAD version to understand what changed. Git diff alone is not always enough context.
- **Show diffs before committing.** For every batched commit, show Della the exact `git diff --staged` output + the commit message before pushing.
- **No commits from sandbox.** All `git add` / `git commit` / `git push` / `git restore` / `git stash` commands go to Della for execution. This thread runs locally on the Mac.
- **Do not touch Session 31's commit `6b5a4d5`.** Files shipped in that commit: `img/diagrams/diagram-not06-push-to-inbox-v5.html`, `img/diagrams/diagram-not07-preference-architecture-v5.html`, `img/diagrams/diagram-not09-global-settings-v5.html`, `img/diagrams/diagram-not11-cross-channel-v5.html`, `img/diagrams/diagram-not11-cross-channel-v5-mobile.html`, `case-notifications.html`, `working/mobile-audit/audit-tracker.xlsx`, `working/mobile-audit/case-notifications-responsive-fix-progress.md`, `working/mobile-audit/session31-local-verify.html`.
- **Do not touch `/Users/della/CoworkWorkspace/Skills/`** — separate workspace directory, not tracked by the portfolio-site repo.
- **Get-a-job/BUILD-LOG.md and SESSION-STATE.md live at the project root** (`/Users/della/CoworkWorkspace/Get-a-job/`), NOT inside `portfolio-site/`. Any `BUILD-LOG.md` that shows as modified INSIDE `portfolio-site/` is a separate file — do not stage it without confirming with Della what it is.
- **Pre-commit hook runs quality-check + voice-check on staged HTML files.** Expect it to fire on every commit. Address failures rather than bypassing with `--no-verify`.
- **Confirm before restore.** `git restore` is destructive. Show Della what will be restored and get explicit yes before running.

---

## Start here (thread kickoff flow)

1. Read the pre-flight files (above, in order).
2. Run `cd /Users/della/CoworkWorkspace/Get-a-job/portfolio-site && git status` to get the current noise inventory. Compare against the Key Reference Table below — it's a snapshot from 2026-04-22 post-Session-31-commit; anything new that's appeared since is fair game to add to triage.
3. Ask Della these three upfront (cap at three):
   - For the modified (tracked) files — is there any that she wants to KEEP as a pending change, or should they all get triaged now?
   - For the untracked `resume-prompt-*.md` files — should most of them move to `working/mobile-audit/archive/` (if their scope is closed) or commit as-is (if still active)?
   - What's the `.gitignore` policy for `working/mobile-audit/screenshots/` and `working/mobile-audit/archive/` — always tracked, always ignored, or per-folder decision?
4. Main execution loop — for each row in the Key Reference Table:
   - Read the file (or investigate the folder) to understand provenance.
   - Check BUILD-LOG.md + SESSION-STATE.md for which prior thread created it.
   - Recommend one of: commit / restore / stash / gitignore. State rationale in one sentence.
   - Show Della the recommendation, wait for approval.
   - On approval, emit the exact Mac-absolute-path command for her to run.
5. Batch related commits. Examples of sensible batching:
   - All prior-thread resume prompts that should archive → one `git mv` batch + commit
   - All legitimate unshipped diagrams (sub07/sub10a/sub10b, if confirmed legit) → one commit
   - The four modified-but-stale working docs (figma-handoff-case-subreddit.md, handoff-shr-ui-screens-to-figma.md, figma-refs/not02-*.png deletions, portfolio-site/BUILD-LOG.md) → one cleanup commit OR restore depending on what they contain
6. After each batched commit lands, run `git status` and verify the noise shrunk as expected. Do not declare progress until the status output confirms.
7. Final pass: `git status` shows clean working tree (or only `.gitignore`d items).
8. Close out per the close-out steps below.

---

## Key reference table — noise inventory (snapshot post-commit `6b5a4d5`)

### Modified tracked files (not from Session 31)

| # | File | Status | First-pass provenance guess |
|---|---|---|---|
| 1 | `BUILD-LOG.md` (inside `portfolio-site/`) | modified | Unknown — may be from the parallel Session 31 resume-prompt-skill thread. Check if this file is a separate copy from `Get-a-job/BUILD-LOG.md` or a symlink/mirror. |
| 2 | `working/mobile-audit/figma-handoff-case-subreddit.md` | modified | Prior case-subreddit thread — likely a pending status update that never committed. |
| 3 | `working/mobile-audit/figma-refs/not02-legacy-inbox.png` | deleted | Session 19 or Session 25 PNG transfer work — the NOT-02 PNGs may have been moved to `img/diagrams/assets/` and the `figma-refs/` originals should be cleaned up. |
| 4 | `working/mobile-audit/figma-refs/not02-unified-inbox.png` | deleted | Same as row 3. |
| 5 | `working/mobile-audit/handoff-shr-ui-screens-to-figma.md` | modified | Session 26 case-sharing close-out — status was updated to "COMPLETE + VERIFICATION PASS" but change didn't commit. |

### Untracked files

| # | Path | First-pass provenance guess | Likely disposition |
|---|---|---|---|
| 6 | `img/diagrams/diagram-sub07-single-text-input.html` | Session 28 / Workstream B deferred scope | Probably commit as legitimate. Verify against `case-subreddit-followups-plan.md`. |
| 7 | `img/diagrams/diagram-sub10a-disorienting-landing.html` | Same — Workstream B | Probably commit. |
| 8 | `img/diagrams/diagram-sub10b-structured-landing.html` | Same — Workstream B | Probably commit. |
| 9 | `working/mobile-audit/archive/` | Accumulating archive folder for retired resume prompts | Verify contents, likely commit as-is or gitignore depending on Della's policy. |
| 10 | `working/mobile-audit/case-subreddit-followups-plan.md` | Session 28 case-subreddit followup plan (A1 + A2 scopes) | Commit. Still referenced in SESSION-STATE. |
| 11 | `working/mobile-audit/reports/session17-ship-complete.md` | Session 17 report — case-sharing deploy | Commit OR archive. Check if reports/ is git-tracked in general. |
| 12 | `working/mobile-audit/resume-prompt-case-ai-ai10-ai16-figma-polish-sync.md` | Prior thread kickoff — scope closed | Archive to `working/mobile-audit/archive/`. |
| 13 | `working/mobile-audit/resume-prompt-case-notifications-phase3-container-fix.md` | **Session 31's kickoff** — scope closed this thread | Archive to `working/mobile-audit/archive/` AFTER Della's phone re-test confirms. Until then, leave in place (explicit rule from Session 31). |
| 14 | `working/mobile-audit/resume-prompt-case-notifications-png-transfer.md` | Session 19 / Session 25 PNG transfer — shipped as commit `c7810cd` | Archive to `working/mobile-audit/archive/`. |
| 15 | `working/mobile-audit/resume-prompt-case-sharing-close-out.md` | Session 26 case-sharing close-out — shipped | Archive. |
| 16 | `working/mobile-audit/resume-prompt-case-subreddit-followups.md` | Session 28 followup thread kickoff — status unclear | Check `case-subreddit-followups-plan.md` status. Archive if retired, commit if still active. |
| 17 | `working/mobile-audit/resume-prompt-case-subreddit-scope-a2.md` | Scope A2 thread kickoff — Workstream B HTML authoring | Commit if scope is still open (sub07/10a/10b suggest it is). |
| 18 | `working/mobile-audit/resume-prompt-followup-filename-hygiene.md` | Prior scope | Archive if closed. |
| 19 | `working/mobile-audit/resume-prompt-html-to-figma-skill-patch-v1.1.0.md` | Prior skill-patch scope | Archive if shipped, commit if open. |
| 20 | `working/mobile-audit/resume-prompt-portfolio-pairing-roundtrip.md` | Prior scope | Archive if closed. |
| 21 | `working/mobile-audit/resume-prompt-portfolio-ship-complete.md` | Prior scope | Archive if closed. |
| 22 | `working/mobile-audit/resume-prompt-session18-figma-polish-to-deploy.md` | Session 18 kickoff — shipped | Archive. |
| 23 | `working/mobile-audit/resume-prompt-shr-deploy-sync-and-wire.md` | Prior scope | Archive if closed. |
| 24 | `working/mobile-audit/resume-prompt-workstream-a-html-updates.md` | Session 27/28 Workstream A — shipped as commit `f57865f` | Archive. |
| 25 | `working/mobile-audit/screenshots/port-ship-complete/` | Screenshot folder | Check `.gitignore` — most portfolio-site screenshot folders are gitignored. If not, decide policy. |

### Also not in the current status but worth checking

- `/Users/della/CoworkWorkspace/Get-a-job/BUILD-LOG.md` and `.../SESSION-STATE.md` — these have my Session 31 additions but live at the project root, NOT inside `portfolio-site/`. Confirm they're version-controlled somewhere (separate repo, Time Machine backup, or not at all). If they need to be in version control, that's a separate scope.

---

## Ship criteria

### Per-item ship criteria

A noise item is "resolved" when:

- [ ] Provenance identified (which prior thread, which scope)
- [ ] Disposition decided with Della (commit / restore / stash / gitignore)
- [ ] Command emitted with Mac absolute path
- [ ] Della confirmed the command ran successfully
- [ ] `git status` no longer shows the item (or shows it under the expected section — e.g., ignored)

### Scope-level ship criteria

- [ ] All 25 rows in the Key reference table above resolved
- [ ] `cd /Users/della/CoworkWorkspace/Get-a-job/portfolio-site && git status` returns "nothing to commit, working tree clean" OR only shows intentionally-gitignored items
- [ ] `git log --oneline -5` shows the batched cleanup commits landed cleanly
- [ ] All batched commits pushed to `origin/main`
- [ ] SESSION-STATE.md updated with this scope's close-out
- [ ] BUILD-LOG.md updated with a "Session XX — git hygiene cleanup" entry listing every disposition decision
- [ ] This resume prompt archived to `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/archive/`

---

## When you're done (close-out steps)

1. Update `/Users/della/CoworkWorkspace/Get-a-job/SESSION-STATE.md` top paragraph — prepend a short "As of: <date> (git hygiene cleanup close-out)" block summarizing what got committed / restored / stashed / gitignored in aggregate. Prior Session 31 narrative stays preserved below.
2. Append to `/Users/della/CoworkWorkspace/Get-a-job/BUILD-LOG.md` with a full session entry: disposition decision per noise item, batched commit SHAs, any provenance surprises, lessons learned about workspace hygiene.
3. If this cleanup surfaces a pattern worth preventing (e.g., "resume prompts should auto-archive when their scope closes"), capture it either as (a) a new rule in the relevant project CLAUDE.md or global CLAUDE.md, or (b) a `.gitignore` update, or (c) a learning in `~/CoworkWorkspace/Skills/skill-forge/learnings.md` if it's a meta-lesson about how skills manage their artifacts.
4. Archive this resume prompt:
   - `git mv /Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/resume-prompt-git-hygiene-cleanup.md /Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/archive/`
5. If Session 31's phone re-test confirmed before this thread runs, also archive `resume-prompt-case-notifications-phase3-container-fix.md` as part of this pass.

---

## Voice-check note

**Voice-check:** full lint via `portfolio-site/voice-check.py` against `voice-rules/banned-patterns.yaml` (32 banned patterns loaded) — PASS, 0 errors, 4 long-sentence warnings on TL;DR + ship-criteria blocks (structural, not stylistic). Fresh thread can re-run the check before any in-place edit if the file is revised.
