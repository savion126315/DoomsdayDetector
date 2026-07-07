"""
Main program for running Doomsday Detector. 

Run with python3 main.py

Savion Ragster and Johnny Tieman 2026
"""

from DoomsdayDef import DoomsdayDetector
from location_helper import loc
import datetime
import test_metrics

dd = DoomsdayDetector(["savionragster@gmail.com", "johnnyflips916@gmail.com"])

dd.collection()
dd.calculator()
test_metrics.record("Location", "Location", f"{loc['city']}, {loc['region']}, {loc['country']}")
test_metrics.write_csv()


# print("Program running, press Ctrl+C to stop.")
# while True:
#    if datetime.datetime.now().hour == 9 and datetime.datetime.now().minute == 0:
#         print(f"You appear to be near {loc['city']}, {loc['region']}, {loc['country']}")
#         dd.collection()
#         dd.calculator()
#         dd.reporter()
