# Underwood & Sellers, "How Quickly do Literary Standards Change?"

Katharine Chua & Elizabeth Fraysse

## 1) [Discussion Questions](https://goo.gl/forms/i8XyeePvJ7bdDez83)

1. What role do you think broader sociological phenomenons (sexism, racism, etc.) have on this type of computational analysis of texts?

2. What did you think about (one of!) the author’s conclusions— that the relationship between literary criticism and how artists react to criticism is circular and self-fulfilling? 

	> “... individual writers are already historical agents, then perhaps the system of interaction between writers, readers, and reviewers also tends to establish a resonance between (implicit, collective) evaluative opinions and directions of change.” (pg. 21)

3. Do you think the author made a logical and strategic decision to look at the data by the century instead of breaking it up into five 20 year periods or four 25 year periods? Discuss the merits and disadvantages of changing the time period chunking. 

4. On page 30, the authors write: “Writers who dismiss models as “merely empirical” or “positivist” strategies are announcing mainly that they haven’t yet engaged the debate about the interpretive limits of modeling that flourishes in other disciplines, and increasingly our own.” Do you agree? To what extent? 

5. If you were to evaluate a poem as either being a reviewed or random, what would you look for? Explain. 

## 2) Summary

The article explores an evaluation of literature, looking at the chances that the poem was reviewed or not solely based on the word frequencies, without the input of overall literary trends and styles that the poems contain. The authors built a model designed to predict whether a given volume had been reviewed in a selective venue— through the process of translating word frequencies into a probability percentage. From these results, the authors want to gain a deeper understanding of how quickly literary standards (and perhaps, in response, literary style) changes. 

## 3) Level of Engagement/Analysis

The author engages very generally with the primary source and briefly discusses how you would look at a primary source and decide whether it's a reviewed or random piece.  The author looks at the reviewed and random poems closer, looking at the tone that the poets choose, which offers insight into the topic of the poem, and style of poems and how these elements might give a program insight into whether the poem was reviewed or random and what this says about the culture at the time.  

## 4) Argument/Stakes

At the outset, the authors began with this explicit hypothesis:

> "[there exists a] widely-discussed “great divide” between elite literary culture and the rest of the literary field would become increasingly visible as we proceeded through the late nineteenth century and into the twentieth."

Related to that hypothesis, the authors wanted to find answers to the question, “How quickly do literary standards change?” Through the results of their research, they found that “received narratives of literary history lead us generally to overestimate the pace of change,” or in other words, “they change quite slowly.” With regard to their hypothesis, the authors found that a “great divide” was apparent much earlier than they had thought, and for that matter, much earlier than literary historians had popularly thought. This article provides empirical proof by model that the divide has existed for a longer time than previously thought.   

## 5) Method

The paper employs a model that utilizes counting methods, and then from those results, applies a logistic regression classification algorithm (e.g. these words are more likely to appear in positively-reviewed works, as opposed to those words), and therefore this work is more likely to be reviewed or not.

## 6) Issues

The author uses reviews from a select pool of selective venues, there could be a correlation between a selective venue that review multiple works for the same author, which could skew what is considered a theme in poems that were reviewed. In the article the author uses the example of the works of Felicia Hemans and it shows that her poems became more likely to reviewed as her career went on, and her poems made up five of the poems that were evaluated. If the selective venues that evaluate poems have favorite authors, that the venue likes to review, this could manipulate the trends that show up as overall trends in poems, instead of author creative preferences. The selective venues could have authors that they prefer to review because they are authors that their readers enjoy or are ‘popular’.

## 7) Reproducibility/Transparency

The authors are impressively transparent when it comes to describing their methodology (e.g. the entire subsection titled “Potential problems with the model”). Throughout the article, the authors describe their assumptions, hypotheses, tangents in their exploration, as well as changes/deepening of their methodological approach and focus. At the end of the article, they provide a link to a GitHub repository that contains the data that they used, bibliographic information on the data, as well as their actual code. 

## 8) Broader Application

The application of this problem could be used for many different kinds of literature.  Looking at the tone, syntax and themes of the poems, this could be used for any other genre of literature and would offer insight into the social, political and historical trends of the times.  This method could specifically look at the field of novels and see if there are any trends in which genre is preferred at what time or if people preferred a novel that was cheerful and funny or sad and darker.  This could help understand the mindset of people at that time and could apply to a deeper understand of the historical and social context.
