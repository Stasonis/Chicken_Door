from DoorSensor import DoorSensor
from MotorControl import MotorControl
import time

class Door:
    topSensor = None
    bottomSensor = None

    motorControl = None

    maximumTime = 10

    def __init__(self, config):
        self.maximumTime = config["doorMaxRuntime"]

        self.topSensor = DoorSensor(config["doorSensors"]["top"])
        self.bottomSensor = DoorSensor(config["doorSensors"]["bottom"])

        self.motorControl = MotorControl(config)

    def isOpen(self):
        return self.topSensor.isOn()

    def isClosed(self):
        return self.bottomSensor.isOn()

    def close(self):
        if not self.isOpen():
            print("Door is not open")
            return -1

        runningTime = 0;

        self.motorControl.down()

        while not self.isClosed():
            runningTime = runningTime + 1;
            if(runningTime > self.maximumTime):
                print("Timeout closing door")
                self.motorControl.stop()
                return -1
            print("Close Cycle")
            time.sleep(1)

        self.motorControl.stop()
        print("Door closed")
        return 1

    def open(self):
        if not self.isClosed():
            print("Door is not closed")
            return -1

        runningTime = 0;

        self.motorControl.up()

        while not self.isOpen():
            runningTime = runningTime + 1;
            if(runningTime > self.maximumTime):
                print("Timeout opening door")
                self.motorControl.stop()
                return -1
            print("Open Cycle")
            time.sleep(1)

        self.motorControl.stop()
        print("Door opened")
        return 1
