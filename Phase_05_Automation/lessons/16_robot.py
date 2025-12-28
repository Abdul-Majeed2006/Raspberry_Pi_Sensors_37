# -----------------------------------------------------------------------------
# Lesson 16: Robot Vision (Obstacle Avoidance)
# -----------------------------------------------------------------------------
# Module: KY-032 Obstacle Avoidance Module
# Goal: Build a sensor that can "see" walls before hitting them.
#
# WHY THIS MATTERS:
# This is how robotic vacuum cleaners (like Roombas) navigate your house! 
# It's an "Active" sensor, meaning it creates its own signal and listens 
# for the echo.
#
# HOW IT WORKS (Infrared Reflection):
# 1. The sensor shoots out a beam of invisible IR light.
# 2. If there is a wall, the light bounces back (Reflects).
# 3. The receiver eye sees the bounce and tells the Pico to STOP!
#
# WIRING:
# - OUT (Signal) -> GP16
# - + (VCC)      -> 3.3V
# - G (GND)      -> GND
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# We use GP16 (Pin 21) which is clustered at the bottom-right corner.
# - 0 = OBSTACLE (Seeing a reflection)
# - 1 = CLEAR (No reflection)
sensor = machine.Pin(16, machine.Pin.IN)

led = machine.Pin("LED", machine.Pin.OUT)

print("System Active. Move your hand toward the sensor eyes...")

while True:
    # Check if there is a bounce-back of light
    if sensor.value() == 0:
        print(">>> WARNING: OBSTACLE DETECTED! <<<")
        
        # In a real robot, this is where we would stop the motors!
        led.value(1) 
        time.sleep(0.5) 
        led.value(0)
    
    time.sleep(0.1) # Rapid scanning
