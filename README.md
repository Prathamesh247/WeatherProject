# WeatherProject

This project is part of the CSL405 Skill-based Lab Course: Python Programming AY 2020-2021

The group members/collaborators on this project are:
@Prathamesh247
@aaryagit

The project focuses on building GUI application in Python
to track weather of a location with the use of 
OpenWeatherMap API, Requests, Json and PyOWM modules.

The second part of the project gives a combined bar chart of the minimum and maximum
temperatures for the current day and the next 5 days with the use of 
Matplotlib, Datetime, Pytz and PyOWM modules.

alltimezones.py enlists all available from pytz module
in the timezones.txt file. Run this to check the timezone of your desired city for the chart.

Steps to get the OpenWeatherMap API key:
1) Go to https://openweathermap.org/
2) Sign up using either email or other social credentials
3) Get the free tier API key and you are good to go!

Make sure to create a config.py file locally to store "your own" API key. 

To use the 1st part, run the weather.py file
To use the 2nd part, run the chart.py

The trial folder contains results of previous attempts to add new features.