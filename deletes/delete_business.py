

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
