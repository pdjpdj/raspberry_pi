import time
from hardware.components import lightsensor, red, amber, green, buzzer

while True:
  light = round(lightsensor.read_u16()/65535*100, 0)

  print(f"{light}%" )
  buzzer.duty_u16(1000)
  buzzer.freq(int(light * 20))

  if light <= 30:
    red.on()
    amber.off()
    green.off()
  elif 30 < light < 60:
    red.off()
    amber.on()
    green.off()
  elif light >= 60:
    red.off()
    amber.off()
    green.on()

  time.sleep(1)
  buzzer.duty_u16(0)
  time.sleep(1)
  
