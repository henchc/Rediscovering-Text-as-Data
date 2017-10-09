# Piper, Algee-Hewitt, Sinha, Ruths, and Vala, "Studying Literary Characters and Character Networks."

Bjoern Skeel-Gjoerling

## 1) [Discussion Questions](https://goo.gl/forms/DeFIwTGM584J1sqG2)

1. Do you find Algree-Hewitt's findings interesting? Why or why not?

2. What are the pros and cons of analyzing differences in character networks across different literary texts compared to focusing on one literary text alone?

3. Under which circumstances would you find it relevant to use Piper & Vala's computational tool for character analysis? (The tool analysis characters on four parameters: Distinctiveness, Centrality, Positionality, Modality) Can computational character analysis stand alone?

## 2) Summary

1. **Algree-Hewitt** uses network analysis to look at changes in character networks in English plays across time (from 1500-1920). The study finds that modern plays have a smaller periphery of characters but that the number of characters in the core has increased. This indicates that modern plays are more personal and intimate but also use a larger number of sub-networks. 

2.  **Sinha, Piper & Ruths** address the question: "What is interaction?". The study explores reader agreement across different types of interactions - do person A and person B both understand this text passage as an interaction. The different interaction types are identified using unsupervised clustering methods. The results are not described in the reading. 

3. **Piper & Vala** have developed a computational tool to analyze different characters and their characteristics in a text. The tool evaluates characters on four parameters: 1) Distinctiveness (how different are characters from other characters in the novel) 2) Positionality (how often is the character the agent or object of a sentence or a possessor of some object?) 3) Centrality (how important is the character to other characters in the novel?) and 4) Modality (What behaviors and attributes identify the character?). The method is not further elaborated upon in the reading. 

---

*In the following questions I will focus on Algree-Hewitt's study because the results of the other studies are not described.*

## 3) Level of Engagement/Analysis

Algree-Hewitt is interested in the **character relationships of English plays and how they have developed over time**. The scope is very broad and general as he looks at the change in the social networks (Number of characters? The proportions of important characters? The number of bridging characters? etc.) over a 400-year period. The dataset contains 3439 plays. 

## 4) Argument/Stakes

Algree-Hewitt's study has three main findings:

1. Modern plays have **fewer "unimportant" characters**

2. Modern plays have **a larger number of characters with importance to the storytelling**

3. Modern plays use bridging characters to a smaller extent 

## 5) Method

Algree-Hewitt uses **network analysis** to examine the network structures of the plays. From the network analysis he extracts three summary statistics:

1. *Gini Coefficient of the eigenvector centrality*: Measuring the distribution of centrality across characters (= what is the distribution of significance among characters) 

2. *% of characters in the top 25 % of the eigenvector centrality distribution*: Measuring how many characters that are in the core of the social network.

3. *Betweenness centrality*: Measures the importance of bridging characters (characters that mediates other characters' interaction) in the social network.

## 6) Issues

Some issues can be raised:

1. Network analysis has difficulties adjusting for the variation in importance of actions and dialogues. Some character may be very important even if he/she is only mentioned in one sentence if this sentence is crucial to the entire plot. This requires a subjective evaluation of sentences which is not possible in a network analysis. 

2. The network analysis relies on explicit mentioning of the characters. This means that the method can't take implicit character references into account. I imagine this to be very relevant for critical plays with political content as the critique often will be implicit and hidden. 

3. Algree-Hewitt has to use a digitized database of plays to conduct the network analysis. This sample is probably not identical to the entire population of British plays in that period and may therefore be biased toward plays that we today find "significant of the time".

## 7) Reproducibility/Transparency

Reproducibility is easy and the transparency is high due to the study's high emphasis on **objective measures and the usages of a public available database** (Chadwyck Healy drama corpus). 

## 8) Broader Application

The idea of using network analysis to analyze differences in character networks can be applied to many other fields. Within the literary discipline, the same method can be used on novels and to compare the usage of characters networks between different authors. Furthermore, the method can be used at other texts such as news articles, research papers, press releases, business documents etc.      

