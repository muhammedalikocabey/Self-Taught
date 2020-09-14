# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 16:58:59 2020

@author: muham
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("eksikveriler.csv")



from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()

ulke_label_encoding_df = df.iloc[:, 0:1].values

ulke_label_encoding_df[:,0] = label_encoder.fit_transform(ulke_label_encoding_df[:,0])





from sklearn.preprocessing import OneHotEncoder

ulke_one_hot_encoding_df = df.iloc[:, 0:1].values

one_hot_encoder = OneHotEncoder()


ulke_one_hot_encoding_df = one_hot_encoder.fit_transform(ulke_one_hot_encoding_df).toarray()









