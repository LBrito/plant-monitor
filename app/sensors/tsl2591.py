import board
import adafruit_tsl2591
from time import sleep

class TSL2591:
    def get_readings(self): 
        i2c = board.I2C()
        sensor = adafruit_tsl2591.TSL2591(i2c)
        #sensor.gain = adafruit_tsl2591.GAIN_HIGH
        sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_200MS
        lux = sensor.lux
        infrared = sensor.infrared
        visible = sensor.visible
        full_spectrum = sensor.full_spectrum
        
        sleep(0.25)
        
        return lux, infrared, visible, full_spectrum
