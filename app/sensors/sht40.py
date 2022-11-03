import time
import board
import adafruit_sht4x

class SHT40:
    def __init__(self):
        i2c = board.I2C()
        self.sensor = adafruit_sht4x.SHT4x(i2c)
        self.sensor.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION
        
    def get_readings(self):
        return self.sensor.temperature, self.sensor.relative_humidity