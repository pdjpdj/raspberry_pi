from machine import Pin
import time
onboardLED = Pin(25, Pin.OUT)
inter = 1
while True:
  onboardLED.value(1)
  time.sleep(inter)
  onboardLED.value(0)
  time.sleep(inter)

