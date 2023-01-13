import os.path

from .Models.weather import Weather
from .Models.forecast import Forecast
from .weather_api import WeatherAPI
from Visuals.surface_generator import SurfaceGenerator
from pygame.surface import Surface
from typing import List, Optional

k_BASE_ICON_PATH = "Visuals/images/weather_icons"


class WeatherManager:
    """"A class for getting pertinent weather information"""

    def __init__(self):
        self.current_weather: Optional[Weather] = None
        self.next_precipitation_forecast_slice: Optional[Forecast] = None
        self.update_weather()

    def update_weather(self):
        """Updates the stored weather data. Intended to be called ~1x/min"""
        self.current_weather = WeatherAPI.get_current_weather()
        self.next_precipitation_forecast_slice = WeatherAPI.next_precipitation_forecast()

    def get_current_weather_description(self) -> str:
        """Provides a string that describes the current weather"""
        if self.current_weather is None:
            raise Exception("WeatherInterface: self.current_weather is unexpectedly None")

        return self.current_weather.description

    def get_current_weather_icon_filename(self) -> str:
        """Provides the file name for the icon to use"""
        if self.current_weather is None:
            raise Exception("WeatherInterface: self.current_weather is unexpectedly None")

        return self.current_weather.get_icon_filename()

    def get_next_precipitation_string(self) -> str:
        """Provides a string that explains when (if ever) the next precipitation is expected"""
        if self.next_precipitation_forecast_slice:
            forecast_slice = self.next_precipitation_forecast_slice
            description = forecast_slice.weather.description
            return f"Expect {description.lower()} in {forecast_slice.time_to_forecast_string()} or so."

        return "No precipitation expected in the next five days!"

    def get_weather_content(self) -> List[Surface]:
        """Provide the list of surfaces to be rendered for the weather"""
        content: List[Surface] = []
        self.update_weather()
        # 1 "Current weather:"
        content.append(SurfaceGenerator.text_surface("Current weather:"))
        # 2 - Current weather image
        path_to_icon = os.path.join(k_BASE_ICON_PATH, self.current_weather.get_icon_filename())
        content.append(SurfaceGenerator.image_surface(path_to_icon))
        # 3 - Current Weather description
        content.append(SurfaceGenerator.text_surface(self.current_weather.description))
        content.append(SurfaceGenerator.spacer(100))
        # 4 - Next precipitation string
        precip_string = self.get_next_precipitation_string()
        content.append(SurfaceGenerator.text_surface(precip_string))

        return content

