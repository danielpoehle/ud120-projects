#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn import cross_validation
from sklearn import grid_search

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

feat_train, feat_test, lab_train, lab_test = cross_validation.train_test_split(features, labels, test_size = 0.3, random_state = 42)

ctr = 0
for tst in lab_test:
    if tst == 1:
        ctr += 1

print "Number of POIs in the test set: ", ctr

clf = DecisionTreeClassifier()
clf.fit(feat_train, lab_train)

pred = clf.predict(feat_test)

print "Accuracy: ", accuracy_score(pred, lab_test)
print "Precision: ", precision_score(pred, lab_test)
print "Recall : ", recall_score(pred, lab_test)





