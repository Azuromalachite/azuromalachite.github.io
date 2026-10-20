# Thanakrit (Austin) Wongsatit — personal website

[Visit the website](https://azuromalachite.github.io/)

This repository contains my personal website, covering microbiome engineering and related research, Southeast Asian blue-banded bee natural history, art and biodesign, and teaching and community work. It is built with Jekyll using Academic Pages and hosted on GitHub Pages.

## Editing content

| Content | File or directory |
| --- | --- |
| About and homepage | [`_pages/about.md`](_pages/about.md) |
| Full biography within the homepage | [`_includes/home-biography.md`](_includes/home-biography.md) |
| Homepage layout and styles | [`_layouts/home-editorial.html`](_layouts/home-editorial.html), [`assets/css/home.css`](assets/css/home.css) |
| Research overview | [`_pages/research.md`](_pages/research.md) |
| Natural history | [`_pages/natural-history.md`](_pages/natural-history.md) |
| Art and biodesign | [`_pages/art-biodesign.md`](_pages/art-biodesign.md) |
| Teaching and community | [`_pages/teaching.html`](_pages/teaching.html) |
| CV | [`_pages/cv.md`](_pages/cv.md) |
| Publication records | [`_publications/`](_publications/) |
| Publication list layout | [`_pages/publications.html`](_pages/publications.html) |
| Downloadable bibliography | [`files/publications.bib`](files/publications.bib) |
| Main navigation | [`_data/navigation.yml`](_data/navigation.yml) |
| Profile, contact links, and site settings | [`_config.yml`](_config.yml) |
| Photographs and other images | [`images/`](images/) |

Keep publication records and the BibTeX bibliography consistent, using the publisher's exact title, author list, and DOI. Upload full-text papers only when permission to share that version has been established. Give images descriptive alt text and appropriate captions and credits.

The homepage uses a separate editorial layout; inner pages retain Academic Pages. Set `selected_home: true` on a publication record to feature it on the homepage. Its year, title, venue, authorship role, and contribution or summary are read from that record; `homepage_title` can supply a shorter display title without changing the citation.

Some original template examples remain in the repository for reference. They are excluded from publication in `_config.yml`. This README and the maintenance scripts are also excluded from the generated website.

## Publishing updates

1. Create a working branch from the latest `master`.
2. Edit the content and open a pull request into `master`.
3. Wait for **Check website build / build** to pass, and review the changes.
4. Merge the pull request. GitHub Pages then builds and publishes the site from `master` at the repository root.
5. Check the live pages after deployment completes. Delete the working branch once its changes are merged.

The active ruleset on `master` requires a pull request and the passing `build` check, with no required review approvals. It also blocks branch deletion and force pushes. Ordinary working branches are not covered by this ruleset.

[Pull requests](https://github.com/Azuromalachite/azuromalachite.github.io/pulls) · [Build and deployment status](https://github.com/Azuromalachite/azuromalachite.github.io/actions) · [Branch rules](https://github.com/Azuromalachite/azuromalachite.github.io/rules)

## Previewing locally

With Ruby and Bundler installed, run these commands from the repository directory:

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

Open [localhost:4000](http://localhost:4000/). Restart the preview after changing `_config.yml`. Local dependency versions can differ from GitHub Pages; the pull request build is the publishing check.

To run the maintenance checks after generating the site:

```sh
bundle exec jekyll build
python3 scripts/check-seo.py
python3 scripts/check-structure.py
python3 scripts/check-accessibility.py
python3 scripts/check-excluded.py
```

On Windows, use `python` in place of `python3` if that is the installed command. These checks cover search metadata and sitemap contents, navigation and page hierarchy, publication links, and excluded examples and retired assets. Ownership verification files are also checked in the GitHub Actions workflow.

## Credits and licence

The site is adapted from [Academic Pages](https://github.com/academicpages/academicpages.github.io), originally forked by Stuart Geiger from Michael Rose's [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) theme and subsequently maintained by Robert Zupko and other contributors.

The inherited theme code is distributed under the [MIT licence](LICENSE), including the original © 2016 Michael Rose notice. Photographs, artwork, publication files, and other third-party materials may have separate rights or licences; the theme licence does not establish permission to reuse those materials.
