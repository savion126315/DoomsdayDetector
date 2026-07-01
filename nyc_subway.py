import requests
from google.transit import gtfs_realtime_pb2
import time
from datetime import datetime


def subway_running() -> bool:
    """
    Returns True if more than 1 train is coming and is less than 30 mins away. 
    """

    FEED_URL = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz"

    # Myrtle Ave stop IDs
    MYRTLE_STOPS = {"J27N", "J27S"}

    response = requests.get(FEED_URL)

    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(response.content)

    arrivals = []

    for entity in feed.entity:
        if not entity.HasField("trip_update"):
            continue

        trip = entity.trip_update

        for stop_time in trip.stop_time_update:
            if stop_time.stop_id in MYRTLE_STOPS and stop_time.HasField("arrival"):
                arrivals.append(stop_time.arrival.time)

    arrivals.sort()

    # print("\nSubway report for trains at Myrtle Ave:")
    # print("_"*40)
    trains_arriving = False
    trains_arriving = len(arrivals) > 0
    arrival_soon = False
    train_arriving = False

    for t in arrivals[:1]:
        readable = datetime.fromtimestamp(t).strftime("%H:%M:%S")
        minutes = int((t - time.time()) / 60)
        # print(f"Next train at: {readable} (~{minutes} min)")
        trains_arriving = len(arrivals) > 0
        arrival_soon = minutes < 30
        # print(f"Next train < 30 mins away: {arrival_soon}")  # Is nearest train less than 30 mins awayy?
        # print(f"Are any trains coming: {trains_arriving}")

    if trains_arriving and arrival_soon:
        return True
    else:
        return  False

# print(subway_running())  