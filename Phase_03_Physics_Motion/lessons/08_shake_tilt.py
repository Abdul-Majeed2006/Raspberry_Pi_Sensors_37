# -----------------------------------------------------------------------------
# Lesson 08: Shake & Tilt (Physics Sensors)
# -----------------------------------------------------------------------------
# Goal: Detect physical movement.
#       We will use the "Vibration Switch" (Spring inside) or "Tilt Switch" (Ball inside).
#       They act just like buttons: 1 when shaken/tilted, 0 when still.
#
# WIRING:
# - S (Signal) -> GP16
# - - (GND)    -> GND
# - + (Power)  -> 3.3V
#
# Skills Learnt:
# - Digital Inputs
# - Signal Debouncing
# - High-Speed Polling
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# The sensor acts like a button.
# If it's unstable, we can use a PULL_UP or PULL_DOWN depending on the module.
# Most KY-002 (Vibration) modules need PULL_UP.
sensor = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

led = machine.Pin("LED", machine.Pin.OUT)

print("Waiting for movement...")

shake_count = 0

while True:
    # Read sensor
    # Note: Vibration sensors create VERY short pulses (microseconds).
    # A normal loop might miss them!
    # But for now, let's try to catch it.
    
    if sensor.value() == 0: # 0 means "Connected/Triggered" for most vibration switches
        shake_count += 1
        print(f"SHAKE DETECTED! ({shake_count})")
        led.value(1) # Flash LED
        time.sleep(0.1) # Debounce/Pause
        led.value(0)
    
    # No sleep in the 'else' block because we want to check as fast as possible!
