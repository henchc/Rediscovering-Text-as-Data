# Rhody, "Topic Modeling and Figurative Language"

Ismail Salim & Sidney Le

## 1) [Discussion Questions](https://goo.gl/forms/A0opkZ0FKAKBSAe72)

1. How would topic modelling fare in fiction? How would our interpretation of the topics as indicators of "thematic trends" change? What other considerations must we make?

2. What advantages does topic modelling have compared to our previous methods (textual similarity, clustering, classification)? In what ways does it fail comparatively?

3. For topics that are uninterpretable (at least in a concise and simple way), are there any meaningful conclusions to be drawn? 

4. Rhody concludes that the topic models for her corpus produced four types of topics. How do these topics change your understanding of ekphrastic poetry, if at all? Reminder, Rhody has defined the characteristics of ekphrastic poetry as "the language of stillness, breathlessness, desire, and competition". 

## 2) Summary

In an attempt to refine understandings of ekphrastic poetry, Lisa M. Rhody applies a number of computational analysis models to a large corpus of both ekphrastic and non-ekphrastic poetry. One of these models is topic modelling, which in its normal context of non-fiction works well to extract thematic trends in an unsupervised way from a text or large body of texts. Rhody creates 60 topics and finds that they do not describe thematic trends or elements per se, but rather certain aspects of functional discourse in and about the poetry.

## 3) Level of Engagement/Analysis

Rhody, although she mentions the Sexton poem quite often, engages with it very little. The Sexton poem is but an example poem of any number of poems that she could use from her corpus of 4500 poems. While she does use it to illustrate a number of points about the LDA topic model, such as the removal of stopwords and the way the topic words relate to individual texts, little is done beyond strict identification of a few of the topics present in the work. Rhody does, however, mention that the poem "refocuses collective attention on a widely-recognized work of art with a recognized connection to another artist suffering from mental duress."

## 4) Argument/Stakes

Rhody ultimately argues that while the results of topic modelling are not perfectly comprehensible for highly figurative language like poetry; the methodology’s failure can still prove to be “potentially productive for literary scholars”. By accompanying the topics identified by the LDA with close reading, we can contextualise the lists of words to “explore latent patterns in poetic texts”. That is, topic assignment in the context of figurative language found in poetry may not be thematically or semantically meaningful but still useful.
 
Rhody essentially extends the methodology of Blei to the realm of poetry out of curiosity for LDA’s interpretation of figurative language. Rhody even reveals some scepticism and does not express an intent to overturn an existing specific literary theory. Indeed, the article posits LDA as a method of discovery but, similarly to previous articles, seems to conclude that computational tools do not powerfully interpret without closer reading. 

## 5) Method

*Latent Dirichlet Allocation (LDA)* -- mathematically and statistically complicated. Suffice to say, it generates topics unsupervised, which themselves have probabilities for generating certain words. Based on word usage, then, one can predict the "proportion" of a topic will be in a document.

Beyond that, Rhody engages in some close reading of the topics to understand their meanings and functions.

## 6) Issues

Rhody writes that she is focusing on this model as it “prompted a reconsideration of the tropes and conventions of ekphrasis” and “illustrates how figurative language resists thematic topic assignments”. It might be more powerful for her following argument to also show the results of other models for the sake of comparison. 
Further, we are not given a comprehensive list of the 60 topics and the words associated with them for the corpus.  Without these we have to trust Rhody’s topic selection as the best interpretation for LDA’s performance. 

## 7) Reproducibility/Transparency

While Rhody explains the methodology of the LDA with useful analogies, she does not explicitly show the code that she uses to perform the LDA. However, in fairness, the LDA technique is likely to follow a strict and conventional algorithmic process.
However, preprocessing is not discussed by Rhody in detail. Rhody does shows in Figure 3 that she has removed stop words but does not mention whether she lemmatises the text and other potentially important techniques. 

## 8) Broader Application

Topic modelling, as it takes the form of generative and unsupervised machine learning, can essentially explore and cluster features of any new data set where you are unsure of the existing structures.
 
Currently, the New York Time uses Topic Models to increase their user-article recommendation engines. As well as that, they are being used for recruitment agencies to match features of job descriptions to suitable potential applicants.  