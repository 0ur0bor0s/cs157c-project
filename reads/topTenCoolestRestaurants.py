def topTenCoolestRestaurants(db):
    
    collection = db['review']
    businessCollection = db['business']
    while(True):
        coolest = collection.find({},{"business_id"}).sort("cool" , -1)
        print("Enter a city name:")
        city = input()
        print("Enter a state name")
        state = input()
        print("Enter a pin code")
        pincode = input()
        resultDocs = []
        resultDocs = list(businessCollection.find({"$and":[{"city":city},{"state":state},{"postal_code":pincode},{"categories" : {"$regex": "Restaurants"}}]},{"business_id":1}))
        if(len(resultDocs) != 0):
            businessIDs = []
            for resultDoc in resultDocs:
                businessIDs += [resultDoc["business_id"]]
            #aggResults = {}
            aggResults = list(collection.aggregate(
            [{"$match" : {"business_id":{"$in":businessIDs}}},
            {
            "$group" : 
                {
                    "_id" : "$business_id", 
                    "coolness_score" : {"$sum" : "$cool"}
                }
            },
            { "$sort": { "coolness_score": -1 } },
            {"$limit" : 10}
		 
            ]))
    
            
            finalOutput = {}
            for k in range(0,len(aggResults)):
                business_id = aggResults[k]["_id"]
                names = list(businessCollection.find({"business_id" : business_id},{"name" : 1}))
                for one_name in range(0,1):
                    resName = names[one_name]["name"]
                    coolPoints = aggResults[k]["coolness_score"]
                    finalOutput[resName] = coolPoints
            print("Top 10 coolest restaurants in the city:")
            for k,v in finalOutput.items():
                print("Name:"+k)
                print("Cool Score:"+str(v))
        else:
            print("Data not found, please try again.")
        print("Do you want to try again? (y/n)")
        choice = input()
        
        if(choice.lower() != 'y' and choice.lower() != 'n'):
            while(True):
                print("Please enter either y or n")
                choice = input()
                if(choice.lower() == 'y' or choice.lower() == 'n'):
                    break
                    
        if(choice.lower() == 'n' ):
            break        