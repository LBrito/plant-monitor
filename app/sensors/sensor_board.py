from sensors.sht40 import SHT40
from sensors.soil_sensor import SoilSensor
from sensors.tsl2591 import TSL2591
import json
import time
import os
import subprocess
import time
import smbus

class SensorBoard():
    def __init__(self):
        #self.print_available_sensors()
        self.ambient_sensor = SHT40()
        self.light_sensor = TSL2591()
        self.soil_sensors = self.soil_sensor_search()
    
    
    def print_available_sensors(self):
        p = subprocess.Popen(['i2cdetect', '-y','1'],stdout=subprocess.PIPE,) 
        for i in range(0,9):
            line = str(p.stdout.readline())
            print(line)
        pass
    
    def soil_sensor_search(self):
        bus = smbus.SMBus(1)
        sensors = []
        for device in range(0x36, 0x40):
            try:
                bus.write_byte(device, 0)
                print("Found soil sensor @ {0}".format(hex(device)))
                sensors.append(SoilSensor(device))
            except:
                pass
        return sensors
    
    def read_sensors(self):
        rTemperature, rHumidity = self.ambient_sensor.get_readings()
        lux, infrared, visible, full_spectrum = self.light_sensor.get_readings()
        readings = {
            "relativeHumidity": rHumidity,
            "relativeTemperature": rTemperature,
            "lux": lux,
            "infrared": infrared,
            "visible": visible,
            "full_spectrum": full_spectrum
        }
        for i, sensor in enumerate(self.soil_sensors):
            try:
                moisture, temperature = sensor.get_readings()
                readings["{}{}".format("soil", i)] = {
                    "soilTemperature": temperature,
                    "soilMoisture": moisture,
                }
            except Exception as e:
                print("Error reading sensor: ", e)
                pass
        
        return readings