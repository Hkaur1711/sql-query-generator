"""
    Author: Ankit Dutta <cruxbeaker>
    Naive Bayes spam detection for NLP
    dataset: http://www.cs.jhu.edu/~mdredze/datasets/sentiment/index2.html
"""

from __future__ import print_function, division
from future.utils import iteritems
from builtins import range

import nltk
import numpy as np

from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag, ne_chunk
from sklearn.linear_model import LogisticRegression
from bs4 import BeautifulSoup

wordnet_lemmatizer = WordNetLemmatizer()

# from http://www.lextek.com/manuals/onix/stopwords1.html
stopwords = set(w.rstrip() for w in open('./stopwords.txt'))

doc = "Visuaize all the  product codes of the city Paris?"
print("Input: ", doc)
doc = doc.lower()
# tokenize doc
tokenized_doc = nltk.word_tokenize(doc)
 
# tag sentences and use nltk's Named Entity Chunker
tagged_sentences = nltk.pos_tag(tokenized_doc)
ne_chunked_sents = nltk.ne_chunk(tagged_sentences)
print(tagged_sentences)

# extract all named entities
def posToSql(tagged_sentences):
    noun_list = []
    adj_list = []
    for tagged_tree in tagged_sentences:
        if tagged_tree[1] == 'NN' or tagged_tree[1] == 'NNP' or tagged_tree[1] == 'NNS':
            noun_list.append(tagged_tree[0])
        elif tagged_tree[1] == 'JJ':
            adj_list.append(tagged_tree[0])

    if(len(adj_list) == 0):
        sql_obj = {'target_col' : noun_list[0], 'cond_col' : noun_list[-2], 'val' : noun_list[-1]}
    else:
        sql_obj = {'target_col' : noun_list[0], 'cond_col' : noun_list[-1], 'val' : adj_list[-1]+'('+noun_list[-1]+')'}
    # print("Noun List: ", noun_list)
    # print("Adjective List: ", adj_list)
    
    return sql_obj

sql_obj = posToSql(tagged_sentences)

sql_query = "SELECT '{target_col}' from 'sales' WHERE '{cond_col}'='{val}'".format(target_col=sql_obj['target_col'], 
cond_col=sql_obj['cond_col'], val=sql_obj['val'])
print("SQL: ", sql_query)