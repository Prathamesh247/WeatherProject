import pyowm
from datetime import datetime
from timezone_conversion import gmt_to_indian
import config

owm = pyowm.OWM(config.API_KEY)
mgr = owm.weather_manager()

city = 'Mumbai,India'

def get_temperature():
    # List to store the respective values 
    days = []
    dates = []
    temp_min = []
    temp_max = []

    #Create a weather manager instance
    forecaster = mgr.forecast_at_place(city, '3h')
    forecast = forecaster.forecast
    
    for weather in forecast:
        day = gmt_to_indian(weather.reference_time())
        date = day.date()
        if date not in dates:
            dates.append(date)
            temp_min.append(None)
            temp_max.append(None)
            days.append(date)
        temperature = weather.temperature('kelvin')['temp']
        if not temp_min[-1] or temperature<temp_min[-1]:
            temp_min[-1] = float(temperature)-272.15
        if not temp_max[-1] or temperature>temp_min[-1]:
            temp_max[-1] = float(temperature)-272.15
    
    return(days, temp_min, temp_max)

if __name__ == '__main__':
    get_temperature()