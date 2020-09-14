# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 23:30:13 2020

@author: muham
"""

import pandas as pd
import numpy as np

#%% Get Data from online
# from sklearn.datasets import fetch_openml

# mnist = fetch_openml('mnist_784', version=1)
# print(mnist.keys())

# X, y = mnist["data"], mnist["target"]


#%% Get data to Local
# X_df = pd.DataFrame(X, columns=mnist["feature_names"])
# y_df = pd.DataFrame(y, columns=["target"])

# X_df.to_csv("mnist_data.csv", index=False)
# y_df.to_csv("mnist_target.csv", index=False)


X_df = pd.read_csv("mnist_data.csv")
y_df = pd.read_csv("mnist_target.csv")


X = X_df.to_numpy()
y = y_df.to_numpy()



#%%
# import matplotlib as mpl
# import matplotlib.pyplot as plt

some_digit = X[0]
# some_digit_image = some_digit.flatten().reshape(28,28)

# plt.imshow(some_digit_image, cmap=mpl.cm.binary, interpolation="nearest")
# plt.axis="off"
# plt.show()

# print(y[0])

#%%

X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]

y_train_5 = (y_train==5)
y_test_5 = (y_test==5)

#%%
# from sklearn.linear_model import SGDClassifier

# sgd_clf = SGDClassifier(random_state=42)
# sgd_clf.fit(X_train, y_train_5)


#%% Now have we trained our model. Lets get save it and continue with the trained model

from sklearn.externals import joblib


#   # Saving Model
# joblib.dump(sgd_clf, "sgd_clf_mnist_model.pkl")


  # Loading Mode
sgd_clf = joblib.load("sgd_clf_mnist_model.pkl")


#%% Performance Measurement

# from sklearn.model_selection import StratifiedKFold
# from sklearn.base import clone 

# skfolds = StratifiedKFold(n_splits=3, random_state=2, shuffle=True)

# for train_index, test_index in skfolds.split(X_train, y_train_5):
#     clone_clf = clone(sgd_clf)
    
#     X_train_folds = X_train[train_index]
#     y_train_folds = y_train_5[train_index]
    
#     X_test_folds = X_train[test_index]
#     y_test_folds = y_train_5[test_index]
    
#     clone_clf.fit(X_train_folds, y_train_folds)
#     y_pred = clone_clf.predict(X_test_folds)
#     n_correct = sum(y_pred == y_test_folds)
    
#     print(n_correct / len(y_pred))
    
    

# from sklearn.model_selection import cross_val_score

# print(cross_val_score(sgd_clf, X_train, y_train_5, cv=3, scoring="accuracy"))


# from sklearn.base import BaseEstimator

# class Never5Classifier(BaseEstimator):
#     def fit(self, X, y=None):
#         pass
#     def predict(self, X):
#         return np.zeros((len(X), 1), dtype=bool)

# never_5_clf = Never5Classifier()

# print(cross_val_score(never_5_clf, X_train, y_train_5, cv=3, scoring="accuracy"))


#%% 

# from sklearn.model_selection import cross_val_score

# y_train_pred = cross_val_score(sgd_clf, X_train, y_train, cv=3)
# #   = [0.87365, 0.85835,0.8689]


# #%%

# from sklearn.metrics import confusion_matrix


# conf_mat = confusion_matrix(y_train_5, y_train_pred)


#%%

from sklearn.model_selection import cross_val_predict
y_scores = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3,
                             method="decision_function")



