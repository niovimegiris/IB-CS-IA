# API helper functions
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
    print ("Searching the web for some things to do in {}!").format(location)
    resp = requests.get(url=irl, params=params)
    data = json.loads(resp.text)
    return data

test = getTopVenues('Soho, NY')
    
    
