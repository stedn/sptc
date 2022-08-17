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
    <div class="inner" style="padding:0">
        <div class="iframeholder image right">
            <iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%234285F4&ctz=America%2FChicago&showPrint=0&showCalendars=0&showNav=1&showTitle=0&src=c29sYXJwdW5rdHJhdmVsQGdtYWlsLmNvbQ&color=%23039BE5" style="border:solid 1px #777" width="100%" height="400" frameborder="0" scrolling="no"></iframe>
        </div>
    </div>
</section>
<h2 style="text-align:center;padding-top:0.2em;">Upcoming Events</h2>

<section id="two" class="shrink"></section>

<section style="clear:both;padding-top:1em;">
    <p style="text-align:center;font-size: 20px;padding: 4px ;letter-spacing: 2px;color: #14171c;background: #e0f3db;font-weight:700;"> <i>Have an idea for an event we should spotlight? </i> <a href="#" onclick="document.getElementById('modform2').style.display='block'; return false;">Submit it here!</a></p>
</section>

<hr>

<section id="three" class="spotlights-small" style="clear:both;">
    <h3 style="text-align:center;">Past Events</h3>
</section>


<script>
today = new Date()
console.log(today)
format_today = today.getFullYear()*10000 + (today.getMonth()+1)*100 + today.getDate();
console.log(format_today)
fetch("https://docs.google.com/spreadsheets/d/1FH5pfClecsTA_4hLp5HJ7JOL2wkj6QO1GQ0oDPgBRjo/gviz/tq?tqx=out:json")
    .then(res => res.text())
    .then(text => {
        meta_result = JSON.parse(text.substr(47).slice(0, -2))
        console.log(meta_result)
        keys = []
        for (var i = 0; i < 5; i += 1){
          keys.push(meta_result.table.cols[i].label)
        }
        var data = {};
        for (var i = 0; i < meta_result.table.rows.length; i += 1) {
          to_push = {};
          for (var j = 0; j < 7; j += 1){
            if (meta_result.table.rows[i].c[j] != null){
                to_push[keys[j]]=meta_result.table.rows[i].c[j].v
            }
          }
          data[meta_result.table.rows[i].c[0].v] = to_push
        }
        for (var i in data){
          d = data[i]
          var newElement = document.createElement("section");
          to_add = `<div class="content" >
                        <div class="inner" >
                            <header>
                                <h3><a target="_blank" href="${d.link}">${d.name}</a></h3>
                            </header>
                            <p>${d.desc}</p>
                            <ul class="actions">
                                <li><a target="_blank" href="${d.link}" class="button">Learn more</a></li>
                            </ul>
                        </div>
                    </div>
                </section>`
          if (d.image) {
            to_add = `<a href="${d.link}" target="_blank" class="image" style="max-height:300px;overflow:hidden;">
                        <img src="${d.image}" alt="" data-position="center center" />
                    </a>` + to_add
          }else{
            to_add = `<a href="${d.link}" target="_blank" class="image" style="max-height:300px;overflow:hidden;">
                        <img src="assets/images/sptc.png" alt="" data-position="center center" />
                    </a>` + to_add
          }
          newElement.innerHTML = to_add
          console.log(d.date)
          if(d.date>format_today){ //TODO: make date test
            document.getElementById("two").appendChild(newElement);
          }else{
            document.getElementById("three").appendChild(newElement);
          }
    }
    })
</script>

</div>
