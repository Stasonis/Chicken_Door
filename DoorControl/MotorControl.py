import RPi.GPIO as GPIO

class MotorControl:
    motorUpPin = None
    motorDownPin = None

    def __init__(self, config):
        self.motorUpPin = config["motor"]["up"]
        self.motorDownPin = config["motor"]["down"]
        GPIO.setup(self.motorUpPin, GPIO.OUT)
        GPIO.setup(self.motorDownPin, GPIO.OUT)

    def status(self):
        return {"upPin": self.motorUpPin,
                "downPin": self.motorDownPin}

    def up(self):
        GPIO.output(self.motorDownPin, False)
        GPIO.output(self.motorUpPin, True)

    def down(self):
        GPIO.output(self.motorUpPin, False)
        GPIO.output(self.motorDownPin, True)

    def stop(self):
        GPIO.output(self.motorUpPin, False)
        GPIO.output(self.motorDownPin, False)
