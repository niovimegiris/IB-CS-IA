from flask import render_template
from app import app
from app.input_form import TripForm
from app.api_helper_functions import * # importing files

@app.route('/', methods=['GET', 'POST']) #http methods: protocol that allows for retrieving data and post referring to how clients can input data
def index(): # main page
    form = TripForm() # instantiates a trip form for the user
    venues = []
    trip_legs = []
    trip_plan = [] # empty lists that will be added to when user inputs data
    if form.validate_on_submit(): # checks if user inputs are valid before retrieving data from APIs
        venues = get_top_venues(location=form.destination.data,
                                section=form.interest.data) # 2 parameters
        if venues: # checks if venues exists
            optimized_route = optimize_route(origin=form.origin.data,
                                        destination=form.destination.data,
                                        venues=venues,
                                        travel_mode=form.travel_mode.data,
                                        trip_duration=form.trip_duration.data,
                                        avg_time_spent_per_venue=30,
                                        return_to_start=form.return_to_start.data)
            if optimized_route:
                trip_legs = create_trip_legs(origin=form.origin.data,
                                             venues=[leg['destination_name'] for
                                                     leg in optimized_route],
                                             travel_mode=form.travel_mode.data)
                trip_plan = build_trip_plan(route=optimized_route,
                                            avg_time_spent_per_venue=30,
                                            destination=form.destination.data,
                                            return_to_start=form.return_to_start.data)

        if not venues: # if venues does not exists
            trip_plan.append('No venues found. Try another destination.')
        if venues and not optimized_route: # when venues exists but Google can't find an optimal route
            trip_plan.append('Venues found, no route found. Try again.')
    return render_template('index.html',
                           form=form,
                           venues=venues,
                           trip_legs=trip_legs,
                           trip_plan=trip_plan)
