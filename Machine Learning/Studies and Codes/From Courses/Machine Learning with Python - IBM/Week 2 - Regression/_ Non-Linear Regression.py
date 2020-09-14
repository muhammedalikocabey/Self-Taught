# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 11:03:35 2020

@author: muham
"""

import numpy as np
import matplotlib.pyplot as plt 

    # Y = ax^3 + bx^2 + cx + d
    

x = np.arange(-5.0, 5.0, 0.1)


y = 2*(x) + 3


y_noise = 2 * np.random.normal(size=x.size)

ydata = y + y_noise

# plt.figure(figsize = (8,6))
# plt.plot(x, ydata, "bo")
# plt.plot(x, y, 'r')
# plt.xlabel('Independent Variable')
# plt.ylabel('Dependent Variable')
# plt.show()


#%%
    
    # Y = log(ax^3 + bx^2 + cx + d)
    
    
    
x = np.arange(-5.0, 5.0, 0.1)

y = 1*(x ** 3) + 1 * (x ** 2) + 1 * x + 3

y_noise = 20 * np.random.normal(size=x.size)

ydata = y + y_noise


# plt.plot(x, ydata,  'bo')
# plt.plot(x, y, 'r') 
# plt.xlabel('Indepdendent Variable')
# plt.ylabel('Dependent Variable')
# plt.show()


#%% Quadratic

    # Y = X^2
    
    
    
x = np.arange(-5.0, 5.0, 0.1)

y = np.power(x,2)

y_noise = 2 * np.random.normal(size=x.size)

ydata = y + y_noise

# plt.plot(x, ydata,  'bo')
# plt.plot(x,y, 'r') 
# plt.xlabel('Indepdendent Variable')
# plt.ylabel('Dependent Variable')
# plt.show()


#%% Exponential

    # Y = a + bc^x
    
    
    
X = np.arange(-5.0, 5.0, 0.1)

Y= np.exp(X)

# plt.plot(X,Y) 
# plt.xlabel('Indepdendent Variable')
# plt.ylabel('Dependent Variable')
# plt.show()


#%% Logarithmic

    # Y = log(x)
    
    

X = np.arange(-5.0, 5.0, 0.1)

Y = np.log(X)

# plt.plot(X,Y) 
# plt.xlabel('Indepdendent Variable')
# plt.ylabel('Dependent Variable')
# plt.show()



#%% Sigmoidal/Logistic

    # Y = a + fracb1 + c^(x-d)
    
    
    
X = np.arange(-5.0, 5.0, 0.1)


Y = 1-4/(1+np.power(3, X-2))

# plt.plot(X,Y) 
# plt.xlabel('Indepdendent Variable')
# plt.ylabel('Dependent Variable')
# plt.show()


#%% Non-Linear Regression Example

# Data
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-Coursera/labs/Data_files/china_gdp.csv

import pandas as pd


df = pd.read_csv("china_gdp.csv")

print("\n\n\nFirst 10 row Data\n", df.head(10))

x_data, y_data = (df["Year"].values, df["Value"].values)

# plt.figure(figsize=(8,5))
# plt.plot(x_data, y_data, 'ro')
# plt.ylabel('GDP')
# plt.xlabel('Year')
# plt.show()


#%%

def sigmoid(x, beta_1, beta_2):
    y = 1 / (1 + np.exp(-beta_1 * (x - beta_2)))
    return y


beta_1 = 0.10
beta_2 = 1990.0


y_pred = sigmoid(x_data, beta_1, beta_2)


# plt.plot(x_data, y_pred*15000000000000.)
# plt.plot(x_data, y_data, 'ro')


#%% Normalize

xdata = x_data / max(x_data)
ydata = y_data / max(y_data)


from scipy.optimize import curve_fit

popt, pcov = curve_fit(sigmoid, x_data, y_data)

print("\n\n\nbeta_1 = %f,  beta_2 = %f" % (popt[0], popt[1]))


