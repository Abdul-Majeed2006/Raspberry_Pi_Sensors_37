# -----------------------------------------------------------------------------
# Lesson 15: Invisible Tripwire (IR Break-Beam)
# -----------------------------------------------------------------------------
# Modules: KY-005 IR LED (TX) / KY-022 IR Receiver (RX)
# Goal: Create an active security beam.
#
# ANATOMY:
# - TX: Flashes IR light at 38,000 Hz (38kHz).
# - RX: Specific sensor that ONLY sees 38kHz light (ignores the sun).
#
# WIRING:
# 1. Transmitter (TX): S -> GP17 | - -> GND
# 2. Receiver (RX):    S -> GP16 | + -> 3.3V | - -> GND
# -----------------------------------------------------------------------------

import machine
import time

class HardwareConfig:
    PIN_TX_LED = 17
    PIN_RX_EYE = 16
    PIN_ALARM  = "LED"
    CARRIER_FREQ = 38000 # 38kHz Standard for IR

def main():
    # 1. Setup Transmitter (Always ON)
    tx = machine.PWM(machine.Pin(HardwareConfig.PIN_TX_LED))
    tx.freq(HardwareConfig.CARRIER_FREQ)
    tx.duty_u16(32768) # 50% Duty Cycle (Perfect Square Wave)
    
    # 2. Setup Receiver
    rx = machine.Pin(HardwareConfig.PIN_RX_EYE, machine.Pin.IN)
    
    # 3. Setup Alarm
    alarm = machine.Pin(HardwareConfig.PIN_ALARM, machine.Pin.OUT)
    
    print("--- SYSTEM READY: SECURITY BEAM ---")
    print("Break the beam to trigger alarm...")
    
    while True:
        # RX Logic: 0 = Seeing 38kHz Signal (Beam Intact)
        #           1 = Signal Lost (Beam Broken)
        is_beam_broken = (rx.value() == 1)
        
        if is_beam_broken:
            print("!!! BREACH DETECTED !!!")
            alarm.value(1)
        else:
            alarm.value(0)
            
        time.sleep(0.1)

if __name__ == "__main__":
    main()
