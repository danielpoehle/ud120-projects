#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop( "TOTAL", 0 ) 
data = featureFormat(data_dict, features)


### your code below

i = 0

for point in data:
    salary = point[0]
    bonus = point[1]
    if bonus > 10000000:
        print i, salary, bonus
    matplotlib.pyplot.scatter( salary, bonus )
    i += 1

for name in data_dict:
    if data_dict[name]["bonus"] >= 5000000:
        print name, data_dict[name]["salary"], data_dict[name]["bonus"]

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

