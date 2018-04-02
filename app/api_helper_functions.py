# API helper functions
# libraries/modules
import json
import requests
import random #python library
import urllib #handles characters that are not alphabetical/encoding issues
import math

#API Keys
GOOGLE_MAPS_KEY = 'AIzaSyC0UFVze8X0mIJ9-o0TYVKE_eZBqYR3-Ws' #constants should be capitalized
FOURSQUARE_ID = 'KO2FJZFUOY4SF0JEBVXA4DYVHY4QF4IJEC1IHB2XORULPSVE'
FOURSQUARE_SECRET = 'IGZJ0YRZVTMSSZ0C2T0Z4YRUN2U0AGGZTRP5JAGFQU5TMIIF'

# FOURSQUARE
def get_top_venues(location, section, num_locations = 50):
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
        client_id=FOURSQUARE_ID,
        client_secret=FOURSQUARE_SECRET,
        v='20170001',
        near=location,
        section=section,
        limit=num_locations,
        offset=random.randint(1, 50) # pages through results (which are random)
        )

    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    top_venues_list = [] #this is a list, not a dictionary
    if data['meta']['code'] == 200: #only look into data if the foursquare API returns success
        for each_location in data['response']['groups'][0]['items']: #loops through each iteration
            venue_name = each_location['venue']['name'] + ', ' + location #adds city to the venue
            top_venues_list.append(venue_name) # Adds venue (element) to existing list of venues
    return top_venues_list

# GOOGLE MAPS
def get_route(start_address, end_address, venues, travel_mode, return_to_start):
    """
    INPUT:
    - origin: start address (string)
    - destination: end address (string)
    - venues: places to visit (list)
    - travel mode: mode of traveling (string)
    - return to start: boolean
    OUTPUT:
    - list of dictionaries (each dictionary contains the
    - destination and corresponding trip times)
    - Note: list is ordered based on optimized route
    """
    url = 'https://maps.googleapis.com/maps/api/directions/json'
    waypoints = 'optimize:true'
    for venue in venues:
        waypoints = waypoints + '|{0}'.format(venue) # pipe | separates the venues in the list
    if return_to_start:
        end_address = start_address
    params = dict(
        origin=start_address,
        destination=end_address,
        waypoints=waypoints,
        mode=travel_mode,
        key=GOOGLE_MAPS_KEY
        )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    route = [] # an empty list
    if data['status'] == 'OK': # if google maps API verifies address
        waypoint_order = data['routes'][0]['waypoint_order'] # orders which waypoint/venue is most efficient in regard to map
        for leg_number, each_leg in enumerate(data['routes'][0]['legs']):
            if leg_number < len(venues):
                route.append({'destination_name': venues[waypoint_order[leg_number]],
                              'trip_duration_value': each_leg['duration']['value'],
                              'trip_duration_text': each_leg['duration']['text']})
            elif return_to_start:
                route.append({'destination_name': end_address,
                              'trip_duration_value': each_leg['duration']['value'],
                              'trip_duration_text': each_leg['duration']['text']})
    return route

def format_gmap_url(origin, destination, travel_mode):
    gmap_embed_url = "https://www.google.com/maps/embed/v1/directions?key={0}&origin={1}&destination={2}".format(GOOGLE_MAPS_KEY,
        urllib.parse.quote(origin.encode('utf-8')), urllib.parse.quote(destination.encode('utf-8')))
    if travel_mode:
        gmap_embed_url += "&mode={}".format(travel_mode)
    return gmap_embed_url

def create_trip_legs(origin, venues, travel_mode):
    embed_map_urls = [format_gmap_url(origin, venues[0], travel_mode)]
    for index in range(0, len(venues)-1):
        embed_map_urls.append(format_gmap_url(venues[index], venues[index+1], travel_mode))
    return embed_map_urls

def optimize_route(origin, destination, venues, travel_mode, trip_duration, avg_time_spent_per_venue, return_to_start):

   initial_attempt = math.floor(trip_duration)
   venues_selected = random.sample(venues, initial_attempt) #grab random venues out of the 50
   venues = [x for x in venues if x not in venues_selected] #removes from list of 50
   trip_time_diff = 0 #create a time difference variable to keep track of how close the route is compared to user input
   last_trip_time_diff = 1000000 #create another time difference variable to keep track of the last attempt

   while abs(trip_time_diff) <= last_trip_time_diff:
       optimized_route = get_route(origin, destination, venues_selected, travel_mode, return_to_start)
       trip_time_diff = (trip_duration*60) - (sum(leg['trip_duration_value'] for leg in optimized_route)/60 + len(venues_selected) * avg_time_spent_per_venue)
       if abs(trip_time_diff) <= last_trip_time_diff:
           last_trip_time_diff = abs(trip_time_diff)
           previous_route = optimized_route #replace old route with new optimal route
           if trip_time_diff > 0:
               # add one venue from the route (at random)
               venues_selected += random.sample(venues, 1)
               venues = [x for x in venues if x not in venues_selected]
           else:
               # remove one venue from the route
               venues_selected.pop()
   return previous_route

def build_trip_plan(route, avg_time_spent_per_venue, destination, return_to_start):
    trip_plan = 'Hi traveler! ' #default greeting
    if return_to_start:
        trip_duration = math.floor(sum(leg['trip_duration_value'] for leg in route) / 60) + (len(route)-1) * avg_time_spent_per_venue
    else:
        trip_duration = math.floor(sum(leg['trip_duration_value'] for leg in route) / 60) + len(route) * avg_time_spent_per_venue
    trip_duration_hours = int(math.floor(trip_duration / 60))
    trip_duration_minutes = int(trip_duration % 60)
    if trip_duration_minutes == 0:
        trip_plan += 'Your trip will take roughly {0} hours. '.format(trip_duration_hours)
    else:
        trip_plan += 'Your trip will take roughly {0} hours and {1} minutes. '.format(trip_duration_hours, trip_duration_minutes)
    trip_plan += 'Please allocate 30 minutes for each stop on your trip. Enjoy!'

    for leg_number, leg in enumerate(route):
        trip_plan += '\nStep {0}: Travel {1} to {2}'.format(leg_number + 1,
            leg['trip_duration_text'], leg['destination_name'].replace(', ' + destination, ''))
    return trip_plan.split('\n')
