from machine import ADC, Pin, PWM
import time

potentiometer = ADC(Pin(27))

red = PWM(Pin(18))
red.freq(1000)
amber = PWM(Pin(19))
amber.freq(1000)
green = PWM(Pin(20))
green.freq(1000)

reading = 0

while True:
    reading = potentiometer.read_u16()
    print(reading)
    if reading <= 500:
        red.duty_u16(0)
        amber.duty_u16(0)
        green.duty_u16(0)
    if 500 < reading: 
        red.duty_u16(reading)
    if 20000 < reading:
        amber.duty_u16(reading -20000)  
    if 40000 < reading:
        green.duty_u16(reading - 40000)
    if reading < 40000: 
        green.duty_u16(0)
    if reading < 20000:
        amber.duty_u16(0) 
    time.sleep(0.001)
    
    