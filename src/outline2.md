# Are we all going to live in giant cities?

## 1. Hook: the stakes

This question pressures me.

The bigger a city gets, the more it **amplifies** everything about us.

Double a city's population, and you more than double some of its most powerful outputs: ideas, invention, productivity, wealth.

[VIZ width=medium: one animated scaling explainer showing population vs innovation / GDP]

[For example, add some stats here of how much more innovation/patents, etc. to make things precise. ]

But city size also amplifies the bad: congestion, pollution, disease risk, crime, pressure on housing.

[VIZ width=medium: same frame, second layer revealing emissions / disease / congestion]

[Same add some stats to make this more precise. How do CO2 emission scale with size, what does it mean? Leverage a bit climate change here to raise the stakes]

So if humanity were slowly piling itself into a handful of giant cities, that would not just change where we live. It would change the scale of our lives, our economies, and our problems.

Are we heading there?

Text width: narrow

---

## 2. The question

Over the last half century, the world has become much more urban, and much more concentrated in large cities.

At first glance, the trend seems obvious: the giants are pulling away.

But to answer that seriously, I first need to solve a more basic question:

**What is a city, exactly?**

And once a city grows, spills outward, swallows nearby settlements, or pushes growth into suburbs, how do you measure the size of the *same* city across decades?

Text width: narrow

---

## 3. The measurement problem

This sounds simpler than it is.

Administrative borders are often useless for this question. They are political lines, not living urban footprints. A city's legal boundary may stay fixed while its real urban area sprawls far beyond it.

[Illustration of the adminstrative borders of paris on top of a satellite image. Short discussion of that. I think this renders the point very well. Its a very impressive image, paris admin borders are so small and all the city has spilled out.]

Functional definitions are better in some ways, because they follow commuting and economic ties. But they are harder to compare consistently across countries and over time.

What I need is a definition that is stable, comparable, and flexible enough to grow with the city itself.

So I build cities from the ground up.

[VIZ width=full-bleed: comparison of administrative boundary vs functional area vs geographic built-up footprint for one iconic city]

Text width: narrow

---

## 4. From satellite image to city

I start with satellite-based global settlement data.

[Explain here how we get from satellite to grid cells using the GHSL grid. We need one viz + a brief explanation. I would also add a small note about how many satellites have been shot up and that now with satelites we can see the world on an unprecendented scale. Anyone that is interestd in EO or technoogyu will get goosbumps just by thinking about this. And it sets the stage for what is next. ]

At the base level, the world is broken into grid cells. Each cell tells us something about built-up land and population.

First, I classify cells as urban or non-urban.

Then I group neighboring urban cells together into clusters.

Then I track those clusters through time, so that when the shape of a city changes, I am not accidentally comparing one boundary in 1975 with a totally different one in 2025.

That last step matters a lot.

If a city's boundary expands simply because a few edge cells cross an arbitrary threshold, I do not want to mistake that for true population growth. I need a **stable boundary** that lets me measure change without being fooled by changing definitions.

[This explanation is too much methodological. We want to keep it simple and intuitive. I think we need to say the boundary adapts but the cell reclassifiation problem is maybe too much]

[VIZ width=full-bleed: satellite image -> built-up raster -> binary urban/non-urban -> clustered boundary animation]

[VIZ width=wide: two-year boundary matching / stable city boundary explainer]

This gives me a way to estimate city populations consistently across countries and across time.
[There is a leap here. This gives us the city boundaries. But how is then population inferred? We need to go back to GHSl and explain how they build their population grids. Then say when we have the population grid + the boundaries we can compute the population. ]

And once that machinery is in place, I can repeat it for cities across the world from 1975 to 2025.

[VIZ width=full-bleed: rotating globe or world map filling with city polygons / boundaries over time]

Text width: narrow, split into short blocks around visuals

---

## 5. A second dataset, much deeper in time

[This should appear later. At the moment its needless further methodology. WE can jump in the results directly and come back to this when we discuss depth. ]

Global satellite data gives me breadth.

But I also want depth.

So I build a second dataset for the United States, stretching from 1850 to 2020, using census microdata and reconstructed historical places.

That requires a different kind of work: harmonizing old census places, correcting disappearances and anomalies, and rebuilding a long-run picture of how settlements evolved over nearly the full course of US urbanization.

The global dataset shows me the pattern across many countries.

The US dataset lets me watch one urban system mature over a century and a half.

[VIZ width=wide: historical census places -> harmonized places -> gridded surface -> evolving city blobs over time]

Text width: narrow

---

## 6. First result: it looks like the giants are winning

Now the first answer comes into view.

A huge human tide is flowing into cities. Every month, roughly a New York City's worth of people becomes urban.

[VIZ width=wide: global urban population growth over time]

And that tide is not flowing evenly.

Some giant cities have expanded at astonishing speed. Shanghai is one of the clearest examples: what was already a major city in the late 20th century has become something far larger in just a few decades.

[VIZ width=full-bleed: Shanghai then vs now / urban footprint expansion]

Seen in aggregate, the picture looks even more dramatic.

Large cities, on average, appear to be outpacing smaller ones.

[VIZ width=medium: megacities vs average city, stock-chart style]

[VIZ width=medium: intuitive size vs growth chart, with annotation instead of technical labels]

If you stopped here, the conclusion would feel almost unavoidable:

**we are heading toward a world dominated by giant cities.**

Text width: narrow

---

## 7. The twist: the world is not moving in one uniform way

But that first answer is misleading.

Once I split the data, a different pattern appears.

In Asia and Africa, large cities have often grown faster than the rest.

In Europe and the Americas, that advantage is much weaker, and sometimes gone.

[VIZ width=wide: split comparison, Asia/Africa vs Europe/Americas]

At first this can look like a geographic divide, or even a civilizational one.

It is not.

The deeper pattern is about timing.

[I Think here we could introduce the US dataset. Talk about our effort and then move up the part on the US. Then we could pivot saying, but is this still true today and talk about south korea. Then we could speculate about why. This why part should be substantial. even though I do not show it in the paper. This is the place where I can freely speculate. After all no peer review, just a contract of confidence with the reader of which by now I have full trust because I ahve been super thorough.]

Some countries are earlier in the urbanization process. Others are later.

And the growth advantage of large cities changes as that process unfolds.

Text width: narrow

---

## 8. The urban lifecycle

This is the core idea of the piece.

Early in urbanization, the biggest cities often surge ahead. They attract migrants, capital, infrastructure, firms, and state attention. Their growth advantage is real.
[Maybe here we could speculate a bit more about why this happens. We cna give a bunch of reasons. This is not an academic piece. Its a blog post. So I cna say things that are plausible but for which I don't have a direct proof. The idea is that the reader must belive me. And I think I earned their trust by now. ]

Later, that advantage weakens. [Same here we can speculate a bit. Teh discussion of my paper has some thiis speculation. Why exactly does it weaken. Let's say some thigns. Let's say tha tsuburbanization amtters but its not the whole story for example]

Large cities do not disappear. They do not shrink into irrelevance. But they stop pulling away at the same pace.

The urban system matures, and growth becomes more balanced across cities of different sizes.

South Korea makes this visible over a relatively short period. In the 1970s and 1980s, Seoul raced ahead. But later, its special advantage faded.

[VIZ width=medium: Seoul vs rest of Korea over time]

[VIZ width=medium: South Korea size-growth curve flattening over time]

The same thing happened in the United States, only earlier and over a much longer span. In the 19th century, big-city advantage was strong. Over time, it weakened.

[VIZ width=wide: US historical animation of city system evolution]

[VIZ width=medium: US size-growth curve flattening across long-run periods]

This is the **urban lifecycle**.

A phase of urban adolescence forges giant cities. A later phase of urban maturity flattens their growth advantage.

[VIZ width=medium: idealized animated curve labeled Adolescence -> Maturity]

Text width: narrow

---

## 9. What that means for the future

This lifecycle changes the forecast.

If we simply extrapolate the recent surge of giant cities forward, we get one future: ever-rising concentration.

If we assume cities of all sizes grow proportionally, we get another: a much flatter future. [Let's avoid talking about proportional growth. That's an academic debate no one really cares in the real world about it and its kinda hard to explain and justify. Just extrapolation of current trends and what we really get. ]

But the data suggest something in between.

Large cities are likely to keep gaining population share, but more slowly than a simple extrapolation would imply.

[VIZ width=wide: three future scenarios compared
- extrapolation of current trend
- proportional growth
- lifecycle-based projection]

My estimate is that by 2100, about 38% of the world's population will live in cities above one million people.
[Let's state absolute numb]

That is higher than the proportional-growth benchmark.
Lower than the runaway-giant-city scenario.
And much closer to the story the long-run data actually tell.
[Let's state absolute numbers e.g. 450 million. We want to state the magnitude of the difference. Make the reader feel how many lives are different in these two model of the world]

Text width: narrow

---

## 10. Ending: a world of giants

So no, we are probably not heading toward a single planetary future in which giant cities endlessly pull away from everything else.

But neither are we returning to a world of evenly sized settlements.

The adolescent growth spurt of urbanization leaves a permanent mark.

It forges giants.

And those giants, once created, continue to shape the world we live in. They remain our biggest amplifiers: of wealth, invention, pressure, inequality, emissions, possibility.

The lifecycle does not erase the giants.

It explains how they were made.

[VIZ width=full-bleed: closing world-of-giants visual, likely global rank-size / skyline / planet-scale city distribution concept]

Text width: narrow

---

## Notes on pacing and layout

- Default text width: `narrow`
- Default chart width: `medium`
- Use `wide` for comparisons and sticky explanatory sections
- Use `full-bleed` only for major visual set pieces:
  - city definition comparison
  - satellite-to-city pipeline
  - global city map
  - Shanghai expansion
  - closing visual

- Aim for about 8 to 10 major visual moments in the whole piece
- Keep the overall feel text-led, roughly 60-65% text and 35-40% visuals
- Break the methodology section into several short readable text blocks, not one long exposition
- If needed, the reader should be able to skim the visuals and still follow the prose
