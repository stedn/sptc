---
title: Updates and Interviews
layout: page
description: 'Find out the latest about Solarpunk Travel and interviews with other co-ops.'
image: assets/images/pacific_northwest/frontstreet0.jpg
nav-menu: true
hide_image: true
---
{% assign mytiles = site.posts %}

<!-- Main -->
<div id="main">

<section id="one">
    <div class="inner">

        <p>There's always something going on with Solarpunk Travel.  Check out our newsletter archives below with info on what we've been up to as well as our sustainable travel and co-op spotlight series.</p>
	</div>
</section>

<!-- Two -->
<section id="two" class="spotlights-small">
    {% for tile in mytiles %}
    <section>
        {% if tile.post_type == "event" %}
            <a href="{{ tile.link }}" class="image" style="max-height:300px;overflow:hidden;">
                <img src="{{ tile.image }}" alt="" data-position="center center" />
            </a>
            <div class="content">
                <div class="inner">
                    <header class="major">
                        <h3>Event: {{ tile.title }}</h3>
                    </header>
                    <p>{{ tile.description }}</p>
                    <ul class="actions">
                        <li><a href="{{ tile.link }}" class="button">Learn more</a></li>
                    </ul>
                </div>
            </div>
        {% else %}
            <a href="{{ tile.url  | relative_url }}" class="image" style="max-height:300px;overflow:hidden;">
                <img src="{{ tile.image }}" alt="" data-position="center center" />
            </a>
            <div class="content">
                <div class="inner">
                    <header class="major">
                        <h3>{{ tile.title }}</h3>
                    </header>
                    <p>{{ tile.description }}</p>
                    <ul class="actions">
                        <li><a href="{{ tile.url  | relative_url }}" class="button">Learn more</a></li>
                    </ul>
                </div>
            </div>
        {% endif %}
    </section>
    {% endfor %}
</section>


</div>
