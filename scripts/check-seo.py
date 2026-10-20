"""Check the rendered site, including sitemap contents and JSON-LD."""
from pathlib import Path
from html.parser import HTMLParser
import json
import struct
import xml.etree.ElementTree as ET

BASE = 'https://azuromalachite.github.io'
SITE = Path('_site')
class Head(HTMLParser):
    def __init__(self):
        super().__init__(); self.title=''; self.meta=[]; self.links=[]; self.json=[]; self.in_title=False; self.in_json=False
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag=='title': self.in_title=True
        if tag=='meta': self.meta.append(attrs)
        if tag=='link': self.links.append(attrs)
        if tag=='script' and attrs.get('type')=='application/ld+json': self.in_json=True; self.json.append('')
    def handle_endtag(self, tag):
        if tag=='title': self.in_title=False
        if tag=='script': self.in_json=False
    def handle_data(self, data):
        if self.in_title: self.title+=data
        if self.in_json: self.json[-1]+=data

routes=['/','/publications/','/cv/','/art-biodesign/','/teaching/',
        '/publications/2020-cas13-clinical-validation/', '/publications/2022-metagenomic-pet-hydrolase/',
        '/publications/2023-multiplexed-cas13-diagnostics/', '/publications/2024-pet-recycling-upcycling-review/',
        '/publications/2025-recombinase-condensates/']
profiles={'https://scholar.google.com/citations?user=ejfOOWAAAAAJ&hl=en',
          'https://www.linkedin.com/in/thanakrit-wongsatit-59a540125/',
          'https://github.com/Azuromalachite','https://bsky.app/profile/austintw.bsky.social'}
descriptions=[]
for route in routes:
    path=SITE / route.lstrip('/') / 'index.html'
    parser=Head(); parser.feed(path.read_text(encoding='utf-8'))
    desc=[m['content'] for m in parser.meta if m.get('name')=='description']
    assert len(desc)==1 and len(desc[0])>50, f'Missing/duplicate description: {route}'
    descriptions.append(desc[0])
    assert [link['href'] for link in parser.links if link.get('rel')=='canonical']==[BASE+route], route
    assert not any('noindex' in m.get('content','') for m in parser.meta if m.get('name')=='robots'), route
    assert any(m.get('property')=='og:image' and m.get('content')==BASE+'/images/social-preview.png' for m in parser.meta), route
    assert any(m.get('name')=='twitter:card' and m.get('content')=='summary_large_image' for m in parser.meta), route
    data=[json.loads(s) for s in parser.json]
    person=next(s for s in data if s.get('@type')=='Person')
    assert person['name']=='Thanakrit Wongsatit' and set(person['sameAs'])==profiles, route
    assert person['affiliation']['@type']=='CollegeOrUniversity', route
    assert 'Austin Wongsatit' in person['alternateName'], route
    if route=='/':
        assert parser.title=='Thanakrit (Austin) Wongsatit — Microbiome Engineering at KAIST', parser.title
        assert any(s.get('@type')=='WebSite' for s in data)
assert len(set(descriptions))==len(routes), 'Page descriptions should be distinct'

urls={x.text for x in ET.parse(SITE/'sitemap.xml').findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
allowed={BASE+r for r in routes}|{BASE+'/files/2020-08-26-paper.pdf'}
assert urls <= allowed, f'Unexpected sitemap URLs: {urls-allowed}'
assert {BASE+r for r in routes} <= urls, 'Missing real content in sitemap'
for path in ['markdown/index.html','non-menu-page/index.html','terms/index.html','markdown_generator/index.html',
             'files/paper1.pdf','files/paper2.pdf','files/paper3.pdf','files/slides1.pdf','files/slides2.pdf','files/slides3.pdf','talkmap/map.html']:
    assert not (SITE/path).exists(), f'Template content still published: {path}'
assert BASE+'/sitemap.xml' in (SITE/'robots.txt').read_text()
for path in ['404.html','sitemap/index.html']:
    parser=Head();parser.feed((SITE/path).read_text(encoding='utf-8'))
    assert any(m.get('name')=='robots' and 'noindex' in m.get('content','') for m in parser.meta), path
image=(SITE/'images/social-preview.png').read_bytes()
assert image[:8]==b'\x89PNG\r\n\x1a\n' and struct.unpack('>II',image[16:24])==(1200,630)
print('SEO checks passed for 10 content pages, identity data, sharing metadata, and clean sitemap.')
