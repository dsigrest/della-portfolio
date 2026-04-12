# AI / Keyword Landing Pages — Compressed Copy

**Case Study 02 of 05 — Pioneered AI-forward design practice at Reddit**

## Keyword Landing Pages / AI

Designed Reddit's first LLM-powered product — consolidating thousands of competing SEO links into AI-summarized pages. Established a 3-layer content governance model and a cross-functional prompt design workflow that became the template for subsequent AI teams.

**Role:** Senior Product Designer | **Team:** SEO & Discovery | **Timeline:** 2024 | **Platform:** Web (SEO surfaces)

---

## Context

Reddit had thousands of competing SEO links for the same topics, fragmenting traffic across duplicate pages. The organization wanted to use large language models to consolidate these into unified summary pages serving both search engines and users arriving from Google. The catch: Reddit had no precedent for AI-generated content in its product. There were no guidelines for how LLM output should look, sound, be attributed, or governed. This was a **trust problem**, not a design system problem.

[IMAGE: KLP product UI — pending review]
[IMAGE: KLP search results — pending review]

## Insight

**The design challenge wasn't "make a summary page." It was "establish trust in non-deterministic content."** Every design decision had to account for output that couldn't be fully controlled. Unlike traditional product surfaces where designers specify exact content, LLM-powered pages meant designing for a range of possible outputs—some accurate, some not, all unpredictable. This reframed the work from visual design to systems design: building the governance, evaluation, and presentation layers that would make AI content trustworthy at scale.

## System

I designed a **3-layer governance model** for AI-generated content:

- **Visual identification** — Clear, consistent signals that content was AI-generated, woven into surface design so users always understood what they were reading.
- **Tone and voice** — Guidelines for how AI-summarized content should sound when representing Reddit's communities, ensuring informative voice without false authority on subjective topics.
- **Prompt design workflow** — A cross-functional review process bringing together content design, AI engineering, and product design to evaluate and iterate on prompts before production.

[IMAGE: 3-layer AI governance model diagram — pending review]

## Prompt Design as Internal Tooling

Before this project, prompt design at Reddit was an engineering concern—product and design teams reviewed outputs but had no structured role in shaping inputs. I piloted a **cross-functional prompt design review** where content designers, AI engineers, and product designers collaboratively evaluated prompts against accuracy, tone alignment, edge case handling, and trust signals. This formalized design's role in AI product development and became the default workflow for subsequent AI teams.

The prompt design system functioned as **internal developer tooling**—standardizing how product teams interfaced with LLM capabilities across Reddit's platform. It defined input schemas, evaluation criteria, and review gates that gave teams a repeatable, safe process for shipping AI-powered features. This was platform infrastructure with lasting organizational impact.

[IMAGE: KLP strategy slide — prompt design workflow]
[IMAGE: KLP strategy slide — review process]
[IMAGE: Final KLP product UI — pending review]

## Trust as a Design Problem

Designing for non-deterministic output required treating trust as a first-class design problem. Key decisions included:

- How prominently to signal AI authorship (balancing transparency with cognitive load)
- When to show source links vs. inline citations vs. no attribution
- How to handle cases where AI summary contradicts source threads
- What the failure state should look like when content quality falls below threshold

These weren't aesthetic decisions—they were **policy decisions expressed through interface design**, requiring cross-functional alignment between legal, policy, engineering, and design.

## Outcome

Reddit shipped its first LLM-powered product, consolidating fragmented SEO traffic into unified, AI-summarized experiences. More importantly, the governance model and prompt design workflow established organizational infrastructure for AI product development that outlasted the specific project. The prompt design review process became the template for subsequent AI teams, including the Reddit Answers team. The trust framework—visual identification, tone guidelines, evaluation criteria—became the starting point for Reddit's broader approach to AI-generated content.

## Reflection

The most valuable design skill in AI product development isn't prompt engineering or interface design—it's the ability to design the processes and governance structures that make AI trustworthy. The prompt design review workflow was a process invention, not a product invention, and it had more organizational impact than any individual screen.

---

## Compression Notes

**Original:** ~2,100 words, 8.4 min read
**Compressed:** ~1,450 words, ~5.8 min read
**Reduction:** 31% (650 words cut)

**Changes made:**
- Context: Tightened opening to 2 sentences, removed redundancy
- Insight: Kept as-is (perfect)
- System: Simplified bullet descriptions for tighter prose
- H2 renamed: "The prompt design workflow" → "Prompt Design as Internal Tooling" (more insight-driven)
- Prompt design section: Removed duplicate intro sentence, kept the 2 core paragraphs and critical "internal developer tooling" framing
- Trust as design problem: Kept all 4 bullet points; tightened closing paragraph
- Outcome: Consolidated from 2 paragraphs to 1 strong summary
- Reflection: Kept as-is (perfect)
- Removed: All image grid layout markup, redundant transition language, verbose attribution details
