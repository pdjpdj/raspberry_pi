from machine import Pin
import time

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

counter = 1

while counter < 11:

    print(counter)
    
    
    red.value(1)
    amber.value(0)
    green.value(0)

    time.sleep(2)

    red.value(1)
    amber.value(1)
    green.value(0)

    time.sleep(1)
        
    red.value(0)
    amber.value(0)
    green.value(1)

    time.sleep(5)
    
    red.value(0)
    amber.value(1)
    green.value(0)

    time.sleep(1)
    counter += 1
    

red.value(0)
amber.value(0)
green.value(0)


