def updateBusinessHours(db):
    print("Enter the name of restaurant , for which you want to update timings")
    name = input()
    hoursJSON = {}
    output = []
    collection = db['business']
    daysChoice = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday',6: 'Saturday', 7:'Sunday'}
    updatedTimings = {}
    output = list(collection.find({"name" : name},{"hours" : 1}))
    if(len(output) != 0):
        hoursJSON = output[0]['hours']
        #hoursJSON = json.loads(jsonString)
        print("timings for "+name+":") 
        for key, value in hoursJSON.items():
            print(key)
            #print("\n")
            print(value)
        
        while(True):
            print("Please enter the number shown before the day of the week shown below:")
            for key, value in daysChoice.items():
                print(str(key)+":"+value)
                
            dayNum = input()
            dayNum = int(dayNum)
            if(dayNum >= 1 and dayNum <=7):
                day = daysChoice.get(dayNum)
                hourString = "hours"
                param = hourString+"."+day
                print("Enter the new timings for the chosen day:")
                timings = input()
                filter = {'name' : name}
                query = {param : timings}
                collection.update_one(filter,{"$set" : query})
                output = list(collection.find({"name" : name},{"hours" : 1}))
                hoursJSON = output[0]['hours']
                print("The updated timings:")
                for key, value in hoursJSON.items():
                    print(key)
                    #print("\n")
                    print(value)
                
                print('Do you want to update any more timings? (y/n)')
                choice = input()
                while(True):
                    if(choice.lower() != 'y' and choice.lower() != 'n'):
                        print("Please enter either y or n")
                        choice = input()
                    else:
                        break
                if(choice.lower() == 'n'):
                    break
            else:
                print("Please enter the day correctly.")
        
    else:
        print("Sorry, could not find such a restaurant")
