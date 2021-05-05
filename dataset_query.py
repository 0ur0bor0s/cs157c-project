#!/usr/bin/env python3
from pymongo import MongoClient

from deletes.delete_business import delete_business
from deletes.delete_review import delete_review

from insertions.insert_business import insert_business
from insertions.insert_review import insert_review
from insertions.insert_tip import insert_tip

from reads.find_top_tips import find_top3_tips
from reads.list_by_specified_time import list_by_specified_time
from reads.list_category_rest_takeout import list_category_rest_takeout
from reads.get_romantic_restaurants import getRomanticAmbience
from reads.top_10_cities_category import top_10_cities_category
from reads.business_with_wifi_exact import getBusinessWithWifi
from reads.topTenCoolestRestaurants import topTenCoolestRestaurants

from updates.update_business_hours import updateBusinessHours

def main():
    # Make database connection
    client = MongoClient('localhost', 27017)
    db = client['yelp_dataset']

    if db:
        print("Database connection established")
    else:
        print("Database connection not established")

    # operations map
    operations = {
        0 : insert_business,
        1 : insert_review,
        2 : insert_tip,
        3 : delete_business,
        4:  delete_review,
        5 : find_top3_tips,
        6:  list_category_rest_takeout,
        7:  list_by_specified_time,
        8 : updateBusinessHours,
        9 : getRomanticAmbience,
        10: getBusinessWithWifi,
        11 : top_10_cities_category,
        12 : topTenCoolestRestaurants
    } 

    while True:
        print("\nCurrently supported operations:")
        print("    (0): Insert business")
        print("    (1): Insert review")
        print("    (2): Insert Tip")
        print("    (3): Delete business")
        print("    (4): Delete review")
        print("    (5): Find top tips for business")
        print("    (6): List take-out restaurants by certain category (at least 3 stars) ")
        print("    (7): List businesses / restaurants by specified time.")
        print("    (8): Update business hours")
        print("    (9): Find romantic restaurants in a city")
        print("    (10): Find Businesses with Wi-Fi in a city")
        print("    (11): Find Top 10 Cities for Specific Category")
        print("    (12): Find Top 10 coolest restaurants in a city")
        print("    (q): Quit app\n")
        user_input = input("Enter the number of the operation you wish to perform: ")
        
        if user_input == "q" or user_input == "Q":
            break

        user_input = int(user_input)

        if user_input > len(operations) - 1 or user_input < 0:
            print("Invalid number")
            continue

        operations[user_input](db)
    

main()
