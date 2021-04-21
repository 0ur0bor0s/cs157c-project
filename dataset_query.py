from pymongo import MongoClient

"""
To add a new function do the following:
    1) create a new function
    2) add function name to the operations map in main
    3) add function description with associated number to program output
"""

def insert_business(db):
    print("insert business")


def insert_review(db):
    print("insert review")


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
        print("    (q): Quit app")
        user_input = input("Enter the number of the operation you wish to perform: ")
        
        if user_input == "q" or user_input == "Q":
            break

        user_input = int(user_input)

        if user_input > len(operations) - 1 or user_input < 0:
            print("Invalid number")
            continue

        operations[user_input](db)
    

main()