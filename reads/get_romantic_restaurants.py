def getRomanticAmbience(db):
    collection = db['business']
    while(True):
        print("Enter a city name:")
        name = input()
        print("Enter a state. Example: CA")
        state = input()
        print("Enter a postal code:")
        postalCode = input()
        #filter = {"city" : name},{"state" : state},{"postal_code":postalCode}
        field = "attributes.Ambience"
        resultDocs = list(collection.find({"$and":[{field:{"$regex": "'romantic': True"}},{"city" : name},{"state" : state},{"postal_code":postalCode},{"stars" : {"$gte":3.0}},{"categories" : {"$regex": "Restaurants"}}]})) #works , do not touch
        names = []
    
        if(len(resultDocs) != 0):
            for num in range(0,len(resultDocs)):
        
                print("Name:"+resultDocs[num]["name"])
                print("Address:"+resultDocs[num]["address"])
           
    
            
        else:
            print("No data found, please try again.")
        
        print("do you want to try again? (y/n)")
        choice = input()
        
        while(True):
            if(choice.lower() == 'n' or choice.lower() == 'y'):
                break
        
            if(choice.lower() != 'n' and choice.lower() != 'y'):
                print("please enter either y or n:")
                choice = input()
        if(choice.lower() == 'n'):
            break
            