# AI Doesn't Have Taste — I Do

## Three Title Options (For LinkedIn/Medium)

1. **"AI Doesn't Have Taste — I Do"** (strongest, most memorable, mic-drop opening)
2. **"How I Designed This Portfolio With Claude (And What I Learned)"** (clearer, more explanatory)
3. **"The Governance Model That Made AI-Designed Artifacts Trustworthy"** (more technical, systems-focused)

**Recommendation:** Option 1. It's the mic-drop insight from the process. Use it as the title, let the subtitle explain.

---

## Blog Post (1,400 words)

**Subtitle:** *A working designer's case study in human judgment gates, AI scaffolding, and why speed only matters if you're moving in the right direction.*

### Hook: The Missing Proof Point

My resume claimed AI-forward design practice. My LinkedIn said I'd integrated Claude into my workflow. But I had no artifact to back it up. No published proof. No case study. Just assertions.

That gap mattered. I was interviewing for senior roles at six companies—Ramp, Anthropic, Meta, Figma, OpenAI, Cursor—and five of them flagged the same concern: "No public thought leadership. No evidence of how you actually work with AI. Just résumé language."

So I did what designers do. I identified the problem and built the proof. The proof was this portfolio site.

But here's the thing: I could have used a template. I could have handed everything to an AI and let it run. I could have published something in a week and claimed velocity. Instead, I spent two months designing a portfolio collaboratively with Claude—documenting the process, the gates, the governance model—to prove that speed without judgment is just noise.

This is how it worked, and what I learned.

### The Collaboration Wasn't Black-Box

The workflow looked like this: **Prompt → Generate → Review → Iterate.**

I'd define a task. Claude generated options. I reviewed for accuracy, tone, and strategic fit. If it missed, I redirected. If it was close, I iterated on voice or emphasis. If it was strong, it went into the build log and moved to the next task.

Human approval was required before anything shipped. The AI proposed. The human disposed.

This isn't revolutionary. It's not even that different from how I'd collaborate with a copywriter or junior designer. But it forced me to be explicit about something I usually do implicitly: *where does human judgment actually matter?*

**Research synthesis:** Claude analyzed 50+ job requirements across six company descriptions and extracted the recurring themes. This would have taken me a day to do by hand. Claude did it in minutes. I reviewed the frameworks for accuracy and made one correction. Three hours of my time became 20 minutes.

**Content architecture:** I explored four different structures for the portfolio case study. Four different information hierarchies. Four different narrative arcs. Without fatigue. Without the friction of starting from scratch each time. I tested the hypothesis "which story do I want to lead with?" using variants instead of arguments. Two days of thinking compressed into one.

**Code generation:** The HTML, CSS, and JavaScript came from prompts. I specified the structure. I reviewed the output. I caught bugs. I refined. The site went from concept to deployed in weeks, not months. But it wasn't autopilot. Every line of code passed human review before deploy.

**Iteration velocity:** Copy variants, layout options, design token explorations. High volume meant high confidence in final choices because I'd seen the alternatives.

### Where AI Excels / Where Human Judgment is Essential

This is the useful part—not the speed, but the honesty.

**AI excelled at:**
- Synthesis (extracting patterns from 50+ requirements)
- Variation (generating 4–5 options without writing fatigue)
- Scaffolding (HTML/CSS/JS backbone)
- Rapid iteration (exploring alternatives without friction)

**Judgment remained decisively human:**
- Strategic direction: Which stories to tell. How to position work given confidentiality. What omit entirely.
- Voice and authenticity: Recruiting isn't marketing. This portfolio needed to sound like me—direct, precise, reflective—not corporate or over-polished. I rewrote entire sections to recover that voice.
- Visual design: Color palette, typography, layout decisions. Restraint signals confidence. That was a judgment call, not a generation task.
- Confidentiality: What could be shown. What needed redaction or ethical consideration. Business and ethics judgment.
- Quality gate: Knowing when "good enough" is actually good enough. Knowing what needs another pass.

And here's the critical one: **AI doesn't have taste. I do.**

Taste isn't a synonym for preference. It's the ability to recognize quality patterns and know when something works. It's editorial judgment. It's the difference between "option A is faster" and "option A is right." Claude can't make that distinction. I can.

### The Governance Model

Here's how accountability actually worked:

**Session 1:** Define task (e.g., "Research and synthesize Reddit design patterns from my work there"). Claude generates research summary and framework. I review for accuracy, spot-check three claims against my own memory, approve. Build log documents what was generated and why.

**Session 2:** Task escalates. "Structure the Reddit case study. Here's the framework. Here's what I want readers to understand about notifications design." Claude generates structure + three headline options. I review for strategic fit, pick one, iterate on tone. Build log tracks the decision.

**Session 3:** "Generate the opening section for the notifications case study using this structure." Claude writes draft. I review paragraph by paragraph. Some passages feel wrong—too corporate, missing the insight, incomplete. I mark those and redirect: "This section should focus on constraint, not feature. Try again." Claude tries again. I accept or iterate.

Final output goes to the build log with notes about what changed and why.

This isn't bureaucracy. It's accountability. If a recruiter asks "walk me through how this site was built," I can explain every decision. I can say what AI generated and what I edited. I have proof. I have continuity. I have editorial control.

Most importantly: I have an artifact that reflects my taste, not someone else's automation.

### What Changed About The Work

Using AI at this level—not for drafting first passes, but for scaffolding and iteration—changed how I think about design velocity.

Traditional design: I sit down, I write, I feel the friction. The friction is part of the thinking. I write one paragraph at a time. I refine as I go. I finish exhausted. Time: 3 hours per section.

AI-assisted design: I specify what I want. Claude generates options. I review, I iterate, I refine. The friction is in editing and judgment, not in starting from nothing. I see alternatives. I make choices faster because I'm not starting from a blank canvas. Time: 1 hour per section, higher confidence.

But here's what matters: *I'm doing more editing, not less.* The volume of words increases. The quality bar stays the same. I'm doing more curation, more filtering, more saying "no." That's the actual work.

This is what I'd tell anyone using AI in design: The limiting factor isn't generation. It's judgment. Speed is cheap when you can generate anything. The valuable skill is knowing what to ask for and when to reject the answer.

### Why This Proof Point Matters

This portfolio is:
- ~560 lines of CSS
- 6 HTML pages, fully responsive, WCAG AA accessible
- No frameworks, no templates, no build step
- Deployed on Vercel
- Designed in Figma; implemented in code

For senior product roles that value prototyping velocity and technical literacy, this matters. Code-based prototyping is a natural extension of design practice, not a separate skill someone else owns.

But the real proof is this: I can use AI strategically in product work without sacrificing judgment, authenticity, or taste. I can move fast without moving recklessly. I know when to lean on AI and when to override the output.

That's the signal I wanted to send.

### What Comes Next

The most important insight came at the end, not the beginning.

Speed is only valuable if you're moving in the right direction. Direction comes from somewhere else. It comes from taste, judgment, editorial control, and a clear picture of what you're building and why.

AI doesn't provide direction. It accelerates movement. The direction has to come from you.

If you use AI as a substitute for judgment, you get fast bad work. If you use AI as scaffolding for better judgment, you get fast good work. The difference is responsibility.

I'm continuing this practice. Next step: documenting how this governs design when the system outputs are non-deterministic (AI-generated content in products). How do you design trust when you can't control the output? That's the next frontier of AI-integrated design thinking.

For now: This portfolio is the artifact. This article is the reflection. Together, they answer the question my recruiters asked.

This is how I work with AI. This is the judgment I bring. This is the speed I can sustain without sacrifice.

---

## Metadata & Publication Notes

**Target Length:** 1,400 words | **Actual:** 1,398 words
**Estimated Read Time:** 8–9 minutes
**Target Platforms:** LinkedIn (native article) or Medium
**Voice:** Reflective, honest, practitioner-to-practitioner
**Key Insight:** "AI doesn't have taste — I do"

### Core Elements Preserved from Case Study:
- ~560 lines CSS, 6 HTML pages stat
- Governance model (Prompt → Generate → Review → Iterate)
- Six target companies (Ramp, Anthropic, Meta, Figma, OpenAI, Cursor)
- Key distinction: scaffolding vs. strategy
- Human review gates at every decision point
- Emphasis on editorial control and taste

### Additions for Blog Format:
- Personal hook (recruiter gap, why this matters)
- Reflective tone (what I learned, what surprised me)
- Forward-looking ending (non-deterministic systems, next frontier)
- Vulnerability (editing is the real work, speed is cheap)
- Specific governance examples (session-by-session breakdown)

### Distribution Plan:
1. Publish on LinkedIn (native article for network reach)
2. Republish to Medium (SEO, long-tail discovery)
3. Link from portfolio case study
4. Share once on LinkedIn profile
5. Update Writing page within 24 hours
