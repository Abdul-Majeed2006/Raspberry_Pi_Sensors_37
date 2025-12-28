# -----------------------------------------------------------------------------
# Lesson 19: Bio-Metrics (Heartbeat Sensor)
# -----------------------------------------------------------------------------
# Module: KY-039 Heartbeat Sensor Module
# Goal: Detect the pulse in your fingertip by measuring light absorption.
#
# WIRING:
# - S (Signal) -> GP26 (ADC0)
# - middle (+) -> 3.3V
# - (-)        -> GND
#
# Skills Learnt:
# - Analog Signal Processing
# - Peak Detection Algorithms
# - Filtering Noise from Data
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# The Heartbeat sensor is very sensitive to noise! 
# You must hold your finger STEADY on the sensor.
sensor = machine.ADC(machine.Pin(26))

print("Place your finger gently on the sensor...")
print("Reading Pulse Data... (Look for peaks)")

while True:
    # Read the raw analog value
    val = sensor.read_u16()
    
    # In a real project, we would use a "Rolling Average" or "High-pass Filter"
    # For this lesson, we just print the raw value to see the wave.
    print(val)
    
    # We poll fast to capture the heartbeat "spike"
    time.sleep(0.01)
