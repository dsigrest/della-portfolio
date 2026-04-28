# Git Hygiene Retrospective — Sessions 28–32 Noise Accumulation

**Date:** 2026-04-23 (Session 34 — retrospective thread following Session 33 cleanup)
**Predecessor cleanup:** commits `8277342..0651157` on `origin/main` (8 commits, 22 noise items resolved)
**Author:** Claude (autonomous retrospective thread, executed while Della slept — all rule changes pending her morning review)

---

## TL;DR

Session 33 spent several hours resolving 22 noise items that silently accumulated over Sessions 28–32. The cleanup shipped clean. This retrospective answers the question the cleanup did not: **why did the mess accumulate, and how do we prevent a Session 66 rerun?**

Three findings matter most:

1. **The single highest-impact prevention is already in effect.** Moving session scaffolding (resume prompts, plans, handoffs, scratchpads) outside the portfolio git repo at `~/CoworkWorkspace/Get-a-job/sessions/` removes ~14 of the 22 noise items from the portfolio's future surface area. That rule needs to be formalized in global CLAUDE.md so it applies to every project.
2. **Nine noise categories trace back to four root causes.** No end-of-session `git status` sweep, parallel threads that never reconcile, "Retirable when" ambiguity in resume prompts, and ad-hoc skill outputs without gitignore policy.
3. **Three MUST-tier rules + one storage lifecycle rule would have caught all 22 items.** The rules are low-friction (Claude runs the checks, Della approves in under two minutes). Cost is bounded; recurrence prevention is high.

Della's explicit morning asks: **a scalable handoff solution that does not bloat the git repo with unrelated commits, and does not bloat any storage either.** Both are answered below under Scalable Storage Lifecycle.

---

## 1. Noise taxonomy (9 categories, 22 items)

Every item from the Session 33 kickoff's 22-item list appears below, grouped by category. Each category names its root cause + candidate rule tier.

### Category A — Orphan staged-never-committed work (6 items)

| # | Item | Created by |
|---|---|---|
| 1 | `img/diagrams/diagram-sub07-single-text-input.html` | Session 31c |
| 2 | `img/diagrams/diagram-sub10a-disorienting-landing.html` | Session 31c |
| 3 | `img/diagrams/diagram-sub10b-structured-landing.html` | Session 31c |
| 4 | `img/diagrams/diagram-sub11a-surface-adapts-to-stage.html` | Session 31c |
| 5 | `img/diagrams/diagram-sub11b-contextual-depth.html` | Session 31c |
| 6 | `img/diagrams/diagram-sub12s-text-bars-stall-points-static.html` | Session 31c |

**Root cause:** Session 31c staged six HTML files via `git add`, then the thread exited without running `git commit`. No end-of-scope check caught that staging ≠ shipping. The files landed mid-Session-33 as surprise commit `c463d70` when the parallel thread resumed — not through Session 33's triage.

**Candidate rule tier:** MUST.

### Category B — Uncommitted tracked-file edits (4 items)

| # | Item | Created by |
|---|---|---|
| 7 | `working/mobile-audit/audit-tracker.xlsx` (edits layered from 3 sessions) | Sessions 30, 31c, 32 |
| 10 | `portfolio-site/BUILD-LOG.md` (+44 Session 17 entry) | Session 17 |
| 11 | `working/mobile-audit/figma-handoff-case-subreddit.md` (+61 Session 17 addendum) | Session 17 |
| 12 | `working/mobile-audit/handoff-shr-ui-screens-to-figma.md` (Session 26 COMPLETE) | Session 26 |

**Root cause:** Threads edited tracked docs to reflect shipped work but exited before staging the change. Three things compound here. First, the edit step and the stage step are separated by time — the author writes the log entry, context-switches, and forgets to return. Second, the tracker xlsx is an append-heavy living doc that three separate threads stacked edits onto without ever committing a reset point, so each thread inherited an already-dirty tree and stopped treating dirtiness as a signal. Third, no end-of-session sweep surfaced the dirty state before context closed.

**Candidate rule tier:** MUST.

### Category C — Orphan file deletions (2 items)

| # | Item | Created by |
|---|---|---|
| 13 | `working/mobile-audit/figma-refs/not02-legacy-inbox.png` (deleted, not staged) | Session 25 |
| 14 | `working/mobile-audit/figma-refs/not02-unified-inbox.png` (deleted, not staged) | Session 25 |

**Root cause:** PNGs moved from `figma-refs/` to `img/diagrams/assets/` via filesystem move. The `mv` pattern creates a dual effect git sees as "delete + untracked add," and both sides need explicit staging (`git rm` on the source path, `git add` on the destination). Session 25 staged the add; the delete sat pending for 8 sessions. This is a subset of Category B, but the failure mode is specific enough to earn its own rule if the sweep does not already handle deletes explicitly.

**Candidate rule tier:** SHOULD — folded into the same sweep rule as Category B.

### Category D — Orphan retired resume prompts (7 files, item 18)

| Sessions that shipped | Sessions whose prompts sat un-archived |
|---|---|
| 15–27 | ai-ai10+ai16-polish · notifications-png-transfer · case-sharing-close-out · portfolio-pairing-roundtrip · portfolio-ship-complete · shr-deploy-sync · workstream-a-della-review · workstream-a-html-updates · Session 18 figma-polish-to-deploy |

**Root cause:** Every resume prompt carries a "Retirable when X" clause stating what has to happen before the prompt moves to `archive/`. Two failure modes cluster here. First, the clauses are ambiguous — "retirable when Della approves" or "retirable when workstream closes" are abstract conditions with no single observable trigger a thread can check. Second, and more structurally, **no session's explicit scope is "retire predecessor prompts."** Every thread executes a forward-motion scope; retiring last week's prompts is orphan work that belongs to no one, and orphan work accumulates. Three different prompts that shipped in April sat at the root of `working/mobile-audit/` for 15+ days after their scope closed.

**Candidate rule tier:** MUST.

### Category E — Orphan active resume prompts (5 files, items 8, 9, 19)

| # | File | Created by | Why it was uncommitted |
|---|---|---|---|
| 8 | `resume-prompt-case-subreddit-followups.md` | Session 28 | Written to hand off A1/A2 work; author treated it as "in flight" mentally |
| 9 | `resume-prompt-case-subreddit-scope-a2.md` | Session 30 | Successor to #8; same pattern |
| 19a | `resume-prompt-case-notifications-phase3-container-fix.md` | Session 31 | Left uncommitted deliberately (pending phone re-test) — legitimate, not failure |
| 19b | `resume-prompt-html-to-figma-skill-patch-v1.1.0.md` | Session 22 | Written + never committed; may be obsolete after Session 32 bumped to 1.2.0 |
| 19c | `resume-prompt-followup-filename-hygiene.md` | Session 27 | Written + never committed; waiting on Workstream A close |

**Root cause:** Resume prompts are deliverables — they are the artifact a future thread reads to execute the next scope. But they get treated as ephemeral scratch ("I wrote the handoff, my job is done") rather than as the handoff contract itself. Commit discipline for resume prompts specifically broke down.

**Candidate rule tier:** SHOULD. Note: once Category F's "session docs live outside the git repo" MUST rule applies, this category mostly evaporates — the prompts live in `~/CoworkWorkspace/Get-a-job/sessions/` which is not version-controlled at all, so the question of "commit when" stops mattering.

### Category F — Session docs commingled with portfolio code (root cause across D + E + G)

**Not a separate noise category — this is the structural root cause underneath Categories D, E, G, and partially H.** Sessions 15–32 wrote resume prompts, plan docs, scratchpads, and reports into `portfolio-site/working/mobile-audit/`. That folder is inside the portfolio git repo. Every resume prompt Della's threads wrote was a choice about whether to pollute portfolio commit history with session scaffolding that has nothing to do with portfolio code.

Session 33 closed this by relocating session scaffolding to `~/CoworkWorkspace/Get-a-job/sessions/` (outside the portfolio repo entirely). This retrospective file is the first artifact written under the new model.

**Candidate rule tier:** MUST — formalize as a global CLAUDE.md rule so every project inherits the separation.

### Category G — Orphan scratchpads without deletion contracts (1 item)

| # | Item | Created by |
|---|---|---|
| 20 | `working/mobile-audit/session32-closeout-content.md` | Session 32 |

**Root cause:** Session 32's close-out needed to append to BUILD-LOG + SESSION-STATE, but both files had exceeded 25K tokens — which is the soft threshold above which Claude's in-place edits become unsafe. Session 32 worked around the limit by writing the content to a scratchpad for a human (or a smaller-context thread) to paste in. But the scratchpad was created with no stated deletion trigger. It sat at the root of `working/mobile-audit/` until the parallel `b24c890` cleanup commit accidentally tracked it into git history before Session 33 could delete it.

**Candidate rule tier:** MUST.

### Category H — Orphan working docs (2 items)

| # | Item | Created by |
|---|---|---|
| 15 | `working/mobile-audit/case-subreddit-followups-plan.md` | Session 28 |
| 16 | `working/mobile-audit/reports/session17-ship-complete.md` | Session 17 |

**Root cause:** Generated during session work, decision to commit was never explicitly made. Similar to Category E — authors treated them as process exhaust, not as artifacts that needed a staging decision. Handled by the same sweep rule.

**Candidate rule tier:** SHOULD — folded into the sweep rule.

### Category I — Unclaimed archive folder (1 item)

| # | Item | Created by |
|---|---|---|
| 17 | `working/mobile-audit/archive/resume-prompt-workstream-a-della-review.md` | Session 28 |

**Root cause:** Session 28 created `working/mobile-audit/archive/` and put a file in it, but `archive/` itself had never been `git add`-ed. First-use of a new folder is a staging gap — the file sat as "untracked inside untracked directory" and was invisible to casual `git status` reads.

**Candidate rule tier:** SHOULD — folded into the sweep rule (the sweep sees untracked directories and flags them).

### Category J — Undecided gitignore policy for skill outputs (2 items)

| # | Item | Size | Created by |
|---|---|---|---|
| 21 | `working/mobile-audit/screenshots/port-ship-complete/` | 11 MB | Session 17 |
| 22 | `working/mobile-audit/screenshots/shr01-html-375-thread-b-gate.png` | ~1 MB | Session 18 |

**Root cause:** The responsive-audit skill and ad-hoc verification scripts write screenshot folders to `working/mobile-audit/screenshots/`. Neither the skill nor Session 17/18 documented whether these outputs should be tracked, gitignored, or promoted to a reports folder. Ambient "Della will decide later" never surfaced as an explicit decision, so the folders accumulated as untracked for several sessions. Session 33 resolved by gitignoring `port-ship-complete/` and `*-gate.png`.

**Candidate rule tier:** MUST for skills that write to `working/` — each carries a gitignore-policy reference.

---

## 2. Cross-cutting root causes (the "why" beneath the categories)

Four process failures produce nine noise categories:

1. **No end-of-session `git status` sweep.** Threads write, stage, or delete files throughout a scope; the stage-it-now step and the commit-it-now step are separated by time. Without a forcing function at session close, dirty state stays dirty and rolls forward. Would have caught Categories A, B, C, G, H, I, J.
2. **Parallel threads create independent artifact streams that never reconcile.** Session 31 spawned three sub-threads (31a, 31b, 31c). Session 32 ran parallel to Session 33's cleanup investigation. Each parallel thread stacks edits on tracked files or creates new files; no coordination commits them. Would be caught by a session-start `git status` check that surfaces prior-thread work.
3. **Resume prompts have retirement ambiguity + no owner for the retire action.** "Retirable when X" is abstract; no session takes retirement as explicit scope. Would be caught by a resume-prompt retire check that runs at every execution close.
4. **Session docs live in the portfolio git repo.** Commingled session scaffolding with portfolio code means every resume prompt was a commit-vs-don't-commit decision, and most threads deferred. Resolved by relocating to `sessions/` outside the repo (Session 33).

A fifth underlying issue is worth naming even though it sits adjacent to git hygiene: **Living docs (BUILD-LOG, SESSION-STATE) exceed safe in-place edit thresholds**, which drives scratchpad workarounds without deletion contracts. Not a git-hygiene rule strictly, but it causes Category G and deserves a tag.

---

## 3. Prevention rules

Three tiers. MUST rules would have caught every item in the 22-item list. SHOULD rules cover patterns that MUST rules also cover, but which benefit from explicit documentation. MAY rules are opt-in patterns worth naming but not worth forcing.

### MUST tier

**M1. Session docs live outside the git repo.** Every project's session scaffolding (resume prompts, plans, handoffs, scratchpads, retrospective reports) lives at `~/CoworkWorkspace/<project>/sessions/`, NOT inside any git-tracked subfolder. This folder is intentionally outside version control. Artifacts that belong to the project itself (code, content, trackers that ship, reports the user wants versioned) stay in the git repo; everything else goes to `sessions/`.

- **Evidence:** Categories D (7 files), E (5 files), F (structural), G (1 file), H (2 files). Roughly 14 of 22 noise items trace to this structural issue.
- **Location:** New section in global `~/CoworkWorkspace/CLAUDE.md`, inherited by project CLAUDE.md files.
- **Tradeoff:** Loses revision history for session docs. Net positive — session docs are write-once handoff contracts, not collaborative living documents, so revision history adds little value and large surface area. Mitigated by Della's Time Machine / iCloud backup.
- **Scalability answer:** This is Della's "scalable handoff that does not bloat the git repo" ask.

**M2. End-of-session `git status` sweep with explicit disposition per item.** Before Claude declares a scope complete, it runs `git status` in every repo touched during the session. For each untracked / modified / staged / deleted item, Claude proposes a disposition (commit / restore / stash / gitignore / leave-as-is-with-reason) and waits for Della's approval. Close-out does not complete while items are ambiguous.

- **Evidence:** Would have caught Categories A (6 items), B (4 items), C (2 items), G (1 item), H (2 items), I (1 item), J (2 items). 18 of 22 items.
- **Location:** Global CLAUDE.md `## Session Protocol → Ending a session` section.
- **Tradeoff:** Adds 30–120 seconds at session close when the tree is dirty. Zero cost when clean. Net positive.

**M3. Resume prompt retire check at execution close.** Any session that executes against a resume prompt's scope ends by either archiving the prompt (`mv` to `sessions/archive/`) or explicitly re-marking it active with the reason logged in BUILD-LOG. "Retirable when X" clauses must specify either (a) "archive at close-out" or (b) "keep active until [single concrete observable trigger]" — abstract conditions like "when Della approves" are banned.

- **Evidence:** Category D (7 files), partially E (5 files).
- **Location:** Global CLAUDE.md `## Session Protocol → Ending a session` + resume-prompt skill Step 8 ("Offer next actions").
- **Tradeoff:** Authors have to commit to concrete retirement triggers at creation time. Small authorial cost; large accumulation savings.

**M4. Scratchpad deletion contract.** Any file Claude creates as a paste-ready or session-close-out scratchpad names a deletion trigger in its first paragraph, lives in `sessions/` (never in `working/`), and gets deleted by the session that created it unless the trigger defers deletion explicitly. If the creating session cannot delete (context exhausted), the next session's close-out sweep surfaces it and asks.

- **Evidence:** Category G (1 file, but the file sat for 3 sessions).
- **Location:** Global CLAUDE.md `## Session Protocol → During a session` section.
- **Tradeoff:** Adds one sentence to every scratchpad. Trivial.

### SHOULD tier

**S1. Resume prompt close-out block names exact commands.** Every resume prompt ends with the file-specific `git add` / `git commit` / `mv` commands the executing thread should emit. No `git add -A`, no placeholders.

- **Evidence:** Category E (5 files) — the files executing threads created but never committed.
- **Location:** resume-prompt skill `references/structure-template.md`, version bump to 1.0.2.
- **Tradeoff:** Small authorial cost. Already partially covered by M2 sweep.

**S2. Parallel-thread pickup check at session start.** Session start protocol runs `git status` as the first action and surfaces any uncommitted work from prior threads. If uncommitted work exists, ask Della whether to handle now or defer before starting the scope.

- **Evidence:** Root cause #2. Three parallel Session 31 threads + Session 32 stacking tracker edits (items 1–7).
- **Location:** Global CLAUDE.md `## Session Protocol → Starting a session` section.
- **Tradeoff:** Adds 15 seconds at session start when tree is clean. Higher cost when dirty — but the alternative is letting the dirtiness compound.

**S3. Gitignore policy per skill that writes to `working/`.** Any skill that creates files under `working/<subfolder>/` carries a `references/gitignore-policy.md` documenting what should and should not be tracked. Skill output paths are added to `.gitignore` or whitelisted explicitly at install time.

- **Evidence:** Category J (2 items, 12 MB of untracked screenshots).
- **Location:** skill-forge SKILL.md quality checklist; audit existing skills (responsive-audit, codesign, interview-prep, screenshot-sorter) and add the reference file to any that writes to `working/`.
- **Tradeoff:** Small skill-authoring cost.

**S4. Living doc split rule.** SESSION-STATE.md and BUILD-LOG.md each get a size threshold (proposed: 50 KB or 1500 lines). When the threshold is approached, the oldest year/quarter worth of entries archives to a dated sibling file (e.g., `BUILD-LOG-2026-Q1.md`) instead of driving scratchpad workarounds.

- **Evidence:** Category G root cause (Session 32 hit the 25K-token limit).
- **Location:** Global CLAUDE.md `## Session Protocol → Context management`.
- **Tradeoff:** Occasional archiving pass (5 minutes per quarter).

### MAY tier

**May1. Daily scheduled `git status` digest.** A scheduled task runs every morning at 9 AM across every active project, pipes `git status` output into a single daily digest doc in Della's Drive inbox. Ambient awareness of accumulating noise.

- **Evidence:** Root cause #1. The 5-session accumulation would have surfaced by morning 2.
- **Tradeoff:** Notification noise; most mornings the digest will say "clean." Low ROI if M2 sweep works reliably — skip unless the sweep proves unreliable.

**May2. `session-close-hygiene` standalone skill.** Wraps M2 + M3 + M4 + S2 into a single invocation. Alternative: fold all four checks into `resume-prompt` skill's close-out step. The standalone skill is worth it only if Della routinely wants to run the checks mid-session (not just at close), or if multiple sessions share the same close-out flow.

- **Evidence:** MUST-tier rules benefit from a runner rather than manual recall.
- **Tradeoff:** New skill to maintain. Recommendation: fold into resume-prompt skill unless Della has mid-session use cases.

**May3. Commit message prefix `chore: close-out`.** Distinct category in `git log` so future retrospectives cleanly filter close-out commits from feature commits.

- **Evidence:** Future retrospectives would benefit.
- **Tradeoff:** Small convention change. Opt-in.

---

## 4. Scalable storage lifecycle (Della's explicit morning ask)

Della asked for a solution that does not bloat the git repo with unrelated commits AND does not bloat any storage. M1 handles the git-repo half. The storage half needs an explicit lifecycle.

**Proposed lifecycle for `~/CoworkWorkspace/<project>/sessions/`:**

| Stage | Location | Policy |
|---|---|---|
| Active resume prompts | `sessions/` (loose files at root) | 5–10 files typical. Active handoffs awaiting execution. |
| Archived (recent, last 90 days) | `sessions/archive/` | Loose files. Scope closed, retention for quick lookup. |
| Archived (older, >90 days) | `sessions/archive/older/<YYYY-QQ>.tar.gz` | Compressed quarterly bundles. Preserves history at ~20× compression. |
| Purged | Deleted | Optional annual purge of tarballs older than 1 year. Della's call. |

**Size projections** (rough):

- Active resume prompts: ~15 KB each × 10 = 150 KB
- Recent archive: ~15 KB each × 40 = 600 KB
- Quarterly tarball: ~20 KB per quarter after compression
- Annual footprint: well under 1 MB per project

**Automation:** a scheduled task (weekly or monthly) checks `sessions/archive/` for files with mtime >90 days and rolls them into the quarterly tarball. This is a candidate for the `schedule` skill.

---

## 5. Three decisions for Della's morning review

### Decision 1 — Friction tolerance at session close

If Della accepts 30–120 seconds at session close for a sweep that Claude runs (not Della remembers), MUST tier rules can be ambitious. If she wants zero added friction, MAY tier dominates and the 22-item recurrence rate stays roughly where it is today.

**Recommended default:** Accept the sweep. It is cheap when the tree is clean (15 seconds) and prevents the multi-hour Session 33 cleanup.

### Decision 2 — Skill placement for the sweep

Two options:

- **Option A — Fold into `resume-prompt` skill's close-out step.** Every session that ends with a handoff already invokes resume-prompt. Adding the sweep to its close-out block costs nothing to the user.
- **Option B — Build standalone `session-close-hygiene` skill.** Separate invocation. Makes sense only if she wants the sweep available mid-session (e.g., before a long context break) or without writing a handoff.

**Recommended default:** Option A. Lower maintenance. Consolidate the close-out ritual in one skill.

### Decision 3 — Daily `git status` digest via scheduled task

Morning email/Drive doc showing `git status` across every active project. Ambient awareness of accumulating noise.

**Recommended default:** Skip unless M2 sweep proves unreliable in practice. Re-evaluate after 30 days of running M2.

---

## 6. Proposed CLAUDE.md edits (drafts — pending Della's approval)

Edits for each MUST-tier rule are drafted in a companion document:

**File:** `~/CoworkWorkspace/Get-a-job/sessions/git-hygiene-morning-review-2026-04-23.md`

That doc contains:

- Exact diffs for `~/CoworkWorkspace/CLAUDE.md` (three new rules: M1, M2+S2, M3+M4)
- Exact diffs for `~/CoworkWorkspace/Get-a-job/CLAUDE.md` (inherit + project-specific storage lifecycle note)
- Proposed version bump + content for `~/CoworkWorkspace/Skills/resume-prompt/SKILL.md` if Della picks Option A for Decision 2
- Skeleton for `sessions/` storage lifecycle scheduled task

**No edits applied.** Every diff is draft-only until Della signs off.

---

## 7. Ship criteria (self-check)

- [x] All 22 noise items appear in the taxonomy (Categories A–J).
- [x] Every category has at least one cited noise item + root-cause paragraph.
- [x] Every proposed rule cites at least one noise item as evidence.
- [x] Every proposed rule names its tier with a one-sentence rationale.
- [x] Tradeoff analysis present for each rule.
- [x] Scalable storage lifecycle answers Della's explicit ask.
- [x] Three decisions queued with recommended defaults.
- [x] No CLAUDE.md edits applied. All diffs are drafts pending approval.
- [ ] Voice-check run on this file (pending).
- [ ] Quality-check run on any portfolio files (not applicable — this report touches zero portfolio code).

---

## 8. Carry-forward to the morning

Della should read, in order:

1. This file (retrospective report, ~15-minute read).
2. `~/CoworkWorkspace/Get-a-job/sessions/git-hygiene-morning-review-2026-04-23.md` (the decision doc with draft diffs).
3. `~/CoworkWorkspace/Get-a-job/SESSION-STATE.md` (Session 34 "As of" block, drafted but not saved — lives in the morning-review doc for her to paste).
4. `~/CoworkWorkspace/Get-a-job/BUILD-LOG.md` (Session 34 entry, drafted but not saved — same).

Every change is staged as a draft. Her approval is required before anything touches a CLAUDE.md, a skill, or a scheduled task.
