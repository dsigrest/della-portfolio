# Resume prompt — case-notifications Phase 3 verify

**Paste the message below into a fresh Claude Cowork thread.** Everything you need for Phase 3 is in the workstream handoff doc; this prompt is just the launch.

---

## Kickoff message

Resuming mobile responsive audit on case-notifications — Phase 3.

Previous thread (Session 29) shipped the v4 embed-retrofit on all 10 v5 NOT diagrams: `body.embedded` CSS + iframe detection script + `@media (max-width: 600px)` grid collapse. Commit pushed to `main`; Vercel rebuild should be live. Everything is captured in the living workstream handoff doc:

→ `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/case-notifications-responsive-fix-progress.md`

**START HERE (mandatory reads, in order):**

1. `~/CoworkWorkspace/CLAUDE.md`
2. `~/CoworkWorkspace/PATH-MAPPINGS.md`
3. `~/CoworkWorkspace/Get-a-job/CLAUDE.md`
4. The progress file above — Phase 2 summary + Phase 3+ checklist at the bottom
5. `~/CoworkWorkspace/Skills/responsive-audit/SKILL.md` + references

**Phase 3 objectives (in order):**

### 1. Visual verification on phone (Phase 4 per the progress file)

Hard-refresh the comparison tracker at:
`~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/comparison-tracker-case-notifications-2026-04-22.html`

(open via http://localhost:8000/working/... if assets need to resolve — tracker uses Vercel iframes so it works on file:// too).

Scroll through all 10 diagram cards at 375 and 320. Confirm each:

- NOT-02/03/06/08/09/14 (2-col before/after) — mocks stack vertically, full iframe width, legible
- NOT-04 — 3 level cards stacked; each has a small "1 — Inbox / 2 — Tab / 3 — Row" header at mobile (from `::before` pseudo); horizontal flow arrows gone
- NOT-07 — Before/After preference columns stacked; middle `.transform-arrow` hidden
- NOT-11 — 3 platform cards stacked full-width
- NOT-12 — 3 layout experiment cards stacked

Also do a real phone test of the live `case-notifications.html` on `della-portfolio.vercel.app`. Confirm problems #1, #2, #3, #7, #8, #9 from Della's original 9-problem list are resolved.

### 2. Investigate problems #4, #5, #6 (PNG suspects)

Della's original phone test flagged three problems that the progress file notes may map to the 4 static PNG images on `case-notifications.html` (not the iframe diagrams we just fixed):

- `notif-ds-migration.png`
- `notif-push-landing.png` (Discovery / Following / Conversation cards)
- `notif-pipeline-separation.png`
- `notif-unified-inbox.png` (4-panel progression)

Grep `case-notifications.html` for these, check how they're sized/styled, and see whether any of them show the symptoms Della described: "cards too large vs diagram, cut off" (#4 and #6), "wrong part of header PNG showing" (#5). If a PNG is broken at mobile width, decide Pattern 1 (responsive image CSS) vs. Pattern 2 (build a dedicated mobile image or crop).

### 3. Capture v4 embed-retrofit as skill reference

Per the Lessons → Skill References rule in the global CLAUDE.md, capture the three-piece v4 embed-retrofit pattern into the responsive-audit skill:

- Create `~/CoworkWorkspace/Skills/responsive-audit/references/v4-embed-retrofit.md`
- Document: symptom (v5-era diagrams break at mobile despite existing `@media` rules), cause (missing `body.embedded` + iframe script + restructuring media queries), fix (the exact three-piece pattern applied in Session 29), code recipe (body.embedded CSS block + iframe detection one-liner + `@media (max-width: 600px)` grid collapse), date stamp, version history
- Wire the new file into SKILL.md Step 0 mandatory reads
- Bump skill version: v0.3.x → v0.4.0 (new recipe = minor per semver)
- Log the capture in BUILD-LOG

### 4. (Optional, separate thread) Figma mobile frames

After all 10 diagrams are visually verified, the natural next step is pushing 10 dedicated mobile Figma frames (one per v5 NOT diagram at 375px) via the `html-to-figma` skill. This is the "editable mobile state" that Della asked about. Not blocking — treat as its own focused thread.

### Non-negotiable rules (carry forward)

- Mac absolute paths only in terminal commands (no `/sessions/...`)
- Living documents: additive edits only on the progress file + tracker
- Verify before claiming: actually render / take screenshots / run linters before saying anything is done
- File-specific `git add` per file. Never `git add -A` or `git add .`
- Skill execution: if invoking `html-to-figma` or any skill, actually read its SKILL.md + references, don't summarize

### Close-out when Phase 3 is done

Update the progress file's handoff checklist. Append a Session 30 entry to BUILD-LOG. Update SESSION-STATE "As of" header. Move this kickoff prompt to `working/mobile-audit/archive/` if Phase 3 is fully closed out; leave in place if any items roll forward.
