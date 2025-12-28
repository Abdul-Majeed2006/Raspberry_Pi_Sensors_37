# -----------------------------------------------------------------------------
# Lesson 07: Spinning Control (Rotary Encoder)
# -----------------------------------------------------------------------------
# Module: KY-040 Rotary Encoder Module
# Goal: Detect the direction and speed of a spinning knob.
#
# WHY THIS MATTERS:
# Unlike a Volume Knob in an old car (which stops at a certain point), a 
# Rotary Encoder spins forever. It's used on modern stereos, 3D printers, 
# and digital cameras to scroll through menus.
#
# HOW IT WORKS (Quadrature Encoding):
# Inside are two switches (CLK and DT). When you spin, they click on and off 
# but one is slightly behind the other. 
# - If CLK clicks FIRST, you are spinning RIGHT.
# - If DT clicks FIRST, you are spinning LEFT.
#
# WIRING:
# - GND -> GND
# - +   -> 3.3V
# - SW  -> GP22 (The button inside the knob)
# - DT  -> GP21 (Data pin)
# - CLK -> GP20 (Clock pin)
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# We moved these to 20/21 to avoid the dead pins (13/14).
# Encoders need to be read as INPUTS.
dt_pin = machine.Pin(21, machine.Pin.IN)
clk_pin = machine.Pin(20, machine.Pin.IN)

# We store the previous state so we can tell when the knob moves.
previous_value = True
counter = 0

def update_encoder():
    """
    Checks if the knob has moved and updates the counter.
    """
    global previous_value, counter
    
    # Read the current state of the CLK pin
    current_value = clk_pin.value()
    
    # If the pin state CHANGED (e.g. from 1 to 0), the knob moved!
    if current_value != previous_value:
        
        # Now we check the DT pin to see which way it's spinning.
        # This is the "Magic" of encoders: comparing the two pins.
        if dt_pin.value() != current_value:
            # Spinning Clockwise
            counter += 1
            print(">>> CLOCKWISE [", counter, "]")
        else:
            # Spinning Counter-Clockwise
            counter -= 1
            print("<<< COUNTER-CLOCKWISE [", counter, "]")
            
    # Save the current value for the next check
    previous_value = current_value

print("System Ready. Start spinning the knob!")

# --- The High Speed Loop ---
while True:
    # We call our function as fast as possible. 
    # If we add a time.sleep() here, we might MISS a pulse while the 
    # computer is sleeping!
    update_encoder()
