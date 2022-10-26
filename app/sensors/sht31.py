import board
import busio
import adafruit_sht31d
import time

class SHT31:
    
    def get_readings(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        sensor = adafruit_sht31d.SHT31D(i2c)

        return sensor.temperature, sensor.relative_humidity