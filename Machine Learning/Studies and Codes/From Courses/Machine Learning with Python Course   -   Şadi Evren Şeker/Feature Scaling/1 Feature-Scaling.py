# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 22:20:43 2020

@author: muham
"""

import pandas as pd
import numpy as np

from sklearn.preprocessing import OneHotEncoder

from sklearn.impute import SimpleImputer

import statistics

df = pd.read_csv("eksikveriler.csv")




imputer = SimpleImputer(missing_values=np.nan, strategy='mean')



boy = df.iloc[: , 1:2].values
boy_df = pd.DataFrame(data=boy, index=range(len(boy)), columns=["boy"])


kilo = df.iloc[: , 2:3].values
kilo_df = pd.DataFrame(data=kilo, index=range(len(kilo)), columns=["kilo"])


yas = df.iloc[: , 3:4].values
yas = imputer.fit_transform(yas)
yas_df = pd.DataFrame(data=yas, index=range(len(yas)), columns=["yas"] )


ulke = df.iloc[: , 0:1].values
one_hot_encoder = OneHotEncoder()
ulke = one_hot_encoder.fit_transform(ulke).toarray()
ulke_df = pd.DataFrame(data=ulke, index=range(len(ulke)), columns=["fr", "tr", "us"])

cinsiyet = df.iloc[: , -1:]
cinsiyet_df = pd.DataFrame(data=cinsiyet, index=range(len(cinsiyet)), columns=["cinsiyet"])




all_df = pd.concat([ulke_df, boy_df, kilo_df, yas_df, cinsiyet_df], axis=1)

all_df2 = all_df.copy()


boy_min_val = min(boy)
boy_max_val = max(boy)
boy_mean = (sum(boy) / len(boy))
boy_stdev = np.std(boy)

kilo_min_val = min(kilo)
kilo_max_val = max(kilo)
kilo_mean = (sum(kilo) / len(kilo))
kilo_stdev = np.std(kilo)

yas_min_val = min(yas)
yas_max_val = max(yas)
yas_mean = (sum(yas) / len(yas))
yas_stdev = np.std(yas)


all_df["boy_standardisation"] = None
all_df["boy_normalisation"] = None

all_df["kilo_standardisation"] = None
all_df["kilo_normalisation"] = None

all_df["yas_standartisation"] = None
all_df["yas_normalisation"] = None


for i in all_df.index:
    all_df["boy_standardisation"][i] = (all_df["boy"][i] - boy_mean)/boy_stdev
    all_df["boy_normalisation"][i] = ((all_df["boy"][i] - boy_min_val) / (boy_max_val - boy_min_val))
    
    all_df["kilo_standardisation"][i] = (all_df["kilo"][i] - kilo_mean) / kilo_stdev
    all_df["kilo_normalisation"][i] = ((all_df["kilo"][i] - kilo_min_val) / (kilo_max_val - kilo_min_val))

    all_df["yas_standartisation"][i] = (all_df["yas"][i] - yas_mean) / yas_stdev
    all_df["yas_normalisation"][i] = ((all_df["yas"][i] - yas_min_val) / (yas_max_val - yas_min_val))
    
     

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split((pd.concat([ulke_df, boy_df, kilo_df, yas_df], axis=1)), cinsiyet_df, test_size=0.33, random_state=0)
from sklearn.preprocessing import StandardScaler

standart_scaler = StandardScaler()

x_t = standart_scaler.fit_transform(x_train)







