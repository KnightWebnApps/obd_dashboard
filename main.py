import obd
import json
import time
import sys

# creates a continuous stream of data
connection = obd.Async()

def new_spd(s):
  string = str(s.value.to('mph'))
  data = {"speed" : string}
  print(json.dumps(data))
  sys.stdout.flush()

def new_rpm(r):
  string = str(r.value)
  data = {"rpm" : string}
  print(json.dumps(data))
  sys.stdout.flush()

def new_maf(r):
  string = str(r.value)
  data = {"maf" : string}
  print(json.dumps(data))
  sys.stdout.flush()

def new_fuel(r):
  string = str(r.value)
  data = {"fuel" : string}
  print(json.dumps(data))
  sys.stdout.flush()

def new_temp(r):
  string = str(r.value)
  data = {"temp" : string}
  print(json.dumps(data))
  sys.stdout.flush()

# commands to watch
connection.watch(obd.commands.SPEED, callback=new_spd)
connection.watch(obd.commands.RPM, callback=new_rpm)
connection.watch(obd.commands.MAF, callback=new_maf)
connection.watch(obd.commands.FUEL_LEVEL, callback=new_fuel)
connection.watch(obd.commands.COOLANT_TEMP, callback=new_temp)

# start the connection
connection.start()

while True:
  

connection.stop()