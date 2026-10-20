"""Check the site's navigation and content hierarchy after Jekyll renders it."""
from html.parser import HTMLParser
from pathlib import Path

class Structure(HTMLParser):
    def __init__(self):
        super().__init__();self.content=False;self.headings=[];self.links=[];self.heading=None;self.text='';self.nav=False;self.nav_links=[];self.anchor=None;self.anchor_text=''
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'href' in a:a['href']=a['href'].removeprefix('https://azuromalachite.github.io')
        if tag=='section' and 'page__content' in a.get('class','').split():self.content=True
        if tag=='nav' and a.get('id')=='site-nav':self.nav=True
        if tag=='a':
            self.links.append(a.get('href',''))
            if self.nav:self.anchor=a.get('href','');self.anchor_text=''
        if self.content and tag in ['h2','h3']:self.heading=tag;self.text=''
    def handle_data(self,data):
        if self.heading:self.text+=data
        if self.anchor is not None:self.anchor_text+=data
    def handle_endtag(self,tag):
        if tag==self.heading:self.headings.append((tag,self.text.strip().replace('’', "'")));self.heading=None
        if tag=='section':self.content=False
        if tag=='a' and self.anchor is not None:
            self.nav_links.append((self.anchor,self.anchor_text.strip()));self.anchor=None
        if tag=='nav':self.nav=False

def page(route):
    parser=Structure();parser.feed((Path('_site')/route.lstrip('/')/'index.html').read_text(encoding='utf-8'));return parser

expected=[('/', 'About'),('/research/','Research'),('/natural-history/','Natural History'),('/art-biodesign/','Art & Biodesign'),('/teaching/','Teaching & Community'),('/cv/','CV')]
home=page('/')
assert home.nav_links[1:]==expected,home.nav_links
assert [title for level,title in home.headings if level=='h2']==['Background','Life in context','Beyond research']
assert [title for level,title in home.headings if level=='h3']==['Natural history','Art & biodesign','Teaching & community']
for route,_ in expected:
    assert route in home.links,route
research=page('/research/')
assert '/publications/' in research.links
for slug in ['2020-cas13-clinical-validation','2022-metagenomic-pet-hydrolase','2023-multiplexed-cas13-diagnostics','2024-pet-recycling-upcycling-review','2025-recombinase-condensates']:
    assert '/publications/'+slug+'/' in research.links
natural=page('/natural-history/')
assert 'https://www.inaturalist.org/people/austintw' in natural.links
assert all(link and '{{' not in link for link in natural.links)
art=page('/art-biodesign/')
assert [title for level,title in art.headings if level=='h2']==["Molecular Soundtrack: Designing Proteins with IU's Song Titles",'Collaborations','Visual design'],art.headings
assert [title for level,title in art.headings if level=='h3']==['Intimacy with Nature','Happy Ending','Phantom Dining']
cv=page('/cv/')
assert '/teaching/' in cv.links and '/natural-history/' in cv.links and '/publications/' in cv.links
print('Navigation, parallel homepage teasers, research-publication links, art hierarchy, and CV cross-links passed.')
