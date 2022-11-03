# Soil sensor
import time
import board
from adafruit_seesaw.seesaw import Seesaw

class SoilSensor:
    def __init__(self, address):
        bus = board.I2C()
        self.sensor = Seesaw(bus, addr=address)

    def get_readings(self):
        return self.sensor.moisture_read(), self.sensor.get_temp()