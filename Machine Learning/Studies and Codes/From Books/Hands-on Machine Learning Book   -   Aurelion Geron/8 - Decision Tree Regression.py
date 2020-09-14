# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 05:40:58 2020

@author: muham
"""



from sklearn.datasets import make_moons

from sklearn.tree import DecisionTreeClassifier


#%%


def visualize_tree(file_path, filename, data, tree_model):
    from sklearn.tree import export_graphviz
    
    file_path = file_path + filename + ".dot"
    
    with open(file_path, "w") as f:
        
        export_graphviz(
            tree_model,
            out_file=f,
            # feature_names=data.feature_names[2:],
            # class_names=data.target_names,
            rounded=True,
            filled=True)
    
    
    import os
    os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz 2.44.1/bin'
    
    from graphviz import Source
    
    output = Source.from_file(file_path, format="png")
    output.view()


#%%
moons_data = make_moons()


X = moons_data[0]
y = moons_data[1]



#%%     Decision Tree Regression

from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor(max_depth=2)
tree_reg.fit(X, y)


path = "C:/Users/muham/Desktop/"
filename = "tree_reg_depth2"
visualize_tree(path, filename, moons_data, tree_reg)
