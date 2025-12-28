# -----------------------------------------------------------------------------
# Lesson 10: Sound Detection (The Microphone)
# -----------------------------------------------------------------------------
# Modules: KY-037 (Small) / KY-038 (Big) Sound Sensor
# Goal: Detect loud noises like claps, snaps, or bangs.
#
# WHY THIS MATTERS:
# This is the "Ear" of your robot. You can use it to build a "Clapper" light 
# switch or a security system that hears a window breaking. 
#
# CALIBRATION (The Blue Box):
# There is a blue box with a tiny screw on your sensor. This is a 
# "Potentiometer." 
# - Turn it until the LED on the module just turns OFF.
# - Now, if you clap, the LED should flash! This sets the "Threshold."
#
# WIRING:
# - OUT (Signal) -> GP16
# - GND          -> GND
# - VCC (+)      -> 3.3V
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# We use GP16 (Pin 21) which is clustered at the bottom-right corner.
# The microphone is a digital input. It says "1" when it hears a spike in volume.
mic_pin = machine.Pin(16, machine.Pin.IN)
led = machine.Pin("LED", machine.Pin.OUT)

print("System Active. Clap your hands to toggle the light!")

# --- State Tracking variables ---
# We use these to remember the past so we can make decisions in the future.
last_trigger_time = 0
clap_count = 0

while True:
    # 1. Listen for a sound spike
    if mic_pin.value() == 1:
        current_time = time.ticks_ms()
        
        # --- Debouncing (The "Ignore" Window) ---
        # Sound echoes. One clap might look like 50 tiny spikes to a computer.
        # we calculate the difference between 'now' and the 'last time' we clapped.
        # If it's less than 200ms, we ignore it as an echo.
        if time.ticks_diff(current_time, last_trigger_time) > 200:
            clap_count += 1
            print(f"CLAP #{clap_count} DETECTED!")
            
            # .toggle() is a shortcut: If it's ON, turn it OFF. If it's OFF, turn it ON.
            led.toggle()
            
            # Remember this moment as the new "Last Time"
            last_trigger_time = current_time
    
    # We don't sleep here because we need to hear that fast clap!
