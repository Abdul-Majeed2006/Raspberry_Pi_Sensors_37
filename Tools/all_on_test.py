# -----------------------------------------------------------------------------
# Tool: All-On Test
# -----------------------------------------------------------------------------
# Goal: Turn ON all commonly used testing pins simultaneously.
# Why: To differentiate between a "Dead Sensor" and a "Dead Pin".
#      If the sensor doesn't work here, the sensor is broken.
# -----------------------------------------------------------------------------

import machine
import time

class HardwareConfig:
    # We test the standard "Cluster" used in this curriculum
    # GP16/17/18 (Bottom Right Digital Block)
    # GP26/27    (Analog Block)
    TEST_CLUSTER = [16, 17, 18, 26, 27]

def main():
    print("========================================")
    print("       THE 'POKE' TEST TOOL")
    print("========================================")
    print(f"Setting Clustered Pins {HardwareConfig.TEST_CLUSTER} to HIGH.")
    
    print("\nTROUBLESHOOTING:")
    print("1. Keep this script running.")
    print("2. Touch your component wire to the pins listed.")
    print("3. If it lights up on GP16 but NOT GP26, GP26 is dead.")
    print("----------------------------------------\n")
    
    # Activate All
    active_pins = []
    for pin_id in HardwareConfig.TEST_CLUSTER:
        try:
            p = machine.Pin(pin_id, machine.Pin.OUT)
            p.value(1)
            active_pins.append(p)
        except Exception as e:
            print(f"FAILED to open GP{pin_id}: {e}")
            
    print(">>> ALL PINS ACTIVE. Start Probing! <<<")
    
    # Keep alive loop
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
