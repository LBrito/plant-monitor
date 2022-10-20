# Soil sensor
import time
import board
from adafruit_seesaw.seesaw import Seesaw

class SoilSensor:
    def __init__(self):
        self.get_readings()

    @classmethod
    def get_readings(self):
        bus = board.I2C()
        ss = Seesaw(bus, addr=0x36)
    
        return ss.moisture_read(), ss.get_temp()