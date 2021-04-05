# -*- coding: utf-8 -*-
"""
Spyder Editor and VS Code Editor
This is a temporary script file.
"""

import requests,json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

api_key = "56b68c7a673ba0a55a2035d3d7c0a2eb"

def credits():
    cred=Toplevel()
    cred.geometry('300x170')

def proceed():
    cityname=name.get()
    if cityname=='':
        return messagebox.showerror('Error','Enter City Name')
    elif api_key!='56b68c7a673ba0a55a2035d3d7c0a2eb':
        return messagebox.showerror('Error','Enter your api key')

    else:
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + cityname 
        response = requests.get(complete_url) 
        x = response.json()  
        
        if x["cod"] != "404":
            y = x["main"] 
            currenttemp = y["temp"] 
            currentpressure = y["pressure"] 
            currenthumidiy = y["humidity"]
            z = x["weather"] 
            weather_description = z[0]["description"]  
            Label(home,text='Temperature: '+str(round(currenttemp-272.15))+' degree celsius').place(x=2,y=90)
            Label(home,text='Atmospheric Pressure: '+str(currentpressure)+' hPa').place(x=2,y=120)
            Label(home,text='Humidity: '+str(currenthumidiy)).place(x=2,y=150)
            Label(home,text='Description: '+str(weather_description)).place(x=2,y=180)
        else: 
            return messagebox.showerror('Error','No City Found')
   

home=Tk()
home.geometry('400x400')
home.title('Weather App 1.1')
name=StringVar()

Label(home,text='Tkinter Weather',font='Helvetica 12 bold').grid(row=1,column=3)
Label(home,text='Enter City:').grid(row=2,column=1)
Entry(home,width=15,textvariable=name).grid(row=2,column=2)
Button(home,text='Proceed',command=proceed).grid(row=3,column=3)

home.mainloop()