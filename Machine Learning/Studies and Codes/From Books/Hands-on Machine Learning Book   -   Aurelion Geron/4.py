# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 02:34:13 2020

@author: muham
"""

import pandas as pd

import numpy as np

from sklearn import datasets

import matplotlib.pyplot as plt

iris = datasets.load_iris()

# print(list(iris.keys()))

X = iris["data"][:, 3:] # petal width
y = (iris["target"] == 2).astype(np.int) # 1 if Iris-Virginica, else 0



#%%      Build classifier to detech the Iris-Virginica type
#           based only on the petal width feature

from sklearn.linear_model import LogisticRegression

log_reg = LogisticRegression()

log_reg.fit(X, y)

X_new = np.linspace(0, 3, 1000).reshape(-1, 1)
y_proba = log_reg.predict_proba(X_new)



# plt.plot(X_new, y_proba[:, 1], "g-", label="Iris-Virginica")
# plt.plot(X_new, y_proba[:, 0], "b--", label="Not Iris-Virginica")
# plt.legend()


# print(log_reg.predict([[1.7], [1.5]]))


#%%     Softmax Regression

X = iris["data"][:, (2,3)] # petal length, petal width
y = iris["target"]


softmax_reg = LogisticRegression(multi_class="multinomial", solver="lbfgs",
                                 C=10)
softmax_reg.fit(X, y)

print(softmax_reg.predict([[5, 2]]))

print(softmax_reg.predict_proba([[5, 2]]))














