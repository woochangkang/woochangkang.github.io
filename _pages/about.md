---
permalink: /
title: ""
layout: single
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

<div class="home-hero">
  <img class="home-hero__avatar" src="{{ '/images/profile.png' | relative_url }}" alt="Woo Chang Kang">
  <div class="home-hero__body">
    <h1 class="home-hero__name">Woo Chang Kang</h1>
    <p class="home-hero__role">Associate Professor of Political Science</p>
    <p class="home-hero__affil">Korea University · Seoul</p>
    <p class="home-hero__statement">I study how voters and political elites interact in representative democracies — with a focus on inequalities among social groups by partisanship, gender, age, and migration status.</p>
    <div class="home-hero__links">
      <a href="mailto:{{ site.author.email }}">Email</a>
      <a href="{{ site.author.googlescholar }}" target="_blank" rel="noopener">Google Scholar</a>
      <a href="{{ '/cv/' | relative_url }}">CV</a>
      <a href="https://instagram.com/{{ site.author.instagram }}" target="_blank" rel="noopener">Instagram</a>
    </div>
  </div>
</div>

<section class="home-section">
  <h2 class="home-section__label">Research interests</h2>
  <div class="tag-row">
    <span class="tag">Representation &amp; Polarization</span>
    <span class="tag">Gender &amp; Intergroup Politics</span>
    <span class="tag">Immigration</span>
    <span class="tag">Economic Inequality</span>
    <span class="tag">Politics of Face</span>
  </div>
</section>

<section class="home-section">
  <div class="home-section__head">
    <h2 class="home-section__label">Selected publications</h2>
    <a class="home-section__more" href="{{ '/publications/' | relative_url }}">View all &rarr;</a>
  </div>
  <div class="pub-cards">
  {% assign published = site.publications | where_exp: "p", "p.category != 'wip'" %}
  {% assign recent = published | sort: "date" | reverse %}
  {% for p in recent limit: 5 %}<div class="pub-card">
    <div class="pub-card__title">{{ p.title }}</div>
    <div class="pub-card__meta">{{ p.authors }} &middot; <em>{{ p.venue }}</em>{% if p.detail and p.detail != "" %}, {{ p.detail }}{% endif %} ({{ p.year }}){% if p.doi %} &middot; <a href="https://doi.org/{{ p.doi }}" target="_blank" rel="noopener">DOI</a>{% elsif p.link %} &middot; <a href="{{ p.link }}" target="_blank" rel="noopener">Link</a>{% endif %}</div>
  </div>
  {% endfor %}</div>
</section>

<section class="home-section">
  <h2 class="home-section__label">About</h2>
  <p>I am an associate professor in the Department of Politics and International Relations at Korea University. I received my Ph.D. from New York University in 2015. Before joining Korea University in 2019, I worked as a postdoc at Yale University and a lecturer at the Australian National University. My research explores the interactions between voters and political elites during political processes within representative democracy, aiming to identify ways to mitigate inequalities and enhance representation.</p>
</section>

<section class="home-section">
  <h2 class="home-section__label">Education</h2>
  <ul>
    <li>Ph.D. in Politics, New York University</li>
    <li>M.A. in Politics, Korea University</li>
    <li>B.A. in English Literature, Korea University</li>
  </ul>
</section>
