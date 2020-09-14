# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 18:05:56 2020

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


ulke_df = pd.DataFrame(data=ulke_one_hot_encoding_df, index=range(22), columns=["fr", "tr", "us"])



boy_kilo_yas = df.iloc[: , 1:4].values
cinsiyet = df.iloc[: , -1:].values


boy_kilo_yas_df = pd.DataFrame(data=boy_kilo_yas, index=range(22), columns=["Boy", "Kilo","Yaş"])


cinsiyet_df = pd.DataFrame(data=cinsiyet, index=range(22), columns=["Cinsiyet"])


ulke_boy_kilo_yas_df = pd.concat([ulke_df, boy_kilo_yas_df], axis=1)







from sklearn.model_selection import train_test_split


x_train, x_test, y_train, y_test = train_test_split(ulke_boy_kilo_yas_df, cinsiyet_df, test_size=0.33, random_state=0)












