#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

    NaN means "Not a Number" and it's used when the exact number is unknown
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

##HERE'S MY CODE 

#this is how to find the keys (people) inside 'enron' dictionary...
print "Number of peaple in the dataset is: %d \n" %( len(enron_data.keys()) )

print "Number of features per person in the dataset is: %d \n" %(len( enron_data["SKILLING JEFFREY K"].values() ))

#To find the people of interest:
people_in_charge = 0
for key in enron_data:
	if enron_data[key]["poi"] == 1:
		people_in_charge = people_in_charge + 1

print "People with (poi==1) is: %d \n" %(people_in_charge) 

print "All features about James Prentice: \n %s \n"  %(enron_data["PRENTICE JAMES"])

print "The total message from wesley colwell to poi is: %d \n" %(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"] )

print "The value of stock options exercised by Jeffrey Skilling is: %d \n" %(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"] )

#who gets the largest value of "total_payments" feature
print "Jeffrey Skilling: %d" %enron_data["SKILLING JEFFREY K"]["total_payments"]
print"Andrew Fastow: %d " %enron_data["FASTOW ANDREW S"]["total_payments"]
print "Kenneth Lay: %d" %enron_data["LAY KENNETH L"]["total_payments"]

#to find quantified features in the data set
sal = 0
mail = 0
pay = 0
it = 0
for k in enron_data.keys():
    it = it + 1
    if enron_data[k]["salary"] != "NaN":
        sal = sal + 1
    if enron_data[k]["email_address"] != "NaN":
        mail = mail + 1

print "Number of quantified salary is: %d" %sal
print "Number of known e-mail addresses is: %d" %mail


#my amazing solution
for k in enron_data.keys():
    if 'LAY KENNETH' in k:
        name = k


#OPTIONAL part
total = 0
pois = 0
pay = 0
poi_pay = 0
for k in enron_data.keys():
    total = total + 1
    if enron_data[k]["total_payments"] == "NaN":
        pay = pay + 1
    if enron_data[k]["poi"] == True:
        pois = pois + 1
        if enron_data[k]["total_payments"] == "NaN":
            poi_pay = poi_pay + 1

print "Number of people who have NaN in total_payments is: %d, which forms a percentage of %f \n" %(pay, pay*100/total)
print "Number of POI who have NaN in total_payments is: %d, which forms a percentage of %f \n" %(poi_pay, poi_pay*100/pois)

