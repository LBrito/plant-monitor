import time
import schedule
import random
import json
from sensors.sensor_board import SensorBoard
from iot.paho_mqtt import MQTT
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


schedule.every(1).minute.do(main).run()

while True:
    schedule.run_pending()
    time.sleep(30)
