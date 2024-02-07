import requests

import json
import csv


from secret import OPEN_WEATHER_API_KEY


def load_cities(file_path):
    """ load all cities from json file """
    try:
        with open(file=file_path, mode='r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError as err:
        print(err)
    except:
        print("Error Encountered")

    
def get_lat_long(city_name):
    """ Given a location return the latitude and longitude. """
    
    lat, long = None, None

    
    try:
        geo_api = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={OPEN_WEATHER_API_KEY}"
        response = requests.get(url = geo_api).json()
    except:
        return f"Couldnt connect to {geo_api}."
    else:
        # check if the response return atleast an item
        if len(response) != 0:
            lat = response[0]['lat']
            long = response[0]['lon']
            
    return (lat, long)


print(get_lat_long("yeeyu"))