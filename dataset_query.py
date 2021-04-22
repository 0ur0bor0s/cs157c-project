#!/usr/bin/env python3
from pymongo import MongoClient

from deletes.delete_business import delete_business
from insertions.insert_business import insert_business
from insertions.insert_review import insert_review
from insertions.insert_tip import insert_tip

def main():
    # Make database connection
    client = MongoClient('localhost', 27017)
    db = client.testdb

    if db:
        print("Database connection established")
    else:
        print("Databse connection not established")

    # operations map
    operations = {
        0 : insert_business,
        1 : insert_review,
        2:  insert_tip,
        3 : delete_business
    } 

    while True:
        print("\nCurrently supported operations:")
        print("    (0): Insert business")
        print("    (1): Insert review")
        print("    (2): Insert Tip")
        print("    (3): Delete business")
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