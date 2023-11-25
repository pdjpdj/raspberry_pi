from machine import Pin
import time

button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

while True:
    time.sleep(0.2)

    if button1.value() == 1 and button2.value() == 1 and button3.value() == 1:
        print("All Buttons pressed")
        green.value(0)
        amber.value(0)
        red.value(0)
        
    elif button1.value() == 1 and button2.value() == 1:
        print("Button 1 and 2 pressed")
        green.toggle()
        red.value(0)
        
    elif button1.value() == 1 or button3.value() == 1:
        print("Button 1 or 3 pressed")
        amber.toggle()
        red.value(0)

    else:
        print("no buttons pressed")
        red.value(1)
    