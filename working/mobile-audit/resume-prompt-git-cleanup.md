# Resume prompt — Git hygiene pass for portfolio-site

**Copy the block below as the first message in a fresh Cowork thread.**

---

Clean up the uncommitted state in `portfolio-site` and decide what to do about the branch-protection bypass that happened in Session 16.

**Background.** Session 16 shipped `35390fa` (carousel deploy + port-01b repair) to `origin/main` via `git push`. The remote logged a bypass of branch protection rules — the repo is configured to require PRs and 3 status checks, but admin rights let the push through. Separately, a `git status` before that commit surfaced a backlog of uncommitted work from prior sessions that needs to be sorted.

**Uncommitted state observed at Session 16 start** (may have grown since — re-run `git status` first):

Modified (tracked):
- `case-ai.html`
- `working/mobile-audit/reports/figma-handoff-case-building-portfolio.md`

Untracked (new):
- `img/diagrams/diagram-ai10-failure-state-v4.html` + `-mobile` variant
- `img/diagrams/diagram-ai16-final-identification-v4.html` + `-mobile` variant
- `working/mobile-audit/audit-tracker.xlsx.bak-sess10`
- `working/mobile-audit/case-notifications-e-series-placement-recommendation.md`
- `working/mobile-audit/case-notifications-forward-iterations-progress.md`
- `working/mobile-audit/figma-refs/` (whole directory)
- `working/mobile-audit/mobile-verify-ai10-ai16.html`
- `working/mobile-audit/resume-prompt-case-ai-add-ai10-ai16.md`
- `working/mobile-audit/resume-prompt-case-building-portfolio-mobile-batch2.md`
- `working/mobile-audit/resume-prompt-case-notifications-forward-iterations-html.md`
- `working/mobile-audit/screenshots/shr01-html-375-thread-b-gate.png`

**Tasks**

1. **Re-run `git status`** in `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/` — the list above is a snapshot; confirm current reality before proceeding.

2. **Categorize each file** by destination:
   - Public & shippable (case study HTML, live diagrams, styles) → commit to `main`
   - Tracking / historical context (audit artifacts, progress docs, resume-prompts) → commit to `main` if useful for future sessions, else gitignore
   - Backups (`*.bak-*`, duplicates) → gitignore
   - Purely ephemeral (one-off screenshots, throwaway HTML) → gitignore or `rm`

3. **Propose a `.gitignore` patch** for anything that shouldn't be tracked. Candidates: `audit-tracker.xlsx.bak-*`, any one-off verification HTML (`mobile-verify-*.html`), temporary screenshots.

4. **Group the remaining committable files into 2–4 coherent commits.** Commit messages in Della's voice (no "implemented", no "stakeholder", no corporate jargon — read the global CLAUDE.md voice rules). Suggested groupings to consider:
   - `case-ai.html` + the `ai10`/`ai16` diagram files ("Integrate ai10 + ai16 diagrams into case-ai")
   - `working/mobile-audit` artifacts ("Mobile audit — session progress tracking")
   - `figma-handoff-case-building-portfolio.md` update ("Handoff doc — Sessions 9 + 15 status")

5. **For each group**, give Della specific commands: `git add` by filename (never `git add -A`), commit message via HEREDOC per `/Users/della/CoworkWorkspace/CLAUDE.md` conventions. Mac-absolute paths only — no `/sessions/` paths.

6. **Flag the branch-protection bypass.** Session 16's push logged:
   ```
   remote: Bypassed rule violations for refs/heads/main:
   remote: - Changes must be made through a pull request.
   remote: - 3 of 3 required status checks are expected.
   ```
   Present Della two options (do not recommend one — let her choose):
   - (a) Keep the rules and route session-scale work through PRs. Requires understanding what the 3 status checks are and whether they run on PRs. Investigation command: `gh api repos/dsigrest/della-portfolio/branches/main/protection`.
   - (b) Relax the rules if they're aspirational rather than actually enforced.

**Mandatory pre-work**

- Read `/Users/della/CoworkWorkspace/CLAUDE.md` — commit message style, git safety rules.
- Read `/Users/della/CoworkWorkspace/Get-a-job/CLAUDE.md` — project-specific conventions.
- Read `/Users/della/CoworkWorkspace/PATH-MAPPINGS.md` — Mac paths required in every terminal command.

**Verification before reporting done**

- For each proposed commit group, open at least one representative file and confirm its content matches the categorization claim. Don't assume the `ai10` diagrams are finished if you haven't looked at them.
- Mentally dry-run each commit: does `git add <files> && git status` show a clean additive diff with nothing unintended?

**Deliverables in chat**

- Categorization table: file → destination → reason
- Proposed `.gitignore` lines
- Numbered commit plan with exact Mac-path commands and HEREDOC messages
- Branch-protection investigation steps + the two options
- A "do NOT commit" list for anything that should stay local, with reasons
