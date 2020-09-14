# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 06:15:06 2020

@author: muham
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

moons_data = make_moons(n_samples=1000, noise=0.4)

X = moons_data[0]
y = moons_data[1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

log_clf = LogisticRegression()
rnd_clf = RandomForestClassifier()
svm_clf = SVC()

voting_clf = VotingClassifier(
    estimators=[("lr", log_clf), ("rf", rnd_clf), ("svc", svm_clf)],
    voting="hard")

voting_clf.fit(X_train, y_train)


from sklearn.metrics import accuracy_score

for clf in (log_clf, rnd_clf, svm_clf, voting_clf):
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("\nAccuracy: ", clf.__class__.__name__, accuracy_score(y_test, y_pred))
    
    
#%%     Bagging and Pasting

from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

bag_clf = BaggingClassifier(
    DecisionTreeClassifier(), n_estimators=500,
    max_samples=100, bootstrap=True, n_jobs=-1)

bag_clf.fit(X_train, y_train)

y_pred = bag_clf.predict(X_test)

print("\n\nAccuracy: ", bag_clf.__class__.__name__, accuracy_score(y_test, y_pred))


#%%     Out-of-Bag Evaluation

bag_clf_oob = BaggingClassifier(
    DecisionTreeClassifier(), n_estimators=500,
    bootstrap=True, n_jobs=-1, oob_score=True)

bag_clf_oob.fit(X_train, y_train)


print("\n\nOOB Score ", bag_clf_oob.__class__.__name__, bag_clf_oob.oob_score_)

y_pred = bag_clf_oob.predict(X_test)
print("Accuracy: ", bag_clf_oob.__class__.__name__, accuracy_score(y_test, y_pred))



