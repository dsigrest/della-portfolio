# Keyword Landing Pages / AI

**Word count:** 1,156 | **Reading time:** 5–7 minutes

---

## The Problem: Trust in Non-Deterministic Content

Reddit had thousands of competing SEO links for identical topics—fragmenting search traffic across duplicate and near-duplicate pages. The organization wanted to consolidate these into unified summary pages using large language models. The product idea was straightforward. The design problem was not.

Reddit had no precedent for AI-generated content in its product. There were no guidelines for how LLM output should look, sound, be attributed, or be governed. **How do you establish trust in content you can't fully control?** Every design decision had to account for the fact that LLM output was inherently unpredictable. 

Unlike traditional product design where content is fully specified, AI-powered pages meant designing for a *range* of possible outputs—some accurate, some not, all unpredictable. Most teams ship the feature and hope users don't notice the instability. This project assumed users would notice. The design challenge was the experience of that uncertainty.

[IMAGE: KLP product UI, KLP search results, prototype variations]

---

## The Insight: Trust is Design, Not Just Governance

The design challenge wasn't "make a summary page." **It was "establish trust in non-deterministic content"—a systems problem dressed as a UX problem.**

The reframe shifted the project from visual design to governance design: building the layers—visual, linguistic, and operational—that made AI content trustworthy at scale.

**Trust lived in the interface itself.** Visual signals, tone choices, attribution models, failure states—these were the core design. This meant understanding what the model could and couldn't do reliably, working with legal on attribution and liability, and building trust through transparency, not obfuscation.

---

## Three-Layer Governance Model

I designed a **3-layer governance system for AI-generated content:**

- **Visual identification**: Clear, consistent signals that content was AI-generated, woven into surface design. Not a badge. A structural commitment to transparency.
- **Tone and voice**: Guidelines ensuring AI-summarized content was informative without falsely claiming authority on subjective topics. The voice reflected synthesis, not journalism.
- **Prompt design workflow**: A cross-functional review process bringing content design, AI engineering, and product design to evaluate and iterate on prompts before production. This was process design.

### Prompt Design as Internal Developer Tooling

The most novel contribution was the **prompt design review process**—the first time at Reddit that design had a structured role in shaping LLM inputs, not just evaluating outputs.

Before this project, prompt design at Reddit was an engineering concern. Product and design teams reviewed outputs but had no structured role in shaping inputs. I piloted a cross-functional workflow where content designers, AI engineers, and product designers evaluated prompts against: accuracy, tone alignment, edge case handling, and trust signals. 

Each prompt was analyzed for failure modes. What happens when the topic is contentious? When sources contradict? When the summarization introduces inadvertent bias? **This formalized design's role in AI product development.** Subsequent AI teams adopted this as their default workflow.

**The system functioned as internal developer tooling:** It standardized how product teams interfaced with LLM capabilities across Reddit's platform. It defined input schemas, evaluation criteria, and review gates. This architecture proved reusable when building later AI products.

Prototyped the governance review flow in Figma Make—interactive models let the team align on where human review gates belonged and validate that review criteria would catch edge cases identified in failure-mode analysis.

[IMAGE: Prompt design workflow diagram, governance model visualization, review process flow]

---

## Trust as First-Class Design Problem

Treating trust as a primary constraint meant deciding what others delegated to legal/policy:

- **Prominence of AI authorship signal**: Too subtle and users didn't know they were reading AI output. Too prominent and the feature collapsed. The signal had to be discoverable, not obtrusive.
- **Attribution models**: Source links vs. inline citations vs. no direct attribution. Each carried different trust implications and different implications for communities with strong attribution norms.
- **Contradiction handling**: When the AI summary contradicted source threads, what do we show? Hide it? Flag it? Surface the disagreement?
- **Failure states**: When content quality fell below threshold, what does the interface become? Degraded summary? Human curation fallback? Feature removal?

These weren't aesthetic decisions. **They were policy decisions expressed through interface design.** The design work made trust tangible and enabled cross-functional alignment with legal, policy, engineering, and product.

[IMAGE: Trust signal variations, contradiction handling examples, content quality states]

---

## Outcome: Infrastructure That Scaled

Reddit's first shipped LLM-powered product—keyword landing pages consolidated fragmented SEO traffic into unified, AI-summarized experiences. The product worked. Users engaged with consolidated pages rather than bouncing across duplicates. Traffic concentrated.

More importantly, **the governance model and prompt design workflow became organizational infrastructure for AI product development.** The prompt design review process became the template adopted by subsequent AI teams, including the team that built Reddit Answers. The trust framework—visual identification, tone guidelines, evaluation criteria—became the starting point for Reddit's broader approach to AI-generated content.

A senior engineer said: "Before this, we were shipping AI features and hoping users didn't notice the unpredictability. After this, we were designing the experience *of* AI." That shift—from hiding non-determinism to designing for it—changed how the organization approached AI product development.

---

## Reflection: Systems Before Solutions

This project crystallized something: the most valuable design skill in AI product development isn't prompt engineering or interface design. **It's the ability to design the processes and governance structures that make AI trustworthy.**

The prompt design review workflow was a process invention, not a product invention. It had more organizational impact than any individual screen. It changed how teams thought about the responsibility they carried when shipping AI features.

Scaling AI product development means thinking like infrastructure. How do I design not just this product, but the framework product teams use to ship AI safely? That's the highest-impact design work.