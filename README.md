# Plant Texter

Plant texter is an app that sends me an sms when it is particularly hot and tells me to water my plants.

### Tech Stack
Python, HTML, CSS, Flask, Jinja, Bootstrap <br>
APIs: Dark Sky, Twilio

### Prerequisites

You must have the following to run Plant Texter:

- Python 3.x installed on your computer
- API keys for the Dark Sky API and Twilio API

### Run Plant Texter on your local computer

Clone or fork repository:
```
$ git clone https://github.com/teganbroderick/plant-texter
```
Create and activate a virtual environment inside your Plant Texter directory:
```
$ virtualenv env
$ source env/bin/activate
```
Install dependencies:
```
$ pip install -r requirements.txt
```
Create a secrets.sh file and add your API keys to it.
<br>
Source your secrets.sh file in the terminal:
```
$ source secrets.sh
```
Run the app from the command line.
```
$ python server.py
```
Open another terminal window/tab, activate a virtual environment, source secrets.sh, and run the scheduler from the command line.
```
$ source env/bin/activate
$ source secrets.sh
$ python3 scheduler.py
```

### Features

#### Index Page <br>
The index page asks the question: "Does Tegan need to water her plants today?". It displays "NO" if the maximum temperature in Berkeley that day is less than or equal to 25 degrees celcius, and "YES" if it is greater than or equal to 25 degrees celcius. A Weather Summary button brings up a Modal displaying weather information for that day and the week ahead.
![Index_no](https://raw.githubusercontent.com/teganbroderick/plant-texter/master/static/img/plant-texter-index.gif)
<br><br>
![Index_yes](https://raw.githubusercontent.com/teganbroderick/plant-texter/master/static/img/plant-texter-index-yes.png)
<br>

#### SMS Feature <br>
Every day at 9am, a scheduler checks the maximum temperature in Berkeley for the day. If it is greater than or equal to 25 degrees celcius, I recieve a text message telling me to consider giving my plants some extra water.
![Index_yes](https://raw.githubusercontent.com/teganbroderick/plant-texter/master/static/img/plant-texter-sms.png)
