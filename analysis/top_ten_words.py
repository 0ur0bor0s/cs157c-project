from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import operator

from analysis.find_business import find_business

def top_ten_words(db):
    print("== Top ten words ==")

    b_again = True
    while b_again:
        
        # Get business id and name
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

            # only check 300 reviews
            if idx+1 >= 300:
                break

        
        # Get top 5 most used words for review
        print("\nTop Ten Most used words for {}\n".format(business_name))
        for i in range(10):
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

    


    


    

    
    
    
    

    
