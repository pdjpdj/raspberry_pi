from machine import Pin
from alarm import alarm
import time

tilt = Pin(26, Pin.IN, Pin.PULL_DOWN)
tiltcount = 0
tiltstate = 0

while True:
  time.sleep(0.01)
  if tiltstate == 0 and tilt.value() == 1:
    tiltcount = tiltcount + 1
    tiltstate = 1
    print(f"{tiltcount} tilts" )
    alarm()
  if tiltstate == 1 and tilt.value() == 0:
    tiltstate = 0
    print("reset")
  