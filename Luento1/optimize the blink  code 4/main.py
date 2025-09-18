from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)

print("Ready to go!")

for i in range(10):
    led.toggle()
    print(f"Loop number {i}")
    sleep(0.5)

led.off()               
print("Loop finished")