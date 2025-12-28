# -----------------------------------------------------------------------------
# Lesson 18: Path Finder (Tracking Sensor)
# -----------------------------------------------------------------------------
# Module: KY-033 Tracking Sensor Module
# Goal: Build a sensor that can "read" a path on the floor.
#
# WHY THIS MATTERS:
# This is how factory robots move parts around a warehouse. They follow a 
# painted line on the floor. It's much cheaper and more reliable than 
# using a camera or GPS!
#
# HOW IT WORKS (Absorption):
# The sensor shoots IR light at the ground. 
# - White Surfaces: Reflect the light back (Mirror effect).
# - Black Lines:   Suck up the light (Absorption effect). 
# By seeing where the light disappears, the robot knows exactly where the 
# line is.
#
# WIRING:
# - S (Signal) -> GP16
# - + (VCC)    -> 3.3V
# - - (GND)    -> GND
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# We use GP16 (Pin 21) which is clustered at the bottom-right corner.
# - 1 = Light surface (Reflection)
# - 0 = Dark line (Absorption)
sensor = machine.Pin(16, machine.Pin.IN)

led = machine.Pin("LED", machine.Pin.OUT)

print("System Active. Move the sensor eyes over a thick black marker line!")

while True:
    # Read the state of the reflection
    if sensor.value() == 0:
        print(">>> PATH DETECTED <<<")
        led.value(1)
    else:
        led.value(0)
        
    time.sleep(0.1) # Check 10 times per second
