# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 21:29:15 2020

@author: muham
"""

import pandas as pd
import numpy as np 

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# df = pd.read_csv("anscombe.csv")

housing = pd.read_csv("housing.csv")


#%% Informations About Data
# print(housing.info)



# print("\n\n\n", housing.head(100))

# unique_proximity_values =  housing.ocean_proximity.unique()
# print(housing["ocean_proximity"].value_counts())

# print(housing.describe())

# housing.hist(bins=100, figsize=(40,30))
# plt.show()


#%% Train-Test Split

def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[: test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    
    return data.iloc[train_indices], data.iloc[test_indices]

train_set, test_set = split_train_test(housing, 0.2)

    
#%% 

# from zlib import crc32

# def test_set_check(identifier, test_ratio):
#     return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32

# def split_train_test_by_id(data, test_ratio, id_column):
#     ids = data[id_column]
#     in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
#     return data.loc[~in_test_set], data.loc[in_test_set]


# housing_with_id = housing.reset_index()
# train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")

# housing_with_id["id"] = housing["longitude"] * 1000 + housing["latitude"]


# train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")


#%%

from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
    

#%% Median Income to Categorical Attribute

housing["income_cat"] = pd.cut(housing["median_income"],
                                bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                                labels=[1,2,3,4,5])

# housing["income_cat"].hist()


#%% Strafied Sampling Based on the Income Category

from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]


# print(strat_test_set["income_cat"].value_counts() / len(strat_test_set))


#%% Removing Income Category 

for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)
    
    
#%% Visualizing the Data

housing_copy = strat_train_set.copy()

# Visualizing the Longitude and Latitude


# housing_copy.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
#                   s=housing_copy["population"]/100, label="population", figsize=(10,7),
#                   c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True)

# plt.legend()


#%% Correlations

corr_matrix = housing.corr()

from pandas.plotting import scatter_matrix

attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]

# scatter_matrix(housing[attributes], figsize=(12,8))


# housing.plot(kind="scatter", x="median_income", y="median_house_value")


#%% 

housing["rooms_per_household"] = housing["total_rooms"] / housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"] / housing["total_rooms"]
housing["population_per_household"] = housing["population"] / housing["households"]

corr_matrix = housing.corr()

# print(corr_matrix["median_house_value"].sort_values(ascending=False))


housing = strat_train_set.drop("median_house_value", axis=1)
housing_labels = strat_train_set["median_house_value"].copy()


#%% Missing Values 

# housing.dropna(subset=["total_bedrooms"]) # Option 1 for Missing Values

# housing.drop("total_bedrooms",) # Option 2 for Missing Values

# median = housing["total_bedrooms"].median() # Option 3 for Missing Values
# housing["total_bedrooms"].fillna(median, inplace=True)


# Alternative for Option 3 

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="median")

# Median can only be computed on numerical attributes we need drop ocean_proximity text values
housing_num = housing.drop("ocean_proximity", axis=1)

imputer.fit(housing_num)

# print(imputer.statistics_)

# print("\n\n", housing_num.median().values)

# We can use "Tranined" imputer for transform the training set

X = imputer.transform(housing_num)
# X is plain NumPy array containing the transformed features

housing_transformed = pd.DataFrame(X, columns=housing_num.columns)


#%% Handling Text and Categoring Values

housing_cat = housing[["ocean_proximity"]]
# print(housing_cat.head(10))


from sklearn.preprocessing import OrdinalEncoder

ordinal_encoer = OrdinalEncoder()

housing_cat_encoded = ordinal_encoer.fit_transform(housing_cat)

# print(housing_cat_encoded[:10])

# print("\n\n", ordinal_encoer.categories_)


from sklearn.preprocessing import OneHotEncoder

cat_encoder = OneHotEncoder()

housing_cat_1hot = cat_encoder.fit_transform(housing_cat)

arr_housing_cat_1hot = housing_cat_1hot.toarray()

      
#%% Custom Transformers

from sklearn.base import BaseEstimator, TransformerMixin

rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True): # no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household,
                         bedrooms_per_room]
        
        else:
            return np.c_[X, rooms_per_household, population_per_household]
        
attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False)
    
housing_extra_attribs = attr_adder.transform(housing.values)


#%% Feature Scaling

#   Transformation Pipelines

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy="median")),
    ("attribs_adder", CombinedAttributesAdder()),
    ("std_scaler", StandardScaler())
    ])

housing_num_tr = num_pipeline.fit_transform(housing_num)



from sklearn.compose import ColumnTransformer

num_attribs = list(housing_num)
cat_attribs = ["ocean_proximity"]

full_pipeline = ColumnTransformer([
    ("num", num_pipeline, num_attribs),
    ("cat", OneHotEncoder(), cat_attribs)
    ])

housing_prepared = full_pipeline.fit_transform(housing)


#%% Select and Train a Model

#       Training and Evaluating on the Training Set

from sklearn.linear_model import LinearRegression

# lin_reg = LinearRegression()
# lin_reg.fit(housing_prepared, housing_labels)


# some_data = housing.iloc[:5]
# some_labels = housing_labels.iloc[:5]

# some_data_prepared = full_pipeline.transform(some_data)

# print("Predictions: ", lin_reg.predict(some_data_prepared))
# print("Labels: ", list(some_labels))


from sklearn.metrics import mean_squared_error

# housing_predictions = lin_reg.predict(housing_prepared)

# lin_mse = mean_squared_error(housing_labels, housing_predictions)
# lin_rmse = np.sqrt(lin_mse)

# print("\t\tLinear Regression")
# print("Mean Squared Error = ", lin_mse)
# print("Root Mean Squared Error = ", lin_rmse)



#%% Lets Try with Decision Tree Regressor

from sklearn.tree import DecisionTreeRegressor

# tree_reg = DecisionTreeRegressor()

# tree_reg.fit(housing_prepared, housing_labels)

# tree_housing_predictions = tree_reg.predict(housing_prepared)

# tree_mse = mean_squared_error(housing_labels, tree_housing_predictions)

# tree_rmse = np.sqrt(tree_mse)

# print("\n\n\n\t\tDecision Tree Regressor")
# print("Mean Squared Error = ", tree_mse)
# print("Root Mean Squared Error = ", tree_rmse)


#%% Better Evaluation Using Cross-Validation

from sklearn.model_selection import cross_val_score

# scores = cross_val_score(tree_reg, housing_prepared, housing_labels,
#                          scoring="neg_mean_squared_error", cv=10)

# tree_rmse_scores = np.sqrt(-scores)


# def display_scores(model_name, scores):
#     print("\n\n\n\t\t",model_name)
#     print("Scores: ", scores)
#     print("\nMean: ", scores.mean())
#     print("Standart Deviation: ", scores.std())
    
# display_scores("Decision Tree Cross-Validation", scores)


# lin_scores = cross_val_score(lin_reg, housing_prepared, housing_labels,
#                              scoring="neg_mean_squared_error", cv=10)

# lin_rmse_scores = np.sqrt(-lin_scores)

# display_scores("Linear Regression Cross-Validation", lin_rmse_scores)




from sklearn.ensemble import RandomForestRegressor

# forest_reg = RandomForestRegressor()

# forest_reg.fit(housing_prepared, housing_labels)

# forest_scores = cross_val_score(forest_reg, housing_prepared, housing_labels,
#                          scoring="neg_mean_squared_error", cv=10) 

# forest_rmse_scores= np.sqrt(-forest_scores)

# display_scores("Random Forest Regressor Cross-Validation", forest_rmse_scores)


#%% Saving and Loading the Model

# from sklearn.externals import joblib


#   Saving Model
# joblib.dump(my_model, "my_model.pkl")


#   Loading Model
# my_model_loaded = joblib.load("my_model.pkl")


#%% Fine-Tune Model

#       Grid Search

from sklearn.model_selection import GridSearchCV

param_grid = [
    {'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
    {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]}
    ]

forest_reg = RandomForestRegressor()

grid_search = GridSearchCV(forest_reg, param_grid, cv=5,
                            scoring="neg_mean_squared_error",
                            return_train_score=True)

grid_search.fit(housing_prepared, housing_labels)


print(grid_search.best_params_)

print("\n\n\n", grid_search.best_estimator_)


cvres = grid_search.cv_results_

print("\n\n\n")
for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
    print(np.sqrt(-mean_score), params)


feature_importances = grid_search.best_estimator_.feature_importances_
print("\n\n\n\t\tFeature Importances\n", feature_importances)

extra_attribs = ["rooms_per_hhold", "pop_per_hhold", "bedrooms_per_room"]
cat_encoder = full_pipeline.named_transformers_["cat"]
cat_one_hot_attribs = list(cat_encoder.categories_[0])
attributes = num_attribs + extra_attribs + cat_one_hot_attribs

print("\n\n\n", sorted(zip(feature_importances, attributes), reverse=True))
      
      
#%% Final Model

final_model = grid_search.best_estimator_

X_test = strat_test_set.drop("median_house_value", axis=1)
y_test = strat_test_set["median_house_value"].copy()

X_test_prepared = full_pipeline.transform(X_test)

final_predictions = final_model.predict(X_test_prepared)

final_mse = mean_squared_error(y_test, final_predictions)
final_rmse = np.sqrt(final_mse)

print("\n\n\n\t\tFinal Model Scores\n")
print("Final Model Mean Squared Error: ", final_mse)
print("Final Model Root Mean Squared Error: ", final_rmse)







