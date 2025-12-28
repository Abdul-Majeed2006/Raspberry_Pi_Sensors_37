# -----------------------------------------------------------------------------
# Lesson 02: Magic Light Cup (Tilt Switch)
# -----------------------------------------------------------------------------
# Goal: Use a "Light Cup" module to detect tilting.
#       When you tilt the board, the LED brightness changes.
#
# WHAT IS THIS MODULE?
# It contains two things:
# 1. A Mercury Switch (The glass ball): Detects if it's upright or tilted.
# 2. An LED: Just a normal light.
#
# WIRING (KY-027 "Magic Light Cup"):
# - G (Ground) -> GND
# - + (Power)  -> 3.3V
# - S (Signal) -> GP16 (Reads the tilt)
# - L (LED)    -> GP15 (Controls the light)
#
# Skills Learnt:
# - Digital Inputs (1/0)
# - GPIO Polling Loops
# - Conditional Logic (If/Else)
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# The Tilt Switch is an INPUT (we read from it)
tilt_switch = machine.Pin(16, machine.Pin.IN)

# The LED is an OUTPUT (we write to it)
# We use PWM to make it "fade" instead of just snapping on/off
led = machine.PWM(machine.Pin(15))
led.freq(1000)

print("Tilt the module to change the brightness!")

while True:
    # Read the switch (1 = Tilted/Upright depending on orientation, 0 = Opposite)
    tilt_status = tilt_switch.value()

    if tilt_status == 1:
        # If the ball connects the circuit, go Full Brightness
        print("Status: CLOSED (Bright)")
        led.duty_u16(65535) # Max brightness
    else:
        # If the circuit is broken, go Dim (or Off)
        print("Status: OPEN (Dim)")
        led.duty_u16(5000)  # Very dim glow

    time.sleep(0.1) # Check 10 times a second
