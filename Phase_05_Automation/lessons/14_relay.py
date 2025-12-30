# -----------------------------------------------------------------------------
# Lesson 14: Heavy Lifting (The Relay)
# -----------------------------------------------------------------------------
# Module: KY-019 Relay Module
# Goal: Control high-power circuits (like a lamp or fan) safely.
#
# ANATOMY:
# A Relay is an electromagnet that pulls a physical metal switch.
# - NO (Normally Open): Disconnected until you turn it ON.
# - NC (Normally Closed): Connected until you turn it OFF.
# - click! : The sound of the magnet moving the switch.
#
# WIRING:
# - S (Signal) -> GP16
# - + (VCC)    -> 3.3V
# - - (GND)    -> GND
# -----------------------------------------------------------------------------

import machine
import time

class HardwareConfig:
    PIN_RELAY = 16
    CYCLE_TIME_SEC = 2.0

def main():
    # 1. Setup Output
    relay_switch = machine.Pin(HardwareConfig.PIN_RELAY, machine.Pin.OUT)
    
    print("--- SYSTEM READY: HIGH POWER RELAY ---")
    print("Listen for the click...")
    
    while True:
        # A. Turn ON
        print(">>> RELAY CLOSED (ON)")
        relay_switch.value(1)
        time.sleep(HardwareConfig.CYCLE_TIME_SEC)
        
        # B. Turn OFF
        print("<<< RELAY OPEN   (OFF)")
        relay_switch.value(0)
        time.sleep(HardwareConfig.CYCLE_TIME_SEC)

if __name__ == "__main__":
    main()
