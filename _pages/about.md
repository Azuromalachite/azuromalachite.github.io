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

<section class="hero" aria-labelledby="intro-title"><div><p class="eyebrow">Engineering biology / natural history / design</p><h1 id="intro-title">Tools for<br>microbial life.<br><span class="serif"><em>A wider biological<br>perspective.</em></span></h1><p class="intro">I develop experimental and computational tools for microbiome engineering at KAIST. Ecology, evolution, and the diversity of living systems shape how I approach that work.</p><div class="inline-links"><a href="{{ '/research/' | relative_url }}">Explore research ↗</a><a href="{{ '/publications/' | relative_url }}">Publications ↗</a></div>
<div class="hero-contact" role="group" aria-label="Contact and profiles"><a href="mailto:{{ site.author.email }}">Email</a><a href="{{ site.author.googlescholar | escape }}">Google Scholar ↗</a><a href="https://www.linkedin.com/in/{{ site.author.linkedin }}/">LinkedIn ↗</a><a href="https://bsky.app/profile/{{ site.author.bluesky }}">Bluesky ↗</a><a href="https://github.com/{{ site.author.github }}">GitHub ↗</a></div></div>
<aside class="practice-map" aria-label="A connected scientific practice"><div class="map-title meta"><span>A connected practice</span><span>Field / lab / studio</span></div>
<svg viewBox="0 0 440 310" role="img" aria-labelledby="diagram-title diagram-desc"><title id="diagram-title">Four practices, connected across scales</title><desc id="diagram-desc">Research, Natural History, Art and Biodesign, and Teaching and Community are four equal-sized nodes connected by two adjoining triangles and a curved outline. The lines represent conceptual connections and shared habits of observation, comparison, and contextual thinking. Node sizes carry no ranking; the arrangement is not chronological.</desc>
<g fill="none" stroke="#aab29d" stroke-width="1"><path class="practice-orbit" d="M78 70C176 32 289 54 315 110S409 190 365 255S236 292 170 235S39 172 78 70Z" stroke-opacity=".6"/><path class="practice-triangle" d="M78 70L315 110L170 235Z"/><path class="practice-triangle" d="M315 110L365 255L170 235"/><circle class="practice-node" cx="78" cy="70" r="32"/><circle class="practice-node" cx="315" cy="110" r="32"/><circle class="practice-node" cx="170" cy="235" r="32"/><circle class="practice-node" cx="365" cy="255" r="32"/></g>
<g fill="#36583f"><circle cx="78" cy="70" r="4"/><circle cx="315" cy="110" r="4"/><circle cx="170" cy="235" r="4"/><circle cx="365" cy="255" r="4"/></g><g font-size="12"><text x="14" y="18">Research</text><text x="262" y="50">Natural History</text><text x="118" y="299">Art &amp; Biodesign</text><text x="426" y="195" text-anchor="end">Teaching &amp;</text><text x="426" y="212" text-anchor="end">Community</text></g><g font-size="10"><text x="12" y="166">Observation</text><text x="12" y="184">Comparison</text><text x="12" y="202">Context</text></g></svg>
<p class="diagram-caption">Different scales, shared habits: observing variation, finding relationships, and building ways to ask better questions.</p><div class="location"><span>PhD · Engineering Biology<br>KAIST, South Korea</span><span>Originally from Thailand<br>Based in Daejeon</span></div></aside></section>
<section class="perspective-section" aria-labelledby="perspective-title"><h2 id="perspective-title">Why context matters</h2><div>
<figure class="perspective-quote"><blockquote><p>“We are the first generation of scientists with the tools to address the dimensions of biodiversity on Earth…and ironically we may be the last generation with the opportunity to discover and understand Earth’s biodiversity before it is irrevocably changed or lost.”</p></blockquote>
<figcaption><em>— James P. Collins, 13 February 2009, as recorded in the <a href="https://www.nationalacademies.org/read/13109/chapter/3">National Research Council symposium report</a>, p. 11 (2011).</em></figcaption></figure>
<p class="perspective-response">The tension between increasingly powerful molecular tools and the urgency of understanding living diversity in context shapes how I think about biology.</p>
</div></section>
<section class="practice-list" aria-labelledby="practice-title"><div class="section-heading"><span class="section-index">Fields of practice</span><h2 id="practice-title">In the lab. In the field. In between.</h2></div>
<a class="practice-row" href="{{ '/research/' | relative_url }}"><span class="number">01</span><h3>Research<span class="tag">Cultivation + sequencing + computation</span></h3><p>Tools and methods for microbiome engineering, informed by biological variation and context.</p><span class="arrow" aria-hidden="true">↗</span></a>
<a class="practice-row" href="{{ '/natural-history/' | relative_url }}"><span class="number">02</span><h3>Natural History<span class="tag">Organisms + environments</span></h3><p>Southeast Asian blue-banded bees, taxonomic questions, and a practice of looking closely.</p><span class="arrow" aria-hidden="true">↗</span></a>
<a class="practice-row" href="{{ '/art-biodesign/' | relative_url }}"><span class="number">03</span><h3>Art &amp; Biodesign<span class="tag">Molecular + cultural</span></h3><p>Predicted molecular forms, art–science collaborations, and visual systems grounded in biology.</p><span class="arrow" aria-hidden="true">↗</span></a>
<a class="practice-row" href="{{ '/teaching/' | relative_url }}"><span class="number">04</span><h3>Teaching &amp; Community<span class="tag">Knowledge + participation</span></h3><p>Lectures, workshops, HTGAA, and recurring spaces for scientific exchange and community-building.</p><span class="arrow" aria-hidden="true">↗</span></a></section>
<section class="work-section" aria-labelledby="work-title"><div class="section-heading"><span class="section-index">Selected published work</span><h2 id="work-title">From biological diversity to useful tools.</h2></div><div class="work-list">
{% assign selected = site.publications | where: 'selected_home', true | sort: 'year' | reverse %}
{% for paper in selected %}
<article class="work"><span class="year">{{ paper.year }}</span><div>
<h3><a href="{{ paper.url | relative_url }}">{{ paper.homepage_title | default: paper.title | escape }} <span aria-hidden="true">↗</span></a></h3>
<div class="meta">{{ paper.venue | escape }} · {% if paper.co_first_author %}Co-first author{% elsif paper.first_author %}First-author {{ paper.publication_type | downcase | escape }}{% else %}{{ paper.publication_type | escape }}{% endif %}</div>
{% if paper.contribution_summary %}<p>{{ paper.contribution_summary | escape }}</p>{% elsif paper.publication_summary %}<p>{{ paper.publication_summary | escape }}</p>{% endif %}
</div></article>
{% endfor %}
<p class="work-tail"><a href="{{ '/publications/' | relative_url }}">Complete publication list &amp; bibliography ↗</a></p></div></section>
<section class="about-strip" aria-labelledby="about-title"><h2 id="about-title">A little background</h2><div><p>My scientific interests began with fishkeeping, birdwatching, and amateur astronomy, and later broadened through formal training in biology and Earth science. A high-school molecular docking workshop then introduced me to proteins as nanoscale objects I could visualize and explore computationally.</p><p class="small">I studied Bio and Brain Engineering at KAIST and worked at VISTEC on CRISPR diagnostics, plastic-degrading enzymes, and microscopy analysis. Today, I work with Professor Sung Sun Yim in KAIST’s Graduate School of Engineering Biology.</p><details class="full-biography" id="biography"><summary>Read the full biography</summary><div class="biography-content">
{% capture biography %}{% include home-biography.md %}{% endcapture %}{{ biography | markdownify }}
</div></details></div></section>
