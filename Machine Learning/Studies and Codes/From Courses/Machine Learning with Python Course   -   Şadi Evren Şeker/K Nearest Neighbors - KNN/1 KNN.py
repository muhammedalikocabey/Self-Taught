# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 16:37:06 2020

@author: muham
"""

import pandas as pd 

df = pd.read_csv("veriler.csv")



x = df.iloc[: , 1:4].values
y = df.iloc[: , 4:].values



#%%
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)



#%%
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)


#%%
from sklearn.linear_model import LogisticRegression

logistic_reg = LogisticRegression(random_state=0)

logistic_reg.fit(X_train, y_train)



y_pred = logistic_reg.predict(X_test)
print(y_pred)
print(y_test)


#%%
from sklearn.metrics import confusion_matrix

conf_matrix = confusion_matrix(y_test, y_pred)



#%%

from sklearn.neighbors import KNeighborsClassifier

knn_classifier = KNeighborsClassifier(n_neighbors=1, metric='minkowski')


knn_classifier.fit(X_train, y_train)


y_pred_knn = knn_classifier.predict(X_test)


cm_knn = confusion_matrix(y_test, y_pred_knn)



























from sklearn.neighbors import KNeighborsClassifier

knn_classifier = KNeighborsClassifier()

