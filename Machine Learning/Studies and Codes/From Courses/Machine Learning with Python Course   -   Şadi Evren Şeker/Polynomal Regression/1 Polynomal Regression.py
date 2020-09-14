# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 17:09:25 2020

@author: muham
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("maaslar.csv")



x = df.iloc[: , 1:2]
X = x.values

y = df.iloc[: , 2:]
Y = y.values


#%% Linear Reg
from sklearn.linear_model import LinearRegression

linear_reg = LinearRegression()

linear_reg.fit(X, Y)


# plt.scatter(X, Y, color="red")
# plt.plot(x, linear_reg.predict(X), color="blue")


#%% Polynomal Reg

from sklearn.preprocessing import PolynomialFeatures

polynomal_reg = PolynomialFeatures(degree = 8)


x_poly = polynomal_reg.fit_transform(X)

print(x_poly)

linear_reg_2 = LinearRegression()

linear_reg_2.fit(x_poly, y)

plt.scatter(X, Y, color="red")
plt.plot(X, linear_reg_2.predict(polynomal_reg.fit_transform(X)), color="blue")





