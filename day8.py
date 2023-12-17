import onewire, ds18x20, time
from machine import Pin
from alarm import alarm

SensorPin = Pin(26, Pin.IN)
sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin))

roms = sensor.scan()

while True:
  sensor.convert_temp()
  time.sleep(1)

  for rom in roms:

    reading = sensor.read_temp(rom)
    print(f"{reading}C" )

    if reading < 18:
      alarm()

  time.sleep(5)