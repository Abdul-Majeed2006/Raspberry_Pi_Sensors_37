# -----------------------------------------------------------------------------
# Lesson 05: The Power of Inputs (Buttons & Touch)
# -----------------------------------------------------------------------------
# Modules: KY-004 Button / KY-036 Metal Touch
# Goal: Detect physical contact using both a mechanical switch and a sensor.
#
# WHY THIS MATTERS:
# Every interaction you have with a machine (Keyboard, Mouse, Phone screen) 
# starts with an "Input." Learning to read a button correctly is the 
# first step in building an interactive device.
#
# PULL-DOWN RESISTORS:
# Imagine a pin is like a "Floating" antenna. If it's not connected to 
# anything, it picks up static electricity from the air and might say 
# "1" or "0" randomly. 
# We use a "Pull-Down" to tie the pin to Ground (0) so it stays at 0 
# until someone pushes a button to force it to 3.3V (1).
#
# WIRING:
# - Button S  -> GP16 (Master Pin)
# - Touch S   -> GP17 (Nearby Neighbor)
# - All GND   -> GND
# - All +     -> 3.3V
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# We use PULL_DOWN to ensure safety and stability.
# We cluster these on GP16 and GP17 for clean wiring.
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
touch_sensor = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

# The onboard LED acts as our "Success" indicator.
led = machine.Pin("LED", machine.Pin.OUT)

print("Ready! Press the Button or touch the point.")

while True:
    # .value() reads the voltage. 
    # High Voltage (3.3V) = 1
    # Low Voltage (0V)   = 0
    btn_pushed = button.value()
    sensor_touched = touch_sensor.value()
    
    # --- Boolean Logic (The 'OR' Gate) ---
    # We want the LED to turn on if EITHER one is activated.
    # In coding, 'or' allows us to combine multiple conditions.
    if btn_pushed == 1 or sensor_touched == 1:
        print("INPUT DETECTED!")
        led.value(1) # Send 3.3V to the LED
    else:
        led.value(0) # Send 0V to the LED
        
    # --- Debouncing ---
    # Metal contacts 'bounce' physically when they hit. 
    # A tiny delay helps ignore these microscopic bounces.
    time.sleep(0.05) 
