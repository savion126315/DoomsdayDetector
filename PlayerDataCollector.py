import requests

def iracingcheck():
    APP_ID = 266410

    url = "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/"

    resp = requests.get(url, params={"appid": APP_ID}, timeout=10)
    resp.raise_for_status()

    data = resp.json()
    players_online = data["response"]["player_count"]

    return players_online > 0