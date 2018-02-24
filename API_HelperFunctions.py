# API helper functions
# libraries
import json
import requests

# FOURSQUARE
def getTopVenues(location, section = 'topPicks', num_locations = 10):
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
        client_id = 'KO2FJZFUOY4SF0JEBVXA4DYVHY4QF4IJEC1IHB2XORULPSVE',
        client_secret = 'IGZJ0YRZVTMSSZ0C2T0Z4YRUN2U0AGGZTRP5JAGFQU5TMIIF',
        v = '20170001',
        near = num_locations,
        section = section,
        limit = 10
        )
    #print ("Searching the web for some things to do in {}!").format(location)
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    return data

test = getTopVenues('Soho, NY')
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

def getRoute(start_address, end_address): #FIX GOOGLE MAPS APIIIII
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
        key='AIzaSyAWNzuFCqmmZQwRyg5vmOwnLDfv0Ma0o5s'
        )

    #print ("Searching Google Maps for best route to take from {0} to {1}").format(start_address, end_address)
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    return data

test = getRoute('Soho', 'Brooklyn')
print(test)
