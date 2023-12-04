from machine import Pin, PWM
import time

pir = Pin(26, Pin.IN, Pin.PULL_DOWN)
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)
buzzer = PWM(Pin(13))

buzzer.duty_u16(0)
print("Warming up...")

time.sleep(10)

print("Sensor ready!")

def alarm():

  buzzer.duty_u16(1000)
  for i in range(5):
    buzzer.freq(5000)

    red.on()
    amber.on()
    green.on()
    time.sleep(1)

    buzzer.freq(500)

    red.off()
    amber.off()
    green.off()
    time.sleep(1)

  buzzer.duty_u16(0)

while True:
  time.sleep(0.01)
  print(pir.value())
  if pir.value() == 1:
    print("I SEE YOU!")

    alarm()

    print("Sensor active")