
from datascience import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import gensim

metadata_tb = Table.read_table('../data/txtlab_Novel150_English.csv')

metadata_tb = Table.from_df(metadata_tb.to_df().sample(frac=1))

novel_list = []

# iterate through filenames in metadata table
for filename in metadata_tb['filename']:

    # read in novel text as single string, make lowercase
    with open('../data/txtlab_Novel150_English/' + filename, 'r') as f:
        novel = f.read()

    # clean up for TM analysis
    toks = novel.split()
    # quick & dirty no titles/proper nouns
    toks = [t for t in toks if not t.istitle() and not t.isupper()]
    novel = ' '.join(toks)

    # add list of tokens to master list
    novel_list.append(novel)


def fast_tokenizer(text):

    # Get a list of punctuation marks
    from string import punctuation

    # Iterate through text removing punctuation characters
    no_punct = "".join([char for char in text if char not in punctuation])

    # Split text over whitespace
    tokens = no_punct.split()

    return tokens

# Tokenize
noveltokens_list = [fast_tokenizer(novel.lower()) for novel in novel_list]
print(len(noveltokens_list))

# Create dictionary based on corpus tokens
# Each token is mapped to its own unique ID
dictionary = gensim.corpora.dictionary.Dictionary(noveltokens_list)

# Map lists of tokens to the dictionary IDs
dictionary.doc2bow(['pride', 'prejudice', 'pride'])

# Remove stopwords, (some!) proper names from dictionary
from nltk.corpus import stopwords, words
proper_names = [word.lower() for word in words.words() if word.istitle()]
bad_words = stopwords.words('english') + proper_names

# Map stopwords, proper names to dictionary IDs
stop_ids = [_id for _id, count in dictionary.doc2bow(bad_words)]

# Remove stopwords from dictionary mappings
dictionary.filter_tokens(bad_ids=stop_ids)

# Remove terms by document frequency
dictionary.filter_extremes(no_below=15)

# Create list of dictionary mappings by novel
# This is gensim's version of a document-term matrix
corpus = [dictionary.doc2bow(doc) for doc in noveltokens_list]


try_topic_n = list(range(5, 200, 5))


import pickle
from joblib import Parallel, delayed
import multiprocessing


def try_topic_number(i):
    lda_model = gensim.models.LdaModel(
        corpus,
        num_topics=i,
        id2word=dictionary,
        iterations=1000,
        alpha='auto',
        passes=4)

    cm = gensim.models.CoherenceModel(
        model=lda_model,
        corpus=corpus,
        dictionary=dictionary,
        coherence='c_v')

    return cm.get_coherence()


if __name__ == '__main__':

    num_cores = multiprocessing.cpu_count()

    results = Parallel(n_jobs=num_cores)(delayed(try_topic_number)(i)
                                         for i in try_topic_n)

    print(results)
    pickle.dump(results, open('scores.pkl', 'wb'))
