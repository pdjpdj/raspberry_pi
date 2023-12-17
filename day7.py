import time
from alarm import alarm
from hardware.components import pir

print("Warming up...")

time.sleep(10)

print("Sensor ready!")


while True:
  time.sleep(0.01)
  print(pir.value())
  if pir.value() == 1:
    print("I SEE YOU!")

    alarm()

    print("Sensor active")