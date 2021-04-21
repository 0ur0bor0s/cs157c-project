import datetime

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

