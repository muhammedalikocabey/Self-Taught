# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 00:18:47 2020

@author: muham
"""


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("satislar.csv")



# aylar = df.iloc[: , 0:1].values
# aylar_df = pd.DataFrame(data=aylar, index=range(len(aylar)), columns=["ay"])
aylar_df = df[["Aylar"]]

# satislar = df.iloc[:, -1:].values
# satislar_df = pd.DataFrame(data=satislar, index=range(len(satislar)), columns=["satis"])
satislar_df = df[["Satislar"]]


# plt.xlabel("Aylar")
# plt.ylabel("Satışlar")
# plt.scatter(aylar, satislar)



from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(aylar_df, satislar_df, test_size = 0.33, random_state=0)



from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

Y_train = sc.fit_transform(y_train)
Y_test = sc.fit_transform(y_test)




# x_train = pd.DataFrame(data=x_train, index=range(len(x_train)), columns=["Aylar"])
# x_test = pd.DataFrame(data=x_test, index=range(len(x_test)), columns=["Aylar"])


# y_train = pd.DataFrame(data=y_train, index=range(len(y_train)), columns=["Satislar"])
# y_test = pd.DataFrame(data=y_test, index=range(len(y_test)), columns=["Satislar"])



from sklearn.linear_model import LinearRegression

linear_reg = LinearRegression()

linear_reg.fit(x_train, y_train)
    
prediction = linear_reg.predict(x_test) 
    

    

x_train = x_train.sort_index()
y_train = y_train.sort_index()


plt.plot(x_train, y_train)

plt.plot(x_test, linear_reg.predict(x_test))








    
    
    
    
    
    
    
