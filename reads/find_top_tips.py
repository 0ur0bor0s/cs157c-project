import datetime
import pymongo


def find_top3_tips(db):
    print("== List Top 3 Tips of Restaurant ==")
    found_busi = False
    name, address, city, state, text_tip = "", "", "", "", ""
    result = None

    while not found_busi:
        name = input("Enter exact name of business (if you want to leave, type 'exit'): ")
        if name.lower() == "exit":
            break
        
        address = input("Enter exact street address: ")
        city = input("Enter exact city: ")
        state = input("Enter exact state (ex: TX): ")

        # query database to find business
        result = list(db.business.find({ "name": name, 
                                    "address": address, 
                                    "city": city, "state": state }))

        if result is None:
            print("No results found. Please try again. \n")
            continue
        else:
            found_busi = True
    
    if name.lower() == "exit":
        return
    
    listed_busi = result[0]

    list_tips = list( db.tip.find({ "business_id": listed_busi["business_id"]}).sort("compliment_count", pymongo.DESCENDING) )[0:3]

    i = 0
    print("\n ======= ")
    for tip in list_tips:
        i = i + 1
        print(" ({}) {} - Compliment Count: {}".format(i, tip["text"], tip["compliment_count"]))
    print("\n{} tips found\n".format(i))
        