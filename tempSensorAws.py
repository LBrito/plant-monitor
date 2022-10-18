import time
import schedule
import random
import json
from sensor_board import SensorBoard
from paho_mqtt import MQTT
from datetime import datetime

def readSensors():
    readings = SensorBoard().read_sensors()
    print("Sending message: ", json.dumps(readings, indent=4))
    
    return readings

def sendMessage(message):
    message['timestamp'] = datetime.utcnow().isoformat() + 'Z'
    MQTT().publishMessage(message)
    pass
    
def main():
    readings = readSensors()
    sendMessage(readings)
    pass


schedule.every(10).seconds.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
