import requests

def get_airborne_aircraft_count():
    url = "https://opensky-network.org/api/states/all"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    states = data.get("states", [])

    airborne = [
        aircraft for aircraft in states
        if aircraft[8] is False  # index 8 = on_ground
        ]

    return len(airborne) > 500

# print(get_airborne_aircraft_count())
