import machine
import utime
import urandom

# Set up LED and button
led = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Global variables
timer_start = 0

# Interrupt handler
def button_handler(pin):
    button.irq(handler=None)  # turn off the trigger, so it is used only once
    reaction_time = utime.ticks_diff(utime.ticks_ms(), timer_start)
    print("Your reaction time was " + str(reaction_time) + " milliseconds")
    print("Program complete.")

# Signal user to get ready
led.value(1)
utime.sleep(urandom.uniform(5, 10))  # random amount of seconds between 5 and 10

# Turn off LED – signal to press the button
led.value(0)
timer_start = utime.ticks_ms()  # starts counting milliseconds after the LED turns off

# Enable interrupt
button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
