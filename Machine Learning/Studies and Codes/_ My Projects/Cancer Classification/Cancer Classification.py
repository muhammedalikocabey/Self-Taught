# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 03:34:25 2020

@author: muham
"""


from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()


print("Length of data :", len(data["data"]))

print("\n\nLength of features : ", len(data["feature_names"]))

print("\n\nFeature names:\n", data["feature_names"])


#%%

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
X, y = data["data"], data["target"]

    
    
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


from sklearn.linear_model import LogisticRegressionCV
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC



from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

log_reg = LogisticRegressionCV(max_iter=4000)
gauss_nb = GaussianNB()
lin_disc_analy = LinearDiscriminantAnalysis()
svc = SVC(kernel="rbf")

print("\n\n\n")


from plot_learning_curve import *

for model in (log_reg, gauss_nb, lin_disc_analy, svc):
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    ac_sc = accuracy_score(y_test, y_pred)
    rc_sc = recall_score(y_test, y_pred, average="weighted")
    pr_sc = precision_score(y_test, y_pred, average="weighted")
    f1_sc = f1_score(y_test, y_pred, average="micro")
    
    # results.append([i, ac_sc, rc_sc, pr_sc, f1_sc])
    
    print("Model = ", model.__class__.__name__, "\nAccuracy = ", ac_sc, "\nRecall = ", rc_sc, "\nPrecision = ", pr_sc, "\nF1 = ", f1_sc, "\n\n\n")
    
    plot_learning_curve(model, model.__class__.__name__, X, y)

