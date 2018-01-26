# User input
#def gatherInputs():


#class Trip():
def checkIntInputs(input_question, limit):
    while True:
        try:
            input_var = int(input(input_question))
            if input_var < limit:
                break
            else:
                print("Sorry the limit is: {0}").format(limit)
                continue # do it again
        except ValueError:
            print("Sorry I didn't understand that") # user did not enter an integer
            continue # return to start of loop
        else:
            break # success

# User budget
budget = checkIntInputs("What is your budget? ", 100000)
##while True:
##    try:
##        budget = int(input("What is your budget? ")) # asking the user
##    except ValueError:
##        print("Sorry I didn't understand that") # user did not enter an integer
##        continue # return to start of loop
##    else:
##        break # success
print()

# Day Traveling
days_in_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] # list to be compared to
while True:    
    day_of_week = input("What day of the week are you traveling? " ) 
    if day_of_week.lower() in days_in_week: # comparing user input to elements in list
        break
    else:
        print("Sorry I didn't get that") # user did not enter valid response
print()

# Time traveling
while True:
    when = input("Would you like to go now or later? ")  
    if not when.isalpha():
        print("Sorry I didn't get that")
    elif when.lower() == 'now':
        break
    elif when.lower() == 'later':
        try:
            start_time = input("When would you like to go? (e.g. 1:35 PM) ")
            from datetime import *
            start_time = datetime.strptime(start_time, '%I:%M %p')
            #print(start_time)
            #break
        except ValueError:
            print("Sorry I didn't get that")
            continue
        break
    else:
        print("Sorry I didn't get that")
print()

# Duration
duration = checkIntInputs("How many hours do you have free? (e.g. 5) ", 24)
print()

# Start location
start_location = input("Where are you beginning this trip? (e.g. 14435 Wall Street) ")
start_location = start_location.lower()
#print(start_location)
print()

# Destination neighborhood
dest_neighborhood = input("Which neighborhood in NYC would you like to visit? (ex. Upper West Side, SoHo, etc.) ")
dest_neighborhood = dest_neighborhood.lower()

# End location of user
while True:
    end_location = input("You began at {0}, would you like to return here? ".format(start_location))
    end_location = end_location.lower()
    if end_location == 'yes':
        end_location = start_location
        break
    elif end_location == 'no':
        break
    else:
        print("Sorry I didn't get that")
        

# User interests
print()
def getVenueInterest():
    sections = {'food':'food', 'drinks':'drinks', 'coffee':'coffee', 'shops':'shops', 'arts':'arts', 'outdoors':'outdoors', 'sights':'sights', 'trending':'trending', 'random':'topPicks'} #dictionary
    print (*sections.keys(), sep='\n') # prints list
    while True:    
        interest = input("Of the choices above, enter one that interests you for this trip: ")
        if interest.lower() in sections.keys():
            interest = section[interest.lower()]
            break
        else:
            print("Sorry I didn't get that")
    return interest




