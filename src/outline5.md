Are we all going to live in megacities?

Take two cities. One has 100,000 people. The other has 10 million. The bigger one does not just contain more people. Those people are qualitatively different. They are more productive, as measured by their wage, which is 74% higher. 
They are more innovative: they are 3.5 times more likely to produce a patent. As a result, wealth and innovation concentrate.  In the United States, the ten most innovative metros account for 23% of the population, but 48% of patents and 33% of GDP.

[Figure 1]

And when we get to fronteer knowledge this is even more pronounced. People in large cities are more 3.5 time more likely to produce any type of patent, but are X times more likely to produce a patent in a fronteer industry like farma or advanaced tech. 

The general idea is that there are non-linear scaling laws. As city get bigger --- their scale increases --- the people within them become qualitatively different, e.g.,they are more innovative, more productive.

The scaling pattern, however, cuts both ways. The downsides scale too. For example, people in big cities have X\% higher CO2 emissions. They are X\% more likely to contract sexually transmitted diseases. They spend X\% more time in traffic and X\% more of their salary on their homes. 

Put simply, big cities amplify invention and income, but they also amplify congestion, land pressure, infrastructure stress.

So whether we are all going to live in megacities is a curiosity. It is a crucial determinant of how much wealth we can produce, where our technological frontier sits, and how we are going to impact and consume the resources of our planet. 

Cities overall are growing fast. Every 2 months the urban population adds 20 million people. That is one New York City worth of people. It was not always like this. In the 1800s, urbanization was a thing of few countries. Mostly industrializing countries in the west. England was first, followed by Benelux area. Then the US. Latin America. Southern Europe. North Africa. Evereyone else. [Check the sequence is correct]. Today, every country is either urban or rapidly urbanizing. More than 50\% of humanity lives in cities. And in the next 75 years, cities are projected to add about X billion residents. 

Where will these people go? Small towns or sprawling mega-cities? Three scenarios are possible. 

In one, new urban residents spread across large and small cities alike, and the overall shape of the urban system stays roughly intact.
That means that a good share of the whole population, say around X\%, will continue to live in cities with fewer than 1M people. 

Another scenarios, the biggest cities absorb a disproportionate share of growth. People move to these urban behemoths. They grow faster than the rest and gobble up an every increasing share of the population. If today X\% of the world population lives in 1M+ cities, in 2100 it could be X\% or even much higher. Eventually, there will be just a couple of massive cities dominating the world population. 

In third scenario growth leans toward smaller cities, producing a more distributed urban future. The small cities get more of the pie. They grow faster than the big ones. Their X\% share today becomes larger over time. And altough they grow larger, the population remains distributed across many places instead of piling up in a handfull of winners. 

[Figure 2]

So, which of these futures is more likely? That is the real question. The world is urbanizing fast, but which cities are absorbing that growth? 

Answering this question is hard. And the reason why its hard might be different from what you expect. Or at least it was different from what I expected. We use this word "city" to describe this thing where people live near each other. 
But the more I ponder the question "what is a city" the more it becomes hard to answer. Its one of those abstractions that make sweep all the complexity under the rug. But once you lift the rug, its a total mess. 

Take for example Paris. If you ask the French government what is Paris they might point you to the Legal borders of the city. This is an area of just 105.4 square kilometers and had about 2.11 million residents in 2022. This border is a fossil of historical accident. If you take a satellite picture of paris, you see that the built-up area has spilled way beyond the border in a much broader area. Various parts of the banlieu are effectively one physical unit with paris. And you can push it even further. Let's say now you consider not only the physical city, but the attraction area. The area from where people move into paris for work or other reasons. The people who are connected to paris but by invisble ties. Then that area is most of northern france. It stretched across 18,940.7 square kilometers and holds 13.24 million people. I guess you start seeing the problem: What is Paris? This question is hard to answer for Paris. But to understand where the world population is headed we have to answer them for every single damn city on this planet.

[Figure 3]

For most of history, answering this questions was impossible. Not hard, impossible. You would have to put everyone in aggreement, every statistical agency on the planet, abotu the definition of city, and then maintain that agreement across time. 

Then satellites started quietly building a memory of the planet. Landsat has been observing the Earth since the 1970s. Sentinel-2 added much sharper optical imagery in the 2010s. Today, the planet get's photographed every second by a different satellites. This imagery made it possible to skip all the agreement. It created a picture of the earth that is comparable across all places, and adjusting the resolution also across all times. With some wizardry one could use those pictures to reconstruct cities and their populations. 

The basic idea is simple. First, you start from the pictures. You break this pictures into small cells. For each cell, you esitmate how much of each cell is physically built up: roofs, roads, blocks, industrial surfaces, the material footprint of settlement. With this data you can trace the boundaries of physical cities. That is, you get a grid 1kmx1km cells covering the whole planet, and its kinda easy to say whether a cell is urban or not. This is the work of the GHSL a european initiative. 

In my work, I take these grid to construct cities. The algorithm is simpl.  First,  I identify which cells count as urban. Then, I connect neighboring urban cells into clusters. Each cluster is a city. 

[Figure 4]

Next, I need to assign it a population. After all, we are interested in the population growth. 
Doing that require quite a bit of extra effort. You start by estimating the physical volume of houses in the cells. You look at shadows, re-project harmonize, to infer how a 3D volume of the built up material in a cell. You collect census totals reported for administrative areas. These areas tile up the whole worrld into small pieces. They might be of different size in different countries.Usually they are farily small, but not always so. Given the population in these areas, you redistributes those residents into grid cells using their volume from before. Where there is more volume, more people are assigned.Tada, you know have an guess, a pretty educated one, of how many people live in eavch 1kmx1km cell of the world. I then take this and my city boundaries, sum up all the people within the boundaries and get the population of the city in some givne year. 


[Figure 5]


Using that procedure, I build a dataset of global cities that covers 99 countries, about 94% of the world’s population, from 1975 to 2025, with 1,604,593 city-year observations.

[Figure 6]

At first glance, the giants really do seem to be winning. The share of the world population living in million-plus cities rose from 11% in 1975 to 24% in 2025.
And that in 10M+ cities rose from X\% to X\%. This trend is clear in developing coutnreis. Take for instance, Shenzen. It was a fisherman village in 1980 and its a 150 million metropolis today. 

[Figure 7]

Acoss the global data, larger cities often appear to outpace smaller ones. If we plot the size of city on the x-axis and its growth on the y-axis we observe that over time large cities outpaced their peers. 

[Figure 8]

Now this is self-reinforcing: If larger cities grow faster, they become larger, and this leads them to grow even faster, and so becom even larger. A small lead turns into a large lead. Follow that logic far enough and the future starts to look like a world increasingly dominated by giant cities.

Yet, when you split the data, a different pattern appears. The average 1M+ city in Asia and Africa outgrew its national urban average by about 7% between 1975 and 2025. But in Europe, these cities barely outgrew the national average and in the Americas, 1M+ cities actually grew about 1.6% more slowly than the national average. 

[Figure 9]

At first, that looks like a geographic divide: perhaps Asia and Africa are giant-city regions, while Europe and the Americas are not. But another hypothesis is that timing matters: What looks like a map of regional difference is, to a large extent, a map of countries sitting at different stages of the same process. 

One way to check this is oreder countries on the x-axis by how much they are urbanized, and on the y-axis use a metric of how steep is teh curve between growth and size. How much large cities grow faster. When we do this, we observe a neat downward sloping correlation. More urbanized countries tend to see their large cities outgrowing the rest less. 

But to really determine this a cross-sectional snapshot is not enough. WE need a longitudinal series. 

The United States provides likely the one of the few longitudinal snapshot that are long enough to capture this phenoomenon. Long before satellites, long before digital maps, long before modern geographic information systems, the United States was already collecting census material rich enough that it can be turned back into a map of urban development. Census bureau officers went around the country, they asked registered individual people in individual places, every 10 years [More about how the census was collected]. These handwritten documents were passed down in library through generation, until recentrly a massive project transformed those old project in machine readable format, linked across years, matched to old places. The result of this massice effort is the: IPUMS Full Count now makes available over 800 million individual-level census records for 1850–1950. 

I took those records and reconstructed cities from 1850 to today. I constructed first grids of population and then aggregated them to cities. 
Surpsingly, these incredbile long run data. shows exactly the pattern the global data hint at. Early on, large U.S. cities had a strong growth advantage. Over time, that advantage weakened dramatically, until today its roughly flat. 

[Figure 11]

Another historical accident allows us to dig deeper. South Korea's economic miracle. Korea’s postwar transformation was not merely fast. It was historically extreme. The IMF describes three decades through the 1965-1995, in which annual real income growth averaged over 8% per year. The World Bank describes urbanization rising from 28% in 1960 to 79% in 1996, and GDP per person climbing from about $158 in 1960 to above $31,000 by 2020. That is development in fast-forward. This massive development pace implies that our global cities dataset 1975-2025 sees much of Korea's development. Of no other countries can be said the same. 

And guess what. Korea shows much the same plot in a few decades. Early on, Seoul and the largest Korean cities pull away hard. Later, the advantage fades. Put differntly, we continue to see evidence of this urban lyfecylce where big cities take the lead and but then petter out. 

[Figure 12]

Why would that be? The causes are likely many. Here is my take. Early in development, distance is expensive, markets are thin, and much of the economy is still tied tightly to land. Then transport improves. Manufacturing scales. Rail, ports, power, finance, universities, and state capacity reward concentration. Once one place gets ahead, the feedback loops start. Firms want access to customers. Workers go where the jobs are. Suppliers follow firms. Infrastructure follows everyone. A city that got a little ahead can suddenly get far ahead. Essentially, its like the arrival of modern technology opens new vast opportunities and large cities are the first to seize them. 

Then the systme. start hitting its limit. The logic changes. The rural reservoir shrinks. Transport and infrastructure spread outward. Secondary cities become capable of supporting their own thick labor markets. Land and housing costs bite harder in the biggest cores. Some growth spills into suburbs and satellites. S. All these conspire to slow the giants down.

So where does this leaves us going forward? Where are we headed in 2100? If current 1975–2025 size-growth patterns were simply extended forward, that figure would be about 42%. But the self-reinforcing nature suggested above could push this even higher. The lifecycle model suggests instead somewhere around 38%. Relative to the straight extrapolation, that means about 450 million fewer people in million-plus cities by the end of the century. 

[Figure 13]

That is not a bookkeeping difference. The same scaling logic applies: these 450 million inhabitants will have see less wealth, invention, but also less inequality and climate risk as compared to a world where they had lived in large cities, and this will be visible in the aggregate, from global economic growth to climate change. 

So are we all going to live in giant cities?

Probably not. At least not in the runaway way that a first glance at global city growth estimates suggests. But the giants forged by the large growth advantage in the early phases of urbanization will remain, amplifying wealth, invention, ambition, pressure, inequality, climate risk, and much more. 