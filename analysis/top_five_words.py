import nltk

def top_five_words(db):
    print('== Top five words ==')

    while True:
        business_name = input('Enter the exact name of the business: ')
        
        # find business that match
        business_result = db.business.find({'name': business_name})

        if business_name.count() != 0:
            print("Businesses found")
            break
        else:
            print("No business found")
                       


    return