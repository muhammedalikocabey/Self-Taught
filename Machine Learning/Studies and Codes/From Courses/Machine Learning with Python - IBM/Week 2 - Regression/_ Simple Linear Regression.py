# -*- coding: utf-8 -*-
"""
@author: Muhammed Ali Kocabey
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


cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]

print("\n\n\n", df.head(9))


#%%

# viz = cdf[['CYLINDERS', 'ENGINESIZE', 'CO2EMISSIONS', 'FUELCONSUMPTION_COMB']]
# viz.hist()
# plt.show()




# plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS, color='blue')
# plt.xlabel("FUELCONSUMPTION_COMB")
# plt.ylabel('Emissions')
# plt.show()



# plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color='blue')
# plt.xlabel('Engine Size')
# plt.ylabel('Emissions')
# plt.show()


# plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS, color='blue')
# plt.xlabel('Cylinders')
# plt.ylabel('Emissions')
# plt.show()


#%%

msk = np.random.rand(len(df)) < 0.8

train = cdf[msk]
test = cdf[~msk]


# plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue')
# plt.title('Train Set EngineSize with Emissions')
# plt.xlabel('Engine Size')
# plt.ylabel('Emissions')
# plt.show()


from sklearn.linear_model import LinearRegression

linear_reg = LinearRegression()

train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])

linear_reg.fit(train_x, train_y)


# The Coefficients

print('\n\n\nCoefficients : ', linear_reg.coef_)
print('Intercept: ', linear_reg.intercept_)


# plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue')
# plt.plot(train_x, linear_reg.coef_[0][0]*train_x + linear_reg.intercept_[0], '-r')
# plt.title('Linear Model with Data')
# plt.xlabel('Engine Size')
# plt.ylabel('Emissions')


#%%

from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
y_pred = linear_reg.predict(test_x)

print("\n\n\nMean Absolute Error: %.2f" % np.mean(np.absolute(y_pred - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((y_pred - test_y) ** 2))
print("R2-Score: %.2f" % r2_score(y_pred, test_y))







