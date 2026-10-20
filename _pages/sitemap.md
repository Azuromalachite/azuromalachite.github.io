---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
noindex: true
sitemap: false
description: "Browse the main pages and publications on Thanakrit (Austin) Wongsatit's personal website."
---

{% include base_path %}

A guide to the main pages and publications on this website. An [XML sitemap]({{ '/sitemap.xml' | relative_url }}) is available for search engines.

<h2>Pages</h2>
<ul>
{% for item in site.data.navigation.main %}
  <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
{% endfor %}
  <li><a href="{{ '/publications/' | relative_url }}">Publications</a></li>
</ul>

<h2>Publications</h2>
<ul>
{% assign publications = site.publications | sort: 'year' | reverse %}
{% for paper in publications %}
  <li>{{ paper.year }} · <a href="{{ paper.url | relative_url }}">{{ paper.title }}</a></li>
{% endfor %}
</ul>
