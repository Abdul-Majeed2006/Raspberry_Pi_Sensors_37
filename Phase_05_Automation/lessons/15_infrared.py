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
# 1. Transmitter: S -> GP20, - -> GND
# 2. Receiver:    S -> GP21, + -> 3.3V, - -> GND
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Transmitter (The "Light Bulb") ---
# We use PWM to create that super-fast 38,000Hz flicker.
transmitter = machine.PWM(machine.Pin(20))
transmitter.freq(38000)
transmitter.duty_u16(32768) # 50% duty cycle

# --- Setup Receiver (The "Eye") ---
# The IR Receiver is "Active Low." 
# - Seeing Light = 0
# - Light Blocked = 1
receiver = machine.Pin(21, machine.Pin.IN)

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
