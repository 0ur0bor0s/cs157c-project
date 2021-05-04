import pymongo
import json
import re
import geocoder
import pdb
from pymongo import ASCENDING, DESCENDING

def getBusinessWithWifi(db):
    # Create index first to search faster
    db.business.create_index([("state", ASCENDING), ("city", ASCENDING)])

    collection = db['business']
    
    while(True):
        print("Enter a city you want to search in")
        city = input()
        print("Enter the state you are in.Example: CA")
        state = input()
        print("Enter the exact postal-code")
        pincode = input()
        businesses = list()
        
        businesses = list(collection.find({"$and":[{"attributes.WiFi":{"$regex": "u'free'"}},{"city": city},{"state": state},{"postal_code": pincode}]},{"name":1}))
        names = []
        if(len(businesses) != 0):
            print("Businesses  with Wi-Fi:")
            for business in businesses:
                names += [business["name"]]
            for name in names:
                print(name)
                
        else:
            print("No result found.Please try again")
        print("Do you want to continue to search (y/n)")
        choice = input()
        while(True):
            if(choice.lower() == 'n' or choice.lower() == 'y'):
                break
            if(choice.lower() != 'y' and choice.lower != 'n'):
                print("please enter either y or n")
                print("Do you want to continue search (y/n)")
                choice = input()
        
        if(choice.lower() == 'n'):
            break

        
    # Once you're done, drop the user-defined indexes in case application wants to do writes
    db.business.drop_indexes()
            



                