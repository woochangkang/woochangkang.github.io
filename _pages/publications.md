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

## Peer-reviewed Articles (in English)
{% assign en_n = en | size %}
<ol>
{% for p in en %}<li value="{{ en_n | minus: forloop.index0 }}">{{ p.content }}</li>
{% endfor %}</ol>

## Peer-reviewed Articles (in Korean)
{% assign ko_n = ko | size %}
<ol>
{% for p in ko %}<li value="{{ ko_n | minus: forloop.index0 }}">{{ p.content }}</li>
{% endfor %}</ol>

## Works in Progress
<ul>
  <li>Kang, Woo Chang and Sein Park. "Housing Prices, Rental Prices, and Perceptions about the Economy: Evidence from South Korea"</li>
  <li>Kang, Woo Chang. "Politics of Face: Gender Typicality, Perceived Competence and Electoral Viability"</li>
  <li>Kang, Woo Chang, Osbern Huang, Koh Iwabuchi, Tetusro Kobayashi and Sunkyng Park. "Democratic Accountability in East Asia: A Comparative Experimental Study of Voter Responses to Norm Violations"</li>
  <li>Kang, Woo Chang, June Kang, Kyu-Man Han. "Depressive Symptoms Around the 2025 South Korean Presidential Election: The Roles of Voting, Electoral Outcomes, and Manipulation Beliefs"</li>
  <li>Kang, Woo Chang and Hannah Kim. "Correcting Political Misperceptions to Rebuild Norms of Good Citizenship in Polarized Democracies: Evidence from South Korea"</li>
  <li>Kang, Woo Chang and Hong-gie Kim. "Online Media Fragmentation and Political Polarization: A Cross-National Analysis of 51 Countries"</li>
  <li>Kang, Woo Chang. "Unraveling Gender Bias in Candidate Evaluations through the analysis of Representativeness, Competence, and Electability"</li>
  <li>Kang, Woo Chang and Han Il Chang. "How Does International Naming and Shaming Affect South Korean Attitudes Toward Refugees?"</li>
  <li>Kang, Woo Chang and Chris Dawes. "Electoral Effect of Stop and Frisk"</li>
</ul>

## Grants
<ul>
  <li>SSK 글로벌아젠다연구. 책임연구원. "다양성, 공존, 통합을 위한 이민정치연구." 한국연구재단. 2024-2025</li>
  <li>신진연구자 지원사업. 책임연구원. "인공지능을 활용한 선거 후보자 이미지 연구." 한국연구재단. 2023-2025</li>
  <li>일반공동연구. 공동연구원. "젠더갈등 해소를 위한 통합의 정치: 선호, 과정, 제도 연구." 한국연구재단. 2023-2026</li>
  <li>신진연구자 지원사업. 책임연구원. "지리정보시스템을 활용한 선거당일 날씨 효과 연구." 한국연구재단, 2020-2022</li>
  <li>일반공동연구. 공동연구원. "딥페이크 시대의 유권자: 빅데이터와 실험을 통한 가짜뉴스 효과연구." 한국연구재단, 2020-2023</li>
  <li>Laboratory Program for Korean Studies. Academy of Korean Studies, 2018</li>
</ul>
