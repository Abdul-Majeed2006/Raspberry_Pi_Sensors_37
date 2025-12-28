# -----------------------------------------------------------------------------
# Lesson 06: Analog Control (The Joystick)
# -----------------------------------------------------------------------------
# Module: KY-023 Joystick Module
# Goal: Understand the difference between Digital (Pulse) and Analog (Smooth).
#
# WHY THIS MATTERS:
# A button is like a light switch (ON/OFF). A joystick is like a steering 
# wheel or a gas pedal—it has many levels of intensity.
#
# HOW IT WORKS (The ADC):
# The Pico has an "Analog to Digital Converter" (ADC). It measures the 
# voltage on a pin and turns it into a number. 
# - 0 Volts       = 0
# - 3.3 Volts     = 65535
#
# WIRING:
# - GND   -> GND
# - +5V   -> 3.3V (The Pico uses 3.3V logic!)
# - VRx   -> GP26 (Analog Input 0)
# - VRy   -> GP27 (Analog Input 1)
# - SW    -> GP22 (Button)
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins (The ADC Class) ---
# We use the ADC class to "measure" the voltage on the pins.
joy_x = machine.ADC(machine.Pin(26))
joy_y = machine.ADC(machine.Pin(27))

# The switch is a digital button. 
# We use PULL_UP because the joystick connects to GND when pressed.
# (So 1 = Idle, 0 = Pressed).
joy_btn = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

print("Starting Joystick... Move it around!")

while True:
    # --- Reading Analog Values ---
    # .read_u16() reads the voltage and returns its 16-bit number (0-65535).
    # Since the stick is held by springs, the "Center" is usually near 32768.
    x_val = joy_x.read_u16()
    y_val = joy_y.read_u16()
    
    # Read Button (Returns 1 if up, 0 if pushed down)
    btn_pushed = (joy_btn.value() == 0)
    
    # --- Threshold Logic ---
    # We use "If" statements to turn numbers into directions.
    # If the number is very high or very low, we know which way it's leaning.
    direction = "Center"
    if y_val < 10000: direction = "UP"
    elif y_val > 50000: direction = "DOWN"
    elif x_val < 10000: direction = "LEFT"
    elif x_val > 50000: direction = "RIGHT"
        
    # Build a nice display string
    btn_text = "[CLICK]" if btn_pushed else "       "
    print(f"{btn_text} X: {x_val:5d} | Y: {y_val:5d} | Direction: {direction}")
    
    time.sleep(0.1)
