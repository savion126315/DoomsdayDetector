import requests
import test_metrics

def iracingcheck() -> bool:
    APP_ID = 266410

    url = "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/"

    resp = requests.get(url, params={"appid": APP_ID}, timeout=10)
    resp.raise_for_status()

    data = resp.json()
    players_online = data["response"]["player_count"]
    test_metrics.record("iRacing_Check", "iracing_players", players_online)

    return players_online > 0
