# -----------------------------------------------------------------------------
# Lesson 05: The Power of Inputs (Buttons & Touch)
# Modules: KY-004 Button / KY-036 Metal Touch
# Goal: Read a signal from a physical button or touch sensor.
#       When you press the button, the Pico should react (turn on an LED).
#
# WIRING:
# 1. Push Button Module:
#    - S (Signal) -> GP16
#    - - (GND)    -> GND
#    - + (Power)  -> 3.3V (Some small buttons don't need this)
#
# 2. Touch Sensor Module:
#    - S (Signal) -> GP17
#    - - (GND)    -> GND
#    - + (Power)  -> 3.3V
#
# Skills Learnt:
# - Digital Inputs (Pull-Down Resistors)
# - Boolean Logic (OR Gates)
# - Signal Debouncing
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# We use PULL_DOWN to make sure the pin reads "0" when the button is NOT pressed.
# If we didn't do this, the wire might act like an antenna and pick up random static!
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
touch_sensor = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Onboard LED to show status
led = machine.Pin("LED", machine.Pin.OUT) # Use "LED" for Pico W/2W, or 25 for older Pico

print("Ready! Press the Button or Touch the Sensor.")

while True:
    # Read the inputs (returns 1 or 0)
    btn_state = button.value()
    touch_state = touch_sensor.value()
    
    # Logic: OR gate
    # If EITHER the Button IS pressed OR the Sensor IS touched...
    if btn_state == 1 or touch_state == 1:
        print("Detected!")
        led.value(1) # Turn LED ON
    else:
        led.value(0) # Turn LED OFF
        
    time.sleep(0.05) # Small delay to debounce
