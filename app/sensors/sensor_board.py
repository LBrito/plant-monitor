from sensors.sht40 import SHT40
from sensors.soil_sensor import SoilSensor
from sensors.tsl2591 import TSL2591
import json
import time
import os
import subprocess
import time
import smbus
from datetime import datetime

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
                sensors.append(SoilSensor(device))
            except:
                pass
        return sensors
    
    def read_sensors(self):
        timestamp = datetime.utcnow().isoformat() + 'Z'
        readings = {
            "timestamp": timestamp
        }
        
        readings = self.setTemperatureHumidityReadings(readings)
        readings = self.setLightReadings(readings)
        
        return self.setSoilSensorReadings(readings)
    
    def setTemperatureHumidityReadings(self, readings):
        try:
            rTemperature, rHumidity = self.ambient_sensor.get_readings()
            readings["relativeHumidity"]	= rHumidity
            readings["relativeTemperature"]	= rTemperature
        except Exception as e:
            print("Error reading temperature/humidity: ", e)
            readings["relativeHumidity"] = {"error": str(e)}
            pass
        
        return readings
    
    def setLightReadings(self, readings):
        try:
            lux, infrared, visible, full_spectrum = self.light_sensor.get_readings()           
            readings["lux"]				= lux
            readings["infrared"]		= infrared
            readings["visible"]			= visible
            readings["full_spectrum"]	= full_spectrum
        except Exception as e:
            print("Error reading light measurements: ", e)
            readings["lux"] = {"error": str(e)}
            pass
        
        return readings
    
    def setSoilSensorReadings(self, readings):
        for i, sensor in enumerate(self.soil_sensors):
            sensorKey = "{}{}".format("soil", i)
            try:
                moisture, temperature = sensor.get_readings()
                readings[sensorKey] = {
                    "soilTemperature": temperature,
                    "soilMoisture": moisture,
                }
            except Exception as e:
                print("Error reading soil sensor: ", e)
                readings[sensorKey] = {"error": str(e)}
                pass
        
        return readings
