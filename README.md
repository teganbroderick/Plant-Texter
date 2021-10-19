# Plant Texter

Plant Texter is an app that sends me a text message when the weather in Berkeley is over 25 degrees celcius, reminding me to water my plants. The app has two main features - a website that displays weather information and tells me whether I need to water my plants, and the scheduled sms reminder.

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
The index page asks the question: "Does Tegan need to water her plants today?". It displays "YES" if the maximum temperature for the day in Berkeley is >= 25 degrees celcius, and "NO" if not. A Weather Summary button brings up a modal displaying weather information for that day and the week ahead. <br>
![Index_no](https://raw.githubusercontent.com/teganbroderick/plant-texter/master/static/img/plant-texter-index.gif)
<br><br>
<img src="https://raw.githubusercontent.com/teganbroderick/plant-texter/master/static/img/plant-texter-index-yes.png" width="62%" height="62%"/>


#### SMS Feature <br>
Every day at 9am, a scheduler checks the maximum temperature in Berkeley for the day. If it is greater than or equal to 25 degrees celcius, I receive a text message telling me to consider giving my plants some extra water. <br>
<img src="https://raw.githubusercontent.com/teganbroderick/plant-texter/master/static/img/plant-texter-sms.png" width="40%" height="40%"/>
