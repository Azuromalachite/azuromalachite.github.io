"""Focused regression checks for the rendered navigation/footer styles and menu label.

This is not a complete accessibility audit; browser checks remain necessary.
"""
from pathlib import Path
import re

css=Path('_site/assets/css/main.css').read_text(encoding='utf-8')
def declarations(selector):
    result={}
    for selectors,body in re.findall(r'([^{}]+)\{([^{}]*)\}',css):
        if selector in [s.strip() for s in selectors.split(',')]:
            for property,value in re.findall(r'([\w-]+)\s*:\s*([^;]+)',body):result[property]=value.strip()
    return result

def luminance(color):
    assert re.fullmatch(r'#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?',color),color
    value=color[1:]
    if len(value)==3:value=''.join(c*2 for c in value)
    rgb=[int(value[i:i+2],16)/255 for i in (0,2,4)]
    channels=[v/12.92 if v<=0.04045 else ((v+0.055)/1.055)**2.4 for v in rgb]
    return sum(a*b for a,b in zip(channels,[0.2126,0.7152,0.0722]))

def contrast(foreground,background):
    values=sorted([luminance(foreground),luminance(background)])
    return (values[1]+0.05)/(values[0]+0.05)

nav=declarations('.greedy-nav a');container=declarations('.greedy-nav')
footer=declarations('.page__footer')
nav_ratio=contrast(nav['color'],container['background'])
footer_ratio=contrast(footer['color'],footer['background-color'])
assert nav_ratio>=4.5,nav_ratio
assert footer_ratio>=4.5,footer_ratio
assert float(declarations('.page__title')['line-height'])>=1.15
inner=Path('_site/natural-history/index.html').read_text(encoding='utf-8')
assert 'aria-label="Toggle navigation menu"' in inner
assert '.greedy-nav button:focus-visible' in css
home=Path('_site/index.html').read_text(encoding='utf-8')
assert 'aria-controls="navigation"' in home and 'aria-expanded="false"' in home
research=Path('_site/research/index.html').read_text(encoding='utf-8')
assert 'aria-controls="navigation"' in research and 'aria-expanded="false"' in research
home_css=Path('_site/assets/css/home.css').read_text(encoding='utf-8')
tokens=dict(re.findall(r'--([\w-]+):\s*(#[0-9a-fA-F]{6})',home_css))
for name in ['ink','muted','green']:
    assert contrast(tokens[name],tokens['paper'])>=4.5,name
assert contrast(tokens['muted'],tokens['wash'])>=4.5
assert ':focus-visible' in home_css and 'prefers-reduced-motion' in home_css
assert 'Escape' in Path('_site/assets/js/home.js').read_text(encoding='utf-8')
print(f'Navigation contrast {nav_ratio:.2f}:1; footer contrast {footer_ratio:.2f}:1; heading spacing and menu label passed.')
