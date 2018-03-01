# API helper functions
# libraries
import json
import requests

#API Keys
google_maps_key = 'AIzaSyAWNzuFCqmmZQwRyg5vmOwnLDfv0Ma0o5s'
foursquare_id = 'KO2FJZFUOY4SF0JEBVXA4DYVHY4QF4IJEC1IHB2XORULPSVE'
foursquare_secret = 'IGZJ0YRZVTMSSZ0C2T0Z4YRUN2U0AGGZTRP5JAGFQU5TMIIF'

# FOURSQUARE
def getTopVenues(client_id, client_secret, location, section = 'topPicks', num_locations = 50, offset = 20):
    """
    INPUT:
    - location: string containing location
    section: category of venues
    num_locations: number of locations to return to user
    OUTPUT:
    = dictionary with top locations
    """
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
        client_id = client_id,
        client_secret = client_secret,
        v = '20170001',
        near = location,
        section = section,
        limit = num_locations,
        offset = offset # pages through results (which are random)
        )
    #print ("Searching the web for some things to do in {}!").format(location)
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    #return data #returns all data, however we want to return a subset

    #Retrieve both the names of the top venues
    top_venues_list = [] #this is a list, not a dictionary
    for each_location in range(0, num_locations): #loops through each iteration
        venue_name = data['response']['groups'][0]['items'][each_location]['venue']['name'] # Subset of data
        top_venues_list.append(venue_name) # Adds venue (element) to existing list of venues
    return top_venues_list

#ISSUE
    # how do we randomize the names of venues for new trips?

test = getTopVenues(foursquare_id, foursquare_secret, 'Soho, NY')
print(test)





#test['meta'] everytime i request, gives unique id
# write a for loops that loops through test['response']['groups'][0]['items'][0]['venue']['name']
# changes second 0 add one each time to get all locations
# every time i loop, each name of each location will append it to a list
# return all names at end of function

#`all_names = []`
#all_names.append(name)`


# GOOGLE MAPS
# key: AIzaSyAWNzuFCqmmZQwRyg5vmOwnLDfv0Ma0o5s

def getRoute(API_Key, start_address, end_address): #FIX GOOGLE MAPS APIIIII
    """
    INPUT:
    - start_address : starting location
    - end_address : destination
    OUTPUT:
    - dictionary with direction
    """
    url = 'https://maps.googleapis.com/maps/api/directions/json'
    params = dict(
        origin= start_address,
        destination= end_address,
        key= API_Key
        )

    #print ("Searching Google Maps for best route to take from {0} to {1}").format(start_address, end_address)
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    return data

test = getRoute(google_maps_key, 'Soho', 'Brooklyn')

#print(test) #testing
