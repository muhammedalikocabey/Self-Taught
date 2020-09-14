# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 03:23:03 2020

@author: muham
"""


import numpy as np

from sklearn import datasets

from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler

from sklearn.svm import LinearSVC



    
iris = datasets.load_iris()

X = iris["data"][:, (2,3)] # petal length, petal width
y = (iris["target"] == 2).astype(np.float64) # If is Iris-Virginica == 1
                                                    # else == 0
                                                    
                                                   

#%%     SVM Classification
                                                    
svm_clf = Pipeline([
    ("scaler", StandardScaler()),
    ("linear_svc", LinearSVC(C=1, loss="hinge"))
    ])                                             

svm_clf.fit(X, y)   

print(svm_clf.predict([[5.5, 1.7]]))


#%%     Nonlinear SVM Classification

from sklearn.preprocessing import PolynomialFeatures

polynomial_svm_clf = Pipeline([
    ("poly_features", PolynomialFeatures(degree=3)),
    ("scaler", StandardScaler()),
    ("svm_clf", LinearSVC(C=10, loss="hinge"))
    ])

polynomial_svm_clf.fit(X, y)


print(polynomial_svm_clf.predict([[5.5, 1.7]]))


#%%     Kernel Trick

from sklearn.svm import SVC

poly_kernel_svm_clf_kernel_trick = Pipeline([
    ("scaler", StandardScaler()),
    ("svm_clf", SVC(kernel="poly", degree=3, coef0=1, C=5))
    ])

poly_kernel_svm_clf_kernel_trick.fit(X, y)





#%%     Gaussian RBF Kernel

rbf_kernel_svm_clf = Pipeline([
    ("scaler", StandardScaler()),
    ("svm_clf", SVC(kernel="rbf", gamma=5, C=0.0001))
    ])

rbf_kernel_svm_clf.fit(X, y)










