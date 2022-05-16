---
title: Trips and Events
layout: page
description: 'Find a cycle tour, backpacking trip, or solarpunk social near you'
image: assets/images/fun_us_small.jpg
nav-menu: true
hide_image: true
---

{% assign mytiles = site.posts | where_exp: "item", "item.post_type == 'event'" %}

<!-- Main -->
<div id="main">

<section id="one">
    <div class="inner">
        <div class="iframeholder">
            <iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%234285F4&ctz=America%2FChicago&showPrint=0&showCalendars=0&showNav=1&showTitle=0&src=c29sYXJwdW5rdHJhdmVsQGdtYWlsLmNvbQ&color=%23039BE5" style="border:solid 1px #777" width="100%" height="600" frameborder="0" scrolling="no"></iframe>
        </div>
    </div>
</section>


<section id="two" class="spotlights">
    <h2 style="margin-top:5%;text-align:center;">Upcoming Events</h2>
    {% for tile in mytiles %}
    <section class="myevents" data-datefilter={{ tile.datefilter }}>
        <a href="{{ tile.link }}" target="_blank" class="image" style="max-height:300px;overflow:hidden;">
            <img src="{{ tile.image }}" alt="" data-position="center center" />
        </a>
        <div class="content">
            <div class="inner">
                <header class="major">
                    <h3>{{ tile.title }}</h3>
                </header>
                <p>{{ tile.description }}</p>
                <ul class="actions">
                    <li><a target="_blank" href="{{ tile.link }}" class="button">Learn more</a></li>
                </ul>
            </div>
        </div>
    </section>
    {% endfor %}
</section>

<section id="three" class="spotlights">
    <h2 style="margin-top:5%;text-align:center;">Past Events</h2>
    {% for tile in mytiles reversed %}
    <section class="mypastevents" data-datefilter={{ tile.datefilter }}>
        <a href="{{ tile.link }}" target="_blank" class="image" style="max-height:300px;overflow:hidden;">
            <img src="{{ tile.image }}" alt="" data-position="center center" />
        </a>
        <div class="content">
            <div class="inner">
                <header class="major">
                    <h3>{{ tile.title }}</h3>
                </header>
                <p>{{ tile.description }}</p>
                <ul class="actions">
                    <li><a target="_blank" href="{{ tile.link }}" class="button">Learn more</a></li>
                </ul>
            </div>
        </div>
    </section>
    {% endfor %}
</section>

<script>
today = new Date()
console.log(today)
format_today = today.getFullYear()*10000 + (today.getMonth()+1)*100 + today.getDate();
console.log(format_today)
tst = document.getElementsByClassName("myevents")
for (let i = 0; i < tst.length; i++){
    console.log(tst[i].dataset.datefilter)
    if (tst[i].dataset.datefilter<format_today){
        tst[i].style.display = "none"
    }
}

tst = document.getElementsByClassName("mypastevents")
for (let i = 0; i < tst.length; i++){
    console.log(tst[i].dataset.datefilter)
    if (tst[i].dataset.datefilter>format_today){
        tst[i].style.display = "none"
    }
}
</script>

</div>
