---
layout: archive
title: "Media"
permalink: /media/
author_profile: true
---

{% assign vids = site.media | sort: 'order' %}
<div class="vid-grid">
  {% for m in vids %}{% include media-card.html m=m %}{% endfor %}
</div>