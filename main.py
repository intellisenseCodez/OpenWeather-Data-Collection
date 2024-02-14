
# Collecting Weather data from OpenWeather.
import requests
import json
import csv
import os


from dotenv import load_dotenv


def get_weather_data(latitude, longitude):
    """ Given the latitude and longitude of a city return the weather details """
    
    API_KEY = os.environ.get('OPEN_WEATHER_API_KEY')
    try:
        weather_api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}"
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
    


def main():
    
    load_dotenv()
    
    scraped_data = 'scraped_data'
    
    # loop through each data in the json object
    with open('nigeria-cities-weather-data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        
            fieldnames = ['country','city','latitude','longitude','temp','temp_min','temp_max','pressure','humidity','sea_level','ground_level','wind_speed','wind_degree','sunrise','sunset','rain_1h','rain_3h','timezone','cloud','description', 'region', 'population']
            
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
    
            if os.path.isdir(scraped_data):
                # loop through all files in the directory
                for file in os.listdir(scraped_data):
                    sample = ['ekiti.json','lagos.json','ogun.json','ondo.json','osun.json','oyo.json']
                    if file in sample:
                        file_path = os.path.join(scraped_data,file)
                        
                        with open(file=file_path, mode='r') as json_file:
                            json_data = json.load(json_file)
                            print(file_path)
                            for data in json_data: 
                                if isinstance(data, dict):
                                    lat = data['lat']
                                    long = data['long']
                                    region = data['region']
                                    population = data['pop est']
                                    
                                    if lat != None and long != None:
                                        data = get_weather_data(latitude=lat, longitude=long)
                                        if isinstance(data, dict):
                                            data['region']= region
                                            data['population'] = population

                                            if isinstance(data, dict):
                                                writer.writerow(data)


if __name__ == "__main__":
    main()
    
    
    
                
                
                    
                
       

