#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import cross_validation
from sklearn import grid_search


sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

feat_train, feat_test, lab_train, lab_test = cross_validation.train_test_split(features, labels, test_size = 0.3, random_state = 42)



### it's all yours from here forward!  

parameters = {"splitter": ("best", "random"),
              "max_depth":  [2,3,4,5,10,100,1000, None],
              "min_samples_split": [2,5,10]}

tr = DecisionTreeClassifier()
clf = grid_search.GridSearchCV(tr, parameters)
clf.fit(feat_train, lab_train)

pred = clf.predict(feat_test)
print accuracy_score(pred, lab_test)
print clf.best_estimator_


