# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 21:00:49 2020

@author: muham
"""

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt



data = pd.read_csv("Data/ex2data1.txt", header=None, names=["Exam 1", "Exam 2", "Admitted"])


X = data.iloc[:, 0:2]

y = data.iloc[:, 2]


#%%

def plot_data(data):
    positive = data[data["Admitted"].isin([1])]
    negative = data[data["Admitted"].isin([0])]
    
    fig, ax = plt.subplots(figsize=(10,5))
    ax.scatter(positive["Exam 1"], positive["Exam 2"], s=50, c='b', marker="o", label="Admitted")
    ax.scatter(negative["Exam 1"], negative["Exam 2"], s=50, c='r', marker="x", label="Not Admitted")
    ax.legend()
    ax.set_xlabel("Exam 1  Score")
    ax.set_ylabel("Exam 2  Score")
  
    
  
        # Show Data        
# plot_data(data)




#%%

m, n = X.shape
theta = np.zeros(n + 1)

X = np.hstack((np.ones((m, 1)), X))



def sigmoid(z):
    g = 1 / (1 + np.exp(-z))
    return g

nums = np.arange(-10, 10, step=1)

    # Draw Sigmoid Function
# fig, ax = plt.subplots(figsize=(10,4))
# ax.plot(nums, sigmoid(nums), "r")


#%%

a = np.matrix(y)

def cost(X, y, theta):
    theta = np.matrix(theta)
    
    X = np.matrix(X)
    y = np.matrix(y)
    
    first = np.multiply(-y ,np.log(sigmoid(X * theta.T)))
    second = np.multiply((1-y), np.log(1 - sigmoid(X * theta.T)))
    
    return np.sum(first - second) / (len(X))


cost = cost(X, y, theta)




#%%

data.insert(0, "ones", 1)

cols = data.shape[1]
X = data.iloc[:, 0:cols-1]
y = data.iloc[:, cols-1:cols]

X = np.array(X.values)
y = np.array(y.values)

theta = np.zeros(3)


print("X.shape = ", X.shape, "\ntheta.shape = ", theta.shape, "\ny.shape = ", y.shape)

print("\n\nCost\n", cost)


#%%
    
def gradient(theta, X, y):
    theta = np.matrix(theta)
    
    X = np.matrix(X)
    y = np.matrix(y)
    
    parameters = int(theta.ravel().shape[1])
    grad = np.zeros(parameters)

    error = sigmoid(X * theta.T) - y

    for i in range(parameters):
        term = np.multiply(error, X[:, i])
        grad[i] = np.sum(term) / len(X)
        
    return grad


print("\n\n1 Step Gradient Descent Result:\n", gradient(theta, X, y))





