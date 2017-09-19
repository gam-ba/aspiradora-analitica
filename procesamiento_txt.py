import pandas as pd
import datetime as dt
import matplotlib as plt
import numpy as np
import logging
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from collections import defaultdict
from gensim import corpora, models, similarities

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

stop_words = set(stopwords.words('spanish'))
stemmer = SnowballStemmer('spanish')

def extract_stem(x):
    if type(x) == list:
        stemmed = []
        for i in x:
            stemmed.append(stemmer.stem(i))
        return stemmed
    else:
        return stemmer.stem('x')
        
def remove_stopwords(list):
    no_stopwords = []
    for i in list:
        if i not in stop_words:
            no_stopwords.append(i)
    return no_stopwords

def generate_dict(stemmed):
    frequency = defaultdict(int)
    for row in stemmed:
    for l in row:
        frequency[l] += 1
    return frequency

df = pd.read_csv('nombre_de_archivo', sep='\t', encoding='utf-8')
df['comments_token'] = df.comments_clean.apply(lambda x: word_tokenize(str(x)))
df['no_stopwords'] = df.comments_token.apply(remove_stopwords)
df['stemmed'] = df.no_stopwords.apply(extract_stem)

generate_dict(df.stemmed)
df['no_rarewords'] = [[token for token in row if frequency[token] > 1] for row in df.stemmed]

df_lista = df.no_rarewords.tolist()
dictionary = corpora.Dictionary(df_lista)
corpus = [dictionary.doc2bow(text) for text in df_lista]
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=300)
corpus_lsi = lsi[corpus_tfidf]
