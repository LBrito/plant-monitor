from sht31 import SHT31
from soil_sensor import SoilSensor
from tsl2591 import TSL2591

class SensorBoard():
    def __init__(self):
        self.read_sensors()

    @classmethod
    def read_sensors(self):
        rTemperature, rHumidity = SHT31().get_readings()
        ssMoisture, ssTemperature = SoilSensor().get_readings()
        lux, infrared, visible, full_spectrum = TSL2591().get_readings()
        
        readings = {
            "relativeHumidity": rHumidity,
            "relativeTemperature": rTemperature,
            "soilTemperature": ssTemperature,
            "soilMoisture": ssMoisture,
            "lux": lux,
            "infrared": infrared,
            "visible": visible,
            "full_spectrum": full_spectrum
        }
        return readings
    
