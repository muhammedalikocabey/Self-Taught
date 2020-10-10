#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 11:52:06 2020

@author: makocabey
"""

import nltk
from nltk.corpus import movie_reviews
import random

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)


all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())

word_features = list(all_words)[:2000]


def document_features(document):
    document_words = set(document)
    features = {}
    
    for word in word_features:
        features['contains({}]'.format(word)] = (word in document_words)
        
    return features


feature_sets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = feature_sets[100:], feature_sets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)


print(nltk.classify.accuracy(classifier, test_set))


print("\n\n", classifier.show_most_informative_features(5))
