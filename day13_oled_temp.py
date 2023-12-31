import onewire, ds18x20, time
from machine import Pin, I2C
from hardware.ssd1306 import SSD1306_I2C

SensorPin = Pin(26, Pin.IN)
sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin))
i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

time.sleep(1)

display = SSD1306_I2C(128, 32, i2c)
roms = sensor.scan()

while True:
  sensor.convert_temp()
  display.fill(0)
  time.sleep(1)

  for rom in roms:

    reading = sensor.read_temp(rom)
    display.text("Temperature:", 0, 0)
    display.text(f"{reading}C", 0, 24)
  
  display.show()

  time.sleep(5)