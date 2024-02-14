# Nigerian Weather Data Collection and Scraping

## Overview
This repository contains scripts and documentation for collecting and scraping weather data for cities in Nigeria using the OpenWeather API. 
The dataset encompasses a range of weather parameters, including temperature, humidity, wind speed, and more, providing a comprehensive overview 
of weather conditions across the country.

## Contents
1. Data Collection Script:

The main.py file is the main Python script responsible for interfacing with the OpenWeather API, retrieving real-time weather data for each city, 
and storing it in a structured format - CSV.

2. Scraped City Data:

The scraped_data folder includes information about scraped about all cities in Nigeria, such as names and coordinates. This data is used to batch process weather data 
retrieval for each city.

3. Dependencies:
Ensure that the required Python libraries are installed. You can install them using the following command:

`shell
pip install -r requirements.txt
`

## Usage
1. API Key:

Obtain an API key from OpenWeather and replace the placeholder in the script with your key.

2. Run the Script:

Execute the main.py script to initiate data collection. Adjust parameters such as the number of cities processed concurrently, time intervals, etc., based on your requirements.

3. Data Storage:

The collected weather data will be stored in a file (e.g., nigeria-cities-weather-data.csv). Customize the storage mechanism if needed.

## Customization
Feel free to customize the script or incorporate additional features based on specific project requirements. Consider parallel processing, error handling, 
or integrating with other APIs for enhanced functionality.

## Contributions
Contributions are welcome! If you identify improvements or additional features, submit a pull request to enhance the functionality and robustness of the data collection process.


## Acknowledgments
OpenWeather for providing the API to access real-time weather data.
Contributors to the project for their efforts in enhancing and maintaining the data collection script.

Happy data collecting! 🌦️
