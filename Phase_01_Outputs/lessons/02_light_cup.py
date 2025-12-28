# -----------------------------------------------------------------------------
# Lesson 02: Magic Light Cup (Tilt Switch)
# -----------------------------------------------------------------------------
# Module: KY-027 Magic Light Cup Module
# Goal: Detect gravity and dim an LED based on tilt orientation.
#
# WHY THIS MATTERS:
# This is how your smartphone knows to rotate the screen when you turn it 
# sideways! This "Magic Cup" is a simplified version of a Motion Sensor.
#
# HOW IT WORKS:
# Inside the glass tube is a tiny metal ball (or mercury). When you tilt it, 
# the ball rolls onto two wires, completing a circuit like a button press.
#
# WIRING:
# - G (Ground) -> GND
# - + (Power)  -> 3.3V
# - S (Signal) -> GP21 (Reads the tilt)
# - L (LED)    -> GP15 (Controls the light)
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# The Tilt Switch is an INPUT. The Pico "listens" to this pin.
# We moved this to GP21 to stay away from the dead pins (13/14).
tilt_switch = machine.Pin(21, machine.Pin.IN)

# The LED is an OUTPUT. The Pico "talks" to this pin.
# We use PWM so we can set specific brightness levels (0 to 65535).
led = machine.PWM(machine.Pin(15))
led.freq(1000)

print("Tilt the module to see the 'Magic' happen!")

while True:
    # --- The Digital Input ---
    # .value() returns a "Boolean" (True/1 or False/0).
    # 1 means the ball is touching the contacts (Circuit Closed).
    # 0 means the ball has rolled away (Circuit Open).
    tilt_status = tilt_switch.value()

    if tilt_status == 1:
        # If tilted, set LED to 100% Power.
        print("Status: ACTIVATED (Full Bright)")
        led.duty_u16(65535) 
    else:
        # if not tilted, set LED to about 8% Power (Dim Glow).
        print("Status: IDLE (Dim Glow)")
        led.duty_u16(5000) 

    # --- Polling Rate ---
    # Running the loop too fast can make the terminal hard to read.
    # 0.1 seconds (100ms) is perfect for human interaction.
    time.sleep(0.1) 
