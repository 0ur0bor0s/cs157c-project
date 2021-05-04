# RALPH
import datetime
import pymongo

# Used Case #14: List of restaurants of a certain category (i.e. Mexican, Japanese, Indian, Hawaiin, etc) and offers take-out and has at least 3 stars (limit 5 restaurants).

def top_10_cities_category(db):
    print("== Top 10 Cities For Specific Category =====")
    found_busi = False
    category = ""
    result = None

    while not found_busi:
        category = input("Enter exact category (if you want to leave, type 'exit'): ")
        if category.lower() == "exit":
            break

        # query database to find business
        result = list( db.business.aggregate([ 
            { '$match': { "categories": { '$regex': category } } }, 
            { '$group': { '_id': '$city', 'state': { '$first': '$state' }, 
            'avg': { '$avg': '$stars' }, 'total': { '$sum' : 1 }  } }, 
            { '$sort': { 'total': -1, 'avg': -1 } }, { '$limit': 10 } ] ) )
        
        if result is None:
            print("No results found. Please try again. \n")
            continue
        else:
            found_busi = True
    
    print(result)
    if category.lower() == "exit":
        return
    
    i = 0
    print("\n ======= ")
    for city in result:
        i = i + 1
        print(" ({}) City: {}".format(i, city["_id"] ))
        print("State: {}".format(city["state"] ))
        print("Average Star Rating: {}".format(city["avg"] ))
        print("Total Businesses: {}".format(city["total"] ))
        print("------------------------------\n")
