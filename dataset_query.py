from pymongo import MongoClient

"""
To add a new function do the following:
    1) create a new function
    2) add function name to the operations map in main
    3) add function description with associated number to program output
"""

def insert_business():
    print("insert business")


def insert_review():
    print("insert review")


def delete_business():
    print("delete business")


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

        operations[user_input]()
    

main()