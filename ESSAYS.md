# Versioned essays

Essays are published like preprints. Each version keeps its own address forever, and one stable address always leads to the latest version.

```
_essays/<slug>/index.md  → /essays/<slug>/      record page: abstract, latest version, history, citation
_essays/<slug>/v1.md     → /essays/<slug>/v1/   frozen once published
_essays/<slug>/v2.md     → /essays/<slug>/v2/
```

`_essays/example-essay/` shows every field. It is never published on the live site. CI publishes it into a scratch copy, builds that copy, checks the pages, and uploads the result as the `essay-example` artifact.

## The rule

**A published version never changes.** `scripts/check-essays.py` enforces this in CI. Every `vN.md` that was published on the base commit must still exist, with the same text and the same front matter. The one exception is its `errata:` list, which may only grow.

- **To fix a typo or an error:** add an `errata:` entry to that version. If the fix matters to readers, publish a new version.
- **To revise:** add the next `vN.md`. The older versions stay online and gain a "newer version exists" notice automatically.
- **To prepare a draft:** add `vN.md` with `published: false`. A draft can be edited freely until it is published, and only the newest version may be a draft.

## Publish a first version

1. Copy `_essays/example-essay/` to `_essays/<slug>/`. The slug must be lowercase and hyphenated.
2. In `index.md`, set these fields and delete `published: false`:
   - `essay: <slug>`
   - `permalink: /essays/<slug>/`
   - `title`
   - `abstract`
   - a `description` over 50 characters, distinct from other pages
3. In `v1.md`, set these fields, put the text below the front matter, and delete `published: false`:
   - `essay: <slug>`
   - `version: 1`
   - `date: YYYY-MM-DD`
   - `title`
   - `description`
   - `changes`
4. Delete `v2.md` and the example erratum.
5. Open a PR. CI checks the numbering, the record page, and (after merge) the frozen text.

## Publish a revision

1. Copy the latest `vN.md` to `v(N+1).md` and edit the copy. Never edit the original.
2. Bump `version:` and `date:`, and replace `changes:` with what changed. This list is the changelog readers see on the record page.
3. Merge. Optionally tag the merge commit, so that GitHub can show the exact text diff between versions:

   ```bash
   git tag -a essays/<slug>/v2 -m "<title>, version 2"
   git push origin essays/<slug>/v2
   ```

   GitHub then shows the diff at `https://github.com/Azuromalachite/azuromalachite.github.io/compare/essays/<slug>/v1...essays/<slug>/v2`.

## Optional: a DOI

To get a DOI, create a GitHub Release for each version tag in a repository connected to Zenodo. Zenodo mints:
- one **concept DOI** for the essay as a whole;
- one DOI per version.

Put the concept DOI in `index.md` as `doi:`. The record page and every version's citation then show it.

Use a small repository that holds only the essay, so that each release doesn't archive the whole website.

## Linking from social posts

Link to the version the post describes (`/essays/<slug>/v2/`), so the post never quotes text that has since changed. That page's notice will point readers to anything newer.

Link to the record page (`/essays/<slug>/`) when you mean "the essay" in general.
