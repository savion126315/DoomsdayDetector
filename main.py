from DoomsdayDef import DoomsdayDetector
import datetime


dd = DoomsdayDetector(["savionragster@gmail.com", "johnnyflips916@gmail.com"])

dd.collection()
dd.calculator()
print(dd.percentage_chance)
dd.reporter()



# while True:
   # if datetime.datetime.now().hour == 9 and datetime.datetime.now().minute == 0:
    # dd.collection()
   # dd.calculator()
   # dd.reporter()