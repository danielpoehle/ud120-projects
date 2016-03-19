#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm
from sklearn.metrics import accuracy_score

# reduce trainsig set size
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 
c_param = 10000

while c_param <= 10000:
    print "C= " + str(c_param)
    clf = svm.SVC(kernel = "rbf", C = c_param)

    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time:", round(time()-t0, 3), "s"

    t1 = time()
    pred = clf.predict(features_test)
    print "predicting time:", round(time()-t1, 3), "s"

    print "C= " + str(c_param)
    print accuracy_score(pred, labels_test)
    c_param = c_param * 10


print "Predictions No. 10, 26, 50:"
print pred[10]
print pred[26]
print pred[50]

print "Total Number of Predictions for Chris (1):"
print str(sum(pred))


#########################################################


