from hardware.components import potentiometer, buzzer
import time

reading = 0

while True:
  time.sleep_ms(10)

  reading = potentiometer.read_u16()

  freq = int(reading/32)

  if(10 < freq ):
    buzzer.freq(freq)
    buzzer.duty_u16(2500)
  else:
    buzzer.duty_u16(0)
