from hardware.components import red, amber, green
import time

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
