# -----------------------------------------------------------------------------
# Lesson 14: Heavy Lifting (The Relay)
# -----------------------------------------------------------------------------
# Module: KY-019 Relay Module
# Goal: Control high-power devices physically.
#       A "Relay" is a mechanical switch controlled by a magnet.
#       You will HEAR it "Click" when it turns on.
#
# WIRING:
# - S (Signal) -> GP16
# - + (Power)  -> 3.3V (or 5V if your module requires it)
# - - (GND)    -> GND
#
# RELAY PORTS (The Blue Box):
# - NC (Normally Closed): Connected when OFF.
# - NO (Normally Open):   Connected when ON. (Most common used)
# - COM (Common):         The wire you want to switch.
#
# Skills Learnt:
# - Digital Outputs
# - High Voltage Control Logic
# - Normally Open (NO) vs Normally Closed (NC)
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# The Relay is just a big digital switch.
# Some relays are "Active LOW" (ON when 0).
# Some are "Active HIGH" (ON when 1).
relay = machine.Pin(16, machine.Pin.OUT)

print("Cycling the Relay...")

while True:
    print("Relay ON (Click!)")
    relay.value(1) # Try 0 if this doesn't click
    time.sleep(2)
    
    print("Relay OFF")
    relay.value(0) # Try 1 if this doesn't click
    time.sleep(2)
