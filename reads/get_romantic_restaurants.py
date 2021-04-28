def getRomanticAmbience(db):
    collection = db['business']
    print("Enter a city name:")
    name = input()
    filter = {"city" : name}
    field = "attributes.Ambience"
    resultDocs = list(collection.find({"$and":[{field:{"$regex": "'romantic': True"}},filter]},{"name":1})) #works , do not touch
    names = []
    
    for resultDoc in resultDocs:
        
        names += [resultDoc["name"]]
           
    
    for item in names:
        print(item)
