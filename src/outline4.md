# Are we all going to live in giant cities?

## 1. Hook: the stakes

This question pressures me.

City size is not neutral.

Take a city of **100,000** people and a city of **10 million**. The big one is not just 100 times larger. It is richer, faster, more inventive, and usually more intense in ways that are easy to feel and hard to ignore.

A person in the big city tends to produce more.

[STAT: compare per-capita GDP / wages between a 100K city and a 10M city]

Its firms and labs also tend to invent more.

[STAT: compare patenting / papers / frontier-tech concentration between a 100K city and a 10M city]

<Here use the balland2020complexb to sharpen the argument>
And when the work gets more complex, the concentration gets sharper. The most advanced technologies, the most specialized research, and the highest-end industries do not spread out evenly. They pile up in the biggest places.

[STAT: add one concrete fact about top tech / pharma / complex industries being concentrated in a few big metros]

[VIZ width=medium: x-axis city size, y-axis income per capita, patents per capita, etc. as the user scrolls show increasing lines developing. highlight the gap between a 100K and 10M city ]

The downside can scale too. Big cities can concentrate emissions, housing pressure, disease exposure, and the daily friction of urban life.

[STAT: add one climate stat and one social-cost stat here]

[VIZ width=medium: same small-city / big-city graph as above, now for emissions, housing costs, disease, congestion]

So this whether we all are going to live in giant cities in not a decorative question about city rankings.

If humanity were slowly piling itself into a handful of giant cities, it would change the scale of wealth, innovation, carbon, pressure, and inequality all at once.

And humanity is moving fast.

<Here we could explan a bit on the history of urbanization. When did it start. Its exponential growth ,initially slow but then explosive. Where it is today.>
A huge human tide is flowing into cities. Every month, roughly a New York City's worth of people becomes urban.

[STAT: add exact monthly / annual equivalent, current urban population, and projected new urban residents by 2050/2100]

[VIZ width=medium: x-axis time, y-axis urban population share globally + Western countries. Nto sure what else depends on the story of urbanization]

That sets up three futures.

If new urban residents spread across big and small cities alike, urbanization is a tide that lifts all boats. That means that the shape of the urban system remains roughly intact. There will still be a lot of people in big cities, but also in small cities. 100K cities won't disappear. Actually, their total share of population will remain roughly the same. 

If they flow disproportionately into the biggest cities, the giants get even larger, and their lead compounds. Thus, the future contains little place for small cities. 

If they flow disproportionately into smaller cities, I think you can guess: the future is more dispersed; more small cities. 

That is the real question.

Not whether the world is urbanizing. It clearly is.

The question is **which cities are absorbing that growth**.

But what is a **what is a city at all?**

Text width: narrow

---

## 2. What is a city?

This sounds trivial until you try to measure it.

A legal border is often a bad joke. Cities do not stop where the municipality stops. They spill outward, absorb nearby settlements, and keep changing shape.

Consider Paris. Put the administrative boundary on top of a satellite image and it looks tiny, almost comically small. The legal city is a dense historical core. The real city is a much larger physical organism.

[STAT: add Paris comparison here, e.g. admin area vs built-up area / metro area / population]

[VIZ width=full-bleed: Paris administrative boundary over satellite imagery, with callouts]

<this could be explained better>
So to understand which cities are growing we need to build a city definition that moves when the city moves. It cannot remain fixed. 

If the boundary stays fixed while the city spreads outward, any story about urban growth is already contaminated. 

With this in mind, I set out to find a new defintion of city that I can construct from the ground up

Text width: narrow

---

## 3. Measuring cities from space

For decades, satellites have been quietly building a memory of the planet. Landsat has been imaging the Earth since the 1970s. Sentinel added another leap in resolution and coverage. Together with census data, they make it possible to watch urbanization unfold almost cell by cell.

[STAT: add one crisp Earth-observation fact here: first Landsat year, Sentinel launch years, GHSL resolution, number of epochs]

[VIZ width=wide: satellite rotating around earth and taking pictures. Would be great to embed a GIF of what earth orbit looked in 1970 vs today]

<This is shit. It looks like GPT2 did the research. One could explain much better how GHSL Made their datasets. Please take some time to give me a very good description. 3 paragraphs. Use GHSL_Data_Package_2023 to explain it thoroughly>
The global data I use comes from the GHSL, which turns satellite imagery and census information into global grids.

The intuitive idea is simple enough to explain.

From above, satellites can see where the surface has been transformed: roofs, roads, blocks, industrial sites, the physical traces of settlement.

Census data, meanwhile, tell us how many people need to be placed back onto that surface.

Put those together and the world becomes a mosaic of cells. Some cells estimate built-up land. Others estimate population. The result is a gridded picture of human settlement on a planetary scale.

[STAT: add grid resolution, epoch cadence, and one line about how built-up and population layers are derived]
[VIZ: We need a nice viz to explain the GHSL methodology. A constructed viz when one scrolls. ]

<This is aweful prose. Please make this interesting. Explain it. Here you are just regurgitating made sentences>
But grids are not cities.

So the next move is to reconstruct cities from those cells.

First, identify which cells are urban.

Then connect neighboring urban cells into clusters.

Then let those clusters evolve through time, so the boundary can adapt as the city grows.

Then take the population grid and sum up the people inside that evolving boundary.

That is the basic trick: **boundary from one grid, population from another**.

[VIZ width=full-bleed: satellite image -> built-up grid -> urban cells -> connected cluster]

[VIZ width=wide: cluster boundary over population grid, population sum appearing cell by cell]

This gives me a way to estimate city populations consistently across countries and through time. Using that procedure, I build a global dataset covering **99 countries**, about **94% of the world's population**, from **1975 to 2025**.

[STAT: add city-year observations and/or number of cities here]

[VIZ width=full-bleed: world map filling with city polygons / boundaries over time]

Text width: narrow, split into short blocks around visuals

---

## 4. First answer: the giants seem to be winning

So where is the urban tide going?

Not evenly.

Some giant cities have expanded at astonishing speed. Shanghai is one of the clearest examples: what was already a major city a few decades ago has become something vastly larger.

[STAT: insert Shanghai population growth, built-up expansion, or rank change here]

[VIZ width=full-bleed: Shanghai then vs now / urban footprint expansion]

Seen across the whole system, the picture looks even more dramatic.

Large cities, on average, appear to be outpacing smaller ones.

[STAT: add one aggregate growth comparison here, e.g. megacities vs median city, or large-city advantage]

[VIZ width=medium: megacities vs average city, stock-chart style]

[VIZ width=medium: intuitive size-vs-growth chart, with direct annotation]

And this is where the danger of the pattern becomes clear.

If large cities grow faster, they become larger.

If they become larger, and size itself confers an advantage, they grow faster still.

That is not just unequal growth. It is a **self-reinforcing loop**.

Once that loop starts, the endpoint begins to look obvious:

**a future dominated by giant cities.**

Text width: narrow

---

## 5. The twist: the same tide lands differently in different places

But that first answer is misleading.

Once I split the data, a different pattern appears.

In Asia and Africa, large cities have often grown faster than the rest.

[STAT: add exact Asia/Africa comparison here, with time unit]

In Europe and the Americas, that advantage is much weaker, and in parts of the Americas it can even turn negative.

[STAT: add Europe and Americas comparison here]

[VIZ width=wide: split comparison, Asia/Africa vs Europe/Americas]

At first this can look like a geographic divide.

It is not.

The deeper pattern is about timing.

Some countries are earlier in the urbanization process. Others are later. And the growth advantage of large cities changes as that process unfolds.

But to really believe that, I need more than a global snapshot.

I need to watch an urban system develop from near the beginning.

Text width: narrow

---

## 6. America in slow motion

So I built a second dataset, this time for the United States, stretching from **1850 to 2020**.

Let me repeat 1850. 1850 is astonishingly early. Long before satellites, long before digital maps, long before modern data systems, the United States was already collecting census information rich enough that, with a lot of work, it can be turned back into a map of urban development. Its insane that we can still know where people lived in 1850. But exactly what data has the US collected and made public?

[STAT: add one authority / wow fact here about census scale or early data richness]

<Here we should explain the ipums full count census project: https://usa.ipums.org/usa/full_count.shtml. You should read about it here and produce 1-2 paragraphs explaining what they did. Its a massive project, super interesting.>


That means harmonizing old place names, dealing with places that disappear and reappear, linking historical settlements to stable identifiers, and rebuilding gridded population surfaces from the cleaned historical geography.

[STAT: add number of records, places, decades, stable places, and/or city-year observations here]

[VIZ width=wide: historical census places -> harmonized places -> gridded surface -> evolving city blobs over time]

The global dataset gives me breadth.

The U.S. dataset gives me deep time.

And deep time shows something crucial: in the 19th century, the growth advantage of big cities in the United States was strong. Over time, it weakened.

[STAT: add U.S. early-vs-late slope numbers here]

[VIZ width=medium: U.S. size-growth curve flattening across long-run periods]

Text width: narrow

---

## 7. Korea in fast-forward

The U.S. shows the whole movie, but from very far away in time.

South Korea shows a much faster version of the same arc.

That is what makes it so valuable.

In the early 1960s, South Korea was still overwhelmingly poor and rural. A few decades later it had become a rich industrial economy. Development happened so fast that a process which took far longer elsewhere can be watched in compressed form. 
<Here we should discuss a bit more the Korean miracel: https://en.wikipedia.org/wiki/Miracle_on_the_Han_River. This is a fascinating parentheses. >

[STAT: add a couple of “Korean miracle” stats here, e.g. urban share, GDP per capita, manufacturing share]

This makes Korea the only country that started its urbanizstion late, but that has already finished. That makes its full urbanization cycle part of our dataset. 

[STAT: add Seoul / South Korea early-vs-late comparison here]

[VIZ width=medium: Seoul vs rest of Korea over time]

[VIZ width=medium: South Korea size-growth curve flattening over time]

Put the United States and South Korea together and the pattern becomes much harder to dismiss.

What looks like a geographic divide in today's world is, to a large extent, a difference in where countries sit along the same urban lifecycle.

Text width: narrow

---

## 8. Why big cities surge ahead, and why that fades
<We still have a lot of work on the why. I think krugman1991increasing and pumain2006evolutionary have some interesting ideas in that direction. the paragraphs below are emabrasisngly written and we should probably re-write them from scratch, but I guess you see the idea of this section>

This is the core idea of the piece.

Early in development, a country is still tied tightly to land, distance, and small local markets. Then transport gets cheaper, manufacturing scales up, railways and ports matter more, and industry starts hunting for bigger markets.

Once one place gets ahead, demand and production begin to feed each other.

Firms want to be near customers.

Customers go where the jobs are.

Suppliers follow the firms.

Workers follow the suppliers.

Infrastructure follows everyone.

And the city that got a little ahead can suddenly pull far ahead.

[VIZ width=wide: idealized “takeoff” explainer, with transport, factories, migrants, and feedback loops reinforcing the core]

At the city level, that advantage comes through three channels at once.

Big cities let people **share** specialized infrastructure and services.

They make it easier to **match** workers with firms, buyers with suppliers, and ideas with institutions.

And they let people **learn** faster, because dense places are full of imitation, comparison, apprenticeship, gossip, and spillovers.

That is why the most advanced activities cluster so strongly in the biggest places.

[STAT: add one complexity / agglomeration stat here]

Then the logic starts to change.

The rural reservoir shrinks.

Transport and infrastructure spread.

Secondary cities become more capable.

Housing and land costs bite harder.

Some growth spills outward into suburban rings and satellite towns.

Old giants remain enormous, but they are no longer the only places where opportunity compounds.

[STAT: add one or two candidate-mechanism stats here]

Suburbanization matters here, but it is not the whole story. It explains part of the flattening, especially in mature urban systems, yet the slowdown in big-city advantage is larger than suburbanization alone.

[STAT: add suburbanization benchmark here]

So the urban system matures, and growth becomes more balanced across cities of different sizes.

[VIZ width=medium: idealized animated curve labeled Takeoff -> Maturity]

This is the **urban lifecycle**.

Text width: narrow

---

## 9. What that means for the future

<This is ok though it could be made more precise and absolute numbers still need to be calculated>

This lifecycle changes the forecast.

If current trends were simply extrapolated forward, the future would be highly concentrated: by 2100, about **42%** of the world's population would live in cities above one million people.

[STAT: add full arc here: 1975 -> 2025 -> 2100]

And there is an even harsher thought experiment.

If the big-city advantage kept reinforcing itself instead of fading, the outcome would be more extreme still.

[STAT: add “runaway feedback” benchmark here]

But the lifecycle suggests a slower path.

Large cities are likely to keep gaining population share, but more slowly than a simple extrapolation would imply. The estimate here is about **38%** of the world's population in 1M+ cities by 2100.

[VIZ width=wide: lifecycle projection vs current-trend extrapolation vs runaway-feedback scenario]

That may sound like a small gap. It is not.

It means roughly **450 million fewer people** living in million-plus cities than under the naive extrapolation of current trends.

[STAT: add one human-scale comparison here]

And because city size changes output, emissions, and pressure nonlinearly, a reallocation of hundreds of millions of people across the urban hierarchy is not a bookkeeping detail.

[STAT: add rough GDP / emissions / housing implication placeholders here]

It is a different urban future for hundreds of millions of lives.

Text width: narrow

---

## 10. Ending: a world of giants

<This ending is decent>

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
- Use fewer but stronger visuals than in the previous draft
- Keep the hook fact-heavy and intuitive: 100K city vs 10M city, not abstract scaling jargon
- Keep external facts in declarative voice
- Keep first person mainly for the data-building and discovery sections
