"""
Use like:
# print(f"You appear to be near {loc['city']}, {loc['region']}, {loc['country']}")

Savion Ragster 2026
"""

import requests


loc = requests.get("https://ipinfo.io/json").json()
