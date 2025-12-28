# -----------------------------------------------------------------------------
# Lesson 09: Magnetic Fields (Hall Effect)
# -----------------------------------------------------------------------------
# Module: KY-003 Hall Magnetic Sensor Module
# Goal: Detect if a magnet is nearby without any physical contact.
#
# WHY THIS MATTERS:
# This is how your laptop knows when you close the lid (there's a magnet in 
# the screen and a Hall sensor in the keyboard). It's also used in anti-lock 
# brakes (ABS) to count how fast wheels are spinning!
#
# HOW IT WORKS:
# The "Hall Effect" is a scientific discovery: electricity moving through a 
# conductor gets pushed sideways by a magnetic field. The sensor detects 
# this "push" and tells the Pico!
#
# WIRING:
# - S (Signal) -> GP21 (Safe Pin)
# - - (GND)    -> GND
# - + (Power)  -> 3.3V
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# Most Hall sensors are "Active Low." This means they report "0" when 
# they see a magnet. We use PULL_UP to keep it at "1" the rest of the time.
hall_sensor = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)

led = machine.Pin("LED", machine.Pin.OUT)

print("System Active. Bring a magnet close to the black chip...")

while True:
    # --- Reading the Magnetic State ---
    # 0 = Detected (The magnetic field opened the gate)
    # 1 = Nothing nearby
    if hall_sensor.value() == 0:
        print(">>> MAGNET DETECTED <<<")
        led.value(1) 
    else:
        led.value(0) 
        
    time.sleep(0.1) 
