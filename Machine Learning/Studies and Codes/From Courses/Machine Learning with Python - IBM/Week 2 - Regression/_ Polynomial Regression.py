# -*- coding: utf-8 -*-
"""
@author: Muhammed Ali KOCABEY
"""

import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np



# We have downloaded a fuel consumption dataset, FuelConsumption.csv, 
    # which contains model-specific fuel consumption ratings and estimated carbon dioxide
    # emissions for new light-duty vehicles for retail sale in Canada. Dataset source =
    # https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-Coursera/labs/Data_files/FuelConsumptionCo2.csv
    

# MODELYEAR e.g. 2014
# MAKE e.g. Acura
# MODEL e.g. ILX
# VEHICLE CLASS e.g. SUV
# ENGINE SIZE e.g. 4.7
# CYLINDERS e.g 6
# TRANSMISSION e.g. A6
# FUEL CONSUMPTION in CITY(L/100 km) e.g. 9.9
# FUEL CONSUMPTION in HWY (L/100 km) e.g. 8.9
# FUEL CONSUMPTION COMB (L/100 km) e.g. 9.2
# CO2 EMISSIONS (g/km) e.g. 182 --> low --> 0





df = pd.read_csv('FuelConsumptionCo2.csv')

print("Top 5 row in the Data\n", df.head(5))

print("\n\n\nDescribe Data\n", df.describe())



cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
print("\n\n\nCdf Top 10 row\n", cdf.head(10))


#%%

# plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
# plt.xlabel("Engine size")
# plt.ylabel("Emission")
# plt.show()




msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]


#%%

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])

test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])


poly = PolynomialFeatures(degree=2)
train_x_poly = poly.fit_transform(train_x)


#%%

clf = LinearRegression()
train_y_ = clf.fit(train_x_poly, train_y)

# The coefficients
print ('\n\nCoefficients: ', clf.coef_)
print ('Intercept: ',clf.intercept_)


#%%

# plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
# XX = np.arange(0.0, 10.0, 0.1)
# yy = clf.intercept_[0]+ clf.coef_[0][1]*XX+ clf.coef_[0][2]*np.power(XX, 2)
# plt.plot(XX, yy, '-r' )
# plt.xlabel("Engine size")
# plt.ylabel("Emission")


#%%

from sklearn.metrics import r2_score

test_x_poly = poly.fit_transform(test_x)
y_pred = clf.predict(test_x_poly)

print("\n\n\nMean absolute error: %.2f" % np.mean(np.absolute(y_pred - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((y_pred - test_y) ** 2))
print("R2-score: %.2f" % r2_score(y_pred , test_y) )


#%% Practice

poly3 = PolynomialFeatures(degree=3)

train_x_poly3 = poly3.fit_transform(train_x)

clf3 = LinearRegression()

train_y3_ = clf3.fit(train_x_poly3, train_y)


# The coefficients
print ('\n\n\nCoefficients: ', clf3.coef_)
print ('Intercept: ',clf3.intercept_)

plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')

XX = np.arange(0.0, 10.0, 0.1)

yy = clf3.intercept_[0]+ clf3.coef_[0][1]*XX + clf3.coef_[0][2]*np.power(XX, 2) + clf3.coef_[0][3]*np.power(XX, 3)

plt.plot(XX, yy, '-r' )
plt.xlabel("Engine size")
plt.ylabel("Emission")

test_x_poly3 = poly3.fit_transform(test_x)
test_y3_ = clf3.predict(test_x_poly3)

print("\n\nMean absolute error: %.2f" % np.mean(np.absolute(test_y3_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y3_ - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y3_ , test_y) )

















