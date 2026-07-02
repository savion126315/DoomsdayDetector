import requests

loc = requests.get("https://ipinfo.io/json").json()

# print(f"You appear to be near {loc['city']}, {loc['region']}, {loc['country']}")
