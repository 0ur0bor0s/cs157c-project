

def delete_review(db):
    print("== Delete review ==")
    
    while True:
        name = input("Exact business name: ")
        address = input("Exact business address (ex: 123 Fake Ave): ")
        city = input("City: ")
        state = input ("State (ex: CA, OR, etc.): ")

        # Find business query
        found_busi = db.business.find_one({"name": name, "address": address, "city": city, "state": state})
        if not found_busi:
            print("{} not found in database".format(name))
            break

        user_id = input("What is your user id?: ")

        # Find list of reviews made by user
        list_reviews = list ( db.review.find({"business_id": found_busi["business_id"], "user_id": user_id}) )

        if len(list_reviews) < 1:
            print("Reviews Not Found in Database")
            break

        print("\n== Which Review to Delete? ==")
        for i in range(len(list_reviews)):
            print("({}) Review: {} - Stars: {}".format(i, list_reviews[i]["text"], list_reviews[i]["stars"] ) )
            print("---------------------------")
        print("\n ======================\n")
        
        option = input("Which review do you want to delete? (Type number or 'q' to quit): ")

        if option == 'q':
            break
        
        confirm = input("Are you sure you wish to delete {}? (y/n) ".format(name))

        # Confirm input
        if confirm != "y" and confirm != "Y":
            break
        
        # use deletion query
        document_sel = list_reviews[int(option)]
        result = db.review.delete_one(document_sel)

        if result.deleted_count == 1:
            print("{} successfully deleted".format(name))
            break
        else:
            print("Review not successfully deleted")
            break

        