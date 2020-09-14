# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 05:50:37 2020

@author: muham
"""


import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

veriler = pd.read_csv("musteriler.csv")



X = veriler.iloc[:, 3:].values







from sklearn.cluster import KMeans

km_cluster = KMeans(n_clusters=3, init='k-means++')

km_cluster.fit(X)

print(km_cluster.cluster_centers_)


sonuclar = list()


for i in range(1, 11): 
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=123)
    kmeans.fit(X)
    
    sonuclar.append(kmeans.inertia_)
    
    
plt.plot(range(1,11), sonuclar)