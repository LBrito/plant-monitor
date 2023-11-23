import time
import schedule
from devices.relay_device import RelayDevice
from datetime import datetime
import json
import os
import calendar

LIGHT_SCHEDULE_JSON = os.environ["PTM_HOME"] + '/conf/light_schedule.json'
WATERING_SCHEDULE_JSON = os.environ["PTM_HOME"] + '/conf/watering_schedule.json'
WATERING_SCHEDULE_LOG = os.environ["PTM_HOME"] + '/logs/watering_schedule.log'
light = RelayDevice(27)
pump = RelayDevice(22)


def read_schedule_conf():
    f = open(LIGHT_SCHEDULE_JSON, 'r')
    config = json.load(f)
    start = datetime.strptime(config['start'], "%H:%M")
    end = datetime.strptime(config['end'], "%H:%M")
    return start, end


def check_light_schedule():
    start, end = read_schedule_conf()
    now = datetime.now().time()
    start = now.replace(hour=start.hour, minute=start.minute, second=0, microsecond=0)
    end = now.replace(hour=end.hour, minute=end.minute, second=0, microsecond=0)
    print("[", datetime.now(), "] Lighting scheduled to start @", start, "and end @", end)
    if start < now < end:
        if not light.is_on():
            print("Turning light on!")
            light.switch(is_on=True)
        return
    if light.is_on():
        print("Turning light off!")
        light.switch(is_on=False)
    pass


def read_watering_schedule_conf():
    f = open(WATERING_SCHEDULE_JSON, 'r')
    config = json.load(f)
    enabled = config['enabled']
    days = config['water_on_weekdays']
    scheduled_start = datetime.strptime(config['water_at_time'], "%H:%M")
    water_for = config['water_for_seconds']
    f = open(WATERING_SCHEDULE_LOG, 'r')
    last_watering_date = datetime.strptime(f.read(), "%Y-%m-%d %H:%M:%S.%f")
    return enabled, days, last_watering_date, scheduled_start, water_for


def check_pump_schedule():
    enabled, watering_days, last_watering, scheduled_start, water_for = read_watering_schedule_conf()
    now = datetime.now()
    weekday = datetime.now().weekday()
    print("[", now, "] Watering scheduled, today is", now.strftime("%A"), ", last watered @", last_watering)
    if not enabled:
        print("Skipping, not enabled")
        return
    if last_watering.date() == now.date():
        print("Skipping, already watered @", scheduled_start.time())
        return
    if weekday not in watering_days:
        print("Skipping, not today! Scheduled weekdays:",
              [calendar.day_name[int(day)] for day in watering_days])
        return
    if now.time() < scheduled_start.time():
        print("Skipping, will start after", scheduled_start.time())
        return
    seconds = water_for if weekday == watering_days[-1] else (water_for / 4)
    print("Watering now for", seconds, "seconds")
    pump.switch(True)
    time.sleep(seconds)
    pump.switch(False)
    finish_time = datetime.now()
    print("Finished... Saving log @", finish_time)
    with open(WATERING_SCHEDULE_LOG, 'w') as file:
        file.write(str(finish_time))


def run_schedules():
    schedule.every(1).minutes.do(check_light_schedule).run()
    schedule.every(10).minutes.do(check_pump_schedule).run()


try:
    run_schedules()
    while True:
        schedule.run_pending()
        time.sleep(1)
except Exception as error:
    print("Error!", str(error))
    pump.switch(False)