from machine import ADC, Pin, PWM
import time

buzzer = PWM(Pin(13))
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)
potentiometer = ADC (Pin(27))

#Notes:
A = 440
As = 466
B = 494
C = 523
Cs = 554
D = 587
Ds = 622
E = 659
F = 740
G = 784
Gs = 830


volume = 2500

def playNote(note, delay1, delay2):
  if(note == E or note == D):
    red.on()
  if(note == G or note == D):
    amber.on()
  if(note == C or note == D):
    green.on()
  buzzer.duty_u16(potentiometer.read_u16())
  buzzer.freq(note)
  time.sleep(delay1)
  buzzer.duty_u16(0)
  red.off()
  amber.off()
  green.off()
  time.sleep(delay2)

playNote(E, 0.1, 0.2)
playNote(E, 0.1, 0.2)
playNote(E, 0.1, 0.5)
playNote(E, 0.1, 0.2)
playNote(E, 0.1, 0.2)
playNote(E, 0.1, 0.5)
playNote(E, 0.1, 0.2)
playNote(G, 0.1, 0.2)
playNote(C, 0.1, 0.2)
playNote(D, 0.1, 0.2)
playNote(E, 0.1, 0.2)

buzzer.duty_u16(0)