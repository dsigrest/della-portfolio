# Threads Kickoff — responsive-audit Scaling

Copy-paste these into new Cowork threads AFTER Thread 1 (case-notifications POC) passes. One thread per case study keeps context clean — the `responsive-audit` skill reads the shared tracker and picks up where prior threads left off.

**Tracker location:** `~/CoworkWorkspace/Get-a-job/portfolio-site/working/mobile-audit/audit-tracker.xlsx`

---

## Thread 2 — case-ai (19 diagrams, biggest)

```
Run responsive-audit on case-ai. Read the tracker at Get-a-job/portfolio-site/working/mobile-audit/audit-tracker.xlsx, audit all 19 diagrams across the 6 breakpoints, apply L1 + L2 fixes inline, and produce L3 redesigns paired in Figma (mobile on right of desktop, same row, on the case-ai page). Update the tracker as you go. Pause and surface the L3 diagrams for my review before finalizing Figma.
```

---

## Thread 3 — case-subreddit (10 + 1 orphan)

```
Run responsive-audit on case-subreddit. 10 live diagrams plus the sub12-text-bars orphan (audit only, no Figma pairing for orphan). Read the tracker first, do full audit + fix + Figma pairing per the skill's convention. Update the tracker. Flag any L3 redesigns for my review before pairing.
```

---

## Thread 4 — case-sharing (8 diagrams)

```
Run responsive-audit on case-sharing. 8 diagrams. Read the tracker, do full audit + fix + Figma pairing per the skill. Update the tracker. Flag L3 redesigns for my review.
```

---

## Thread 5 — case-building-portfolio (5 diagrams)

```
Run responsive-audit on case-building-portfolio. 5 diagrams. Della's read: probably mostly L0-L1, but confirm via audit. Read the tracker, do full audit + fix + Figma pairing per the skill. Update the tracker.
```

---

## Recommended order

1. Thread 2 first (case-ai) — highest value, stress-tests the skill with 19 diagrams before scaling
2. Thread 3 (case-subreddit) — second most work
3. Threads 4 and 5 can run in parallel on different devices if you want

## Common flags to add to any thread

- `--dry-run` if you want the audit output without applying fixes
- `--skip-figma` if Figma MCP is flaky that day (fixes happen, pairing deferred)
- `--verify-only` to just re-screenshot and check for regressions on a previously-fixed case study
