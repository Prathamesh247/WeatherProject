# -*- encoding: utf-8 -*-
"""
Spyder Editor and VS Code Editor
"""

import requests, json
from tkinter import *
from tkinter import messagebox
from config import API_KEY

degree_sign= u'\N{DEGREE SIGN}'

def check():
    # Take city name as input 
    cityname = name.get()

    # Error for blank entry
    if cityname=='':
        return messagebox.showerror('Error', 'Enter City Name')

    else:
        # Base URL for API call
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        # Complete URL for API call with city name 
        complete_url = base_url+"q="+cityname+"&appid="+API_KEY
        
        # GET method from requests, returns an object
        response = requests.get(complete_url)
        
        # Convert json data to pyhton-readable
        # data format in the form of list of nested dictionaries
        city = response.json()  
        
        # Proceed if the coordinates are found
        # i.e. the value of key "cod" is not 404
        if city["cod"] != "404":

            # Retrieve the current weather conditions
            main = city["main"] 
            currenttemp = main["temp"] 
            currentpressure = main["pressure"] 
            currenthumidiy = main["humidity"]

            # Retrieve weather description
            weather = city["weather"] 
            weather_description = weather[0]["description"]

            # Display the results
            Label(home, text='Temperature: ' +str(round(currenttemp-272.15))+ degree_sign+ ' C').place(x=11,y=90)
            Label(home, text='At. Pressure: ' +str(currentpressure)+ ' hPa').place(x=141,y=90)
            Label(home, text='Humidity: ' +str(currenthumidiy)+ '%').place(x=290,y=90)
            Label(home, text='Description: ' +str(weather_description).capitalize()).place(x=150,y=111)

        # Display error popup
        else: 
            return messagebox.showerror('Error','No City Found')
   

home=Tk()
home.geometry('400x200')
home.title('Weather App 2.0')
name = StringVar()

Label(home, text='Tkinter Weather', font='Roboto 12 bold').grid(row=1,column=3)
Label(home, text='Enter City:').grid(row=2,column=1)
Entry(home, width=15, textvariable=name).grid(row=2,column=2)
Button(home, text='Check', command=check).grid(row=3,column=3)

home.mainloop()