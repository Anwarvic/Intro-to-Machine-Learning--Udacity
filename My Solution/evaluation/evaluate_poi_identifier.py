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
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

from sklearn import tree
from sklearn.metrics import accuracy_score

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
#acc = accuracy_score(labels_test, pred)
#print "Accuracy: ", acc

"""
temp = 0
for x in pred:
	if x == 1:
		temp = temp + 1

print "Number of POI in predictions is: ", temp
print "Number of people in the test set for classifier is", len(labels_test)

temp2 = 0
for i in range(29):
	if (labels_test[i] == 1 and pred[i] == 1):
		temp2 = temp2+1

print temp2

from sklearn.metrics import recall_score
from sklearn.metrics import precision_score

recall = recall_score(labels_test, pred)
precision = precision_score(labels_test, pred)
print "Recall: ", recall
print "Percision: ", precision
"""
from sklearn.metrics import recall_score
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

print recall_score(true_labels, predictions)