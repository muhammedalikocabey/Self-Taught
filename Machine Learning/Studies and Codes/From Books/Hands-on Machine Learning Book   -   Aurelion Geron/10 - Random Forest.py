# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:27:54 2020

@author: muham
"""

import pandas as pd
import numpy as np

from sklearn.datasets import make_moons


moons_data = make_moons(n_samples=1000, noise=0.4)

X = moons_data[0]
y = moons_data[1]


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#%%     Random Forest Classifier

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

rnd_clf = RandomForestClassifier(n_estimators=500, max_leaf_nodes=16, n_jobs=-1)
rnd_clf.fit(X_train, y_train)

y_pred_rf = rnd_clf.predict(X_test)

from sklearn.metrics import accuracy_score

print("\n\nAccuracy: ", rnd_clf.__class__.__name__, " : ", accuracy_score(y_test, y_pred_rf))


bag_clf_equivalet_to_rnd_clf = BaggingClassifier(
    DecisionTreeClassifier(splitter="random", max_leaf_nodes=16),
    n_estimators=500, max_samples=1.0, bootstrap=True, n_jobs=-1)

bag_clf_equivalet_to_rnd_clf.fit(X_train, y_train)

y_pred = bag_clf_equivalet_to_rnd_clf.predict(X_test)

print("\n\nAccuracy: ", bag_clf_equivalet_to_rnd_clf.__class__.__name__, " : ", accuracy_score(y_test, y_pred))



#%%     Feature Importance

from sklearn.datasets import load_iris

iris = load_iris()

rnd_clf = RandomForestClassifier(n_estimators=500, n_jobs=-1)

rnd_clf.fit(iris["data"], iris["target"])

print("\n\n\n")


for name, score in zip(iris["feature_names"], rnd_clf.feature_importances_):
    print(name, score)


#%%     AdaBoost

from sklearn.ensemble import AdaBoostClassifier

ada_clf = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=1), n_estimators=200,
    algorithm="SAMME.R", learning_rate=0.5)

ada_clf.fit(X_train, y_train)

y_pred = ada_clf.predict(X_test)

print("\n\nAccuracy: ", ada_clf.__class__.__name__, " : ", accuracy_score(y_test, y_pred))


#%%     Gradient Boosting

from sklearn.ensemble import GradientBoostingRegressor

gbrt = GradientBoostingRegressor(max_depth=2, n_estimators=3, learning_rate=1.0)
gbrt.fit(X, y)

y_pred = gbrt.predict(X)

print("\n\nAccuracy: ", gbrt.__class__.__name__, " : ", accuracy_score(y, y_pred))












