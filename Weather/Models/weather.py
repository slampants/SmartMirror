from typing import Dict

k_WEATHER_KEY = "weather"
k_MAIN_KEY = "main"
k_CURRENT_TEMP_KEY = "temp"
k_MIN_TEMP_KEY = "temp_min"


class Weather:
    def __init__(self, weather_dict: Dict):
        temp_dict: Dict = weather_dict[k_MAIN_KEY]
        self.current_temp: int = int(temp_dict[k_CURRENT_TEMP_KEY])
        self.low_temp: int = int(temp_dict[k_MIN_TEMP_KEY])
        weather_values_dict = weather_dict[k_WEATHER_KEY][0]
        self.id: int = weather_values_dict.get('id')
        self.description: str = weather_values_dict.get('description', "No description available").capitalize()
        self.icon_name: str = weather_values_dict.get('icon')

    def get_icon_filename(self) -> str:
        """Returns the actual filename for the icon"""
        return f"{self.icon_name}.png"
