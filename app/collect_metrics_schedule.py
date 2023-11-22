import time
import schedule
import random
import json
from sensors.sensor_board import SensorBoard
from iot.paho_mqtt import MQTT

board = SensorBoard()

def readSensors():
    readings = board.read_sensors()
    return readings

def sendMessage(message):
    print("Sending message @", message['timestamp'])
    MQTT().publishMessage(message)
    pass

def writeToFile(readings):
    readingsJson = json.dumps(readings, indent=4)
    #print(readingsJson + "\n")
    with open('/home/pi/.ptm/app/data/readings.json', 'w') as f:
        f.write(readingsJson)
    pass
    
def main():
    readings = readSensors()
    writeToFile(readings)
    #sendMessage(readings)
    pass

schedule.every(60).seconds.do(main).run()

while True:
    schedule.run_pending()
    time.sleep(10)
