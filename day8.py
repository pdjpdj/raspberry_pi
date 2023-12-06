import onewire, ds18x20, time
from machine import Pin
from hardware.components import red, amber, green, buzzer

SensorPin = Pin(26, Pin.IN)
sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin))

roms = sensor.scan()

def alarm(): # Our alarm function
    
    buzzer.duty_u16(10000) # Buzzer duty (volume) up

    for i in range(5): # Run this 5 times
        
        buzzer.freq(5000) # Higher pitch
        
        # LEDs ON
        red.on()
        amber.on()
        green.on()
        
        time.sleep(0.2) # wait 1 second
        
        buzzer.freq(1000) # Lower pitch
        
        # LEDs OFF
        red.off()
        amber.off()
        green.off()        
        
        time.sleep(0.2) # wait 1 second

    buzzer.duty_u16(0) # Buzzer duty (volume) off 

while True:
  sensor.convert_temp()
  time.sleep(1)

  for rom in roms:

    reading = sensor.read_temp(rom)
    print(f"{reading}C" )

    if reading < 18:
      alarm()

  time.sleep(5)