# -----------------------------------------------------------------------------
# Lesson 10: Sound Detection (The Microphone)
# -----------------------------------------------------------------------------
# Modules: KY-037 (Small) / KY-038 (Big) Sound Sensor
# Goal: Detect loud noises like claps, snaps, or bangs.
#
# TUNING:
# Use the tiny screw (Potentiometer) on the blue box to set the threshold.
# Turn until the LED *just* turns off, then clap to test.
#
# WIRING:
# - OUT (Signal) -> GP16 (Digital)
# - GND          -> GND
# - VCC (+)      -> 3.3V
# -----------------------------------------------------------------------------

import machine
import time

class HardwareConfig:
    PIN_MIC = 16
    PIN_LED = "LED"
    DEBOUNCE_MS = 200 # Ignore echoes for 200ms

def main():
    # 1. Setup Pins
    mic_pin = machine.Pin(HardwareConfig.PIN_MIC, machine.Pin.IN)
    led = machine.Pin(HardwareConfig.PIN_LED, machine.Pin.OUT)
    
    print("--- SYSTEM READY: CLAP DETECTOR ---")
    
    # State Tracking
    last_trigger_time = 0
    clap_count = 0
    
    while True:
        # 2. High Speed Listening loop
        if mic_pin.value() == 1:
            current_time = time.ticks_ms()
            
            # 3. Debounce Logic (Ignore Echoes)
            time_since_last = time.ticks_diff(current_time, last_trigger_time)
            
            if time_since_last > HardwareConfig.DEBOUNCE_MS:
                clap_count += 1
                print(f"CLAP #{clap_count} DETECTED!")
                led.toggle()
                
                # Update timestamp
                last_trigger_time = current_time
    
    # No sleep here. We need max sampling rate for sound.

if __name__ == "__main__":
    main()
