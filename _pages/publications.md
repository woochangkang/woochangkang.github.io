---
layout: archive
title: "Publications"
permalink: /publications/
redirect_from:
  - /research/
author_profile: true
---

{% assign en = site.publications | where: "category", "english" | sort: "date" | reverse %}
{% assign ko = site.publications | where: "category", "korean" | sort: "date" | reverse %}

<div class="pub-metrics" id="pubTabs" role="tablist">
  <button class="metric is-active" data-tab="english"><span class="metric__n">{{ en | size }}</span><span class="metric__l">English articles</span></button>
  <button class="metric" data-tab="korean"><span class="metric__n">{{ ko | size }}</span><span class="metric__l">Korean articles</span></button>
  <button class="metric" data-tab="wip"><span class="metric__n">9</span><span class="metric__l">Works in progress</span></button>
  <button class="metric" data-tab="grants"><span class="metric__n">6</span><span class="metric__l">Grants</span></button>
</div>

<div class="filter-chips" id="topicFilter">
  <span class="filter-chips__label">Filter</span>
  <button class="chip is-active" data-topic="all">All</button>
  <button class="chip" data-topic="AI">AI</button>
  <button class="chip" data-topic="Elections">Elections</button>
  <button class="chip" data-topic="Voting">Voting</button>
  <button class="chip" data-topic="Public Opinion">Public Opinion</button>
  <button class="chip" data-topic="Polarization">Polarization</button>
  <button class="chip" data-topic="Gender">Gender</button>
  <button class="chip" data-topic="Inequality">Inequality</button>
  <button class="chip" data-topic="Real Estate Price">Real Estate Price</button>
  <button class="chip" data-topic="Immigration">Immigration</button>
  <button class="chip" data-topic="Weather">Weather</button>
  <button class="chip" data-topic="Face">Face</button>
  <button class="chip" data-topic="Legacies">Legacies</button>
  <button class="chip" data-topic="South Korea">South Korea</button>
  <button class="chip" data-topic="US">US</button>
  <button class="chip" data-topic="Australia">Australia</button>
  <button class="chip" data-topic="North Korea">North Korea</button>
  <button class="chip" data-topic="Cross-national Studies">Cross-national Studies</button>
</div>

<section class="pub-tab" data-tab="english">
<ol class="pub-list">
{% for p in en %}{% include publication-item.html p=p %}{% endfor %}
</ol>
</section>

<section class="pub-tab" data-tab="korean" hidden>
<ol class="pub-list">
{% for p in ko %}{% include publication-item.html p=p %}{% endfor %}
</ol>
</section>

<section class="pub-tab" data-tab="wip" hidden>
<ul class="plain-list">
  <li>Kang, Woo Chang and Sein Park. "Housing Prices, Rental Prices, and Perceptions about the Economy: Evidence from South Korea"</li>
  <li>Kang, Woo Chang. "Politics of Face: Gender Typicality, Perceived Competence and Electoral Viability"
    <details class="pub__abs"><summary>Show abstract</summary><p>Voters form rapid impressions from candidate faces, and these impressions carry electoral consequences. This study examines whether gender typicality&mdash;the degree to which a face displays features prototypical of one's biological sex&mdash;affects competence evaluations and electoral outcomes in South Korea. Drawing on two surveys of higher-level elections (5,576 candidates) and lower-level local council elections (2,602 candidates) linked to official election returns, I find that gender typicality enhances women's perceived competence in both studies, contradicting the linear masculine premium of Sex Role Theory. In high-information elections, the femininity&ndash;competence relationship is curvilinear (extreme femininity penalized) for female candidates evaluated by male respondents; in low-information elections it is monotonically positive. Yet only in low-information elections does gender typicality shape actual vote share, where an inverted-U pattern survives party controls. The effect does not vary by candidate ideology, favoring Gender Typicality Theory over Role Congruity Theory among the theories predicting a curvilinear relationship. The information environment is a boundary condition for the electoral relevance of facial gender typicality.</p></details>
  </li>
  <li>Kang, Woo Chang, Sunkyoung Park, Osbern Huang, Koh Iwabuchi and Tetsuro Kobayashi. "Democratic Accountability in East Asia: A Comparative Experimental Study of Voter Responses to Norm Violations"
    <details class="pub__abs"><summary>Show abstract</summary><p>Existing research shows that voters in established democracies often fail to penalize politicians who violate democratic norms, as many are willing to trade democratic principles for partisan interests in polarized environments. Yet such partisan double standards remain underexplored in East Asia, where countries share authoritarian legacies, face ongoing risks of democratic backsliding, and operate under the geopolitical shadow of powerful authoritarian neighbors. Using a large-scale vignette experiment conducted in Japan, South Korea, Taiwan, and the United States (N = 10,211), this study examines whether voters sanction politicians who engage in democratic norm violations. We focus on reactions to three types of undemocratic statements: election denial, protest suppression, and attacks on the judiciary. The results show that voters in East Asian democracies impose stronger penalties than their American counterparts, though the degree and pattern of accountability differ across cases. Election denial consistently generates the strongest sanctions, while Japan and Taiwan show robust reactions across all scenarios. South Korea displays comparatively modest responses to protest suppression, and the United States shows the weakest effects overall. These findings highlight both the resilience and the heterogeneity of democratic accountability in East Asia and underscore the need to understand regional variation when assessing the prospects for democratic stability.</p></details>
  </li>
  <li>Kang, Woo Chang, June Kang, Kyu-Man Han. "Depressive Symptoms Around the 2025 South Korean Presidential Election: The Roles of Voting, Electoral Outcomes, and Manipulation Beliefs"</li>
  <li>Kang, Woo Chang and Hannah Kim. "Correcting Political Misperceptions to Rebuild Norms of Good Citizenship in Polarized Democracies: Evidence from South Korea"</li>
  <li>Kang, Woo Chang and Hong-gie Kim. "Online Media Fragmentation and Political Polarization: A Cross-National Analysis of 51 Countries"</li>
  <li>Kang, Woo Chang. "Unraveling Gender Bias in Candidate Evaluations through the analysis of Representativeness, Competence, and Electability"</li>
  <li>Kang, Woo Chang and Han Il Chang. "How Does International Naming and Shaming Affect South Korean Attitudes Toward Refugees?"</li>
  <li>Kang, Woo Chang and Chris Dawes. "Electoral Effect of Stop and Frisk"</li>
</ul>
</section>

<section class="pub-tab" data-tab="grants" hidden>
<ul class="plain-list">
  <li>SSK 글로벌아젠다연구. 책임연구원. "다양성, 공존, 통합을 위한 이민정치연구." 한국연구재단. 2024-2025</li>
  <li>신진연구자 지원사업. 책임연구원. "인공지능을 활용한 선거 후보자 이미지 연구." 한국연구재단. 2023-2025</li>
  <li>일반공동연구. 공동연구원. "젠더갈등 해소를 위한 통합의 정치: 선호, 과정, 제도 연구." 한국연구재단. 2023-2026</li>
  <li>신진연구자 지원사업. 책임연구원. "지리정보시스템을 활용한 선거당일 날씨 효과 연구." 한국연구재단, 2020-2022</li>
  <li>일반공동연구. 공동연구원. "딥페이크 시대의 유권자: 빅데이터와 실험을 통한 가짜뉴스 효과연구." 한국연구재단, 2020-2023</li>
  <li>Laboratory Program for Korean Studies. Academy of Korean Studies, 2018</li>
</ul>
</section>

<script src="{{ '/assets/js/pubfilter.js' | relative_url }}"></script>
