import board
import adafruit_tsl2591
from time import sleep

class TSL2591:
    def __init__(self):
        i2c = board.I2C()
        self.sensor = adafruit_tsl2591.TSL2591(i2c)
        print("Found TSL2591 @ 0x29")
        self.sensor.gain = adafruit_tsl2591.GAIN_LOW
        self.sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_500MS
    
    def get_readings(self):
        sensor = self.sensor
        lux = sensor.lux
        infrared = sensor.infrared
        visible = sensor.visible
        full_spectrum = sensor.full_spectrum
        
        return lux, infrared, visible, full_spectrum
    
    def enable(self):
        self.sensor.enable()
        pass
    
    def disable(self):
        self.sensor.disable()
        pass
    
