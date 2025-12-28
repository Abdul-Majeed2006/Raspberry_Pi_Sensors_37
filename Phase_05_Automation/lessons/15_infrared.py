# -----------------------------------------------------------------------------
# Lesson 15: Invisible Tripwire (Infrared Beam)
# -----------------------------------------------------------------------------
# Modules: KY-005 IR Transmitter / KY-022 IR Receiver
# Goal: Build an invisible security beam that triggers when someone walks through.
#
# WHY THIS MATTERS:
# This is how your TV remote works, and how automatic garage doors know if 
# a car (or a cat) is in the way before they close. It's a "Wireless Wire."
#
# HOW IT WORKS (The 38kHz Secret):
# The sun emits IR light too. To stop the sun from scale-triggering our 
# alarm, the receiver ONLY looks for light flashing at exactly 38,000Hz 
# (38,000 times per second). This is called "Modulation."
#
# WIRING:
# 1. Transmitter: S -> GP17, - -> GND
# 2. Receiver:    S -> GP16, + -> 3.3V, - -> GND
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Transmitter (The "Light Bulb") ---
# We use GP17 for the transmitter.
transmitter = machine.PWM(machine.Pin(17))
transmitter.freq(38000)
transmitter.duty_u16(32768) # 50% duty cycle

# --- Setup Receiver (The "Eye") ---
# We use GP16 (Pin 21) right next to it for the receiver 'Eye'.
receiver = machine.Pin(16, machine.Pin.IN)

led = machine.Pin("LED", machine.Pin.OUT)

print("Security System Online. Try to block the invisible beam!")

while True:
    # Read the eye
    beam_broken = receiver.value()
    
    if beam_broken == 1:
        # If the beam is broken, the 'Eye' goes High (1)
        print(">>> ALERT: INTRUDER DETECTED <<<")
        led.value(1) 
    else:
        # Beam is solid, everything is fine.
        led.value(0)
        
    time.sleep(0.1) # Check 10 times per second
