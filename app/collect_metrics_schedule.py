import time
import schedule
import random
import json
from sensors.sensor_board import SensorBoard
from iot.paho_mqtt import MQTT
from datetime import datetime

board = SensorBoard()

def readSensors():
    readings = board.read_sensors()
    return readings

def sendMessage(message):
    message['timestamp'] = datetime.utcnow().isoformat() + 'Z'
    print("Sending message @", message['timestamp'])
    MQTT().publishMessage(message)
    pass
    
def main():
    readings = readSensors()
    sendMessage(readings)
    pass

schedule.every(30).seconds.do(main).run()

while True:
    schedule.run_pending()
    time.sleep(10)
