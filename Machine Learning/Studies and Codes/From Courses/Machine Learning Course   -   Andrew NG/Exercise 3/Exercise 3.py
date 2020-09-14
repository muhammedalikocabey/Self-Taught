# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 03:19:30 2020

@author: muham
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat


#%%


def displayData(X, example_width=None, figsize=(10, 10)):
    """
    Displays 2D data stored in X in a nice grid.
    """
    # Compute rows, cols
    if X.ndim == 2:
        m, n = X.shape
    elif X.ndim == 1:
        n = X.size
        m = 1
        X = X[None]  # Promote to a 2 dimensional array
    else:
        raise IndexError('Input X should be 1 or 2 dimensional.')

    example_width = example_width or int(np.round(np.sqrt(n)))
    example_height = n / example_width

    # Compute number of items to display
    display_rows = int(np.floor(np.sqrt(m)))
    display_cols = int(np.ceil(m / display_rows))

    fig, ax_array = plt.subplots(display_rows, display_cols, figsize=figsize)
    fig.subplots_adjust(wspace=0.025, hspace=0.025)

    ax_array = [ax_array] if m == 1 else ax_array.ravel()

    for i, ax in enumerate(ax_array):
        ax.imshow(X[i].reshape(example_width, example_width, order='F'),
                  cmap='Greys', extent=[0, 1, 0, 1])
        ax.axis('off')
        
        
#%%

data = loadmat("Data/ex3data1.mat")


input_layer_size  = 400
num_labels = 10



m = data["y"].size

rand_indices = np.random.choice(m, 100, replace=False)

#%%

sel = data["X"][rand_indices, :]


#%%

def sigmoid(z):
    return 1 / (1 + np.exp(-z))


#%%

def cost(theta, X, y, learningRate):
    theta = np.matrix(theta)
    
    X = np.matrix(X)
    y = np.matrix(y)
    
    first = np.multiply(-y, np.log(sigmoid(X * theta.T)))
    second = np.multiply((1 - y), np.log(1 - sigmoid(X * theta.T)))
    
    reg = (learningRate / 2 * len(X)) * np.sum(np.power(theta[:, 1:theta.shape[1]], 2))

    return sum(first - second) / len(X) + reg


#%%

def gradient_with_loop(theta, X, y, learningRate):
    theta = np.matrix(theta)
    
    X = np.matrix(X)
    y = np.matrix(y)
    
    parameters = int(theta.ravel().shape[1])
    grad = np.zeros(parameters)
    
    error = sigmoid(X * theta.T) - y
    
    for i in range(parameters):
        term = np.multiply(error, X[:, i])
        
        if (i == 0):
            grad[i] = np.sum(term) / len(X)
            
        else:
            grad[i] = (np.sum(term)) / len(X) + ((learningRate / len(X)) * theta[:, i])

    return grad


#%%

def gradient(theta, X, y, learningRate):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    
    parameters = int(theta.ravel().shape[1])
    error = sigmoid(X * theta.T) - y
    
    grad = ((X.T * error) / len(X)).T + ((learningRate / len(X)) * theta)
    
    # intercept gradient is not regularized
    grad[0, 0] = np.sum(np.multiply(error, X[:,0])) / len(X)
    
    return np.array(grad).ravel()


#%%

from scipy.optimize import minimize
    
def one_vs_all(X, y, num_labels, learningRate):
    rows = X.shape[0]
    params = X.shape[1]
    
    all_theta = np.zeros((num_labels, params + 1))
    
    X = np.insert(X, 0, values=np.ones(rows), axis=1)

    for i in range(1, num_labels + 1):
        theta = np.zeros(params + 1)
        
        y_i = np.array([1 if label == i else 0 for label in y])
        y_i = np.reshape(y_i, (rows, 1))
        
        fmin = minimize(fun=cost, x0=theta, args=(X, y_i, learningRate), method="TNC", jac=gradient)
        
        all_theta[i-1, :] = fmin.x
        
    return all_theta



all_theta = one_vs_all(data["X"], data["y"], 10, 1)


#%%

def predict_all(X, all_theta):
    rows = X.shape[0]
    params = X.shape[1]
    num_labels = all_theta.shape[0]
    
    
    X = np.insert(X, 0, values=np.ones(rows), axis=1)
    
    X = np.matrix(X)
    
    all_theta = np.matrix(all_theta)
    
    
    h = sigmoid(X * all_theta.T)
    
    h_argmax = np.argmax(h, axis=1)
    
    h_argmax = h_argmax + 1
    
    return h_argmax


y_pred = predict_all(data["X"], all_theta)

correct = [1 if a == b else 0 for (a, b) in zip(y_pred, data['y'])]

accuracy = (sum(map(int, correct)) / float(len(correct)))

print("Accuracy = ", (accuracy * 100))


    








