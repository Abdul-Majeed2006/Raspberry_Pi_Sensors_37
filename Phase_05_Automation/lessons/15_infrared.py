# -----------------------------------------------------------------------------
# Lesson 15: Invisible Tripwire (Infrared)
# -----------------------------------------------------------------------------
# Modules: KY-005 IR Transmitter / KY-022 IR Receiver
# Goal: Create a secret security beam.
#       IR Receivers (VS1838B) are designed to see flashing light (38kHz),
#       NOT constant light. This prevents sunlight from triggering them.
#
# WIRING:
# 1. IR Transmitter (IR LED):
#    - S (Signal) -> GP14
#
# 2. IR Receiver (Black module with metal cage or bump):
#    - S (Signal) -> GP16
#    - + (Power)  -> 3.3V
#    - - (GND)    -> GND
#
# Skills Learnt:
# - Signal Modulation (38kHz)
# - PWM Frequency Generation
# - Receiver Demodulation
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Transmitter (The Gun) ---
# We must flash it 38,000 times a second (38kHz) for the receiver to see it.
transmitter = machine.PWM(machine.Pin(14))
transmitter.freq(38000)
transmitter.duty_u16(32768) # 50% Power

# --- Setup Receiver (The Target) ---
# It goes LOW (0) when it sees the 38kHz signal.
# It goes HIGH (1) when the beam is broken.
receiver = machine.Pin(16, machine.Pin.IN)

led = machine.Pin("LED", machine.Pin.OUT)

print("Beam Active. Don't cross the line!")

while True:
    # 0 = Safe (Seeing Signal)
    # 1 = BROKEN (Blocked Signal)
    status = receiver.value()
    
    if status == 1:
        print("ALARM! BEAM BROKEN!")
        led.value(1) # Flash LED
    else:
        led.value(0)
        
    time.sleep(0.1)
