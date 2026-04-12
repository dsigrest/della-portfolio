# Notifications & Inbox

**Word count:** 1,087 | **Reading time:** 5–6 minutes

---

## The Problem: Five Years of Neglect

**+1.4% DAU. +6.4% push CTR. +5.4% good visits.** These numbers came from redesigning Reddit's most neglected surface—a notification system that hadn't received dedicated design attention in six years. When I joined the Notifications team, the surfaces—push notifications, email digests, in-app inbox, and chat—were managed independently. No unified strategy. No cohort thinking. No systematic approach to engagement.

This wasn't a visual refresh project. This was building the strategic foundation for how a billion-user platform communicates with its users from scratch. The organization had tried piecemeal improvements before. They failed. Each team optimized for their channel (push team pushed for more push notifications; chat team competed for inbox real estate) without understanding what users actually needed at each stage of their journey.

[IMAGE: Inbox wireframe exploration, Figma notification design variants, context map]

---

## The Insight: Five Problems Hiding in One

Early exploration revealed a counterintuitive pattern: **the inbox wasn't one problem—it was five fundamentally different problems for five different user archetypes.** A casual lurker visiting weekly has completely different notification needs than a power moderator managing 12 communities. They want different information, different timing, different channels, different controls.

A monolithic redesign would serve none of them well. The team's initial instinct was to build the "ultimate notification system"—one interface trying to serve everyone. It would collapse under competing demands: features half the users didn't need, missing features the other half required.

**Instead, I built a segmented system with distinct strategies for each cohort.** The reframe became the strategic backbone—the organizing principle for the entire team's roadmap.

---

## Three-Pillar System Design

The **Inbox 2.0 strategy** mapped three pillars to user needs:

- **Build Habits** — New/returning users: consistent, valuable patterns that establish Reddit as a daily touchpoint. Notifications that rewarded opening the app, not notifications that created regret.
- **Enable Curation** — Active users: granular control to reduce noise without killing engagement. Users overwhelmed by signal needed filtering, not discovery.
- **Create Focus** — Power users/moderators: unified signal across channels for efficient action. High-volume users needed consolidation—noise compressed into actionable summaries.

### From Framework to Platform Infrastructure

The 5-archetype framework wasn't a feature spec—**it was an API for how product teams across the organization thought about user communication.** Teams building new features plugged into the framework rather than inventing notification strategies from scratch. A subscription team could ask: "Which cohort are we targeting? What does Build Habits / Enable Curation / Create Focus mean?"

This abstraction scaled. When Reddit's AI teams built communication for LLM-generated content, they inherited the framework. The governance patterns became reusable. Design could speak with engineering and product about cohorts and value propositions, not pixel placement.

Prototyped Inbox 2.0 and Unified Inbox in Figma Make—interactive models let the team validate the navigation pattern and surface edge cases in notification grouping. The prototypes revealed how cohorts experienced different information hierarchies, where actions overlapped, and what happened when urgency signals conflicted across channels.

### Unified Inbox: Freeing Navigation Real Estate

Simultaneously, I led the **Unified Inbox initiative**—merging notifications and chat into a single tab. This wasn't just a UX improvement. It freed a critical navigation slot required for Reddit 2.0, the platform's broader redesign. That one slot was contested. Three teams had legitimate claims to it. The business case required negotiating competing ownership interests across notifications, chat, and the platform team.

The Figma Make prototype showed where boundaries belonged between notification types and chat threads, and how the search/filter model needed to shift to unify two previously separate information structures.

**This work taught me that the hardest part of systems thinking isn't the framework—it's securing buy-in from competing stakeholders.** Design thinking is useless if you can't convince other teams to move with you.

[IMAGE: Unified Inbox before/after, strategy framework diagram, navigation impact visualization]

---

## Experiments: Testing the Framework

With the strategic system in place, I ran focused experiments to validate the framework and optimize within it:

**Push notification optimization** for new users—testing copy framing, send cadence, deep-link destinations to find the balance between engagement and fatigue:

| Metric | Lift |
|--------|------|
| New user DAU | **+1.4%** |
| Push CTR | **+6.4%** |
| Good visits | **+5.4%** |

The copy framing was sharp: new users responded to notifications mentioning other users ("Sarah replied to your comment") vs. abstract value ("New notifications in r/technology"). This wasn't optimizing for clicks. This was optimizing for *good* clicks—visits that led to sustained engagement, not one-off taps.

**Subscription notification improvements** to optimize reach and visit quality:

| Metric | Lift |
|--------|------|
| Good visits | **+1%** |
| Subscription good visits | **+2–3%** |

**Inbox modernization**: Redesigned the in-app surface with updated hierarchy, clearer grouping, and improved action affordances. **The component patterns became the Design Systems team's reference for scalable notification architecture**, adopted into the shared library. This work created a foundation that other teams could extend rather than rebuilding from scratch.

[IMAGE: Notification variant layouts—grouped vs. action-oriented, live UI, analytics dashboard]

---

## Outcome: Framework as Roadmap

The **Inbox 2.0 strategy became the team's multi-quarter roadmap**—the first coherent vision Notifications had. The Unified Inbox work freed the navigation slot for platform redesign. Push experiments delivered measurable engagement gains.

Most lasting: **the cohort segmentation framework continued to guide the team after I moved to my next rotation.** It became the shared language for making tradeoffs between competing user needs. Junior designers inherited a decision-making framework, not just a design system.

---

## Reflection: Systems Over Surfaces

The most impactful design work is often invisible. It's not the interface—it's the strategic frame that makes good interface decisions possible. The cohort segmentation, which shipped no UI, was more valuable than the visual redesign—it gave the team language for navigating competing needs simultaneously.

Scaling systems thinking means thinking like a platform. How do I design not just this product, but the framework product teams use to make decisions? That's where the leverage is.