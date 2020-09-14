# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 22:56:19 2020

@author: muham
"""


import pandas as pd
import numpy as np

df = pd.read_csv("veriler.csv")


ulke = df.iloc[: , 0:1].values
ulke_df = pd.DataFrame(data=ulke, index=range(len(ulke)), columns=["ulke"])

boy = df.iloc[: , 1:2].values
boy_df = pd.DataFrame(data=boy, index=range(len(boy)), columns=["boy"])

kilo = df.iloc[: , 2:3].values
kilo_df = pd.DataFrame(data=kilo, index=range(len(kilo)), columns=["kilo"])

yas = df.iloc[: , 3:4].values
yas_df = pd.DataFrame(data=yas, index=range(len(yas)), columns=["yas"])

cinsiyet = df.iloc[: , -1:].values
cinsiyet_df = pd.DataFrame(data=cinsiyet, index=range(len(cinsiyet)), columns=["cinsiyet"])


#%%

from sklearn.preprocessing import OneHotEncoder

one_hot_encoder = OneHotEncoder()


ulke_ohe = one_hot_encoder.fit_transform(ulke).toarray()
ulke_ohe_df = pd.DataFrame(data=ulke_ohe, index=range(len(ulke_ohe)), columns=["fr", "tr", "us"])

cinsiyet_ohe = one_hot_encoder.fit_transform(cinsiyet).toarray()
cinsiyet_ohe_df = pd.DataFrame(data=cinsiyet_ohe[:, 0:1], index=range(22), columns=["cinsiyet"])


all_df_ex_cnsyt = pd.concat([ulke_ohe_df, boy_df, kilo_df, yas_df], axis=1)


#%%

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(all_df_ex_cnsyt, cinsiyet_ohe_df, test_size=0.33, random_state=0)


#%%

from sklearn.linear_model import LinearRegression

linear_regressor = LinearRegression()

linear_regressor.fit(x_train, y_train)


y_pred = linear_regressor.predict(x_test)


#%%



all_df_ex_boy = pd.concat([ulke_ohe_df, kilo_df, yas_df, cinsiyet_ohe_df], axis=1)


x2_train, x2_test, y2_train, y2_test = train_test_split(all_df_ex_boy, boy_df, test_size=0.33, random_state=0)


linear_regressor_2 = LinearRegression()

linear_regressor_2.fit(x2_train, y2_train)

y2_pred = linear_regressor_2.predict(x2_test)
 

#%% 

import statsmodels.api as smf

X = np.append(arr = np.ones((22,1)).astype(int), values=all_df_ex_boy, axis=1)

X_l = all_df_ex_boy.iloc[:, [0,1,2,3,5]].values

r_ols = smf.OLS(endog = boy, exog = X_l).fit()

print(r_ols.summary())
