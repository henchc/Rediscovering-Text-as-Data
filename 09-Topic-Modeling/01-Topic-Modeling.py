from datascience import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


metadata_tb = Table.read_table('data/txtlab_Novel150_English.csv')

np.random.seed(0)
metadata_tb = Table.from_df(metadata_tb.to_df().sample(frac=1))

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


from sklearn.feature_extraction.text import CountVectorizer


cv = CountVectorizer(
    max_features=5000,
    stop_words='english',
    max_df=0.80,
    min_df=5)

train = novel_list[:120]
test = novel_list[120:]

dtm = cv.fit_transform(train)

dtm_feature_names = cv.get_feature_names()


from sklearn.decomposition import LatentDirichletAllocation


try_topic_n = list(range(5, 200, 5))
try_topic_n


import pickle
from joblib import Parallel, delayed
import multiprocessing


def try_topic_number(i):
    lda = LatentDirichletAllocation(n_components=i, max_iter=1000)
    lda_model = lda.fit(dtm)
    test_dtm = cv.transform(test)
    p = lda_model.perplexity(test_dtm)
    ll = lda_model.score(test_dtm)
    return p, ll

if __name__ == '__main__':

    num_cores = multiprocessing.cpu_count()

    results = Parallel(n_jobs=num_cores)(delayed(try_topic_number)(i)
                                         for i in try_topic_n)

    pickle.dump(results, open('scores.pkl', 'wb'))
