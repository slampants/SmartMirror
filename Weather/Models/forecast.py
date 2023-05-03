from .weather import Weather
from datetime import datetime
from typing import Dict

k_MINUTES_IN_HOUR = 60
k_MINUTES_IN_DAY = 1440


class Forecast:
    """A forecast interval slice"""
    def __init__(self, forecast_slice: Dict):
        raw_timestamp = float(forecast_slice.get('dt'))
        self.datetime: datetime = datetime.fromtimestamp(raw_timestamp)
        self.possibility_of_precipitation: float = forecast_slice.get('pop')
        self.weather = Weather(forecast_slice)

    def _minutes_from_now(self) -> float:
        """How many minutes this Forecast slice is from the current time"""
        delta = self.datetime - datetime.now()
        delta_seconds = delta.seconds
        return float(delta_seconds) / 60.0

    def time_to_forecast_string(self) -> str:
        """Provides a string describing the time to this forecast in the most appropriate unit"""
        time_description: str = str()
        minutes: float = self._minutes_from_now()
        hours = minutes / 60.0
        if minutes >= k_MINUTES_IN_DAY:
            days = round(hours / 24)
            time_description = f"{days} days"

        elif minutes >= k_MINUTES_IN_HOUR:
            hours_string = str(round(hours))
            time_description = f"{hours_string} hour{'' if hours == 1 else 's'}"

        else:
            rounded_minutes = round(minutes)
            time_description = f"{rounded_minutes} minute{'' if rounded_minutes == 1 else 's'}"

        return time_description
