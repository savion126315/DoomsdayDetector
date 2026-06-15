"""
Class Definition for Doomsday Detector. 


"""
from nyc_subway import subway_running
from PlayerDataCollector import iracingcheck
from dmv import dmv_wait_times
from email_handler import send_email
import utils


class DoomsdayDetector():

    def __init__(self):  # Note: All these must add to 1.
        self.weights = {"subway": 0.25,
                        "iracing": 0.1,
                        "dmv": 0.3
                        }
        
        self.values_dict = {}
        self.percentage_chance = 0

    def collection(self) -> None:
        logger = utils.get_logger("Collection")
        logger.info("Collecting world stats...")

        self.values_dict = {"subway":subway_running(),
                       "iracing": iracingcheck(),
                       "DMV": dmv_wait_times()
                       }
        
        return None

    def calculator(self) -> float:
        logger = utils.get_logger("Calculator")
        logger.info("Crunching numbers")

        self.subway_scaled = self.values_dict["subway"]*self.weights["subway"]
        self.iracing_scaled = self.values_dict["iracing"]*self.weights["iracing"]
        self.dmv_scaled = self.values_dict["dmv"]*self.weights["dmv"]

        self.percentage_chance = self.subway_scaled + self.iracing + self.dmv_scaled
    
    def aggregator(self) -> str:
        pass

    def reporter(self) -> None:
        logger = utils.get_logger("Reporter")
        logger.info("Sending out email report!")
        send_email(["savionragster@gmail.com", "johnnyflips916@gmail.com"], f"There is a {1-self.percent_chance} that the world has ended.")
