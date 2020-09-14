# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 04:53:11 2020

@author: muham
"""


from sklearn.datasets import load_iris

from sklearn.tree import DecisionTreeClassifier



#%%


def visualize_tree(file_path, filename, data, tree_model):
    from sklearn.tree import export_graphviz
    
    file_path = file_path + filename + ".dot"
    
    with open(file_path, "w") as f:
        
        export_graphviz(
            tree_model,
            out_file=f,
            feature_names=data.feature_names[2:],
            class_names=data.target_names,
            rounded=True,
            filled=True)
    
    
    import os
    os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz 2.44.1/bin'
    
    from graphviz import Source
    
    output = Source.from_file(file_path, format="png")
    output.view()


#%%

iris = load_iris()


X = iris.data[:, 2:] # petal length and width
y = iris.target


#%%     Decision Tree Classifier

tree_clf = DecisionTreeClassifier(max_depth=2)

tree_clf.fit(X, y)


#%%     Decision Tree Visualization

path = "C:/Users/muham/Desktop/"
filename = "tree_depth2"

visualize_tree(path, filename, iris, tree_clf)


#%% 

print(tree_clf.predict_proba([[5, 1.5]]))
print(tree_clf.predict([[5, 1.5]]))