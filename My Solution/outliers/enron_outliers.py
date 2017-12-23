#!/usr/bin/python

import numpy as np
import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
###notice that data is a numpy array not dictionary as they say !!

#First Outlier (Total)
print data.argmax(axis=0)	#gets the index of the maximum point, which is [67]
max_value = data [67]				#this is the maximum value 
print max_value
data = np.delete(data, (67), axis=0)

#Second Outlier (LAVORATO JOHN J)
print data.argmax(axis=0)	
max_value = data [26]
print max_value
data = np.delete(data, (26), axis=0)

#Third Outlier (LAY KENNETH L)
print data.argmax(axis=0)	
max_value = data [40]
print max_value
data = np.delete(data, (40), axis=0)





###visualization code
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()