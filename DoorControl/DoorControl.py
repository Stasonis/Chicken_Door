from Chicken_Door.DoorControl.Door import Door
import RPi.GPIO as GPIO
from twilio.rest import Client
import time

class DoorControl:
    door = None
    twilioSid = None
    twilioAuthToken = None
    twilioFromNumber = None
    twilioToNumber = None

    def __init__(self, config):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        self.twilioSid = config["twilio"]["sid"]
        self.twilioAuthToken = config["twilio"]["authToken"]
        self.twilioFromNumber = config["twilio"]["fromNumber"]
        self.twilioToNumber = config["twilio"]["toNumber"]

        self.door = Door(config)

    def shutdown(self):
        GPIO.cleanup()

    def status(self):
        return {"door": self.door.status()}

    def open(self):
        if self.door.open() == 1:
            self.statusNotification("Door Opened Successfully")
            return True
        else:
            self.statusNotification("Door Failed to Open")
            return False

    def close(self):
        if self.door.close() == 1:
            self.statusNotification("Door Closed Successfully")
            return True
        else:
            self.statusNotification("Door Failed to Close")
            return False

    def up(self, duration):
        return self.door.up(duration)

    def down(self, duration):
        return self.door.down(duration)

    def statusNotification(self, message):
        print("Sending message via Twilio - " + message)
        client = Client(self.twilioSid, self.twilioAuthToken)

        message = client.messages \
                        .create(
                             body=message,
                             from_=self.twilioFromNumber,
                             to=self.twilioToNumber
                         )

        print("Sent message via twilio - " + message.sid)
