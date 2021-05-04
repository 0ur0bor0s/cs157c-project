# RALPH
import datetime
import pymongo
from pymongo import ASCENDING, DESCENDING

# Used Case #14: List of restaurants of a certain category (i.e. Mexican, Japanese, Indian, Hawaiin, etc) and offers take-out and has at least 3 stars (limit 5 restaurants).

def list_category_rest_takeout(db):
    # Create index first to search faster
    db.business.create_index([("state", ASCENDING), ("city", ASCENDING)])

    print("== List Restaurants That Do Takeout and of Certain Category Within Area (Zipcode) =====")
    found_busi = False
    city, state, zipcode = "", "", ""
    result = None

    while not found_busi:
        city = input("Enter exact city (if you want to leave, type 'exit'): ")
        if city.lower() == "exit":
            break

        state = input("Enter exact state (ex: TX): ")
        zipcode = input("Enter exact zipcode: ")
        category = input("What category you want? ")

        # query database to find business
        result = list( db.business.find({ "city": city, 
                                        "state": state,
                                        "postal_code": zipcode,
                                        "categories": { '$regex': category },
                                        "stars": {'$gte': 3 },
                                        "attributes.RestaurantsTakeOut": "True" } ).limit(5) )
        
        if result is None:
            print("No results found. Please try again. \n")
            continue
        else:
            found_busi = True
    
    if city.lower() == "exit":
        return
    
    i = 0
    print("\n ======= ")
    for rest in result:
        i = i + 1
        print(" ({}) Name: {}".format(i, rest["name"] ))
        print("Address: {}".format(rest["address"] ))
        print("City: {}".format(rest["city"] ))
        print("State: {}".format(rest["state"] ))
        print("Zipcode: {}".format(rest["postal_code"] ))
        print("Stars: {}".format(rest["stars"] ))
        print("Categories: {}".format(rest["categories"] ))
        print("TakeOut?: {}".format(rest["attributes"]["RestaurantsTakeOut"] ))
        print("------------------------------\n")

    print("\n{} Restaurants found\n".format(i))

    # Once you're done, drop the user-defined indexes in case application wants to do writes
    db.business.drop_indexes()
    