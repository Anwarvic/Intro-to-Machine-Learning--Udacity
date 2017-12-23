#!/usr/bin/python
import numpy as np
"""
    Clean away the 10% of points that have the largest
    residual errors (difference between the prediction
    and the actual net worth).

    Return a list of tuples named cleaned_data where 
    each tuple is of the form (age, net_worth, error).
"""

############### FOR TESTING ####################################
"""
from random import randint
ages = []
net_worths = []
predictions = []
for i in range (10):
    ages.append(randint(0,9))
    net_worths.append(randint(0,9))
    predictions.append(randint(0,9))
print "%s\n%s\n%s" %(ages, net_worths, predictions)
"""
################################################################
def outlierCleaner(predictions, ages, net_worths):
    cleaned_data = []
    max_value = 0
    ### your code goes here
    residual_error = list( abs(np.array(predictions) - np.array(net_worths) ) )
    
    ages = np.array(ages).tolist()
    net_worths = np.array(net_worths).tolist()

    for i in range( int( 0.1* len(residual_error) ) ):
        max_value = max(residual_error)
        idx = residual_error.index( max_value )
        del residual_error[idx]
        del ages[idx]
        del net_worths[idx]

    for i in range (len(ages)):
        cleaned_data.insert(i, (ages[i], net_worths[i], residual_error[i]) )

    
    return cleaned_data


#print 
#print outlierCleaner(predictions, ages, net_worths)
