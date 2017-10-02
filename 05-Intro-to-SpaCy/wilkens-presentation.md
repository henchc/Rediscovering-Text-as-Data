# Wilkens, "The Geographic Imagination of Civil War-Era American Fiction"

## 1) [Discussion Questions](https://goo.gl/forms/eeN7IVP0vwQyY7TC3)

1. Wilkens asserts that “population figures weren’t the whole story.” He describes time-lag in literature and the exciting appeal of war stories as important factors in the shifts in geographic representation of certain places associated with the war after it ended. What are potential other reasons for the results listed in Table 4, and figures 8 and 9?

2. Wilkens explains that American authors have a surprising affinity with the Bible and with classical antiquity. Do you expect that these references increased or decreased into the late 19th, and even 20th century? How might the rate of references compare with references made in British or French literature of the same era? Why?

3. According to Wilkens’ analysis, “literary interest in many Confederate states apart from Texas...  rose relative to population after the Civil War.” What further analysis could be conducted on these same pieces of work to understand more about the literary world’s changing engagement with and perspective on these areas over time?

4. How do you think that Wilkens’ data would differ if it focused solely on regionalist works?

## 2) Summary

Wilkens analyzes both pre- and post-Civil War era literature, specifically in the context of understanding literary geography - the recurrence of places in American fiction. He concludes that despite the divisive war within the nation, the changes in setting are not consistent with changes due to the war, and seem to occur more as consequence of population growth and migration patterns within the country.

## 3) Level of Engagement/Analysis

The author does not engage with the particular text that we read, *The Romance of the Republic*; however, he addresses specific examples from a number of works in citing examples of statistically significant changes or inconsistencies in the data. Specifically, Wilkens is engaging with an exploration of literary geography during the time. The piece we read, set in New Orleans with many references to France, etc., clearly fits within this grouping of literary works that Wilkens analyzed. However, he made no specific reference to its characters, prose, structure, or setting beyond listing its title midway through the analysis as an example of a setting affected by the war.

## 4) Argument/Stakes

The author intended to argue that computational analysis over such a large volume of works written within a concentrated era would shed light on changes in American authors’ and public’s perspective on geography, domestic and international, as a result of the American Civil War. This question is fascinating, in particular because of its wide approach across over one thousand works of that time; however, the results found seem to provide insignificant evidence for the Civil War as a strong factor towards geographic perspective in that time.

The article does, however, discuss interesting correlations between population size and literary reference, as well as some exceptions. It also addresses the issue of lag in literature - that population migration and the birth of new towns, cities, metropoles is not addressed in literature until some years after its influence has begun. 

## 5) Method

- Data source: Lyle Wright’s American Fiction, 1851-1875.

- Sample: 1,050 novels. Of the 2,925 novels, only 1,050 were digitized, hand-corrected, and verifiably published between 1851-1875.

Methods: 

- Named entity extraction using Stanford CoreNLP.
- Geospatial analysis using Google Maps Geocoding API.
- Statistical test for association (Dunning’s log-likelihood ratio), comparing population to location occurrences at two distinct times, pre-1861 (1850 US Census) and post-1861 (1880 US Census), for each location.


## 6) Issues

Wilkens never fully explains why regionalism should correlate to increased geographic diversity in American fiction or why relative frequency of location occurrences is a good proxy for regionalism. While it seems reasonable that novels emphasizing the importance of a particular place would often mention that place, the opposite could also be true. For example, in the first two chapters of A Romance of the Republic, the story takes place in New Orleans and Child describes the setting in great detail, but “New Orleans” appears less often than “Boston.” 

Wilkens acknowledges that literature may not immediately reflect social and political changes, but his data source spans less than three decades. This makes it difficult for him to draw solid conclusions about the influence of particular events on American literature.


## 7) Reproducibility/Transparency

Wilkens’ corpus and location occurrence data are publicly accessible, so his methods are transparent and his results are largely reproducible. 

## 8) Broader Application

Wilkens’ methods have broad applications. They could be used to compare the speeches of different political actors or a single political actor over time. They could be used to detect cheating or confirm authorship by identifying similarities in vocabularies or literary patterns. 


