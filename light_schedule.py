import time
import schedule
from light import PlantSpectrum
from datetime import datetime

light = PlantSpectrum()

def checkLightSchedule():
    now = datetime.now().time()
    today6am = now.replace(hour=7, minute=0, second=0, microsecond=0)
    today5pm = now.replace(hour=16, minute=30, second=0, microsecond=0)
    print("Current Time =", now)
    if((now > today6am and now < today5pm)):
        if not light.isOn():
            print("Turning light on!")
            light.switch(isOn = True)
        return
    if(light.isOn()):
        print("Turning light off!")
        light.switch(isOn = False)
    pass

schedule.every(10).minutes.do(checkLightSchedule)

checkLightSchedule()

while True:
    schedule.run_pending()
    time.sleep(60)
