"""Check versioned essays: numbering, frozen published versions, and rendered routes.

    python3 scripts/check-essays.py source [BASE_REF]   # before building
    python3 scripts/check-essays.py rendered SITE_DIR   # after building

A published version is permanent. Against BASE_REF (the PR base or the previous
push), every vN.md that was published there must still exist with the same text
and the same front matter; only its `errata:` block may grow. See ESSAYS.md.
"""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path('_essays')

def split(text, source):
    text = text.replace('\r\n', '\n')
    assert text.startswith('---\n'), f'{source}: missing front matter'
    _, front, body = text.split('---', 2)
    return front, body

def scalar(front, key):
    match = re.search(r'^' + key + r':\s*(.+?)\s*$', front, re.M)
    return match[1].strip('"\'') if match else None

def published(front):
    return scalar(front, 'published') != 'false'

def frozen(front):
    """Front matter without the errata block, which is the one part allowed to change."""
    kept, in_errata = [], False
    for line in front.splitlines():
        if line.startswith('errata:'):
            in_errata = True; continue
        if in_errata and (line.startswith((' ', '-')) or not line.strip()):
            continue
        in_errata = False; kept.append(line)
    return kept

def essays():
    """Yield (slug, record front matter, {version number: front matter})."""
    for directory in sorted(p for p in ROOT.iterdir() if p.is_dir()):
        slug = directory.name
        names = sorted(p.name for p in directory.iterdir())
        assert 'index.md' in names, f'{slug}: missing index.md (the record page)'
        stray = [n for n in names if n != 'index.md' and not re.fullmatch(r'v[1-9]\d*\.md', n)]
        assert not stray, f'{slug}: only index.md and vN.md belong here, found {stray}'
        record, _ = split((directory / 'index.md').read_text(encoding='utf-8'), directory / 'index.md')
        versions = {}
        for name in names:
            if name != 'index.md':
                versions[int(name[1:-3])], _ = split((directory / name).read_text(encoding='utf-8'), directory / name)
        yield slug, record, versions

def check_source(base):
    count = 0
    for slug, record, versions in essays():
        assert re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', slug), f'{slug}: use a lowercase, hyphenated folder name'
        assert scalar(record, 'essay') == slug, f'{slug}/index.md: essay: must be {slug}'
        assert scalar(record, 'layout') == 'essay-record', f'{slug}/index.md: layout: must be essay-record'
        assert scalar(record, 'permalink') == f'/essays/{slug}/', f'{slug}/index.md: permalink: must be /essays/{slug}/'
        assert scalar(record, 'sitemap') == 'true', f'{slug}/index.md: sitemap: must be true'
        assert scalar(record, 'abstract'), f'{slug}/index.md: missing abstract:'
        assert len(scalar(record, 'description') or '') > 50, f'{slug}/index.md: description: must be over 50 characters'
        numbers = sorted(versions)
        assert numbers == list(range(1, len(numbers) + 1)), f'{slug}: versions must run v1..vN without gaps, found {numbers}'
        dates = []
        for n in numbers:
            front = versions[n]
            assert scalar(front, 'essay') == slug, f'{slug}/v{n}.md: essay: must be {slug}'
            assert scalar(front, 'version') == str(n), f'{slug}/v{n}.md: version: must be {n}'
            assert scalar(front, 'permalink') is None, f'{slug}/v{n}.md: remove permalink:, versions use /essays/{slug}/v{n}/'
            assert scalar(front, 'title'), f'{slug}/v{n}.md: missing title:'
            date = scalar(front, 'date')
            assert date and re.fullmatch(r'\d{4}-\d{2}-\d{2}', date), f'{slug}/v{n}.md: date: must be YYYY-MM-DD'
            dates.append(date)
        assert dates == sorted(dates), f'{slug}: version dates go backwards: {dates}'
        live = [published(versions[n]) for n in numbers]
        # Published versions are a prefix: a draft of the next version may wait, an old one may not be withdrawn.
        assert live == sorted(live, reverse=True), f'{slug}: a draft version sits below a published one'
        assert published(record) == any(live), f'{slug}: the record page and its versions must be published together'
        count += 1
    print(f'{count} essay folder(s): numbering, dates and record pages are consistent.')
    check_frozen(base)

def git(*args):
    return subprocess.run(['git', *args], capture_output=True, text=True, encoding='utf-8')

def check_frozen(base):
    if not base or set(base) == {'0'} or git('rev-parse', '--verify', '--quiet', base + '^{commit}').returncode:
        print(f'No base commit available ({base or "none given"}); frozen-version check skipped.')
        return
    checked = 0
    for name in git('ls-tree', '-r', '--name-only', base, '--', str(ROOT)).stdout.split():
        if not re.fullmatch(r'_essays/[^/]+/v\d+\.md', name):
            continue
        old_front, old_body = split(git('show', f'{base}:{name}').stdout, f'{name}@{base[:7]}')
        if not published(old_front):
            continue  # drafts may still change
        assert Path(name).exists(), f'{name} was published at {base[:7]} and has been deleted; published versions are permanent'
        front, body = split(Path(name).read_text(encoding='utf-8'), name)
        assert body == old_body, f'{name}: published text changed since {base[:7]}; publish a new version, or add an errata entry'
        assert frozen(front) == frozen(old_front), f'{name}: front matter changed since {base[:7]}; only errata: may be added'
        checked += 1
    print(f'{checked} published version(s) unchanged since {base[:7]}.')

def check_rendered(site):
    site = Path(site)
    sitemap = (site / 'sitemap.xml').read_text(encoding='utf-8')
    count = 0
    for slug, record_front, versions in essays():
        route = site / 'essays' / slug
        live = [n for n in sorted(versions) if published(versions[n])]
        if not published(record_front):
            assert not route.exists(), f'Unpublished essay rendered: {route}'
            continue
        record = (route / 'index.html').read_text(encoding='utf-8')
        latest = live[-1]
        assert len(re.findall(r'<h1\b', record)) == 1, f'{slug}: record page needs exactly one h1'
        assert f'/essays/{slug}/v{latest}/' in record and 'Read the latest version' in record, f'{slug}: record page must link the latest version'
        assert f'/essays/{slug}/</loc>' in sitemap, f'{slug}: record page missing from sitemap'
        for n in live:
            html = (route / f'v{n}' / 'index.html').read_text(encoding='utf-8')
            assert f'/essays/{slug}/v{n}/' in record, f'{slug}: record page does not list v{n}'
            assert len(re.findall(r'<h1\b', html)) == 1, f'{slug}/v{n}: needs exactly one h1'
            assert '{{' not in html and '{%' not in html, f'{slug}/v{n}: unrendered Liquid'
            assert f'href="/essays/{slug}/"' in html, f'{slug}/v{n}: no link back to the record page'
            assert f'Version {n} of {latest}' in html, f'{slug}/v{n}: version status missing'
            if n < latest:
                assert 'A newer version exists' in html and f'/essays/{slug}/v{latest}/' in html, f'{slug}/v{n}: no pointer to v{latest}'
            else:
                assert 'This is the latest version' in html, f'{slug}/v{n}: not marked as latest'
            if 'errata:' in versions[n]:
                assert 'class="essay-errata"' in html, f'{slug}/v{n}: errata not shown'
            assert f'/essays/{slug}/v{n}/</loc>' not in sitemap, f'{slug}/v{n}: frozen versions stay out of the sitemap'
        for n in sorted(set(versions) - set(live)):
            assert not (route / f'v{n}').exists(), f'{slug}/v{n}: draft version rendered'
        count += 1
    print(f'{count} published essay(s) render with version status, history and sitemap entries.')

if __name__ == '__main__':
    mode, arg = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else '')
    {'source': check_source, 'rendered': check_rendered}[mode](arg)
