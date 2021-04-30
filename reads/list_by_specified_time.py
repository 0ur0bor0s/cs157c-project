from datetime import datetime, timedelta
import pymongo

def parse_time(s):
    return datetime.strptime(s, '%H:%M')

def check_in_range(start, end, input_time):
    start_time = parse_time(start)
    end_time = parse_time(end)
    checked_time = parse_time(input_time)
    if checked_time < end_time < start_time:
        checked_time += timedelta(days=1)

    if end_time < start_time:
        end_time += timedelta(days=1)

    return (start_time <= checked_time < end_time)

def list_by_specified_time(db):
    print("== List Businesses / Restaurants Within Area (Zipcode) By Time =====")
    found_busi = False
    city, state, zipcode = "", "", ""
    result = None

    while not found_busi:
        city = input("Enter exact city (if you want to leave, type 'exit'): ")
        if city.lower() == "exit":
            break

        state = input("Enter exact state (ex: TX): ")
        zipcode = input("Enter exact zipcode: ")

        # query database to find business
        result = list( db.business.find({ "city": city, 
                                        "state": state,
                                        "postal_code": zipcode } ))
        

        if result is None:
            print("No businesses found. Please try again. \n")
            continue
        else:
            found_busi = True
    
    if city.lower() == "exit":
        return

    specified_day = input("Specify day (ex: Monday): ")
    specified_time = input("Specify time (ex: 21:17): ")

    i = 0
    print("\n ======= ")
    for rest in result:
        if rest["hours"] is not None:
            range_times = rest["hours"][specified_day]
            range_hours = range_times.split("-")
            if not check_in_range(range_hours[0], range_hours[1], specified_time):
                continue
            else:
                i = i + 1
                print(" ({}) Name: {}".format(i, rest["name"] ))
                print("Address: {}".format(rest["address"] ))
                print("City: {}".format(rest["city"] ))
                print("State: {}".format(rest["state"] ))
                print("Zipcode: {}".format(rest["postal_code"] ))
                print("Stars: {}".format(rest["stars"] ))
                print("Categories: {}".format(rest["categories"] ))
                print("{} Times: {}".format(specified_day, rest["hours"][specified_day]))
                print("------------------------------\n")
    