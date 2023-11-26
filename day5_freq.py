from machine import Pin, PWM, ADC
import time

potentiometer = ADC (Pin(27))
buzzer = PWM(Pin(13))

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
