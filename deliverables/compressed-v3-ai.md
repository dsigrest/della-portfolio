# Keyword Landing Pages / AI

**How do you establish trust in content you can't fully control?**

Reddit wanted to consolidate fragmented SEO traffic using LLMs. Straightforward product idea. Impossible design problem: the organization had no precedent for AI-generated content, no guidelines for governance, no framework for handling non-deterministic output.

Most teams ship features and hope users don't notice instability. This project assumed users would. **Trust in AI-generated content is a systems problem, not a governance problem.** Design for the range of possible outputs, not the happy path.

[IMAGE: KLP product UI, prototype variations, edge case states]

## The Reframe: Trust as Design Infrastructure

Trust lives in the interface itself—visual signals, tone, attribution, failure states. This shifted the work from "make a summary page" to "build the layers that make AI trustworthy at scale."

I designed a **3-layer governance system:**

1. **Visual identification** — Clear signals that content was AI-generated, woven into structure. Not a badge. A commitment to transparency.
2. **Tone and voice** — Guidelines ensuring AI summaries were informative without falsely claiming authority. The voice reflected synthesis, not journalism.
3. **Prompt design as internal tooling** — A cross-functional review process: content design, AI engineering, product design evaluating prompts before production.

## Prompt Design Workflow: Process as Product

Before this, prompt design was engineering-only. Product and design reviewed outputs but had no role in shaping inputs.

I established a **cross-functional review process** where product and design partnered with ML engineers to analyze prompts for accuracy, tone alignment, edge case handling, and trust signals. Each prompt was stress-tested: what happens with contentious topics? Contradicting sources? Inadvertent bias?

**This formalized design's role in AI product development.** Subsequent AI teams adopted the same workflow. It became organizational infrastructure.

The system functioned as developer tooling: it standardized how product teams interfaced with LLM capabilities. It defined input schemas, evaluation criteria, review gates. Later AI products reused this architecture.

Prototyped the governance review flow in Figma Make. The review interface used progressive disclosure—reviewers drilled into failing prompts without context-switching—which reduced cognitive load for high-volume review. Interactive models validated that this pattern would catch edge cases from failure-mode analysis.

[IMAGE: Prompt design workflow, governance model, review criteria]

## Trust Decisions Were Policy Decisions Expressed Through Design

- **AI authorship prominence** — Too subtle: users didn't know they were reading AI. Too prominent: feature collapsed. The signal had to be discoverable, not obtrusive.
- **Attribution models** — Source links vs. inline citations vs. no direct attribution. Each carried different trust implications for communities with strong attribution norms.
- **Contradiction handling** — When AI summary contradicted sources, what should we show? Hide it? Flag it? Surface disagreement?
- **Failure states** — Below-threshold quality triggered what? Degraded summary? Human curation fallback? Feature removal?

These weren't aesthetic decisions. They were policy decisions that design made tangible.

## Outcome: Governance Infrastructure

Reddit's first LLM-powered product shipped. Traffic consolidated. Users engaged with unified AI-summarized pages instead of bouncing across duplicates.

More important: **the governance model and prompt design workflow became organizational infrastructure for AI product development.** The review process became the template for subsequent AI teams, including the Answers product. The trust framework—visual identification, tone guidelines, evaluation criteria—became Reddit's starting point for all AI-generated content.

A senior engineer: "Before this, we shipped AI features and hoped users didn't notice unpredictability. After this, we designed the experience *of* AI." 

The shift from hiding non-determinism to designing for it changed how the organization approached AI products.

Systems before solutions. **The prompt design workflow—a process invention—had more organizational impact than any individual screen.** It changed how teams thought about responsibility when shipping AI.

---

**Word count: 469** | **Reading time: 2–3 minutes**