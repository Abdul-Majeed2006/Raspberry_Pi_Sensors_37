# -----------------------------------------------------------------------------
# Lesson 18: Path Finder (Line Tracking)
# -----------------------------------------------------------------------------
# Module: KY-033 Tracking Sensor
# Goal: Distinguish between Light (Floor) and Dark (Tape) surfaces.
#
# PHYSICS:
# - White/Light surfaces REFLECT light.
# - Black/Dark surfaces ABSORB light.
# The sensor detects the difference in reflection.
#
# WIRING:
# - S -> GP16
# - + -> 3.3V
# - - -> GND
# -----------------------------------------------------------------------------

import machine
import time

class HardwareConfig:
    PIN_SENSOR = 16
    PIN_INDICATOR = "LED"

def main():
    # 1. Setup Sensor
    # Logic depends on surface, typically:
    # 0 = Reflection (White/Light)
    # 1 = No Reflection (Black/Dark Line)
    # *Note: Check your specific module behavior!
    sensor = machine.Pin(HardwareConfig.PIN_SENSOR, machine.Pin.IN)
    
    indicator = machine.Pin(HardwareConfig.PIN_INDICATOR, machine.Pin.OUT)
    
    print("--- SYSTEM READY: LINE TRACKER ---")
    
    while True:
        val = sensor.value()
        
        if val == 1:
            print(">>> ON LINE (Dark) <<<")
            indicator.value(1)
        else:
            # print("...searching...") # Commented out to reduce spam
            indicator.value(0)
            
        time.sleep(0.05) # FAST polling for high speed robots

if __name__ == "__main__":
    main()
