# -----------------------------------------------------------------------------
# Lesson 08: Shake & Tilt (Physics Sensors)
# -----------------------------------------------------------------------------
# Modules: KY-002 (Vibration) / KY-020 (Tilt)
# Goal: Detect physical motion using a mechanical switch.
#
# ANATOMY:
# Inside the Vibration sensor is a tiny spring. When shaken, it wobbles and
# touches a center post, completing the circuit.
#
# WIRING:
# - S (Signal) -> GP16
# - - (GND)    -> GND
# - + (Power)  -> 3.3V
# -----------------------------------------------------------------------------

import machine
import time

class HardwareConfig:
    PIN_SENSOR = 16
    PIN_LED    = "LED"
    DEBOUNCE_MS = 100

def main():
    # 1. Setup Input (Active Low: 0 = Vibration Detected)
    # We use PULL_UP because the switch connects to Ground when triggered.
    sensor = machine.Pin(HardwareConfig.PIN_SENSOR, machine.Pin.IN, machine.Pin.PULL_UP)
    
    # 2. Setup Output
    led = machine.Pin(HardwareConfig.PIN_LED, machine.Pin.OUT)
    
    print("--- SYSTEM READY: SHAKE DETECTOR ---")
    move_count = 0
    
    while True:
        # High Speed Polling Loop
        # Vibration is a micro-second event. We cannot sleep here!
        if sensor.value() == 0:
            move_count += 1
            print(f"BUMP DETECTED! Total: {move_count}")
            
            # Visual Feedback
            led.value(1)
            
            # Debounce: Wait for the spring to settle
            time.sleep(HardwareConfig.DEBOUNCE_MS / 1000)
            led.value(0)
            
        # No loop sleep = Maximum Responsiveness

if __name__ == "__main__":
    main()
