<span id="page-0-0"></span>![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_1.jpeg)

# Universal scaling laws in metro area election results

Eszter Bokányi<sup>1</sup>\*, Zoltán Szállási<sup>2</sup>, Gábor Vattay<sup>1</sup>

- 1 Department of Physics of Complex Systems, Eötvös Loránd University, Budapest, Hungary, 2 Children's Hospital, Harvard Medical School, Boston, Massachusetts, United States of America
- \* bokanyi@complex.elte.hu

![](_page_0_Picture_6.jpeg)

# G OPEN ACCESS

Citation: Bokányi E, Szállási Z, Vattay G (2018) Universal scaling laws in metro area election results. PLoS ONE 13(2): e0192913. https://doi.org/10.1371/journal.pone.0192913

Editor: Dan Braha, New England Complex Systems Institute & University of Massachusetts, UNITED STATES

Received: May 4, 2017
Accepted: January 17, 2018
Published: February 22, 2018

Copyright: © 2018 Bokányi et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

**Data Availability Statement:** Data are available from http://dx.doi.org/10.7910/DVN/SUCQ52, and public resources indicate in the Supplementary Information.

**Funding:** Authors were supported by the Hungarian National Research, Development and Innovation Office under Grant No. 125280 and by the grant of Ericsson Inc. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

## **Abstract**

We explain the anomaly of election results between large cities and rural areas in terms of urban scaling in the 1948–2016 US elections and in the 2016 EU referendum of the UK. The scaling curves are all universal and depend on a single parameter only, and one of the parties always shows superlinear scaling and drives the process, while the sublinear exponent of the other party is merely the consequence of probability conservation. Based on the recently developed model of urban scaling, we give a microscopic model of voter behavior in which we replace diversity characterizing humans in creative aspects with social diversity and tolerance. The model can also predict new political developments such as the fragmentation of the left and the immigration paradox.

#### Introduction

Formation of cities is the result of socio-economic advantages of concentrating human populations in space outpacing associated costs. Urban agglomeration effects are systematic changes in socio-economic performance, innovation, trade and infrastructure characteristics of all cities as functions of their size. A variety of disciplines including economics [1-3], geography [4, 5], engineering [6] and complex systems [7-9] explain the existence of agglomeration or scaling effects and relate macroscopic properties of a city to its scale (population size). Such relations are known across the sciences as scaling relations [10], and the systematic study of such relationships in cities is known as urban scaling [11-14]. Using the population N as the measure of city size, power law scaling takes the form

$$Y = Y_0 \cdot N^{\beta},\tag{1}$$

where Y can denote material resources such as energy or infrastructure or measures of social activity such as wealth, patents and pollution;  $Y_0$  is a normalization constant. The exponent  $\beta$  reflects general dynamic rules at play across the urban system. Similar scale-free, fractal-like behavior has been observed in many human social networks [15] including cities [16]. Therefore, it is natural and compelling that the essential features of a quantitative, predictive theory of cities originate in the dynamics and structure of social [17, 18] and infrastructural networks [19], and that these underlie the observed scaling relations and the values of the exponents

<span id="page-1-0"></span>![](_page_1_Picture_1.jpeg)

**Competing interests:** E. B. received a scholarship from Ericsson throughout the research. This does not alter our adherence to PLOS ONE policies on sharing data and materials.

[20–22]. In the case of innovation [23], scaling has been related to the long-distance ties that are prevalent in a higher proportion when a larger population provides the potential for productive social interactions.

Most urban socioeconomic indicators have superlinear  $\beta>1$  exponents and as a result, larger cities are disproportionally the centers of innovation and wealth. Sublinear scaling  $\beta<1$  characterizes material quantities displaying economies of scale associated with infrastructure, where the agglomeration into cities pays off in having to provide fewer roads, shorter cables etc. Thus, material costs related to living in larger cities is disproportionally low. Linear scaling  $\beta\approx1$  is usually associated with individual human needs such as jobs, housing or water consumption [14].

Gomez-Lievano, Patterson-Lomba and Hausmann in Ref. [24] recently proposed a new model (GLPLH model) of superlinear scaling and demonstrated its validity on 43 urban phenomena related to employment, innovation, crime, education and diseases. The model accounts for the difference in scaling exponents and average prevalence across phenomena as well as for the difference in the variance within phenomena across cities of similar size. The central idea is that a number M of necessary complementary factors must simultaneously be present for an urban phenomenon to occur. For example, to get a patent at least the following six factors should be present: have a technological problem, have a solution, present the idea clearly, apply for a patent, include subsequent corrections from examiners, and satisfy all the legal requirements.

The fraction of factors that an individual does not have and is expected to require from the city in order to be counted into a phenomenon is  $q \in (0, 1)$ , and it quantifies the complexity of that phenomenon. The fraction of factors that a city provides for an individual is  $r \in (0, 1)$ . It represents a measure of urban diversity and tends to accumulate logarithmically  $r = a + b \cdot \log N$  with the population size, where a and b has been found to be constant across a wide range of urban phenomena. Alternatively, the fraction of factors not present in a city is  $1 - r = b \cdot \log N_0/N$ , where  $\log N_0 = (1 - a)/b$ , and  $N_0 \approx 1.8 \cdot 10^{14}$  is a hypothetical maximal diversity attainable in a city. Given a city with m factors present, the probability that an individual requires any number of the m factors that the city has, but none of the M - m factors that the city does not have is  $P = (1 - q)^{M - m} \approx e^{q(M - m)}$  for  $q \ll 1$ , and the average number of occurrence of the phenomena is  $Y = N\langle P \rangle_N$ , yielding  $Y \approx Ne^{qM(1 - r(N))} = Ne^{qMb \log N_0/N}$  where we used  $\langle e^{-qm} \rangle_N \approx e^{-Mr(N)}$  and averaging goes for cities of population N. Introducing the the scaling exponent  $\beta = 1 + Mbq$ , this scaling curve then takes the universal form

$$Y = N_0 \left(\frac{N}{N_0}\right)^{\beta},\tag{2}$$

where *N* is now the part of population conceivably susceptible to the given urban phenomena. Scaling laws and universality have been observed in various aspects of the political process and elections [25–31], that can be even used to detect election anomalies [32]. In the last decade complex systems-based approaches via social contagion theory has been developed [33–39] for understanding scaling in election data. Here, we concentrate on the phenomenological aspects of the observed scaling only, and don't study the detailed mechanism behind the process.

In the recent presidential elections in the US it has been noticed that votes for Democrats were disproportionally high in large cities [40], and in the UK major cities also voted to remain in the EU. While this phenomenon can be understood int he context of social contagion, where larger cities are shown to facilitate opinion spreading due to network effect [39], the exact statistical properties of the dependence of the votes on city size can be better explained

<span id="page-2-0"></span>![](_page_2_Picture_1.jpeg)

through scaling laws. Here we show that election data in the US and the referendum votes in the UK show strong evidence of urban scaling. Moreover, in the US, the scaling curves follow a hidden rule, a single parameter family of scaling curves, for both parties and for all the elections in the investigated period of almost 70 years. Using the concept that tolerance and diversity are strongly coupled in cities [[41\]](#page-9-0), we develop a microscopic model of voter behavior which produces the macroscopic level urban scaling, explains the observed single parameter scaling, and describes the distribution of deviations from the macroscopic curve. The new model can even explain unexpected voter behaviors like the immigration paradox in Britain, that is, communities that had the fewest recent immigrants from the EU were the most likely in wanting to leave the EU [[42](#page-10-0)].

## **Results and discussion**

First, we analyze data for the votes cast for the two main political parties in urban areas in all post-World War II US presidential elections [[43](#page-10-0)] and in the UK EU referendum [\[44\]](#page-10-0) (see Sections A-B in S1 [File](#page-7-0) for method details). In Fig 1A we show votes for the political options as a function of voter turnout for the 912 largest Metropolitan and Micropolitan Statistical Areas representing about 82% of the total voter population for the 2016 presidential election in the US. Fig 1B shows the votes as a function of voter turnout for the Remain and Leave opinions in the 2016 EU referendum for the urban electoral districts of the UK. The votes for Democrats and Remain in the EU scale superlinearly with exponents *β<sup>D</sup>* 1.14 and *βrem* 1.09, while votes for Republicans and Leave the EU follow sublinear scaling with *β<sup>R</sup>* 0.92 and *βlea* 0.91, with high regression coefficients *R*<sup>2</sup> 0.9 indicating robust urban scaling. While the elections took place in two different political situations, nevertheless they show very similar exponents.

In [Fig](#page-3-0) 2 we show the historical record of scaling exponents of the Democrats *β<sup>D</sup>* and of the Republicans *β<sup>R</sup>* for the 18 presidential elections in the period 1948–2016. The exponent of the Democrats has an increasing, while the exponent of the Republicans a decreasing historical trend. The Democrat and Republican curves roughly mirror each other in the whole period.

![](_page_2_Figure_6.jpeg)

**Fig 1. Urban scaling in the presidential elections in the US and in the EU referendum in the UK.** Best OLS fit line slopes *β* and regression coefficients *R*<sup>2</sup> are in the insets (see Section B in S1 [File](#page-7-0) for method details). **A** Doubly logarithmic plot of votes cast for Republicans (red) and Democrats (blue) as the function of the voter turnout for the 912 largest Metropolitan and Micropolitan Statistical Areas of the US in 2016. **B** Doubly logarithmic plot of votes cast for Leave (red) and Remain (blue) as the function of the voter turnout for UK urban electoral districts (see Section B in S1 [File](#page-7-0) for method details).

<https://doi.org/10.1371/journal.pone.0192913.g001>

<span id="page-3-0"></span>![](_page_3_Picture_1.jpeg)

![](_page_3_Figure_2.jpeg)

Fig 2. Scaling exponents for the Republicans (red) and Democrats (blue) with error bars for the 18 presidential elections of the US from 1948 to 2016.

https://doi.org/10.1371/journal.pone.0192913.g002

The relation of the two exponents becomes apparent when we plot the Republican exponent as a function of the Democrat exponent in Fig 3A.

For each election and for each party we can determine the scaling exponent  $\beta$  and the constant  $Y_0$  independently from the fits. In Fig 3B we plot log  $Y_0$  as a function of  $\beta$ . We find a very strong ( $R^2 = 0.96$ ) linear relation

$$\log Y_0 = -\alpha \beta + \delta, \tag{3}$$

for both parties and for all elections, with  $\alpha$  = 12.111 and  $\delta$  = 11.396. This indicates that the form of the scaling relation is independent of the party and election and has the universal form

$$Y = e^{\delta - \alpha} N^* \left(\frac{N}{N^*}\right)^{\beta} \approx \frac{1}{2} N^* \left(\frac{N}{N^*}\right)^{\beta}, \tag{4}$$

where *N* is the voter turnout in a city,  $\beta$  is the exponent of the party and  $\log N^* = \alpha$ . The

<span id="page-4-0"></span>![](_page_4_Figure_2.jpeg)

Fig 3. Interrelation of the parameters of urban scaling in US elections. A Urban scaling exponents of Republicans as a function of the Democrats for 18 US presidential elections from 1948 to 2016 (dots) and the theoretical curve (red line) derived from probability conservation (5). **B** Intercepts of the scaling relations log  $Y_0$  as a function of the scaling exponent β for Republicans (red) and Democrats (blue) for presidential elections in the period 1948–2016. Fitted line (3) with parameters and regression coefficient in the inset.

https://doi.org/10.1371/journal.pone.0192913.g003

numerical factor  $e^{\delta - \alpha}$  is equal to 1/2 within numerical error and the parameter  $N^* \approx 182,000$  is the average turnout of a US city of total population 429,000 in 2016. This is about the size of Fort Wayne IN, the 125th Metropolitan Statistical Area of the US.

The remarkable property of this scaling relation is that in average at turnout  $N = N^*$  the parties share the votes equally ( $Y_D = Y_R = N^*/2$ ) independent of their exponents  $\beta_D$  and  $\beta_R$  or of the year of the election and unaffected by historic changes in population. For cities above turnout  $N^*$  the party with higher  $\beta$  gets the majority of votes, while below this turnout the party with smaller  $\beta$  succeeds in average. While in 2016 already 125 metropolitan areas surpassed the population corresponding to this critical turnout, only 45 did so in 1948.

The observed linear relationship (3) and the single parameter form (4) of the scaling curve is predicted by the GLPLH model, therefore, it is reasonable to assume that it can be adapted to the election process. Formally, we recover our scaling curve (4) from this theory by identifying the susceptible population with half of the voter turnout N/2 and by setting  $N_0 = N^*/2$ . There are two discrepancies between our scaling curve (4) and that of the GLPLH model. The GLPLH model is applicable for superlinear  $\beta > 1$  (Mq > 0) values only, while in case of elections both superlinear and sublinear exponents arise, and the numerical value of  $N_0 \approx 1.8 \cdot 10^5$  is nine orders of magnitude smaller for elections.

The main difference of elections from other urban phenomena is that the scaling curves influence each other via the competition for votes. This competition is expressed mathematically by the probability conservation  $Y_D/N + Y_R/N = 1$  for the sum of the fraction of votes the parties get. Using (4) and averaging for all cities yields

$$\frac{1}{2} \left\langle (N/N^*)^{\beta_D - 1} \right\rangle + \frac{1}{2} \left\langle (N/N^*)^{\beta_R - 1} \right\rangle = 1. \tag{5}$$

This equation guarantees that one of the exponents will be superlinear while the other sublinear (see Section D in S1 File for details). Its numerical solution is shown in Fig 3A. Since we can determine the scaling exponent of one of the parties from the other, a single parameter, the scaling exponent of one of the parties, fully determines the urban scaling curves for both

<span id="page-5-0"></span>![](_page_5_Picture_1.jpeg)

parties. Accordingly, only one of the scaling exponents needs a detailed explanation. A model derived for the results of one of the parties will determine the results of the other party via probability conservation. The strategy of one of the parties will result in a superlinear exponent, which can be explained by an adaptation of the GLPLH model, while the result of the party with the sublinear exponent is just a consequence of the other party's strategy and the probability conservation law. The explanation of a strategy that results in a superlinear scaling follows later.

Next, we analyze the results in the period 2000–2016, where the Democratic party has a pronounced superlinear scaling, and the Republican party a sublinear scaling. We show that the statistical distribution of the results for Democrats is in accordance with the GLPLH model, while the distribution of the votes for Republicans deviates from it and is merely the consequence of probability conservation. We note here, that while our fits show a superlinear scaling for the Republican party before 1960, the *R*<sup>2</sup> -values of these fits are not as reliable as that of the more recent ones, and therefore, we will continue our analysis of superlinear processes and of the model only for the aforementioned years.

A Scale-Adjusted Metropolitan Indicator [[13](#page-8-0), [45](#page-10-0)–[48](#page-10-0)] (SAMI) is the logarithmic deviation of the value *Yi* from the average scaling curve for a city with population *Ni*

$$\xi_i = \log Y_i - \log Y_0 - \beta \log N_i. \tag{6}$$

The articles [[13](#page-8-0), [46](#page-10-0)] predict that SAMIs for a given city size range are normally distributed if the investigated measure obeys the urban scaling laws. The GLPLH model states that the SAMI variance can be expressed with the former complexity parameter *q* and the number of complementary factors *M* as s<sup>2</sup> *SAMI* ¼ *q*<sup>2</sup> *Mb*ðlog*N*<sup>0</sup> hlog*N*iÞ*;* where hlog *N*i is the mean of the logarithm of city sizes. It can also be expressed with the scaling exponent

$$\sigma_{SAMI}^2 = q(\beta - 1)(\log N_0 - \langle \log N \rangle). \tag{7}$$

In [Fig](#page-6-0) 4 we check the general validity of this formula for both parties and for all elections in the 1948–2016 period. For the variance averaged over all metropolitan areas, though the data is noisy, we cannot reject the notion of proportionality with *β* − 1 (see inset of [Fig](#page-6-0) 4A), indicating also that the complexity parameter *q* is approximately constant over several elections. From the fitted line and from the numerical value hlog *N*i = 10.55 for the 2016 election, we get *q* 0.28. Then, in the 2000–2016 period for the superlinearly scaling results of the Democrats, we can make a more detailed calculation for ten windows of city sizes. In [Fig](#page-6-0) 4A (main) we can see that curves of s<sup>2</sup> *SAMI=*ðb 1Þ for different elections in these windows collapse onto the same curve. While for low city sizes the linear relationship expected after the data collapse does not fit well, for greater city sizes, where statistical errors are lower, the collapse confirms that the complexity parameter is constant. This implies that the change of the scaling exponent *β<sup>D</sup>* for the Democrats in this period comes solely from the change of the number of complementary factors *M*.

Deviations of cities from the average scaling curves can then be standardized in the windows using the window-wise variances. In [Fig](#page-6-0) 4B we show the distribution of these standardized SAMIs for both parties. The distribution of these standardized SAMIs for Democratic party is standard Gaussian, in agreement with the SAMI literature [\[13,](#page-8-0) [46\]](#page-10-0). However, the same procedure results in a skewed distribution for the Republicans. Their rescaled SAMI distribution is not normal and the GLPLH model doesn't apply. This also confirms that two parties don't have an equal role in the coupled urban scaling phenomenon.

Now, the question arises, what the necessary complementary factors in the context of elections are that must simultaneously be present in order to vote for Democrats in the 1988–2016

<span id="page-6-0"></span>![](_page_6_Picture_1.jpeg)

![](_page_6_Figure_2.jpeg)

**[Fig](#page-5-0) 4. Fluctuations around the average scaling curve. A**, Variance of the deviation from the average scaling curve as a function of the logarithmic city size, measured in voter turnout. City sizes are binned into 20 windows of uniform sizes on logarithmic scale. In the inset, standard deviation of SAMIs ([6\)](#page-5-0) for all metropolitan areas in our study as a function *β* − 1. Best fit line parameters are in the inset. **B**, Standardized deviation of SAMIs for the last five US presidential elections. Lower panel: Scatter plot for the Democrat (left) and Republican (right) standardized deviations (horizontal axis) and logarithmic city size (vertical axis). Upper panel: Distribution of the standardized deviations. For the Democrats (left) it is a standard normal distribution (solid line). For Republicans (right) it is a skewed distribution deviating from the standard normal distribution (solid line). We used the Kolmogorov-Smirnov test to check the normality of the distributions at a significance level of 5% (see Section G in S1 [File](#page-7-0) for details).

<https://doi.org/10.1371/journal.pone.0192913.g004>

period, where their exponent is superlinear? These factors can be best understood in the terms of issue voting, where voters choose a candidate or an opinion by comparing their own viewpoints in different political issues to that of the voted one [\[49–51](#page-10-0)].

We found that the complexity parameter *q* is approximately constant. Thus, from the 4–6 times growth of *β<sup>D</sup>* − 1 in this period we can conclude that the number of issues *M* got multiplicated about 4–6 times. The concrete value of *M* cannot be determined from our data, only the product *bM* that changed from about 0.09 to 0.52 with *b* being constant. If we could find these factors, then Republicans (or the Leave campaign) could be characterized as comprising of those voters, who don't accept at least one of those *M* issues that are necessary for a voter voting for the superlinearly scaling opinion or party.

Here, we can just conjecture based on the agenda of Democrats, that these are liberal values in general, and the Democrat voter typically accepts all of these *M* values or issues simultaneously. Such values include tolerance and acceptance towards various social groups ranging from women and blacks at the beginning and middle of the 20th century to LGBT communities, immigrants, refugees and various other social minorities recently. In case someone is not able to accept at least one of these, then he or she will probably not vote for the Democrats. That explains why groups of the Republican and the Leave voters look so heterogeneous: they consist of groups that oppose at least one of these liberal values, and that are not held together by a common political agenda otherwise. This also explains the recent steady increase of the Democrat exponent: as more and more *M* values are introduced, it increases the exponent, making bigger cities having disproportionally more Democrats than smaller ones. This result is in line with the findings of [\[39\]](#page-9-0), who explain the same phenomenon via the increasing impact of social contagion in the more populated areas of the United States.

In this context, we can identify *q* as a probability that a voter—left on its own devices rejects one of the *M* liberal values, and *r*(*N*) is the probability that a city of size *N* makes a voter

<span id="page-7-0"></span>![](_page_7_Picture_1.jpeg)

tolerant towards those values. Social diversity grows with the city size and voters in cities can face an increasing number of social issues and can develop tolerance towards them. This is in accordance with the immigration paradox in Britain, where voters living near immigrants develop a tolerance, while those who do not are more likely to reject them [42]. Therefore, we expect that just like other types of diversities in cities, tolerance grows like  $r(N) \sim \log N/N_0$ , but the number of maximal social diversity is reached at  $N_0 \approx 4 \cdot 10^5$ , which is smaller than the diversity  $N^* \approx 1.8 \cdot 10^{14}$  observed for the more general type of diversity, characterizing humans in creative aspects. Finally, there is one more consequence of this model: as the number of liberal values M seems to grow continuously, the potential voters who don't accept one of them also increases, and becomes detrimental for electoral success. This leads to the fragmentation of the political left, since a larger number of smaller parties accepting only a subset of the M values, or even "single-issue" parties can minimize the number of estranged voters and maximize the aggregated votes of all these parties.

### Conclusion

We applied urban scaling theory to the number of votes cast in the Metropolitan and Micropolitan Statistcal Areas in the 1948-2016 presidential elections of the US and the votes cast in the urban areas of the 2016 EU referendum in the UK. We found that out of the two voting options (Democrat/Republican, Remain/Leave), one always follows a superlinear, while the other a sublinear scaling. Using the historical dataset, we showed that instead of four parameters (two for both scaling fits), the single exponent of the superlinearly scaling party is enough to characterize all processes across the elections and the parties. We derived the other exponent from the superlinear exponent by using the conservation of voting probabilities, and showed that the city turnout distribution determines that this other exponent must be sublinear. We then analyzed the fluctuations around the scaling curve distributions and found that the distribution corresponding to the superlinear exponent is lognormal. We concluded that the two parties play different roles in urban scaling. The party with superlinear exponent drives the process, while the scaling of the party with the sublinear exponent is merely the result of probability conservation. In the context of elections we identified the the elements of the GLPLH model and showed that social tolerance and diversity replaces creative diversity in this context. We pointed to new political consequences of the model. We believe that he model and the calculations could further be extended to metropolitan areas in other countries or to electoral systems with multiple choices.

## **Materials and methods**

See Sections A-G in S1 File for details.

## **Supporting information**

**S1 File. Detailed materials and methods.** The file contains detailed description of the data sources, fitting procedures (power laws and the Kolmogorov-Smirnov test) and calculations. (PDF)

#### **Author Contributions**

Conceptualization: Eszter Bokányi, Zoltán Szállási, Gábor Vattay.

**Data curation:** Eszter Bokányi, Zoltán Szállási, Gábor Vattay.

Formal analysis: Eszter Bokányi, Zoltán Szállási, Gábor Vattay.

<span id="page-8-0"></span>![](_page_8_Picture_1.jpeg)

**Funding acquisition:** Ga´bor Vattay.

**Investigation:** Eszter Boka´nyi, Zolta´n Sza´lla´si, Ga´bor Vattay. **Methodology:** Eszter Boka´nyi, Zolta´n Sza´lla´si, Ga´bor Vattay.

**Project administration:** Ga´bor Vattay. **Resources:** Zolta´n Sza´lla´si, Ga´bor Vattay. **Software:** Eszter Boka´nyi, Ga´bor Vattay. **Supervision:** Zolta´n Sza´lla´si, Ga´bor Vattay. **Validation:** Zolta´n Sza´lla´si, Ga´bor Vattay.

**Visualization:** Eszter Boka´nyi.

**Writing – original draft:** Eszter Boka´nyi, Ga´bor Vattay.

**Writing – review & editing:** Eszter Boka´nyi.

## **References**

- **[1](#page-0-0).** Henderson JV. Urban Development: Theory, Fact, and Illusion. No. 9780195069020 in OUP Catalogue. Oxford University Press; 1991.
- **2.** Fujita M, Krugman P, Venables AJ. The Spatial Economy: Cities, Regions, and International Trade. MIT Press Books. 2001;1.
- **[3](#page-0-0).** Glaeser E. Triumph of the City: How Our Greatest Invention Makes Us Richer, Smarter, Greener, Healthier, and Happier. Penguin; 2011.
- **[4](#page-0-0).** Batty M. The size, scale, and shape of cities. Science. 2008; 319(5864):769–771. [https://doi.org/10.](https://doi.org/10.1126/science.1151419) [1126/science.1151419](https://doi.org/10.1126/science.1151419) PMID: [18258906](http://www.ncbi.nlm.nih.gov/pubmed/18258906)
- **[5](#page-0-0).** Isard W. Location and space-economy: a general theory relating to industrial location, market areas, land use, trade amd urban structure. Massachusetts Institute of Technology; 1972.
- **[6](#page-0-0).** Kennedy C. The evolution of great world cities: Urban wealth and economic growth. University of Toronto Press; 2011.
- **[7](#page-0-0).** Bettencourt LM, Lobo J, Helbing D, Ku¨hnert C, West GB. Growth, innovation, scaling, and the pace of life in cities. Proceedings of the national academy of sciences. 2007; 104(17):7301–7306. [https://doi.](https://doi.org/10.1073/pnas.0610172104) [org/10.1073/pnas.0610172104](https://doi.org/10.1073/pnas.0610172104)
- **8.** Bettencourt LM. The origins of scaling in cities. Science. 2013; 340(6139):1438–1441. [https://doi.org/](https://doi.org/10.1126/science.1235823) [10.1126/science.1235823](https://doi.org/10.1126/science.1235823) PMID: [23788793](http://www.ncbi.nlm.nih.gov/pubmed/23788793)
- **[9](#page-0-0).** Schla¨pfer M, Bettencourt LM, Grauwin S, Raschke M, Claxton R, Smoreda Z, et al. The scaling of human interactions with city size. Journal of the Royal Society Interface. 2014; 11(98):20130789. <https://doi.org/10.1098/rsif.2013.0789>
- **[10](#page-0-0).** Mitzenmacher M. A brief history of generative models for power law and lognormal distributions. Internet mathematics. 2004; 1(2):226–251. <https://doi.org/10.1080/15427951.2004.10129088>
- **[11](#page-0-0).** Pumain D, Paulus F, Vacchiani-Marcuzzo C, Lobo J. An evolutionary theory for interpreting urban scaling laws. Cybergeo. 2006; 2006:1–20.
- **12.** Bettencourt L, West G. A unified theory of urban living. Nature. 2010; 467(7318):912–913. [https://doi.](https://doi.org/10.1038/467912a) [org/10.1038/467912a](https://doi.org/10.1038/467912a) PMID: [20962823](http://www.ncbi.nlm.nih.gov/pubmed/20962823)
- **[13](#page-5-0).** Gomez-Lievano A, Youn H, Bettencourt LMA. The statistics of urban scaling and their connection to Zipf's law. PLoS ONE. 2012; 7(7). <https://doi.org/10.1371/journal.pone.0040393> PMID: [22815745](http://www.ncbi.nlm.nih.gov/pubmed/22815745)
- **[14](#page-0-0).** Bettencourt LMA, Lobo J, Youn H. The hypothesis of urban scaling: formalization, implications and challenges. SFI Working Paper. 2013;2013-01-00:37.
- **[15](#page-0-0).** Newman M, Barabasi AL, Watts DJ. The structure and dynamics of networks. Princeton University Press; 2011.
- **[16](#page-0-0).** Batty M. Cities and complexity: understanding cities with cellular automata, agent-based models, and fractals. The MIT press; 2007.
- **[17](#page-0-0).** Fischer CS. To dwell among friends: Personal networks in town and city. University of chicago Press; 1982.

<span id="page-9-0"></span>![](_page_9_Picture_1.jpeg)

- **[18](#page-0-0).** Wellman B. Networks in the global village. Westview Press, Boulder CO; 1999.
- **[19](#page-0-0).** Samaniego H, Moses ME. Cities as organisms: Allometric scaling of urban road networks. Journal of Transport and Land use. 2008; 1(1). <https://doi.org/10.5198/jtlu.v1i1.29>
- **[20](#page-0-0).** Arbesman S, Christakis NA. Scaling of prosocial behavior in cities. Physica A: Statistical Mechanics and its Applications. 2011; 390(11):2155–2159. <https://doi.org/10.1016/j.physa.2011.02.013> PMID: [22639486](http://www.ncbi.nlm.nih.gov/pubmed/22639486)
- **21.** Pan W, Ghoshal G, Krumme C, Cebrian M, Pentland A. Urban characteristics attributable to densitydriven tie formation. Nature communications. 2013; 4. <https://doi.org/10.1038/ncomms2961>
- **[22](#page-0-0).** Sim A, Yaliraki SN, Barahona M, Stumpf MP. Great cities look small. Journal of The Royal Society Interface. 2015; 12(109):20150315. <https://doi.org/10.1098/rsif.2015.0315>
- **[23](#page-1-0).** Arbesman S, Kleinberg JM, Strogatz SH. Superlinear scaling for innovation in cities. Physical Review E. 2009; 79(1):016115. <https://doi.org/10.1103/PhysRevE.79.016115>
- **[24](#page-1-0).** Gomez-Lievano A, Patterson-Lomba O, Hausmann R. Explaining the prevalence, scaling and variance of urban phenomena. Nature Human Behaviour. 2016; 1:0012. [https://doi.org/10.1038/s41562-016-](https://doi.org/10.1038/s41562-016-0012) [0012](https://doi.org/10.1038/s41562-016-0012)
- **[25](#page-1-0).** Filho RNC, Almeida MP, Andrade JS, Moreira JE. Scaling behavior in a proportional voting process. Physical Review E. 1999; 60(1):1067–1068. <https://doi.org/10.1103/PhysRevE.60.1067>
- **26.** Costa Filho RN, Almeida MP, Moreira JE, Andrade JS. Brazilian elections: Voting for a scaling democracy. Physica A: Statistical Mechanics and its Applications. 2003; 322:698–700. [https://doi.org/10.](https://doi.org/10.1016/S0378-4371(02)01823-X) [1016/S0378-4371\(02\)01823-X](https://doi.org/10.1016/S0378-4371(02)01823-X)
- **27.** Lyra ML, Costa UMS, Filho RNC, Andrade JS Jr. Generalized Zipf's Law in proportional voting processes. Europhysics Letters. 2002; 62(1):5.
- **28.** Fortunato S, Castellano C. Scaling and Universality in Proportional Elections. Physical Review Letters. 2007; 99(13):138701. <https://doi.org/10.1103/PhysRevLett.99.138701> PMID: [17930647](http://www.ncbi.nlm.nih.gov/pubmed/17930647)
- **29.** Mantovani MC, Ribeiro HV, Moro MV, Picoli S, Mendes RS. Scaling laws and universality in the choice of election candidates. EPL (Europhysics Letters). 2011; 96(4):48001. [https://doi.org/10.1209/0295-](https://doi.org/10.1209/0295-5075/96/48001) [5075/96/48001](https://doi.org/10.1209/0295-5075/96/48001)
- **30.** Mantovani MC, Ribeiro HV, Lenzi EK, Picoli S, Mendes RS. Engagement in the electoral processes: Scaling laws and the role of political positions. Physical Review E—Statistical, Nonlinear, and Soft Matter Physics. 2013; 88(2).
- **[31](#page-1-0).** Chatterjee A, Mitrović M, Fortunato S. Universality in voting behavior: an empirical analysis. Scientific Reports. 2013; 3:1049. <https://doi.org/10.1038/srep01049> PMID: [23308342](http://www.ncbi.nlm.nih.gov/pubmed/23308342)
- **[32](#page-1-0).** Klimek P, Yegorov Y, Hanel R, Thurner S. Statistical detection of systematic election irregularities. Proceedings of the National Academy of Sciences. 2012; 109(41):16469–16473. [https://doi.org/10.1073/](https://doi.org/10.1073/pnas.1210722109) [pnas.1210722109](https://doi.org/10.1073/pnas.1210722109)
- **[33](#page-1-0).** Bernardes AT, Stauffer D, Kerte´sz J. Election results and the Sznajd model on Barabasi network. The European Physical Journal B—Condensed Matter. 2002; 25(1):123–127.
- **34.** Arau´jo NAM, Andrade JS, Herrmann HJ. Tactical voting in plurality elections. PLoS ONE. 2010; 5(9):1– 5.
- **35.** Borghesi C, Bouchaud JP. Spatial correlations in vote statistics: a diffusive field model for decision-making. The European Physical Journal B. 2010; 75(3):395–404. [https://doi.org/10.1140/epjb/e2010-](https://doi.org/10.1140/epjb/e2010-00151-1) [00151-1](https://doi.org/10.1140/epjb/e2010-00151-1)
- **36.** Palombi F, Toti S. Stochastic Dynamics of the Multi-State Voter Model Over a Network Based on Interacting Cliques and Zealot Candidates. Journal of Statistical Physics. 2014; 156(2):336–367. [https://doi.](https://doi.org/10.1007/s10955-014-1003-1) [org/10.1007/s10955-014-1003-1](https://doi.org/10.1007/s10955-014-1003-1)
- **37.** Ferna´ndez-Gracia J, Suchecki K, Ramasco JJ, San Miguel M, Eguı´luz VM. Is the Voter Model a Model for Voters? Physical Review Letters. 2014; 112(15):158701. [https://doi.org/10.1103/PhysRevLett.112.](https://doi.org/10.1103/PhysRevLett.112.158701) [158701](https://doi.org/10.1103/PhysRevLett.112.158701) PMID: [24785078](http://www.ncbi.nlm.nih.gov/pubmed/24785078)
- **38.** Borghesi C, Raynal JC, Bouchaud JP. Election turnout statistics in many countries: Similarities, differences, and a diffusive field model for decision-making. PLoS ONE. 2012; 7(5):1–12. [https://doi.org/10.](https://doi.org/10.1371/journal.pone.0036289) [1371/journal.pone.0036289](https://doi.org/10.1371/journal.pone.0036289)
- **[39](#page-1-0).** Braha D, de Aguiar MAM. Voting contagion: Modeling and analysis of a century of U.S. presidential elections. PLOS ONE. 2017; 12(5):e0177970. <https://doi.org/10.1371/journal.pone.0177970> PMID: [28542409](http://www.ncbi.nlm.nih.gov/pubmed/28542409)
- **[40](#page-1-0).** Florida R. Mapping How America's Metro Areas Voted: The geography of the 2016 election is spiky. The Atlantic Citylab, [http://www.citylab.com/politics/2016/12/mapping-how-americas-metro-areas](http://www.citylab.com/politics/2016/12/mapping-how-americas-metro-areas-voted/508313/)[voted/508313/](http://www.citylab.com/politics/2016/12/mapping-how-americas-metro-areas-voted/508313/); 2016.
- **[41](#page-2-0).** Florida R. The Rise of the Creative Class—Revisited: Revised and Expanded. Basic books; 2014.

<span id="page-10-0"></span>![](_page_10_Picture_1.jpeg)

- **[42](#page-2-0).** Goodwin MJ, Heath O. The 2016 Referendum, Brexit and the Left Behind: An Aggregate-level Analysis of the Result. The Political Quarterly. 2016; 87(3):323–332. <https://doi.org/10.1111/1467-923X.12285>
- **[43](#page-2-0).** Leip D. Dave Leip U.S. Presidential General County Election Results. Harvard Dataverse; 2016. Available from: <http://dx.doi.org/10.7910/DVN/SUCQ52>.
- **[44](#page-2-0).** EU referendum results, The Electoral Commission (UK); Date accessed: 2017-02-09. [http://www.](http://www.electoralcommission.org.uk) [electoralcommission.org.uk.](http://www.electoralcommission.org.uk)
- **[45](#page-5-0).** Bettencourt LM, Lobo J, Strumsky D, West GB. Urban scaling and its deviations: Revealing the structure of wealth, innovation and crime across cities. PloS one. 2010; 5(11):e13541. [https://doi.org/10.](https://doi.org/10.1371/journal.pone.0013541) [1371/journal.pone.0013541](https://doi.org/10.1371/journal.pone.0013541) PMID: [21085659](http://www.ncbi.nlm.nih.gov/pubmed/21085659)
- **[46](#page-5-0).** Alves LGA, Ribeiro HV, Lenzi EK, Mendes RS. Distance to the Scaling Law: A Useful Approach for Unveiling Relationships between Crime and Urban Metrics. PLoS ONE. 2013; 8(8):e69580. [https://doi.](https://doi.org/10.1371/journal.pone.0069580) [org/10.1371/journal.pone.0069580](https://doi.org/10.1371/journal.pone.0069580) PMID: [23940525](http://www.ncbi.nlm.nih.gov/pubmed/23940525)
- **47.** Lobo J, Bettencourt LMA, Strumsky D, West GB. Urban Scaling and the Production Function for Cities. PLoS ONE. 2013; 8(3):e58407. <https://doi.org/10.1371/journal.pone.0058407> PMID: [23544042](http://www.ncbi.nlm.nih.gov/pubmed/23544042)
- **[48](#page-5-0).** Alves LGA, Mendes RS, Lenzi EK, Ribeiro HV. Scale-Adjusted Metrics for Predicting the Evolution of Urban Indicators and Quantifying the Performance of Cities. PLOS ONE. 2015; 10(9):e0134862. <https://doi.org/10.1371/journal.pone.0134862> PMID: [26356081](http://www.ncbi.nlm.nih.gov/pubmed/26356081)
- **[49](#page-6-0).** Rabinowitz G, Macdonald SE. A Directional Theory of Issue Voting. The American Political Science Review. 1989; 83(1):93–121. <https://doi.org/10.2307/1956436>
- **50.** Denver D, Hands G. Issues, principles or ideology? How young voters decide. Electoral Studies. 1990; 9(1):19–36. [https://doi.org/10.1016/0261-3794\(90\)90039-B](https://doi.org/10.1016/0261-3794(90)90039-B)
- **[51](#page-6-0).** McCarthy N, Poole KT. Polarized America. The Dance of Ideology and Unequal Riches. Rassegna Italiana di Sociologia. 2008; 49(2):495–497.