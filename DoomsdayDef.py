"""
Class Definition for Doomsday Detector. 


"""
from nyc_subway import subway_running
from PlayerDataCollector import iracingcheck
from dmv import dmv_wait_times
from email_handler import send_email
from flight_tracker import get_airborne_aircraft_count
from google_ping import google_ping
import utils


class DoomsdayDetector():

    def __init__(self, email_list: list):  # Note: All these must add to 1.
        self.email_list = email_list
        self.weights = {"subway": 0.25,
                        "iracing": 0.1,
                        "dmv": 0.3,
                        "flights": 0.25,
                        "google": 0.1
                        }
        
        self.values_dict = {}
        self.percentage_chance = 0

    def collection(self) -> None:
        logger = utils.get_logger("Collection")
        logger.info("Collecting world stats...")

        self.values_dict = {"subway":subway_running(),
                            "iracing": iracingcheck(),
                             "DMV": dmv_wait_times(),
                            "flights": get_airborne_aircraft_count(),
                            "google": google_ping()
                            }
        return None

    def calculator(self) -> float:
        logger = utils.get_logger("Calculator")
        logger.info("Crunching numbers")

        self.subway_scaled = self.values_dict["subway"]*self.weights["subway"]
        self.iracing_scaled = self.values_dict["iracing"]*self.weights["iracing"]
        self.dmv_scaled = self.values_dict["dmv"]*self.weights["dmv"]
        self.flights_scaled = self.values_dict["flights"]*self.weights["flights"]
        self.google_scaled = self.values_dict["google"]*self.weights["google"]       

        self.percentage_chance = self.subway_scaled + self.iracing_scaled + self.dmv_scaled + self.flights_scaled + self.google_scaled  # Total percent chance.
  
    def reporter(self) -> None:
        logger = utils.get_logger("Reporter")
        logger.info("Sending out email report!")
        send_email(self.email_list, f"There is a {1-self.percentage_chance} that the world has ended.")
