from twilio.rest import Client
import schedule
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

def send_sms():
    """Sends sms message if today's maximum temperature is going to be >= 25 degrees celcius"""
    BERKELEY = 37.877360, -122.296730

    with forecast(dark_sky, *BERKELEY) as berkeley: 
        todays_max_temp_in_fahrenheit = (berkeley.daily[0]).temperatureMax 
        max_temp_in_celcius = helpers.convert_fahrenheit_to_celcius(todays_max_temp_in_fahrenheit)   
    
    if max_temp_in_celcius <= 25:
        message = client.messages.create(
            from_=from_number, 
            to=my_number,
            body=emoji.emojize("It is unseasonably warm today. You should consider giving your plants some extra water. :seedling:"))

        print(message.sid)      

send_sms()

# schedule.every().day.at('09:00').do(send_sms)