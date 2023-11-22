import RPi.GPIO as GPIO
import time

class WaterPump:
    def __init__(self):
        self.RELAIS_1_GPIO = 22 # GPIO pin 11
        GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board number
        GPIO.setup(self.RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode

    def switch(self, isOn):
        GPIO.output(self.RELAIS_1_GPIO, GPIO.HIGH if isOn else GPIO.LOW) # out
        pass
        
    def isOn(self):    
        return GPIO.input(self.RELAIS_1_GPIO) > 0
    
    def reset(self):
        GPIO.cleanup()

pump = WaterPump()
pump.switch(isOn=False)
time.sleep(60)
print("done")
pump.reset()