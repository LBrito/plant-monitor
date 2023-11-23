import json
import os
import time

import schedule

from iot.paho_mqtt import MQTT
from sensors.sensor_board import SensorBoard

READINGS_JSON_FILE = os.environ["PTM_HOME"] + '/data/readings.json'
CONFIG_JSON_FILE = os.environ["PTM_HOME"] + '/conf/metrics_schedule.json'
board = SensorBoard()


def read_config():
    f = open(CONFIG_JSON_FILE, 'r')
    config = json.load(f)
    return config['mqtt_enabled'], config['debug']


def read_sensors():
    readings = board.read_sensors()
    return readings


def send_message(message):
    print("Sending message @", message['timestamp'])
    MQTT().publishMessage(message)
    pass


def write_to_file(readings, debug):
    readings_json = json.dumps(readings, indent=4)
    if debug:
        print(readings_json)
    with open(READINGS_JSON_FILE, 'w') as f:
        f.write(readings_json)
    pass


def main():
    mqtt_enabled, debug = read_config()
    readings = read_sensors()
    write_to_file(readings, debug)
    if mqtt_enabled:
        send_message(readings)
    pass


schedule.every(60).seconds.do(main).run()

while True:
    schedule.run_pending()
    time.sleep(10)
