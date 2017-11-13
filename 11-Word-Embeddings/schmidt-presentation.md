# Schmidt, "Rejecting the gender binary: a vector-space operation"

Jessica Au, Jake Hyman, Samantha Ku & Alicia Lin

## 1) [Discussion Questions](https://goo.gl/forms/QjjzceDzkzlyc1si1)

1) Was Schmidt’s choice to use ‘she’ and ‘he’ the most appropriate or effective in encompassing gender in language?

2) Schmidt makes the claim that a distinctive feature of new word embedding models allows vector rejection to be “meaningful on vectors between words as well as vectors of words.” What does this mean and how does it differ from or relate to other models that we’ve looked at before?  

3) How would Schmidt’s findings be affected if he used a corpus other than RateMyProfessor (if it would be affected at all)?

4) How else can we apply this method to tackle different constructs besides gender?


## 2) Summary

Schmidt uses word embeddings and vector rejection to analyze gendered language within a corpus of reviews from [ratemyprofessors.com](http://www.ratemyprofessors.com/). By exploring these differences and paired ‘gendered synonyms’ between male and female categories, Schmidt hopes to uncover the ways in which gender is deeply and often times invisibly ingrained into language.

## 3) Level of Engagement/Analysis

In the article, Schmidt engages with the corpus through his computational analysis of the reviews. Overall, there is a very surface-level analysis of the results. He may sometimes point certain things out such as how students are more likely to use “professor” when talking about male professors than when talking about female professors, or that women are “nasty” whereas men are “disgusting.” However, beyond mentioning certain points, he only gives a few arbitrary possible explanations of the results. This is most likely due to that fact that Schmidt is in more of an “exploratory” phase in which he is just trying to show how the models can help us better understand gendered language. Although it would be nice for him to provide more analysis, it is not his purpose to do so at this point in the analysis. 

## 4) Argument/Stakes

Schmidt doesn’t make any substantial claims regarding gendered language or sexism at large given that his analysis is mainly exploratory. His approach differs from other digital humanists in that he uses this model as a different lens through which to read language that is naturalized to us, whereas others often depend on models to give more direct answers or explanations. Ultimately, Schmidt’s argument is less about the findings themselves but more about how this specific method can help people think about gendered language and other constructs at large. And since the main focus of this article is to merely explore the use of the model on gendered language, there is not much at stake. If anything, he discounts a lot of his findings out of sheer confusion or lack of thought, but acknowledges that further investigation into this topic could be more fruitful in tackling gender biases in language and in society.


## 5) Method

Schmidt uses methods called word embeddings and vector rejection to map out the networks of meaning in language by seeing how words are used in context within the corpus, and then removing the patterns that map onto gender. He begins by tracing out the path between 'male' and 'female' words and extracting gendered words, then using cosine-similarity to compare their similarities. He then “rejects the gender binary” through vector rejection by “building a new vector space from the old by transforming each element to no longer have any directionality along the vector that separates male from female.” By comparing the list of words and their cosine similarities between the ‘gendered vector space’ and ‘agender vector space’, we see how these relations are affected if the technical ‘gender binary’ were rejected.

## 6) Issues

Schmidt’s argument is limited by his use of only the Rate My Professors corpus and his focus on criticism. Schmidt implies that women are criticized more harshly, which albeit most likely true, an analysis of positive reviews would provide a more holistic view of whether the inequality is sufficiently supported by the text. It should also be noted that the majority of reviews on Rate My Professor skew towards the negative, whereas people are less motivated to leave positive or neutral reviews.

In addition, Schmidt fails to take into account real world gender biases into his analysis. It would be helpful to know what the breakdown of percentages between female and male professor reviews were and whether or not that reflected real world gender breakdowns in universities. Especially since if there was more data for one category, then that category’s analysis or word embeddings might be more nuanced which would affect our results.

## 7) Reproducibility/Transparency

Schmidt is very clear in his presentation, including all of the code relevant to the specific project in this post and providing links to past posts that contain the R-package he created for the project. He gets his corpus from reviews on Rate My Professor and explains in the footnotes how he cleaned up and formatted the corpus.  The corpus is highly  accessible and the method is described in detail for those wishing to recreate it themselves.  Overall, the reproducibility and transparency is high. 

## 8) Broader Application

This method can be applied to tackle gendered language in different contexts. For example, using this method on historical literature could help us better understand how perspectives on gender evolved over time. This method could also be applied to fixate on other categories such as race. And even in the post itself, Schmidt says that he plans to turn the model to 19th vs. 20th century newspapers to see how the constellation around political terms changed over time. And aside from other applications in terms of different corpora, this method could potentially be used to expose large scale inequalities that underlie gendered language and therefore society if explored further.