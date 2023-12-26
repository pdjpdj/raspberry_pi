from machine import Pin, I2C, ADC
from hardware.ssd1306 import SSD1306_I2C
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

time.sleep(1)

display = SSD1306_I2C(128, 32, i2c)

lightsensor = ADC(Pin(26))

while True:
  time.sleep(0.5)

  light = round(lightsensor.read_u16()/65535*100, 0)
  display.fill(0)

  display.text("Light level:", 0, 0)
  count = 0
  while count < light :
    display.text("|", count, 12)
    count += 1
  display.text("|", 100, 12)

  display.show()
