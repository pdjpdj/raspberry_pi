import time
from machine import Pin, ADC
from neopixel import NeoPixel

strip = NeoPixel(Pin(28), 15)
potentiometer = ADC(Pin(26))
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

red = 255,0,0
green = 0,255,0
blue = 0,0,255

colours = [red, green, blue]

myIndex = 0

indexLength = len(colours)
rcol = 0
gcol = 0
bcol = 0

while True:
  # select the colour
  if button() == 1:
    if myIndex < indexLength:
      myIndex += 1
    else:
      myIndex = 0
  
  if myIndex != 3:
    # show which colour currently editing
    strip[0] = ((colours[myIndex]))
    strip[1] = ((colours[myIndex]))
    strip[2] = ((colours[myIndex]))

    # adjust that colour

    reading = potentiometer.read_u16()
    if myIndex == 0:
      # set red intensity
      rcol = int((reading / 65535) * 255)
      strip[3] = ((rcol, 0, 0))
      strip[4] = ((rcol, 0, 0))
      strip[5] = ((rcol, 0, 0))
    elif myIndex == 1:
      # set green intensity
      gcol = int((reading / 65535) * 255)
      strip[6] = ((0, gcol, 0))
      strip[7] = ((0, gcol, 0))
      strip[8] = ((0, gcol, 0))
    elif myIndex == 2:
      # set blue intensity
      bcol = int((reading / 65535) * 255)
      strip[9] = ((0, 0, bcol))
      strip[10] = ((0, 0, bcol))
      strip[11] = ((0, 0, bcol))
    
    # final colour
    strip[12] = ((rcol, gcol, bcol))
    strip[13] = ((rcol, gcol, bcol))
    strip[14] = ((rcol, gcol, bcol))
  else:
    # on last button press fill whole strip with the chosen colour
    strip.fill((rcol, gcol, bcol))

  print(f"index:{myIndex}, colour({rcol},{gcol},{bcol})")
  
  strip.write()
  time.sleep(0.5)