import requests
from google.transit import gtfs_realtime_pb2
import time
from datetime import datetime
import test_metrics


def subway_running() -> bool:
    """
    Returns True if more than 1 train is coming and is less than 30 mins away. 
    """

    FEED_URL = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz"

    # Myrtle Ave stop IDs
    MYRTLE_STOPS = {"J27N", "J27S"}
    trains_arrving_bool = False  # If any trains are coming at all.
    arrival_soon_bool = False  # Bool if train is coming < 30 mins. 
    

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
    trains_arriving_num = len(arrivals) > 0  # If there's at least one train coming.

    for t in arrivals[:1]:
        readable = datetime.fromtimestamp(t).strftime("%H:%M:%S")
        minutes = int((t - time.time()) / 60)
        # print(f"Next train at: {readable} (~{minutes} min)")

        trains_arriving_num: int = len(arrivals)
        trains_arrving_bool: bool = trains_arriving_num > 0 
        next_train_arriving_min = minutes
        arrival_soon_bool: bool = next_train_arriving_min < 30
        test_metrics.record("nyc_subway,Myrtle_stop", "trains_arriving", trains_arriving_num)
        test_metrics.record("nyc_subway,Myrtle_stop", "arrival_soon", next_train_arriving_min)

    if arrival_soon_bool and trains_arrving_bool:
        return True
    else:
        return  False
    