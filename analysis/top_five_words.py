from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import operator

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



def top_five_words(db):
    print("== Top five words ==")

    b_again = True
    while b_again:
        
        # get business id of business
        (business_id, business_name) = find_business(db)

        # Query for reviewd for this business
        review_result = db.review.find({"business_id": business_id})

        # Print the number of reviews
        print("{} reviews found.".format(review_result.count()))

        if (review_result.count() < 5):
            print("Not enough data to properly analyze.")
            return

        # stop words to filter out
        stop_words = set(stopwords.words("english"))

        # Iterate through 50 reviews and tokenize the numbers
        word_dict = {}
        tokenizer = RegexpTokenizer(r'\w+')
        for idx, r in enumerate(review_result):

            # tokenize text
            review_text = r["text"]
            r_tokens = tokenizer.tokenize(review_text)

            # make all text lowercase
            for i in range(len(r_tokens)):
                r_tokens[i] = r_tokens[i].lower()

            # filter out stop words
            #filtered_tokens = [w for w in word_dict if not w in stop_words]
            filtered_tokens = []
            for w in r_tokens:
                if w not in stop_words:
                    filtered_tokens.append(w)

            for token in filtered_tokens:
                # Add to dictionary if word does not exist
                if token not in word_dict:
                    word_dict[token] = 0
                # increment word count
                word_dict[token] += 1

            # only check 10 reviews
            if idx > 10:
                break

        
        # Get top 5 most used words for review
        print("\nTop Five Most used words for {}\n".format(business_name))
        for i in range(5):
            top_tuple = max(word_dict.items(), key=operator.itemgetter(1))
            
            print("Number {}:".format(i+1))
            print("---------")
            print("Word: {}".format(top_tuple[0]))
            print("Frequency: {}\n".format(top_tuple[1]))

            del word_dict[top_tuple[0]]
            

        # Run again?
        again_str = input("Run again? (y/n) ")
        if (again_str == "n" or again_str == "N"):
            b_again = False

    


    


    

    
    
    
    

    
