I want to make a scrollytell in the style of the pudding:

https://pudding.cool/

The scrolly tell is about the paper in [paper.md](src/paper.md) 

In @outline.md There is a brief outline of the rough idea of what I would like to build in the Scroll Italia, the main idea is that it should tell the story of the paper, but in a more interesting and less scientific way. Should be more empathetic. You should be quite ambitious about the visualizations. There are many cool visualizations one can do! Put some ideas in the scroll, Italy, but let's get more ambitious since now we have this automated code and you can code most of this shit. Let's think it through. Maybe we can do animations or 3D renderings or these cool things. But the core thing is still to write an interesting story, and to be interesting it has to be really a story, not more a collection of visualizations, but something that kind of guides the reader on a journey, an intellectual journey.

Let's modify together outline.md to kind of enrich the story. Add the interesting bits and pieces here and there. 

Here are some thoughts that he had. 

- So I open with the scaling theory, and now it's really underdeveloped. The ideas around scaling theory and what it means are kind of vague. I think to make it an interesting intellectual journey, this thing should be slightly expanded to explain the nuts and bolts of the ideas here. Obviously, we don't have a nice thing here. We don't have to be rigorous; we don't have to hedge our things and say "correlated" or "x" or "y" or "kind of is associated with" or this shitty academic terms. We can just say "kind of drives" or "causes" and these kind of stronger verbs that are rarely used in academia. In fact, this is kind of an opinion piece; it's a story we want to tell. I put in the resources a couple of papers on scaling theory, from which you can pull maybe some ideas. The papers: I pre-parsed them and put them in Markdown so you can read them easily. Also have the figures. You can check them out in case it helps with some inspiration. Kind of academics have thought a lot about how to structure the figures. This could help with some vids. Sample figure 1 of Ballant and Al might be a good one! I think one of the best discussions of agglomeration economies (Scaling) is Durantan and Puga (see duranton2004micro).

- Next, I pivot to the data. How I construct this data: there are various things that could be done here. I think it is underexplained how we get from a satellite image to the estimation to the grids. This is explained in the ghsl_paper and we might want to say more about that, add viz expalining ideas in there. 

- Then you want to explain the city clustering algorithm that moves from the grids to the cities. This is in my paper. You can read the description there, and yeah, think about visualizations. It could help. 

Okay, now we have constructed the premise, so scaling theory. Why do we care about the outcome? We've built the credibility through illustrating this data and showing essentially that we did quite a bit of data work. Actually, in my paper I do also another data work that is relative to the US Census from 1850 to 2020, and reconstructing the cities there. Maybe we could first discuss kind of the global results, and then afterwards say, "Okay, we have seen these results mainly cross-sectionally, but do they also hold longitudinally in the right? Is it true that, kind of, in one country across time? And then we can pivot to that data and that reply. I think industry data front is over, but happy to hear your take on this. Here I added a couple of papers with the data about this stuff:
- The IPUMS paper that kind of tells the full consensus, the story, what's going on.
- The berkesh paper, where they kind of geolocated elements. You can use that to understand better what this data looks like.
That'd be all my paper and supplementary information. I actually do not have the IPUMS paper but here is a link
https://usa.ipums.org/usa/full_count.shtml


So, for what concerns the results, what we are kind of the way we want to set it is first to create this tier. Yes, we're all moving there, and then to insert the new ones. Now, look, if you are an advanced economist, not really like this, so the idea is to start with kind of globally aggregated data. Show the massive base of urbanization itself. Every month, a population in the South New York becomes urban, and then show that it's not equal everywhere with examples. We need to find cool examples. Maybe we can even show satellite images. Look, this is Shanghai, beyond the photos that I've already seen. You can maybe show really satellite images, like this is Shanghai in 1975. This is fucking Shanghai today; it's like ten times bigger. Ideally, here we could have three plus for the population, which would really illustrate the change. It's so important to use intuitive charts, like charts that people can understand easily. For example, the stock market chart I'm proposing is one of those. You see the Omega Z's versus average sitting stock market kind of chart over time. It's really intuitive when it's going to the moon. 

 Okay, we created the scale. We push it by projecting into a future that movement, maybe making it accelerate a bit on purpose to show to increase the scale, increase the path at that point. 

 then we pivot and we say, "Okay, no, it's not like that. Let's split it up. Let's compare Germany to China. Let's compare the US to China." That's the best comparison I think we can do the one that most people wouldn't be interested in, also for geopolitical reasons

 you show these look very much different.  here we introduce the size grouped curves that are kind of the point of the paper, but we need to do this very intuitively. It's very intuitive axis  we can call the log growth rate just a growth rate, to keep things simple. Otherwise,  not everybody knows what the log is 

 Then we kind of generalize beyond the USA and China, and instead we look at continents. As suggested in the outline, we go and look at Africa and Europe, African Asia versus Europe and the Americas, kind of this bifurcation. 

 And then we ask Are then Asia and Africa are headed in a future of megacities. This is kind of the lead to introduce the Life Cycles Theory, and here maybe it would make sense to use the longitudinal data, so we start with South Korea and we show, for example, South Korea. 

 Then we moved to the US, and we said, "Look, with the Cadillac, that is crazy dataset from IBMs that goes back to 1850. What the hell would the US look like in 1850?" Maybe we have an animation or some kind of data thing where people can look at the cities as they evolve over time or blobs. 

 And then we show kind of the relationship between size and growth changing over time. That can also be an animation or just showing the size growth slope, even though we have to introduce that slope and so we would have to kind of explain that intuitively. 

 So essentially, here we use the data to explain this life cycle theory. 

 Once we have the Life Cycle theory, then we use it to make predictions and projections about the future. It will be kind of interesting to say, "Okay, we show again the kind of chart that we were showing before with the cities going to the moon, and then we show our predictions that are slightly flatter. They flattened out over time before 2100. We show the curve; could be cool." 

But the adolescent growth spurt leaves behind a permanent legacy: **a world of giants.**

[CLOSING VIZ, to think though]

Maybe we could discuss the power law distribution, what is left behind. We could discuss power laws and what power laws are, show that this is a power law, and kind of intuitively explain what it means that this is a power law. How different are the sizes of cities, and how much this is kind of surprising with respect to the heights of humans. You can check out the Clauset paper to get more information about power laws and interesting facts to put in. 
We can close with implications that these giants were forced in the past until you would kind of stay there. I don't know; I think I have to think through more here, but this is already a kind of decent first draft. Yeah, there was a better ending. 

Also, another option would be to start with this power law stuff and close with the skating stuff, but I think that's more technical. I'm not sure. What do you think? 


