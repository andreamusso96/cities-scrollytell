
\begin{document}

\title[Large cities lose their growth advantage as countries urbanize]{Large cities lose their growth advantage countries urbanize}


\author[1,2]{\fnm{Andrea} \sur{Musso}}\email{andrea.musso@gess.ethz.ch}

\author[2,3]{\fnm{Diego} \sur{Rybski}}\email{ca-dr@rybski.de}

\author[1,2]{\fnm{Dirk} \sur{Helbing}}\email{dirk.helbing@gess.ethz.ch}

\author[2]{\fnm{Frank} \sur{Neffke}}\email{neffke@csh.ac.at}

\affil[1]{\orgdiv{Computational Social Science}, \orgname{ETH Zurich}, \orgaddress{\city{Zurich}, \postcode{8006}, \country{Switzerland}}}
\affil[2]{\orgdiv{Complexity Science Hub Vienna}, \orgaddress{\city{Vienna}, \postcode{1030}, \country{Austria}}}
\affil[3]{\orgdiv{Leibniz Institute of Ecological Urban and Regional Development}, \orgaddress{\city{Dresden}, \postcode{01217}, \country{Germany}}}

\abstract{\textbf{Abstract}: The share of the world population living in cities with more than one million people rose from 11\% in 1975 to 24\% in 2025 (our estimates). Will this trend towards greater concentration in large cities continue or level off? We introduce two new city population datasets that use consistent city definitions across countries and over time. The first covers the world between 1975 and 2025, using satellite imagery. The second covers the U.S. between 1850 and 2020, using census microdata. We find that urban growth follows a characteristic life cycle. Early in a country's urbanization, large cities grow faster than smaller ones. Later, growth rates equalize across sizes. We use this life cycle to project future population concentration in large cities. Our projections suggest that 38\% of the world population will be living in cities with more than one million people by 2100. This estimate is higher than the 33\% implied by the well-known theory of proportional growth but lower than the 42\% obtained by extrapolating current trends. \\

\textbf{Significance statement}: Will most people end up living in large cities? This depends on whether large cities tend to grow faster than small ones. Inconsistent city definitions have limited our understanding of this question. We construct two city population datasets with the same definition of city across countries and over time: a global dataset from satellite imagery (1975–2025) and a U.S. dataset from census microdata (1850–2020). We find that city growth follows a common pattern. Early in a country's urbanization, large cities grow fastest. Later, cities of all sizes grow at similar rates. Our projections based on this pattern suggest that the rise of large cities will slow down but not stop.}

\maketitle

\newpage
\linenumbers
\section{Introduction}
Over the past 50 years, the world population has become increasingly concentrated in large cities. Whether this concentration will continue depends on the relationship between a city's size and its growth rate, a topic on which the literature is divided.

Increasing returns theories, such as the New Economic Geography \cite{krugman1991increasing, fujita2001spatial} and the evolutionary approach of Pumain \textit{et al.} \cite{pumain2006evolutionary, paulus2004coevolution, pumain2012theorie}, argue that large cities tend to grow faster than small ones. Large cities are typically more innovative and productive \cite{bettencourt2007growtha, bettencourt2014professionala}, have more educated workforces \cite{combes2008spatial, keuschnigg2019urban}, sit more centrally in trade and knowledge networks \cite{pumain2012theorie}, and host more advanced economic activities \cite{balland2020complexa, gomez-lievano2016explainingb}. These factors can plausibly confer them a growth advantage. Based on our novel projection method, even a mild growth advantage---where a 10-fold increase in size corresponds to a 0.7\% increase in yearly growth---would result in $47\%$ of the world population living in 1M$+$ cities by the end of the century. 

Proportional growth theories argue instead that cities of all sizes tend to grow at similar rates (Gibrat's Law) \cite{sutton1997gibrats, eeckhout2004gibrats, eaton1997cities, gonzalez-val2014newa, henderson2007urbanizationa}. After all, scale also brings costs such as increased congestion \cite{louf2014how, barthelemy2016structure}, crime \cite{oliveira2017scaling, bettencourt2010urban}, disease risk  \cite{rocha2015nonlineara, bilal2021scaling}, and housing expenses \cite{sarkar2019urban, duranton2004chaptera}; and these costs may offset advantages. If city size exhibits no growth advantage, our projections suggest that $33\%$ of the world population will live in 1M$+$ cities in 2100. 

This 14 percentage point gap between the two predictions represents a difference of 1.4 billion people and thus has significant implications for future planning and development. In this paper, we analyze which of these two scenarios is more likely using two newly built city population datasets. The first dataset, built from satellite-derived grids \cite{schavina2023ghsl}, spans 1975-2025 and covers 99 countries, together representing 94\% of the world population. The second, built from census microdata \cite{ruggles2024ipums, manson2024ipums, berkes2023censusa}, spans 1850-2020 and covers the United States (USA) urban system over nearly its entire history. 

These datasets substantially extend the spatial and temporal coverage of previous efforts to build such harmonized data \cite{pumain2015multilevel}. Before the advent of satellite imagery and geospatial processing tools, assembling harmonized datasets of city sizes across countries and years was extremely difficult, primarily because national data collection efforts are not designed to produce outputs that are comparable across countries or consistent over time. As a result, most empirical studies of urban growth focused on just a handful of countries over limited time periods. The conclusions of these studies are varied, some supporting proportional growth \cite{eeckhout2004gibrats, eaton1997cities, gonzalez-val2014newa, henderson2007urbanizationa} and others not \cite{guerin-pace1995ranksizea, desmet2017settlementa, michaels2012urbanizationa, rozenfeld2008lawsa, black2003urban, soo2007zipfs}. Integrating these results has proved difficult due to substantial differences in methodology \cite{cottineau2017metazipf}, leaving us with an incomplete understanding of how urban growth evolves over time \cite{verbavatz2020growtha}.

Using these new datasets, we sharpen our understanding of temporal trends in urban growth. First, we show that proportional growth and increasing returns are better understood as two phases of the same underlying process, not competing realities. In the early phases of urbanization, large cities enjoy a strong growth advantage, consistent with increasing returns. As an urban system matures, this advantage weakens, and the growth rates of large and small cities converge, consistent with proportional growth. Second, we show that this size-growth relationship translates into systematic changes in the shape of a country's city-size distribution \cite{zipf1949humana, batty2006rank, rybski2023auerbach}. When large cities have a growth advantage, the distribution stretches and its rank-size slope (a spline-based analogue of the Zipf exponent \cite{saichev2010theory}) increases. Third, combining this mechanism and a novel projection method, we project that by 2100, 38\% of the world's population will live in 1M$+$ cities. This projection lies between the proportional-growth (33\%) and increasing-returns (47\%) benchmarks, and below an extrapolation of current trends (42\%).

\section{Results}

\begin{table}[]
    \centering
\begin{tabular*}{0.8\linewidth}{@{\extracolsep{\fill}}lccccc}
\\[-1.8ex]\hline\hline \\[-1.8ex]Dataset & City-year obs. & Countries & Frequency (years) & Time Period \\
\midrule
Global cities & 1,604,593 & 99 & 5 & $1975-2025$ \\
USA cities & 26,902 & 1 & 10 & $1850-2020$ \\
\hline\hline \\[-1.8ex]\end{tabular*}
    \caption{Description of the two large-scale city population datasets created for the analysis. The Global cities dataset covers 99 countries around the world (amounting to 94\% of the world population in 2025) between 1975 and 2025. Its primary source is the GHSL 2023 data package \cite{schavina2023ghsl}. The USA cities dataset covers the continental USA between 1850 and 2020. Its primary sources are IPUMS USA \cite{ruggles2024ipums}, IPUMS NHGIS \cite{manson2024ipums}, and the Census Place Project \cite{berkes2023censusa}.}
    \label{tab:1}
\end{table}

Our city population datasets (Table \ref{tab:1}) define ``cities'' geographically, as clusters of contiguous built-up areas or regions of high population density \cite{makse1995modelling, rozenfeld2008lawsa, arcaute2015constructing} (Methods \ref{methods:constructing_cities}). This definition has three main advantages: (i) it dynamically adjusts as urban areas expand; (ii) it is consistent across space and time, facilitating robust comparative analyzes; and (iii) it is unaffected by political boundary changes such as municipal mergers. The trade-off is that this definition captures morphological clusters rather than functional urban areas, so suburbs tied to large cities by commuting flows may appear as separate clusters (see SI 5 for further discussion).

\begin{figure}[ht!]
    \centering
    \includegraphics[width=0.95\textwidth]{figures/figure_1.png}
    \caption{The growth advantage of large cities varies systematically across regions: it is strong in Asia and Africa and weak in Europe and the Americas. \textbf{(A)} We compare the average growth rate of a country's cities, denoted by $g_{\text{national}}$, with the average growth rate of specific sub-groups of its cities (e.g., the largest city, 1M$+$ cities, etc.), denoted by $g_{\text{group}}$. Each bar in the chart shows the ratio $g_{\text{group}} \ / \ g_{\text{national}} - 1$ for a given region. \textbf{(B)} \emph{Size-growth curve} by region. These curves are obtained by fitting a penalized cubic B-spline ($\lambda = 100$) to the relationship between city log-size in year $t$ and city log-growth between year $t$ and $t + 10$ (Methods \ref{methods:measurement}). \textbf{(C)} \emph{Size-growth slopes} $\beta$ by country. $\beta$ is obtained by first estimating the national size-growth curve (as in panel (B)), and then averaging the local slope of this curve across the size spectrum (see left inset and Methods \ref{methods:measurement}). The map shows the mean value of $\beta$ between 1975 and 2025; hatched indicates no data. The right inset shows a kernel density estimate of the distribution of $\beta$ across countries (dotted-line = median).}
    \label{fig:1}
\end{figure}

Our analysis of these datasets reveals substantial global variation in urban growth patterns. Between 1975 and 2025, an average 1M$+$ city in Asia/Africa outgrew the national average by $\sim 7\%$ (Fig. \ref{fig:1}A). In contrast, Europe's large cities grew modestly faster than the rest (Fig. \ref{fig:1}A-B), and in the Americas, city growth displayed an inverted-U-shaped trend, with 1M$+$ cities growing 1.6\% slower than their national average (Fig. \ref{fig:1}A-B). 

These patterns are also visible at the country level. Figure \ref{fig:1}C maps national size-growth slopes, $\beta$ (definition in the caption of Figure \ref{fig:1}C). A positive $\beta$ indicates that growth increases with size, or, in other words, that large cities have a growth advantage. This growth advantage varies significantly across countries, with $\beta$ ranging from -0.02 to 0.1 (median $\approx 0.012$; Fig. \ref{fig:1}C inset). Notably, $\beta$s are generally higher in Asia and Africa and lower in Europe and the Americas.

\begin{figure}[ht!]
    \centering
    \includegraphics[width=0.95\textwidth]{figures/figure_2.png}
    \caption{The growth advantage of large cities weakens as countries urbanize. \textbf{(A)} Size-growth curve by urbanization group (Methods \ref{methods:measurement}) (Inset) $\beta$ vs. urban population share (fit with a penalized cubic B-spline with $\lambda = 100$). \textbf{(B-C)} Size-growth curves in South Korea and the USA across different time periods. (Insets) $\beta$ vs. time (bootstrapped confidence intervals $n = 1000$). \textbf{(D)} Country-level regression with regional dummies ($\beta_{t, \text{country}} \sim \delta_{\text{region}} + \text{urban population share}_{t, \text{country}}$). Regional differences in $\beta$ become significantly smaller once we control for the level of urbanization.}
    \label{fig:2}
\end{figure}

This regional divide can be understood as part of a universal dynamic in which the growth advantage of large cities weakens as a country's urban system matures. This inverse relationship is evident in both cross-sectional and longitudinal data (Fig. \ref{fig:2}).

Across countries, a lower national share of urban population correlates with higher $\beta$ (Fig. \ref{fig:2}A inset and Table \ref{tab:2}). Put differently, growth rates increase rapidly with city size in less urbanized countries, whereas the size-growth relationship is nearly flat in more urbanized ones (Fig. \ref{fig:2}A). The numbers speak clearly: between 1975 and 2025, 1M$+$ cities in more urbanized countries grew at the national average rate, while 1M$+$ cities in less urbanized ones grew 7.3\% faster.

Within countries, $\beta$ declines as urbanization rises. A regression with country fixed effects shows that a 20\% increase in a country's urban population share is associated with a $\sim 0.01$ reduction in $\beta$ (Table \ref{tab:2}). This pattern is clearly observed in South Korea and the USA, two countries for which our data cover a large window of the urbanization process. Both countries saw large cities grow substantially faster than smaller ones in the early phases of urbanization, but by their mature phases, this advantage nearly vanished (Fig. \ref{fig:2}B-C).

These results help explain the regional differences in $\beta$ observed in Figure \ref{fig:1}. A simple regression shows that when controlling for urbanization level, regional dummies converge toward the global average, with differences becoming either statistically insignificant or much smaller (Fig. \ref{fig:2}D). This indicates that regional differences in $\beta$ largely reflect each country's stage in the urbanization process.

\begin{figure}[ht!]
    \centering
    \includegraphics[width=0.95\textwidth]{figures/figure_3.png}
    \caption{Historical trends and projections for national city size distributions. \textbf{(A)} Rank-size curves for the USA and South Korea. These curves are obtained by fitting penalized cubic B-splines ($\lambda = 1$) to the relationship between city log-rank and city log-size in a fixed year. The USA plot displays also a scatter of the underlying data points. \textbf{(B-C)} The rank-size slope $\alpha$ is estimated by averaging the local slope of the rank-size curve across ranks and then taking the absolute value (Methods \ref{methods:measurement}). Note that $\alpha$ is a spline-based analogue of the Zipf exponent. \textbf{(B)} Change in $\alpha$ for South Korea and the USA from a base year $t_0$ (South Korea $t_0 = 1975,2000$; USA $t_0=1850,1930$). \textbf{(C)} Change in average $\alpha$ across more/less urbanized countries since 1975 (binned scatter plot by year with bootstrapped confidence intervals; $n = 1000)$. \textbf{(D)} Average $\alpha$ across groups of countries in different years. 2100 values are projected using the technique in Methods \ref{methods:projections}. \textbf{(E)} Share of the world population in 1M$+$ cities in 1975, 2025, and 2100. 2100 values are projected under four urban growth models, which differ in their estimates for the future trajectories of $\beta$: proportional growth (PG; $\beta = 0$), increasing returns (IR; $\beta = 0.03$), current trend extrapolation (EX; $\beta$ equal to the country's average between 1975-2025), and our model (OM; time-varying $\beta$ according to the country's urbanization). See Methods \ref{methods:projections}.} 
    \label{fig:3}
\end{figure}

The size-growth patterns observed in Figure \ref{fig:2} change national city size distributions.
We can quantify this change by looking at the distribution's rank-size curve (Fig. \ref{fig:3}A), or more precisely at the absolute value of its slope, $\alpha$ (exact definition of $\alpha$ in the caption of Figure \ref{fig:3}B-C). If $\beta$ is positive, large cities have a growth advantage, the left tail of the rank-size curve rises faster than the right one, the curve steepens, and $\alpha$ increases. Thus, if $\beta$ declines with urbanization (as in Fig.\ref{fig:2}) , $\alpha$ should increase at a decelerating rate. Our data confirm this: $\alpha$ increased in both the USA and South Korea (Fig. \ref{fig:3}B), and it did so faster early on. Further, since 1975, $\alpha$ grew $18\%$ on average across less urbanized countries, against $4\%$ across more urbanized ones (Fig. \ref{fig:3}C). 

With the mechanism in hand---$\beta$ shapes $\alpha$, and $\beta$ weakens as countries urbanize---we move from description to prediction by projecting trajectories of national $\alpha$s to 2100 (Methods \ref{methods:projections}). Our projections suggest that growth in $\alpha$ will slow over the coming decades. Between 1975 and 2025, $\alpha$ grew by 2.3\% per decade, on average across the countries in our sample. Between 2025 and 2100 that same average is projected to grow at 0.9\% per decade. Further, $\alpha$ will continue to grow faster in countries that were less urbanized in 1975. By 2100, their average $\alpha$ is projected to be $16\%$ larger than that of the more urbanized group, while it was $12\%$ smaller in 1975 (Fig. \ref{fig:3}D). 

Translating projected $\alpha$s into population shares, we estimate that 38\% of the world population will live in 1M$+$ cities by 2100 (Fig. \ref{fig:3}E; Methods \ref{methods:projections}). This projection sits below an extrapolation of current trends ($42\%$; Fig. \ref{fig:3}E) and above the proportional-growth benchmark (33\%; Fig. \ref{fig:3}E), consistent with a weakening growth advantage of large cities as urban systems mature. 

\section{Discussion}

Using a robust geographic definition of city and a comprehensive database spanning several countries and historical periods, we show that urban growth follows a common life cycle. Early in urbanization, large cities experience a strong growth advantage, stretching the city size distribution. As urban systems mature, this growth advantage weakens and the distribution stabilizes. We use this model to forecast urban concentration at the end of the century. Relative to an extrapolation of 1975-2025 trends, our model projects 450 million fewer residents in 1M$+$ cities by 2100 ($-4.4\%$); relative to proportional growth, 490 million more ($+4.8\%$).

This study has several limitations. First, our city definition is geographic rather than functional. It tracks clusters of built-up area or high population density, making it well suited for comparative analysis across countries and years. However, because it separates central cores from their surrounding suburbs, it may fail to fully capture the true gravitational pull of large cities. As a result, this definition might underestimate the growth advantage of large functional urban areas, especially in urbanized countries where growth shifts outward. Our supplementary analyses suggest that this is the case: size-growth slopes estimated using geographic urban areas are typically flatter than those estimated using functional urban areas (SI 5.1). However, this underestimation is small relative to the overall trends, so our qualitative results should hold for functional urban areas, though with different point estimates. Accordingly, our projections should be read as conservative estimates of future concentration in functional urban areas.

Second, we identify urban systems with countries. This identification is imperfect, especially in settings with strong cross-border integration, such as Belgium, the Netherlands, and Luxembourg (Benelux). Our choice is dictated by both convenience and principle. Conveniently, countries provide the most comparable unit for global analysis and the most common unit for historical data and projections. In principle, national borders define the migration patterns, trade, institutions, and infrastructure that profoundly shape urban development \cite{ades1995tradea}. Developing a more principled approach to defining urban systems, perhaps through migration networks \cite{bettencourt2020demographyb}, is a promising area for future research. Here, we provide a supplementary analysis at the level of UN M49 sub-regions (SI 4.1). This analysis aligns with our country-level findings, suggesting that the declining growth advantage of large cities is also visible at intermediate spatial scales.

Third, we focus on population, neglecting other dimensions of city size, such as GDP, innovation, or employment. Population is the natural starting point for this analysis because it is broadly comparable across countries and central to the Gibrat, Zipf, and scaling literatures \cite{batty2006rank, bettencourt2007growtha, gabaix1999zipfs, pumain2015multilevel, cottineau2017metazipf}. However, extending our work to economic outcomes and measuring how scaling laws change over time is a valuable direction for future research \cite{pumain2006evolutionary, bettencourt2020urban, balland2020complexa}. The IPUMS full-count census data used in this paper are an excellent starting point for such work \cite{ruggles2024ipums, berkes2023censusa}.

Fourth, our framework is phenomenological rather than causal. We document a robust empirical regularity and show how to use it to improve projections. However, we do not isolate the causal mechanisms underpinning this regularity. Several mechanisms could cause the weakening of the growth advantage of large cities, including slowing rural-to-urban migration, reduced imbalances in migration flows \cite{reia2022spatial, verbavatz2020growtha, bettencourt2020demographyb}, rising congestion and housing costs \cite{sarkar2019urban}, diffusion of economic activity \cite{pumain1997city, pumain2012theorie}, and the redistribution of metropolitan growth toward suburban peripheries (suburbanization) \cite{soo2005zipfs}. In SI 5, we provide a brief discussion of the role of suburbanization, showing that its effect is real but insufficient to fully explain this phenomenon. Distinguishing the relative contributions of other causes remains a promising area of future work, though it is likely to be extremely difficult given the very limited scope for experimentation.

Fifth, our projections are conditional on major shocks not radically changing the future trajectory of urbanization. Since our model is not structural, we cannot explicitly integrate major external shocks, such as geopolitical disruptions, climate-driven migration, pandemics, or technological revolutions that change the cost/benefit ratios of city size. For example, AI-assisted digital twins could reduce the diseconomies of scale that constrain large cities, extending their growth advantage. Climate-induced migration could disproportionately target large cities, where local cultural fluency is less necessary for employment. Countless other scenarios could similarly alter the current trajectory of urbanization. That said, the pattern we document has persisted through historical disruptions of comparable magnitude, including the automobile revolution, the internet, the construction of modern urban infrastructure, and the globalization of trade. While this suggests some level of robustness, our projections should be read as baseline forecasts rather than shock-robust scenarios.

Despite these limitations, our results have relevant implications when viewed through the lens of urban scaling theory \cite{rybski2019urban}. Because many urban outcomes scale nonlinearly with population, reallocating people across cities of different sizes changes aggregate outcomes (see SI 2.3 and \cite{bettencourt2007growtha, ribeiro2021association, gomez-lievano2012statistics}). Our results suggest that as urban systems mature, this reallocation becomes less skewed toward the largest cities and more evenly distributed across the urban system. The policy implications are mixed. On the one hand, if productivity scales super-linearly with city size, a slowdown in the growth of large cities implies a slowdown in reallocation-driven productivity growth \cite{bettencourt2007growtha, keuschnigg2019urban, roca2017learning}. On the other hand, if emissions, urban heat islands, or other environmental burdens rise super-linearly with city size, the same slowdown may ease some environmental pressures \cite{sarzynski2012bigger, yang2025scaling}. Put simply, whether urban concentration or equalization is preferable depends on which of these trade-offs policymakers prioritize----a question that research can inform but not resolve.






\section{Methods}
\subsection{Data}
\label{methods:data}
This paper builds on several datasets, all of which are publicly available. Below we provide a high-level overview of the main datasets. In Methods \ref{methods:code_and_data_availability}, we document how to retrieve them. \\

\noindent \textbf{Population and Urbanization data}: The population projections come from the United Nations World Population Prospect 2024 \cite{undesa2024wpp}, the History database of the Global Environment 2023 \cite{pbl2023hyde}, and Gapminder \cite{gapminder2023systema, gapminder2022population}, with processing from Our World in Data \cite{owid2024population}. We use projections under the medium fertility scenario. The urbanization data come from Chen \textit{et al.} \cite{chen2022updating}. We use their World Bank-based annual projections under SSP2 (``middle of the road''), which extend the World Bank series to 2100.  This data relies on national statistical definitions of ``urban'', which vary across countries and differ from our morphological definition. We adopt these projections for three reasons. First, they are independently validated. Second, they are directly connected to future projections. Third, they provide more reliable estimates of the urban population share than GHSL grids, which are known to underestimate rural populations \cite{schavina2023ghsl, lang-ritter2025global}. We therefore use GHSL grids only to compare urban areas, not to estimate the overall urban population share. Our results are robust to the use of a different definition of urban population share (SI 4.2).
 \\

\noindent \textbf{Country borders}: Boundaries as of 2019, from the CShapes database \cite{schvitz2022mapping}. \\

\noindent  \textbf{Global grids}: Our global cities dataset is based on the population (pop) and degree-of-urbanization (smod) grids from the Global Human Settlement Layer (GHSL) 2023 data package \cite{schavina2023ghsl}. These grids estimate population counts and urbanization levels for 1km-by-1km cells covering the whole planet by combining satellite imagery with census data. \\

\noindent \textbf{USA grids}: Our USA cities dataset is based on custom grids derived from census place population estimates from various data sources.
For the 1990-2020 period, we use estimates from the National Historical Geographic Information System (IPUMS NHGIS) \cite{manson2024ipums}. For the 1850-1940 period, we reconstruct census place population estimates using the IPUMS USA full count census data \cite{ruggles2024ipums} with geocoding from the Census Place Project \cite{berkes2023censusa}. To do so, we match over 500 million individual census records to approximately 40,000 census places. We then aggregate these records to estimate the population of each census place.
Because this historical data comes from century-old handwritten documents, it contains numerous inconsistencies, such as census places disappearing and reappearing over time. We correct for these issues using several preprocessing steps that leverage individual migration data, as detailed in SI 1.1.

We use these clean census place population estimates to build population grids suitable for the City Clustering Algorithm. 
For each year $t$, we create a 1km-by-1km grid covering the continental US. Each grid cell $c_j$ receives an initial population $\text{pop}_{\text{init}}(c_j)$, given by the sum of the population of all census places whose geographic center falls within that cell. We then smooth this initial grid using a spatial convolution kernel: the final population of cell $c_i$ becomes a distance-weighted average of the initial population of neighboring cells $c_j$, with weights decreasing exponentially with distance $d_{c_ic_j}$:
\begin{equation}
    \text{pop}(c_i) = \frac{1}{\sum_{j} e^{-\eta \cdot d_{c_ic_j}}} \sum_{j} e^{-\eta \cdot d_{c_ic_j}} \cdot \text{pop}_{\text{init}}(c_j) \ .
\end{equation}
The decay parameter $\eta$, which controls how quickly population decays around a census place, is set to $\eta = 0.2$, similar to estimates in prior work \cite{batistaesilva2020uncovering}. 

\subsection{Constructing cities: the City Clustering Algorithm}
\label{methods:constructing_cities}

\begin{figure}[h!]
    \centering
    \includegraphics[width=\textwidth]{figures/figure_4.png}
    \caption{
    The City Clustering Algorithm \cite{rozenfeld2008lawsa} computes stable city boundaries for a time interval $(y_1, y_2)$. This algorithm proceeds in five steps: \textbf{(A)} It takes two grids as input, one for each year, containing estimates of population or built-up area. \textbf{(B)} It classifies grid cells as either urban or non-urban using a threshold on these population/built-up area estimates. \textbf{(C)} It groups contiguous urban grid cells to form clusters. \textbf{(D)} It matches clusters across years when they overlap spatially, forming a bipartite graph. \textbf{(E)} It defines a city's boundary as the spatial union of all clusters within a single connected component of the graph.
    }
    \label{fig:4}
\end{figure}

To construct cities from the USA and global grids, we use the City Clustering Algorithm \cite{rozenfeld2008lawsa}. This algorithm identifies stable city boundaries between two years $t_1$ and $t_2$ based on the city's geographic extent, allowing for robust measurement of population growth and comparable city definitions across countries and times. The algorithm, illustrated in Figure \ref{fig:4}, involves five steps:
\begin{enumerate}
    \item \textbf{Classify urban cells}: For each year independently, we classify all grid cells as either ``urban'' or ``non-urban'' using population density or degree-of-urbanization thresholds.
    \item \textbf{Form initial clusters}: For each year independently, we group contiguous \emph{urban} cells into initial clusters using a flood fill algorithm \cite{hoshen1976percolation}.
    \item \textbf{Match clusters over time}: For a pair of years $t_1 \leq t_2$, we construct a bipartite graph $G = (A,B)$, where nodes in part $A$ are clusters in year $t_1$, and nodes in part $B$ are clusters in year $t_2$. We connect clusters with an edge if and only if they overlap spatially. 
    \item \textbf{Define stable city boundaries}: We extract the connected components of the bipartite graph $G$ that have at least one cluster in year $t_1$ \footnote{We do so to avoid ``new cluster bias'' (see below)}. Each component represents a single, evolving city that existed throughout the $(t_1, t_2)$ period. The city's boundary for the period is the spatial union of all clusters within the component (from both $t_1$ and $t_2$).
    \item \textbf{Calculate population growth}:  For each city, we calculate its population in years $t_1$ and $t_2$ by summing the population of all grid cells that fall within its boundary. The ratio of these two population values gives us the city's growth rate over the period.
\end{enumerate}

While the above algorithm largely follows the same approach as the original paper \cite{rozenfeld2008lawsa}, we introduce some minor improvements and clarifications to its implementation.

First, using a bipartite graph to match clusters (Step 3) provides a more systematic and scalable approach than the manual specifications suggested in the original paper. It improves conceptual clarity, simplifies implementation, and naturally handles events like the merger or split of more than two clusters.

Second, our implementation is less ambiguous with respect to the ``cell reclassification problem''. This problem occurs when cells flip their classification, moving from ``non-urban'' in year $t_1$ to ``urban'' in year $t_2$ (or vice versa). These flips do not require any dramatic transformation. As we use thresholds to determine ``urban'' and ``non-urban'' status, even small changes in population or built-up area can cause a flip.  But if not treated carefully, flips may lead to biased growth estimates. For example, imagine a city where hundreds of grid cells flip from ``non-urban'' to ``urban''. If we simply count the population in these newly ``urban'' cells as if they were entirely new additions to the city, we grossly overestimate its growth. Our solution (Steps 4 and 5) is to define a stable city boundary for the entire period and measure population changes only within that boundary. This isolates true population growth from the artifacts of reclassification. While this solution was adopted in the original CCA paper, the implementation is framed ambiguously and the problem is not mentioned. 

Third, our implementation addresses a form of selection bias that we call ``new cluster bias''. This bias arises if one includes urban clusters that appear in year $t_2$ but have no predecessors in year $t_1$. These ``new'' clusters represent only the fastest-growing locations among a larger pool of similar areas, many of which did not grow enough to become urban clusters. Including these successful outliers while ignoring the rest would upwardly bias the estimated growth rates for small cities. Our method avoids this by analyzing only components that contain at least one cluster from the start of the period (Step 4).

To produce the final datasets for our analysis, we apply the CCA to the USA and global grids with specific hyper-parameters. We classified urban cells using distinct criteria for the USA and the global grids. For the USA grids, we use a simple population threshold, classifying a cell as ``urban'' if it has more than 50 people. For the global grids, we use degree-of-urbanization estimates from the smod grid, classifying a cell as urban if it belongs to a ``semi-dense urban cluster'' or higher (cell value $\geq 22$). Further, we applied a common city threshold to both datasets, filtering out clusters with fewer than 5000 inhabitants. Finally, we excluded from the global cities dataset: (i) Nepal and Myanmar due to data quality issues; (ii) countries with fewer than 50 cities; (iii) countries not present in the urbanization data (\cite{chen2022updating}). In SI 3.1 and 3.2, we discuss these hyperparameter choices in more detail and conduct sensitivity analyzes confirming that our results are robust to reasonable variations in their values.

\subsection{Analysis}
\subsubsection{Analytical framework}
\label{methods:theory}
We use a simple analytical framework to guide our analysis. Its purpose is bookkeeping: it links size-growth slopes, rank-size slopes, and the share of the population in 1M+ cities. It is not a causal theory of urban growth.

This analytical framework rests on two simplifying assumptions. First, a city's size $S(t)$ at time $t$ is a power-law function of its (descending) rank $R(t)$, meaning that the rank-size curve (x=log-rank;y=log-size) is a straight line with slope $a_t$\footnote{Note that with this definition the complementary cumulative density function (CCDF) of the city size distribution is $P(S > x) \propto x^{-1/a_t}$. Other authors define the exponent with its reciprocal $\zeta_t = 1/a_t$ so that the CCDF is $P(S > x) \propto x^{-\zeta_t}$.}:
\begin{equation}
    S(t) \propto R(t)^{-a_t}
\end{equation}
Second, a city's growth rate between $t$ and $t + 10$ is a power-law function of its size $S(t)$, meaning that the size-growth curve (x=log-size; y=log-growth) is a straight line with slope $b_t$:
\begin{equation}
g(t, S(t)) = \frac{S(t + 10)}{S(t)} \propto S(t)^{b_t} \ .
\end{equation}
Under these assumptions, $a_t$ and $b_t$ are related by a simple equation:
\begin{equation}
\label{eq:power_law_change}
a_{t + 10} = a_t \cdot (1 + b_t) \ .
\end{equation}
For $t_1 > t_0$, this equation generalizes to:
\begin{equation}
\label{eq:power_law_change_iterated}
a_{t_1} = \exp\Big(\log(a_{t_0}) + \sum_{s \in t_0, t_0 + 10, \cdots, t_1 - 10} \log(1 + b_s)\Big) \ .
\end{equation}
Furthermore, $a_t$ is linked to the share of the \emph{urban} population living in 1M$+$ cities, $m_t$. In fact, the probability of observing a city larger than size $x$ in year $t$ is given by $P(S(t) > x) \propto x^{-1/a_t}$, so:
\begin{align}
\label{eq:shares_vs_rank_size_slope}
m_t &= \int_{z}^{x_{t, \max}} P(S(t) > x) dx  \ / \  \int_{x_{t, \min}}^{x_{t, \max}} P(S(t) > x) dx \\
&=\frac{x_{t, \max}^{1 - 1/a_t} - z^{1 - 1/a_t}}{x_{t, \max}^{1 -1/a_t} - x_{t, \min}^{1 - 1/a_t}} \ .
\end{align}
Here, $x_{t, \max}$  and $x_{t, \min}$ are upper and lower bounds on the size of a country's cities, and $z =10^6 = \text{1M}$.

In sum, this analytical framework provides simple closed-form equations relating the growth advantage of large cities $(b)$ to the concentration of population within them ($a$, $m$).

\subsubsection{Empirical measurement}
\label{methods:measurement}
The above framework highlights $a$ and $b$ as the core parameters governing the evolution of urban systems. We estimate these parameters as follows:
\begin{itemize}
    \item[$a$] The rank-size slope $\alpha$ is our empirical estimate for the parameter $a$. To obtain $\alpha$ we first estimate the rank-size curve $h$ by fitting a penalized cubic B-spline (with penalty $\lambda = 1$) to city log-rank vs. city log-size data points:
    \begin{equation}
    \log_{10}\big(S(t)\big) = h\big(\log_{10}(R(t))\big) \ .
    \end{equation}
     Then we take the absolute value of the mean derivative of $h$ over the log-rank spectrum:
     \begin{equation}
    \alpha =  \frac{1}{r_{\max} - r_{\min}} \Big| \int_{r_{\min}}^{r_{\max}} h'(r)dr \Big| = \Big|\frac{h(r_{\max}) - h(r_{\min})}{r_{\max} - r_{\min}}\Big| \ , \ r = \log_{10}(R) \ .
    \end{equation}
    \item[$b$] The size-growth slope $\beta$ is our empirical estimate for the parameter $b$. As above, we obtain $\beta$ by first estimating the size-growth curve $f$, a penalized cubic B-spline (with penalty $\lambda = 100$) fit to the city log-size vs. city log-growth data points:
    \begin{equation}
    \log_{10}\big(g(t, S(t))\big) = f\big(\log_{10}(S(t))\big) \ .
    \end{equation}
    Then we take the mean derivative of $f$ over the observed log-size spectrum:
\begin{equation}
    \beta = \frac{1}{s_{\max} - s_{\min}}\int_{s_{\min}}^{s_{\max}} f'(s)ds = \frac{f(s_{\max}) - f(s_{\min})}{s_{\max} - s_{\min}} \ , \ s = \log_{10}(S) \ .
\end{equation}
\end{itemize}

We also estimate size-growth curves for groups of countries (such as Europe or less urbanized countries in 1975). The procedure to estimate a group-level size-growth curve $f_g$ features three steps. First, we normalize each city's growth rate $g(t, S_{ic}(t)) = S_{ic}(t+10) / S_{ic}(t)$ by the average city growth rate of its country $c$:
\begin{equation}
g_{c}(t) = \sum_{i \in c}S_{ic}(t + 10) / \sum_{i \in c}S_{ic}(t) = \sum_{i} \frac{S_{ic}(t)}{\sum_{i \in c}S_{ic}(t)}\cdot g(t, S_{ic}(t)) \ .
\end{equation}
Second, we pool the normalized growth rates from all countries in the group and fit a single penalized cubic B-spline $\bar{f}_g$ (with $\lambda = 100$):
\begin{equation}
\log_{10}\Big(\frac{g(t, S_{ic}(t))}{g_c(t)}\Big) = \bar{f}_g\big(\log_{10}(S_{ic}(t))\big) \ .
\end{equation}
Third, we recenter the function $\bar{f}_g$ by the group's average growth rate:
\begin{equation}
f_g = \bar{f}_g + \frac{1}{|g|}\sum_{c \in g}\log_{10}(g_{c}(t)) \ .
\end{equation}

Other authors use ordinary least squares (OLS) regression to estimate the parameters $a$ and $b$. Our approach has two advantages over the OLS approach. First, the resulting parameter estimates are more robust to arbitrary design choices, such as the lower threshold for city size. Second, the estimates align more closely with the equations derived from the analytical framework, even when the data deviate from the framework's ideal assumptions (SI Figs. S4 and S5). These advantages can be explained by how each approach calculates average slopes. Our approach calculates the average slope of a given curve by putting equal weights on each part of the x-range. The OLS approach, in contrast, weights parts of the x-range by the density of data that are within them. Because small cities dominate city population data, the OLS slope is disproportionately influenced by the small-city end of the curve. This makes the OLS slope susceptible to variation in the city size lower threshold and less consistent with our theoretical equations. In SI 2.1, we compare spline-based and OLS-based parameter estimates in greater detail.  

\subsection{Projections}
\label{methods:projections}
The core idea of our projection method is to take the closed-form equations from Methods \ref{methods:theory} and populate them with our spline-based measurements from Methods \ref{methods:measurement}. The logic is that the equations capture the form of the relationship between parameters, while our spline-based measurements provide the most accurate values for these parameters (see SI 2.2).

\begin{table}[t]
    \centering
\begin{tabular*}{0.8\linewidth}{@{\extracolsep{\fill}}lcc}
\\[-1.8ex]\hline\hline \\[-1.8ex]Independent \textbackslash{} Dependent& \multicolumn{2}{c}{Size-growth slope $\beta$} \\
\midrule
Urban population share & -0.049*** & -0.049*** \\
 & (0.004) & (0.012) \\
Country fixed effect & No & Yes \\
Observations & 891 & 891 \\
$R^2$ & 0.168 & 0.545 \\
\hline\hline \\[-1.8ex]& \multicolumn{2}{r}{$^{*}$p$<$0.1; $^{**}$p$<$0.05; $^{***}$p$<$0.01} \\
\end{tabular*}
    \caption{Association between country urbanization and $\beta$. Column (1): pooled specification. Column (2): country fixed effects. The sample is the global cities dataset (Table \ref{tab:1}). }
    \label{tab:2}
\end{table}

We start by projecting $\beta$. We consider four scenarios:
\begin{itemize}
    \item Proportional growth: We set $\beta_{tc} = 0$ for all $t \geq 2020$ and all countries $c$. 
    \item Increasing returns: We set $\beta_{tc} = 0.03$ for all $t \geq 2020$ and all countries $c$. 
    \item Current trend extrapolation: We set $\beta_{tc} = \bar{\beta}_c$ for all $t \geq 2020$ and all countries $c$. Here,  $\bar{\beta}_c$ is the average $\beta$ for country $c$ over 1975-2025 (as mapped in Figure \ref{fig:1}C). 
    \item  Our model: We regress $\beta$ on the urban population share $u$ to obtain $\rho = -0.049$ (Table \ref{tab:2}). Then, for $t \geq 2020$, we set:
    \begin{equation}
        \beta_{tc} = \bar{\beta}_c + \rho \cdot (u_{ct} - \bar{u}_c) \ .
    \end{equation}
    Here, $u_{ct}$ is the projected urban population share for country $c$ from \cite{chen2022updating} (Methods \ref{methods:data}) and $\bar{u}_c$ is the average urban population share for country $c$ over 1975-2025. 
\end{itemize}

We project $\alpha$ for $t \geq 2030$ by plugging the projected $\beta$s into an empirical version of equation \eqref{eq:power_law_change_iterated}:
\begin{equation}
    \alpha_t = \exp\Big(\log(\alpha_{2020}) + \sum_{s \in 2020, \cdots, t - 10} \log(1 + \beta_{s})\Big) \ .
\end{equation}

We project the share of \emph{total} population living in 1M$+$ cities using a two-step approach. 
\begin{enumerate}
    \item First, we project the share of \emph{urban} population in 1M$+$ cities using an empirical version of equation \eqref{eq:shares_vs_rank_size_slope}:
    \begin{equation}
    \label{eq:shares_vs_rank_size_slope_empirical}
        m_t = \frac{x_{t, \max}^{1 - 1/\alpha_t} - z^{1- 1/\alpha_t}}{x_{t, \max}^{1- 1/\alpha_t} - x_{t, \min}^{1- 1/\alpha_t}} \ .
    \end{equation}
    The key challenge in evaluating the right-hand side of this equation is to set plausible values for $x_{t,\min}$ and $x_{t,\max}$, the lower and upper bounds on the sizes of a country's cities. For $x_{t, \min}$, we use the city size lower bound used throughout the paper, $x_{t, \min} = 5000$. For $x_{t, \max}$, the choice is less straightforward because there is no clear upper bound for the size of a country's cities. We assume that $x_{t, \max}$ is proportional to the total urban population of a country $U_{t}$, i.e., $x_{t, \max} = \omega \cdot U_{t}$ where $\omega$ is a tunable parameter. We then calibrate $\omega$ using historical data. For each country, we select $\omega \in (0.1, 2)$ to minimize the average deviation between the shares $m_t$ calculated using equation \eqref{eq:shares_vs_rank_size_slope_empirical} and the shares $\hat{m}_t$ observed directly in the data. Aggregated at the regional level, the calibrated estimates $m_t$ closely match the observed data $\hat{m}_t$ (mean absolute error $|m_t - \hat{m}_t|$ below $0.01$; see SI Fig. S6).
    \item Second, we multiply the projected shares $m_t$ by the projected urban population share $u_t$ to obtain the share of \emph{total} population living in 1M$+$ cities.
\end{enumerate}

\subsection{Code and data availability}
\label{methods:code_and_data_availability}
All data and source code underlying this paper are publicly available. \\

\noindent \textbf{Code}: To enable exact re-execution, we provide a fully automated, end-to-end pipeline that reproduces the entire analysis with a single command. The pipeline is available on GitHub \url{https://github.com/ethz-coss/global-city-growth} and archived on Zenodo at the time of publication \url{https://doi.org/10.5281/zenodo.17339403}. It handles $\sim 300$ GB of data spanning heterogeneous formats like raster, vector/shapefile, CSV, and Parquet. It executes $100+$ tasks in a directed acyclic graph and produces $200+$ output tables persisted in PostgreSQL (primary store) and processed with DuckDB (for fast processing of large tables). It is containerized with Docker. On a MacBook Pro (Apple M2, 32 GB RAM), a full run completes in $\sim 5$ hours. \\

\noindent \textbf{Source data}: We deposited all redistributable source data at \url{https://doi.org/10.5281/zenodo.17343655}. Some datasets (IPUMS and NHGIS) are public but not redistributable. The pipeline retrieves them via the IPUMS API. Running the pipeline requires a personal IPUMS API key (see \url{https://developer.ipums.org/docs/v2/apiprogram/}). \\

\noindent \textbf{Output data}: A full database dump of all aggregate tables resulting from a pipeline run is available at \url{https://doi.org/10.5281/zenodo.17338968}. The key output datasets --- city boundaries and populations for the USA (1850-2020) and the world (1975-2025) + projections of population shares in 1M$+$ cities by country --- are available at \url{https://doi.org/10.5281/zenodo.17315338}. 

\subsection{Acknowledgments}
Andrea Musso and Dirk Helbing acknowledge support from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation program (833168). Frank Neffke acknowledges financial support from the Austrian Research Promotion Agency (FFG) in the framework of the project ESSENCSE (873927), within the funding program Complexity Science. Diego Rybski acknowledges support from the German Research Foundation (DFG) project UPon (451083179) and project Gropius (511568027). Andrea Musso is grateful to Simone Daniotti, Cesare Carissimo, and Ricardo Hausmann for helpful conversations. 

\bibliography{sn-bibliography}
