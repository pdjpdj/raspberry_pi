from machine import Pin, PWM
import time

buzzer = PWM(Pin(13))
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

def playNote(note, vol, delay1, delay2):
  buzzer.duty_u16(vol)
  buzzer.freq(note)
  time.sleep(delay1)
  buzzer.duty_u16(0)
  time.sleep(delay2)

playNote(E, volume, 0.1, 0.2)
playNote(E, volume, 0.1, 0.2)
playNote(E, volume, 0.1, 0.5)
playNote(E, volume, 0.1, 0.2)
playNote(E, volume, 0.1, 0.2)
playNote(E, volume, 0.1, 0.5)
playNote(E, volume, 0.1, 0.2)
playNote(G, volume, 0.1, 0.2)
playNote(C, volume, 0.1, 0.2)
playNote(D, volume, 0.1, 0.2)
playNote(E, volume, 0.1, 0.2)

buzzer.duty_u16(0)