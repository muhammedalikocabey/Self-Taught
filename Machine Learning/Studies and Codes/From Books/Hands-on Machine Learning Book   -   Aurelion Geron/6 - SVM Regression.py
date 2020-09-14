# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 04:18:05 2020

@author: muham
"""

import pandas as pd

import numpy as np

from sklearn import datasets



iris = datasets.load_iris()

X = iris["data"][:, (2,3)] # petal length, petal width
y = (iris["target"] == 2).astype(np.float64) # If is Iris-Virginica == 1
                                                    # else == 0
                                                    
                                                    
#%%     Linear - Support Vector Regression

from sklearn.svm import LinearSVR

svm_reg = LinearSVR(epsilon=1.5)

svm_reg.fit(X, y)


#%%     Support Vector Regression

from sklearn.svm import SVR

svm_poly_reg = SVR(kernel="poly", degree=2, C=100, epsilon=0.1) 

svm_poly_reg.fit(X, y)

