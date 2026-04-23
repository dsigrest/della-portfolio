# Resume prompt — Filename-hygiene sweep for case-subreddit diagrams

**Copy the block below as the first message in a fresh Cowork thread.**

**When to run this thread:** After Workstream A (x=914 polish pass) completes and commits. Do NOT run in parallel with Workstream A — rename churn conflicts with content edits.

---

Filename-hygiene sweep — rename case-subreddit diagram HTMLs where the filename doesn't match the actual diagram content, and update every inbound reference in the repo.

**Background.** During Session 17 Figma introspection, at least one legacy filename mismatch was confirmed: `portfolio-site/img/diagrams/diagram-sub11-text-bars.html` contains the **three-pillars** diagram, not text-bars content. The filename predates the current Figma naming convention on page `29:40` (`SUB-11t — Three Pillars`). Workstream A deliberately left the filename alone to stay scoped. This thread closes that gap and sweeps for any other stale names.

**Goal.** For each case-subreddit diagram HTML in `portfolio-site/img/diagrams/diagram-sub*.html`, confirm the filename matches the actual content. Where it doesn't, rename with `git mv` and update every inbound reference (case-subreddit.html iframe, working/mobile-audit tracker rows, figma-handoff docs, any other repo references).

**Confirmed mismatch:**

| Current filename | Actual content | Figma frame (x=914) | Proposed new name |
|---|---|---|---|
| `diagram-sub11-text-bars.html` | three-pillars | `SUB-11t — Three Pillars` (node `678:1196`) | `diagram-sub11-three-pillars.html` |

**Suspected mismatches to confirm in this thread (inspect each before renaming):**

- All 10 other `diagram-sub*.html` files — compare filename to: (a) inline `<title>` tag, (b) top-level heading visible in desktop render, (c) x=914 Figma frame name on page `29:40`. Flag any others that don't match.
- `diagram-sub12-text-bars.html` — filename suggests "text-bars" but in Session 17 mobile context we also saw "stall points" framing (`SUB-12t — Text Bars` in Figma). If the content is about stall-points / text-bars together, the current filename may actually be fine — verify before touching.

**Workflow per rename:**

1. **Confirm the mismatch.** Open the HTML, read the `<title>` and hero heading. Open the corresponding x=914 Figma frame (introspect page `29:40`). If the current filename misleads a reader vs. the actual content, it's in scope. If it just feels slightly off but still reads the content correctly, leave it.
2. **Present the rename list to Della before any git operations.** One-line justifications per rename. She approves the list explicitly.
3. **`git mv old-name new-name`** — use the git rename, not a copy-delete, so history survives.
4. **Grep for inbound references across the repo.** Expected hits for the confirmed sub11 case:
   - `portfolio-site/case-subreddit.html` — iframe `src=""` reference
   - `portfolio-site/working/mobile-audit/figma-handoff-case-subreddit.md` — Session 17 addendum table
   - `portfolio-site/working/mobile-audit/live-diagrams.md`
   - `portfolio-site/working/mobile-audit/resume-prompt-session18-workstream-a-html-updates.md` (if not yet consumed)
   - Any tracker `.xlsx` `file_path` column — inspect via openpyxl, NOT pandas.
5. **Update every reference.** Use `Edit` tool for text files. For xlsx, use `scripts/tracker-helpers.py` or a dedicated openpyxl script — atomic write + `.bak` backup.
6. **Run `quality-check.py`** — catches broken iframe src paths if a rename was missed somewhere.
7. **Screenshot-verify case-subreddit.html** at 1440 + 375 — confirm the renamed diagram still embeds correctly. No 404s, no broken iframes.
8. **Commit per rename** (or one atomic commit if all renames are batched) — conventional-commit style, Della-voice message, include the xlsx backup in `.gitignore` first if one was created.

**Non-negotiables:**

1. **`git mv`, not copy-delete.** History has to survive the rename.
2. **Rename list approved by Della before any git ops.** This is a breaking change for URLs, iframe embeds, and any external deep-links to specific diagrams. No autopilot.
3. **One thread, one concern.** This thread renames files. It does NOT edit diagram content — Workstream A owns content. If a diagram looks content-wrong mid-rename, flag it and stop.
4. **Tracker writes via openpyxl atomic** (`scripts/tracker-helpers.py`). Never pandas overwrites.
5. **Reference sweep must be exhaustive.** Before committing, run a final `grep -r "old-filename"` across the repo — count should be zero. If any hit remains, fix or explicitly document why it's intentional.
6. **No scope creep to other case studies.** This is case-subreddit only. If the thread discovers `diagram-ai*.html` or `diagram-not-e*.html` mismatches, note them as a separate follow-up — do not fix in this thread.

**Mandatory pre-work:**

- Read `/Users/della/CoworkWorkspace/CLAUDE.md` and `/Users/della/CoworkWorkspace/Get-a-job/CLAUDE.md` — voice rules, verify-before-claiming, terminal-command safety check, living-documents rule.
- Read `/Users/della/CoworkWorkspace/PATH-MAPPINGS.md` — Mac absolute paths required for all terminal commands.
- Read `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/figma-handoff-case-subreddit.md` — Session 17 addendum maps all 11 x=914 frames to their HTML counterparts.
- Confirm Workstream A has completed and committed. This thread cannot run in parallel with content edits.

**Verification before reporting done:**

- `git log --follow <new-name>` shows the history from before the rename — confirms `git mv` preserved lineage.
- `grep -r "<old-name>"` across repo returns zero hits.
- `case-subreddit.html` renders all 11 diagrams without any 404 or broken iframe at 1440 + 375.
- `quality-check.py` passes.
- Tracker xlsx rows carry the new filename in `file_path`; `.bak` backup lives alongside.

**Deliverables in chat:**

- Pre-rename approval table (filename-in vs. filename-out, one-line justification each).
- Final rename commit(s) with SHAs.
- Zero-hit grep confirmation for each old filename.
- Updated tracker row dump — proving the `file_path` column flipped to new names.
- A brief session close-out entry written directly into `BUILD-LOG.md`, matching the Session 17/18 entry structure. Additive, no rewrites.

**Out of scope for this thread:**

- Any diagram content edits (Workstream A owns that).
- Any other case study's diagrams.
- Figma edits.
- Deploy to production (confirm with Della after the rename commits land).

**Stop conditions — surface and wait, don't self-resolve:**

- Any rename affects more than one inbound reference and Della hasn't approved the specific new name yet.
- A grep sweep finds a reference in an unexpected location (skill file, external config, README) — ask before touching.
- A diagram's content looks wrong independent of the filename — flag to Workstream A's owner, do not fix here.
- Any xlsx write fails atomicity check (no `.bak`, stale lock) — stop and surface.
