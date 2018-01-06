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
        
    

start_location = input("Start Location: ")
dest_neighborhood = input("Which neighborhood in NYC would you like to visit? (ex. Upper West Side, Soho, etc.) ")
end_location = bool(input("Would you like to return to your start location? "))


