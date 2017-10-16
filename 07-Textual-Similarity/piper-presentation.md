# Piper, "Novel Devotions"

Alleanna Clark, Avni Prasad. Jillian Smith

## 1) [Discussion Questions](https://goo.gl/forms/kvZJfrsAtU4KPxA12)

1. Why do you think Piper chose to specifically use Augustine’s *Confessions* to examine text clustering? What do his results on text clustering tell us about Augustine’s *Confessions*? (Look at the Cross-Half Distance and In-Half Distance graphs on page 73)

2. Towards the end, Piper talks about his process of discovery and validation by examining conversion in a story. What does Piper mean when he uses the term “conversion”? Can we use data analysis and text clustering to determine how conversional a book is? If so, how? If not, why not?

3. In the last pages, Piper introduces multiple hypotheses that could be tested through text clustering. Do you think text clustering is sufficient in testing these hypotheses? Why or why not? 

4. The first rule of computational hermeneutics is “simplification is the cost of understanding complexity at a greater degree of scale” (page 70). Piper shared his thoughts on why it’s worthwhile to sacrifice detail and context to analyze literature on a larger scale. In your opinion, what are the pros and cons of working on a large scale analysis versus working on a small scale analysis or doing a close reading? Do you think one technique is better than another?


## 2) Summary

Piper looks at how novels transform from start to finish, and argues that this transformation, or “conversion”, is another important way to think about, group, and compare novels. Piper is also interested in text clustering models, and uses them to defend his points on conversion, discovery (validation), and the pros and cons of distant vs. close reading analysis. 


## 3) Level of Engagement/Analysis

Piper engages directly with Augustine’s Confessions to look at conversion. It is his main example for the models he outlines within the first half of his essay. While he does engage with it computationally, all the computations are very broad. He doesn’t touch upon the meaning of the text or provide any kind of close reading analysis. Piper does, however, provide some meaning and context for the other pieces he mentions in the section Discovery (Validation). He also address current culture when touching upon the recent debates between distant and close reading.

## 4) Argument/Stakes

1. Piper advocates for computational tools as a means of shining light on patterns that are difficult to notice without data analysis. He says technology can produce “new truths” about novels and genres that can potentially change the way we interact and understand the texts we read.

2. Textual clustering provides us with the tool to monitor “conversion.” By taking into account how the book evolves over the course of time (comparing the before and after of a turning point), Piper suggests we can understand “text’s transformative force” and its purpose. Textual clustering helps us track linguistic shifts through textual models over time and understand a novel more wholistically by providing context. 

3. Piper shows a strong sense of before and after in Augustine’s *Confessions* by tracking the dissimilarity of language by clustering of the vector-space models of the first 10 “books” and the last three. He seems to argue that Augustine’s language not only became more heterogeneous at the end of the novel, marking a conversion, but also his language became increasingly different. 

4. Piper suggests that narrative novels embody a more binary nature and strong sense of conversion than autobiographies and non-narrative texts do. Because of this, Piper believes genres could potentially be distinguished using his model of textual clustering. 

5. At the end, Piper indicates his model for textual clustering can be used to examine many other hypotheses testing for conversion including its relationship to binariness and negativity in a book.  


## 5) Method

**Vector-space Modeling**: Used to understand relative recurrence of words, relies on the assumption that “textual meaning is a function of linguistic repetition” 

**Multidimensional Scaling**: Makes it possible to compare multidimensional vectors of word frequency with others in a 2-dimensional manner (represented in a graph)

**Text Clustering** (uses k-means clustering and silhouette test): allows us to determine this notion of “before and after” that Piper talks about at the beginning of his paper. Piper takes vector-space models from different parts of the novel or genre and is able to see how they compare through text clustering

**Cross-half distance** (distance between earlier and later parts of work): helps us determine how the text has changed linguistically over the course of the book

**In-half distance** (distance within earlier and later parts of work): helps us determine how fast the text is changing linguistically 

**Process of Discovery/Validation** (not strictly computational): Piper builds this process of computational extracting meaning from novels and genres, then tests these models by running the computational methods and seeing whether we get the answers we expect

## 6) Issues

Does not engage with close reading. We discussed the need for a balance between the computational methods and close reading in order to have a comprehensive analysis.

Piper assumes that there is a similarity between genres which could lead the research astray because it does not account for exceptions. Although most texts from the same genre have similar characteristics, just because one does not fit the mold of the science fiction genre, for example, does not mean it is not considered part of the category. 

## 7) Reproducibility/Transparency

Piper could have been more transparent by providing some way to access the code he used since his argument was centered so much around the iteration. However, the step-by-step instructions he provided in the notes gives us a way to produce the results but there is room for variation because of some decisions he made. For example, in note 34, Piper states that he only kept words that were “consistently” present in a sample but consistency of a word could differ depending on the person conducting the analysis.

## 8) Broader Application

Piper’s argument was interesting because it looked at a text’s ability to transform. This method could be applied to other forms of text, such as newspaper articles, and look at the way certain events had an effect on the way they were talked about, thus, giving us a better look at the important historical events. One could look at the “sense of before and after” Piper mentions by focusing on a single turning point in history. 

