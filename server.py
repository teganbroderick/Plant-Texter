from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from darksky import forecast
from datetime import date, timedelta

import helpers
import os

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined

dark_sky = os.environ['DARK_SKY_API']

@app.route('/')
def index():
    """Get weather, render index.html"""
    
    BERKELEY = 37.877360, -122.296730

    
    with forecast(dark_sky, *BERKELEY) as berkeley:
        print(berkeley.daily)
        print(berkeley.daily.summary, end='\n---\n')

    todays_weather = 100

    weekday = date.today()
    week_summary = []
    max_temp_array = []
    for day in berkeley.daily:
        day = dict(day = date.strftime(weekday, '%a'),
                   sum = day.summary,
                   tempMin = day.temperatureMin,
                   tempMax = day.temperatureMax
                   )
        min_temp_in_celcius = helpers.convert_fahrenheit_to_celcius(day['tempMin'])
        max_temp_in_celcius = helpers.convert_fahrenheit_to_celcius(day['tempMax'])
        max_temp_array.append(max_temp_in_celcius)
        week_summary_string = day['day'] + ': ' + day['sum'] + ' Temp range: ' + str(min_temp_in_celcius) + '-' + str(max_temp_in_celcius)
        week_summary.append(week_summary_string)
         
        weekday += timedelta(days=1)

    return render_template("index.html", weekly_report=berkeley.daily, week_summary=week_summary, max_temp_array=max_temp_array)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')