# Sharing & Embeds

Reddit content looked terrible when shared. Link previews broke across platforms. The share sheet was friction-heavy. There was no coherent model for how sharing interacted with privacy norms. Users wanted to share more but didn't.

**Sharing isn't a feature—it's a system with three simultaneous events:** distribution (content reaches new audiences), acquisition (new users encounter Reddit), and re-engagement (the sharer returns to see responses). The infrastructure wasn't designed to capitalize on any of them.

[IMAGE: Share sheet UI, link preview variants, cross-platform comparison]

## The Insight: Privacy as Growth Lever

Users weren't sharing because they couldn't control what was visible. When sharing, you expose your interest graph—communities, upvotes, comment history. That vulnerability made casual users reluctant to share in semi-public channels like Slack.

**Privacy wasn't a constraint on sharing. Privacy controls were the growth lever.** Most users who didn't share had already opted out. Giving them confidence in what they exposed unlocked sharing from a population that had gone silent.

## Three-Stage Flywheel

**Stage 1: Streamline the sheet**
Reduced friction, added channels. Most-used destinations first. Users willing to share need velocity—sub-3-tap execution or momentum breaks.

**Stage 2: Improve the preview**
Redesigned link previews and embeds. Shared Reddit content looked like Reddit when received, not like generic URLs. Open Graph metadata consistency across platforms. Rich previews.

**Stage 3: Privacy as activation**
Introduced granular controls: share a post but hide your profile. Share a thread but limit visibility to DMs. Controls visible in the sheet itself, not buried in settings.

These weren't friction. They were *enablers.*

## Privacy Unlocks Silent Cohorts

**The composition of sharers shifted.** Lurkers started sharing posts they found valuable—with controls ensuring their profile stayed hidden. Mid-tier users shared more frequently because they controlled visibility. Power users felt safer resharing community discussions with limited visibility.

Test results with privacy controls visible in the sheet: **[sharing volume increase %]. More diverse distribution of sharers—more lurkers, more mid-tier, more geographic diversity.**

The pool of willing sharers grew more than per-share friction reduced. Privacy controls activated previously silent cohorts.

[IMAGE: Privacy control UI, share sheet redesign, control levels]

## System Design

- **Persistence** — Save share sheet state across sessions
- **Channel priority** — Surface most-used first, all visible in one tap
- **Preview refresh** — See how content renders on destination platform before sending
- **Granular controls** — Post, subreddit, profile levels—different content needs different strategies

## Outcome

Three-stage approach increased **off-platform reach by [●●]%, expanded channels from [X to Y], established reusable embed components** adopted across product teams.

Later, when Reddit built third-party publisher embeds, this architecture scaled into developer-facing infrastructure.

Most lasting: **privacy-as-growth-lever became a reference point for how growth initiatives approached user control and distribution.** The framework influenced subsequent initiatives: growth doesn't always mean removing friction. Sometimes privacy is the unlock.

The embed components became the reference architecture when building infrastructure for external publishers—showing how systems thinking scales beyond mobile into platform infrastructure.

## Reflection

Design's most impactful contribution is often the frame, not the form. The reframe—seeing sharing as a flywheel with privacy as the activation point—unlocked an entirely different set of design possibilities.

A better interface without the right frame optimizes the wrong thing.

---

**Word count: 441** | **Reading time: 2–3 minutes**