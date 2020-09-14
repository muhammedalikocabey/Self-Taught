# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 17:34:01 2020

@author: muham
"""

import numpy as np 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/drug200.csv



df = pd.read_csv("drug200.csv", delimiter=",")

print("First 5 row of Data\n", df[0:5])


X = df[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values
print("\n\nFirst 5 row of X\n", X[0:5])


from sklearn.preprocessing import LabelEncoder

le_sex = LabelEncoder()
le_sex.fit(['F', 'M'])

X[:, 1] = le_sex.transform(X[:, 1])


# le_BP = LabelEncoder()
# le_BP.fit(['NORMAL', "HIGH"])
# X[:, (2)] = le_BP.transform(X[:, (2)])

le_Chol = LabelEncoder()
le_Chol.fit(['NORMAL', 'HIGH'])
X[:, 3] = le_Chol.transform(X[:, 3])

y = df['Drug']


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=3)

print("\n\nTrain shape: ", X_train.shape, " - ", y_train.shape)
print("Test shape: ", X_test.shape, " - ", y_test.shape)


from sklearn.tree import DecisionTreeClassifier

dec_tree = DecisionTreeClassifier(criterion='entropy', max_depth=4)
print("\n\nTree: ", dec_tree)

dec_tree.fit(X_train, y_train)


