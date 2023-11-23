import RPi.GPIO as GPIO


class RelayDevice:
    def __init__(self, pin):
        self.RELAY_GPIO_PIN = pin  # GPIO pin
        GPIO.setmode(GPIO.BCM)  # GPIO Numbers instead of board number
        GPIO.setup(self.RELAY_GPIO_PIN, GPIO.OUT)  # GPIO Assign mode

    def switch(self, is_on):
        GPIO.output(self.RELAY_GPIO_PIN, GPIO.HIGH if is_on else GPIO.LOW)  # out
        pass

    def is_on(self):
        return GPIO.input(self.RELAY_GPIO_PIN) > 0

    @staticmethod
    def reset():
        GPIO.cleanup()
