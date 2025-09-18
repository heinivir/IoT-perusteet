from machine import Pin
import time

led = Pin(25, Pin.OUT)  # GPIO 25
while True:
    led.value(1)  # LED on
    time.sleep(0.5)
    led.value(0)  # LED off
    time.sleep(0.5)
