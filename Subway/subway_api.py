import requests

from .constants import *
from datetime import datetime
from typing import List, Optional

'''
Notes

To get the stop ID of a particular station, you need to consult the GTFS Static feed
https://api.mta.info/#/staticFeeds

TODO: The static feeds can also provide info about service outages
'''


class SubwayAPI:
    """A class for handling the API side of things"""
    @staticmethod
    def __make_request() -> Optional[requests.Response]:
        """Make a request to the API and return the response"""
        url = f"https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l.json"
        headers = {"x-api-key": k_API_KEY}

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response

        return None

    @staticmethod
    def __get_next_departure_times_strings(resp: requests.Response) -> List[str]:
        """Get a list of the next three departure times in minutes from now"""
        trains = resp.json()['entity']
        desired_updates = []
        for train in trains:
            if train["trip_update"] is not None:
                for update in train["trip_update"]['stop_time_update']:
                    if update['stop_id'] == "L14N":
                        desired_updates.append(update['arrival']['time'])

        result: [str] = []
        next_three_arrival_timestamps = sorted(desired_updates)[:3]
        for departure_time in next_three_arrival_timestamps:
            now = datetime.now()
            departure_time_datetime = datetime.fromtimestamp(departure_time)
            minutes_to_departure = int((departure_time_datetime - now).total_seconds() / 60)
            result.append(f"{minutes_to_departure} minutes")

        return result

    @staticmethod
    def __departure_time_string(departure: dict):
        """Returns the minutes to departure from current moment for a given departure dictionary"""
        # Extract the next three departure times and convert them to minutes from now
        now = datetime.now()
        departure_time = datetime.strptime(departure['departure_time'], "%Y-%m-%dT%H:%M:%S")
        minutes_to_departure = int((departure_time - now).total_seconds() / 60)
        return f"{minutes_to_departure} minutes"

    @staticmethod
    def get_subway_departure_strings() -> List[str]:
        """Method for outside callers to get the requisite subway info"""
        resp = SubwayAPI.__make_request()
        failure_string_list = ["N/A"] * 3
        # TODO: Handle this differently?
        if not resp:
            return failure_string_list

        departure_strings = SubwayAPI.__get_next_departure_times_strings(resp)
        return departure_strings
