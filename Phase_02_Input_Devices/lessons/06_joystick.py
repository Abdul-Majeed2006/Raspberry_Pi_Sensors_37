# -----------------------------------------------------------------------------
# Lesson 06: Analog Control (The Joystick)
# -----------------------------------------------------------------------------
# Goal: Read "Analog" signals. A button is 0 or 1. A Joystick is 0 to 65535!
#       We will read the X and Y positions of the thumbstick.
#
# WIRING:
# The Joystick has 5 pins:
# - GND -> GND
# - +5V -> 3.3V (The Pico is 3.3V logic, so use 3.3V!)
# - VRx (Variable Resistor X) -> GP26 (ADC0)
# - VRy (Variable Resistor Y) -> GP27 (ADC1)
# - SW  (Switch)              -> GP22 (Digital Button)
#
# Skills Learnt:
# - Analog to Digital Conversion (ADC)
# - Threshold Logic
# - Pull-Up Resistors
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# Joysticks need ADC (Analog to Digital Converter)
joy_x = machine.ADC(machine.Pin(26))
joy_y = machine.ADC(machine.Pin(27))

# The switch is just a normal button
joy_btn = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

print("Starting Joystick... Move it around!")

while True:
    # Read Analog values (Range: 0 to 65535)
    # Center is usually around ~32768
    x_val = joy_x.read_u16()
    y_val = joy_y.read_u16()
    
    # Read Button (0 = Pressed, 1 = Released because of PULL_UP)
    btn_val = joy_btn.value()
    
    # Print status
    status = ""
    if btn_val == 0:
        status = "[PRESSED] "
    
    # Determine direction based on values
    # (Thresholds: < 20000 is Low, > 50000 is High)
    direction = "Center"
    if y_val < 20000: direction = "Up"
    if y_val > 50000: direction = "Down"
    if x_val < 20000: direction = "Left"
    if x_val > 50000: direction = "Right"
        
    print(f"X: {x_val} | Y: {y_val} | Dir: {status}{direction}")
    
    time.sleep(0.1)
