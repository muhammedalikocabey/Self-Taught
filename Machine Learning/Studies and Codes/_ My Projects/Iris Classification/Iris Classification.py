# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 17:15:13 2020

@author: muham
"""

import pandas as pd

import seaborn as sns
sns.set(color_codes=True)
import matplotlib.pyplot as plt
import sweetviz as sv
from pandas.plotting import parallel_coordinates

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv("Iris.csv")
df.drop(["Id"], axis=1, inplace=True)

X = df.iloc[:, :-1].values
y = df.iloc[:, -1:].values


le = LabelEncoder()

y = le.fit_transform(y)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=df["Species"], random_state=42)


#%%          Explaratory Data Analysis

    # Way 1
def EDA_way_1():
    print("Info\n", df.info())
    
    print("\n\n\nData Describe\n", df.describe())
    
    print("\n\n\nFirst 5 Row of Data\n", df.head())
    
    print("\n\n\nLast 5 Row of Data\n", df.tail())
    
    print("\n\n\nData Types\n", df.dtypes)
    
    print("\n\n\nCounting the number of rows\n", df.count())
    
    
    
    
    n_bins = 10
    fig, axs = plt.subplots(2, 2)
    axs[0,0].hist(df['SepalLengthCm'], bins = n_bins);
    axs[0,0].set_title('Sepal Length');
    axs[0,1].hist(df['SepalWidthCm'], bins = n_bins);
    axs[0,1].set_title('Sepal Width');
    axs[1,0].hist(df['PetalLengthCm'], bins = n_bins);
    axs[1,0].set_title('Petal Length');
    axs[1,1].hist(df['PetalWidthCm'], bins = n_bins);
    axs[1,1].set_title('Petal Width');
    
    fig.tight_layout(pad=1.0);
    
    
    
    fig, axs = plt.subplots(2, 2)
    fn = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
    cn = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    sns.boxplot(x = 'Species', y = 'SepalLengthCm', data = df, order = cn, ax = axs[0,0]);
    sns.boxplot(x = 'Species', y = 'SepalWidthCm', data = df, order = cn, ax = axs[0,1]);
    sns.boxplot(x = 'Species', y = 'PetalLengthCm', data = df, order = cn, ax = axs[1,0]);
    sns.boxplot(x = 'Species', y = 'PetalWidthCm', data = df,  order = cn, ax = axs[1,1]);
    # add some spacing between subplots
    fig.tight_layout(pad=1.0);

    sns.violinplot(x="Species", y="PetalLengthCm", data=df, size=5, order = cn, palette = 'colorblind');

    sns.pairplot(df, hue="Species", height = 2, palette = 'colorblind');
    
    
    corrmat = df.corr()
    sns.heatmap(corrmat, annot=True, square=True)
    
    
    parallel_coordinates(df, "Species", color = ['blue', 'red', 'green']);

    
# EDA_way_1()




    # Way 2 
def EDA_way_2():
    # analyze dataset
    advert_report = sv.analyze(df)
    
    # display the report
    advert_report.show_html('Advanced-EDA.html')


# EDA_way_2()


#%% 

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

from plot_learning_curve import *


#      Models
gradB_clf = GradientBoostingClassifier()
decTree_clf = DecisionTreeClassifier(max_depth=3, random_state=1)
knn_clf = KNeighborsClassifier()
nb_clf = GaussianNB()
logReg_clf = LogisticRegression()
svm_clf = SVC()





for model in (gradB_clf, decTree_clf, knn_clf, nb_clf, logReg_clf, svm_clf):
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    ac_sc = accuracy_score(y_test, y_pred)
    rc_sc = recall_score(y_test, y_pred, average="weighted")
    pr_sc = precision_score(y_test, y_pred, average="weighted")
    f1_sc = f1_score(y_test, y_pred, average="micro")
    
    # results.append([i, ac_sc, rc_sc, pr_sc, f1_sc])
    
    print("Model = ", model.__class__.__name__, "\nAccuracy = ", ac_sc, "\nRecall = ", rc_sc, "\nPrecision = ", pr_sc, "\nF1 = ", f1_sc, "\n\n\n")

    plot_learning_curve(model, model.__class__.__name__, X, y)
    
























