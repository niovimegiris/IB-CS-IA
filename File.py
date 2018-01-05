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
    
while True:    
    day_to_explore = input("When are you traveling?" )
    if not day_to_explore.isalpha():
        print("Sorry I didn't get that")
        continue
    else:
        break


start_location = input("Start Location: ")
dest_neighborhood = input("Which neighborhood in NYC would you like to visit? (ex. Upper West Side, Soho, etc.) ")
end_location = bool(input("Would you like to return to your start location? "))


