import requests
import os

class OpenWeatherApi:
    def __init__(self):
        self.open_weather_api_key=os.environ.get('OPEN_WEATHER_API_KEY')
        self.open_weather_current_url=os.environ.get('OPEN_WEATHER_CURRENT_API_URL')
        self.open_weather_forecast_url=os.environ.get('OPEN_WEATHER_FORECAST_API_URL')

    def getCityCurrentWeatherByName(self, city_name):
        api_url = self.open_weather_current_url + self.open_weather_api_key + '&q=' + city_name

        responseData = requests.get(api_url)
        return responseData.json()

    def getCityForecastWeatherByName(self, lat, lon):
        api_url = self.open_weather_forecast_url + self.open_weather_api_key + '&lat=' + lat + '&lon=' + lon + '&exclude=current,minutely,hourly'

        responseData = requests.get(api_url)
        return responseData.json()
