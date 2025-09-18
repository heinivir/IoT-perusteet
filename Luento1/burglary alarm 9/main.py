from machine import Pin
from time import sleep

pir = Pin(14, Pin.IN)

led = Pin(15, Pin.OUT)

print("Burglary alarm activated!")

while True:
    if pir.value() == 1:  
        print("Movement detected! Alert!")
        led.value(1)       
        sleep(0.5)
        led.value(0)      
        sleep(0.5)
    else:
        led.value(0)      
        sleep(0.1)
