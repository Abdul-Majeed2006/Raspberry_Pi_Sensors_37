# -----------------------------------------------------------------------------
# Lesson 14: Heavy Lifting (The Relay)
# -----------------------------------------------------------------------------
# Module: KY-019 Relay Module
# Goal: Use a tiny signal from the Pico to control a large physical switch.
#
# WHY THIS MATTERS:
# Your Pico can only output a tiny bit of power (3.3V). You can't plug a lamp 
# or a motor directly into it! A Relay acts like a middleman: the Pico 
# flips the relay, and the relay flips the heavy power.
#
# HOW IT WORKS:
# Inside the relay is an electromagnet. When the Pico sends power, the 
# magnet pulls a metal lever with a "CLICK!" that completes a separate 
# circuit.
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
relay = machine.Pin(16, machine.Pin.OUT)

print("System Active. Listen for the physical 'CLICK' of the relay!")

# --- The Blue Screw Block (Terminology) ---
# NO (Normally Open): The circuit is BROKEN when the relay is off.
# NC (Normally Closed): The circuit is CONNECTED when the relay is off.
# COM (Common): The moving part of the switch.

while True:
    # 1. Flip the switch ON
    print(">>> RELAY ON  (Internal Magnet Active)")
    relay.value(1) 
    time.sleep(2) # Keep it on for 2 seconds
    
    # 2. Flip the switch OFF
    print("<<< RELAY OFF (Spring pulls it back)")
    relay.value(0) 
    time.sleep(2)
