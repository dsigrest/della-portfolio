# Resume Prompt — SHR UI Screens Deploy Sync + Optional `.diagram-pair` Wiring

**Created:** 2026-04-22 (close of Session 18 Thread B)
**Scope:** 1 urgent deploy sync (shr10) + 8 optional swap-rule wraps in `case-sharing.html`
**Previous thread:** Session 18 — Thread B of SHR UI screens, 8 native-layer Figma mobile frames shipped on page `29:41` at x=-1300.
**Context budget estimate:** 30-50% (mostly file edits + verification, no heavy Figma work)

---

## Pre-flight reads (mandatory, in order)

1. `CoworkWorkspace/CLAUDE.md` — global config, voice rules, file routing, PATH-MAPPINGS
2. `CoworkWorkspace/Get-a-job/CLAUDE.md` — project-specific rules (voice, verify-before-claiming, living-documents)
3. `CoworkWorkspace/Get-a-job/SESSION-STATE.md` — Session 18 close-out context
4. This file — scope, constraints, close-out checklist
5. `CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/handoff-shr-ui-screens-to-figma.md` — the full Thread B handoff with executed node IDs

---

## What Session 18 delivered (recap)

8 SHR UI screens now have:
- ✅ Responsive v4 HTML files at `working/diagrams/v4/SHR-XX-*.html` (Session 13 Thread A)
- ✅ Deployed versions at `portfolio-site/img/diagrams/diagram-shrXX-*-v4.html` (Session 14 Thread C)
- ✅ `.diagram-embed` iframe wrappers in `case-sharing.html` (Session 14 Thread C)
- ✅ Native-layer Figma mobile frames on page `29:41` at x=-1300 (Session 18 Thread B — this is the just-closed thread)

**Executed Figma mobile node IDs:**
| shr01 | shr02 | shr06 | shr07 | shr08 | shr10 | shr11 | shr12 |
|---|---|---|---|---|---|---|---|
| 1011:8 | 1028:8 | 1041:8 | 1043:8 | 1047:8 | 1066:8 | 1073:8 | 1077:8 |

---

## 🚨 Priority 1 — URGENT: Sync deployed shr10 to the redesigned working version

**The problem:** During Thread B, shr10 was redesigned from hub-and-spoke (4 spokes) to a stacked 2×3 grid (6 platform cards) because the original layout overlapped at ≤320px and contradicted the "6 platforms" subtitle. The working file was rewritten:

- `working/diagrams/v4/SHR-10-cross-platform-previews-v4.html` ← **NEW 2×3 grid, Telegram + SMS added**
- `portfolio-site/img/diagrams/diagram-shr10-cross-platform-previews-v4.html` ← **STILL has old hub-and-spoke**

**Right now della-portfolio.vercel.app/case-sharing is serving the broken hub-and-spoke layout.**

### Fix steps

1. **Diff the two files** to confirm the scope of the change:
   ```
   diff <working-shr10> <deployed-shr10>
   ```

2. **Copy working → deployed** with the embed-mode overlay reapplied. The deployed files include `body.embedded` CSS + iframe-detection script that the working files don't have. Reference any existing `diagram-shrXX-*-v4.html` (e.g. shr08) to see the exact embed overlay block.

3. **Run quality checks**:
   ```
   cd portfolio-site && python3 quality-check.py img/diagrams/diagram-shr10-cross-platform-previews-v4.html
   cd portfolio-site && python3 voice-check.py img/diagrams/diagram-shr10-cross-platform-previews-v4.html
   ```

4. **Visual verify at 320 / 375 / 1440** — use Chrome MCP or Playwright if available, or give Della a screenshot command to run. This is the mandatory "verify before claiming" gate — don't tell Della it's done without seeing it render.

5. **Commit + push**:
   - Commit message: something like `fix(case-sharing): sync deployed shr10 to redesigned 2×3 platform grid (6 platforms)`
   - Branch: `main` (portfolio repo has admin bypass on main)
   - Show Della the git commands, don't run `git push` from sandbox

---

## Priority 2 — OPTIONAL: `.diagram-pair` swap-rule wiring

**Context — this is optional, not required:**

The 8 v4 files are RESPONSIVE (single file handles desktop + mobile via CSS media queries). So the current `.diagram-embed` wrappers without `.diagram-pair` already render correctly at all viewports.

A `.diagram-pair` wrapper uses TWO iframes — a desktop variant and a mobile variant — with a CSS `@media (max-width: 768px)` rule in `styles.css` swapping between them. The case has ONE precedent: `shr-fw` at line 354 of `case-sharing.html`, which points to `diagram-shrfw-flywheel-v4.html` + `diagram-shrfw-flywheel-v4-mobile.html`.

**When to add `.diagram-pair` wiring to the 8 SHR UI screens:**
- If Della wants to use `figma-to-html` on the new Figma mobile frames to generate separate `-v4-mobile.html` variants
- If she wants more precision at mobile than the responsive CSS allows
- If there's a specific screen where the single-file responsive approach still feels tight

**When NOT to bother:**
- If the live site renders fine at 375 — the single-file pattern is working

**Recommendation:** **SKIP Priority 2 unless Della explicitly wants it.** The `figma-to-html` skill is the right tool to generate separate mobile variants from the Figma frames built in Thread B — invoke it only when Della says "polish shr01 in Figma and push it back to HTML" or similar. At that point, the output would be `diagram-shrXX-*-v4-mobile.html` and the `case-sharing.html` wrapper would upgrade from `.diagram-embed` to `.diagram-embed.diagram-pair` with two iframe children.

### If Della asks for it anyway, the pattern

For any SHR screen `XX`:

1. Invoke `figma-to-html` skill with the mobile frame (e.g. `shr01-mobile` = `1011:8`) → generates `diagram-shr01-before-share-sheet-v4-mobile.html`
2. Drop mobile file into `portfolio-site/img/diagrams/`
3. Upgrade the `.diagram-embed` wrapper in `case-sharing.html`:
   ```html
   <!-- BEFORE -->
   <div class="case-img-full diagram-embed" data-diagram="shr-01">
     <iframe src="img/diagrams/diagram-shr01-before-share-sheet-v4.html" ...></iframe>
   </div>

   <!-- AFTER -->
   <div class="case-img-full diagram-embed diagram-pair" data-diagram="shr-01">
     <iframe class="desktop-variant" src="img/diagrams/diagram-shr01-before-share-sheet-v4.html" ...></iframe>
     <iframe class="mobile-variant" src="img/diagrams/diagram-shr01-before-share-sheet-v4-mobile.html" ...></iframe>
   </div>
   ```
4. Verify styles.css swap rule covers `.diagram-pair .desktop-variant { display: none; }` + `.diagram-pair .mobile-variant { display: block; }` at `@media (max-width: 768px)` (already in file, no edit needed).
5. `quality-check.py` + `voice-check.py` + visual verify.

---

## Hard constraints (same as all portfolio work)

1. **PATH-MAPPINGS.md** — never show Della a `/sessions/...` path in a terminal command. Always convert to Mac-absolute (`~/CoworkWorkspace/...`).
2. **Verify before claiming** — if you say "shr10 deployed," prove it with a screenshot or a curl of the live URL. Don't guess.
3. **Voice rules** — no filler words in any committed text. Rare for a deploy sync to need voice work, but the commit message still counts.
4. **Never push to git from sandbox** — show Della the commands to run.
5. **Living documents rule** — if you touch `case-sharing.html`, make targeted edits, don't rewrite.

---

## Close-out checklist

- [ ] Priority 1: shr10 deployed file synced to working version, embed-mode overlay preserved
- [ ] Priority 1: quality-check.py + voice-check.py clean
- [ ] Priority 1: visually verified at 320 / 375 / 1440
- [ ] Priority 1: Della pushed the commit
- [ ] Priority 1: Live URL spot-checked (della-portfolio.vercel.app/case-sharing at 375)
- [ ] Priority 2 (if Della opted in): each SHR screen wired with `.diagram-pair` + separate mobile variant
- [ ] Tracker row for shr10 appended with deploy-sync note (optional — the row is already `verified`)
- [ ] `SESSION-STATE.md` updated with new session close-out
- [ ] `BUILD-LOG.md` appended with new session entry

---

## References

- `portfolio-site/working/mobile-audit/handoff-shr-ui-screens-to-figma.md` — Thread B handoff (now closed)
- `portfolio-site/working/mobile-audit/audit-tracker.xlsx` — row 62 is shr10
- `CoworkWorkspace/Skills/html-to-figma/references/plugin-api-gotchas.md` — **NEW** (v1.0.0) — if this session invokes figma-to-html, read it first
- `CoworkWorkspace/Skills/figma-to-html/SKILL.md` — if generating mobile variants
- `CoworkWorkspace/Skills/diagram-deploy/SKILL.md` — if deploying new mobile variants to img/diagrams/
