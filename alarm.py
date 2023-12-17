from hardware.components import red, amber, green, buzzer
import time

def alarm(): # Our alarm function
    
    buzzer.duty_u16(10000) # Buzzer duty (volume) up

    for i in range(5): # Run this 5 times
        
        buzzer.freq(5000) # Higher pitch
        
        # LEDs ON
        red.on()
        amber.on()
        green.on()
        
        time.sleep(0.2) # wait 1 second
        
        buzzer.freq(1000) # Lower pitch
        
        # LEDs OFF
        red.off()
        amber.off()
        green.off()        
        
        time.sleep(0.2) # wait 1 second

    buzzer.duty_u16(0) # Buzzer duty (volume) off 
