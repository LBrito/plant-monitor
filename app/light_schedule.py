import time
import schedule
from devices.light import PlantSpectrum
from datetime import datetime
import json
from pathlib import Path

light = PlantSpectrum()

def getSchedule():
    f = open('/home/pi/.ptm/app/light_schedule.json')
    return json.load(f)

def checkLightSchedule():
    schedule = getSchedule()
    now = datetime.now().time()
    start = now.replace(hour=schedule['start'], minute=0, second=0, microsecond=0)
    end = now.replace(hour=schedule['end'], minute=0, second=0, microsecond=0)
    print("Current Time =", now,". Scheduled to start @", start, " and end @", end)
    if((now > start and now < end)):
        if not light.isOn():
            print("Turning light on!")
            light.switch(isOn = True)
        return
    if(light.isOn()):
        print("Turning light off!")
        light.switch(isOn = False)
    pass

schedule.every(5).minutes.do(checkLightSchedule).run()

while True:
    schedule.run_pending()
    time.sleep(30)
