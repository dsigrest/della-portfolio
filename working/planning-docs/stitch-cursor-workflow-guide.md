# Stitch + Cursor Workflow Guide

**For:** Della Sigrest — Portfolio Site  
**Date:** April 2026  
**Objective:** Seamless design-to-code iteration using Stitch (exploration) and Cursor (implementation)

---

## Quick Start (5 Minutes)

If you're new to this workflow:

1. **Skip to "Setup Stitch (First Time Only)"** — takes 10 minutes
2. **Then skip to "The Iteration Loop"** — shows the pattern you'll repeat
3. **Bookmark "Quick Reference" at the bottom** — your cheat sheet

---

## PART 1: SETUP (First Time Only)

### Step 1: Sign Up for Google Stitch 2.0

1. Go to [Google Labs](https://labs.google.com) (or search "Stitch 2.0")
2. Click **"Get Stitch 2.0"** (it says "Experimental" but it's stable for design)
3. Sign in with your Google account (use the same one as your Vercel deployment)
4. You'll land in an empty Stitch workspace

**Expected:** A blank canvas with a toolbar on the left (shapes, text, upload, etc.)

---

### Step 2: Create Your Portfolio Project in Stitch

1. In Stitch, click **"New Project"** or **"Create"** in top-left
2. Name it: **"Della Portfolio — Spring 2026"**
3. Click **"Create"**

**What you'll see:** A large blank canvas (like Figma's viewport)

---

### Step 3: Import Design Tokens into Stitch

This is the bridge between design and code.

**Option A: Copy/Paste DESIGN.md (Easiest)**
1. Open `/mnt/Get-a-job/portfolio-site/DESIGN.md` in your text editor
2. Copy everything from "COLOR PALETTE" down to "IMPLEMENTATION NOTES"
3. In Stitch, create a new text frame on your canvas
4. Paste the content
5. Label it: **"Design Tokens — Reference"**

**Option B: Use MCP Server (Advanced)**
- If you're using Claude Code with MCP, the DESIGN.md is already available to Claude
- Stitch can pull these tokens directly (setup instructions in Stitch settings)
- More on this below

---

### Step 4: Set Up Cursor IDE

If you don't have Cursor yet:

1. Download from [cursor.sh](https://cursor.sh)
2. Install and open
3. Click **"File"** → **"Open Folder"**
4. Navigate to `/mnt/Get-a-job/portfolio-site/`
5. Click **"Open"**

**Expected:** Your portfolio files in the left sidebar (index.html, styles.css, case-*.html, etc.)

---

### Step 5: Understand Your Two Windows

You now have:

| Tool | Role | Window |
|------|------|--------|
| **Stitch** | Design exploration + direction-setting | Browser (open in separate tab) |
| **Cursor** | Code implementation + refinement | Desktop IDE |

You'll bounce between them, not at the same time.

---

## PART 2: THE ITERATION LOOP

This is the pattern you'll repeat for every improvement:

### Phase 1: Explore in Stitch (10-30 min)

**Goal:** Decide *what* to change and *why*

1. Open your Stitch project
2. Create a new frame (canvas area) for your exploration
3. Grab inspiration:
   - Screenshot your current site (use Cursor's browser preview)
   - Paste the screenshot into Stitch
   - Sketch variations directly on top with Stitch's drawing tools
   - Add notes: "Try darker teal here," "Add more space between cards," etc.

**Example Exploration:**
- Take a screenshot of a case card
- Duplicate it 3 times
- On version 2: Increase padding, adjust colors
- On version 3: Add shadow, change typography
- On version 4: Combine best elements
- Write notes beside each: "This feels too heavy," "Better breathing room"

4. Pin down your decision
   - Which variation looks best?
   - What CSS needs to change?
   - Take a final screenshot of your chosen design

**Don't worry about:** Perfect pixel alignment, exact hex codes — Stitch is for direction, not precision.

---

### Phase 2: Consult DESIGN.md (5 min)

Before coding, review what tokens exist.

1. Open `DESIGN.md` (in your editor or in Stitch's reference frame)
2. Find the section for what you're changing:
   - Changing colors? Look at "COLOR PALETTE"
   - Changing spacing? Look at "SPACING SYSTEM"
   - Adding animation? Look at "TRANSITIONS & ANIMATIONS"

3. Note the current values
   - Example: "Current case card padding is 28px vertical, 32px horizontal"
   - Example: "Hero H1 is clamp(34px, 4.5vw, 52px)"

**Why?** You want to update `DESIGN.md` after coding, so knowing the old values helps you track what changed.

---

### Phase 3: Implement in Cursor (15-60 min)

**Goal:** Make the CSS changes you decided on

1. **Open Cursor** and navigate to `styles.css`
2. **Use Cursor's Visual Editor** (new feature):
   - Click "Visual Editor" button in Cursor (top-right)
   - You'll see your portfolio rendered in a preview pane
   - Click any element to select it in the CSS
   - Drag handles to resize, drag text to move, use sliders for colors/spacing

3. **Or edit CSS directly:**
   - Find the selector in `styles.css` (e.g., `.case-card`)
   - Update the property (e.g., `padding: 36px 40px;`)
   - Save (Cmd+S / Ctrl+S)
   - Watch the preview update in real-time

**Example: Increase Case Card Padding**
```css
/* In styles.css, find: */
.case-content { 
  padding: 28px 32px;  /* OLD */
}

/* Change to: */
.case-content { 
  padding: 36px 40px;  /* NEW — 28% increase */
}

/* Save → Preview updates instantly */
```

4. **Test on mobile:**
   - In Cursor's preview, click the device icon (bottom-right)
   - Toggle between desktop/tablet/mobile views
   - Make sure spacing still looks good

5. **Check accessibility:**
   - In Cursor, press Cmd+Shift+P (Ctrl+Shift+P on Windows) → "Accessibility"
   - Run a color contrast check
   - Ensure your new colors meet WCAG AA (4.5:1 minimum)

---

### Phase 4: Review in Browser (5 min)

1. Open Cursor's integrated browser preview (or open `index.html` in your browser)
2. Navigate to the page you changed
3. Test:
   - Does it match your Stitch exploration?
   - Does it feel right on mobile?
   - Are hover states still working?
   - Are animations smooth (no jank)?

4. If something's off, go back to Phase 3 and tweak

---

### Phase 5: Update DESIGN.md (5 min)

Keep your design documentation in sync.

1. Open `DESIGN.md`
2. Find the section you changed (e.g., "SPACING SYSTEM")
3. Update the values:
   ```markdown
   /* OLD */
   .case-content { padding: 28px 32px; }
   
   /* NEW (April 2026) */
   .case-content { padding: 36px 40px; }
   ```

4. Save `DESIGN.md`

**Why?** If you or Claude revisit this project later, DESIGN.md is your single source of truth.

---

### Phase 6: Deploy (1 min)

Once you're happy with the changes:

1. In Cursor, open the Terminal (Ctrl+`)
2. Run:
   ```bash
   git add .
   git commit -m "Increase case card padding for dark mode breathing room"
   git push origin main
   ```

3. Wait 2-3 minutes
4. Visit [della-portfolio.vercel.app](https://della-portfolio.vercel.app) to see live changes

**Vercel auto-deploys on push.** No manual upload needed.

---

## PART 3: USING CLAUDE INTEGRATION (Optional but Recommended)

If you're using Claude Code with MCP server:

### Claude Can Read Your Design System

1. Claude has access to `DESIGN.md` automatically
2. You can ask Claude things like:
   - "Make the hero CTA more prominent"
   - "Add more breathing room to dark mode surfaces"
   - "Update Tier 1 improvements from ui-tools-recommendation.md"

3. Claude will:
   - Read DESIGN.md for current tokens
   - Suggest CSS changes respecting your design system
   - Update files
   - Suggest when to update DESIGN.md

### The Handoff Pattern

**You to Claude:**
```
"I explored in Stitch and want to implement these changes:
- Increase padding on .case-card by 25%
- Make hero CTA use accent color instead of border
- Check color contrast after changes"
```

**Claude will:**
1. Read DESIGN.md
2. Calculate 25% increase on current padding values
3. Update styles.css
4. Verify contrast
5. Suggest DESIGN.md updates
6. Verify changes in Cursor's Visual Editor

---

## QUICK REFERENCE: Common Tasks

### Change the Accent Color (Teal → Different)

**In Stitch:**
- Explore what the new color looks like on your cards, hero, etc.
- Decide: "This blue is better than teal"

**In Cursor/styles.css:**
```css
:root {
  --accent: #2dd4bf;  /* OLD teal */
  /* Change to your new color: */
  --accent: #0ea5e9;  /* NEW blue example */
  
  /* Also update accent variations: */
  --accent-dim:     rgba(14, 165, 233, 0.08);
  --accent-hover:   rgba(14, 165, 233, 0.14);
  --accent-muted:   rgba(14, 165, 233, 0.2);
}
```

**Then:** Update DESIGN.md COLOR PALETTE section

---

### Increase Spacing (Dark Mode Breathing Room)

**Target:** Add 20-30% more padding throughout

**In Cursor/styles.css:**
```css
/* Case Cards */
.case-content { 
  padding: 28px 32px;  /* OLD */
  padding: 36px 40px;  /* NEW: +28% */
}

/* Pillars */
.pillar {
  padding: 40px 36px;  /* OLD */
  padding: 48px 44px;  /* NEW: +20% */
}

/* Case Body */
.case-body {
  padding: 60px var(--side-pad) 120px;  /* OLD */
  padding: 80px var(--side-pad) 140px;  /* NEW */
}
```

**Test:** Mobile should still feel natural, not cramped or too loose

---

### Add a Hover Animation to Cards

**In Cursor/styles.css:**

Before (current):
```css
.case-card:hover {
  border-color: var(--border-hover);
  box-shadow: 0 8px 40px rgba(0,0,0,0.25);
  transform: translateY(-3px);
}
```

After (enhanced):
```css
.case-card:hover {
  border-color: var(--border-hover);
  box-shadow: 0 20px 40px rgba(0,0,0,0.3);  /* Stronger shadow */
  transform: translateY(-6px);  /* Bigger lift */
  transition: all var(--transition);  /* Ensure smooth */
}
```

**Test:** Hover over a case card; feel the lift? Good.

---

### Update Typography Size

**Example: Make Hero H1 Bigger**

**In Cursor/styles.css:**
```css
.hero h1 {
  font-size: clamp(34px, 4.5vw, 52px);  /* OLD */
  font-size: clamp(38px, 5vw, 56px);    /* NEW: bigger min/max */
}
```

**Why clamp()?**
- First number: Smallest size on mobile (380px)
- Middle: Percentage of viewport width (responsive)
- Last number: Largest size on desktop (1200px+)

**Test mobile + desktop to verify readability**

---

### Change Text Color

**All text colors use CSS variables — never hardcode hex values:**

```css
/* Good */
color: var(--text-primary);      /* #e8e8e8 */
color: var(--text-secondary);    /* #888 */
color: var(--accent);            /* #2dd4bf */

/* Avoid */
color: #e8e8e8;  /* Hardcoded — won't respect system updates */
```

To change all primary text at once, update `:root {}` in `styles.css`

---

### Add a New Animation

**In Cursor/styles.css:**

1. Define the keyframes:
```css
@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}
```

2. Apply to an element:
```css
.case-card {
  animation: slideInLeft 0.5s ease forwards;
  animation-timeline: view();
  animation-range: entry 0% cover 25%;
}
```

3. Always include reduced-motion fallback:
```css
@media (prefers-reduced-motion: reduce) {
  .case-card {
    animation: none;
    opacity: 1;
    transform: none;
  }
}
```

---

### Test Mobile Responsiveness

**In Cursor:**
1. Open Visual Editor (top-right)
2. Click device icon (bottom-right)
3. Toggle between:
   - Desktop (1400px+)
   - Tablet (768px)
   - Mobile (375px)

**Breakpoints in your code:**
- `@media (max-width: 768px)` — tablet adjustments
- `@media (max-width: 480px)` — mobile adjustments

---

### Check Color Contrast (Accessibility)

**In Cursor:**
1. Press Cmd+Shift+P (Ctrl+Shift+P Windows)
2. Type "Color contrast"
3. View the results
4. Target: 4.5:1 minimum for body text

**If failing:**
- Use WCAG contrast checker (online tool)
- Adjust --text-secondary or --accent to be brighter
- Test again

---

## WORKFLOW CHECKLIST

Use this before deploying:

- [ ] Explored design in Stitch (took screenshots, sketched alternatives)
- [ ] Reviewed DESIGN.md for current token values
- [ ] Made CSS changes in Cursor
- [ ] Tested changes in Visual Editor (desktop + mobile)
- [ ] Tested hover states, animations, interactions
- [ ] Checked color contrast (WCAG AA: 4.5:1 minimum)
- [ ] Checked mobile responsiveness (768px, 480px)
- [ ] Checked animations respect prefers-reduced-motion
- [ ] Updated DESIGN.md with new values
- [ ] Committed to git with clear message
- [ ] Deployed to Vercel
- [ ] Verified live on della-portfolio.vercel.app

---

## TROUBLESHOOTING

### "My changes aren't showing up"
1. Make sure you **saved** (Cmd+S / Ctrl+S)
2. Check you edited the **right selector** (e.g., `.case-card` not `.case-cards`)
3. Refresh the browser (F5 or Cmd+R)
4. Clear cache (Cmd+Shift+Delete / Ctrl+Shift+Delete)

### "Text contrast is failing"
1. Check your text color vs. background in WCAG checker
2. Make --text-secondary brighter (was #888, try #a0a0a0)
3. Or make background slightly darker/lighter to increase contrast
4. Test after each change

### "Mobile layout is broken"
1. Check media query breakpoints (@media 768px, 480px)
2. Verify padding/margin scales down on mobile
3. Test toggle between desktop/mobile in Visual Editor
4. Use Chrome DevTools → Device Emulation if needed

### "Hover animation is too fast/slow"
- Change the duration in the animation rule:
  ```css
  animation: slideInLeft 0.5s ease forwards;  /* 0.5s duration */
  /* Try: 0.3s (faster) or 0.7s (slower) */
  ```

### "Vercel deployment not updating"
1. Check git push was successful: `git log` shows your commit
2. Wait 2-3 minutes (Vercel takes time to build)
3. Check vercel.com dashboard for deploy status
4. Try hard refresh on portfolio site (Cmd+Shift+R)

---

## TIPS & BEST PRACTICES

### Always Use CSS Variables
- Don't hardcode colors/sizes
- Update `:root {}` once, affects whole site
- Example: Change `--accent: #2dd4bf` to update all teal uses

### Keep DESIGN.md Updated
- Every time you change a token, update DESIGN.md
- This keeps your documentation in sync with code
- Future you (or Claude) will thank you

### Test on Real Devices
- Emulation in browser is good, but real phones are better
- Ask a friend to visit your deployed site on their phone
- Ask: "Does this look right to you?"

### Dark Mode Design Needs Breathing Room
- Light mode: 60px padding feels good
- Dark mode: Same 60px feels cramped
- Add 20-30% more padding on dark sites

### Use Clamp() for Responsive Typography
```css
/* Instead of: */
font-size: 16px;  /* Same size everywhere */

/* Do: */
font-size: clamp(14px, 2vw, 18px);  /* Scales from 14 to 18 */
```

### Test Animations with Motion Preference
1. macOS: System Preferences → Accessibility → Display → Reduce Motion
2. Windows: Settings → Ease of Access → Display → Show animations
3. Enable and refresh your site
4. Animations should stop or be instant

---

## NEXT STEPS AFTER SETUP

**Week 1:**
- Explore Tier 1 improvements in Stitch (accent color, padding, contrast)
- Implement in Cursor
- Deploy

**Week 2:**
- Explore Tier 2 improvements (shadows, typography, spacing)
- Implement and test
- Deploy

**Week 3:**
- Optional: Explore Tier 3 (animations, borders)
- Or take a break and gather feedback from recruiters

**Ongoing:**
- Update DESIGN.md after each change
- Keep this guide handy for reference
- Share your improvements with mentors/peers

---

## FILES YOU'LL TOUCH MOST

| File | Purpose | How Often |
|------|---------|-----------|
| `styles.css` | All CSS rules | Every session |
| `DESIGN.md` | Design token documentation | After CSS changes |
| `index.html` | Homepage structure | Rarely (for major layout changes) |
| `case-*.html` | Case study pages | Occasionally (for new cases) |
| `about.html` | About page | Rarely |

---

## RESOURCES

- **Stitch Docs:** [Google Stitch 2.0 Help](https://labs.google.com/stitch) (within the app)
- **Cursor Docs:** [cursor.sh/docs](https://cursor.sh)
- **CSS Variables:** [MDN: CSS Custom Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/--*)
- **Clamp Function:** [MDN: clamp()](https://developer.mozilla.org/en-US/docs/Web/CSS/clamp)
- **WCAG Contrast:** [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- **Your Design System:** `DESIGN.md` in your portfolio folder

---

**Questions?** Reference this guide, check DESIGN.md, or ask Claude Code with your DESIGN.md context.

**Ready to start?** Jump to "Setup Stitch (First Time Only)" above.

Happy designing!