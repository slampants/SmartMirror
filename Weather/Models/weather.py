from typing import Dict


class Weather:
    def __init__(self, weather_dict: Dict):
        self.id: int = weather_dict.get('id')
        self.description: str = weather_dict.get('description')
        self.icon_name: str = weather_dict.get('icon')

    def get_icon_filename(self) -> str:
        """Returns the actual filename for the icon"""
        return f"{self.icon_name}.png"
