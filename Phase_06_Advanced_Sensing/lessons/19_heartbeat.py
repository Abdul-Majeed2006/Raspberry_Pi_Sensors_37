# -----------------------------------------------------------------------------
# Lesson 19: Bio-Metrics (Heartbeat Sensor)
# -----------------------------------------------------------------------------
# Module: KY-039 Heartbeat Sensor Module
# Goal: Use light to see the blood pumping inside your own body!
#
# WHY THIS MATTERS:
# This is the same technology in an Apple Watch or a hospital finger-clip. 
# It's called "Photoplethysmography" (PPG). It's a non-invasive way to check 
# a person's health using nothing but an LED and a light sensor.
#
# HOW IT WORKS:
# Blood absorbs IR light. When your heart beats, a "wave" of blood rushes 
# into your finger, making it slightly more opaque. 
# 1. The sensor shines light THROUGH your finger.
# 2. When blood pulses, LESS light reaches the receiver.
# 3. By measuring these tiny changes in light, we can count your heart rate!
#
# WIRING:
# - S (Signal) -> GP26 (Analog Input 0)
# - (Center)   -> 3.3V
# - (-)        -> GND
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# This sensor is extremely sensitive. Movement or external room lights 
# can ruin the reading. Hold your finger very still!
sensor = machine.ADC(machine.Pin(26))

print("System Active. Place your finger GENTLY over the LED and Receiver...")

# --- Note on Noisy Data ---
# In a professional medical device, we would use complex math (Digital 
# Filters) to clean this data. For now, we are looking at the "Raw Wave."

while True:
    # Read the pulse intensity (0 to 65535)
    pulse_value = sensor.read_u16()
    
    # We print the raw number. If you use a "Plotter," you will see a wave!
    print(pulse_value)
    
    # We check 100 times per second to catch the fast heart spike
    time.sleep(0.01)
