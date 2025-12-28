# -----------------------------------------------------------------------------
# Lesson 18: Path Finder (Tracking Sensor)
# -----------------------------------------------------------------------------
# Module: KY-033 Tracking Sensor Module
# Goal: Detect black lines on a white surface (or vice versa).
#       This is the core of "Line Following" robots.
#
# WIRING:
# - S (Signal) -> GP16
# - + (Power)  -> 3.3V
# - - (GND)    -> GND
#
# Skills Learnt:
# - Infrared Reflection Thresholds
# - Digital State Filtering
# - Surface Property Detection
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# 1 = Detecting white (Reflection received)
# 0 = Detecting black (No reflection - infrared absorbed)
sensor = machine.Pin(16, machine.Pin.IN)

led = machine.Pin("LED", machine.Pin.OUT)

print("Line Tracking Active. Move the sensor over a dark line!")

while True:
    is_on_line = (sensor.value() == 0) # 0 often means "Line Detected"
    
    if is_on_line:
        print("!! LINE DETECTED !!")
        led.value(1)
    else:
        led.value(0)
        
    time.sleep(0.1)
