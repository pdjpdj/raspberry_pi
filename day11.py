from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

time.sleep(1)

display = SSD1306_I2C(128, 32, i2c)

counter = 0
while True:

  display.fill(0)

  display.text("The Endless", 0, 0)
  display.text("Counter!", 0, 12)
  display.text(str(counter), 0, 24)
  
  display.show()

  time.sleep(0.1)
  counter +=  1