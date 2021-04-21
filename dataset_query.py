from pymongo import MongoClient
import datetime

"""
To add a new function do the following:
    1) create a new function
    2) add function name to the operations map in main
    3) add function description with associated number to program output
"""

def insert_business(db):
    print("== Insert business ==")

    while True:
        name = input("Exact business name: ")
        address = input("Exact business address (ex: 123 Fake Ave): ")
        city = input("City: ")
        state = input ("State (ex: CA, OR, etc.): ")
        postal_code = input("Postal code: ")
        lat = input("Latitude: ")
        lon = input("Longitude: ")

        print("Categories (enter q to cancel): ")
        categories = None
        while True:
            cat = input(" - ")

            if cat == "q" or cat == "Q":
                break
            
            if (categories == None):
                categories = cat
            else:
                cat_f = ", "
                cat_f += cat
                categories += cat_f 

        confirm = input("Are you sure you wish to insert {}? (y/n) ".format(name))

        # Confirm input
        if confirm != "y" and confirm != "Y":
            break

        # Enter query
        insertion = {
            "name": name,
            "address": address,
            "city": city,
            "state": state,
            "postal_code": postal_code,
            "latutude": lat,
            "longitude": lon,
            "stars": 0.0,
            "review_count": 0,
            "is_open": 1,
            "attributes": None,
            "categories": categories,
            "hours": None
        }
        result = db.business.insert_one(insertion)
        
        if result.inserted_id:
            print("{} successfully inserted".format(name))
            break

        print("{} insert unsuccessful".format(name))



def insert_review(db):
    print("== Leave a review ==")

    name = input("Enter exact name of business: ")
    
    # query database to find business
    result = db.business.find({"name": name})
    
    while result.count() == 0:
        name = input("No results found. Please enter again: ")
        result = db.business.find({"name": name})

    # print out all businesses which have the name
    ids = []
    print("\n ======= ")
    for idx, b in enumerate(result):
        print(" ({}) {}".format(idx, b["name"]))
        print("     {}".format(b["address"]))
        print("     {}, {}".format(b["city"], b["state"]))
        print(" ======= ")
        ids.append(b["business_id"]) 
    print("\n{} business(es) found\n".format(result.count()))

    # Get business user wishes to write a review for
    review_num = input("Select the number of one of business you wish to review: ")

    while int(review_num) > result.count()-1 or int(review_num) < 0:
        review_num = input("Invalid entry: ")

    # business id to be written into database insertikon
    business_id = ids[int(review_num)]

    # Enter review
    print("\n== Review ==")

    # Stars
    stars = input(" - Number of stars (0-5): ")
    
    while int(stars) not in range(5):
        stars = input("Invalid number of stars: ")

    # Qualities
    qualities = {
        "Useful": 0,
        "Funny": 0,
        "Cool": 0
    }

    print("== Answer y or n to the following questions ==")
    for q_key in qualities:
        inp = input(" - {}? ".format(q_key))

        while inp != "y" and inp != "n" and inp != "Y" and inp != "N":
            inp = input("   Invalid input: ")

        if inp == "y":
            qualities[q_key] = 1
        else:
            qualities[q_key] = 0

    print("== Write your review ==")
    review = input("")

    insertion = {
        "business_id": business_id,
        "stars": int(stars),
        "useful": qualities["Useful"],
        "funny": qualities["Funny"],
        "cool": qualities["Cool"],
        "text": review,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    result = db.review.insert_one(insertion)

    if result.inserted_id:
        print("Review successfully inserted")
    else:
        print("Review insert unsuccessful")


def delete_business(db):
    print("== Delete business ==")
    
    while True:
        name = input("Exact business name: ")
        address = input("Exact business address (ex: 123 Fake Ave): ")
        city = input("City: ")
        state = input ("State (ex: CA, OR, etc.): ")
        confirm = input("Are you sure you wish to delete {}? (y/n) ".format(name))

        # Confirm input
        if confirm != "y" and confirm != "Y":
            break

        # Enter query
        result = db.business.delete_one({"name": name, "address": address, "city": city, "state": state})
        
        if result.deleted_count == 1:
            print("{} successfully deleted".format(name))
            break

        print("{} not found in database".format(name))



def main():
    # Make database connection
    client = MongoClient('localhost', 27017)
    db = client.yelp_dataset
    print("Database connection established")

    # operations map
    operations = {
        0 : insert_business,
        1 : insert_review,
        2 : delete_business
    } 

    while True:
        print("\nCurrently supported operations:")
        print("    (0): Insert business")
        print("    (1): Insert review")
        print("    (2): Delete business")
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