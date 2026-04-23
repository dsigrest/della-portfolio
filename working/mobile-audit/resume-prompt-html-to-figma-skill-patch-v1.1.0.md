# Resume prompt — html-to-figma v1.1.0 skill patches

**Copy the block below as the first message in a fresh Cowork thread.**

---

Roll the Session 15 + 16 learnings into `html-to-figma` v1.1.0. Four known bugs surfaced across 9 frames built this month; patch the skill so the next batch doesn't repeat them. Use the `skill-forge` meta-skill to drive the change (Define → Build → Evaluate loop with regression eval).

## Mandatory pre-work

1. Read `/Users/della/CoworkWorkspace/Skills/skill-forge/SKILL.md` and `/Users/della/CoworkWorkspace/Skills/skill-forge/learnings.md` in full. Do not summarize — execute the skill's steps.
2. Read `/Users/della/CoworkWorkspace/Skills/html-to-figma/SKILL.md` (current version) in full. If there's a `references/` folder, read every file in it.
3. Read `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/reports/figma-handoff-case-building-portfolio.md` for full session history of bugs caught.
4. Read `/Users/della/CoworkWorkspace/CLAUDE.md` for semver + portability + skill-modification rules (custom skills require evals before "Active" status; update `Skills/SKILLS-REGISTRY.md` after modification).

## The four bugs to fix

### Bug 1 — `reassertFillHug` over-reaches into HUG auto-layout parents

**Symptom:** Tab labels inside HUG-width tab buttons collapsed to 0-width and character-wrapped vertically on the `port-01a-carousel` build. Reproduced on any pattern that uses HUG-wrapping chips (Ramp / Anthropic / Meta / Figma / OpenAI / Cursor tabs).

**Root cause:** The `reassertFillHug` helper walks all auto-layout descendants and forces `layoutSizingHorizontal = 'FILL'`. On a label inside a HUG-width parent, FILL means "fill 0px" (because HUG has no intrinsic width until its children resolve), producing character-wrapped text.

**Patch direction:**
- Before reasserting, inspect each descendant's parent. If the parent's `layoutSizingHorizontal === 'HUG'` and the node is a TEXT, keep the TEXT as `textAutoResize = 'WIDTH_AND_HEIGHT'` + `layoutSizingHorizontal = 'HUG'`. Do not promote it to FILL.
- Alternatively: only call `reassertFillHug` on auto-layout FRAMEs whose children are other FRAMEs, not TEXT nodes. Let TEXT auto-size default through.

**Regression test:** Build a 6-chip HUG-wrapping tab bar at 375px wide. Expect chips to wrap into 2 rows with horizontal text intact. Fail condition: any chip with height > 20px (indicating vertical character wrap).

### Bug 2 — Bar-fill children in non-auto-layout parents get no width

**Symptom:** Carousel dimension bars rendered with no fill color on first pass of `port-01a-carousel`. `barBg` was `layoutMode: 'NONE'`, so the child `barFill` had no anchor and the percent-width calc was never applied.

**Root cause:** The skill's "bars" section assumes auto-layout parents. When the bar background is a fixed-size non-auto-layout frame (needed so fills can overlay with absolute positioning), the child needs explicit `layoutPositioning = 'ABSOLUTE'` + `resize(pxWidth, pxHeight)` at `x = 0, y = 0`. Without those, the child inherits no size.

**Patch direction:** In the skill's bars/fills section, document both patterns:
- Pattern A — auto-layout parent: bar child uses `layoutSizingHorizontal` + the percent-width helper.
- Pattern B — absolute-positioned fill (the CSS `position: absolute; top: 0; left: 0; bottom: 0; width: X%` pattern): parent is `layoutMode: 'NONE'`, child is `layoutPositioning = 'ABSOLUTE'` + explicit `resize(fillWidthPx, barHeightPx)` at `x = 0, y = 0`.

Add a snippet showing how to compute `fillWidthPx` when the parent width is known (e.g., `parentInnerWidth = 375 − (padding * 2)`; `fillWidthPx = Math.round(parentInnerWidth * pct / 100)`).

**Regression test:** Translate a bar-chart card with 5 rows where each bar fills a different percentage (10/25/50/75/100). Expect all 5 fills visible with correct proportional widths at 375px mobile.

### Bug 3 — `strokeDashPattern` not valid on FRAME

**Symptom:** Governance diagram's loopback indicator threw `TypeError: node.strokeDashPattern: no such property 'strokeDashPattern' on FRAME node` when trying to render a dashed border frame.

**Root cause:** `strokeDashPattern` only exists on VECTOR / LINE / POLYGON nodes in the Figma Plugin API. Applying to FRAME silently... actually no, it errors out.

**Patch direction:** Add a constraint note to the skill: "For dashed strokes on non-vector shapes, either (a) use a solid-color stroke with reduced opacity as a visual substitute, or (b) composite the dashed effect as a child VECTOR node overlay with `strokeDashPattern` applied to the vector." Include a short helper `createDashedRect(x, y, w, h, color, dashPattern)` that produces a VECTOR equivalent.

**Regression test:** Translate an HTML element with `border: 1px dashed rgba(196,120,120,0.5)` and verify the Figma output has visible dashing, not a solid stroke.

### Bug 4 — Font name inconsistency: "Semi Bold" vs "SemiBold"

**Symptom:** Font-load failures surfaced occasionally across Session 9/15/16 builds when agents used `"SemiBold"` instead of `"Semi Bold"` (with a space).

**Root cause:** Inter's canonical PostScript name is `"Semi Bold"` (with space). Same for `"Extra Bold"`. Agents inheriting via summarization drop the space.

**Patch direction:** Add an explicit constants block at the top of the skill:

```javascript
const FONTS = {
  interRegular:  { family: 'Inter', style: 'Regular' },
  interMedium:   { family: 'Inter', style: 'Medium' },
  interSemiBold: { family: 'Inter', style: 'Semi Bold' },   // SPACE, not camel
  interBold:     { family: 'Inter', style: 'Bold' },
  interExtraBold:{ family: 'Inter', style: 'Extra Bold' },  // SPACE, not camel
  jetbrainsReg:  { family: 'JetBrains Mono', style: 'Regular' },
  jetbrainsBold: { family: 'JetBrains Mono', style: 'Bold' },
};
```

Require all translations to use these constants. Lint check: reject any raw `"SemiBold"` or `"ExtraBold"` string in a use_figma payload.

**Regression test:** Translate a frame with one sample of each font weight (Regular, Medium, Semi Bold, Bold, Extra Bold, JetBrains Regular, JetBrains Bold). Verify all 7 load without errors on first try.

## Execution instructions for this thread

1. **Invoke skill-forge.** Frame the task as: "Evaluate `html-to-figma` v1.0.0, specify 4 regression tests from the bug list above, patch to v1.1.0, re-evaluate, confirm regression suite passes."
2. **Parallelize the 3-agent loop.** Define agent writes the updated SKILL.md + test specs. Build agent patches the JavaScript helpers. Evaluate agent runs each regression test against a minimal representative HTML file and reports pass/fail with screenshots.
3. **Don't break existing behavior.** The 9 frames already built with v1.0.0 should still translate correctly with v1.1.0. Run at least one of them through as a smoke test (suggest `diagram-port01d-implication.html` — simple, clean, already verified).
4. **Update the skill registry.** After validation, bump version in frontmatter (`version: 1.1.0`), update `Skills/SKILLS-REGISTRY.md` row for html-to-figma, append to `Skills/skill-forge/learnings.md`.
5. **Portability check.** Run the portability checklist from `skill-forge` — is this skill safe to share via git? (No hardcoded Della paths, no Reddit-internal references, generic design-system assumptions.)

## Non-negotiables

- **Read the actual skill file, don't summarize.** The skill execution rule in `CoworkWorkspace/CLAUDE.md` is non-negotiable. Any agent editing html-to-figma reads the current SKILL.md first.
- **Semver.** v1.0.0 → v1.1.0 for backward-compatible bug fixes. Do not bump to 2.0 unless you change the skill's public API.
- **Show Della the diff.** Before saving the patched SKILL.md, show her exactly what changed (unified diff). She approves before commit.
- **Never commit from sandbox.** Give Della the Mac absolute path `git add` / `git commit` commands.
- **Evals required.** Per Della's working preferences: skills must have evals before being marked "Active." If you can't get the regression suite green, keep v1.0.0 as the active version and mark v1.1.0 as `experimental`.

## Deliverables in chat

- Summary of 4 patches landed, with before/after snippets.
- Regression test run report: 4 tests × pass/fail × screenshot.
- Smoke test result on one existing diagram (port-01d-implication or similar).
- Updated `SKILLS-REGISTRY.md` row for html-to-figma.
- Portability checklist result (green / flagged items).
- Git commands for Della to commit the skill change.

## Source references for the bug details

- `/Users/della/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/reports/figma-handoff-case-building-portfolio.md` — Session 15 and 16 write-ups include the exact error messages and reproduction context.
- Session 16 report in the Cowork conversation history — the "html-to-figma v1.1.0 — skill-patch issues encountered" section is the source for this prompt.
- Existing frames to use as "don't break me" smoke tests: nodes `849:14`, `849:35`, `838:14`, `852:14`, `852:95` on page 29:2 of file `TArUrZsBUocaAsqetjXq7V`.
