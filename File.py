##def checkIntType(input_variable):
##    if input_variable == int:
##        return input_variable
##    else:
##        return ("I didn't understand that")


# User input
#def gatherInputs():

while True:
    try:
        budget = int(input("What is your budget? "))
    except ValueError:
        print("Sorry I didn't understand that") # return to start of loop
        continue
    else:
        break # success
print()
# Day Traveling
days_in_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
while True:    
    day_of_week = input("What day of the week are you traveling? " )
    if day_of_week.lower() in days_in_week:
        break
    else:
        print("Sorry I didn't get that")
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
        except ValueError:
            print("Sorry I didn't get that")
            continue
        break
    else:
        print("Sorry I didn't get that")
print()

# Duration
while True:
    try:
        duration = int(input("How many hours do you have free? (e.g. 5)"))
    except ValueError: # what if user inputs "five"that techinically isnt wrong???????????????
        print("Sorry I didn't understand that") # return to start of loop
        continue
    else:
        break # success
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
sections = ['food', 'drinks', 'coffee', 'shops', 'arts', 'outdoors', 'sights', 'trending', 'topPicks']
print (*sections, sep='\n') # prints list
while True:    
    interest = input("Of the choices above, enter one that interests you for this trip: ")
    if interest.lower() in sections:
        break
    else:
        print("Sorry I didn't get that")




