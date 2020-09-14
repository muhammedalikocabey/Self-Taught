# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 05:18:12 2020

@author: muham
"""

import numpy as np
import pandas as pd

X = 2 * np.random.rand(100,1)
y = 4 + 3 * X + np.random.randn(100,1)


#%%
import matplotlib.pyplot as plt

# plt.plot(X, y, "ro")


#%%

X_b = np.c_[np.ones((100,1)), X]
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)


X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2,1)), X_new]

y_predict = X_new_b.dot(theta_best)
print(y_predict)

# plt.plot(X_new, y_predict, "r-")
# plt.plot(X,y, "b.")
# plt.axis([0, 2, 0, 15])
# plt.show()


#%%

from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()

lin_reg.fit(X, y)

print("\n\n\n", lin_reg.intercept_, lin_reg.coef_)

print("\n\n\n---------------------------------------------------\n\n\n")


#%%

theta_best_svd, residuals, rank, s = np.linalg.lstsq(X_b, y, rcond=1e-6)


print("\n\n\nNormal Equation\n", np.linalg.pinv(X_b).dot(y))

print("\n\n\n---------------------------------------------------\n\n\n")


#%%

eta = 0.1 # learning rate
n_iterations = 1000
m = 100

theta = np.random.randn(2, 1) # random initialization




for iteration in range(n_iterations):
    gradients = 2 / m * X_b.T.dot(X_b.dot(theta) - y)
    theta = theta - eta * gradients
    



print("\nLast Theta from Batch Gradient Descent\n", theta)
# that’s exactly what the Normal Equation found!

print("\n\n\n---------------------------------------------------\n\n\n")


#%% 

n_epochs = 50
t0, t1 = 5, 50 # learning schedule hyperparameters

def learning_schedule(t):
    return t0 / (t + t1)

theta = np.random.randn(2, 1)


for epoch in range(n_epochs):
    for i in range(m):
        random_index = np.random.randint(m)
        
        xi = X_b[random_index : random_index+1]
        yi = y[random_index : random_index+1]
        
        gradients = 2 * xi.T.dot(xi.dot(theta) - yi)
        
        eta = learning_schedule(epoch * m + i)
        
        theta = theta - eta * gradients
        
        
print("\nLast Theta from Stochastic Gradient Descent\n", theta)


#           ----- or ------

from sklearn.linear_model import SGDRegressor

sgd_reg = SGDRegressor(max_iter=1000, tol=1e-3, penalty=None)
sgd_reg.fit(X, y.ravel())

# close to the one returned by the Normal Equation
print("\n\n\nStochastig Gradient Descent\n", sgd_reg.intercept_, sgd_reg.coef_)
        
print("\n\n\n---------------------------------------------------\n\n\n")


#%% Polynomial Regression

m = 100
X = 6 * np.random.randn(m, 1) - 3
    
# plt.plot(X, "b.")


from sklearn.preprocessing import PolynomialFeatures

poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X)



print("\nX[0] = ", X[0])
print("\n\n\nX_poly[0] = ", X_poly[0])


lin_reg = LinearRegression()
lin_reg.fit(X_poly, y)
y_poly_pred = lin_reg.predict(X_poly)

print("\n\n\nIntercept = ", lin_reg.intercept_, "\tCoef = ", lin_reg.coef_)



from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def plot_learning_curves(model, X, y):
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)
    
    train_errors, val_errors = [], []
    
    for m in range (1, len(X_train)):
        model.fit(X_train[:m], y_train[:m])
        
        y_train_predict = model.predict(X_train[:m])
        y_val_predict = model.predict(X_val)
        
        train_errors.append(mean_squared_error(y_train[:m], y_train_predict))
        val_errors.append(mean_squared_error(y_val, y_val_predict))
        
    plt.plot(np.sqrt(train_errors), "r-+", linewidth=2, label="train")
    plt.plot(np.sqrt(val_errors), "b-", linewidth=3, label="val")
    plt.legend()
    
lin_reg = LinearRegression()
# plot_learning_curves(lin_reg, X, y)
    

#%%

from sklearn.pipeline import Pipeline

polynomial_regression = Pipeline([
    ("poly_features", PolynomialFeatures(degree=10, include_bias=False)),
    ("lin_reg", LinearRegression()),
    ])

plot_learning_curves(polynomial_regression, X, y)

print("\n\n\n---------------------------------------------------\n\n\n")


#%% Ridge Regression

from sklearn.linear_model import Ridge

ridge_reg = Ridge(alpha=1, solver="cholesky")
ridge_reg.fit(X, y)

print("Ridge Regression Predict\n ", ridge_reg.predict([[1.5]]))


sdg_reg = SGDRegressor(penalty='l2')
sgd_reg.fit(X, y.ravel())

print("\n\n\n", sgd_reg.predict([[1.5]]))

print("\n\n\n---------------------------------------------------\n\n\n")


#%% Lasso Regression

from sklearn.linear_model import Lasso

lasso_reg = Lasso(alpha=0.1)
lasso_reg.fit(X, y)

print("Lasso Regression Predict\n", lasso_reg.predict([[1.5]]))

print("\n\n\n---------------------------------------------------\n\n\n")


#%% Elastic Net

from sklearn.linear_model import ElasticNet

elastic_net = ElasticNet(alpha=0.1, l1_ratio=0.5)

elastic_net.fit(X, y)

print("Elastic Net Predict ", elastic_net.predict([[1.5]]))

print("\n\n\n---------------------------------------------------\n\n\n")


#%% Early Stop

from sklearn.base import clone
from sklearn.preprocessing import StandardScaler
# prepare the data

poly_scaler = Pipeline([
    ("poly_features", PolynomialFeatures(degree=90, include_bias=False)),
    ("std_scaler", StandardScaler())
    ])

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)


X_train_poly_scaled = poly_scaler.fit_transform(X_train)
X_val_poly_scaled = poly_scaler.transform(X_val)


sgd_reg = SGDRegressor(max_iter=1, tol=-np.infty, warm_start=True,
                       penalty=None, learning_rate="constant", eta0=0.0005)


minimum_val_error = float("inf")

best_epoch = None
best_model = None

for epoch in range(1000):
    sgd_reg.fit(X_train_poly_scaled, y_train)
    y_val_predict = sgd_reg.predict(X_val_poly_scaled)
    val_error = mean_squared_error(y_val, y_val_predict)
    if val_error < minimum_val_error:
        minimum_val_error = val_error
        best_epoch = epoch
        best_model = clone(sgd_reg)











































