# -----------------------------------------------------------------------------
# Tool: Diagnostic Cycler
# -----------------------------------------------------------------------------
# Goal: Cycle through pins one by one to verify wiring order.
# Why:  If you wired GP16 to the LED but the code triggers GP17, valid
#       hardware will look broken. This test confirms PHYSICAL wiring.
# -----------------------------------------------------------------------------

import machine
import time

class HardwareConfig:
    TEST_CLUSTER = [16, 17, 18, 26, 27]
    CYCLE_SPEED = 1.0

def main():
    print("========================================")
    print("     CLUSTERED WIRING DIAGNOSTIC")
    print("========================================")
    
    while True:
        for pin_id in HardwareConfig.TEST_CLUSTER:
            print(f"--> TESTING: GP{pin_id} ...")
            try:
                # Turn ON
                p = machine.Pin(pin_id, machine.Pin.OUT)
                p.value(1)
                time.sleep(HardwareConfig.CYCLE_SPEED)
                
                # Turn OFF
                p.value(0)
                time.sleep(0.2)
                
            except Exception as e:
                print(f"    ERROR: {e}")
        
        print("\n--- Cycle Complete (Restarting) ---\n")

if __name__ == "__main__":
    main()
