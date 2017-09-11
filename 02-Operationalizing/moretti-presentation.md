# Moretti, "Operationalizing"

## 1) Discussion Questions

1. At the beginning of the article Moretti constantly returns to the popular critique of the Digital Humanities as "making existing knowledge somewhat better, but not really different." [5] Can computational approaches to literature really tell us anything new? How might we do that?

2. What does Moretti mean when he writes: "I assumed, like so many others, that the new approach would change the history, rather than the theory of literature" [9] ?

3. What other literary theories could be operationalized?

4. Moretti ends his article with an ominous statement: "because, if the data revolt against their creator, then the concept is really in trouble." [13] While Moretti certainly admits that not *all* concepts can be operationalized, what does this statement mean for existing theories?

5. To what degree can (should) humanist conclusions be "reproducible"?

## 2) Summary

Moretti looks at character-space and the most distinctive words of characters in dramas using computational techniques in order to prove or disprove existing literary theories through *measurement* (Woloch 2003, Hegel 1818-1829).

## 3) Level of Engagement/Analysis

Moretti is interested in relationships between characters and what role they play in a drama, more specifically in tragedy. He also considers the actual dialogue text toward the end of the article in his discussion of most distinctive words and stichomythia.

## 4) Argument/Stakes

Moretti makes arguments both concerning the general application of Digital Humanities methods, as well as *Antigone* the individual text:

1. "Operationalizing" can tell us that such a concept *exists* in the first place. [4]
2. measuring a concept is *precise* [5]
3. We can use two criteria for *measuring* protagonism: "the volume of words, and the number of
interactions." [5]
4. Moretti proposes a new hypothesis of character *function* ('conflict', 'mediation', and 'obedience') instead of *importance* ('minor', 'minor minor'). [8]
5. Moretti argues that, at least in *Antigone*, Hegel's emphasis of direct face-to-face conflict as the location of "ethically justified pathos" is misidentified. This pathos actually lies within Antigone's conversations with Ismene, the Chorus, and others, and not with the antagonist.

## 5) Method

*Character-space*:

- "character-space turns smoothly into “word-space”—“the number of words allocated to a particular character”—and, by counting the words each character utters, we can determine how much textual space it occupies." [2]

*Most Distinctive Words (MDW)*:

- "To do this, the Literary Lab follows an approach (which we call Most Distinctive Words) in several steps. First, we establish how often a word occurs in the corpus, and hence how often a specific character is expected to use it given the amount of words at its disposal; then we count how often the character actually utters the word, and calculate the ratio between actual and expected frequency; the higher the ratio, the greater the deviation from the average, and the more typical the word is of that character." [10]

## 6) Issues

- I tend to disagree with Moretti on precision, and agree more with Koyré. Morever, especially with textual data, and even more so with *ancient* textual data, different editions and manuscripts will obscure any true precision.

- Moretti admits that it is only a hypothesis, but I'm not sure his idea of 'conflict', 'mediation' and 'obedience' would play out over networks in a larger corpus. I can think of many examples where a pivotal character only engages with one other, and not in an obedient manner. I think looking for functions within the network is promising, but his assignments are almost too specific. This approach is interesting for single texts, however.

- While his actual method (data/preprocessing, see below) is unclear, I appreciate his final argument about tragedy for focusing on a single text and a single theory proposed by Hegel.

## 7) Reproducibility/Transparency

The actual data analysis is relatively reproducible. Measuring character-space and most distinctive words is straight-forward for the texts he describes. But what edition of the texts is Moretti using? Is he using the original Greek or the English translation? Footnote 13 makes us assume the former, but it's never actually stated. Did Moretti leave any words out? 

For most distinctive words, we'll see that there are many other words that appear more distinct than what Moretti tells us. What rank of "distinctiveness" are the words he gives us? Wasn't he trying to emphasize "precision"? I'm assuming he used the original Greek, but especially for this analysis, the translation could yield an entirely different picture.

Where is the code for this project?

## 8) Broader Application

Both the idea of character-space and the idea of MDW are drawing from the more general goal of distinguishing different texts. In this case, we are looking at the text belonging to different speakers. But this can be generalized to texts of different articles, Twitter users, Facebook profiles, etc. We could look at the "Character-Space" allotted to different articles on Wikipedia (either different languages or topics) or the most distinctive words across political candidates on Twitter or in their campaign speeches.


