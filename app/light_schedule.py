import time
import schedule
from devices.light import PlantSpectrum
from datetime import datetime
import json
from pathlib import Path

light = PlantSpectrum()

def getSchedule():
    f = open('/home/pi/.ptm/app/light_schedule.json')
    config = json.load(f)
    start = datetime.strptime(config['start'], "%H:%M")
    end = datetime.strptime(config['end'], "%H:%M")
    return start, end

def checkLightSchedule():
    start, end = getSchedule()
    now = datetime.now().time()
    start = now.replace(hour=start.hour, minute=start.minute, second=0, microsecond=0)
    end = now.replace(hour=end.hour, minute=end.minute, second=0, microsecond=0)
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
