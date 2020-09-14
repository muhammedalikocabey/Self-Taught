# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 14:29:02 2020

@author: muham
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("eksikveriler.csv")



from sklearn.impute import SimpleImputer


imputer = SimpleImputer(missing_values=np.nan, strategy='mean')


yas = df.iloc[:,1:4].values

imputer = imputer.fit(yas[:,1:4])

yas[:,1:4] = imputer.transform(yas[:,1:4])
