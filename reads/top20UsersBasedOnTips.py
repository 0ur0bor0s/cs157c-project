def topUsersByCompliments(db):
    tipCollection = db['tip']
    topUsers = list(tipCollection.aggregate(
    [
	{
    "$group" : 
        {"_id" : "$user_id", 
         "compliments given" : {"$sum" : "$compliment_count"},
		 "tips given" :{"$sum" : 1}
         }},
	{"$sort" : {"tips given":-1}},
	{"$limit" : 20}
    ]))
    
    print("Top 20 users based on number of tips given:")
    for userNumber in range(0,len(topUsers)):
        
        print("User ID:"+topUsers[userNumber]["_id"])
        print("Tips given:"+str(topUsers[userNumber]["tips given"]))
        print("Compliments given:"+str(topUsers[userNumber]["compliments given"]))