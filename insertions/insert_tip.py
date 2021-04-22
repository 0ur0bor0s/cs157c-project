import datetime

def insert_tip(db):
    print("== Leave a tip ==")
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
        result = db.businesses.find_one({ "name": name, 
                                        "address": address, 
                                        "city": city, "state": state })

        print(result)
        if result is None:
            print("No results found. Please try again. \n")
            continue
        else:
            found_busi = True

    text_tip = input("What is your tip for this place? ")

    if name.lower() == "exit":
        return

    insertion = { "user_id" : "1111111-1111111111-111", 
                  "business_id" : result['business_id'], 
                  "text" : text_tip, 
                  "date" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                  "compliment_count" : 0 }
    
    result = db.tips.insert_one(insertion)

    if result.inserted_id:
        print("Tip successfully inserted")
    else:
        print("Tip insert unsuccessful")
        
        