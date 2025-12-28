# -----------------------------------------------------------------------------
# Lesson 08: Shake & Tilt (Physics Sensors)
# -----------------------------------------------------------------------------
# Modules: KY-002 (Vibration) / KY-020 (Tilt)
# Goal: Detect physical motion using a mechanical switch.
#
# WHY THIS MATTERS:
# This is how a car alarm knows if someone bumped the window, or how your 
# washing machine knows if it's "off balance." It converts a physical 
# shock into a digital signal.
#
# HOW IT WORKS:
# Inside the Vibration sensor is a tiny, loose spring. When you bump it, 
# the spring wobbles and touches a center pin, closing the circuit.
#
# WIRING:
# - S (Signal) -> GP21 (Safe Pin)
# - - (GND)    -> GND
# - + (Power)  -> 3.3V
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# We use PULL_UP because these simple switches usually connect to GND 
# when they vibrate. This keeps the pin at "1" until it is bumped.
sensor = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)

led = machine.Pin("LED", machine.Pin.OUT)

print("System Active. Waiting for vibration/shake...")

move_count = 0

while True:
    # --- High Speed Polling ---
    # Unlike a button which you hold down, a vibration is a MICRO-SECOND event.
    # If the Pico "sleeps" for even 0.01 seconds, it might miss the shock!
    # So we run this loop as fast as the CPU can handle.
    
    if sensor.value() == 0: 
        # 0 means the spring hit the center pin (Vibration occurred).
        move_count += 1
        print(f"BUMP DETECTED! Total: {move_count}")
        
        # Give the user visual feedback
        led.value(1) 
        time.sleep(0.1) # Debounce: Stop checking for 100ms so we don't count 1 bump as 50.
        led.value(0)
    
    # NOTICE: No 'time.sleep' here at the bottom. 
    # We want to "listen" with 100% focus.
