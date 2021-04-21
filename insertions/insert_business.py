

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
