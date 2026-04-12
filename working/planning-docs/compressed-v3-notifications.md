# Notifications & Inbox

**+1.4% DAU. +6.4% push CTR. +5.4% good visits.**

Reddit's notification system hadn't received dedicated design attention in six years. Five independent surfaces—push, email, inbox, chat—competed without unified strategy. The problem wasn't visual. It was systemic: no cohort thinking, no framework for tradeoffs, no way to optimize for different user needs simultaneously.

[IMAGE: Inbox wireframe, notification variants, context map]

## The Insight

**Five archetypes needed five different strategies.** A casual lurker and a power moderator have opposite needs: one needs consistent habits; the other needs unified signal across channels. A monolithic redesign serves neither.

Instead of building the "ultimate notification system," I segmented users into five cohorts and mapped distinct intervention points to each:

- **Build Habits** — New users: consistent, high-signal notifications that reward opening the app
- **Enable Curation** — Active users: granular filtering to reduce noise without killing engagement
- **Create Focus** — Power users: unified inbox compressing multiple channels into actionable summaries

## Three-Pillar Platform Architecture

The segmentation framework became organizational infrastructure. Product teams across Reddit plugged into it rather than inventing notification strategies. When AI teams built communication for LLM-generated content, they inherited the same framework. Design, engineering, and product used cohorts as their shared language—no more pixel debates, just "which cohort does this serve?"

Prototyped Inbox 2.0 and Unified Inbox in Figma Make. Interactive models revealed how different cohorts experienced different information hierarchies, where actions overlapped, and how urgency signals conflicted across channels. The prototypes showed implementation teams what would break.

Unified Inbox freed critical navigation real estate for Reddit's broader platform redesign. This required negotiating across three teams with competing ownership claims. The prototype made boundaries tangible—where notifications belonged, where chat threads belonged, how search/filter unified two separate surfaces.

[IMAGE: Unified Inbox before/after, strategy framework, navigation impact]

## Experiments Validated the Framework

**Push notification optimization for new users:**
| Metric | Lift |
|--------|------|
| New user DAU | **+1.4%** |
| Push CTR | **+6.4%** |
| Good visits | **+5.4%** |

Copy framing mattered: "Sarah replied to your comment" outperformed "New notifications in r/technology." New users responded to other-user signals over abstract value. This wasn't optimizing for clicks—it was optimizing for *good* clicks that led to sustained engagement.

**Inbox modernization** redesigned hierarchy and grouping. The component patterns became the design systems team's reference architecture. Other teams could extend, not rebuild.

## Outcome

The framework became the team's multi-quarter roadmap—their first coherent vision. Unified Inbox freed navigation real estate. Experiments delivered measurable gains.

Most lasting: **the segmentation framework guided the team after I moved to another rotation.** Junior designers inherited a decision system, not just designs. It became how the team navigated competing needs simultaneously.

Systems over surfaces. The cohort segmentation—which shipped no UI—was more valuable than the visual redesign. It gave the team language for making tradeoffs that scale.

---

**Word count: 458** | **Reading time: 2–3 minutes**