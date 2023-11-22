# Soil sensor
import time
import board
from adafruit_seesaw.seesaw import Seesaw

class SoilSensor:
    def __init__(self, address):
        bus = board.I2C()
        self.address = address
        self.sensor = Seesaw(bus, addr=address, reset=True)
        print("Found soil sensor @0x{:02x} with version {}".format(address, self.sensor.get_options()))

    def get_readings(self):
        return self.sensor.moisture_read(), self.sensor.get_temp()

        