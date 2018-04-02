from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class TripForm(FlaskForm): # creating a class with different traits
    origin = StringField('Where are you starting your journey? (e.g. Brooklyn, NYC/13432 Wall Street, NY)',
                         validators=[ DataRequired()])
    destination = StringField('Where would you like to go? (e.g. SoHo, NY)',
                              validators=[DataRequired()])
    interest = RadioField('What would you like to do?',
                          choices=[('arts', 'Art'),
                                   ('food', 'Food'),
                                   ('drinks', 'Drinks'),
                                   ('coffee', 'Coffee'),
                                   ('outdoors', 'Outdoors'),
                                   ('shops', 'Shops'),
                                   ('topPicks', 'Surprise me!')])
    trip_duration = IntegerField('Approximately how many hours do you want your trip to last? (e.g. 4, 6)',
                                 validators=[DataRequired(message='Please enter between 1 and 12 hours'),
                                             NumberRange(min=1, max=12, message='Please enter between 1 and 12 hours')])
    travel_mode = RadioField('How would you like to travel?',
                             choices=[('driving', 'Driving'),
                                      ('bicycling', 'Bicycle'),
                                      ('walking', 'Walking'),
                                      ('', 'No Preference')])
    return_to_start = BooleanField('Would you like to return back to your starting point?')
    submit = SubmitField() # refers to the 'submit' button that will be on the form
