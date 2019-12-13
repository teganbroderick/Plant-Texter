from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined

darksky = DarkSky()


@app.route('/')
def index():
    """Render index.html"""
    latitude = 37.877360
    longitude = -122.296730
    forecast = darksky.get_forecast(
        latitude, longitude,
        extend=False, # default `False`
        lang=languages.ENGLISH, # default `ENGLISH`
        units=units.AUTO, # default `auto`
        exclude=[weather.MINUTELY, weather.ALERTS], # default `[]`,
        timezone='UTC' # default None - will be set by DarkSky API automatically
        )   
    forecast.latitude # 42.3601
    forecast.longitude # -71.0589
    forecast.timezone # timezone for coordinates. For exmaple: `America/New_York`

    forecast.currently # CurrentlyForecast. Can be found at darksky/forecast.py
    forecast.minutely # MinutelyForecast. Can be found at darksky/forecast.py
    forecast.hourly # HourlyForecast. Can be found at darksky/forecast.py
    forecast.daily # DailyForecast. Can be found at darksky/forecast.py
    forecast.alerts # [Alert]. Can be found at darksky/forecast.py

    
    print(forecast.daily)

    return render_template("index.html")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')