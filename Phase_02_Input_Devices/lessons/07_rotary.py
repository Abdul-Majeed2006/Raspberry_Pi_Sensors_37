# -----------------------------------------------------------------------------
# Lesson 07: Spinning Control (Rotary Encoder)
# -----------------------------------------------------------------------------
# Module: KY-040 Rotary Encoder Module
# Goal: Read a Rotary Encoder (the knob that spins forever).
#       Used for volume knobs, menu scrolling, etc.
#
# WIRING (KY-040):
# - GND -> GND
# - +   -> 3.3V
# - SW  -> GP22 (Button) - Optional
# - DT  -> GP18 (Data)
# - CLK -> GP19 (Clock)
#
# Skills Learnt:
# - Rotary Encoding (Quadrature)
# - State Tracking
# - High-Speed Polling
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
dt_pin = machine.Pin(18, machine.Pin.IN)
clk_pin = machine.Pin(19, machine.Pin.IN)

previous_value = True
count = 0

def rotary_changed():
    # We call this every time the logic loop runs
    global previous_value, count
    
    # Read the CLK pin
    current_value = clk_pin.value()
    
    # If the CLK pin changed logic (e.g. went from 0 to 1 or 1 to 0)
    # detecting a "pulse"
    if current_value != previous_value:
        
        # We need to check the DT pin to know the direction.
        # If CLK != DT, we are spinning CLOCKWISE.
        if dt_pin.value() != current_value:
            count += 1
            print("Clockwise ->", count)
        else:
            # Otherwise we are spinning COUNTER-CLOCKWISE
            count -= 1
            print("Counter-Clockwise <-", count)
            
    previous_value = current_value

print("Start spinning!")

while True:
    rotary_changed()
    # No sleep here! We need to run FAST to catch the pulses.
