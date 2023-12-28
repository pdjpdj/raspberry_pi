import time
from machine import Pin, ADC
from neopixel import NeoPixel

strip = NeoPixel(Pin(28), 15)
potentiometer = ADC(Pin(26))

col = 0
while True:
  pos = 0
  while pos < 15:
    strip[pos] = (255,8*col,16*pos)
    pos += 1
    col += 2

  mydelay = potentiometer.read_u16()/50000
  strip.write()
  time.sleep(mydelay)