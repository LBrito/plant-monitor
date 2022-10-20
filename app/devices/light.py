import RPi.GPIO as GPIO
import time

class PlantSpectrum:
    def __init__(self):
        self.RELAIS_1_GPIO = 17 # GPIO pin 11
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board number
        GPIO.setup(self.RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode

    def switch(self, isOn):
        GPIO.output(self.RELAIS_1_GPIO, GPIO.HIGH if isOn else GPIO.LOW) # out
        
    def isOn(self):    
        return GPIO.input(self.RELAIS_1_GPIO) > 0
