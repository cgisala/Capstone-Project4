import requests
import sqlite3
from datetime import datetime
import os

db = os.path.join('database', 'travel_app.db')
# key = os.environ.get('WEATHER_KEY') #Uers must provide their own API key
key = '931ff5eff05bb2caa4f58e70a64f78bb' # Only use for practice


class CurrentWeather():
    # This class deals with the current weather 

    def __init__(self,city):
        self.city = city # Instance variable city
        self.validate = Validation()
        self.url = 'https://api.openweathermap.org/data/2.5/weather'  # Domain and path

    def get_weather(self):

        # Returns the current weather
        weather_data = self.get_weather_data(self.url) 
        if weather_data:
            return weather_data['weather'][0]['description']

    def get_average_temp(self):

        # Returns the average current temperature
        weather_data = self.get_weather_data(self.url)
        if weather_data:
            return weather_data['main']['temp']

    def get_feels_like(self):

        # Returns what the temp feels like with wind
        weather_data = self.get_weather_data(self.url)
        if weather_data:
            return weather_data['main']['feels_like']
    
    def get_lowest_temp(self):

        # Returns lowest temperature
        weather_data = self.get_weather_data(self.url)
        if weather_data:
            return weather_data['main']['temp_min']

    def get_Highest_temp(self):

        # Returns lowest temperature
        weather_data = self.get_weather_data(self.url)
        if weather_data:
            return weather_data['main']['temp_max']

    def get_weather_data(self,url):

        # Takes the city and returns weather API data for that city
        location = f'{self.city},us'  # city and country
        query = {'q': location, 'units':'imperial', 'appid': key} # formats the location, units, and API key into a dictionary
        api_data = self.validate.api_connection(url, query)
        weather_data = self.validate.object_empty(api_data)
        
        return weather_data

class ForecastWeather():
    
    def __init__(self,city):
        self.city = city
        self.validate = Validation()
        self.url = 'https://api.openweathermap.org/data/2.5/forecast'  # Domain and path

    def get_two_day_forecast(self):

        # Gets a two day forecast
        data = self.get_forecast_data(self.url)
        weather_forecast = data['list']
        weather = []
        if weather_forecast:
            for forecast in weather_forecast:
                timestamp = forecast['dt'] #Unix timestamp
                date = datetime.fromtimestamp(timestamp) # Convert to a datetime, for humans
                temp = forecast['main']['temp']
                weather.append(f'{date} temp is {temp}')

        return weather

    def get_forecast_data(self,url):

        # Takes the city and returns weather API data for that city
        location = f'{self.city},us'  # city and country
        query = {'q': location, 'units':'imperial', 'appid': key} # formats the location, units, and API key into a dictionary
        api_data = self.validate.api_connection(url, query)
        weather_data = self.validate.object_empty(api_data)

        return weather_data

class Validation():

    def api_connection(self,url, query):

        # Checks if able to connect to the API server and if not returns an error message
        try:
            data = requests.get(url, params=query).json()
            return data
        except:
            print('Error - unable to connect to the API server')

    def object_empty(self,data):

        # Checks to see if weather data is empty
        if data is None:
            print('Error - there is no data in the object')
        else:
            return data








