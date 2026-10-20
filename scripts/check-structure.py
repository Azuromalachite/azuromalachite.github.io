"""Check the site's navigation and content hierarchy after Jekyll renders it."""
from html.parser import HTMLParser
from pathlib import Path

class Structure(HTMLParser):
    def __init__(self):
        super().__init__();self.content=False;self.headings=[];self.links=[];self.heading=None;self.text='';self.nav=False;self.nav_links=[];self.anchor=None;self.anchor_text=''
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag in ['h1','h2','h3','h4','h5','h6'] and not hasattr(self,'first_heading'):self.first_heading=tag
        if 'author__name' in a.get('class','').split():assert tag=='p','Sidebar name must not be a heading'
        if 'href' in a:a['href']=a['href'].removeprefix('https://azuromalachite.github.io')
        if tag=='section' and 'page__content' in a.get('class','').split():self.content=True
        if tag=='nav' and a.get('id') in ['site-nav','navigation']:self.nav=True
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
assert home.first_heading=='h1'
assert '/publications/' in home.links
assert home.nav_links==expected[1:],home.nav_links
home_html=Path('_site/index.html').read_text(encoding='utf-8')
assert home_html.count('<h1 ')==1
assert home_html.count('class="practice-row"')==4
assert home_html.count('class="work"')==3
assert 'id="biography"' in home_html and 'James P. Collins, 13 February 2009' in home_html
assert 'class="author__avatar"' not in home_html
assert '/assets/css/home.css' in home_html and '/assets/css/main.css' not in home_html
assert 'unpublished' not in home_html.lower() and 'design study' not in home_html.lower()
for route,_ in expected[1:]:
    assert route in home.links,route
research=page('/research/')
assert research.nav_links==expected[1:],research.nav_links
research_html=Path('_site/research/index.html').read_text(encoding='utf-8')
assert research.first_heading=='h1' and research_html.count('<h1 ')==1
assert 'class="author__avatar"' not in research_html
assert '/assets/css/home.css' in research_html and '/assets/css/main.css' not in research_html
assert research_html.count('class="research-paper"')==5
assert 'aria-current="page">Research' in research_html
assert '/publications/' in research.links
for slug in ['2020-cas13-clinical-validation','2022-metagenomic-pet-hydrolase','2023-multiplexed-cas13-diagnostics','2024-pet-recycling-upcycling-review','2025-recombinase-condensates']:
    assert '/publications/'+slug+'/' in research.links
natural=page('/natural-history/')
assert natural.nav_links[1:]==expected,natural.nav_links
assert 'https://www.inaturalist.org/people/austintw' in natural.links
assert 'https://ebird.org/profile/OTA2MjI5' in natural.links
assert all(link and '{{' not in link for link in natural.links)
art=page('/art-biodesign/')
assert [level for level,_ in art.headings]==['h2','h2','h3','h3','h2'],art.headings
teaching=page('/teaching/')
assert [level for level,_ in teaching.headings]==['h2','h3','h3','h2','h3','h3','h3','h2','h3','h3'],teaching.headings
assert 'https://www.youtube.com/watch?v=CvI6IYfv-fk' in teaching.links
assert 'https://drive.google.com/file/d/1G-s3lcT-Z4YbKzUjtrIHVTP0XLCwgFcI/view' in teaching.links
assert home_html.count('r="33"')==4
assert 'Teaching &amp;' in home_html and 'not chronological' in home_html
assert 'POSN' in home_html and 'Team B' in home_html and 'olive-backed sunbird' in home_html
publications=page('/publications/')
assert publications.first_heading=='h1'
published=(Path('_site/publications/index.html')).read_text(encoding='utf-8')
assert published.count('<strong>Co-first author</strong>')==2
assert 'I contributed microscopy image processing and analysis.' in published
cv=page('/cv/')
assert '/teaching/' in cv.links and '/natural-history/' in cv.links and '/publications/' in cv.links
print('Navigation, parallel homepage teasers, research-publication links, art hierarchy, and CV cross-links passed.')
