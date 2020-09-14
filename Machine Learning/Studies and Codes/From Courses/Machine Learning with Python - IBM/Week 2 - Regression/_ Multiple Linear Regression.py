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



# plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
# plt.xlabel("Engine size")
# plt.ylabel("Emission")
# plt.show()


#%%

from sklearn.linear_model import LinearRegression

linear_reg = LinearRegression()

x = np.asanyarray(train[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB']])
y = np.asanyarray(train[['CO2EMISSIONS']])

linear_reg.fit(x, y)


# The Coefficients
print ('\n\n\nCoefficients: ', linear_reg.coef_)



y_pred = linear_reg.predict(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
x = np.asanyarray(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
y = np.asanyarray(test[['CO2EMISSIONS']])

print("\nResidual sum of squares: %.2f" % np.mean((y_pred - y) ** 2))



#%%

linear_reg2 = LinearRegression()

x = np.asanyarray(train[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', "FUELCONSUMPTION_HWY", ]])
y = np.asanyarray(train[['CO2EMISSIONS']])

linear_reg2.fit(x, y)

# The Coefficients
print("\n\n\nReg2 Coefficients: ", linear_reg2.coef_)


y_pred = linear_reg2.predict(test[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', "FUELCONSUMPTION_HWY", ]])
x = np.asanyarray(test[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', "FUELCONSUMPTION_HWY", ]])
y = np.asanyarray(test[['CO2EMISSIONS']])

print("\nResidual sum of squares: %.2f" % np.mean((y_pred - y) ** 2))














