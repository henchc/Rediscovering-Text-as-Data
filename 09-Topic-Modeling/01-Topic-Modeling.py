
# coding: utf-8

# In[ ]:
from datascience import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# # Topic Modeling in Python
#
# In Lisa Rhody's article, "Topic Modeling and Figurative Language", she uses LDA topic modeling to look at ekphrasis poetry. She argues that ekphrasis poetry is particulary well-suited to an LDA analysis because of the assumption of a previously existing set of topics. She's able to extract a number of topics, each constituted of a set of words and probabilities. While we don't have Rhody's corpus, we can use this technique on any large text corpus. We'll use a corpus of novels curated by Andrew Piper.
#
# ## Corpus Description
# We'll look at an English-language subset of Andrew Piper's novel corpus, totaling 150 novels by British and American authors spanning the years 1771-1930. These texts reside on our volume, each in a separate plaintext file. Metadata is contained in a spreadsheet distributed with the novel files by the [txtLAB](https://txtlab.org/) at McGill.
#
# The metadata provided describes the corpus that exists as `.txt` files.
# So let's first read in the metadata:

# In[ ]:


metadata_tb = Table.read_table('data/txtlab_Novel150_English.csv')
metadata_tb.show(5)


# Before we go anywhere, let's randomly shuffle the rows so that we don't
# have them ordered by dates or anything else:

# In[ ]:


np.random.seed(0)
metadata_tb = Table.from_df(metadata_tb.to_df().sample(frac=1))
metadata_tb.show(5)


# We can see the column variables we have with the `.labels` attribute:

# In[ ]:


metadata_tb.labels


# To clarify:
# <ol><li>Filename: Name of file on disk</li>
# <li>ID: Unique ID in Piper corpus</li>
# <li>Language: Language of novel</li>
# <li>Date: Initial publication date</li>
# <li>Title: Title of novel</li>
# <li>Gender: Authorial gender</li>
# <li>Person: Textual perspective</li>
# <li>Length: Number of tokens in novel</li></ol>

# We see a list of `filename`s in the table, these map into a folder we
# have called `txtlab_Novel150_English`:

# In[ ]:

# We can then read in the full text for each novel by iterating through
# the column, reading each file and appending the string to our
# `novel_list`:

# In[ ]:


# create empty list, entries will be list of tokens from each novel
novel_list = []

# iterate through filenames in metadata table
for filename in metadata_tb['filename']:

    # read in novel text as single string, make lowercase
    with open('data/txtlab_Novel150_English/' + filename, 'r') as f:
        novel = f.read()

    # clean up for TM analysis
    toks = novel.split()
    # quick & dirty no titles/proper nouns
    toks = [t for t in toks if not t.istitle() and not t.isupper()]
    novel = ' '.join(toks)

    # add list of tokens to master list
    novel_list.append(novel)


# Let's double check they all came through:

# In[ ]:


len(novel_list)


# And look at the first 200 characters of the fourth novel:

# In[ ]:


metadata_tb['author'][3], metadata_tb['title'][3], novel_list[3][:200]


# ---
#
# ## Document Term Matrix
#
# Now we need to make a document term matrix, just as we have in the past
# two classes. We can the pull in our `CountVectorizer` from `sklearn`
# again to create our dtm:

# In[ ]:


from sklearn.feature_extraction.text import CountVectorizer


# While you may not have seen the importance of `max_features`, `max_df` and `min_df` before, today you'll see just how much this can affect your results.
#
# Let's start out with this:
#
# - `max_features` = 5000  (i.e. only include 5000 tokens in our dtm)
# - `max_df` = .8  (i.e. don't keep any tokens that appear in > 80% of the documents)
# - `min_df` = 5  (i.e. only keep the token if it appears in > 5 documents)
#
# We'll add in a `stop_words='english'` too:

# In[ ]:


cv = CountVectorizer(
    max_features=5000,
    stop_words='english',
    max_df=0.80,
    min_df=5)


# As with most machine learning approaches, to validate your model you
# need training and testing partitions. Since we don't have any labels, we
# just need to do this for the novel strings:

# In[ ]:


train = novel_list[:120]
test = novel_list[120:]


# Now we can use our `cv` to `fit_transform` our training list of novels
# (strings!):

# In[ ]:


dtm = cv.fit_transform(train)


# To get our words back out we'll `.get_feature_names()`

# In[ ]:


dtm_feature_names = cv.get_feature_names()


# We can double check that our feature limit was enforced by calling `len`
# on the `dtm_feature_names`:

# In[ ]:


len(dtm_feature_names)


# We can throw this into a `Table` like we have before too:

# In[ ]:


dtm_tb = Table(dtm_feature_names).with_rows(dtm.toarray())
dtm_tb.show(5)


# ---
#
# ## Topic Modeling
#
# ### [Latent Dirichlet Allocation (LDA)](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) Models
# LDA reflects an intuition that words in a text are not merely chosen at random but are drawn from underlying concepts (the so-called "latent variables"). The goal of LDA is to look across many texts in order to reverse engineer these concepts by finding words that tend to cluster with one another. For this reason, LDA has been referred to as "the mother of all word collocation techniques."
#
# Instead of writing out the complicated math, `sklearn` has the
# `LatentDirichletAllocation` function:

# In[ ]:


from sklearn.decomposition import LatentDirichletAllocation


np.random.seed(0)  # sets the random seed to ensure reproducible results

# In[ ]:


try_topic_n = list(range(5, 200, 5))
try_topic_n


# In[ ]:
import multiprocessing as mp


def try_topic_number(i):
    lda = LatentDirichletAllocation(n_components=i, max_iter=1)
    lda_model = lda.fit(dtm)
    test_dtm = cv.transform(test)
    p = lda_model.perplexity(test_dtm)
    ll = lda_model.score(test_dtm)
    return p, ll

#  removing processes argument makes the code run on all available cores
pool = mp.Pool()
results = pool.map_async(try_topic_number, try_topic_n)
print(results.get())

import pickle

pickle.dump(results.get(), open('scores.pkl', 'wb'))
