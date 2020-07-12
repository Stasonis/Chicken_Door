from DoorControl import DoorControl
import json

configFile = open("config.json")
config = json.load(configFile)

doorControl = DoorControl(config)
doorControl.close()
