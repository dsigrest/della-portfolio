# Hiding & restoring homepage case study cards

Operational reference for temporarily hiding a case study card from `index.html` without removing the underlying detail page or destroying any history. Future chats: when Della says "hide [case]" or "restore [case] on the homepage," follow this doc.

---

## Current hidden state

| Card | Status | Hidden on | Restore via |
|------|--------|-----------|-------------|
| Building This Portfolio (`case-building-portfolio.html`) | **Hidden on live site** as of merge of PR `hide-building-portfolio-card` (Apr 29, 2026). Detail page still reachable at `/case-building-portfolio.html`. | 2026-04-29 | See restore prompt below. |

When the state changes (a card is hidden or restored), update this table.

---

## How the hide works

The hide is a pure HTML edit on `portfolio-site/index.html`: the card's `<a class="card ...">...</a>` block is wrapped in an outer HTML comment with named markers so it's findable and reversible.

Two HTML constraints shape the implementation:

1. **HTML comments don't nest.** `<!-- A <!-- B --> C -->` ends at the first `-->`, leaving "C -->" rendered as live text. So if the card block already contains an inner `<!-- ... -->` (e.g. `<!-- CARD 05 — Full width -->`), we strip the inner comment markers and leave the inner text as bare characters inside the outer comment. Bare text inside a comment is inert.
2. **Findability via grep.** Wrapping leaves the card's identifying string in the file, so `grep -n "CARD 05" portfolio-site/index.html` (or whatever the card's label is) prints the line. The HIDDEN markers themselves are also greppable.

The hide is committed on a dedicated branch (`hide-<card-slug>`) created via `git worktree` from `origin/main`, so it never entangles with in-flight work on the main checkout.

---

## Hide prompt (paste into Claude Code)

Replace `<CARD NAME>`, `<CARD NUMBER>` (e.g. `CARD 05`), and `<DETAIL FILE>` (e.g. `case-building-portfolio.html`) with the actual values.

```
Temporarily hide the "<CARD NAME>" case study from my portfolio homepage.

In portfolio-site/index.html, find the <CARD NUMBER> block — the <a href="<DETAIL FILE>" class="card ..."> ... </a> block including its "<!-- <CARD NUMBER> — ... -->" comment.

Wrap the entire block (including the existing comment) inside an outer HTML comment with these exact marker lines:

  <!-- HIDDEN: <card-slug> case study — restore by removing this wrapper -->
  <!--
  [original block here]
  -->
  <!-- /HIDDEN -->

Important: HTML comments don't nest. If the original block contains "<!-- ... -->" comments, strip those inner comment markers and leave the inner label text as plain characters inside the outer comment. Do NOT leave nested "<!--" or "-->" inside the outer wrapper.

Do not modify <DETAIL FILE> itself — leave the detail page in place so the URL still works for direct links.

Then, do NOT commit on the current branch. Use git worktree to do the commit safely:
1. git fetch origin
2. git worktree add -b hide-<card-slug> ../portfolio-site-<card-slug>-hide origin/main
3. In the worktree, apply the same index.html edit (or cherry-pick from the working tree if cleaner).
4. Commit with message: chore: temporarily hide "<CARD NAME>" case study from homepage
5. git push -u origin hide-<card-slug>
6. Print the GitHub PR creation URL.

Leave the worktree in place. Do NOT touch local main, the original working tree, or any stash. Stop and ask if anything is destructive.

After this, I open the PR on GitHub and merge to main when ready. Vercel auto-deploys from main.
```

After GitHub merge, ask Claude Code to clean up:

```
The hide-<card-slug> PR is merged and the live site is updated. Please:
1. Remove the worktree: git worktree remove ../portfolio-site-<card-slug>-hide
2. Delete the local branch: git branch -D hide-<card-slug>
3. Update working/planning-docs/homepage-card-hide-restore.md — flip the "Current hidden state" row for this card to reflect the merge date.
```

---

## Restore prompt (paste into Claude Code)

Replace `<card-slug>` with the slug used in the HIDDEN marker (e.g. `building-portfolio`).

```
Restore the hidden "<card-slug>" case study card on my portfolio homepage.

In portfolio-site/index.html, find the wrapper marked:
  <!-- HIDDEN: <card-slug> case study — restore by removing this wrapper -->
  ...
  <!-- /HIDDEN -->

Remove the two HIDDEN marker comments and the surrounding <!-- ... --> wrapper, leaving the original card block intact and active. If the original card block had an inner "<!-- ... — ... -->" label comment that was stripped during hide, restore that label as a comment.

Do not commit on the current branch. Use git worktree:
1. git fetch origin
2. git worktree add -b restore-<card-slug> ../portfolio-site-<card-slug>-restore origin/main
3. Apply the unwrap edit in the worktree.
4. Commit with message: chore: restore "<card-slug>" case study on homepage
5. git push -u origin restore-<card-slug>
6. Print the GitHub PR creation URL.

Leave the worktree in place; I'll merge on GitHub. Do NOT touch local main, the original working tree, or any stash.

After merge, update working/planning-docs/homepage-card-hide-restore.md — remove the row for this card from "Current hidden state."
```

---

## Why isolated branches

Local `main` and the original working tree on this repo are often dirty with parallel session work. Pushing from local `main` would carry that work along; cherry-picking onto a dirty `main` risks breakage. The `git worktree` workflow:

- Creates a clean checkout of `origin/main` in a sibling folder.
- Lands the hide/restore commit on a fresh branch in that folder.
- Leaves the original checkout, local `main`, and any stash completely untouched.
- Produces a single-commit PR that's easy to review and merge.

The cost is one extra folder on disk until cleanup. Worth it.

---

## Stronger hide (if direct URL must also be unreachable)

The default hide leaves the detail page accessible at its URL. If a card needs to be fully unreachable (e.g. confidential content, takedown):

- Add a redirect in `vercel.json` from `/<detail-file>` to `/`, or
- Rename the file (e.g. `case-X.html` → `case-X.html.hidden`) and update any other internal links.

Both options are reversible but heavier than the default hide. Use only when needed.
