# This is what ChatGPT spit out

import requests
from datetime import datetime


def get_next_departure_times():
    api_key = "<YOUR_API_KEY>"
    url = f"https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l.json?key={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        # Find the Morgan Avenue station (stop_id = L14) in the Manhattan direction (direction_id = 1)
        departures = [
            departure for departure in data['departure'] if departure['stop_id'] == 'L14' and departure['direction_id'] == 1
        ]

        # Extract the next three departure times and convert them to minutes from now
        now = datetime.now()
        next_departures = []
        for departure in departures[:3]:
            departure_time = datetime.strptime(departure['departure_time'], "%Y-%m-%dT%H:%M:%S")
            minutes_to_departure = int((departure_time - now).total_seconds() / 60)
            next_departures.append(f"{minutes_to_departure} minutes")

        return next_departures

    else:
        print("Failed to fetch data from the MTA API.")
        return []


# Call the function and print the next departure times
departures = get_next_departure_times()
for i, departure in enumerate(departures, 1):
    print(f"Train {i}: {departure}")
