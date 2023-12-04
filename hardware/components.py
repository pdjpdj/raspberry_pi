from machine import Pin, PWM, ADC

pir = Pin(26, Pin.IN, Pin.PULL_DOWN)

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

buzzer = PWM(Pin(13))

lightsensor = ADC(Pin(26))
potentiometer = ADC (Pin(27))

button1 = Pin(12, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)