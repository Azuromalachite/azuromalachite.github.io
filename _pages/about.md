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
<svg viewBox="0 0 440 310" role="img" aria-labelledby="diagram-title diagram-desc"><title id="diagram-title">Four practices connected by shared ways of working</title><desc id="diagram-desc">Research, Natural History, Art and Biodesign, and Teaching and Community are represented by equal-sized circles. Lines connect each practice to shared habits of observation, comparison, and contextual thinking. Circle size does not encode importance, and the arrangement is not chronological.</desc>
<g fill="none" stroke="#aab29d" stroke-width="1"><path d="M86 73L220 155L354 73M86 237L220 155L354 237"/><circle cx="86" cy="73" r="33"/><circle cx="354" cy="73" r="33"/><circle cx="86" cy="237" r="33"/><circle cx="354" cy="237" r="33"/></g>
<g fill="#36583f"><circle cx="86" cy="73" r="4"/><circle cx="354" cy="73" r="4"/><circle cx="86" cy="237" r="4"/><circle cx="354" cy="237" r="4"/></g><rect x="141" y="124" width="158" height="63" fill="#f5f4ef"/><g font-size="12" text-anchor="middle"><text x="86" y="20">Research</text><text x="354" y="20">Natural History</text><text x="86" y="293">Art &amp; Biodesign</text><text x="354" y="286">Teaching &amp;</text><text x="354" y="303">Community</text><text x="220" y="143">Observation</text><text x="220" y="162">Comparison</text><text x="220" y="181">Context</text></g></svg>
<p class="diagram-caption">Four practices, shared habits. Lines connect each field to observation, comparison, and contextual thinking; equal circles carry no ranking or chronological order.</p><div class="location"><span>PhD · Engineering Biology<br>KAIST, South Korea</span><span>Originally from Thailand<br>Based in Daejeon</span></div></aside></section>
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
<div class="meta">{{ paper.venue | escape }} · {% if paper.co_first_author %}Co-first author{% elsif paper.first_author %}First-author {{ paper.publication_type | downcase | escape }}{% else %}{{ paper.publication_type | escape }}{% endif %}</div>
{% if paper.contribution_summary %}<p>{{ paper.contribution_summary | escape }}</p>{% elsif paper.publication_summary %}<p>{{ paper.publication_summary | escape }}</p>{% endif %}
</div></article>
{% endfor %}
<p class="work-tail"><a href="{{ '/publications/' | relative_url }}">Complete publication list &amp; bibliography ↗</a></p></div></section>
<section class="about-strip" aria-labelledby="about-title"><h2 id="about-title">A little background</h2><div><p>Before molecular biology, my scientific interests grew through natural history, astronomy, biology, and Earth science. A high-school docking workshop then introduced me to proteins as nanoscale objects I could visualize and explore computationally.</p><p class="small">I studied Bio and Brain Engineering at KAIST and worked at VISTEC on CRISPR diagnostics, plastic-degrading enzymes, and microscopy analysis. Today, I work with Professor Sung Sun Yim in KAIST’s Graduate School of Engineering Biology.</p><details class="full-biography" id="biography"><summary>Read the full biography</summary><div class="biography-content">
{% capture biography %}{% include home-biography.md %}{% endcapture %}{{ biography | markdownify }}
</div></details></div></section>
