import time
from machine import Pin
from neopixel import NeoPixel

strip = NeoPixel(Pin(28), 15)

delay =  0.0001
while True:
    for i in range(1,255,1):
      for pos in range(15):
        strip[pos] = ((i,0,0))
      
        strip.write()
        time.sleep(delay)
    for i in range(255,1,-1):
      for pos in range(15):
        strip[pos] = ((i,0,0))
      
        strip.write()
        time.sleep(delay)
    for i in range(1,255,1):
      for pos in range(15):
        strip[pos] = ((0,i,0))
      
        strip.write()
        time.sleep(delay)
    for i in range(255,1,-1):
      for pos in range(15):
        strip[pos] = ((0,i,0))
      
        strip.write()
        time.sleep(delay)
    for i in range(1,255,1):
      for pos in range(15):
        strip[pos] = ((0,0,i))
      
        strip.write()
        time.sleep(delay)
    for i in range(255,1,-1):
      for pos in range(15):
        strip[pos] = ((0,0,i))
      
        strip.write()
        time.sleep(delay)