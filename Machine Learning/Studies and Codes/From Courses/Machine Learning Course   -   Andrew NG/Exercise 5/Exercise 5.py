# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 04:41:00 2020

@author: muham
"""

import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt


data = loadmat("Data/ex5data1.mat")

X = data["X"]
y = data["y"].ravel()

X_test = data["Xtest"]
y_test = data["ytest"].ravel()

X_val = data["Xval"]
y_val = data["yval"].ravel()

m = X.shape[0]

m_val = X_val.shape[0]
m_test = X_test.shape[0]


#%%

# plt.figure()
# plt.plot(X, y, linestyle='', marker='x', color='r')
# plt.xlabel("Change in water level (X)")
# plt.ylabel("Water flowing out of the dam (y)")
# plt.show()


#%%

def linear_reg_cost_function(theta, X, y, l):
    m = X.shape[0]
    
    J = 1.0 / (2 * m) * np.sum(np.square(X.dot(theta) - y)) + 1.0 * l / (2 * m) * np.sum(np.square(theta[1:]))
    
    mask = np.eye(len(theta))
    mask[0, 0] = 0
    
    grad = 1.0 / m * X.T.dot(X.dot(theta) - y) + 1.0 * l / m * (mask.dot(theta))
    
    return J, grad
    

theta = np.array([1, 1])
J, Grad = linear_reg_cost_function(theta, np.hstack((np.ones((m, 1)), X)), y, 1)

print("Cost J = ", J, "\n\nGrad:\n", Grad)


#%%

import scipy.optimize as opt

def train_linear_reg(X, y, l, iteration=200):
    m, n = X.shape
    
    initial_theta = np.zeros((n,1))
    
    result = opt.minimize(fun=linear_reg_cost_function, x0=initial_theta, args=(X, y, l), method='TNC',
                          jac=True, options={'maxiter':iteration})
    
    return result.x


l = 0.0

theta = train_linear_reg(np.hstack((np.ones((m,1)), X)), y, l)

pred = np.hstack((np.ones((m, 1)), X)).dot(theta)


# plt.figure()
# plt.plot(X, y, linestyle='', marker='x', color='r')
# plt.plot(X, pred, linestyle='--', marker=''6, color='b')
# plt.xlabel('Change in water level (x)')
# plt.ylabel('Water flowing out of the dam (y)')
# plt.show()


#%%

def learning_curve(X, y, X_val, y_val, l):
    m = X.shape[0]
    m_val = X_val.shape[0]
    error_train = np.zeros(m)
    error_val = np.zeros(m)
    
    for i in range(1, m+1):
        theta = train_linear_reg(X[:i,], y[:i,], l)
        
        error_train[i - 1] = 1.0 / (2 * i) * np.sum(np.square(X[:i, ].dot(theta) - y[:i, ]))
        error_val[i - 1] = 1.0 / (2 * m_val) * np.sum(np.square(X_val.dot(theta) - y_val))

    return error_train, error_val



l = 0.0
error_train, error_val = learning_curve(np.hstack((np.ones((m, 1)), X)), y, np.hstack((np.ones((m_val, 1)), X_val)), y_val, l)

# plt.figure()
# plt.plot(range(1, m + 1), error_train, color='b', label='Train')
# plt.plot(range(1, m + 1), error_val, color='r', label='Cross Validation')
# plt.legend(loc='upper right')
# plt.xlabel('Number of training examples')
# plt.ylabel('Error')
# plt.show()

print ('\n\n\nTraining Examples / Train Error / Cross Validation Error')
for i in range(m):
    print ('  {0:<19} {1:<13.8f} {2:<.8f}'.format(i + 1, error_train[i], error_val[i]))


#%%

aaa = X[: 1]

def poly_features(X, p):
    X_poly = np.zeros((len(X), p))
    
    for i in range(p):
        X_poly[:, i] = np.power(X, i+1).ravel()
        
        
    return X_poly

#%%

def feature_normalize(X, mu=None, sigma=None):
    if mu is None:
        mu = np.mean(X, axis=0)
        
    if sigma is None:
        sigma = np.std(X, ddof=1, axis=0)
    
    X_norm = (X-mu) / sigma
    
    return X_norm, mu, sigma


p = 8

X_poly = poly_features(X, p)
X_poly, mu, sigma = feature_normalize(X_poly)
X_poly = np.hstack((np.ones((m, 1)), X_poly))

X_poly_test = poly_features(X_test, p)
X_poly_test, dummy_mu, dummy_sigma = feature_normalize(X_poly_test, mu, sigma)
X_poly_test = np.hstack((np.ones((m_test, 1)), X_poly_test))

X_poly_val = poly_features(X_val, p)
X_poly_val, dummy_mu, dummy_sigma = feature_normalize(X_poly_val, mu, sigma)
X_poly_val = np.hstack((np.ones((m_val, 1)), X_poly_val))

print('\n\n\nNormalized Training Example 1:')
print(X_poly[0, :])


#%%

def plot_fit(min_x, max_x, mu, sigma, theta, p):
    x = np.arange(min_x-15, max_x+25, 0.05)
    
    X_poly = poly_features(x, p)
    X_poly, dummy_mu, dummy_sigma = feature_normalize(X_poly, mu, sigma)
    X_poly = np.hstack((np.ones((X_poly.shape[0], 1)), X_poly))
    
    plt.plot(x, X_poly.dot(theta), linestyle='--', marker='', color='b')
    
    
    
l = 0.0
theta = train_linear_reg(X_poly, y, l, iteration=500)

plt.figure()
plt.plot(X, y, linestyle='', marker='x', color='r')
plot_fit(np.min(X), np.max(X), mu, sigma, theta, p)
plt.xlabel('Change in water level (x)')
plt.ylabel('Water flowing out of the dam (y)')
plt.title('Polynomial Regression Fit (lambda = {})'.format(l))
plt.show()
    


error_train, error_val = learning_curve(X_poly, y, X_poly_val, y_val, l)
plt.figure()
plt.plot(range(1, m + 1), error_train, color='b', marker='v', label='Train')
plt.plot(range(1, m + 1), error_val, color='r', label='Cross Validation')
plt.legend(loc='upper right')
plt.title('Polynomial Regression Learning Curve (lambda = {})'.format(l))
plt.xlabel('Number of training examples')
plt.ylabel('Error')
plt.show()


#%%

def validation_curve(x, y, x_val, y_val):
    lambda_vec = np.array([0, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10])
    error_train = np.zeros(len(lambda_vec))
    error_val = np.zeros(len(lambda_vec))
    m = x.shape[0]
    m_val = x_val.shape[0]
    for i in range(len(lambda_vec)):
        l = lambda_vec[i]
        theta = train_linear_reg(x, y, l)
        error_train[i] = 1.0 / (2 * m) * np.sum(np.square(x.dot(theta) - y))
        error_val[i] = 1.0 / (2 * m_val) * np.sum(np.square(x_val.dot(theta) - y_val))

    return lambda_vec, error_train, error_val


lambda_vec, error_train, error_val = validation_curve(X_poly, y, X_poly_val, y_val)

plt.figure()
plt.plot(lambda_vec, error_train, color='b', label='Train')
plt.plot(lambda_vec, error_val, color='r', label='Cross Validation')
plt.legend(loc='upper right')
plt.xlabel('lambda')
plt.ylabel('Error')
plt.show()

print('# lambda / Train Error / Validation Error')
for i in range(len(lambda_vec)):
    print('  {0:<8} {1:<13.8f} {2:<.8f}'.format(lambda_vec[i], error_train[i], error_val[i]))
    