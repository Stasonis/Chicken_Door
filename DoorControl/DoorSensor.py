import RPi.GPIO as GPIO

class DoorSensor:
    gpioPin = 0

    callback = None

    def __init__(self, gpioPin):
        print("Initing Door Sensor - Pin " + str(gpioPin))
        GPIO.setup(gpioPin ,GPIO.IN)
        GPIO.add_event_detect(gpioPin, GPIO.BOTH, callback=self.onChange)

        self.gpioPin = gpioPin

    def status(self):
        return {"active": self.isOn(),
                "gpioPin": self.gpioPin}

    def isOn(self):
        if GPIO.input(self.gpioPin):
            return False
        else:
            return True

    def setCallback(self, callback):
        self.callback = callback

    def onChange(self, channel):
        if self.callback is not None:
            self.callback()
