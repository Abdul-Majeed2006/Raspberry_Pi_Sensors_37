# -----------------------------------------------------------------------------
# Lesson 10: Sound Detection (The Microphone)
# -----------------------------------------------------------------------------
# Goal: Detect loud noises (like a Clap or a Snap).
#       The module has a potentiometer (blue box with a screw) to adjust sensitivity.
#
# WIRING:
# - OUT (Signal) -> GP16
# - GND          -> GND
# - VCC (+)      -> 3.3V
#
# Skills Learnt:
# - Digital Inputs
# - Non-blocking Timers (ticks_ms)
# - Sensitivity Tuning
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# The microphone usually sends a HIGH (1) or LOW (0) signal when sound is detected.
mic_pin = machine.Pin(16, machine.Pin.IN)
led = machine.Pin("LED", machine.Pin.OUT)

print("Quiet please... I'm listening.")

last_clap_time = 0
clap_count = 0

while True:
    # Read the microphone
    if mic_pin.value() == 1: # Some modules might trigger on 0, try both if it doesn't work!
        current_time = time.ticks_ms()
        
        # Debounce: Ignore echoes or long noises (must be 200ms apart)
        if time.ticks_diff(current_time, last_clap_time) > 200:
            clap_count += 1
            print(f"CLAP DETECTED! ({clap_count})")
            
            # Flash LED
            led.toggle()
            
            last_clap_time = current_time
    
    # Run fast! No sleep.
