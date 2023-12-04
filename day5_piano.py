from hardware.components import potentiometer, red, amber, green, buzzer, button3, button2, button1

#Notes:
A = 440
B = 494
C = 523
D = 587
E = 659
F = 740
G = 784

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
