from sensors.sht40 import SHT40
from sensors.soil_sensor import SoilSensor
from sensors.tsl2591 import TSL2591
import json
import time

class SensorBoard():
    
    def read_sensors(self):
        rTemperature, rHumidity = SHT40().get_readings()
        ssMoisture1, ssTemperature1 = SoilSensor(0x36).get_readings()
        ssMoisture2, ssTemperature2 = SoilSensor(0x37).get_readings()
        ssMoisture3, ssTemperature3 = SoilSensor(0x38).get_readings()
        lux, infrared, visible, full_spectrum = TSL2591().get_readings()
        
        readings = {
            "relativeHumidity": rHumidity,
            "relativeTemperature": rTemperature,
            "soil1" : {
                "soilTemperature": ssTemperature1,
                "soilMoisture": ssMoisture1,
            },
            "soil2" : {
                "soilTemperature": ssTemperature2,
                "soilMoisture": ssMoisture2,
            },
            "soil3" : {
                "soilTemperature": ssTemperature3,
                "soilMoisture": ssMoisture3,
            },
            "lux": lux,
            "infrared": infrared,
            "visible": visible,
            "full_spectrum": full_spectrum
        }
        return readings
