"""Check excluded examples by their actual permalink, including non-sitemap output.

The current config uses a literal scalar exclude list, and sample front matter
uses single-line titles/permalinks. Fail explicitly if that format changes.
"""
from pathlib import Path
from html import unescape
import json
import re

SITE=Path('_site')
config=Path('_config.yml').read_text(encoding='utf-8')
block=re.search(r'^exclude:\s*\n(.*?)(?=^\S)',config,re.M|re.S)
assert block,'Missing exclude list'
excluded=[]
for line in block[1].splitlines():
    if not line.strip() or line.lstrip().startswith('#'):continue
    match=re.fullmatch(r'\s+-\s+(.+?)\s*',line)
    assert match,f'Unsupported exclude syntax: {line}'
    excluded.append(match[1].strip('"\''))

def scalar(front,key):
    match=re.search(r'^'+key+r':\s*(.+?)\s*$',front,re.M)
    return match[1].strip('"\'') if match else None

families={'_posts','_publications','_talks','_teaching','_portfolio'}
examples=[Path(p) for p in excluded if Path(p).parts[0] in families]
assert examples,'No excluded collection examples found'
titles=[]
for source in examples:
    text=source.read_text(encoding='utf-8')
    assert text.startswith('---\n'),source
    front=text.split('---',2)[1]
    title=scalar(front,'title');assert title,source
    titles.append(title)
    route=scalar(front,'permalink')
    if not route:
        # The portfolio samples use the configured collection default.
        collection=source.parts[0][1:]
        assert 'permalink: /:collection/:path/' in config,collection
        route=f'/{collection}/{source.stem}/'
    assert route.startswith('/') and '{{' not in route,source
    base=SITE/route.lstrip('/')
    candidates=[base,Path(str(base)+'.html'),base/'index.html']
    assert not any(p.is_file() for p in candidates),f'Excluded example rendered: {source} -> {route}'

# Also catch copies/alternate routes and sitemap:false pages, outside the sitemap.
for output in list(SITE.rglob('*.html'))+list(SITE.rglob('*.xml')):
    body=unescape(output.read_text(encoding='utf-8'))
    assert not any(title in body for title in titles),f'Template title leaked into {output}'

retired=json.loads(Path('scripts/retired-assets.json').read_text(encoding='utf-8'))
for name in retired:
    assert not (SITE/name).exists(),f'Retired asset still published: {name}'
assert not Path('.github/    workflows  /scrape_talks.yml').exists()
print(f'All {len(examples)} excluded examples and {len(retired)} retired assets are absent.')
