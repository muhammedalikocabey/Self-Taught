# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 05:21:30 2020

@author: muham
"""



import pandas as pd 

from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("veriler.csv")

le = LabelEncoder()


x = df.iloc[: , 1:4].values
y = df.iloc[: , 4:].values

y = le.fit_transform(y) # 0 erkek, 1 kadın


#%%
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)


#%%
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)


from sklearn.tree import DecisionTreeClassifier

dec_tree = DecisionTreeClassifier(criterion="entropy")


dec_tree.fit(X_train, y_train)

y_pred = dec_tree.predict(X_test)


from sklearn.metrics import accuracy_score

acc = accuracy_score(y_test, y_pred)



from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)


print("DTC")
print(cm)






