
"""
    Helper function to find business
"""
def find_business(db):

    while True:
        business_name = input("Enter the exact name of the business: ")
        
        # find business that match
        business_result = db.business.find({"name": business_name})

        if business_result.count() != 0:
            print("Businesses found")
            break
    
        print("No business found")

    # Iterate through business to choose the correct one 
    ids = []  
    print("") 
    for idx, b in enumerate(business_result):
        print(" ======= ")   
        print(" ({}) {}".format(idx, b["name"]))
        print("     {}".format(b["address"]))
        print("     {}, {}".format(b["city"], b["state"]))
        print(" ======= ")
        ids.append(b["business_id"]) 
    print("\n{} business(es) found\n".format(business_result.count()))

    # Get business user wishes to write a review for
    bus_num = input("Select one of the following businesses by number: ")
    
    while int(bus_num) > business_result.count()-1 or int(bus_num) < 0:
        bus_num = input("Invalid entry: ")

    business_id = ids[int(bus_num)]

    return (business_id, business_name)
