# -----------------------------------------------------------------------------
# Lesson 09: Magnetic Fields (Hall Effect)
# -----------------------------------------------------------------------------
# Module: KY-003 Hall Magnetic Sensor Module
# Goal: Detect magnets!
#       We will use the "Hall Effect" sensor (usually a small black chip).
#       Some modules are Digital (ON/OFF), some are Analog (Strength).
#       We will treat it as a Digital Switch for now.
#
# WIRING:
# - S (Signal) -> GP16
# - - (GND)    -> GND
# - + (Power)  -> 3.3V
#
# Skills Learnt:
# - Digital Inputs (Active Low)
# - Internal Pull-Up Resistors
# - Magnetic Sensing Logic
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# Most Hall sensors pull the pin LOW (0) when a magnet is near.
# So we usually want a PULL_UP resistor.
hall_sensor = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

led = machine.Pin("LED", machine.Pin.OUT)

print("Waiting for a Magnet...")

while True:
    # Read the value
    # 1 = No Magnet (because of Pull-Up)
    # 0 = Magnet Detected (The sensor connects to Ground)
    is_magnet_near = hall_sensor.value()
    
    if is_magnet_near == 0:
        print("MAGNET DETECTED!")
        led.value(1) # Turn LED on
    else:
        led.value(0) # Turn LED off
        
    time.sleep(0.1)
