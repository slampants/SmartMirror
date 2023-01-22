from typing import List, Optional
from .Models.weather import Weather
from .Models.forecast import Forecast
from .constants import *

import json
import requests

PAYLOAD = {
    "lat": CURRENT_LOCATION_LATITUDE,
    "lon": CURRENT_LOCATION_LONGITUDE,
    "appid": API_KEY,
    "units": "imperial",
}

k_LIST_KEY = "list"


class WeatherAPI:
    """
    An interface with the forecast service API
    More info: https://openweathermap.org/api
    """
    @staticmethod
    def get_current_weather() -> Weather:
        """Returns the `weather` object based on the first weather list item in the response"""
        response = requests.get(CURRENT_WEATHER_URL, params=PAYLOAD)
        current_weather_dict = json.loads(response.text)
        return Weather(current_weather_dict)

    @staticmethod
    def get_forecast_slices() -> List[Forecast]:
        """Returns the `weather` object based on the first weather list item in the response"""
        all_forecasts: List[Forecast] = []
        response = requests.get(FORECAST_URL, params=PAYLOAD)
        content = json.loads(response.text)
        content_list = content[k_LIST_KEY]
        for forecast in content_list:
            all_forecasts.append(Forecast(forecast))
        return all_forecasts

    @staticmethod
    def next_precipitation_forecast() -> Optional[Forecast]:
        """
        Returns the next forecast slice where precipitation is predicted with POP >= k_PRECIP_THRESHOLD
        Returns None if no slice predicts precipitation
        """

        forecasts = WeatherAPI.get_forecast_slices()
        for forecast in forecasts:
            if forecast.possibility_of_precipitation >= k_PRECIP_THRESHOLD and \
                    forecast.weather.id in k_PRECIPITATION_CODES:
                return forecast

        return None
