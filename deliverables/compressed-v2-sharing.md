# Sharing & Embeds

**Word count:** 1,042 | **Reading time:** 5–6 minutes

---

## The Problem: Sharing Was Broken

Reddit content looked terrible when shared. Link previews were inconsistent across platforms—what rendered on Twitter looked broken on Slack. The share sheet offered limited channels and required multiple taps. There was no coherent model for how sharing should interact with Reddit's privacy norms.

The organization knew this was a gap. Research showed that users wanted to share more but didn't because the experience was friction-heavy and the output looked bad. But sharing was nobody's explicit responsibility. It lived between mobile, web, growth, and platform teams.

**Every share represents three simultaneous events:** distribution (content reaches new audiences), acquisition (new users encounter Reddit), and re-engagement (the sharer returns to see responses). The infrastructure wasn't designed to capitalize on any of them.

[IMAGE: Share sheet UI, link preview variations, cross-platform preview comparison]

---

## The Insight: Sharing as a Flywheel

**Sharing isn't a feature—it's a system with multiple intervention points.** The design challenge wasn't "add more buttons" or "make prettier previews." It was designing each stage of the distribution → acquisition → re-engagement loop to maximize throughput while respecting Reddit's community-first privacy culture.

The reframe revealed a counterintuitive lever: **most users weren't sharing because they couldn't control what was visible.** When someone shares a post, they expose their interest graph—their communities, upvoting patterns, and comment history. That vulnerability made casual users reluctant to share, especially in semi-public channels like Slack.

Privacy wasn't a constraint on sharing. **Privacy controls were the growth lever.** Giving users confidence in what they exposed unlocked sharing from the population that had already opted out.

---

## Three-Stage Flywheel

I designed a **3-stage approach**, each building on the last:

**Stage 1: Streamline and expand**
Redesigned the share sheet to reduce friction and added new channels. Focused on making common paths (messaging apps, social media) as fast as possible. The insight here was velocity: a user willing to share should be able to execute the share in under 3 taps. If you make them tap more than that, you lose momentum.

**Stage 2: Improve the preview**
Redesigned link previews and embeds so shared Reddit content actually looked good on the receiving end—consistent metadata, rich previews, proper Open Graph implementation across platforms. A shared post looked like a Reddit post when received, not like a generic URL.

**Stage 3: Privacy as growth**
Introduced privacy controls letting users share with confidence. Not as friction. As an *enabler*. Users could share a post but hide their profile from preview. Share a comment thread but limit visibility to direct messages only. These controls had to be discoverable in the share sheet itself, not buried in settings.

### Privacy Reframes Growth

**Privacy controls increased total sharing volume by unlocking the population that had already opted out.**

Users weren't sharing because they couldn't control what was visible. They self-selected out of the sharing funnel entirely. Granular control over what reached third-party platforms and how their content was represented activated this previously silent cohort.

The composition of sharers shifted. Lurkers started sharing posts they found valuable—with privacy controls ensuring their profile stayed hidden. Mid-tier users shared more frequently because they could control which communities were visible. Power users felt safer resharing community discussions because they could limit visibility.

**Privacy controls increased total sharing volume because the pool of willing sharers grew more than per-share friction reduced it.** In the test condition with privacy controls visible, sharing volume increased 14% and the distribution of sharers became more diverse—more lurkers, more mid-tier users, more geographic diversity.

[IMAGE: Privacy control UI, share sheet redesign, privacy settings flow]

---

## System Design Decisions

- **Persistence**: Save share sheet state across sessions. Repeated shares shouldn't require rediscovery of the right channel.
- **Channel priority**: Surface most-used channels first based on user history, but show all options within one tap. Channel discoverability matters as much as speed.
- **Preview refresh**: Let users see how content will render on the destination platform before sending. This prevented regret shares.
- **Granularity**: Privacy controls operate at three levels—post, subreddit, and profile—not one global toggle. Different content needs different strategies.

[IMAGE: Share sheet state persistence, preview variations, privacy level options]

---

## Outcome: Flywheel in Motion

The 3-stage approach increased off-platform reach by 32%, expanded available sharing channels from 6 to 14, and established reusable components for the share sheet and embed system that other product teams could build on. The embed components became the reference architecture when Reddit later built its embed system for third-party publishers—showing how this work scaled beyond the mobile app into developer-facing infrastructure.

More importantly, **the privacy-as-growth-lever framework influenced how subsequent growth initiatives approached the tension between user control and distribution.** It became a reference point: growth doesn't always mean removing friction. Sometimes it means inverting the constraint. Sometimes privacy is the unlock.

---

## Reflection: Reframing as Design Method

This project taught me that the power of design isn't always in execution—it's in reframing. The share sheet redesign was the expected work. The preview optimization was table stakes. The insight that made the project valuable was the flywheel framing: seeing sharing as a system with multiple intervention points, not a single feature.

And the privacy-as-growth reframe turned what the team initially saw as a blocker into the project's most interesting design decision.

**Design's most impactful contribution is often the frame, not the form.** A better interface without the right frame optimizes the wrong thing. A good frame unlocks entirely different possibilities.