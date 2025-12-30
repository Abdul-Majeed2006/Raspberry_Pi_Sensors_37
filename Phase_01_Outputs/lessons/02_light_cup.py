# -----------------------------------------------------------------------------
# Lesson 02: Magic Light Cup (Tilt Switch)
# -----------------------------------------------------------------------------
# Module: KY-027 Magic Light Cup Module
# Goal: Detect gravity/tilt.
#
# ANATOMY:
# A mercury tilt switch behaves like a button. 
# Tilted = Circuit Closed (1). Upright = Open (0).
#
# WIRING:
# - G (Ground) -> GND
# - + (Power)  -> 3.3V
# - S (Signal) -> GP16 (Digital Input)
# - L (LED)    -> GP17 (Digital Output)
# -----------------------------------------------------------------------------

import machine
import time

class HardwareConfig:
    PIN_TILT = 16
    PIN_LED  = 17
    
def main():
    # 1. Setup Input
    tilt_switch = machine.Pin(HardwareConfig.PIN_TILT, machine.Pin.IN)
    
    # 2. Setup Output (PWM for dimming capability)
    led = machine.PWM(machine.Pin(HardwareConfig.PIN_LED))
    led.freq(1000)
    
    print("--- SYSTEM READY: MAGIC CUP ---")
    print("Tilt the module...")
    
    while True:
        # A. Read Status
        is_tilted = (tilt_switch.value() == 1)
        
        # B. React
        if is_tilted:
            # Full Brightness
            print("Status: ACTIVATED")
            led.duty_u16(65535)
        else:
            # Dim Glow (Standby)
            print("Status: IDLE")
            led.duty_u16(4000)
            
        time.sleep(0.1)

if __name__ == "__main__":
    main()
