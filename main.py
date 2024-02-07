
# Collecting Weather data from OpenWeather.

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
 


def get_weather_data(latitude, longitude):
    """ Given the latitude and longitude of a city return the weather details """
    try:
        weather_api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={OPEN_WEATHER_API_KEY}"
        response = requests.get(url = weather_api).json()

        # data collection
        data = {
            'country': response['sys']['country'],
            'city': response['name'],
            'latitude': response['coord']['lat'],
            'longitude': response['coord']['lon'],
            'temp': response['main']['temp'],
            'temp_min': response['main']['temp_min'],
            'temp_max': response['main']['temp_max'],
            'pressure': response['main']['pressure'],
            'humidity': response['main']['humidity'],
            'sea_level': response['main']['sea_level'],
            'ground_level': response['main']['grnd_level'],
            'wind_speed': response['wind']['speed'],
            'wind_degree': response['wind']['deg'],
            'sunrise': response['sys']['sunrise'],
            'sunset': response['sys']['sunset'],
            'rain_1h': response['rain']['1h'] if 'rain' in response and '1h' in response['rain'] else None,
            'rain_3h': response['rain']['3h'] if 'rain' in response and '3h' in response['rain'] else None,
            'timezone': response['timezone'],
            'cloud': response['clouds']['all'],
            'description': response['weather'][0]['description']
            }
        return data
    except KeyError as err:
        return f"{err}"
    except:
        return f"Couldnt connect to {weather_api}."
    



if __name__ == "__main__":

    cities_data = load_cities('states-and-cities.json')
    
    # loop through each data in the json object
    with open('nigeria-cities-weather-data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        
            fieldnames = ['country','city','latitude','longitude','temp','temp_min','temp_max','pressure','humidity','sea_level','ground_level','wind_speed','wind_degree','sunrise','sunset','rain_1h','rain_3h','timezone','cloud','description']
            
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            
            for data in cities_data:
                for name in data['cities']:
                    
                    # get latitude and longitude of a city
                    lat, long = get_lat_long(name)[0], get_lat_long(name)[1]
                    
                    # print(lat, long)
                    
                    if lat != None and long != None:
                        # get weather dat
                        info = get_weather_data(latitude=lat, longitude=long) 
                        writer.writerow(info)
    
    
                
                
                    
                
       

