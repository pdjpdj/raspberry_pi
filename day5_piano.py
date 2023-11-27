from machine import ADC, Pin, PWM

button1 = Pin(12, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)
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

def playNote(note):
  buzzer.duty_u16(potentiometer.read_u16())
  buzzer.freq(note)

while True:
    if(button1.value() == 1 and button2.value() == 1 and button3.value() == 1):
      red.on()
      amber.on()
      green.on()
      playNote(A)
    elif(button1.value() == 1 and button2.value() == 1):
      red.on()
      amber.on()
      playNote(B)
    elif(button1.value() == 1 and button3.value() == 1):
      red.on()
      green.on()
      playNote(C)
    elif(button2.value() == 1 and button3.value() == 1):
      amber.on()
      green.on()
      playNote(D)
    elif(button1.value() == 1):
      red.on()
      playNote(E)
    elif(button2.value() == 1):
      amber.on()
      playNote(F)
    elif(button3.value() == 1):
      green.on()
      playNote(G)
    else :
      red.off()
      amber.off()
      green.off()
      buzzer.duty_u16(0)
