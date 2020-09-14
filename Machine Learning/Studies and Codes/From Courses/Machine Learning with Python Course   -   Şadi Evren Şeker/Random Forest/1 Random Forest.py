# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:22:06 2020

@author: muham
"""


#1. kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# veri yukleme
veriler = pd.read_csv('maaslar.csv')

x = veriler.iloc[:,1:2]
y = veriler.iloc[:,2:]
X = x.values
Y = y.values





from sklearn.ensemble import RandomForestRegressor

rand_for_reg = RandomForestRegressor(n_estimators=10, random_state=0)

rand_for_reg.fit(X, Y)

pred = rand_for_reg.predict([[6.6]])

plt.scatter(X, Y, color="red")
plt.plot(x, rand_for_reg.predict(X))




