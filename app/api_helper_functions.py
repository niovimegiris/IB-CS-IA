# API helper functions
# libraries
import json
import requests
import random #python library
import numpy # helps with statistics
import math

#API Keys
google_maps_key = 'AIzaSyAWNzuFCqmmZQwRyg5vmOwnLDfv0Ma0o5s'
foursquare_id = 'KO2FJZFUOY4SF0JEBVXA4DYVHY4QF4IJEC1IHB2XORULPSVE'
foursquare_secret = 'IGZJ0YRZVTMSSZ0C2T0Z4YRUN2U0AGGZTRP5JAGFQU5TMIIF'

# FOURSQUARE
def getTopVenues(client_id, client_secret, location, section = 'topPicks', num_locations = 50):
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
        offset = random.randint(1, 50) # pages through results (which are random)
        )
        #print ("Searching the web for some things to do in {}!").format(location)
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    #return data #returns all data, however we want to return a subset

       #Retrieve both the names of the top venues
    top_venues_list = [] #this is a list, not a dictionary
    for each_location in data['response']['groups'][0]['items']: #loops through each iteration
        venue_name = each_location['venue']['name']
        #venue_name = data['response']['groups'][0]['items'][each_location]['venue']['name'] # Subset of data
        top_venues_list.append(venue_name) # Adds venue (element) to existing list of venues
    return top_venues_list

#ISSUE
    # how do we randomize the names of venues for new trips?


def randomlySelectVenues(venues, num_select):
    return numpy.random.choice(venues, num_select, replace=False)

venues = getTopVenues(foursquare_id, foursquare_secret, 'Soho, NY')
venues = randomlySelectVenues(venues, 5) # will randomly select 5 venues

#Issue #2
    # how do we make sure the selected venues are without replacement (dont repeat)?
    #ANSWER: USE NUMPY LIBRARY
print(venues)



#test['meta'] everytime i request, gives unique id
# write a for loops that loops through test['response']['groups'][0]['items'][0]['venue']['name']
# changes second 0 add one each time to get all locations
# every time i loop, each name of each location will append it to a list
# return all names at end of function

#`all_names = []`
#all_names.append(name)`


# GOOGLE MAPS
# key: AIzaSyAWNzuFCqmmZQwRyg5vmOwnLDfv0Ma0o5s

def getRoute(api_key, start_address, end_address, venues): #FIX GOOGLE MAPS APIIIII
    """
    INPUT:
    - start_address : starting location
    - end_address : destination
    OUTPUT:
    - dictionary with direction
    """
    url = 'https://maps.googleapis.com/maps/api/directions/json'
    waypoints = 'optimize:true'
    for venue in venues:
        waypoints = waypoints + '|{0}'.format(venue) # pipe | separates the venues in the list
    # play around with test

    params = dict(
        origin=start_address,
        destination=end_address,
        waypoints=waypoints,
        key=api_key
        )

    #print ("Searching Google Maps for best route to take from {0} to {1}").format(start_address, end_address)
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    durations_list = [] # list to store durations of trips (strings)
    durations_list_values = [] # list to store durations of trips (as values/integers)
    for each_leg in data['routes'][0]['legs']:
        duration_length = each_leg['duration']['text']
        duration_length_value = each_leg['duration']['value']
        #print(each_leg['duration']['text']) #text refers to how long the trip will take
        durations_list.append(duration_length)
        durations_list_values.append(duration_length_value)
    return durations_list, durations_list_values

travel_times, travel_times_values = getRoute(google_maps_key, 'Soho', 'Brooklyn', venues)

print(travel_times, travel_times_values) #testing

while abs(trip_time_diff) <= last_trip_time_diff:
    optimized_route = get_route(origin, destination, venues_selected, travel_mode, return_to_start)
    trip_time_diff = (trip_duration*60) - (sum(leg['trip_duration_value'] for leg in optimized_route)/60 + len(venues_selected) * avg_time)
    if abs(trip_time_diff) <= last_trip_time_diff:
        last_trip_time_diff = abs(trip_time_diff)
        previous_route = optimized_route # replaces old route with new router
        if trip_time_diff > 0:
            # adds one venue from route (randomly)
            venues_selected.append(random.sample(venues, 1))
        else:
            # removes one venue from the router
            venues_selected.pop()
return previous_route

def buildTripPlan(venues, travel_times, travel_times_values, back_to_origin = True, avg_time_per_venue = 30):
    trip_plan = '' #default

    trip_duration = len(venues) * avg_time_per_venue + math.floor(sum(travel_times_values) / 60)
    trip_duration_hours = math.floor(trip_duration / 60)
    trip_duration_minutes = trip_duration % 60
    if trip_duration_minutes == 0:
        trip_plan = trip_plan + '\n Your trip will take {0} hours'.format(trip_duration_hours)
    else:
        trip_plan = trip_plan + '\n Your trip will take {0} hours and {1} minutes'.format(trip_duration_hours, trip_duration_minutes)

    for step_number, venue in enumerate(venues):
        trip_plan = trip_plan + '\n Step {0}: Travel {1} to {2}'.format(step_number + 1, travel_times[step_number], venue)
    if back_to_origin:
        trip_plan = trip_plan + '\n Step {0}: Go to origin'.format(len(venues) +1) #length of venues list
    return trip_plan

print(buildTripPlan(venues, travel_times, travel_times_values, back_to_origin = False))
