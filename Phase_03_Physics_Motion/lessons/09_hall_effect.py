# -----------------------------------------------------------------------------
# Lesson 09: Magnetic Fields (Hall Effect)
# -----------------------------------------------------------------------------
# Module: KY-003 Hall Magnetic Sensor Module
# Goal: Detect if a magnet is nearby without any physical contact.
#
# ANATOMY:
# The Hall Effect occurs when a magnetic field pushes electrons sideways
# in a conductor, creating a voltage difference.
#
# WIRING:
# - S (Signal) -> GP16
# - - (GND)    -> GND
# - + (Power)  -> 3.3V
# -----------------------------------------------------------------------------

import machine
import time

class HardwareConfig:
    PIN_HALL_SENSOR = 16
    PIN_LED         = "LED"

def main():
    # 1. Setup Input (Active Low: 0 = Magnet Detected)
    # Most Hall sensors pull the line to Ground when a field is present.
    # We use PULL_UP to keep it High (1) when no magnet is near.
    hall_sensor = machine.Pin(HardwareConfig.PIN_HALL_SENSOR, machine.Pin.IN, machine.Pin.PULL_UP)
    
    # 2. Setup Output
    led = machine.Pin(HardwareConfig.PIN_LED, machine.Pin.OUT)
    
    print("--- SYSTEM READY: MAGNET DETECTOR ---")
    print("Bring a magnet close to the sensor...")
    
    while True:
        # 3. Read Sensor State
        # Logic Inversion: 0 means YES, 1 means NO
        is_magnet_present = (hall_sensor.value() == 0)
        
        if is_magnet_present:
            print(">>> MAGNET DETECTED <<<")
            led.value(1)
        else:
            led.value(0)
            
        time.sleep(0.1)

if __name__ == "__main__":
    main()
