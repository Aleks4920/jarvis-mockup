from __main__ import *
import python_weather
from geopy.geocoders import Nominatim
import geocoder
import requests
import json
import math
url = "https://community-open-weather-map.p.rapidapi.com/weather"

def getloaction():
    geolocator = Nominatim(user_agent="geoapiExercises")
    g = geocoder.ip('me')
    location = str(geolocator.reverse(g.latlng))
    data = location.split(", ")
    return data

def local():
    data = getloaction()
    api_key = "20f90078bf041039c1967bb5e1f9cabe"
    base_url = "http://api.openweathermap.org/data/2.5/weather?units=metric&"
    city_name = data[2]
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    json_data = response.json()
    forcast =str(json_data['weather'][0]['description'])
    temp = str(round(int(json_data['main']['temp'])))
    feelsLike =str(round(int(json_data['main']['feels_like'])))
    string = str("the weather calls for"+forcast + temp + "degrees celcius, feels like"+ feelsLike)
    return string
