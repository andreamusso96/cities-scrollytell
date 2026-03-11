# Are we all going to live in giant cities?

[Overall comments: Avoid to refer to the "literature" that is an academic idea. There is no literature in the real world. Just facts. State the facts (I can the put a reference to that in a later version of this piece. Don't state them at the first person. State them as facts (So we distinguish them from what I did), but please don't say the damn literature. OR bettencourt. Or whatever academics say.  Makes me vomit. ]

## 1. Hook: the stakes

This question pressures me.

The bigger a city gets, the more it **amplifies** everything about us.

That is not just a metaphor. Across urban scaling research, economic outputs routinely rise faster than population. In U.S. metro data, GDP scales at about **1.11** and patenting at about **1.26** with population. In plain English: double a city's population and you do not just get twice the output. You get a bit more than twice the GDP, and something closer to two-and-a-half times the patents.

[STAT: add 1-2 more concrete scaling examples here, e.g. papers, wages, or invention per capita]

[VIZ width=medium: one animated scaling explainer showing doubling population -> GDP vs patents]

[Add something from balland and al. saying something like and when you look at the most innovative industries this is even more pronounced. Like most of tech is here most of pharma is there. The top industries are just in the big cities. ]

The same logic raises the stakes on the downside. Large cities are also where emissions, congestion, disease exposure, and housing pressure can pile up fast. In recent global work on urban carbon, fewer than **1%** of cities accounted for about **28.5%** of urban CO2 emissions in 2020.

[STAT: add one climate-pressure stat and one social-cost stat here, e.g. emissions elasticity, congestion, housing costs, disease scaling]

[VIZ width=medium: same frame, second layer revealing emissions / disease / congestion, ideally with the 28.5% stat]

So if humanity were slowly piling itself into a handful of giant cities, that would not just change where we live. It would change the scale of our wealth, our innovation, our pressure on the planet, and the intensity of everyday urban life.

[This is much better, it says something interesting. Maybe it would me more intuitive in per capita metrics. So, saying look a person in a big city makes X\% more than in a small city. I think to make the comparison intuitive we should refactor scaling laws and compare a 100K people city (a small city) with a 10M people city (a big city). And state the differences in those terms. Its much more intuitvie than the doubling argument.  ]

Are we heading there?

[Here we could say that A huge human tide is flowing into cities. Every month, roughly a New York City's worth of people becomes urban. Talk about urbanization in general. How fast it is proceeding, how many people are there and how many people will join soon. Quantify with explicit numbers and metaphors. This is just mindboggling. Then we pivot by saying look all these people are moving into cities, but whether we end up all in giant cities depend on which cities these people are going to. if they go to big and small cities alike then urbanization is a tide that lifts all boats, so we will not live all in megacities. Proportions will be preserved, but if instead they head preferentially to large cities ending up in megacities its just a matter of time. So we set out the hypotheses. We could also say if they go preferentially to small cities we will end up with a lot of small cities. I think this is the tensions we were looking for. Then next we privot to the question of what is the city and the data. We could say somethign like, but to understand this we first need to understand what is a city... or something better than this very cheap transition. ]

Text width: narrow

---

## 2. The question

Over the last half century, the world has become much more urban, and much more concentrated in large cities.

[STAT: insert core opening trend here, e.g. urban share of world population and/or share living in 1M+ cities in 1975 vs 2025]

At first glance, the trend seems obvious: the giants are pulling away.

This is not just my question. For decades, urbanists, economists, physicists, and geographers have all been circling the same mystery from different angles: why do big cities seem to punch above their weight?

Duranton and Puga break the answer into three mechanisms: cities let people and firms **share**, **match**, and **learn** better. Bettencourt's scaling work tries to measure what that means in the aggregate. Balland shows that the most complex kinds of knowledge, like advanced technologies and frontier research, are especially concentrated in large cities.

[STAT: add 2-3 anchoring numbers from outside the paper here, e.g. patent scaling, paper scaling, complexity concentration]

But to answer that seriously, I first need to solve a more basic question:

[This part I don't like. We can should instead belnd it in above. After sayign the scaling we should. WEll after all this is intuitive. Scalin, amtching and learning are much stronger in big cities. That's why we have this massive returns. For the downsside, we cna say that richer people consume more, that diseases spread much faster because tehre is much more contact (the same contact that make the city productive). So this why part should be associated to the stakes part above. Here we should say Are we heading there? the part of fast urbanization. And then we pivot to the data. We say to find out we need to figure out what is a city? This seems trivial but is infact hard. Expalin why its hard.  ]

**What is a city, exactly?**

Once a city grows, spills outward, swallows nearby settlements, or pushes growth into suburbs, how do you measure the size of the *same* city across decades?

Text width: narrow

---

## 3. What is a city?

This sounds simpler than it is.

Administrative borders are often useless for this question. They are political lines, not living urban footprints. A city's legal boundary may stay fixed while the real city sprawls far beyond it.

Paris is the cleanest illustration. Put the administrative boundary on top of a satellite image and it looks absurdly small. The legal city is a tiny core. The actual city has long since spilled out into a much larger urban mass.

[STAT: add Paris comparison here, e.g. admin area vs built-up area vs metro population / area]

[VIZ width=full-bleed: administrative boundary of Paris over a satellite image, with a brief callout about how small the legal city is]

Functional definitions are better in some ways, because they follow commuting and economic ties. But they are harder to compare consistently across countries and over time.

[Let's skip this part about fucntional definition. Again its too academic. ]

What I need is a definition that is stable, comparable, and flexible enough to grow with the city itself.

So I build cities from the ground up.

[VIZ width=wide: comparison of administrative vs functional vs geographic built-up footprint for one iconic city]

Text width: narrow

---

## 4. Measuring cities from space

This is the part of the story I love most.

For decades, satellites have been quietly building a memory of the planet. Landsat has been imaging the Earth since the 1970s. Sentinel added another leap in resolution and coverage. Together with census data, they make it possible to see urbanization at a scale that would have been almost unthinkable a generation ago.

[Ahhh this is nice. Much better. Makes me excite to see what's next!]

[STAT: insert a crisp EO fact here, e.g. first Landsat year, Sentinel launch years, GHSL resolution, number of epochs]

[VIZ width=wide: a short Earth-observation prelude, from Landsat-era imagery to modern GHSL products]

The global data I use comes from the GHSL: a system that turns satellite imagery and census information into global grids. [Here we must explain more and better how these grids are derived. This is genuinely interesting and a massive work. So why not give a paragraph of detail. What's the inuitive idea of how to estimate built-up area/ And population? ] The world becomes a mosaic of cells. Some cells tell us where built-up land is. Others estimate how many people live there.

[STAT: add grid resolution and epoch cadence here]

[Here we pivot with something like. But how do we recostruct cities form these grid?]

So the logic is simple.

First, use the built-up and settlement grids to identify which cells are urban.

Then group neighboring urban cells into clusters.

Then let those clusters evolve through time, so the boundary can adapt as the city expands.

Then overlay that boundary onto the population grid and sum up the people inside it.

That is the basic trick: **boundary from one grid, population from another**.

[VIZ width=full-bleed: satellite image -> built-up grid -> urban/non-urban cells -> clustered boundary]

[VIZ width=wide: boundary over population grid, with the final population estimate emerging as a sum of cells]

This gives me a consistent way to estimate city populations across countries and through time. Using that procedure, I build a global dataset covering **99 countries**, about **94% of the world's population**, between **1975 and 2025**.

[STAT: add city-year observations and/or number of cities here]

[VIZ width=full-bleed: rotating globe or world map filling with city polygons / boundaries over time]

Text width: narrow, split into short blocks around visuals

---

## 5. First result: it looks like the giants are winning

Now the first answer comes into view.

A huge human tide is flowing into cities. Every month, roughly a New York City's worth of people becomes urban.
[Here we skip this we already talked about how urbanization is proceeeding very fast and we already set up our hypothesis of whether people are going to gian cities or not. 
Maybe we want to breifly reming that hypothesis here and then go to the unevenly flowing tide. ]

[STAT: put exact annual / monthly equivalent here]

[VIZ width=wide: global urban population growth over time]

And that tide is not flowing evenly.

Some giant cities have expanded at astonishing speed. Shanghai is one of the clearest examples: what was already a major city in the late 20th century has become something far larger in just a few decades.

[STAT: insert Shanghai population growth, built-up expansion, or rank change here]

[VIZ width=full-bleed: Shanghai then vs now / urban footprint expansion]

Seen in aggregate, the picture looks even more dramatic.

Large cities, on average, appear to be outpacing smaller ones.

[STAT: add one aggregate growth comparison here, e.g. megacities vs median city, or slope / group-growth stat]

[VIZ width=medium: megacities vs average city, stock-chart style]

[VIZ width=medium: intuitive size vs growth chart, with annotation instead of technical labels]

If you stopped here, the conclusion would feel almost unavoidable:

**we are heading toward a world dominated by giant cities.**

[Here we should put more emphasis on the self-reinforcing nature of an increasing size growth curve. ITs not just that large cities are growing faster. Its that if learge cities grow faster, they get even larger and so grow even faster, and so on in an exploding spiral. That's why the endpoint looks inevitable. But this has to be explicitly made clear because its not intutivie. Its a runnaway phenomenon. A self-reinforcing loop]

Text width: narrow

---

## 6. The twist: the world is not moving in one uniform way

But that first answer is misleading.

Once I split the data, a different pattern appears.

In Asia and Africa, large cities have often grown faster than the rest. In my data, the average 1M+ city in Asia and Africa outgrew the national urban average by about **7%** (each decade? put the time)

In Europe and the Americas, that advantage is much weaker, and in parts of the Americas it can even disappear.

[STAT: add Europe and Americas comparison here, e.g. Europe slight positive, Americas -1.6%, plus beta range]

[VIZ width=wide: split comparison, Asia/Africa vs Europe/Americas]

At first this can look like a geographic divide.

It is not.

The deeper pattern is about timing.

Some countries are earlier in the urbanization process. Others are later. And the growth advantage of large cities changes as that process unfolds.

But to really believe that, I need more than a global snapshot. I need to watch a single urban system develop.

Text width: narrow

---

## 7. To watch an urban system age, I rebuilt the United States

So I built a second dataset, this time for the United States, stretching from **1850 to 2020**. [Ephasiize here MF 1850. Just to know somethign about that time its amazing.]

This is a different kind of data feat. There are no satellites in 1850. So I reconstruct cities from census microdata, historical census places, modern place boundaries, and the movements of people themselves.

[Add a piece here lauding the USA which was already keeping a respectable census back in 1850 when most countries were just peaseants. They were ahead of time even back then. They had already understood the unresonable effectivness of data (this is a ref for people in data science which might be reading this)]

[STAT: add one or two “authority” numbers here, e.g. number of records matched, number of places, number of decades]

That means harmonizing old place names, dealing with places that disappear and reappear, linking historical settlements to stable modern identifiers, and then turning that cleaned historical geography into gridded population surfaces that can be clustered the same way as the global data.

[STAT: add stable-place count and/or city-year obs for U.S. dataset here]

[VIZ width=wide: historical census places -> harmonized places -> gridded surface -> evolving city blobs over time]

The global dataset gives me breadth.

The U.S. dataset gives me deep time.

And deep time shows something crucial: in the 19th century, the growth advantage of big cities in the U.S. was strong. Over time, it weakened.

[STAT: add U.S. early-vs-late slope numbers here]

[VIZ width=medium: U.S. size-growth curve flattening across long-run periods]

This is not just a cross-sectional pattern across countries. It is something an urban system can live through.

Text width: narrow

---

## 8. And you can still watch that process happen today

The U.S. shows the whole movie, but from very far away in time.

South Korea shows a faster, more recent version of the same arc. 
[Here add a couple of lines on the Korean Miracle. I think everyone should know about this In the 60 korea was a land of peaseants. In the 90s it was a developed economy. This is nothing short of miracolous. The fastest development in world history. And it is because of that massively fast development that we can actually see most of koreas urbanization in such a short window. This is rather unique of korea since almost no other country managed the same feat. ]

In the 1970s and 1980s, Seoul raced ahead. Later, that special advantage faded.

[STAT: add Seoul / South Korea early-vs-late comparison here]

[VIZ width=medium: Seoul vs rest of Korea over time]

[VIZ width=medium: South Korea size-growth curve flattening over time]

Put the two together and the pattern becomes much harder to dismiss.

What looks like a geographic divide in today's world is, to a large extent, a difference in where countries sit along the same urban lifecycle.

Text width: narrow

---

## 9. Why big cities surge ahead, and why that fades

This is the core idea of the piece.

Early in urbanization, the biggest cities often surge ahead because they become magnets. They pull in migrants, capital, infrastructure, firms, universities, ports, ministries, and the kinds of specialized workers who make everyone around them more productive.

This is where the broader literature matters. One tradition says the gains come from sharing: large cities let many people use the same specialized infrastructure and services. Another says they come from matching: thicker labor markets make it easier for firms and workers, buyers and suppliers, ideas and institutions to find each other. A third says they come from learning: dense places are machines for imitation, comparison, gossip, apprenticeship, and knowledge spillovers.

Complex economic activities are especially hungry for this density. That is why patents, research, advanced services, and other knowledge-heavy activities concentrate so strongly in large cities.

[Here the explanation could be a bit strengthend about why exactly in the early phases of urbanization this makes an dimpact. Mayeb you can take inspiration from /Users/andrea/Desktop/PhD/scrollytell/cities-scrollytell/src/resources/scaling/krugman1991increasing which is one of the best papers at telling this story. "Then come the railorads and then steam engine part is great. Read the intro and I think you will have plenty of ideas of how to frame this]

[STAT: add one complexity/agglomeration stat here, e.g. patent scaling, papers scaling, or concentration of complex technologies]

[VIZ width=wide: idealized “urban adolescence” explainer, with large cities pulling in migrants, firms, and infrastructure]

Then the logic starts to change.

The rural reservoir shrinks. Transport and infrastructure spread. Secondary cities become more capable. Housing costs bite. Congestion rises. Some growth spills into suburbs and satellite settlements. Governments and firms diversify across the urban system. In rich urban systems, large cities are still enormous, but they are no longer the only place where opportunity compounds.

The broader urban literature offers several plausible reasons for this fading too: [This is the kind of sentence that makes me vomit. This is good in an academic paper because you just want to say the truth but its stylistically horrible. Like who want't to read this bullshit?]

congestion and land costs start cancelling out agglomeration gains, knowledge diffuses outward, more activities become codified and easier to move, and mature urban systems get less monocentric over time.

[STAT: add one or two candidate-mechanism stats here, e.g. migration slowdown, suburbanization magnitude, housing-cost spread]

Suburbanization matters here, but it is not the whole story. It explains part of the flattening, especially in mature urban systems, yet the broader slowdown in big-city advantage is too large to be reduced to suburbs alone.

[STAT: add suburbanization benchmark here, e.g. historical beta drop vs definitional gap]

So the urban system matures, and growth becomes more balanced across cities of different sizes.

[VIZ width=medium: idealized animated curve labeled Adolescence -> Maturity]

This is the **urban lifecycle**.

Text width: narrow

---

## 10. What that means for the future

This lifecycle changes the forecast.

If I simply extrapolate the recent surge of giant cities forward, I get a very concentrated future: by 2100, about **42%** of the world's population would live in cities above one million people. [And what happens if I use runnaway growth? Maybe I can get something even moreesxtreme]

But the lifecycle suggests a slower path.

Large cities are likely to keep gaining population share, but more slowly than a simple extrapolation would imply. My estimate is that by 2100, about **38%** of the world's population will live in 1M+ cities.

[STAT: add full arc here: 1975 -> 2025 -> 2100]

[VIZ width=wide: current-trend extrapolation vs lifecycle-based projection]

That may sound like a small gap. It is not.

It means roughly **450 million fewer people** living in million-plus cities than under the naive extrapolation of current trends.

That is the population of several large countries. It is a different urban future for hundreds of millions of lives.

[Here we could connect it back to what it means in terms of GDP, emissions and this kind of stuff using the scaling data. We can use approximation. We shoudl come up with some tangible number. How much GDP did we loose? 1 trillion? Less? more? How much Co2 did we save? 1 trillion tons? Less? More?

[STAT: add one human-scale comparison here, e.g. equivalent to U.S. + Mexico / EU big-country scale]

Text width: narrow

---

## 11. Ending: a world of giants

So no, we are probably not heading toward a future in which giant cities pull away forever at the same speed.

But neither are we returning to a world of evenly sized settlements.

The adolescent growth spurt of urbanization leaves a permanent mark.

It forges giants.

And those giants, once created, continue to shape the world we live in. They remain our biggest amplifiers: of wealth, invention, pressure, inequality, emissions, possibility.

[STAT: optional ending stat here, e.g. top x cities share of y outcome, or final 2100 share in giant cities]

The lifecycle does not erase the giants.

It explains how they were made.

[VIZ width=full-bleed: closing world-of-giants visual, likely global rank-size / skyline / planet-scale city distribution concept]

Text width: narrow

---

## Notes on pacing and layout

- Default text width: `narrow`
- Default chart width: `medium`
- Use `wide` for comparisons, sticky explanatory sections, and methodology reveals
- Use `full-bleed` only for major set pieces:
  - Paris boundary over satellite image
  - satellite-to-city pipeline
  - global city map
  - Shanghai expansion
  - closing visual

- Keep the overall feel text-led, roughly 60-65% text and 35-40% visuals
- Use fewer but more legible visuals than in the previous draft
- Break the methodology into two separate acts:
  - the global satellite pipeline early
  - the U.S. historical reconstruction later, when the story needs longitudinal proof
- Reserve one substantial section for causal speculation; that is where the piece can be bolder than the paper
- Bring in surrounding work freely where it sharpens the story:
  - agglomeration mechanisms from Duranton and Puga
  - scaling logic from Bettencourt
  - complexity and innovation concentration from Balland
  - climate and emissions stakes from the urban CO2 literature
