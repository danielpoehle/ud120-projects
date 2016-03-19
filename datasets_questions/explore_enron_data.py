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
    
"""

import pickle
import csv

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print(str(len(enron_data)))
print(str(len(enron_data["SKILLING JEFFREY K"])))

s = 0
salary = 0
mail = 0
payments = 0
pay_pois = 0

for name in enron_data:
    print name
    if enron_data[name]["poi"] == True:
        s += 1
    if enron_data[name]["salary"] != "NaN":
        salary += 1
    if enron_data[name]["email_address"] != "NaN":
        mail += 1
    if enron_data[name]["total_payments"] == "NaN":
        payments += 1
    if enron_data[name]["total_payments"] == "NaN" and enron_data[name]["poi"] == True:
        pay_pois += 1

print "Number of POIs:"
print(str(s))
print "Number of Persones with a given salary:"
print(str(salary))
print "Number of Persones with a known email address:"
print(str(mail))
print "Number of Persones without a given total payment:"
print(str(payments))
print "Number of POIs without a given total payment:"
print(str(pay_pois))

print("JEFFREY K SKILLING:")
print(enron_data["SKILLING JEFFREY K"])



print "POI-Names"
poi_names = []
with open('../final_project/poi_names.txt') as inputfile:
    for row in csv.reader(inputfile):
        poi_names.append(row)

print poi_names
print(str(len(poi_names)))

print "total value of the stock belonging to PRENTICE JAMES:"
print enron_data["PRENTICE JAMES"]["total_stock_value"]

print "email messages from Wesley Colwell to persons of interest:"
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "value of stock options exercised by Jeffrey Skilling:"
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

