import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from analysis.find_business import find_business

nltk.download('vader_lexicon')

def sentiment(db):
    print("== Review sentiment analysis ==")


    b_again = True
    while b_again:

        # Get business id and name
        (business_id, business_name) = find_business(db)

        # Query for reviewd for this business
        review_result = db.review.find({"business_id": business_id})

        # Print the number of reviews
        print("{} review(s) found.".format(review_result.count()))

        if (review_result.count() < 1):
            print("Not enough data to properly analyze.\n")
            # Run again?
            again_str = input("Run again? (y/n) ")
            if (again_str == "n" or again_str == "N"):
                b_again = False
            continue

        # Analyzer
        analyzer = SentimentIntensityAnalyzer()
        
        # Score dictionary
        final_score = {
            "neg": 0,
            "neu": 0,
            "pos": 0,
            "compound": 0
        }

        # Iterate through each review and analyze
        for idx, r in enumerate(review_result):
            # Analyze sentiment
            review_text = r["text"]
            vader_score = analyzer.polarity_scores(review_text)

            #print(vader_output)

            final_score["neg"] += vader_score["neg"]
            final_score["neu"] += vader_score["neu"]
            final_score["pos"] += vader_score["pos"]
            final_score["compound"] += vader_score["compound"]

            if idx+1 >= 10:
                break

        # Calculate the average
        final_score["neg"] = (final_score["neg"] / (idx+1)) * 100
        final_score["neu"] = (final_score["neu"] / (idx+1)) * 100
        final_score["pos"] = (final_score["pos"] / (idx+1)) * 100
        final_score["compound"] = (final_score["compound"] / (idx+1)) * 100

        face_str = ""
        analysis_str = ""
        if final_score["compound"] > 75:
            face_str = "'v'"
            analysis_str = "Good!"
        elif final_score["compound"] < 35:
            face_str = "-_-"
            analysis_str = "Bad"
        else:
            face_str = "'-'"
            analysis_str = "Neutral"

        # Print output
        print("\nFinal review sentiment score for {}".format(business_name))
        print("--------------------------------------------------------")
        print("{} review(s) analyzed.".format(idx+1))
        print("({}) Compound rating: {:.2f}%".format(face_str, final_score["compound"]))
        print(" - (-_-) Negative rating: {:.2f}%".format(final_score["neg"]))
        print(" - ('-') Neutral rating: {:.2f}%".format(final_score["neu"]))
        print(" - ('v') Positive rating: {:.2f}%".format(final_score["pos"]))
        print("Overall analysis: {}\n".format(analysis_str))


        # Run again?
        again_str = input("Run again? (y/n) ")
        if (again_str == "n" or again_str == "N"):
            b_again = False



