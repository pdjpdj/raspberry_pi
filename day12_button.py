import time
from machine import Pin
from neopixel import NeoPixel

button = Pin(15, Pin.IN, Pin.PULL_DOWN)
strip = NeoPixel(Pin(28), 15)

red = 255,0,0
green = 0,255,0
blue = 0,0,255

colours = [red, green, blue]

myIndex = 0

indexLength = len(colours) - 1

while True:
  time.sleep(0.4)

  if button() == 1:
    if myIndex < indexLength:
      myIndex += 1
    else:
      myIndex = 0

    strip.fill((colours[myIndex]))

    strip.write()