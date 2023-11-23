import time
import schedule
from devices.relay_device import RelayDevice
from datetime import datetime
import json
import os

light = RelayDevice(27)
pump = RelayDevice(22)


def get_schedule():
    f = open(os.environ["PTM_HOME"] + '/app/light_schedule.json', 'r')
    config = json.load(f)
    start = datetime.strptime(config['start'], "%H:%M")
    end = datetime.strptime(config['end'], "%H:%M")
    return start, end


def check_light_schedule():
    start, end = get_schedule()
    now = datetime.now().time()
    start = now.replace(hour=start.hour, minute=start.minute, second=0, microsecond=0)
    end = now.replace(hour=end.hour, minute=end.minute, second=0, microsecond=0)
    print("Current Time =", now, ". Scheduled to start @", start, " and end @", end)
    if start < now < end:
        if not light.is_on():
            print("Turning light on!")
            light.switch(is_on=True)
        return
    if light.is_on():
        print("Turning light off!")
        light.switch(is_on=False)
    pass


def get_watering_schedule():
    f = open(os.environ["PTM_HOME"] + '/app/watering_schedule.json', 'r')
    config = json.load(f)


def check_pump_schedule():
    pump.switch(is_on=False)


schedule.every(5).minutes.do(check_light_schedule).run()
schedule.every().wednesday.saturday.do(check_pump_schedule).run()

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
finally:
    light.reset()
