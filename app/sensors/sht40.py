import time
import board
import adafruit_sht4x

class SHT40:
    def get_readings(self):
        i2c = board.I2C()
        sht = adafruit_sht4x.SHT4x(i2c)
        sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION
        
        return sht.temperature, sht.relative_humidity