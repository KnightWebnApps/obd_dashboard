import obd
import json
import time
import sys

# creates a continuous stream of data
connection = obd.Async()

def new_spd(s):
  string = str(s.value.to('mph'))
  data = {
    "speed" : string
  }
  print(json.dumps(data))
  sys.stdout.flush()

def new_rpm(r):
  string = str(r.value)
  data = {
    "rpm": string
  }
  print(json.dumps(data))
  sys.stdout.flush()


# commands to watch
connection.watch(obd.commands.SPEED, callback=new_spd)
connection.watch(obd.commands.RPM, callback=new_rpm)
# connection.watch(obd.commands.FUEL_PRESSURE)

# start the connection
connection.start()

time.sleep(60)
connection.stop()

