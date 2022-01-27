from flask import Flask, request, make_response
from api_methods import OpenWeatherApi

app = Flask(__name__)
open_weather_api_object = OpenWeatherApi()

@app.route('/weather/current', methods=['GET'])
def getCityCurrentWeatherByName():
    return make_response(open_weather_api_object.getCityCurrentWeatherByName(request.args.get('city_name'))) 

@app.route('/weather/forecast', methods=['GET'])
def getCityForecastWeatherByName():
    return open_weather_api_object.getCityForecastWeatherByName(request.args.get('lat'), request.args.get('lon'))
