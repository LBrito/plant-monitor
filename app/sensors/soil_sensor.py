# Soil sensor
import time
import board
from adafruit_seesaw.seesaw import Seesaw

class SoilSensor:
    def __init__(self, address):
        self.address = address

    def get_readings(self):
        bus = board.I2C()
        ss = Seesaw(bus, addr=self.address)
    
        return ss.moisture_read(), ss.get_temp()