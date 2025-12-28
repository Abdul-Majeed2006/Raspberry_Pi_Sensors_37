# -----------------------------------------------------------------------------
# Lesson 16: Robot Vision (Obstacle Avoidance)
# -----------------------------------------------------------------------------
# Module: KY-032 Obstacle Avoidance Module
# Goal: Build the brain of a Roomba.
#       We use the "Obstacle Avoidance Sensor".
#       It emits IR light and checks if it bounces back (Reflection).
#
# WIRING:
# - OUT (Signal) -> GP16
# - + (Power)    -> 3.3V
# - G (GND)      -> GND
#
# Skills Learnt:
# - Digital Inputs (Active Low)
# - Reflection Physics
# - Autonomous Decision Logic
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# 0 = Obstacle Detected (Reflection received)
# 1 = Clear Path (No reflection)
sensor = machine.Pin(16, machine.Pin.IN)

led = machine.Pin("LED", machine.Pin.OUT)

print("Robot Active. Moving Forward...")

while True:
    is_blocked = (sensor.value() == 0)
    
    if is_blocked:
        print("!! OBSTACLE !! -> STOP -> REVERSE -> TURN")
        led.value(1) # Panic Light
        
        # Simulate Evasive Maneuvers
        time.sleep(0.5) 
        print("Resuming Patrol...")
        led.value(0)
    
    time.sleep(0.1)
