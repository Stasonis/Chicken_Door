import RPi.GPIO as GPIO
import time
import signal
import sys

class Door:

	topSensor = 0
	bottomSensor = 0

	maxDoorTime = 45


	def __init__(self, maxDoorTime):
		self.topSensor = GPIO.input(33)
		self.bottomSensor = GPIO.input(31)		

		self.maxDoorTime(maxDoorTime)

	def isOpen():
		return self.topSensor == 0

	def openDoor():
		timeStart=time.process_time()
		runTime=0

		while self.topSensor == 1 and runTime < self.maxDoorTime:
                GPIO.output(35,True)
                GPIO.output(37,False)
                runTime = time.process_time() - timeStart
        if self.maxDoorTime <= runTime:
                return False
        if self.topSensor==0:
                print('Door is open!')
                return True

	def closeDoor():

