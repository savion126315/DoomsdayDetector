"""
Class Definition for Doomsday Detector. 


"""
from nyc_subway import subway_running
from PlayerDataCollector import iracingcheck


class DoomsdayDetector():

    def __init__(self):  # Note: All these must add to 1.
        self.weights = {"subway": 0.25,
                        "iracing": 0.1,
                        "dmv": 0.3
                        }
        
        self.values_dict = {}
        self.percentage_chance = 0

    def collection(self) -> None:
        self.values_dict = {"subway":subway_running(),
                       "iracing": iracingcheck()
                       }
        return None

    def calculator(self) -> float:
        self.subway_scaled = self.values_dict["subway"]*self.weights["subway"]
        self.iracing_scaled = self.values_dict["iracing"]*self.weights["iracing"]
        self.dmv_scaled = self.values_dict["dmv"]*self.weights["dmv"]

        self.percentage_chance = self.subway_scaled + self.iracing + self.dmv_scaled
    
    def aggregator(self) -> str:
        pass

    def reporter(self) -> None:
        pass


