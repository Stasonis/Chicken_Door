#!/usr/bin/python

from DoorControl import DoorControl
import json

# Print necessary headers.
print("Content-Type: text/html\r\n")
print("\r\n")

configFile = open("config.json")
config = json.load(configFile)

doorControl = DoorControl(config)
doorControl.close()
