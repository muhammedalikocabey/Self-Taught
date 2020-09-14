# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 03:37:56 2020

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
from sklearn.metrics import confusion_matrix




from sklearn.tree import DecisionTreeClassifier

dec_tree_classifier = DecisionTreeClassifier(criterion="entropy")

dec_tree_classifier.fit(X_train, y_train)

y_pred = dec_tree_classifier.predict(x_test)


cm = confusion_matrix(y_test, y_pred)

print(cm)





