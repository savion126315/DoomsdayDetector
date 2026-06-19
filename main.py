from DoomsdayDef import DoomsdayDetector
import datetime


dd = DoomsdayDetector(["savionragster@gmail.com", "johnnyflips916@gmail.com"])

while True:
    if datetime.datetime.now().hour == 9 and datetime.datetime.now().minute == 0:
        dd.collection()
        dd.calculator()
        dd.reporter()