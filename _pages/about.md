---
description: "Thanakrit (Austin) Wongsatit is a PhD student at KAIST developing tools for microbiome engineering, with interests in ecology, evolution, natural history, and biodesign."
seo_title: "Thanakrit (Austin) Wongsatit — Microbiome Engineering at KAIST"
permalink: /
title: "Thanakrit (Austin) Wongsatit"
layout: home-editorial
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

<section class="hero" aria-labelledby="intro-title"><div><p class="eyebrow">Engineering biology / natural history / design</p><h1 id="intro-title">Tools for<br>microbial life.<br><span class="serif"><em>A wider biological<br>perspective.</em></span></h1><p class="intro">I develop experimental and computational tools for microbiome engineering at KAIST. Ecology, evolution, and the diversity of living systems shape how I approach that work.</p><div class="inline-links"><a href="{{ '/research/' | relative_url }}">Explore research ↗</a><a href="{{ '/publications/' | relative_url }}">Publications ↗</a></div></div>
<aside class="practice-map" aria-label="A connected scientific practice"><div class="map-title meta"><span>A connected practice</span><span>Field / lab / studio</span></div>
<svg viewBox="0 0 440 310" role="img" aria-labelledby="diagram-title diagram-desc"><title id="diagram-title">Connections across a scientific practice</title><desc id="diagram-desc">A conceptual diagram connecting molecular tools, microbial communities, natural history, and creative practice. It represents interests rather than measured biological relationships.</desc><g fill="none" stroke="#aab29d" stroke-width="1"><path d="M78 68C190 68 238 78 315 113S270 215 170 236S57 189 78 68Z"/><path d="M78 68L170 236L315 113M78 68L315 113"/><circle cx="78" cy="68" r="34"/><circle cx="315" cy="113" r="58"/><circle cx="170" cy="236" r="44"/></g><g fill="#36583f"><circle cx="78" cy="68" r="4"/><circle cx="315" cy="113" r="5"/><circle cx="170" cy="236" r="4"/></g><g font-size="12"><text x="13" y="17">Molecular tools</text><text x="257" y="31">Microbial communities</text><text x="242" y="251">Natural history</text></g><g font-size="10" fill="#586158"><text x="10" y="131">Protein mining</text><text x="10" y="147">Computation</text><text x="275" y="187">Cultivation / sequencing</text><text x="10" y="236">Observation</text><text x="10" y="252">Classification</text></g><path d="M324 283H407" stroke="#36583f"/><text x="324" y="304" font-size="11">Art &amp; design</text></svg>
<p class="diagram-caption">Different scales, shared habits: observing variation, finding relationships, and building ways to ask better questions.</p><div class="location"><span>PhD · Engineering Biology<br>KAIST, South Korea</span><span>Originally from Thailand<br>Based in Daejeon</span></div></aside></section>
<section class="practice-list" aria-labelledby="practice-title"><div class="section-heading"><span class="section-index">Fields of practice</span><h2 id="practice-title">In the lab. In the field. In between.</h2></div>
<a class="practice-row" href="{{ '/research/' | relative_url }}"><span class="number">01</span><h3>Research<span class="tag">Experimental + computational</span></h3><p>Tools and methods for microbiome engineering, informed by biological variation and context.</p><span class="arrow" aria-hidden="true">↗</span></a>
<a class="practice-row" href="{{ '/natural-history/' | relative_url }}"><span class="number">02</span><h3>Natural History<span class="tag">Organisms + environments</span></h3><p>Southeast Asian blue-banded bees, taxonomic questions, and a practice of looking closely.</p><span class="arrow" aria-hidden="true">↗</span></a>
<a class="practice-row" href="{{ '/art-biodesign/' | relative_url }}"><span class="number">03</span><h3>Art &amp; Biodesign<span class="tag">Molecular + cultural</span></h3><p>Predicted molecular forms, collaborative experiments, and visual systems grounded in biology.</p><span class="arrow" aria-hidden="true">↗</span></a>
<a class="practice-row" href="{{ '/teaching/' | relative_url }}"><span class="number">04</span><h3>Teaching &amp; Community<span class="tag">Knowledge + participation</span></h3><p>Workshops, HTGAA, and recurring spaces for scientific exchange across institutions.</p><span class="arrow" aria-hidden="true">↗</span></a></section>
<section class="work-section" aria-labelledby="work-title"><div class="section-heading"><span class="section-index">Selected research</span><h2 id="work-title">From biological diversity to useful tools.</h2></div><div class="work-list">
{% assign selected = site.publications | where: 'selected_home', true | sort: 'year' | reverse %}
{% for paper in selected %}
<article class="work"><span class="year">{{ paper.year }}</span><div>
<h3><a href="{{ paper.url | relative_url }}">{{ paper.homepage_title | default: paper.title | escape }} <span aria-hidden="true">↗</span></a></h3>
<div class="meta">{{ paper.venue | escape }} · {% if paper.co_first_author %}Co-first author{% elsif paper.publication_type == 'Review' %}First-author review{% else %}{{ paper.publication_type | escape }}{% endif %}</div>
{% if paper.contribution_summary %}<p>{{ paper.contribution_summary | escape }}</p>{% elsif paper.publication_summary %}<p>{{ paper.publication_summary | escape }}</p>{% endif %}
</div></article>
{% endfor %}
<p class="work-tail"><a href="{{ '/publications/' | relative_url }}">Complete publication list &amp; bibliography ↗</a></p></div></section>
<section class="about-strip" aria-labelledby="about-title"><h2 id="about-title">A little background</h2><div><p>Originally from Thailand, I came to molecular biology through a high-school docking workshop—and the realization that proteins could be visualized and explored.</p><p class="small">I studied Bio and Brain Engineering at KAIST and worked at VISTEC on CRISPR diagnostics, plastic-degrading enzymes, and microscopy analysis. Today, I work with Professor Sung Sun Yim in KAIST’s Graduate School of Engineering Biology.</p><details class="full-biography" id="biography"><summary>Read the full biography</summary><div class="biography-content">
{% capture biography %}{% include home-biography.md %}{% endcapture %}{{ biography | markdownify }}
</div></details></div></section>
