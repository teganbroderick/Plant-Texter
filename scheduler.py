from flask import Flask
from server import *

import schedule
import requests, json, time

from datetime import date

from twilio.rest import Client

import helpers
import os

app = Flask(__name__)

def job():
    """Finds out whether today's temperature is above 
    25 degrees celcius, sends text if it is.
    """