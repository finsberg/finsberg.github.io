---
layout: archive
title: "Software"
permalink: /software/
author_profile: true
---

{% include base_path %}

You can also check out <u><a href="https://www.github.com/{{ site.author.github }}">my GitHub profile</a>.</u>


{% for post in site.softwares reversed %}
  {% include archive-single.html %}
{% endfor %}
