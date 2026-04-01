# Stitch + Cursor Workflow — What You Need to Do

**Status:** Research-verified, April 2026  
**For:** Della Sigrest  
**TL;DR:** Sign up for one free tool, install one paid tool, follow the 6-phase loop we've documented.

---

## WHAT'S ALREADY READY (From Us)

We've created:

| File | What It Does |
|------|-------------|
| `DESIGN.md` | Complete design system token reference (colors, spacing, typography, components) |
| `.cursorrules` | Cursor IDE configuration for your portfolio rules |
| `css-improvements.css` | Staging area for CSS refactors (optional, for tracking changes) |
| `stitch-cursor-workflow-guide.md` | 5000-word deep-dive playbook with examples and troubleshooting |

You're starting from a strong position. These files are ready to use.

---

## WHAT YOU NEED TO DO

### Step 1: Sign Up for Google Stitch 2.0 (Free)

**URL:** [stitch.withgoogle.com](https://stitch.withgoogle.com)

- Click the sign-up button
- Use your Google account (same one as your Vercel deployment)
- No waitlist, no credit card required
- Free plan: 550 generations/month (plenty for a portfolio)

**Time investment:** 2 minutes

**Reality check:** Google Stitch 2.0 is real, stable, and actively used for design-to-code. It's a free Google Labs experiment (may charge in Q4 2026, but not now). You can immediately start using it.

---

### Step 2: Install Cursor IDE (Paid: $20/month Pro)

**URL:** [cursor.sh](https://cursor.sh)

- Download and install (works on Mac, Windows, Linux)
- Sign in with GitHub or email
- Choose your plan:
  - **Free Hobby Plan:** Limited code completions, good for testing
  - **Pro ($20/month):** Frontier models, full Visual Editor, MCPs (recommended for portfolio work)

**Why not free?** The Visual Editor (drag-and-drop design mode) requires Pro. Worth it for portfolio iteration.

**Time investment:** 5 minutes to install, 2 minutes to choose plan

**Reality check:** Cursor is a paid tool. If budget is tight, you can use VS Code + browser dev tools + Claude Code for free, but Cursor's Visual Editor speeds up the design→code loop significantly. It's genuinely worth the $20 if you're serious about portfolio iteration.

---

### Step 3: Open Your Portfolio in Cursor

1. Download/install Cursor
2. Click **File → Open Folder**
3. Navigate to `/mnt/Get-a-job/portfolio-site/`
4. Click Open

You should see your HTML, CSS, and image files in the left sidebar.

**Time investment:** 2 minutes

---

### Step 4: Import DESIGN.md Into Stitch

**Option A: Quick Reference (5 minutes)**
1. Open `DESIGN.md` (in your editor)
2. Copy the entire COLOR PALETTE and COMPONENT PATTERNS sections
3. In Stitch, create a new text frame
4. Paste the content
5. Label it "Design Tokens Reference"

This gives you a reference sheet while you design.

**Option B: Direct Use (No import needed)**
- Keep `DESIGN.md` open in a separate window while designing in Stitch
- You don't need to formally "import" it; you just reference it

**Reality check:** Stitch doesn't have a native DESIGN.md import format (yet). Copying the text as reference is the practical solution. The idea of "seamless MCP integration" in the original guide is aspirational — it *could* happen, but right now you manually reference the file.

**Time investment:** 5-10 minutes

---

## THE WORKFLOW YOU'LL REPEAT

This is the proven loop. Do this for every improvement:

### Phase 1: Explore in Stitch (10-30 min)
- Open your Stitch project
- Screenshot your current portfolio site
- Paste screenshot into Stitch
- Sketch 2-3 variations directly on it
- Write notes: "Try this darker teal," "Add 20% more padding here"
- Pick your favorite version

### Phase 2: Consult DESIGN.md (5 min)
- Find the current token values you're changing
- Write down the old values (for documentation later)

### Phase 3: Implement in Cursor (15-60 min)
- Open Cursor, navigate to `styles.css`
- Make CSS changes based on your Stitch exploration
- Use Cursor's Visual Editor to drag/resize/test in real-time, OR edit CSS directly
- Save (Cmd+S)
- See changes instantly in the preview

### Phase 4: Review in Browser (5 min)
- Test desktop, tablet, mobile views
- Check hover states, animations, spacing
- Does it match your Stitch sketch?

### Phase 5: Update DESIGN.md (5 min)
- Update the relevant section with your new values
- This keeps documentation in sync with code

### Phase 6: Deploy (1 min)
```bash
git add .
git commit -m "Your clear message"
git push origin main
```
Vercel auto-deploys. Check it live in 2-3 minutes.

---

## WHAT EACH TOOL DOES (NOT WHAT THE MARKETING SAYS)

### Stitch: Design Exploration
- ✅ Sketch variations quickly
- ✅ Test color/spacing ideas visually
- ✅ Document design decisions with notes
- ✅ Reference your design system (DESIGN.md)
- ❌ Does NOT generate production HTML (ignore that hype)
- ❌ Does NOT directly talk to Cursor (yet)

**Realistic use:** Stitch is a visual whiteboard where you explore *what* to change. Then you manually code it in Cursor.

### Cursor: Code Implementation
- ✅ Full IDE with AI code generation
- ✅ Visual Editor (drag/drop live preview)
- ✅ Real-time preview of CSS changes
- ✅ Mobile responsiveness tester built-in
- ✅ Accessibility checker
- ✅ Git integration (commit/push from IDE)
- ❌ Does NOT automatically fetch Stitch designs

**Realistic use:** Cursor is where you *implement* the changes you decided on in Stitch. The Visual Editor is phenomenal for CSS tweaking.

---

## HONEST ASSESSMENT OF THE ORIGINAL RECOMMENDATION

**What was RIGHT:**
- Stitch 2.0 exists and is genuinely useful for design exploration
- Cursor Visual Editor is real and powerful for HTML/CSS portfolio work
- The 6-phase workflow we documented is sound and repeatable
- Free + $20 is an affordable, practical stack

**What was OVERSOLD or WRONG:**
- "Stitch → Claude via MCP" — Not as seamless as promised. You manually reference DESIGN.md; Claude doesn't automatically pull from Stitch
- "Design.md import" — Stitch doesn't have a native parser for DESIGN.md format yet. You copy/reference it manually
- "Zero setup friction" — Setup takes 15-20 minutes (downloading Cursor, signing up for Stitch, opening files). Not instantaneous
- "Real-time design system sync" — DESIGN.md is updated manually after CSS changes, not automatically

**Bottom line:** The workflow *works*, but it's more manual than the hype suggests. You're not in a futuristic AI design studio yet — you're in a well-organized, practical design→code loop with two good tools and one excellent shared reference file (DESIGN.md).

---

## QUICK CHECKLIST: READY TO START?

- [ ] Downloaded Cursor from [cursor.sh](https://cursor.sh)
- [ ] Chose your Cursor plan (Hobby free or Pro $20/month)
- [ ] Opened your portfolio folder in Cursor
- [ ] Signed up for Stitch at [stitch.withgoogle.com](https://stitch.withgoogle.com)
- [ ] Created a Stitch project named "Della Portfolio"
- [ ] Opened `DESIGN.md` in an editor (have it nearby)
- [ ] Read through the 6-phase loop above (or read `stitch-cursor-workflow-guide.md` for the deep version)

Once all boxes are checked, you're ready to start.

---

## YOUR FIRST TASK (This Week)

1. **Explore in Stitch:** Look at your current portfolio. Pick ONE section (hero, case cards, navigation, whatever). Think: "What would make this feel better? More space? Different color? Better visual hierarchy?"

2. **Sketch 2-3 variations** in Stitch based on your idea

3. **Implement the best one** in Cursor using the 6-phase loop

4. **Deploy it** — git commit and push

5. **Screenshot the result** and compare to your Stitch sketch

This single iteration teaches you the workflow. Everything else flows from this pattern.

---

## RESOURCES

- **Stitch Help:** [stitch.withgoogle.com](https://stitch.withgoogle.com) (in-app docs)
- **Cursor Docs:** [cursor.sh/docs](https://cursor.sh)
- **Your playbook:** `stitch-cursor-workflow-guide.md` (same folder)
- **Your design system:** `DESIGN.md` (same folder)
- **Live portfolio:** [della-portfolio.vercel.app](https://della-portfolio.vercel.app)

---

## NEXT CONVERSATION

Once you've done your first iteration, come back with:
- Stitch screenshot of your exploration
- CSS changes you made in Cursor
- Live deployment URL

We can refine, iterate, and build on this foundation from there.

**You've got this. Start with Stitch signup and go from there.**
