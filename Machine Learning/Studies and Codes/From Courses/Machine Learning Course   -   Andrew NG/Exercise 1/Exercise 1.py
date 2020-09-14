# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 18:22:37 2020

@author: muham
"""

import os

import numpy as np

import  matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D




#%%     Simple Numpy Function

def warUpExercise():
    A = np.eye(5)
    
    return A 


# b = warUpExercise()


#%%     Linear Regression with one variable

data = np.loadtxt("Data/ex1data1.txt", delimiter=',')

# First Column  = Population of a city
# Second Column = Profit of a food truck in that city
    # Negative value indicates a loss.
    
x, y = data[:, 0], data[:, 1]
m = y.size


def plotData(x, y):
    fig = plt.figure()
    
    plt.plot(x, y, "ro", ms=10, mec="k")
    plt.ylabel("Profit in $10,000")
    plt.xlabel("Population of City in 10,000s")
    
    

# plotData(x, y)


#%%     Cost Function and Gradient Descent

x = x[:, np.newaxis]
y = y[:, np.newaxis]

theta = np.zeros([2,1])
iterations = 1500
alpha = 0.01
ones = np.ones((m, 1))
X = np.hstack((ones, x))


def computeCost(X, y, theta):
    temp = np.dot(X, theta) - y
    return np.sum(np.power(temp, 2)) / (2*m)
    

J = computeCost(X, y, theta)

# print("Cost Function for Theta = ", theta, "\n\nCost = ", J)



def gradientDescent(x, y, theta, alpha, iterations):
    for _ in range(iterations):
        temp = np.dot(X, theta) - y
        temp = np.dot(X.T, temp)
        theta = theta - (alpha / m) * temp
        
    return theta

theta = gradientDescent(X, y, theta, alpha, iterations)

# print("\n\n\nCost Function for Theta:\n", theta, "\n\nCost = ", computeCost(X, y, theta))


# plotData(X[:, 1], y)
# plt.plot(X[:, 1], np.dot(X, theta), "-")
# plt.legend(["Training Data", "Linear Regression"])


#%%     Linear Regression with multiple variables

import pandas as pd

data2 = np.loadtxt("Data/ex1data2.txt", delimiter=',')
data2 = pd.DataFrame(data2)

x = data2.iloc[:, 0:2] 
    # First Column  = size of the house
    # Second Column = number of bedrooms
    
y = data2.iloc[:, 2]
    # Third Column  = Price of the house
    
m = len(y) # number of training examples

# print(data2.head(10))


#%%     Feature Normalization

x = (x - np.mean(x)) / np.std(x)


#%%     Cost Function for Multivariable 
ones = np.ones((m,1))

x = np.hstack((ones, x))

alpha = 0.01

iterations = 400

theta = np.zeros((3, 1))

y = y[:, np.newaxis]

def computeCostMulti(x, y, theta):
    temp = np.dot(x, theta) - y
    return np.sum(np.power(temp, 2)) / (2 * m)


J = computeCostMulti(x, y, theta)

print("Cost Function for Theta\n", theta, "\n\nCost = ", J)


#%%     Gradient Descent for Multivariable

def gradientDescentMulti(x, y, theta, alpha, iterations):
    m = len(y)
    
    for _ in range(iterations):
        temp = np.dot(x, theta) - y
        temp = np.dot(x.T, temp)
        theta = theta - (alpha / m) * temp
        
    return theta

theta = gradientDescentMulti(x, y, theta, alpha,  iterations)

print("\n\n\nTheta for ", iterations, " iterations == ", theta)

J = computeCostMulti(x, y, theta)

print("\n\n\nCost Function for Theta\n", theta, "\n\nCost = ", J)


#%%

plotData(x[:, 1], y)
plt.plot(x[:, 1], np.dot(x, theta), "-")
plt.legend(['Training data', 'Linear regression'])




