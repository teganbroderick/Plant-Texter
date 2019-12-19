from twilio.rest import Client
import schedule
import time
from darksky import forecast
from datetime import date, timedelta
import emoji

import helpers
import os

#Get darksky api key
dark_sky = os.environ['DARK_SKY_API']

#Get twilio api keys
account_sid = os.environ['account_sid']
auth_token  = os.environ['auth_token']
my_number = os.environ['my_number']
from_number = os.environ['from_number']

client = Client(account_sid, auth_token)

def check_weather():
    """Get today's max temperature in berkeley.
    Send sms message if max temperature is above 25 degrees celcius
    """
    
    BERKELEY = 37.877360, -122.296730

    with forecast(dark_sky, *BERKELEY) as berkeley: 
        todays_max_temp_in_fahrenheit = (berkeley.daily[0]).temperatureMax 
        max_temp_in_celcius = helpers.convert_fahrenheit_to_celcius(todays_max_temp_in_fahrenheit)   
    
    #if max_temp above 25, send sms
    if max_temp_in_celcius >= 25:
        message = client.messages.create(
            from_=from_number, 
            to=my_number,
            body=emoji.emojize("It is unseasonably warm today. You should consider giving your plants some extra water. :seedling:"))
        print(message.sid)      

# check_weather()

schedule.every().day.at('09:00').do(check_weather)

while True:
    schedule.run_pending()
    time.sleep(1)